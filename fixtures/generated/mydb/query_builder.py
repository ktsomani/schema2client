"""Typed PostgREST query builders (single-column select narrowing)."""

from __future__ import annotations

import datetime
import decimal
import uuid
from typing import ClassVar, Literal, Protocol, overload

from pydantic import TypeAdapter

from .models import (
    Posts_author_id,
    Posts_body,
    Posts_edited_on,
    Posts_id,
    Posts_published_at,
    Posts_reminder_time,
    Posts_title,
    Posts_view_count,
    PostsRow,
    Users_avatar,
    Users_created_at,
    Users_display_name,
    Users_email,
    Users_id,
    Users_is_active,
    Users_kind,
    Users_metadata,
    Users_score,
    Users_tags,
    UsersRow,
)


class _Select:
    """Projection passed to PostgREST.

    v0 stores one column (or ``"*"``). ``columns`` is a tuple so a later
    multi-column ``select`` can append names without changing ``execute``.
    """

    def __init__(self, columns: tuple[str, ...]) -> None:
        self.columns = columns

    def query(self) -> str:
        return ",".join(self.columns)


class _Queryable(Protocol):
    _filters: list[tuple[str, str, str]]
    _select: _Select


class _SyncHttpTransport(Protocol):
    def fetch_rows(self, table: str, builder: _Queryable) -> list[object]: ...


class _AsyncHttpTransport(Protocol):
    async def fetch_rows(self, table: str, builder: _Queryable) -> list[object]: ...


