"""Map PostgREST OpenAPI column metadata to Python type source strings."""

from __future__ import annotations

from schema2client.ir import ArrayItem, Column


def _format_base(format_name: str | None) -> str | None:
    if format_name is None:
        return None
    lowered = format_name.lower()
    # PostgREST uses verbose timestamp labels in the format field.
    if "timestamp with time zone" in lowered or lowered in {
        "timestamptz",
        "timestamp with time zone",
    }:
        return "timestamptz"
    if "timestamp without time zone" in lowered or lowered in {
        "timestamp",
        "timestamp without time zone",
    }:
        return "timestamp"
    if lowered.startswith("time without time zone") or lowered == "time":
        return "time"
    if lowered.startswith("time with time zone") or lowered == "timetz":
        return "timetz"
    # integer-family aliases
    if lowered in {"int2", "smallint", "int4", "integer", "int8", "bigint"}:
        return "int"
    if lowered in {"numeric", "decimal"}:
        return "decimal"
    if lowered in {"float4", "real", "float8", "double precision"}:
        return "float"
    if lowered in {"text", "varchar", "character varying", "char", "character", "bpchar"}:
        return "text"
    if lowered in {"bool", "boolean"}:
        return "bool"
    if lowered == "uuid":
        return "uuid"
    if lowered == "date":
        return "date"
    if lowered in {"json", "jsonb"}:
        return "json"
    if lowered == "bytea":
        return "bytea"
    return lowered


def _literal_enum(values: tuple[str, ...]) -> str:
    parts = ", ".join(repr(value) for value in values)
    return f"Literal[{parts}]"


def _map_array_item(item: ArrayItem) -> str:
    inner = _map_openapi(item.openapi_type, item.format, item.enum, for_write=False)
    return f"list[{inner}]"


def _map_openapi(
    openapi_type: str,
    format_name: str | None,
    enum: tuple[str, ...],
    *,
    for_write: bool,
) -> str:
    if enum and openapi_type == "string":
        if for_write:
            return "str"  # Caller emits a dedicated StrEnum; scalar field type is str
        return _literal_enum(enum)

    if openapi_type == "array":
        msg = "array columns must carry array_item on Column"
        raise TypeError(msg)

    base_key = _format_base(format_name)
    if base_key is None and openapi_type == "integer":
        base_key = "int"
    if base_key is None and openapi_type == "number":
        base_key = "float"
    if base_key is None and openapi_type == "boolean":
        base_key = "bool"
    if base_key is None and openapi_type == "string":
        base_key = "text"
    if (
        base_key is None
        and openapi_type == "object"
        and format_name
        and format_name.lower() in {"json", "jsonb"}
    ):
        base_key = "json"

    mapping: dict[str, str] = {
        "int": "int",
        "decimal": "decimal.Decimal",
        "float": "float",
        "text": "str",
        "bool": "bool",
        "uuid": "uuid.UUID",
        "date": "datetime.date",
        "time": "datetime.time",
        "timetz": "datetime.time",
        "timestamp": "datetime.datetime",
        "timestamptz": "datetime.datetime",
        "json": "dict[str, object]",
        "bytea": "bytes",
    }

    if base_key is None:
        msg = f"unsupported OpenAPI type/format: {openapi_type!r} / {format_name!r}"
        raise TypeError(msg)

    if base_key not in mapping:
        if enum:
            return _literal_enum(enum) if not for_write else "str"
        msg = f"unsupported format: {format_name!r}"
        raise TypeError(msg)

    return mapping[base_key]


def py_type(column: Column, *, for_write: bool = False) -> str:
    """Return a Python type expression as source text for templates.

      Read paths (``for_write=False``) use ``Literal[...]`` for Postgres enums.
    Write paths use ``str`` for enum-backed columns because the field type on
      Pydantic models is the generated ``StrEnum`` member type in the emitter.
    """
    if column.openapi_type == "array":
        if column.array_item is None:
            msg = f"column {column.name!r} is array but has no array_item"
            raise TypeError(msg)
        inner = _map_array_item(column.array_item)
        if column.nullable:
            return f"{inner} | None"
        return inner

    inner = _map_openapi(column.openapi_type, column.format, column.enum, for_write=for_write)
    if column.nullable:
        return f"{inner} | None"
    return inner


def enum_str_enum_name(table_name: str, column: Column) -> str:
    """Stable generated name for a Postgres enum ``StrEnum`` on write models."""
    stem = column.format or column.name
    stem = stem.replace(".", "_").replace("-", "_")
    return f"{_pascal_case(table_name)}_{_pascal_case(stem)}Enum"


def _pascal_case(name: str) -> str:
    parts = [piece for piece in name.replace("-", "_").split("_") if piece]
    return "".join(piece[:1].upper() + piece[1:] for piece in parts)
