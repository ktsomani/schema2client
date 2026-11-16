"""Generate typed Python packages from PostgREST OpenAPI schemas."""

from schema2client.emitter import (
    compute_schema_hash,
    emit_models,
    emit_models_package,
    emit_package,
    emit_query_builder,
    render_models,
    render_query_builder,
)
from schema2client.ir import Column, SchemaIR, Table
from schema2client.parser import parse_spec, parse_spec_file
from schema2client.typemap import py_type

__all__ = [
    "Column",
    "SchemaIR",
    "Table",
    "compute_schema_hash",
    "emit_models",
    "emit_models_package",
    "emit_package",
    "emit_query_builder",
    "parse_spec",
    "parse_spec_file",
    "py_type",
    "render_models",
    "render_query_builder",
]
