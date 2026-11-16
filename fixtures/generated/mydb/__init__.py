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

SCHEMA_HASH = "0c071ce8ed978870de92d6b47044fe223adf2e9951571c71a3645aa18e724e6d"

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
