#!/usr/bin/env python3
"""Minimal demo: builder API without network (imports committed fixture)."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_GENERATED = _ROOT / "fixtures" / "generated"
if str(_GENERATED) not in sys.path:
    sys.path.insert(0, str(_GENERATED))

from mydb.client_sync import MydbSyncClient
from mydb.query_builder import UsersQueryBuilder


def main() -> None:
    client = MydbSyncClient("https://example.supabase.co/rest/v1", "anon-key-example")
    qb = client.users().eq("email", "user@example.com")
    select_executor = qb.select("id")
    print("table:", UsersQueryBuilder._table_name)
    print("select column:", qb._select)
    print("filters:", qb._filters)
    print("executor:", type(select_executor).__name__)
    print("Static check: tests/typing/narrowing.py (mypy reveal_type).")


if __name__ == "__main__":
    main()
