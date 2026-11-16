"""Static typing checks for single-column select narrowing (mypy only)."""

from __future__ import annotations

from typing import reveal_type

from mydb.query_builder import UsersQueryBuilder


def narrowed_select_id() -> None:
    qb = UsersQueryBuilder()
    reveal_type(qb.select("id").execute())


def narrowed_select_star() -> None:
    qb = UsersQueryBuilder()
    reveal_type(qb.select("*").execute())
