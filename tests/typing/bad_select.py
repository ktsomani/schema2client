"""Typo column name must fail mypy (mypy only)."""

from __future__ import annotations

from mydb.query_builder import UsersQueryBuilder


def unknown_column() -> None:
    qb = UsersQueryBuilder()
    qb.select("idd").execute()
