"""Intermediate representation of a PostgREST-exposed database schema."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ArrayItem:
    """Element type for an OpenAPI ``array`` column."""

    openapi_type: str
    format: str | None
    enum: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Column:
    """One table column as described in the PostgREST OpenAPI ``definitions``."""

    name: str
    openapi_type: str
    format: str | None
    nullable: bool
    enum: tuple[str, ...] = ()
    array_item: ArrayItem | None = None


@dataclass(frozen=True, slots=True)
class Table:
    """A table or view exposed as a PostgREST resource."""

    name: str
    columns: tuple[Column, ...]


@dataclass(frozen=True, slots=True)
class SchemaIR:
    """Parsed schema ready for code generation."""

    tables: tuple[Table, ...]