class PostsQueryBuilder:
    _table_name: ClassVar[str] = "posts"

    def __init__(self) -> None:
        self._filters: list[tuple[str, str, str]] = []
        self._select: _Select = _Select(("*",))
        self._sync_transport: _SyncHttpTransport | None = None
        self._async_transport: _AsyncHttpTransport | None = None

    @staticmethod
    def _encode(value: object) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    @overload
    def eq(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQueryBuilder: ...
    def eq(self, column: str, value: object) -> PostsQueryBuilder:
        self._filters.append((column, "eq", self._encode(value)))
        return self

    @overload
    def neq(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQueryBuilder: ...
    def neq(self, column: str, value: object) -> PostsQueryBuilder:
        self._filters.append((column, "neq", self._encode(value)))
        return self

    @overload
    def gt(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQueryBuilder: ...
    def gt(self, column: str, value: object) -> PostsQueryBuilder:
        self._filters.append((column, "gt", self._encode(value)))
        return self

    @overload
    def gte(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQueryBuilder: ...
    def gte(self, column: str, value: object) -> PostsQueryBuilder:
        self._filters.append((column, "gte", self._encode(value)))
        return self

    @overload
    def lt(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQueryBuilder: ...
    def lt(self, column: str, value: object) -> PostsQueryBuilder:
        self._filters.append((column, "lt", self._encode(value)))
        return self

    @overload
    def lte(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQueryBuilder: ...
    def lte(self, column: str, value: object) -> PostsQueryBuilder:
        self._filters.append((column, "lte", self._encode(value)))
        return self

    @overload
    def like(
        self,
        column: Literal["author_id"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["edited_on"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["id"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["published_at"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["reminder_time"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["view_count"],
        value: str,
    ) -> PostsQueryBuilder: ...
    def like(self, column: str, value: str) -> PostsQueryBuilder:
        self._filters.append((column, "like", value))
        return self

    @overload
    def ilike(
        self,
        column: Literal["author_id"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["edited_on"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["id"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["published_at"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["reminder_time"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["view_count"],
        value: str,
    ) -> PostsQueryBuilder: ...
    def ilike(self, column: str, value: str) -> PostsQueryBuilder:
        self._filters.append((column, "ilike", value))
        return self

    @overload
    def in_(
        self,
        column: Literal["author_id"],
        value: list[int],
    ) -> PostsQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["body"],
        value: list[str],
    ) -> PostsQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["edited_on"],
        value: list[datetime.date],
    ) -> PostsQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["id"],
        value: list[uuid.UUID],
    ) -> PostsQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["published_at"],
        value: list[datetime.datetime],
    ) -> PostsQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["reminder_time"],
        value: list[datetime.time],
    ) -> PostsQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["title"],
        value: list[str],
    ) -> PostsQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["view_count"],
        value: list[float],
    ) -> PostsQueryBuilder: ...
    def in_(self, column: str, value: object) -> PostsQueryBuilder:
        if isinstance(value, list):
            encoded = ",".join(self._encode(item) for item in value)
        else:
            encoded = self._encode(value)
        self._filters.append((column, "in", encoded))
        return self

    @overload
    def is_(
        self,
        column: Literal["author_id"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["body"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["edited_on"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["id"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["published_at"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["reminder_time"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["title"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["view_count"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQueryBuilder: ...
    def is_(self, column: str, value: Literal["null", "not.null"]) -> PostsQueryBuilder:
        self._filters.append((column, "is", value))
        return self

    @overload
    def select(self, column: Literal["*"]) -> PostsQuery_star: ...
    @overload
    def select(self, column: Literal["author_id"]) -> PostsQuery_author_id: ...
    @overload
    def select(self, column: Literal["body"]) -> PostsQuery_body: ...
    @overload
    def select(self, column: Literal["edited_on"]) -> PostsQuery_edited_on: ...
    @overload
    def select(self, column: Literal["id"]) -> PostsQuery_id: ...
    @overload
    def select(self, column: Literal["published_at"]) -> PostsQuery_published_at: ...
    @overload
    def select(self, column: Literal["reminder_time"]) -> PostsQuery_reminder_time: ...
    @overload
    def select(self, column: Literal["title"]) -> PostsQuery_title: ...
    @overload
    def select(self, column: Literal["view_count"]) -> PostsQuery_view_count: ...
    def select(self, column: str) -> object:
        if column == "*":
            self._select = _Select(("*",))
            return PostsQuery_star(self)
        if column == "author_id":
            self._select = _Select(("author_id",))
            return PostsQuery_author_id(self)
        if column == "body":
            self._select = _Select(("body",))
            return PostsQuery_body(self)
        if column == "edited_on":
            self._select = _Select(("edited_on",))
            return PostsQuery_edited_on(self)
        if column == "id":
            self._select = _Select(("id",))
            return PostsQuery_id(self)
        if column == "published_at":
            self._select = _Select(("published_at",))
            return PostsQuery_published_at(self)
        if column == "reminder_time":
            self._select = _Select(("reminder_time",))
            return PostsQuery_reminder_time(self)
        if column == "title":
            self._select = _Select(("title",))
            return PostsQuery_title(self)
        if column == "view_count":
            self._select = _Select(("view_count",))
            return PostsQuery_view_count(self)
        msg = f"unknown column {column!r}"
        raise ValueError(msg)


class PostsQuery_star:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[PostsRow]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_star.validate_python(raw)

    async def execute_async(self) -> list[PostsRow]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_star.validate_python(raw)


class PostsQuery_author_id:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Posts_author_id]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_author_id.validate_python(raw)

    async def execute_async(self) -> list[Posts_author_id]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_author_id.validate_python(raw)


class PostsQuery_body:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Posts_body]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_body.validate_python(raw)

    async def execute_async(self) -> list[Posts_body]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_body.validate_python(raw)


class PostsQuery_edited_on:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Posts_edited_on]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_edited_on.validate_python(raw)

    async def execute_async(self) -> list[Posts_edited_on]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_edited_on.validate_python(raw)


class PostsQuery_id:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Posts_id]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_id.validate_python(raw)

    async def execute_async(self) -> list[Posts_id]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_id.validate_python(raw)


class PostsQuery_published_at:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Posts_published_at]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_published_at.validate_python(raw)

    async def execute_async(self) -> list[Posts_published_at]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_published_at.validate_python(raw)


class PostsQuery_reminder_time:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Posts_reminder_time]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_reminder_time.validate_python(raw)

    async def execute_async(self) -> list[Posts_reminder_time]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_reminder_time.validate_python(raw)


class PostsQuery_title:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Posts_title]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_title.validate_python(raw)

    async def execute_async(self) -> list[Posts_title]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_title.validate_python(raw)


class PostsQuery_view_count:
    def __init__(self, parent: PostsQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Posts_view_count]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_view_count.validate_python(raw)

    async def execute_async(self) -> list[Posts_view_count]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        return _list_adapter_posts_view_count.validate_python(raw)


class UsersQueryBuilder:
    _table_name: ClassVar[str] = "users"

    def __init__(self) -> None:
        self._filters: list[tuple[str, str, str]] = []
        self._select: _Select = _Select(("*",))
        self._sync_transport: _SyncHttpTransport | None = None
        self._async_transport: _AsyncHttpTransport | None = None

    @staticmethod
    def _encode(value: object) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    @overload
    def eq(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQueryBuilder: ...
    @overload
    def eq(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQueryBuilder: ...
    def eq(self, column: str, value: object) -> UsersQueryBuilder:
        self._filters.append((column, "eq", self._encode(value)))
        return self

    @overload
    def neq(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQueryBuilder: ...
    @overload
    def neq(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQueryBuilder: ...
    def neq(self, column: str, value: object) -> UsersQueryBuilder:
        self._filters.append((column, "neq", self._encode(value)))
        return self

    @overload
    def gt(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQueryBuilder: ...
    @overload
    def gt(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQueryBuilder: ...
    def gt(self, column: str, value: object) -> UsersQueryBuilder:
        self._filters.append((column, "gt", self._encode(value)))
        return self

    @overload
    def gte(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQueryBuilder: ...
    @overload
    def gte(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQueryBuilder: ...
    def gte(self, column: str, value: object) -> UsersQueryBuilder:
        self._filters.append((column, "gte", self._encode(value)))
        return self

    @overload
    def lt(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQueryBuilder: ...
    @overload
    def lt(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQueryBuilder: ...
    def lt(self, column: str, value: object) -> UsersQueryBuilder:
        self._filters.append((column, "lt", self._encode(value)))
        return self

    @overload
    def lte(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQueryBuilder: ...
    @overload
    def lte(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQueryBuilder: ...
    def lte(self, column: str, value: object) -> UsersQueryBuilder:
        self._filters.append((column, "lte", self._encode(value)))
        return self

    @overload
    def like(
        self,
        column: Literal["avatar"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["created_at"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["id"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["is_active"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["kind"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["metadata"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["score"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def like(
        self,
        column: Literal["tags"],
        value: str,
    ) -> UsersQueryBuilder: ...
    def like(self, column: str, value: str) -> UsersQueryBuilder:
        self._filters.append((column, "like", value))
        return self

    @overload
    def ilike(
        self,
        column: Literal["avatar"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["created_at"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["id"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["is_active"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["kind"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["metadata"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["score"],
        value: str,
    ) -> UsersQueryBuilder: ...
    @overload
    def ilike(
        self,
        column: Literal["tags"],
        value: str,
    ) -> UsersQueryBuilder: ...
    def ilike(self, column: str, value: str) -> UsersQueryBuilder:
        self._filters.append((column, "ilike", value))
        return self

    @overload
    def in_(
        self,
        column: Literal["avatar"],
        value: list[bytes],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["created_at"],
        value: list[datetime.datetime],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["display_name"],
        value: list[str],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["email"],
        value: list[str],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["id"],
        value: list[int],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["is_active"],
        value: list[bool],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["kind"],
        value: list[Literal["member", "admin", "guest"]],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["metadata"],
        value: list[dict[str, object]],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["score"],
        value: list[decimal.Decimal],
    ) -> UsersQueryBuilder: ...
    @overload
    def in_(
        self,
        column: Literal["tags"],
        value: list[list[str]],
    ) -> UsersQueryBuilder: ...
    def in_(self, column: str, value: object) -> UsersQueryBuilder:
        if isinstance(value, list):
            encoded = ",".join(self._encode(item) for item in value)
        else:
            encoded = self._encode(value)
        self._filters.append((column, "in", encoded))
        return self

    @overload
    def is_(
        self,
        column: Literal["avatar"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["created_at"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["display_name"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["email"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["id"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["is_active"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["kind"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["metadata"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["score"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    @overload
    def is_(
        self,
        column: Literal["tags"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQueryBuilder: ...
    def is_(self, column: str, value: Literal["null", "not.null"]) -> UsersQueryBuilder:
        self._filters.append((column, "is", value))
        return self

    @overload
    def select(self, column: Literal["*"]) -> UsersQuery_star: ...
    @overload
    def select(self, column: Literal["avatar"]) -> UsersQuery_avatar: ...
    @overload
    def select(self, column: Literal["created_at"]) -> UsersQuery_created_at: ...
    @overload
    def select(self, column: Literal["display_name"]) -> UsersQuery_display_name: ...
    @overload
    def select(self, column: Literal["email"]) -> UsersQuery_email: ...
    @overload
    def select(self, column: Literal["id"]) -> UsersQuery_id: ...
    @overload
    def select(self, column: Literal["is_active"]) -> UsersQuery_is_active: ...
    @overload
    def select(self, column: Literal["kind"]) -> UsersQuery_kind: ...
    @overload
    def select(self, column: Literal["metadata"]) -> UsersQuery_metadata: ...
    @overload
    def select(self, column: Literal["score"]) -> UsersQuery_score: ...
    @overload
    def select(self, column: Literal["tags"]) -> UsersQuery_tags: ...
    def select(self, column: str) -> object:
        if column == "*":
            self._select = _Select(("*",))
            return UsersQuery_star(self)
        if column == "avatar":
            self._select = _Select(("avatar",))
            return UsersQuery_avatar(self)
        if column == "created_at":
            self._select = _Select(("created_at",))
            return UsersQuery_created_at(self)
        if column == "display_name":
            self._select = _Select(("display_name",))
            return UsersQuery_display_name(self)
        if column == "email":
            self._select = _Select(("email",))
            return UsersQuery_email(self)
        if column == "id":
            self._select = _Select(("id",))
            return UsersQuery_id(self)
        if column == "is_active":
            self._select = _Select(("is_active",))
            return UsersQuery_is_active(self)
        if column == "kind":
            self._select = _Select(("kind",))
            return UsersQuery_kind(self)
        if column == "metadata":
            self._select = _Select(("metadata",))
            return UsersQuery_metadata(self)
        if column == "score":
            self._select = _Select(("score",))
            return UsersQuery_score(self)
        if column == "tags":
            self._select = _Select(("tags",))
            return UsersQuery_tags(self)
        msg = f"unknown column {column!r}"
        raise ValueError(msg)


class UsersQuery_star:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[UsersRow]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_star.validate_python(raw)

    async def execute_async(self) -> list[UsersRow]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_star.validate_python(raw)


class UsersQuery_avatar:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_avatar]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_avatar.validate_python(raw)

    async def execute_async(self) -> list[Users_avatar]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_avatar.validate_python(raw)


class UsersQuery_created_at:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_created_at]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_created_at.validate_python(raw)

    async def execute_async(self) -> list[Users_created_at]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_created_at.validate_python(raw)


class UsersQuery_display_name:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_display_name]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_display_name.validate_python(raw)

    async def execute_async(self) -> list[Users_display_name]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_display_name.validate_python(raw)


class UsersQuery_email:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_email]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_email.validate_python(raw)

    async def execute_async(self) -> list[Users_email]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_email.validate_python(raw)


class UsersQuery_id:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_id]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_id.validate_python(raw)

    async def execute_async(self) -> list[Users_id]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_id.validate_python(raw)


class UsersQuery_is_active:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_is_active]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_is_active.validate_python(raw)

    async def execute_async(self) -> list[Users_is_active]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_is_active.validate_python(raw)


class UsersQuery_kind:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_kind]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_kind.validate_python(raw)

    async def execute_async(self) -> list[Users_kind]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_kind.validate_python(raw)


class UsersQuery_metadata:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_metadata]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_metadata.validate_python(raw)

    async def execute_async(self) -> list[Users_metadata]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_metadata.validate_python(raw)


class UsersQuery_score:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_score]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_score.validate_python(raw)

    async def execute_async(self) -> list[Users_score]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_score.validate_python(raw)


class UsersQuery_tags:
    def __init__(self, parent: UsersQueryBuilder) -> None:
        self._parent = parent

    def execute(self) -> list[Users_tags]:
        transport = self._parent._sync_transport
        if transport is None:
            return []
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_tags.validate_python(raw)

    async def execute_async(self) -> list[Users_tags]:
        transport = self._parent._async_transport
        if transport is None:
            return []
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        return _list_adapter_users_tags.validate_python(raw)


_list_adapter_posts_star: TypeAdapter[list[PostsRow]] = TypeAdapter(list[PostsRow])
_list_adapter_posts_author_id: TypeAdapter[list[Posts_author_id]] = TypeAdapter(
    list[Posts_author_id]
)
_list_adapter_posts_body: TypeAdapter[list[Posts_body]] = TypeAdapter(list[Posts_body])
_list_adapter_posts_edited_on: TypeAdapter[list[Posts_edited_on]] = TypeAdapter(
    list[Posts_edited_on]
)
_list_adapter_posts_id: TypeAdapter[list[Posts_id]] = TypeAdapter(list[Posts_id])
_list_adapter_posts_published_at: TypeAdapter[list[Posts_published_at]] = TypeAdapter(
    list[Posts_published_at]
)
_list_adapter_posts_reminder_time: TypeAdapter[list[Posts_reminder_time]] = TypeAdapter(
    list[Posts_reminder_time]
)
_list_adapter_posts_title: TypeAdapter[list[Posts_title]] = TypeAdapter(list[Posts_title])
_list_adapter_posts_view_count: TypeAdapter[list[Posts_view_count]] = TypeAdapter(
    list[Posts_view_count]
)
_list_adapter_users_star: TypeAdapter[list[UsersRow]] = TypeAdapter(list[UsersRow])
_list_adapter_users_avatar: TypeAdapter[list[Users_avatar]] = TypeAdapter(list[Users_avatar])
_list_adapter_users_created_at: TypeAdapter[list[Users_created_at]] = TypeAdapter(
    list[Users_created_at]
)
_list_adapter_users_display_name: TypeAdapter[list[Users_display_name]] = TypeAdapter(
    list[Users_display_name]
)
_list_adapter_users_email: TypeAdapter[list[Users_email]] = TypeAdapter(list[Users_email])
_list_adapter_users_id: TypeAdapter[list[Users_id]] = TypeAdapter(list[Users_id])
_list_adapter_users_is_active: TypeAdapter[list[Users_is_active]] = TypeAdapter(
    list[Users_is_active]
)
_list_adapter_users_kind: TypeAdapter[list[Users_kind]] = TypeAdapter(list[Users_kind])
_list_adapter_users_metadata: TypeAdapter[list[Users_metadata]] = TypeAdapter(list[Users_metadata])
_list_adapter_users_score: TypeAdapter[list[Users_score]] = TypeAdapter(list[Users_score])
_list_adapter_users_tags: TypeAdapter[list[Users_tags]] = TypeAdapter(list[Users_tags])
