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


class Posts_author_id_body(TypedDict):
    author_id: int
    body: str | None


class Posts_author_id_edited_on(TypedDict):
    author_id: int
    edited_on: datetime.date | None


class Posts_author_id_id(TypedDict):
    author_id: int
    id: uuid.UUID


class Posts_author_id_published_at(TypedDict):
    author_id: int
    published_at: datetime.datetime


class Posts_author_id_reminder_time(TypedDict):
    author_id: int
    reminder_time: datetime.time | None


class Posts_author_id_title(TypedDict):
    author_id: int
    title: str


class Posts_author_id_view_count(TypedDict):
    author_id: int
    view_count: float | None


class Posts_body_edited_on(TypedDict):
    body: str | None
    edited_on: datetime.date | None


class Posts_body_id(TypedDict):
    body: str | None
    id: uuid.UUID


class Posts_body_published_at(TypedDict):
    body: str | None
    published_at: datetime.datetime


class Posts_body_reminder_time(TypedDict):
    body: str | None
    reminder_time: datetime.time | None


class Posts_body_title(TypedDict):
    body: str | None
    title: str


class Posts_body_view_count(TypedDict):
    body: str | None
    view_count: float | None


class Posts_edited_on_id(TypedDict):
    edited_on: datetime.date | None
    id: uuid.UUID


class Posts_edited_on_published_at(TypedDict):
    edited_on: datetime.date | None
    published_at: datetime.datetime


class Posts_edited_on_reminder_time(TypedDict):
    edited_on: datetime.date | None
    reminder_time: datetime.time | None


class Posts_edited_on_title(TypedDict):
    edited_on: datetime.date | None
    title: str


class Posts_edited_on_view_count(TypedDict):
    edited_on: datetime.date | None
    view_count: float | None


class Posts_id_published_at(TypedDict):
    id: uuid.UUID
    published_at: datetime.datetime


class Posts_id_reminder_time(TypedDict):
    id: uuid.UUID
    reminder_time: datetime.time | None


class Posts_id_title(TypedDict):
    id: uuid.UUID
    title: str


class Posts_id_view_count(TypedDict):
    id: uuid.UUID
    view_count: float | None


class Posts_published_at_reminder_time(TypedDict):
    published_at: datetime.datetime
    reminder_time: datetime.time | None


class Posts_published_at_title(TypedDict):
    published_at: datetime.datetime
    title: str


class Posts_published_at_view_count(TypedDict):
    published_at: datetime.datetime
    view_count: float | None


class Posts_reminder_time_title(TypedDict):
    reminder_time: datetime.time | None
    title: str


class Posts_reminder_time_view_count(TypedDict):
    reminder_time: datetime.time | None
    view_count: float | None


class Posts_title_view_count(TypedDict):
    title: str
    view_count: float | None


class Posts_author_id_body_edited_on(TypedDict):
    author_id: int
    body: str | None
    edited_on: datetime.date | None


class Posts_author_id_body_id(TypedDict):
    author_id: int
    body: str | None
    id: uuid.UUID


class Posts_author_id_body_published_at(TypedDict):
    author_id: int
    body: str | None
    published_at: datetime.datetime


class Posts_author_id_body_reminder_time(TypedDict):
    author_id: int
    body: str | None
    reminder_time: datetime.time | None


class Posts_author_id_body_title(TypedDict):
    author_id: int
    body: str | None
    title: str


class Posts_author_id_body_view_count(TypedDict):
    author_id: int
    body: str | None
    view_count: float | None


class Posts_author_id_edited_on_id(TypedDict):
    author_id: int
    edited_on: datetime.date | None
    id: uuid.UUID


class Posts_author_id_edited_on_published_at(TypedDict):
    author_id: int
    edited_on: datetime.date | None
    published_at: datetime.datetime


class Posts_author_id_edited_on_reminder_time(TypedDict):
    author_id: int
    edited_on: datetime.date | None
    reminder_time: datetime.time | None


class Posts_author_id_edited_on_title(TypedDict):
    author_id: int
    edited_on: datetime.date | None
    title: str


class Posts_author_id_edited_on_view_count(TypedDict):
    author_id: int
    edited_on: datetime.date | None
    view_count: float | None


