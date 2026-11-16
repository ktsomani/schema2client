"""Sync client. HTTP is delegated to ``postgrest``."""

from __future__ import annotations

from typing import Literal, overload

import httpx
from postgrest import SyncPostgrestClient

from .query_builder import (
    PostsQueryBuilder,
    UsersQueryBuilder,
    _Queryable,
)


class _SyncTransport:
    def __init__(self, session: SyncPostgrestClient) -> None:
        self._session = session

    def fetch_rows(self, table: str, builder: _Queryable) -> list[object]:
        query = self._session.from_(table).select(builder._select.query())
        for column, op, value in builder._filters:
            if op == "in":
                query = query.filter(column, op, f"({value})")
            else:
                query = query.filter(column, op, value)
        response = query.execute()
        rows: list[object] = []
        for item in response.data:
            rows.append(item)
        return rows


class Client:
    """Typed PostgREST client for this schema.

    Construct with the project REST URL and the anon (public) key. Table access
    is ``table("name")`` or the generated ``users()`` / ``posts()`` shortcuts.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        client: httpx.Client | None = None,
    ) -> None:
        headers = {
            "apikey": api_key,
            "Authorization": f"Bearer {api_key}",
        }
        self._http = client or httpx.Client(headers=headers)
        self._session = SyncPostgrestClient(
            base_url,
            headers=headers,
            http_client=self._http,
        )
        self._transport = _SyncTransport(self._session)

    def close(self) -> None:
        self._session.aclose()

    @overload
    def table(self, name: Literal["posts"]) -> PostsQueryBuilder: ...
    @overload
    def table(self, name: Literal["users"]) -> UsersQueryBuilder: ...
    def table(self, name: str) -> object:
        if name == "posts":
            return self.posts()
        if name == "users":
            return self.users()
        msg = f"unknown table {name!r}"
        raise ValueError(msg)

    def posts(self) -> PostsQueryBuilder:
        builder = PostsQueryBuilder()
        builder._sync_transport = self._transport
        return builder

    def users(self) -> UsersQueryBuilder:
        builder = UsersQueryBuilder()
        builder._sync_transport = self._transport
        return builder
