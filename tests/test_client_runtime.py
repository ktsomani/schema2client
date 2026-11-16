"""Runtime checks for the generated client. HTTP is mocked."""

from __future__ import annotations

import asyncio
import importlib
import sys
from pathlib import Path
from types import ModuleType

import pytest

from schema2client.emitter import render_models
from schema2client.parser import parse_spec_file

ROOT = Path(__file__).resolve().parents[1]


def _generated() -> tuple[ModuleType, ModuleType, ModuleType, ModuleType]:
    generated = str(ROOT / "fixtures" / "generated")
    if generated not in sys.path:
        sys.path.insert(0, generated)
    client_sync = importlib.import_module("mydb.client_sync")
    client_async = importlib.import_module("mydb.client_async")
    query_builder = importlib.import_module("mydb.query_builder")
    models = importlib.import_module("mydb.models")
    return client_sync, client_async, query_builder, models


class _Response:
    def __init__(self, data: object) -> None:
        self.data = data


_FULL_USER: dict[str, object] = {
    "avatar": None,
    "created_at": "2020-01-01T00:00:00Z",
    "display_name": None,
    "email": "a@b.c",
    "id": 1,
    "is_active": True,
    "kind": None,
    "metadata": None,
    "score": None,
    "tags": None,
}


class _Query:
    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []
        self.data: object = [{"id": 1, "email": "a@b.c"}]

    def select(self, *args: object) -> _Query:
        self.calls.append(("select", args))
        return self

    def insert(self, payload: object, *args: object, **kwargs: object) -> _Query:
        del args, kwargs
        self.calls.append(("insert", (payload,)))
        self.data = [_FULL_USER]
        return self

    def update(self, payload: object, *args: object, **kwargs: object) -> _Query:
        del args, kwargs
        self.calls.append(("update", (payload,)))
        self.data = [_FULL_USER]
        return self

    def upsert(self, payload: object, *args: object, **kwargs: object) -> _Query:
        self.calls.append(("upsert", (payload, kwargs.get("on_conflict", ""))))
        self.data = [_FULL_USER]
        return self

    def delete(self, *args: object, **kwargs: object) -> _Query:
        del args, kwargs
        self.calls.append(("delete", ()))
        self.data = [_FULL_USER]
        return self

    def filter(self, *args: object) -> _Query:
        self.calls.append(("filter", args))
        return self

    def order(self, *args: object, **kwargs: object) -> _Query:
        self.calls.append(("order", (*args, kwargs.get("desc"))))
        return self

    def limit(self, size: int) -> _Query:
        self.calls.append(("limit", (size,)))
        return self

    def offset(self, size: int) -> _Query:
        self.calls.append(("offset", (size,)))
        return self

    def range(self, start: int, end: int) -> _Query:
        self.calls.append(("range", (start, end)))
        return self

    def single(self) -> _Query:
        self.calls.append(("single", ()))
        self.data = {"id": 1, "email": "a@b.c"}
        return self

    def execute(self) -> _Response:
        return _Response(self.data)


class _Session:
    def __init__(self, base_url: str, *, headers: dict[str, str], http_client: object) -> None:
        self.base_url = base_url
        self.headers = headers
        self.http_client = http_client
        self.query = _Query()
        self.closed = False

    def from_(self, table: str) -> _Query:
        self.query.calls.append(("from", (table,)))
        return self.query

    def aclose(self) -> None:
        self.closed = True


def _install_session(monkeypatch: pytest.MonkeyPatch, module: ModuleType) -> list[_Session]:
    sessions: list[_Session] = []

    def factory(base_url: str, *, headers: dict[str, str], http_client: object) -> _Session:
        session = _Session(base_url, headers=headers, http_client=http_client)
        sessions.append(session)
        return session

    monkeypatch.setattr(module, "SyncPostgrestClient", factory)
    return sessions


def test_posts_query_class_exists() -> None:
    _, _, query_builder, _ = _generated()
    assert query_builder.PostsQuery.__name__ == "PostsQuery"


