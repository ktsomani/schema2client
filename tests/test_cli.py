from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from schema2client.emitter import compute_schema_hash, render_client_async, render_client_sync
from schema2client.parser import parse_spec_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "sample_spec.json"
PACKAGE_DIR = ROOT / "fixtures" / "generated" / "mydb"


def test_schema_hash_in_generated_init() -> None:
    expected = compute_schema_hash(FIXTURE.read_bytes())
    init_source = (PACKAGE_DIR / "__init__.py").read_text(encoding="utf-8")
    assert f'SCHEMA_HASH = "{expected}"' in init_source


def test_cli_generate_matches_fixture(tmp_path: Path) -> None:
    out = tmp_path / "generated"
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "schema2client.cli",
            "generate",
            "--spec",
            str(FIXTURE),
            "--out",
            str(out),
            "--package",
            "mydb",
        ],
        capture_output=True,
        text=True,
        check=False,
        cwd=ROOT,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    for name in (
        "models.py",
        "query_builder.py",
        "client_sync.py",
        "client_async.py",
        "__init__.py",
        "py.typed",
    ):
        generated = (out / "mydb" / name).read_text(encoding="utf-8")
        committed = (PACKAGE_DIR / name).read_text(encoding="utf-8")
        assert generated == committed, name


def test_client_templates_match_committed() -> None:
    ir = parse_spec_file(FIXTURE)
    assert render_client_sync(ir, "mydb") == (PACKAGE_DIR / "client_sync.py").read_text(
        encoding="utf-8"
    )
    assert render_client_async(ir, "mydb") == (PACKAGE_DIR / "client_async.py").read_text(
        encoding="utf-8"
    )
