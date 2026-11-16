"""Typed PostgREST query builders.

``select`` accepts ``"*"`` or 1-3 column names. Every argument order is an
overload. Filters after ``select`` return the same generic query, so
``.execute()`` stays narrowed to that projection.
"""

from __future__ import annotations

import datetime
import decimal
import uuid
from typing import ClassVar, Generic, Literal, Protocol, TypeVar, cast, overload

from pydantic import TypeAdapter

from .models import (
    Posts_author_id,
    Posts_author_id_body,
    Posts_author_id_body_edited_on,
    Posts_author_id_body_id,
    Posts_author_id_body_published_at,
    Posts_author_id_body_reminder_time,
    Posts_author_id_body_title,
    Posts_author_id_body_view_count,
    Posts_author_id_edited_on,
    Posts_author_id_edited_on_id,
    Posts_author_id_edited_on_published_at,
    Posts_author_id_edited_on_reminder_time,
    Posts_author_id_edited_on_title,
    Posts_author_id_edited_on_view_count,
    Posts_author_id_id,
    Posts_author_id_id_published_at,
    Posts_author_id_id_reminder_time,
    Posts_author_id_id_title,
    Posts_author_id_id_view_count,
    Posts_author_id_published_at,
    Posts_author_id_published_at_reminder_time,
    Posts_author_id_published_at_title,
    Posts_author_id_published_at_view_count,
    Posts_author_id_reminder_time,
    Posts_author_id_reminder_time_title,
    Posts_author_id_reminder_time_view_count,
    Posts_author_id_title,
    Posts_author_id_title_view_count,
    Posts_author_id_view_count,
    Posts_body,
    Posts_body_edited_on,
    Posts_body_edited_on_id,
    Posts_body_edited_on_published_at,
    Posts_body_edited_on_reminder_time,
    Posts_body_edited_on_title,
    Posts_body_edited_on_view_count,
    Posts_body_id,
    Posts_body_id_published_at,
    Posts_body_id_reminder_time,
    Posts_body_id_title,
    Posts_body_id_view_count,
    Posts_body_published_at,
    Posts_body_published_at_reminder_time,
    Posts_body_published_at_title,
    Posts_body_published_at_view_count,
    Posts_body_reminder_time,
    Posts_body_reminder_time_title,
    Posts_body_reminder_time_view_count,
    Posts_body_title,
    Posts_body_title_view_count,
    Posts_body_view_count,
    Posts_edited_on,
    Posts_edited_on_id,
    Posts_edited_on_id_published_at,
    Posts_edited_on_id_reminder_time,
    Posts_edited_on_id_title,
    Posts_edited_on_id_view_count,
    Posts_edited_on_published_at,
    Posts_edited_on_published_at_reminder_time,
    Posts_edited_on_published_at_title,
    Posts_edited_on_published_at_view_count,
    Posts_edited_on_reminder_time,
    Posts_edited_on_reminder_time_title,
    Posts_edited_on_reminder_time_view_count,
    Posts_edited_on_title,
    Posts_edited_on_title_view_count,
    Posts_edited_on_view_count,
    Posts_id,
    Posts_id_published_at,
    Posts_id_published_at_reminder_time,
    Posts_id_published_at_title,
    Posts_id_published_at_view_count,
    Posts_id_reminder_time,
    Posts_id_reminder_time_title,
    Posts_id_reminder_time_view_count,
    Posts_id_title,
    Posts_id_title_view_count,
    Posts_id_view_count,
    Posts_published_at,
    Posts_published_at_reminder_time,
    Posts_published_at_reminder_time_title,
    Posts_published_at_reminder_time_view_count,
    Posts_published_at_title,
    Posts_published_at_title_view_count,
    Posts_published_at_view_count,
    Posts_reminder_time,
    Posts_reminder_time_title,
    Posts_reminder_time_title_view_count,
    Posts_reminder_time_view_count,
    Posts_title,
    Posts_title_view_count,
    Posts_view_count,
    PostsRow,
    Users_avatar,
    Users_avatar_created_at,
    Users_avatar_created_at_display_name,
    Users_avatar_created_at_email,
    Users_avatar_created_at_id,
    Users_avatar_created_at_is_active,
    Users_avatar_created_at_kind,
    Users_avatar_created_at_metadata,
    Users_avatar_created_at_score,
    Users_avatar_created_at_tags,
    Users_avatar_display_name,
    Users_avatar_display_name_email,
    Users_avatar_display_name_id,
    Users_avatar_display_name_is_active,
    Users_avatar_display_name_kind,
    Users_avatar_display_name_metadata,
    Users_avatar_display_name_score,
    Users_avatar_display_name_tags,
    Users_avatar_email,
    Users_avatar_email_id,
    Users_avatar_email_is_active,
    Users_avatar_email_kind,
    Users_avatar_email_metadata,
    Users_avatar_email_score,
    Users_avatar_email_tags,
    Users_avatar_id,
    Users_avatar_id_is_active,
    Users_avatar_id_kind,
    Users_avatar_id_metadata,
    Users_avatar_id_score,
    Users_avatar_id_tags,
    Users_avatar_is_active,
    Users_avatar_is_active_kind,
    Users_avatar_is_active_metadata,
    Users_avatar_is_active_score,
    Users_avatar_is_active_tags,
    Users_avatar_kind,
    Users_avatar_kind_metadata,
    Users_avatar_kind_score,
    Users_avatar_kind_tags,
    Users_avatar_metadata,
    Users_avatar_metadata_score,
    Users_avatar_metadata_tags,
    Users_avatar_score,
    Users_avatar_score_tags,
    Users_avatar_tags,
    Users_created_at,
    Users_created_at_display_name,
    Users_created_at_display_name_email,
    Users_created_at_display_name_id,
    Users_created_at_display_name_is_active,
    Users_created_at_display_name_kind,
    Users_created_at_display_name_metadata,
    Users_created_at_display_name_score,
    Users_created_at_display_name_tags,
    Users_created_at_email,
    Users_created_at_email_id,
    Users_created_at_email_is_active,
    Users_created_at_email_kind,
    Users_created_at_email_metadata,
    Users_created_at_email_score,
    Users_created_at_email_tags,
    Users_created_at_id,
    Users_created_at_id_is_active,
    Users_created_at_id_kind,
    Users_created_at_id_metadata,
    Users_created_at_id_score,
    Users_created_at_id_tags,
    Users_created_at_is_active,
    Users_created_at_is_active_kind,
    Users_created_at_is_active_metadata,
    Users_created_at_is_active_score,
    Users_created_at_is_active_tags,
    Users_created_at_kind,
    Users_created_at_kind_metadata,
    Users_created_at_kind_score,
    Users_created_at_kind_tags,
    Users_created_at_metadata,
    Users_created_at_metadata_score,
    Users_created_at_metadata_tags,
    Users_created_at_score,
    Users_created_at_score_tags,
    Users_created_at_tags,
    Users_display_name,
    Users_display_name_email,
    Users_display_name_email_id,
    Users_display_name_email_is_active,
    Users_display_name_email_kind,
    Users_display_name_email_metadata,
    Users_display_name_email_score,
    Users_display_name_email_tags,
    Users_display_name_id,
    Users_display_name_id_is_active,
    Users_display_name_id_kind,
    Users_display_name_id_metadata,
    Users_display_name_id_score,
    Users_display_name_id_tags,
    Users_display_name_is_active,
    Users_display_name_is_active_kind,
    Users_display_name_is_active_metadata,
    Users_display_name_is_active_score,
    Users_display_name_is_active_tags,
    Users_display_name_kind,
    Users_display_name_kind_metadata,
    Users_display_name_kind_score,
    Users_display_name_kind_tags,
    Users_display_name_metadata,
    Users_display_name_metadata_score,
    Users_display_name_metadata_tags,
    Users_display_name_score,
    Users_display_name_score_tags,
    Users_display_name_tags,
    Users_email,
    Users_email_id,
    Users_email_id_is_active,
    Users_email_id_kind,
    Users_email_id_metadata,
    Users_email_id_score,
    Users_email_id_tags,
    Users_email_is_active,
    Users_email_is_active_kind,
    Users_email_is_active_metadata,
    Users_email_is_active_score,
    Users_email_is_active_tags,
    Users_email_kind,
    Users_email_kind_metadata,
    Users_email_kind_score,
    Users_email_kind_tags,
    Users_email_metadata,
    Users_email_metadata_score,
    Users_email_metadata_tags,
    Users_email_score,
    Users_email_score_tags,
    Users_email_tags,
    Users_id,
    Users_id_is_active,
    Users_id_is_active_kind,
    Users_id_is_active_metadata,
    Users_id_is_active_score,
    Users_id_is_active_tags,
    Users_id_kind,
    Users_id_kind_metadata,
    Users_id_kind_score,
    Users_id_kind_tags,
    Users_id_metadata,
    Users_id_metadata_score,
    Users_id_metadata_tags,
    Users_id_score,
    Users_id_score_tags,
    Users_id_tags,
    Users_is_active,
    Users_is_active_kind,
    Users_is_active_kind_metadata,
    Users_is_active_kind_score,
    Users_is_active_kind_tags,
    Users_is_active_metadata,
    Users_is_active_metadata_score,
    Users_is_active_metadata_tags,
    Users_is_active_score,
    Users_is_active_score_tags,
    Users_is_active_tags,
    Users_kind,
    Users_kind_metadata,
    Users_kind_metadata_score,
    Users_kind_metadata_tags,
    Users_kind_score,
    Users_kind_score_tags,
    Users_kind_tags,
    Users_metadata,
    Users_metadata_score,
    Users_metadata_score_tags,
    Users_metadata_tags,
    Users_score,
    Users_score_tags,
    Users_tags,
    UsersRow,
)

