"""Generated typed PostgREST package for ``mydb``."""

from .client_async import AsyncClient
from .client_sync import Client
from .models import (
    PostsInsert,
    PostsRow,
    PostsUpdate,
    UsersInsert,
    UsersRow,
    UsersUpdate,
)
from .query_builder import (
    PostsQueryBuilder,
    UsersQueryBuilder,
)

SCHEMA_HASH = "d0dbf593c3e26ac9e782308c61047461502f296c1e60a2778b8d6044162365cf"

__all__ = [
    "SCHEMA_HASH",
    "AsyncClient",
    "Client",
    "PostsInsert",
    "PostsQueryBuilder",
    "PostsRow",
    "PostsUpdate",
    "UsersInsert",
    "UsersQueryBuilder",
    "UsersRow",
    "UsersUpdate",
]
