"""Static typing checks for select narrowing (mypy only)."""

from __future__ import annotations

from typing import reveal_type

from mydb.query_builder import UsersQueryBuilder


def narrowed_select_id() -> None:
    qb = UsersQueryBuilder()
    reveal_type(qb.select("id").execute())


def narrowed_select_star() -> None:
    qb = UsersQueryBuilder()
    reveal_type(qb.select("*").execute())


def narrowed_select_two_columns() -> None:
    qb = UsersQueryBuilder()
    reveal_type(qb.select("id", "email").eq("is_active", True).execute())


def narrowed_select_reversed_pair() -> None:
    qb = UsersQueryBuilder()
    reveal_type(qb.select("email", "id").execute())
