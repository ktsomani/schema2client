"""Parse a PostgREST OpenAPI document into :class:`SchemaIR`."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from schema2client.ir import ArrayItem, Column, SchemaIR, Table


def load_spec_bytes(data: bytes) -> dict[str, object]:
    raw = json.loads(data)
    if not isinstance(raw, dict):
        msg = "OpenAPI document root must be a JSON object"
        raise TypeError(msg)
    return cast(dict[str, object], raw)


def load_spec_file(path: Path) -> dict[str, object]:
    return load_spec_bytes(path.read_bytes())


def parse_spec(spec: dict[str, object]) -> SchemaIR:
    """Parse definitions and paths into tables and columns."""
    definitions = _definitions(spec)
    table_names = _table_names_from_paths(spec)
    tables: list[Table] = []
    for name in sorted(table_names):
        if name not in definitions:
            continue
        table_def = definitions[name]
        if not isinstance(table_def, dict):
            continue
        columns = _columns_from_definition(table_def)
        if not columns:
            continue
        tables.append(Table(name=name, columns=tuple(columns)))
    return SchemaIR(tables=tuple(tables))


def parse_spec_file(path: Path) -> SchemaIR:
    return parse_spec(load_spec_file(path))


def _definitions(spec: dict[str, object]) -> dict[str, object]:
    defs = spec.get("definitions")
    if isinstance(defs, dict):
        return cast(dict[str, object], defs)
    components = spec.get("components")
    if isinstance(components, dict):
        schemas = components.get("schemas")
        if isinstance(schemas, dict):
            return cast(dict[str, object], schemas)
    return {}


def _table_names_from_paths(spec: dict[str, object]) -> set[str]:
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        return set()
    names: set[str] = set()
    for raw_path in paths:
        if not isinstance(raw_path, str):
            continue
        segment = raw_path.strip("/").split("/")[-1]
        if segment:
            names.add(segment)
    return names


def _columns_from_definition(table_def: dict[str, object]) -> list[Column]:
    properties = table_def.get("properties")
    if not isinstance(properties, dict):
        return []
    required_raw = table_def.get("required")
    required: set[str] = set()
    if isinstance(required_raw, list):
        required = {item for item in required_raw if isinstance(item, str)}

    columns: list[Column] = []
    for col_name in sorted(properties):
        if not isinstance(col_name, str):
            continue
        prop = properties[col_name]
        if not isinstance(prop, dict):
            continue
        col = _column_from_property(col_name, prop, nullable=col_name not in required)
        columns.append(col)
    return columns


def _column_from_property(name: str, prop: dict[str, object], *, nullable: bool) -> Column:
    openapi_type = prop.get("type")
    if not isinstance(openapi_type, str):
        openapi_type = "string"

    format_raw = prop.get("format")
    format_name = format_raw if isinstance(format_raw, str) else None

    enum_raw = prop.get("enum")
    enum: tuple[str, ...] = ()
    if isinstance(enum_raw, list):
        enum = tuple(item for item in enum_raw if isinstance(item, str))

    array_item: ArrayItem | None = None
    if openapi_type == "array":
        items = prop.get("items")
        if isinstance(items, dict):
            item_type = items.get("type")
            if not isinstance(item_type, str):
                item_type = "string"
            item_format = items.get("format")
            item_enum_raw = items.get("enum")
            item_enum: tuple[str, ...] = ()
            if isinstance(item_enum_raw, list):
                item_enum = tuple(item for item in item_enum_raw if isinstance(item, str))
            array_item = ArrayItem(
                openapi_type=item_type,
                format=item_format if isinstance(item_format, str) else None,
                enum=item_enum,
            )

    return Column(
        name=name,
        openapi_type=openapi_type,
        format=format_name,
        nullable=nullable,
        enum=enum,
        array_item=array_item,
    )
