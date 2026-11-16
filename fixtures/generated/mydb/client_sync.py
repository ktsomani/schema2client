"""Sync HTTP client for PostgREST."""

from __future__ import annotations

import httpx

from .query_builder import (
    PostsQueryBuilder,
    UsersQueryBuilder,
    _postgrest_params,
    _Queryable,
)


class _SyncTransport:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        client: httpx.Client,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._client = client

    def fetch_rows(self, table: str, builder: _Queryable) -> list[object]:
        url = f"{self._base_url}/{table}"
        response = self._client.get(url, params=_postgrest_params(builder))
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, list):
            return []
        items: list[object] = []
        for item in data:
            items.append(item)
        return items


class MydbSyncClient:
    """PostgREST sync client (generated)."""

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
        self._client = client or httpx.Client(
            base_url=base_url,
            headers=headers,
        )
        self._transport = _SyncTransport(
            base_url,
            api_key,
            self._client,
        )

    def posts(self) -> PostsQueryBuilder:
        builder = PostsQueryBuilder()
        builder._sync_transport = self._transport
        return builder

    def users(self) -> UsersQueryBuilder:
        builder = UsersQueryBuilder()
        builder._sync_transport = self._transport
        return builder
