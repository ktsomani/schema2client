"""Read and write types for PostgREST tables."""

from __future__ import annotations

import datetime
import decimal
import uuid
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict
from typing_extensions import TypedDict


class PostsRow(TypedDict):
    author_id: int
    body: str | None
    edited_on: datetime.date | None
    id: uuid.UUID
    published_at: datetime.datetime
    reminder_time: datetime.time | None
    title: str
    view_count: float | None


class Posts_author_id(TypedDict):
    author_id: int


class Posts_body(TypedDict):
    body: str | None


class Posts_edited_on(TypedDict):
    edited_on: datetime.date | None


class Posts_id(TypedDict):
    id: uuid.UUID


class Posts_published_at(TypedDict):
    published_at: datetime.datetime


class Posts_reminder_time(TypedDict):
    reminder_time: datetime.time | None


class Posts_title(TypedDict):
    title: str


class Posts_view_count(TypedDict):
    view_count: float | None


class PostsInsert(BaseModel):
    model_config = ConfigDict(extra="forbid")

    author_id: int
    body: str | None = None
    edited_on: datetime.date | None = None
    id: uuid.UUID
    published_at: datetime.datetime
    reminder_time: datetime.time | None = None
    title: str
    view_count: float | None = None


class PostsUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    author_id: int | None = None
    body: str | None = None
    edited_on: datetime.date | None = None
    id: uuid.UUID | None = None
    published_at: datetime.datetime | None = None
    reminder_time: datetime.time | None = None
    title: str | None = None
    view_count: float | None = None


class Users_PublicUserKindEnum(StrEnum):
    member = "member"
    admin = "admin"
    guest = "guest"


class UsersRow(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    display_name: str | None
    email: str
    id: int
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_avatar(TypedDict):
    avatar: bytes | None


class Users_created_at(TypedDict):
    created_at: datetime.datetime


class Users_display_name(TypedDict):
    display_name: str | None


class Users_email(TypedDict):
    email: str


class Users_id(TypedDict):
    id: int


class Users_is_active(TypedDict):
    is_active: bool


class Users_kind(TypedDict):
    kind: Literal["member", "admin", "guest"] | None


class Users_metadata(TypedDict):
    metadata: dict[str, object] | None


class Users_score(TypedDict):
    score: decimal.Decimal | None


class Users_tags(TypedDict):
    tags: list[str] | None


class UsersInsert(BaseModel):
    model_config = ConfigDict(extra="forbid")

    avatar: bytes | None = None
    created_at: datetime.datetime
    display_name: str | None = None
    email: str
    id: int
    is_active: bool
    kind: Users_PublicUserKindEnum | None = None
    metadata: dict[str, object] | None = None
    score: decimal.Decimal | None = None
    tags: list[str] | None = None


class UsersUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    avatar: bytes | None = None
    created_at: datetime.datetime | None = None
    display_name: str | None = None
    email: str | None = None
    id: int | None = None
    is_active: bool | None = None
    kind: Users_PublicUserKindEnum | None = None
    metadata: dict[str, object] | None = None
    score: decimal.Decimal | None = None
    tags: list[str] | None = None
