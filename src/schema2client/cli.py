"""``schema2client`` command-line interface."""

from __future__ import annotations

from pathlib import Path

import click

from schema2client.emitter import compute_schema_hash, emit_package
from schema2client.parser import parse_spec_file


@click.group()
def main() -> None:
    """Generate a typed PostgREST client package from an OpenAPI schema."""


@main.command("generate")
@click.option(
    "--spec",
    required=True,
    type=click.Path(path_type=Path, dir_okay=False, exists=True),
    help="Path to a PostgREST OpenAPI JSON document.",
)
@click.option(
    "--out",
    required=True,
    type=click.Path(path_type=Path, file_okay=False),
    help="Directory to write the generated package into.",
)
@click.option(
    "--package",
    required=True,
    type=str,
    help="Import name of the generated package (for example mydb).",
)
@click.option(
    "--strict-insert",
    is_flag=True,
    default=False,
    help="Keep OpenAPI required columns required on Insert models even when a default is present.",
)
def generate(spec: Path, out: Path, package: str, strict_insert: bool) -> None:
    """Write models, query builders, and Client / AsyncClient for a schema file."""
    spec_bytes = spec.read_bytes()
    schema_hash = compute_schema_hash(spec_bytes)
    ir = parse_spec_file(spec)
    emit_package(ir, out, package, schema_hash, strict_insert=strict_insert)


if __name__ == "__main__":
    main()
