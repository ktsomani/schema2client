from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MYPY = [
    sys.executable,
    "-m",
    "mypy",
    "--strict",
    "--show-error-codes",
    "--no-error-summary",
    "--config-file",
    str(ROOT / "pyproject.toml"),
]


def test_mypy_narrowing_reveal() -> None:
    target = ROOT / "tests" / "typing" / "narrowing.py"
    env = os.environ.copy()
    env["MYPYPATH"] = f"src{os.pathsep}fixtures{os.path.sep}generated"
    completed = subprocess.run(
        [*MYPY, str(target)],
        capture_output=True,
        text=True,
        check=False,
        cwd=ROOT,
        env=env,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    out = completed.stdout + completed.stderr
    assert "Users_id" in out
    assert "Users_email_id" in out
    assert "UsersRow" in out
    assert "list[dict" not in out


def test_mypy_unknown_column_errors() -> None:
    target = ROOT / "tests" / "typing" / "bad_select.py"
    env = os.environ.copy()
    env["MYPYPATH"] = f"src{os.pathsep}fixtures{os.path.sep}generated"
    completed = subprocess.run(
        [*MYPY, str(target)],
        capture_output=True,
        text=True,
        check=False,
        cwd=ROOT,
        env=env,
    )
    assert completed.returncode != 0
    out = completed.stdout + completed.stderr
    assert "idd" in out or "No overload variant" in out
