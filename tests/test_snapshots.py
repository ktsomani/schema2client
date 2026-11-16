"""Snapshot tests for parser IR (canonical fixture)."""

from __future__ import annotations

from pathlib import Path

from syrupy.assertion import SnapshotAssertion

from schema2client.parser import parse_spec_file

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "sample_spec.json"


def test_parse_spec_snapshot(snapshot: SnapshotAssertion) -> None:
    ir = parse_spec_file(FIXTURE)
    tables = [
        {
            "name": table.name,
            "columns": [
                {
                    "name": column.name,
                    "format": column.format,
                    "nullable": column.nullable,
                    "enum": list(column.enum),
                }
                for column in table.columns
            ],
        }
        for table in ir.tables
    ]
    assert tables == snapshot