_RowT = TypeVar("_RowT")


class _Select:
    """Columns sent as PostgREST ``select``. Order is the call order."""

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
    def like(self, column: Literal["author_id"], value: str) -> PostsQueryBuilder: ...
    @overload
    def like(self, column: Literal["body"], value: str) -> PostsQueryBuilder: ...
    @overload
    def like(self, column: Literal["edited_on"], value: str) -> PostsQueryBuilder: ...
    @overload
    def like(self, column: Literal["id"], value: str) -> PostsQueryBuilder: ...
    @overload
    def like(self, column: Literal["published_at"], value: str) -> PostsQueryBuilder: ...
    @overload
    def like(self, column: Literal["reminder_time"], value: str) -> PostsQueryBuilder: ...
    @overload
    def like(self, column: Literal["title"], value: str) -> PostsQueryBuilder: ...
    @overload
    def like(self, column: Literal["view_count"], value: str) -> PostsQueryBuilder: ...
    def like(self, column: str, value: str) -> PostsQueryBuilder:
        self._filters.append((column, "like", value))
        return self

    @overload
    def ilike(self, column: Literal["author_id"], value: str) -> PostsQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["body"], value: str) -> PostsQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["edited_on"], value: str) -> PostsQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["id"], value: str) -> PostsQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["published_at"], value: str) -> PostsQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["reminder_time"], value: str) -> PostsQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["title"], value: str) -> PostsQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["view_count"], value: str) -> PostsQueryBuilder: ...
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
    def select(self, column: Literal["*"], /) -> PostsQuery[PostsRow]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        /,
    ) -> PostsQuery[Posts_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["title"],
        /,
    ) -> PostsQuery[Posts_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["title"],
        /,
    ) -> PostsQuery[Posts_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["title"],
        /,
    ) -> PostsQuery[Posts_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["title"],
        /,
    ) -> PostsQuery[Posts_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["body"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_body_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["body"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["body"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_body_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["body"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_body_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["body"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_body_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["body"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_body_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["edited_on"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["edited_on"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["edited_on"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["edited_on"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["edited_on"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["edited_on"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["published_at"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["published_at"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["published_at"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["published_at"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["published_at"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["published_at"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["title"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["title"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["title"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["title"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["title"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["title"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["view_count"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["view_count"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["view_count"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["view_count"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["view_count"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["author_id"],
        column_2: Literal["view_count"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["author_id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_body_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["author_id"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["author_id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_body_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["author_id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_body_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["author_id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_body_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["author_id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_body_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["edited_on"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["edited_on"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["edited_on"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["edited_on"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["edited_on"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["edited_on"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["id"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["published_at"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["published_at"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["published_at"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["published_at"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["published_at"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["published_at"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["reminder_time"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["reminder_time"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["reminder_time"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["reminder_time"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["reminder_time"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["reminder_time"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["title"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["title"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["title"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["title"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["title"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["title"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["view_count"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["view_count"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["view_count"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["view_count"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["view_count"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["body"],
        column_2: Literal["view_count"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["author_id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["author_id"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["author_id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["author_id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["author_id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["author_id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["body"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_edited_on]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["body"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["body"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["body"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["body"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["body"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["id"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["published_at"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["published_at"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["published_at"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["published_at"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["published_at"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["published_at"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["reminder_time"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["reminder_time"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["reminder_time"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["reminder_time"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["reminder_time"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["reminder_time"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["title"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["title"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["title"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["title"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["title"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["title"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["view_count"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["view_count"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["view_count"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["view_count"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["view_count"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["edited_on"],
        column_2: Literal["view_count"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["author_id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["author_id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["author_id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["author_id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["author_id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["author_id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["body"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["body"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["body"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["body"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["body"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["body"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["edited_on"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["edited_on"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["edited_on"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["edited_on"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["edited_on"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["edited_on"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["published_at"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["published_at"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["published_at"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["published_at"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["published_at"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["published_at"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["reminder_time"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["title"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["title"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["title"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["title"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["title"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["title"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["view_count"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["view_count"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["view_count"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["view_count"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["view_count"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["view_count"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["author_id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["author_id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["author_id"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["author_id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["author_id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["author_id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["body"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["body"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["body"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["body"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["body"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["body"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["edited_on"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["edited_on"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["edited_on"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["edited_on"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["edited_on"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["edited_on"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["id"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_published_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["reminder_time"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["reminder_time"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["reminder_time"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["reminder_time"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["reminder_time"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["reminder_time"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["title"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["title"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["title"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["title"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["title"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["title"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_published_at_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["view_count"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["view_count"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["view_count"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["view_count"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["view_count"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["published_at"],
        column_2: Literal["view_count"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_published_at_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["author_id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["author_id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["author_id"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["author_id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["author_id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["author_id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["body"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["body"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["body"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["body"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["body"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["body"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["edited_on"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["edited_on"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["edited_on"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["edited_on"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["edited_on"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["edited_on"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["id"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["published_at"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["published_at"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["published_at"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["published_at"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_published_at_reminder_time]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["published_at"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["published_at"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["title"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["title"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["title"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["title"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["title"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["title"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_reminder_time_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["view_count"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["view_count"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["view_count"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["view_count"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["view_count"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["reminder_time"],
        column_2: Literal["view_count"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_reminder_time_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["author_id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["author_id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["author_id"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["author_id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["author_id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["author_id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_author_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["body"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["body"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["body"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["body"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["body"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["body"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_body_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["edited_on"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["edited_on"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["edited_on"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["edited_on"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["edited_on"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["edited_on"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_edited_on_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["id"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["id"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["published_at"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["published_at"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["published_at"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["published_at"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_published_at_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["published_at"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["published_at"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_published_at_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["reminder_time"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["reminder_time"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["reminder_time"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["reminder_time"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["reminder_time"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_title]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["reminder_time"],
        column_3: Literal["view_count"],
        /,
    ) -> PostsQuery[Posts_reminder_time_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["view_count"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["view_count"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["view_count"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["view_count"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["view_count"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["title"],
        column_2: Literal["view_count"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_reminder_time_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["author_id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_author_id_body_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["author_id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["author_id"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["author_id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["author_id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["author_id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_author_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["body"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_body_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["body"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["body"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_body_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["body"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_body_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["body"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["body"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_body_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["edited_on"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["edited_on"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_edited_on_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["edited_on"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["edited_on"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["edited_on"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["edited_on"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_edited_on_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["id"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["id"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["id"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_id_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["id"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["id"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["id"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["published_at"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["published_at"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["published_at"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["published_at"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_published_at_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["published_at"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["published_at"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_published_at_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["reminder_time"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["reminder_time"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["reminder_time"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["reminder_time"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["reminder_time"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_reminder_time_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["reminder_time"],
        column_3: Literal["title"],
        /,
    ) -> PostsQuery[Posts_reminder_time_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["title"],
        column_3: Literal["author_id"],
        /,
    ) -> PostsQuery[Posts_author_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["title"],
        column_3: Literal["body"],
        /,
    ) -> PostsQuery[Posts_body_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["title"],
        column_3: Literal["edited_on"],
        /,
    ) -> PostsQuery[Posts_edited_on_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["title"],
        column_3: Literal["id"],
        /,
    ) -> PostsQuery[Posts_id_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["title"],
        column_3: Literal["published_at"],
        /,
    ) -> PostsQuery[Posts_published_at_title_view_count]: ...
    @overload
    def select(
        self,
        column_1: Literal["view_count"],
        column_2: Literal["title"],
        column_3: Literal["reminder_time"],
        /,
    ) -> PostsQuery[Posts_reminder_time_title_view_count]: ...
    def select(self, *columns: str) -> object:
        if columns == ("*",):
            self._select = _Select(("*",))
            return PostsQuery(self, _posts_star)
        if len(columns) < 1 or len(columns) > 3 or len(set(columns)) != len(columns):
            msg = "select() accepts '*' or 1 to 3 distinct columns"
            raise ValueError(msg)
        key = tuple(sorted(columns))
        adapter = _posts_adapters.get(key)
        if adapter is None:
            msg = f"unknown columns {columns!r}"
            raise ValueError(msg)
        self._select = _Select(tuple(columns))
        return PostsQuery(self, adapter)


class PostsQuery(Generic[_RowT]):
    def __init__(self, parent: PostsQueryBuilder, adapter: object) -> None:
        self._parent = parent
        self._adapter = adapter

    @overload
    def eq(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQuery[_RowT]: ...
    def eq(self, column: str, value: object) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "eq", self._parent._encode(value)))
        return self

    @overload
    def neq(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQuery[_RowT]: ...
    def neq(self, column: str, value: object) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "neq", self._parent._encode(value)))
        return self

    @overload
    def gt(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQuery[_RowT]: ...
    def gt(self, column: str, value: object) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "gt", self._parent._encode(value)))
        return self

    @overload
    def gte(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQuery[_RowT]: ...
    def gte(self, column: str, value: object) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "gte", self._parent._encode(value)))
        return self

    @overload
    def lt(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQuery[_RowT]: ...
    def lt(self, column: str, value: object) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "lt", self._parent._encode(value)))
        return self

    @overload
    def lte(
        self,
        column: Literal["author_id"],
        value: int,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["body"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["edited_on"],
        value: datetime.date,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["id"],
        value: uuid.UUID,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["published_at"],
        value: datetime.datetime,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["reminder_time"],
        value: datetime.time,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["title"],
        value: str,
    ) -> PostsQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["view_count"],
        value: float,
    ) -> PostsQuery[_RowT]: ...
    def lte(self, column: str, value: object) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "lte", self._parent._encode(value)))
        return self

    @overload
    def like(self, column: Literal["author_id"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["body"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["edited_on"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["id"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["published_at"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["reminder_time"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["title"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["view_count"], value: str) -> PostsQuery[_RowT]: ...
    def like(self, column: str, value: str) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "like", value))
        return self

    @overload
    def ilike(self, column: Literal["author_id"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["body"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["edited_on"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["id"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["published_at"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["reminder_time"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["title"], value: str) -> PostsQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["view_count"], value: str) -> PostsQuery[_RowT]: ...
    def ilike(self, column: str, value: str) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "ilike", value))
        return self

    @overload
    def in_(
        self,
        column: Literal["author_id"],
        value: list[int],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["body"],
        value: list[str],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["edited_on"],
        value: list[datetime.date],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["id"],
        value: list[uuid.UUID],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["published_at"],
        value: list[datetime.datetime],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["reminder_time"],
        value: list[datetime.time],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["title"],
        value: list[str],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["view_count"],
        value: list[float],
    ) -> PostsQuery[_RowT]: ...
    def in_(self, column: str, value: object) -> PostsQuery[_RowT]:
        if isinstance(value, list):
            encoded = ",".join(self._parent._encode(item) for item in value)
        else:
            encoded = self._parent._encode(value)
        self._parent._filters.append((column, "in", encoded))
        return self

    @overload
    def is_(
        self,
        column: Literal["author_id"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["body"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["edited_on"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["id"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["published_at"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["reminder_time"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["title"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["view_count"],
        value: Literal["null"] | Literal["not.null"],
    ) -> PostsQuery[_RowT]: ...
    def is_(self, column: str, value: Literal["null", "not.null"]) -> PostsQuery[_RowT]:
        self._parent._filters.append((column, "is", value))
        return self

    def execute(self) -> list[_RowT]:
        transport = self._parent._sync_transport
        if transport is None:
            empty: list[_RowT] = []
            return empty
        raw = transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        parsed = cast(TypeAdapter[list[_RowT]], self._adapter).validate_python(raw)
        return parsed

    async def execute_async(self) -> list[_RowT]:
        transport = self._parent._async_transport
        if transport is None:
            empty: list[_RowT] = []
            return empty
        raw = await transport.fetch_rows(PostsQueryBuilder._table_name, self._parent)
        parsed = cast(TypeAdapter[list[_RowT]], self._adapter).validate_python(raw)
        return parsed


_posts_star: object = TypeAdapter(list[PostsRow])
_posts_adapters: dict[tuple[str, ...], object] = {
    ("author_id",): TypeAdapter(list[Posts_author_id]),
    ("body",): TypeAdapter(list[Posts_body]),
    ("edited_on",): TypeAdapter(list[Posts_edited_on]),
    ("id",): TypeAdapter(list[Posts_id]),
    ("published_at",): TypeAdapter(list[Posts_published_at]),
    ("reminder_time",): TypeAdapter(list[Posts_reminder_time]),
    ("title",): TypeAdapter(list[Posts_title]),
    ("view_count",): TypeAdapter(list[Posts_view_count]),
    ("author_id", "body"): TypeAdapter(list[Posts_author_id_body]),
    ("author_id", "edited_on"): TypeAdapter(list[Posts_author_id_edited_on]),
    ("author_id", "id"): TypeAdapter(list[Posts_author_id_id]),
    ("author_id", "published_at"): TypeAdapter(list[Posts_author_id_published_at]),
    ("author_id", "reminder_time"): TypeAdapter(list[Posts_author_id_reminder_time]),
    ("author_id", "title"): TypeAdapter(list[Posts_author_id_title]),
    ("author_id", "view_count"): TypeAdapter(list[Posts_author_id_view_count]),
    ("body", "edited_on"): TypeAdapter(list[Posts_body_edited_on]),
    ("body", "id"): TypeAdapter(list[Posts_body_id]),
    ("body", "published_at"): TypeAdapter(list[Posts_body_published_at]),
    ("body", "reminder_time"): TypeAdapter(list[Posts_body_reminder_time]),
    ("body", "title"): TypeAdapter(list[Posts_body_title]),
    ("body", "view_count"): TypeAdapter(list[Posts_body_view_count]),
    ("edited_on", "id"): TypeAdapter(list[Posts_edited_on_id]),
    ("edited_on", "published_at"): TypeAdapter(list[Posts_edited_on_published_at]),
    ("edited_on", "reminder_time"): TypeAdapter(list[Posts_edited_on_reminder_time]),
    ("edited_on", "title"): TypeAdapter(list[Posts_edited_on_title]),
    ("edited_on", "view_count"): TypeAdapter(list[Posts_edited_on_view_count]),
    ("id", "published_at"): TypeAdapter(list[Posts_id_published_at]),
    ("id", "reminder_time"): TypeAdapter(list[Posts_id_reminder_time]),
    ("id", "title"): TypeAdapter(list[Posts_id_title]),
    ("id", "view_count"): TypeAdapter(list[Posts_id_view_count]),
    ("published_at", "reminder_time"): TypeAdapter(list[Posts_published_at_reminder_time]),
    ("published_at", "title"): TypeAdapter(list[Posts_published_at_title]),
    ("published_at", "view_count"): TypeAdapter(list[Posts_published_at_view_count]),
    ("reminder_time", "title"): TypeAdapter(list[Posts_reminder_time_title]),
    ("reminder_time", "view_count"): TypeAdapter(list[Posts_reminder_time_view_count]),
    ("title", "view_count"): TypeAdapter(list[Posts_title_view_count]),
    ("author_id", "body", "edited_on"): TypeAdapter(list[Posts_author_id_body_edited_on]),
    ("author_id", "body", "id"): TypeAdapter(list[Posts_author_id_body_id]),
    ("author_id", "body", "published_at"): TypeAdapter(list[Posts_author_id_body_published_at]),
    ("author_id", "body", "reminder_time"): TypeAdapter(list[Posts_author_id_body_reminder_time]),
    ("author_id", "body", "title"): TypeAdapter(list[Posts_author_id_body_title]),
    ("author_id", "body", "view_count"): TypeAdapter(list[Posts_author_id_body_view_count]),
    ("author_id", "edited_on", "id"): TypeAdapter(list[Posts_author_id_edited_on_id]),
    ("author_id", "edited_on", "published_at"): TypeAdapter(
        list[Posts_author_id_edited_on_published_at]
    ),
    ("author_id", "edited_on", "reminder_time"): TypeAdapter(
        list[Posts_author_id_edited_on_reminder_time]
    ),
    ("author_id", "edited_on", "title"): TypeAdapter(list[Posts_author_id_edited_on_title]),
    ("author_id", "edited_on", "view_count"): TypeAdapter(
        list[Posts_author_id_edited_on_view_count]
    ),
    ("author_id", "id", "published_at"): TypeAdapter(list[Posts_author_id_id_published_at]),
    ("author_id", "id", "reminder_time"): TypeAdapter(list[Posts_author_id_id_reminder_time]),
    ("author_id", "id", "title"): TypeAdapter(list[Posts_author_id_id_title]),
    ("author_id", "id", "view_count"): TypeAdapter(list[Posts_author_id_id_view_count]),
    ("author_id", "published_at", "reminder_time"): TypeAdapter(
        list[Posts_author_id_published_at_reminder_time]
    ),
    ("author_id", "published_at", "title"): TypeAdapter(list[Posts_author_id_published_at_title]),
    ("author_id", "published_at", "view_count"): TypeAdapter(
        list[Posts_author_id_published_at_view_count]
    ),
    ("author_id", "reminder_time", "title"): TypeAdapter(list[Posts_author_id_reminder_time_title]),
    ("author_id", "reminder_time", "view_count"): TypeAdapter(
        list[Posts_author_id_reminder_time_view_count]
    ),
    ("author_id", "title", "view_count"): TypeAdapter(list[Posts_author_id_title_view_count]),
    ("body", "edited_on", "id"): TypeAdapter(list[Posts_body_edited_on_id]),
    ("body", "edited_on", "published_at"): TypeAdapter(list[Posts_body_edited_on_published_at]),
    ("body", "edited_on", "reminder_time"): TypeAdapter(list[Posts_body_edited_on_reminder_time]),
    ("body", "edited_on", "title"): TypeAdapter(list[Posts_body_edited_on_title]),
    ("body", "edited_on", "view_count"): TypeAdapter(list[Posts_body_edited_on_view_count]),
    ("body", "id", "published_at"): TypeAdapter(list[Posts_body_id_published_at]),
    ("body", "id", "reminder_time"): TypeAdapter(list[Posts_body_id_reminder_time]),
    ("body", "id", "title"): TypeAdapter(list[Posts_body_id_title]),
    ("body", "id", "view_count"): TypeAdapter(list[Posts_body_id_view_count]),
    ("body", "published_at", "reminder_time"): TypeAdapter(
        list[Posts_body_published_at_reminder_time]
    ),
    ("body", "published_at", "title"): TypeAdapter(list[Posts_body_published_at_title]),
    ("body", "published_at", "view_count"): TypeAdapter(list[Posts_body_published_at_view_count]),
    ("body", "reminder_time", "title"): TypeAdapter(list[Posts_body_reminder_time_title]),
    ("body", "reminder_time", "view_count"): TypeAdapter(list[Posts_body_reminder_time_view_count]),
    ("body", "title", "view_count"): TypeAdapter(list[Posts_body_title_view_count]),
    ("edited_on", "id", "published_at"): TypeAdapter(list[Posts_edited_on_id_published_at]),
    ("edited_on", "id", "reminder_time"): TypeAdapter(list[Posts_edited_on_id_reminder_time]),
    ("edited_on", "id", "title"): TypeAdapter(list[Posts_edited_on_id_title]),
    ("edited_on", "id", "view_count"): TypeAdapter(list[Posts_edited_on_id_view_count]),
    ("edited_on", "published_at", "reminder_time"): TypeAdapter(
        list[Posts_edited_on_published_at_reminder_time]
    ),
    ("edited_on", "published_at", "title"): TypeAdapter(list[Posts_edited_on_published_at_title]),
    ("edited_on", "published_at", "view_count"): TypeAdapter(
        list[Posts_edited_on_published_at_view_count]
    ),
    ("edited_on", "reminder_time", "title"): TypeAdapter(list[Posts_edited_on_reminder_time_title]),
    ("edited_on", "reminder_time", "view_count"): TypeAdapter(
        list[Posts_edited_on_reminder_time_view_count]
    ),
    ("edited_on", "title", "view_count"): TypeAdapter(list[Posts_edited_on_title_view_count]),
    ("id", "published_at", "reminder_time"): TypeAdapter(list[Posts_id_published_at_reminder_time]),
    ("id", "published_at", "title"): TypeAdapter(list[Posts_id_published_at_title]),
    ("id", "published_at", "view_count"): TypeAdapter(list[Posts_id_published_at_view_count]),
    ("id", "reminder_time", "title"): TypeAdapter(list[Posts_id_reminder_time_title]),
    ("id", "reminder_time", "view_count"): TypeAdapter(list[Posts_id_reminder_time_view_count]),
    ("id", "title", "view_count"): TypeAdapter(list[Posts_id_title_view_count]),
    ("published_at", "reminder_time", "title"): TypeAdapter(
        list[Posts_published_at_reminder_time_title]
    ),
    ("published_at", "reminder_time", "view_count"): TypeAdapter(
        list[Posts_published_at_reminder_time_view_count]
    ),
    ("published_at", "title", "view_count"): TypeAdapter(list[Posts_published_at_title_view_count]),
    ("reminder_time", "title", "view_count"): TypeAdapter(
        list[Posts_reminder_time_title_view_count]
    ),
}


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
    def like(self, column: Literal["avatar"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["created_at"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["display_name"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["email"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["id"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["is_active"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["kind"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["metadata"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["score"], value: str) -> UsersQueryBuilder: ...
    @overload
    def like(self, column: Literal["tags"], value: str) -> UsersQueryBuilder: ...
    def like(self, column: str, value: str) -> UsersQueryBuilder:
        self._filters.append((column, "like", value))
        return self

    @overload
    def ilike(self, column: Literal["avatar"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["created_at"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["display_name"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["email"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["id"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["is_active"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["kind"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["metadata"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["score"], value: str) -> UsersQueryBuilder: ...
    @overload
    def ilike(self, column: Literal["tags"], value: str) -> UsersQueryBuilder: ...
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
    def select(self, column: Literal["*"], /) -> UsersQuery[UsersRow]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        /,
    ) -> UsersQuery[Users_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        /,
    ) -> UsersQuery[Users_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        /,
    ) -> UsersQuery[Users_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        /,
    ) -> UsersQuery[Users_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        /,
    ) -> UsersQuery[Users_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        /,
    ) -> UsersQuery[Users_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["created_at"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["display_name"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["email"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["id"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["is_active"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["kind"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["metadata"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["score"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["avatar"],
        column_2: Literal["tags"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["avatar"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["display_name"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["email"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["id"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["is_active"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["kind"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["metadata"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["score"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["created_at"],
        column_2: Literal["tags"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["avatar"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_display_name]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["created_at"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["email"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["id"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["is_active"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["kind"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["metadata"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["score"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["display_name"],
        column_2: Literal["tags"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["avatar"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["created_at"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_email]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["display_name"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["id"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["is_active"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["kind"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["metadata"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["score"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["email"],
        column_2: Literal["tags"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["avatar"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["created_at"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["display_name"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_id]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["email"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["is_active"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["kind"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["metadata"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["score"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["id"],
        column_2: Literal["tags"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["avatar"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["created_at"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["display_name"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["email"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_is_active]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["id"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_is_active_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_is_active_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["kind"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_is_active_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_is_active_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["metadata"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_is_active_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["score"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_is_active_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_is_active_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["is_active"],
        column_2: Literal["tags"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_is_active_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["avatar"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["created_at"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["display_name"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["email"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["id"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active_kind]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_is_active_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_is_active_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["is_active"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_is_active_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_kind_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["metadata"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_kind_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_kind_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["score"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_kind_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_kind_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["kind"],
        column_2: Literal["tags"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_kind_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["avatar"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["created_at"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["display_name"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["email"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["id"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_is_active_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["is_active"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_kind_metadata]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_kind_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["kind"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_kind_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["score"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_metadata_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["metadata"],
        column_2: Literal["tags"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_metadata_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["avatar"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_avatar_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["created_at"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_created_at_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["display_name"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_display_name_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["email"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_email_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["id"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_id_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_is_active_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["is_active"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_is_active_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_kind_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_kind_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["kind"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_kind_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_metadata_score]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["metadata"],
        column_3: Literal["tags"],
        /,
    ) -> UsersQuery[Users_metadata_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["score"],
        column_2: Literal["tags"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_metadata_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_avatar_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_avatar_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_avatar_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["avatar"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_avatar_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_created_at_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_created_at_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_created_at_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_created_at_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["created_at"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_created_at_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_display_name_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_display_name_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_display_name_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_display_name_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["display_name"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_display_name_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_email_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_email_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_email_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_email_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_email_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["email"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_email_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_id_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_id_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_id_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_id_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["id"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_id_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_is_active_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_is_active_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["is_active"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_is_active_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_kind_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_kind_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["kind"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_kind_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_metadata_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["metadata"],
        column_3: Literal["score"],
        /,
    ) -> UsersQuery[Users_metadata_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        column_3: Literal["avatar"],
        /,
    ) -> UsersQuery[Users_avatar_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        column_3: Literal["created_at"],
        /,
    ) -> UsersQuery[Users_created_at_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        column_3: Literal["display_name"],
        /,
    ) -> UsersQuery[Users_display_name_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        column_3: Literal["email"],
        /,
    ) -> UsersQuery[Users_email_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        column_3: Literal["id"],
        /,
    ) -> UsersQuery[Users_id_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        column_3: Literal["is_active"],
        /,
    ) -> UsersQuery[Users_is_active_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        column_3: Literal["kind"],
        /,
    ) -> UsersQuery[Users_kind_score_tags]: ...
    @overload
    def select(
        self,
        column_1: Literal["tags"],
        column_2: Literal["score"],
        column_3: Literal["metadata"],
        /,
    ) -> UsersQuery[Users_metadata_score_tags]: ...
    def select(self, *columns: str) -> object:
        if columns == ("*",):
            self._select = _Select(("*",))
            return UsersQuery(self, _users_star)
        if len(columns) < 1 or len(columns) > 3 or len(set(columns)) != len(columns):
            msg = "select() accepts '*' or 1 to 3 distinct columns"
            raise ValueError(msg)
        key = tuple(sorted(columns))
        adapter = _users_adapters.get(key)
        if adapter is None:
            msg = f"unknown columns {columns!r}"
            raise ValueError(msg)
        self._select = _Select(tuple(columns))
        return UsersQuery(self, adapter)


class UsersQuery(Generic[_RowT]):
    def __init__(self, parent: UsersQueryBuilder, adapter: object) -> None:
        self._parent = parent
        self._adapter = adapter

    @overload
    def eq(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def eq(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQuery[_RowT]: ...
    def eq(self, column: str, value: object) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "eq", self._parent._encode(value)))
        return self

    @overload
    def neq(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def neq(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQuery[_RowT]: ...
    def neq(self, column: str, value: object) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "neq", self._parent._encode(value)))
        return self

    @overload
    def gt(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gt(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQuery[_RowT]: ...
    def gt(self, column: str, value: object) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "gt", self._parent._encode(value)))
        return self

    @overload
    def gte(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def gte(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQuery[_RowT]: ...
    def gte(self, column: str, value: object) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "gte", self._parent._encode(value)))
        return self

    @overload
    def lt(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lt(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQuery[_RowT]: ...
    def lt(self, column: str, value: object) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "lt", self._parent._encode(value)))
        return self

    @overload
    def lte(
        self,
        column: Literal["avatar"],
        value: bytes,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["created_at"],
        value: datetime.datetime,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["display_name"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["email"],
        value: str,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["id"],
        value: int,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["is_active"],
        value: bool,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["kind"],
        value: Literal["member", "admin", "guest"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["metadata"],
        value: dict[str, object],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["score"],
        value: decimal.Decimal,
    ) -> UsersQuery[_RowT]: ...
    @overload
    def lte(
        self,
        column: Literal["tags"],
        value: list[str],
    ) -> UsersQuery[_RowT]: ...
    def lte(self, column: str, value: object) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "lte", self._parent._encode(value)))
        return self

    @overload
    def like(self, column: Literal["avatar"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["created_at"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["display_name"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["email"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["id"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["is_active"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["kind"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["metadata"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["score"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def like(self, column: Literal["tags"], value: str) -> UsersQuery[_RowT]: ...
    def like(self, column: str, value: str) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "like", value))
        return self

    @overload
    def ilike(self, column: Literal["avatar"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["created_at"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["display_name"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["email"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["id"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["is_active"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["kind"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["metadata"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["score"], value: str) -> UsersQuery[_RowT]: ...
    @overload
    def ilike(self, column: Literal["tags"], value: str) -> UsersQuery[_RowT]: ...
    def ilike(self, column: str, value: str) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "ilike", value))
        return self

    @overload
    def in_(
        self,
        column: Literal["avatar"],
        value: list[bytes],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["created_at"],
        value: list[datetime.datetime],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["display_name"],
        value: list[str],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["email"],
        value: list[str],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["id"],
        value: list[int],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["is_active"],
        value: list[bool],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["kind"],
        value: list[Literal["member", "admin", "guest"]],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["metadata"],
        value: list[dict[str, object]],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["score"],
        value: list[decimal.Decimal],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def in_(
        self,
        column: Literal["tags"],
        value: list[list[str]],
    ) -> UsersQuery[_RowT]: ...
    def in_(self, column: str, value: object) -> UsersQuery[_RowT]:
        if isinstance(value, list):
            encoded = ",".join(self._parent._encode(item) for item in value)
        else:
            encoded = self._parent._encode(value)
        self._parent._filters.append((column, "in", encoded))
        return self

    @overload
    def is_(
        self,
        column: Literal["avatar"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["created_at"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["display_name"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["email"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["id"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["is_active"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["kind"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["metadata"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["score"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    @overload
    def is_(
        self,
        column: Literal["tags"],
        value: Literal["null"] | Literal["not.null"],
    ) -> UsersQuery[_RowT]: ...
    def is_(self, column: str, value: Literal["null", "not.null"]) -> UsersQuery[_RowT]:
        self._parent._filters.append((column, "is", value))
        return self

    def execute(self) -> list[_RowT]:
        transport = self._parent._sync_transport
        if transport is None:
            empty: list[_RowT] = []
            return empty
        raw = transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        parsed = cast(TypeAdapter[list[_RowT]], self._adapter).validate_python(raw)
        return parsed

    async def execute_async(self) -> list[_RowT]:
        transport = self._parent._async_transport
        if transport is None:
            empty: list[_RowT] = []
            return empty
        raw = await transport.fetch_rows(UsersQueryBuilder._table_name, self._parent)
        parsed = cast(TypeAdapter[list[_RowT]], self._adapter).validate_python(raw)
        return parsed


_users_star: object = TypeAdapter(list[UsersRow])
_users_adapters: dict[tuple[str, ...], object] = {
    ("avatar",): TypeAdapter(list[Users_avatar]),
    ("created_at",): TypeAdapter(list[Users_created_at]),
    ("display_name",): TypeAdapter(list[Users_display_name]),
    ("email",): TypeAdapter(list[Users_email]),
    ("id",): TypeAdapter(list[Users_id]),
    ("is_active",): TypeAdapter(list[Users_is_active]),
    ("kind",): TypeAdapter(list[Users_kind]),
    ("metadata",): TypeAdapter(list[Users_metadata]),
    ("score",): TypeAdapter(list[Users_score]),
    ("tags",): TypeAdapter(list[Users_tags]),
    ("avatar", "created_at"): TypeAdapter(list[Users_avatar_created_at]),
    ("avatar", "display_name"): TypeAdapter(list[Users_avatar_display_name]),
    ("avatar", "email"): TypeAdapter(list[Users_avatar_email]),
    ("avatar", "id"): TypeAdapter(list[Users_avatar_id]),
    ("avatar", "is_active"): TypeAdapter(list[Users_avatar_is_active]),
    ("avatar", "kind"): TypeAdapter(list[Users_avatar_kind]),
    ("avatar", "metadata"): TypeAdapter(list[Users_avatar_metadata]),
    ("avatar", "score"): TypeAdapter(list[Users_avatar_score]),
    ("avatar", "tags"): TypeAdapter(list[Users_avatar_tags]),
    ("created_at", "display_name"): TypeAdapter(list[Users_created_at_display_name]),
    ("created_at", "email"): TypeAdapter(list[Users_created_at_email]),
    ("created_at", "id"): TypeAdapter(list[Users_created_at_id]),
    ("created_at", "is_active"): TypeAdapter(list[Users_created_at_is_active]),
    ("created_at", "kind"): TypeAdapter(list[Users_created_at_kind]),
    ("created_at", "metadata"): TypeAdapter(list[Users_created_at_metadata]),
    ("created_at", "score"): TypeAdapter(list[Users_created_at_score]),
    ("created_at", "tags"): TypeAdapter(list[Users_created_at_tags]),
    ("display_name", "email"): TypeAdapter(list[Users_display_name_email]),
    ("display_name", "id"): TypeAdapter(list[Users_display_name_id]),
    ("display_name", "is_active"): TypeAdapter(list[Users_display_name_is_active]),
    ("display_name", "kind"): TypeAdapter(list[Users_display_name_kind]),
    ("display_name", "metadata"): TypeAdapter(list[Users_display_name_metadata]),
    ("display_name", "score"): TypeAdapter(list[Users_display_name_score]),
    ("display_name", "tags"): TypeAdapter(list[Users_display_name_tags]),
    ("email", "id"): TypeAdapter(list[Users_email_id]),
    ("email", "is_active"): TypeAdapter(list[Users_email_is_active]),
    ("email", "kind"): TypeAdapter(list[Users_email_kind]),
    ("email", "metadata"): TypeAdapter(list[Users_email_metadata]),
    ("email", "score"): TypeAdapter(list[Users_email_score]),
    ("email", "tags"): TypeAdapter(list[Users_email_tags]),
    ("id", "is_active"): TypeAdapter(list[Users_id_is_active]),
    ("id", "kind"): TypeAdapter(list[Users_id_kind]),
    ("id", "metadata"): TypeAdapter(list[Users_id_metadata]),
    ("id", "score"): TypeAdapter(list[Users_id_score]),
    ("id", "tags"): TypeAdapter(list[Users_id_tags]),
    ("is_active", "kind"): TypeAdapter(list[Users_is_active_kind]),
    ("is_active", "metadata"): TypeAdapter(list[Users_is_active_metadata]),
    ("is_active", "score"): TypeAdapter(list[Users_is_active_score]),
    ("is_active", "tags"): TypeAdapter(list[Users_is_active_tags]),
    ("kind", "metadata"): TypeAdapter(list[Users_kind_metadata]),
    ("kind", "score"): TypeAdapter(list[Users_kind_score]),
    ("kind", "tags"): TypeAdapter(list[Users_kind_tags]),
    ("metadata", "score"): TypeAdapter(list[Users_metadata_score]),
    ("metadata", "tags"): TypeAdapter(list[Users_metadata_tags]),
    ("score", "tags"): TypeAdapter(list[Users_score_tags]),
    ("avatar", "created_at", "display_name"): TypeAdapter(
        list[Users_avatar_created_at_display_name]
    ),
    ("avatar", "created_at", "email"): TypeAdapter(list[Users_avatar_created_at_email]),
    ("avatar", "created_at", "id"): TypeAdapter(list[Users_avatar_created_at_id]),
    ("avatar", "created_at", "is_active"): TypeAdapter(list[Users_avatar_created_at_is_active]),
    ("avatar", "created_at", "kind"): TypeAdapter(list[Users_avatar_created_at_kind]),
    ("avatar", "created_at", "metadata"): TypeAdapter(list[Users_avatar_created_at_metadata]),
    ("avatar", "created_at", "score"): TypeAdapter(list[Users_avatar_created_at_score]),
    ("avatar", "created_at", "tags"): TypeAdapter(list[Users_avatar_created_at_tags]),
    ("avatar", "display_name", "email"): TypeAdapter(list[Users_avatar_display_name_email]),
    ("avatar", "display_name", "id"): TypeAdapter(list[Users_avatar_display_name_id]),
    ("avatar", "display_name", "is_active"): TypeAdapter(list[Users_avatar_display_name_is_active]),
    ("avatar", "display_name", "kind"): TypeAdapter(list[Users_avatar_display_name_kind]),
    ("avatar", "display_name", "metadata"): TypeAdapter(list[Users_avatar_display_name_metadata]),
    ("avatar", "display_name", "score"): TypeAdapter(list[Users_avatar_display_name_score]),
    ("avatar", "display_name", "tags"): TypeAdapter(list[Users_avatar_display_name_tags]),
    ("avatar", "email", "id"): TypeAdapter(list[Users_avatar_email_id]),
    ("avatar", "email", "is_active"): TypeAdapter(list[Users_avatar_email_is_active]),
    ("avatar", "email", "kind"): TypeAdapter(list[Users_avatar_email_kind]),
    ("avatar", "email", "metadata"): TypeAdapter(list[Users_avatar_email_metadata]),
    ("avatar", "email", "score"): TypeAdapter(list[Users_avatar_email_score]),
    ("avatar", "email", "tags"): TypeAdapter(list[Users_avatar_email_tags]),
    ("avatar", "id", "is_active"): TypeAdapter(list[Users_avatar_id_is_active]),
    ("avatar", "id", "kind"): TypeAdapter(list[Users_avatar_id_kind]),
    ("avatar", "id", "metadata"): TypeAdapter(list[Users_avatar_id_metadata]),
    ("avatar", "id", "score"): TypeAdapter(list[Users_avatar_id_score]),
    ("avatar", "id", "tags"): TypeAdapter(list[Users_avatar_id_tags]),
    ("avatar", "is_active", "kind"): TypeAdapter(list[Users_avatar_is_active_kind]),
    ("avatar", "is_active", "metadata"): TypeAdapter(list[Users_avatar_is_active_metadata]),
    ("avatar", "is_active", "score"): TypeAdapter(list[Users_avatar_is_active_score]),
    ("avatar", "is_active", "tags"): TypeAdapter(list[Users_avatar_is_active_tags]),
    ("avatar", "kind", "metadata"): TypeAdapter(list[Users_avatar_kind_metadata]),
    ("avatar", "kind", "score"): TypeAdapter(list[Users_avatar_kind_score]),
    ("avatar", "kind", "tags"): TypeAdapter(list[Users_avatar_kind_tags]),
    ("avatar", "metadata", "score"): TypeAdapter(list[Users_avatar_metadata_score]),
    ("avatar", "metadata", "tags"): TypeAdapter(list[Users_avatar_metadata_tags]),
    ("avatar", "score", "tags"): TypeAdapter(list[Users_avatar_score_tags]),
    ("created_at", "display_name", "email"): TypeAdapter(list[Users_created_at_display_name_email]),
    ("created_at", "display_name", "id"): TypeAdapter(list[Users_created_at_display_name_id]),
    ("created_at", "display_name", "is_active"): TypeAdapter(
        list[Users_created_at_display_name_is_active]
    ),
    ("created_at", "display_name", "kind"): TypeAdapter(list[Users_created_at_display_name_kind]),
    ("created_at", "display_name", "metadata"): TypeAdapter(
        list[Users_created_at_display_name_metadata]
    ),
    ("created_at", "display_name", "score"): TypeAdapter(list[Users_created_at_display_name_score]),
    ("created_at", "display_name", "tags"): TypeAdapter(list[Users_created_at_display_name_tags]),
    ("created_at", "email", "id"): TypeAdapter(list[Users_created_at_email_id]),
    ("created_at", "email", "is_active"): TypeAdapter(list[Users_created_at_email_is_active]),
    ("created_at", "email", "kind"): TypeAdapter(list[Users_created_at_email_kind]),
    ("created_at", "email", "metadata"): TypeAdapter(list[Users_created_at_email_metadata]),
    ("created_at", "email", "score"): TypeAdapter(list[Users_created_at_email_score]),
    ("created_at", "email", "tags"): TypeAdapter(list[Users_created_at_email_tags]),
    ("created_at", "id", "is_active"): TypeAdapter(list[Users_created_at_id_is_active]),
    ("created_at", "id", "kind"): TypeAdapter(list[Users_created_at_id_kind]),
    ("created_at", "id", "metadata"): TypeAdapter(list[Users_created_at_id_metadata]),
    ("created_at", "id", "score"): TypeAdapter(list[Users_created_at_id_score]),
    ("created_at", "id", "tags"): TypeAdapter(list[Users_created_at_id_tags]),
    ("created_at", "is_active", "kind"): TypeAdapter(list[Users_created_at_is_active_kind]),
    ("created_at", "is_active", "metadata"): TypeAdapter(list[Users_created_at_is_active_metadata]),
    ("created_at", "is_active", "score"): TypeAdapter(list[Users_created_at_is_active_score]),
    ("created_at", "is_active", "tags"): TypeAdapter(list[Users_created_at_is_active_tags]),
    ("created_at", "kind", "metadata"): TypeAdapter(list[Users_created_at_kind_metadata]),
    ("created_at", "kind", "score"): TypeAdapter(list[Users_created_at_kind_score]),
    ("created_at", "kind", "tags"): TypeAdapter(list[Users_created_at_kind_tags]),
    ("created_at", "metadata", "score"): TypeAdapter(list[Users_created_at_metadata_score]),
    ("created_at", "metadata", "tags"): TypeAdapter(list[Users_created_at_metadata_tags]),
    ("created_at", "score", "tags"): TypeAdapter(list[Users_created_at_score_tags]),
    ("display_name", "email", "id"): TypeAdapter(list[Users_display_name_email_id]),
    ("display_name", "email", "is_active"): TypeAdapter(list[Users_display_name_email_is_active]),
    ("display_name", "email", "kind"): TypeAdapter(list[Users_display_name_email_kind]),
    ("display_name", "email", "metadata"): TypeAdapter(list[Users_display_name_email_metadata]),
    ("display_name", "email", "score"): TypeAdapter(list[Users_display_name_email_score]),
    ("display_name", "email", "tags"): TypeAdapter(list[Users_display_name_email_tags]),
    ("display_name", "id", "is_active"): TypeAdapter(list[Users_display_name_id_is_active]),
    ("display_name", "id", "kind"): TypeAdapter(list[Users_display_name_id_kind]),
    ("display_name", "id", "metadata"): TypeAdapter(list[Users_display_name_id_metadata]),
    ("display_name", "id", "score"): TypeAdapter(list[Users_display_name_id_score]),
    ("display_name", "id", "tags"): TypeAdapter(list[Users_display_name_id_tags]),
    ("display_name", "is_active", "kind"): TypeAdapter(list[Users_display_name_is_active_kind]),
    ("display_name", "is_active", "metadata"): TypeAdapter(
        list[Users_display_name_is_active_metadata]
    ),
    ("display_name", "is_active", "score"): TypeAdapter(list[Users_display_name_is_active_score]),
    ("display_name", "is_active", "tags"): TypeAdapter(list[Users_display_name_is_active_tags]),
    ("display_name", "kind", "metadata"): TypeAdapter(list[Users_display_name_kind_metadata]),
    ("display_name", "kind", "score"): TypeAdapter(list[Users_display_name_kind_score]),
    ("display_name", "kind", "tags"): TypeAdapter(list[Users_display_name_kind_tags]),
    ("display_name", "metadata", "score"): TypeAdapter(list[Users_display_name_metadata_score]),
    ("display_name", "metadata", "tags"): TypeAdapter(list[Users_display_name_metadata_tags]),
    ("display_name", "score", "tags"): TypeAdapter(list[Users_display_name_score_tags]),
    ("email", "id", "is_active"): TypeAdapter(list[Users_email_id_is_active]),
    ("email", "id", "kind"): TypeAdapter(list[Users_email_id_kind]),
    ("email", "id", "metadata"): TypeAdapter(list[Users_email_id_metadata]),
    ("email", "id", "score"): TypeAdapter(list[Users_email_id_score]),
    ("email", "id", "tags"): TypeAdapter(list[Users_email_id_tags]),
    ("email", "is_active", "kind"): TypeAdapter(list[Users_email_is_active_kind]),
    ("email", "is_active", "metadata"): TypeAdapter(list[Users_email_is_active_metadata]),
    ("email", "is_active", "score"): TypeAdapter(list[Users_email_is_active_score]),
    ("email", "is_active", "tags"): TypeAdapter(list[Users_email_is_active_tags]),
    ("email", "kind", "metadata"): TypeAdapter(list[Users_email_kind_metadata]),
    ("email", "kind", "score"): TypeAdapter(list[Users_email_kind_score]),
    ("email", "kind", "tags"): TypeAdapter(list[Users_email_kind_tags]),
    ("email", "metadata", "score"): TypeAdapter(list[Users_email_metadata_score]),
    ("email", "metadata", "tags"): TypeAdapter(list[Users_email_metadata_tags]),
    ("email", "score", "tags"): TypeAdapter(list[Users_email_score_tags]),
    ("id", "is_active", "kind"): TypeAdapter(list[Users_id_is_active_kind]),
    ("id", "is_active", "metadata"): TypeAdapter(list[Users_id_is_active_metadata]),
    ("id", "is_active", "score"): TypeAdapter(list[Users_id_is_active_score]),
    ("id", "is_active", "tags"): TypeAdapter(list[Users_id_is_active_tags]),
    ("id", "kind", "metadata"): TypeAdapter(list[Users_id_kind_metadata]),
    ("id", "kind", "score"): TypeAdapter(list[Users_id_kind_score]),
    ("id", "kind", "tags"): TypeAdapter(list[Users_id_kind_tags]),
    ("id", "metadata", "score"): TypeAdapter(list[Users_id_metadata_score]),
    ("id", "metadata", "tags"): TypeAdapter(list[Users_id_metadata_tags]),
    ("id", "score", "tags"): TypeAdapter(list[Users_id_score_tags]),
    ("is_active", "kind", "metadata"): TypeAdapter(list[Users_is_active_kind_metadata]),
    ("is_active", "kind", "score"): TypeAdapter(list[Users_is_active_kind_score]),
    ("is_active", "kind", "tags"): TypeAdapter(list[Users_is_active_kind_tags]),
    ("is_active", "metadata", "score"): TypeAdapter(list[Users_is_active_metadata_score]),
    ("is_active", "metadata", "tags"): TypeAdapter(list[Users_is_active_metadata_tags]),
    ("is_active", "score", "tags"): TypeAdapter(list[Users_is_active_score_tags]),
    ("kind", "metadata", "score"): TypeAdapter(list[Users_kind_metadata_score]),
    ("kind", "metadata", "tags"): TypeAdapter(list[Users_kind_metadata_tags]),
    ("kind", "score", "tags"): TypeAdapter(list[Users_kind_score_tags]),
    ("metadata", "score", "tags"): TypeAdapter(list[Users_metadata_score_tags]),
}
