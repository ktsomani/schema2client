"""Sync client. HTTP is delegated to ``postgrest``."""

from __future__ import annotations

from typing import Literal, overload

import httpx
from postgrest import (
    SyncPostgrestClient,
    SyncSelectRequestBuilder,
    SyncSingleRequestBuilder,
)

from .query_builder import (
    PostsQueryBuilder,
    UsersQueryBuilder,
    _Queryable,
)


class _SyncTransport:
    def __init__(self, session: SyncPostgrestClient) -> None:
        self._session = session

    def _build(
        self, table: str, builder: _Queryable
    ) -> SyncSelectRequestBuilder | SyncSingleRequestBuilder:
        request = self._session.from_(table)
        mutation = builder._mutation
        query: SyncSelectRequestBuilder
        if mutation is None:
            query = request.select(builder._select.query())
        elif mutation[0] == "insert":
            query = request.insert(mutation[1])
        elif mutation[0] == "update":
            query = request.update(mutation[1])
        elif mutation[0] == "upsert":
            query = request.upsert(mutation[1], on_conflict=builder._on_conflict)
        elif mutation[0] == "delete":
            query = request.delete()
        else:
            msg = f"unknown operation {mutation[0]!r}"
            raise ValueError(msg)
        for column, op, value in builder._filters:
            if op == "in":
                query = query.filter(column, op, f"({value})")
            else:
                query = query.filter(column, op, value)
        for column, desc in builder._order:
            query = query.order(column, desc=desc)
        if builder._limit is not None:
            query = query.limit(builder._limit)
        if builder._offset is not None:
            query = query.offset(builder._offset)
        if builder._range is not None:
            start, end = builder._range
            query = query.range(start, end)
        if builder._single:
            return query.single()
        return query

    def fetch(self, table: str, builder: _Queryable) -> object:
        query = self._build(table, builder)
        response = query.execute()
        return response.data


class Client:
    """Typed PostgREST client for this schema.

    ``api_key`` is the anon (public) key sent as ``apikey``. ``access_token`` is
    the user JWT sent as ``Authorization``. When ``access_token`` is omitted,
    the anon key is also used as the bearer token (public RLS).
    """

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        access_token: str | None = None,
        client: httpx.Client | None = None,
    ) -> None:
        bearer = api_key if access_token is None else access_token
        headers = {
            "apikey": api_key,
            "Authorization": f"Bearer {bearer}",
        }
        self._owns_http = client is None
        self._http = client or httpx.Client(headers=headers)
        self._session = SyncPostgrestClient(
            base_url,
            headers=headers,
            http_client=self._http,
        )
        self._transport = _SyncTransport(self._session)

    def close(self) -> None:
        self._session.aclose()
        if self._owns_http and not self._http.is_closed:
            self._http.close()

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