class Posts_author_id_id_published_at(TypedDict):
    author_id: int
    id: uuid.UUID
    published_at: datetime.datetime


class Posts_author_id_id_reminder_time(TypedDict):
    author_id: int
    id: uuid.UUID
    reminder_time: datetime.time | None


class Posts_author_id_id_title(TypedDict):
    author_id: int
    id: uuid.UUID
    title: str


class Posts_author_id_id_view_count(TypedDict):
    author_id: int
    id: uuid.UUID
    view_count: float | None


class Posts_author_id_published_at_reminder_time(TypedDict):
    author_id: int
    published_at: datetime.datetime
    reminder_time: datetime.time | None


class Posts_author_id_published_at_title(TypedDict):
    author_id: int
    published_at: datetime.datetime
    title: str


class Posts_author_id_published_at_view_count(TypedDict):
    author_id: int
    published_at: datetime.datetime
    view_count: float | None


class Posts_author_id_reminder_time_title(TypedDict):
    author_id: int
    reminder_time: datetime.time | None
    title: str


class Posts_author_id_reminder_time_view_count(TypedDict):
    author_id: int
    reminder_time: datetime.time | None
    view_count: float | None


class Posts_author_id_title_view_count(TypedDict):
    author_id: int
    title: str
    view_count: float | None


class Posts_body_edited_on_id(TypedDict):
    body: str | None
    edited_on: datetime.date | None
    id: uuid.UUID


class Posts_body_edited_on_published_at(TypedDict):
    body: str | None
    edited_on: datetime.date | None
    published_at: datetime.datetime


class Posts_body_edited_on_reminder_time(TypedDict):
    body: str | None
    edited_on: datetime.date | None
    reminder_time: datetime.time | None


class Posts_body_edited_on_title(TypedDict):
    body: str | None
    edited_on: datetime.date | None
    title: str


class Posts_body_edited_on_view_count(TypedDict):
    body: str | None
    edited_on: datetime.date | None
    view_count: float | None


class Posts_body_id_published_at(TypedDict):
    body: str | None
    id: uuid.UUID
    published_at: datetime.datetime


class Posts_body_id_reminder_time(TypedDict):
    body: str | None
    id: uuid.UUID
    reminder_time: datetime.time | None


class Posts_body_id_title(TypedDict):
    body: str | None
    id: uuid.UUID
    title: str


class Posts_body_id_view_count(TypedDict):
    body: str | None
    id: uuid.UUID
    view_count: float | None


class Posts_body_published_at_reminder_time(TypedDict):
    body: str | None
    published_at: datetime.datetime
    reminder_time: datetime.time | None


class Posts_body_published_at_title(TypedDict):
    body: str | None
    published_at: datetime.datetime
    title: str


class Posts_body_published_at_view_count(TypedDict):
    body: str | None
    published_at: datetime.datetime
    view_count: float | None


class Posts_body_reminder_time_title(TypedDict):
    body: str | None
    reminder_time: datetime.time | None
    title: str


class Posts_body_reminder_time_view_count(TypedDict):
    body: str | None
    reminder_time: datetime.time | None
    view_count: float | None


class Posts_body_title_view_count(TypedDict):
    body: str | None
    title: str
    view_count: float | None


class Posts_edited_on_id_published_at(TypedDict):
    edited_on: datetime.date | None
    id: uuid.UUID
    published_at: datetime.datetime


class Posts_edited_on_id_reminder_time(TypedDict):
    edited_on: datetime.date | None
    id: uuid.UUID
    reminder_time: datetime.time | None


class Posts_edited_on_id_title(TypedDict):
    edited_on: datetime.date | None
    id: uuid.UUID
    title: str


class Posts_edited_on_id_view_count(TypedDict):
    edited_on: datetime.date | None
    id: uuid.UUID
    view_count: float | None


class Posts_edited_on_published_at_reminder_time(TypedDict):
    edited_on: datetime.date | None
    published_at: datetime.datetime
    reminder_time: datetime.time | None


class Posts_edited_on_published_at_title(TypedDict):
    edited_on: datetime.date | None
    published_at: datetime.datetime
    title: str


