"""``schema2client`` command-line interface."""

from __future__ import annotations

from pathlib import Path

import click

from schema2client.emitter import compute_schema_hash, emit_package
from schema2client.parser import parse_spec_file


@click.group()
def main() -> None:
    """Generate typed Python packages from PostgREST OpenAPI schemas."""


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
    help="Output directory for the generated package tree.",
)
@click.option(
    "--package",
    required=True,
    type=str,
    help="Python package name for generated code (for example ``mydb``).",
)
def generate(spec: Path, out: Path, package: str) -> None:
    """Emit models, query builders, and HTTP clients from a schema file."""
    spec_bytes = spec.read_bytes()
    schema_hash = compute_schema_hash(spec_bytes)
    ir = parse_spec_file(spec)
    emit_package(ir, out, package, schema_hash)


if __name__ == "__main__":
    main()