def test_select_rejects_more_than_three_columns() -> None:
    _, _, query_builder, _ = _generated()
    builder = query_builder.UsersQueryBuilder()
    with pytest.raises(ValueError, match="1 to 3"):
        builder.select("id", "email", "kind", "score")


def test_close_closes_owned_http_client() -> None:
    client_sync, _, _, _ = _generated()
    client = client_sync.Client("https://example.supabase.co/rest/v1", "anon-key")
    http = client._http
    client.close()
    assert http.is_closed


def test_async_aclose_closes_owned_http_client() -> None:
    _, client_async, _, _ = _generated()

    async def run() -> None:
        client = client_async.AsyncClient("https://example.supabase.co/rest/v1", "anon-key")
        http = client._http
        await client.aclose()
        assert http.is_closed

    asyncio.run(run())


def test_access_token_is_separate_from_apikey(monkeypatch: pytest.MonkeyPatch) -> None:
    client_sync, _, _, _ = _generated()
    sessions = _install_session(monkeypatch, client_sync)
    client = client_sync.Client(
        "https://example.supabase.co/rest/v1",
        "anon-key",
        access_token="user-jwt",
    )
    assert sessions[0].headers["apikey"] == "anon-key"
    assert sessions[0].headers["Authorization"] == "Bearer user-jwt"
    client.close()


def test_insert_update_and_select_hit_postgrest(monkeypatch: pytest.MonkeyPatch) -> None:
    client_sync, _, _, models = _generated()
    sessions = _install_session(monkeypatch, client_sync)
    client = client_sync.Client("https://example.supabase.co/rest/v1", "anon-key")
    rows = (
        client.table("users")
        .select("id", "email")
        .eq("email", "a@b.c")
        .order("id", desc=True)
        .limit(2)
        .offset(1)
        .execute()
    )
    assert rows[0]["id"] == 1
    calls = sessions[0].query.calls
    assert ("from", ("users",)) in calls
    assert ("select", ("id,email",)) in calls
    assert ("filter", ("email", "eq", "a@b.c")) in calls
    assert ("order", ("id", True)) in calls
    assert ("limit", (2,)) in calls
    assert ("offset", (1,)) in calls

    inserted = client.users().insert(models.UsersInsert(email="a@b.c", is_active=True)).execute()
    assert inserted[0]["email"] == "a@b.c"
    assert ("insert", ({"email": "a@b.c", "is_active": True},)) in sessions[0].query.calls

    client.users().update(models.UsersUpdate(display_name="Ada")).eq("id", 1).execute()
    assert ("update", ({"display_name": "Ada"},)) in sessions[0].query.calls

    ranged = client.users().select("id", "email").range(0, 1).execute()
    assert ranged[0]["email"] == "a@b.c"
    assert ("range", (0, 1)) in sessions[0].query.calls

    one = client.users().select("id", "email").single().execute()
    assert one["id"] == 1
    assert ("single", ()) in sessions[0].query.calls

    client.users().upsert(
        models.UsersInsert(email="a@b.c", is_active=True), on_conflict="email"
    ).execute()
    assert ("upsert", ({"email": "a@b.c", "is_active": True}, "email")) in sessions[0].query.calls

    client.users().delete().eq("id", 1).execute()
    assert ("delete", ()) in sessions[0].query.calls
    client.close()
    assert sessions[0].closed


def test_strict_insert_keeps_defaulted_columns_required() -> None:
    ir = parse_spec_file(ROOT / "fixtures" / "sample_spec.json")
    loose = render_models(ir, strict_insert=False)
    strict = render_models(ir, strict_insert=True)

    def insert_block(source: str) -> str:
        start = source.index("class UsersInsert(")
        return source[start : source.index("\nclass ", start + 1)]

    loose_insert = insert_block(loose)
    strict_insert = insert_block(strict)
    assert "id: int | None = None" in loose_insert
    assert "created_at: datetime.datetime | None = None" in loose_insert
    assert "id: int\n" in strict_insert
    assert "id: int | None" not in strict_insert
    assert "created_at: datetime.datetime\n" in strict_insert