class Posts_edited_on_published_at_view_count(TypedDict):
    edited_on: datetime.date | None
    published_at: datetime.datetime
    view_count: float | None


class Posts_edited_on_reminder_time_title(TypedDict):
    edited_on: datetime.date | None
    reminder_time: datetime.time | None
    title: str


class Posts_edited_on_reminder_time_view_count(TypedDict):
    edited_on: datetime.date | None
    reminder_time: datetime.time | None
    view_count: float | None


class Posts_edited_on_title_view_count(TypedDict):
    edited_on: datetime.date | None
    title: str
    view_count: float | None


class Posts_id_published_at_reminder_time(TypedDict):
    id: uuid.UUID
    published_at: datetime.datetime
    reminder_time: datetime.time | None


class Posts_id_published_at_title(TypedDict):
    id: uuid.UUID
    published_at: datetime.datetime
    title: str


class Posts_id_published_at_view_count(TypedDict):
    id: uuid.UUID
    published_at: datetime.datetime
    view_count: float | None


class Posts_id_reminder_time_title(TypedDict):
    id: uuid.UUID
    reminder_time: datetime.time | None
    title: str


class Posts_id_reminder_time_view_count(TypedDict):
    id: uuid.UUID
    reminder_time: datetime.time | None
    view_count: float | None


class Posts_id_title_view_count(TypedDict):
    id: uuid.UUID
    title: str
    view_count: float | None


class Posts_published_at_reminder_time_title(TypedDict):
    published_at: datetime.datetime
    reminder_time: datetime.time | None
    title: str


class Posts_published_at_reminder_time_view_count(TypedDict):
    published_at: datetime.datetime
    reminder_time: datetime.time | None
    view_count: float | None


class Posts_published_at_title_view_count(TypedDict):
    published_at: datetime.datetime
    title: str
    view_count: float | None


class Posts_reminder_time_title_view_count(TypedDict):
    reminder_time: datetime.time | None
    title: str
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


