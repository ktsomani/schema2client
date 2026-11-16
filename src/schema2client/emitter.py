"""Render generated Python packages from :class:`SchemaIR`."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import jinja2

from schema2client.ir import Column, SchemaIR, Table
from schema2client.typemap import enum_str_enum_name, py_type

_TEMPLATES_ROOT = Path(__file__).resolve().parent / "templates"


@dataclass(frozen=True, slots=True)
class EnumDef:
    name: str
    values: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ModelColumn:
    name: str
    read_type: str
    write_required_type: str
    write_optional_type: str
    filter_type: str
    nullable: bool
    has_enum: bool


@dataclass(frozen=True, slots=True)
class TableModels:
    table_name: str
    prefix: str
    row_class: str
    insert_class: str
    update_class: str
    columns: tuple[ModelColumn, ...]
    enums: tuple[EnumDef, ...]


def _pascal_case(name: str) -> str:
    parts = [piece for piece in name.replace("-", "_").split("_") if piece]
    return "".join(piece[:1].upper() + piece[1:] for piece in parts)


def _python_identifier(name: str) -> bool:
    return name.isidentifier()


def _filter_value_type(read_type: str) -> str:
    if read_type.endswith(" | None"):
        return read_type[: -len(" | None")]
    return read_type


def _write_inner_type(column: Column, table: Table) -> str:
    if column.enum:
        return enum_str_enum_name(table.name, column)
    inner = py_type(column, for_write=True)
    if inner.endswith(" | None"):
        return inner[: -len(" | None")]
    return inner


def _table_models(table: Table) -> TableModels:
    prefix = _pascal_case(table.name)
    enums: dict[str, EnumDef] = {}
    columns: list[ModelColumn] = []

    for column in table.columns:
        if column.enum:
            enum_name = enum_str_enum_name(table.name, column)
            enums[enum_name] = EnumDef(name=enum_name, values=column.enum)

        inner = _write_inner_type(column, table)

        read_type = py_type(column, for_write=False)
        columns.append(
            ModelColumn(
                name=column.name,
                read_type=read_type,
                write_required_type=inner,
                write_optional_type=f"{inner} | None",
                filter_type=_filter_value_type(read_type),
                nullable=column.nullable,
                has_enum=bool(column.enum),
            )
        )

    return TableModels(
        table_name=table.name,
        prefix=prefix,
        row_class=f"{prefix}Row",
        insert_class=f"{prefix}Insert",
        update_class=f"{prefix}Update",
        columns=tuple(columns),
        enums=tuple(sorted(enums.values(), key=lambda item: item.name)),
    )


def _collect_imports(tables: tuple[TableModels, ...]) -> tuple[list[str], list[str]]:
    typing_names: set[str] = set()
    stdlib_modules: set[str] = set()

    def note_type(type_src: str) -> None:
        if "Literal" in type_src:
            typing_names.add("Literal")
        if "decimal.Decimal" in type_src:
            stdlib_modules.add("decimal")
        if "datetime." in type_src:
            stdlib_modules.add("datetime")
        if "uuid.UUID" in type_src:
            stdlib_modules.add("uuid")

    for table in tables:
        if table.enums:
            stdlib_modules.add("enum")
        for column in table.columns:
            note_type(column.read_type)
            note_type(column.write_required_type)
            note_type(column.write_optional_type)

    stdlib_sorted = sorted(stdlib_modules)
    typing_sorted = sorted(typing_names)
    return stdlib_sorted, typing_sorted


def _jinja_env() -> jinja2.Environment:
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(_TEMPLATES_ROOT)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )


def _format_python(source: str, *, filename: str = "models.py") -> str:
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=".py",
        delete=False,
    ) as handle:
        handle.write(source)
        temp_path = Path(handle.name)
    try:
        subprocess.run(
            [sys.executable, "-m", "ruff", "format", str(temp_path)],
            check=False,
        )
        subprocess.run(
            [sys.executable, "-m", "ruff", "check", "--fix", str(temp_path)],
            check=False,
        )
        subprocess.run(
            [sys.executable, "-m", "ruff", "format", str(temp_path)],
            check=False,
        )
        return temp_path.read_text(encoding="utf-8")
    finally:
        temp_path.unlink(missing_ok=True)


def _render_models(ir: SchemaIR) -> str:
    tables = tuple(_table_models(table) for table in ir.tables)
    stdlib_imports, typing_imports = _collect_imports(tables)

    env = _jinja_env()
    template = env.get_template("models.py.j2")
    rendered = template.render(
        tables=tables,
        stdlib_imports=stdlib_imports,
        typing_imports=typing_imports,
        col_td_name=lambda prefix, col: f"{prefix}_{col}",
        py_ident=_python_identifier,
    )
    return _format_python(rendered)


def render_models(ir: SchemaIR) -> str:
    """Render ``models.py`` source for ``ir``."""
    return _render_models(ir)


def _render_query_builder(ir: SchemaIR) -> str:
    tables = tuple(_table_models(table) for table in ir.tables)
    stdlib_imports: set[str] = set()
    for table in tables:
        for column in table.columns:
            for type_src in (column.filter_type, column.read_type):
                if "decimal.Decimal" in type_src:
                    stdlib_imports.add("decimal")
                if "datetime." in type_src:
                    stdlib_imports.add("datetime")
                if "uuid.UUID" in type_src:
                    stdlib_imports.add("uuid")
    template = _jinja_env().get_template("query_builder.py.j2")
    rendered = template.render(
        tables=tables,
        col_td_name=lambda prefix, col: f"{prefix}_{col}",
        stdlib_imports=sorted(stdlib_imports),
    )
    return _format_python(rendered, filename="query_builder.py")


def render_query_builder(ir: SchemaIR) -> str:
    """Render ``query_builder.py`` source for ``ir``."""
    return _render_query_builder(ir)


def emit_query_builder(ir: SchemaIR, package_dir: Path) -> None:
    package_dir.mkdir(parents=True, exist_ok=True)
    content = render_query_builder(ir)
    (package_dir / "query_builder.py").write_text(content, encoding="utf-8", newline="\n")


def emit_models(ir: SchemaIR, package_dir: Path) -> None:
    """Write ``models.py`` into ``package_dir``."""
    package_dir.mkdir(parents=True, exist_ok=True)
    content = render_models(ir)
    (package_dir / "models.py").write_text(content, encoding="utf-8", newline="\n")


def compute_schema_hash(spec_bytes: bytes) -> str:
    """Stable SHA-256 hex digest of the input OpenAPI document bytes."""
    return hashlib.sha256(spec_bytes).hexdigest()


def _package_pascal(package_name: str) -> str:
    return _pascal_case(package_name)


def _render_client(ir: SchemaIR, package_name: str, *, async_mode: bool) -> str:
    tables = tuple(_table_models(table) for table in ir.tables)
    package_pascal = _package_pascal(package_name)
    template = _jinja_env().get_template("client.py.j2")
    rendered = template.render(
        tables=tables,
        async_mode=async_mode,
        client_class=f"{package_pascal}{'Async' if async_mode else 'Sync'}Client",
    )
    filename = "client_async.py" if async_mode else "client_sync.py"
    return _format_python(rendered, filename=filename)


def render_client_sync(ir: SchemaIR, package_name: str) -> str:
    return _render_client(ir, package_name, async_mode=False)


def render_client_async(ir: SchemaIR, package_name: str) -> str:
    return _render_client(ir, package_name, async_mode=True)


def _render_init(package_name: str, schema_hash: str) -> str:
    package_pascal = _package_pascal(package_name)
    template = _jinja_env().get_template("__init__.py.j2")
    rendered = template.render(
        package_name=package_name,
        package_pascal=package_pascal,
        schema_hash=schema_hash,
    )
    return _format_python(rendered, filename="__init__.py")


def emit_package(ir: SchemaIR, out_dir: Path, package_name: str, schema_hash: str) -> None:
    """Write the full generated package (models, query builders, clients, ``SCHEMA_HASH``)."""
    package_dir = out_dir / package_name
    package_dir.mkdir(parents=True, exist_ok=True)
    emit_models(ir, package_dir)
    emit_query_builder(ir, package_dir)
    (package_dir / "client_sync.py").write_text(
        render_client_sync(ir, package_name),
        encoding="utf-8",
        newline="\n",
    )
    (package_dir / "client_async.py").write_text(
        render_client_async(ir, package_name),
        encoding="utf-8",
        newline="\n",
    )
    (package_dir / "__init__.py").write_text(
        _render_init(package_name, schema_hash),
        encoding="utf-8",
        newline="\n",
    )


def emit_models_package(ir: SchemaIR, out_dir: Path, package_name: str) -> None:
    """Backward-compatible alias: emits package without ``SCHEMA_HASH`` refresh."""
    package_dir = out_dir / package_name
    init_path = package_dir / "__init__.py"
    existing_hash = ""
    if init_path.exists():
        for line in init_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("SCHEMA_HASH = "):
                existing_hash = line.split("=", maxsplit=1)[1].strip().strip('"')
                break
    emit_package(ir, out_dir, package_name, existing_hash or "0" * 64)