class Users_avatar_created_at(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime


class Users_avatar_display_name(TypedDict):
    avatar: bytes | None
    display_name: str | None


class Users_avatar_email(TypedDict):
    avatar: bytes | None
    email: str


class Users_avatar_id(TypedDict):
    avatar: bytes | None
    id: int


class Users_avatar_is_active(TypedDict):
    avatar: bytes | None
    is_active: bool


class Users_avatar_kind(TypedDict):
    avatar: bytes | None
    kind: Literal["member", "admin", "guest"] | None


class Users_avatar_metadata(TypedDict):
    avatar: bytes | None
    metadata: dict[str, object] | None


class Users_avatar_score(TypedDict):
    avatar: bytes | None
    score: decimal.Decimal | None


class Users_avatar_tags(TypedDict):
    avatar: bytes | None
    tags: list[str] | None


class Users_created_at_display_name(TypedDict):
    created_at: datetime.datetime
    display_name: str | None


class Users_created_at_email(TypedDict):
    created_at: datetime.datetime
    email: str


class Users_created_at_id(TypedDict):
    created_at: datetime.datetime
    id: int


class Users_created_at_is_active(TypedDict):
    created_at: datetime.datetime
    is_active: bool


class Users_created_at_kind(TypedDict):
    created_at: datetime.datetime
    kind: Literal["member", "admin", "guest"] | None


class Users_created_at_metadata(TypedDict):
    created_at: datetime.datetime
    metadata: dict[str, object] | None


class Users_created_at_score(TypedDict):
    created_at: datetime.datetime
    score: decimal.Decimal | None


class Users_created_at_tags(TypedDict):
    created_at: datetime.datetime
    tags: list[str] | None


class Users_display_name_email(TypedDict):
    display_name: str | None
    email: str


class Users_display_name_id(TypedDict):
    display_name: str | None
    id: int


class Users_display_name_is_active(TypedDict):
    display_name: str | None
    is_active: bool


class Users_display_name_kind(TypedDict):
    display_name: str | None
    kind: Literal["member", "admin", "guest"] | None


class Users_display_name_metadata(TypedDict):
    display_name: str | None
    metadata: dict[str, object] | None


class Users_display_name_score(TypedDict):
    display_name: str | None
    score: decimal.Decimal | None


class Users_display_name_tags(TypedDict):
    display_name: str | None
    tags: list[str] | None


class Users_email_id(TypedDict):
    email: str
    id: int


class Users_email_is_active(TypedDict):
    email: str
    is_active: bool


class Users_email_kind(TypedDict):
    email: str
    kind: Literal["member", "admin", "guest"] | None


class Users_email_metadata(TypedDict):
    email: str
    metadata: dict[str, object] | None


class Users_email_score(TypedDict):
    email: str
    score: decimal.Decimal | None


class Users_email_tags(TypedDict):
    email: str
    tags: list[str] | None


class Users_id_is_active(TypedDict):
    id: int
    is_active: bool


class Users_id_kind(TypedDict):
    id: int
    kind: Literal["member", "admin", "guest"] | None


class Users_id_metadata(TypedDict):
    id: int
    metadata: dict[str, object] | None


class Users_id_score(TypedDict):
    id: int
    score: decimal.Decimal | None


class Users_id_tags(TypedDict):
    id: int
    tags: list[str] | None


class Users_is_active_kind(TypedDict):
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None


class Users_is_active_metadata(TypedDict):
    is_active: bool
    metadata: dict[str, object] | None


class Users_is_active_score(TypedDict):
    is_active: bool
    score: decimal.Decimal | None


class Users_is_active_tags(TypedDict):
    is_active: bool
    tags: list[str] | None


class Users_kind_metadata(TypedDict):
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None


class Users_kind_score(TypedDict):
    kind: Literal["member", "admin", "guest"] | None
    score: decimal.Decimal | None


class Users_kind_tags(TypedDict):
    kind: Literal["member", "admin", "guest"] | None
    tags: list[str] | None


class Users_metadata_score(TypedDict):
    metadata: dict[str, object] | None
    score: decimal.Decimal | None


class Users_metadata_tags(TypedDict):
    metadata: dict[str, object] | None
    tags: list[str] | None


class Users_score_tags(TypedDict):
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_avatar_created_at_display_name(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    display_name: str | None


class Users_avatar_created_at_email(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    email: str


class Users_avatar_created_at_id(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    id: int


class Users_avatar_created_at_is_active(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    is_active: bool


class Users_avatar_created_at_kind(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    kind: Literal["member", "admin", "guest"] | None


class Users_avatar_created_at_metadata(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    metadata: dict[str, object] | None


class Users_avatar_created_at_score(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    score: decimal.Decimal | None


class Users_avatar_created_at_tags(TypedDict):
    avatar: bytes | None
    created_at: datetime.datetime
    tags: list[str] | None


class Users_avatar_display_name_email(TypedDict):
    avatar: bytes | None
    display_name: str | None
    email: str


class Users_avatar_display_name_id(TypedDict):
    avatar: bytes | None
    display_name: str | None
    id: int


class Users_avatar_display_name_is_active(TypedDict):
    avatar: bytes | None
    display_name: str | None
    is_active: bool


class Users_avatar_display_name_kind(TypedDict):
    avatar: bytes | None
    display_name: str | None
    kind: Literal["member", "admin", "guest"] | None


class Users_avatar_display_name_metadata(TypedDict):
    avatar: bytes | None
    display_name: str | None
    metadata: dict[str, object] | None


class Users_avatar_display_name_score(TypedDict):
    avatar: bytes | None
    display_name: str | None
    score: decimal.Decimal | None


class Users_avatar_display_name_tags(TypedDict):
    avatar: bytes | None
    display_name: str | None
    tags: list[str] | None


class Users_avatar_email_id(TypedDict):
    avatar: bytes | None
    email: str
    id: int


class Users_avatar_email_is_active(TypedDict):
    avatar: bytes | None
    email: str
    is_active: bool


class Users_avatar_email_kind(TypedDict):
    avatar: bytes | None
    email: str
    kind: Literal["member", "admin", "guest"] | None


class Users_avatar_email_metadata(TypedDict):
    avatar: bytes | None
    email: str
    metadata: dict[str, object] | None


class Users_avatar_email_score(TypedDict):
    avatar: bytes | None
    email: str
    score: decimal.Decimal | None


class Users_avatar_email_tags(TypedDict):
    avatar: bytes | None
    email: str
    tags: list[str] | None


class Users_avatar_id_is_active(TypedDict):
    avatar: bytes | None
    id: int
    is_active: bool


class Users_avatar_id_kind(TypedDict):
    avatar: bytes | None
    id: int
    kind: Literal["member", "admin", "guest"] | None


class Users_avatar_id_metadata(TypedDict):
    avatar: bytes | None
    id: int
    metadata: dict[str, object] | None


class Users_avatar_id_score(TypedDict):
    avatar: bytes | None
    id: int
    score: decimal.Decimal | None


class Users_avatar_id_tags(TypedDict):
    avatar: bytes | None
    id: int
    tags: list[str] | None


class Users_avatar_is_active_kind(TypedDict):
    avatar: bytes | None
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None


class Users_avatar_is_active_metadata(TypedDict):
    avatar: bytes | None
    is_active: bool
    metadata: dict[str, object] | None


class Users_avatar_is_active_score(TypedDict):
    avatar: bytes | None
    is_active: bool
    score: decimal.Decimal | None


class Users_avatar_is_active_tags(TypedDict):
    avatar: bytes | None
    is_active: bool
    tags: list[str] | None


class Users_avatar_kind_metadata(TypedDict):
    avatar: bytes | None
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None


class Users_avatar_kind_score(TypedDict):
    avatar: bytes | None
    kind: Literal["member", "admin", "guest"] | None
    score: decimal.Decimal | None


class Users_avatar_kind_tags(TypedDict):
    avatar: bytes | None
    kind: Literal["member", "admin", "guest"] | None
    tags: list[str] | None


class Users_avatar_metadata_score(TypedDict):
    avatar: bytes | None
    metadata: dict[str, object] | None
    score: decimal.Decimal | None


class Users_avatar_metadata_tags(TypedDict):
    avatar: bytes | None
    metadata: dict[str, object] | None
    tags: list[str] | None


class Users_avatar_score_tags(TypedDict):
    avatar: bytes | None
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_created_at_display_name_email(TypedDict):
    created_at: datetime.datetime
    display_name: str | None
    email: str


class Users_created_at_display_name_id(TypedDict):
    created_at: datetime.datetime
    display_name: str | None
    id: int


class Users_created_at_display_name_is_active(TypedDict):
    created_at: datetime.datetime
    display_name: str | None
    is_active: bool


class Users_created_at_display_name_kind(TypedDict):
    created_at: datetime.datetime
    display_name: str | None
    kind: Literal["member", "admin", "guest"] | None


class Users_created_at_display_name_metadata(TypedDict):
    created_at: datetime.datetime
    display_name: str | None
    metadata: dict[str, object] | None


class Users_created_at_display_name_score(TypedDict):
    created_at: datetime.datetime
    display_name: str | None
    score: decimal.Decimal | None


class Users_created_at_display_name_tags(TypedDict):
    created_at: datetime.datetime
    display_name: str | None
    tags: list[str] | None


class Users_created_at_email_id(TypedDict):
    created_at: datetime.datetime
    email: str
    id: int


class Users_created_at_email_is_active(TypedDict):
    created_at: datetime.datetime
    email: str
    is_active: bool


class Users_created_at_email_kind(TypedDict):
    created_at: datetime.datetime
    email: str
    kind: Literal["member", "admin", "guest"] | None


class Users_created_at_email_metadata(TypedDict):
    created_at: datetime.datetime
    email: str
    metadata: dict[str, object] | None


class Users_created_at_email_score(TypedDict):
    created_at: datetime.datetime
    email: str
    score: decimal.Decimal | None


class Users_created_at_email_tags(TypedDict):
    created_at: datetime.datetime
    email: str
    tags: list[str] | None


class Users_created_at_id_is_active(TypedDict):
    created_at: datetime.datetime
    id: int
    is_active: bool


class Users_created_at_id_kind(TypedDict):
    created_at: datetime.datetime
    id: int
    kind: Literal["member", "admin", "guest"] | None


class Users_created_at_id_metadata(TypedDict):
    created_at: datetime.datetime
    id: int
    metadata: dict[str, object] | None


class Users_created_at_id_score(TypedDict):
    created_at: datetime.datetime
    id: int
    score: decimal.Decimal | None


class Users_created_at_id_tags(TypedDict):
    created_at: datetime.datetime
    id: int
    tags: list[str] | None


class Users_created_at_is_active_kind(TypedDict):
    created_at: datetime.datetime
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None


class Users_created_at_is_active_metadata(TypedDict):
    created_at: datetime.datetime
    is_active: bool
    metadata: dict[str, object] | None


class Users_created_at_is_active_score(TypedDict):
    created_at: datetime.datetime
    is_active: bool
    score: decimal.Decimal | None


class Users_created_at_is_active_tags(TypedDict):
    created_at: datetime.datetime
    is_active: bool
    tags: list[str] | None


class Users_created_at_kind_metadata(TypedDict):
    created_at: datetime.datetime
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None


class Users_created_at_kind_score(TypedDict):
    created_at: datetime.datetime
    kind: Literal["member", "admin", "guest"] | None
    score: decimal.Decimal | None


class Users_created_at_kind_tags(TypedDict):
    created_at: datetime.datetime
    kind: Literal["member", "admin", "guest"] | None
    tags: list[str] | None


class Users_created_at_metadata_score(TypedDict):
    created_at: datetime.datetime
    metadata: dict[str, object] | None
    score: decimal.Decimal | None


class Users_created_at_metadata_tags(TypedDict):
    created_at: datetime.datetime
    metadata: dict[str, object] | None
    tags: list[str] | None


class Users_created_at_score_tags(TypedDict):
    created_at: datetime.datetime
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_display_name_email_id(TypedDict):
    display_name: str | None
    email: str
    id: int


class Users_display_name_email_is_active(TypedDict):
    display_name: str | None
    email: str
    is_active: bool


class Users_display_name_email_kind(TypedDict):
    display_name: str | None
    email: str
    kind: Literal["member", "admin", "guest"] | None


class Users_display_name_email_metadata(TypedDict):
    display_name: str | None
    email: str
    metadata: dict[str, object] | None


class Users_display_name_email_score(TypedDict):
    display_name: str | None
    email: str
    score: decimal.Decimal | None


class Users_display_name_email_tags(TypedDict):
    display_name: str | None
    email: str
    tags: list[str] | None


class Users_display_name_id_is_active(TypedDict):
    display_name: str | None
    id: int
    is_active: bool


class Users_display_name_id_kind(TypedDict):
    display_name: str | None
    id: int
    kind: Literal["member", "admin", "guest"] | None


class Users_display_name_id_metadata(TypedDict):
    display_name: str | None
    id: int
    metadata: dict[str, object] | None


class Users_display_name_id_score(TypedDict):
    display_name: str | None
    id: int
    score: decimal.Decimal | None


class Users_display_name_id_tags(TypedDict):
    display_name: str | None
    id: int
    tags: list[str] | None


class Users_display_name_is_active_kind(TypedDict):
    display_name: str | None
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None


class Users_display_name_is_active_metadata(TypedDict):
    display_name: str | None
    is_active: bool
    metadata: dict[str, object] | None


class Users_display_name_is_active_score(TypedDict):
    display_name: str | None
    is_active: bool
    score: decimal.Decimal | None


class Users_display_name_is_active_tags(TypedDict):
    display_name: str | None
    is_active: bool
    tags: list[str] | None


class Users_display_name_kind_metadata(TypedDict):
    display_name: str | None
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None


class Users_display_name_kind_score(TypedDict):
    display_name: str | None
    kind: Literal["member", "admin", "guest"] | None
    score: decimal.Decimal | None


class Users_display_name_kind_tags(TypedDict):
    display_name: str | None
    kind: Literal["member", "admin", "guest"] | None
    tags: list[str] | None


class Users_display_name_metadata_score(TypedDict):
    display_name: str | None
    metadata: dict[str, object] | None
    score: decimal.Decimal | None


class Users_display_name_metadata_tags(TypedDict):
    display_name: str | None
    metadata: dict[str, object] | None
    tags: list[str] | None


class Users_display_name_score_tags(TypedDict):
    display_name: str | None
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_email_id_is_active(TypedDict):
    email: str
    id: int
    is_active: bool


class Users_email_id_kind(TypedDict):
    email: str
    id: int
    kind: Literal["member", "admin", "guest"] | None


class Users_email_id_metadata(TypedDict):
    email: str
    id: int
    metadata: dict[str, object] | None


class Users_email_id_score(TypedDict):
    email: str
    id: int
    score: decimal.Decimal | None


class Users_email_id_tags(TypedDict):
    email: str
    id: int
    tags: list[str] | None


class Users_email_is_active_kind(TypedDict):
    email: str
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None


class Users_email_is_active_metadata(TypedDict):
    email: str
    is_active: bool
    metadata: dict[str, object] | None


class Users_email_is_active_score(TypedDict):
    email: str
    is_active: bool
    score: decimal.Decimal | None


class Users_email_is_active_tags(TypedDict):
    email: str
    is_active: bool
    tags: list[str] | None


class Users_email_kind_metadata(TypedDict):
    email: str
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None


class Users_email_kind_score(TypedDict):
    email: str
    kind: Literal["member", "admin", "guest"] | None
    score: decimal.Decimal | None


class Users_email_kind_tags(TypedDict):
    email: str
    kind: Literal["member", "admin", "guest"] | None
    tags: list[str] | None


class Users_email_metadata_score(TypedDict):
    email: str
    metadata: dict[str, object] | None
    score: decimal.Decimal | None


class Users_email_metadata_tags(TypedDict):
    email: str
    metadata: dict[str, object] | None
    tags: list[str] | None


class Users_email_score_tags(TypedDict):
    email: str
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_id_is_active_kind(TypedDict):
    id: int
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None


class Users_id_is_active_metadata(TypedDict):
    id: int
    is_active: bool
    metadata: dict[str, object] | None


class Users_id_is_active_score(TypedDict):
    id: int
    is_active: bool
    score: decimal.Decimal | None


class Users_id_is_active_tags(TypedDict):
    id: int
    is_active: bool
    tags: list[str] | None


class Users_id_kind_metadata(TypedDict):
    id: int
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None


class Users_id_kind_score(TypedDict):
    id: int
    kind: Literal["member", "admin", "guest"] | None
    score: decimal.Decimal | None


class Users_id_kind_tags(TypedDict):
    id: int
    kind: Literal["member", "admin", "guest"] | None
    tags: list[str] | None


class Users_id_metadata_score(TypedDict):
    id: int
    metadata: dict[str, object] | None
    score: decimal.Decimal | None


class Users_id_metadata_tags(TypedDict):
    id: int
    metadata: dict[str, object] | None
    tags: list[str] | None


class Users_id_score_tags(TypedDict):
    id: int
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_is_active_kind_metadata(TypedDict):
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None


class Users_is_active_kind_score(TypedDict):
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None
    score: decimal.Decimal | None


class Users_is_active_kind_tags(TypedDict):
    is_active: bool
    kind: Literal["member", "admin", "guest"] | None
    tags: list[str] | None


class Users_is_active_metadata_score(TypedDict):
    is_active: bool
    metadata: dict[str, object] | None
    score: decimal.Decimal | None


class Users_is_active_metadata_tags(TypedDict):
    is_active: bool
    metadata: dict[str, object] | None
    tags: list[str] | None


class Users_is_active_score_tags(TypedDict):
    is_active: bool
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_kind_metadata_score(TypedDict):
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None
    score: decimal.Decimal | None


class Users_kind_metadata_tags(TypedDict):
    kind: Literal["member", "admin", "guest"] | None
    metadata: dict[str, object] | None
    tags: list[str] | None


class Users_kind_score_tags(TypedDict):
    kind: Literal["member", "admin", "guest"] | None
    score: decimal.Decimal | None
    tags: list[str] | None


class Users_metadata_score_tags(TypedDict):
    metadata: dict[str, object] | None
    score: decimal.Decimal | None
    tags: list[str] | None


class UsersInsert(BaseModel):
    model_config = ConfigDict(extra="forbid")

    avatar: bytes | None = None
    created_at: datetime.datetime | None = None
    display_name: str | None = None
    email: str
    id: int | None = None
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
