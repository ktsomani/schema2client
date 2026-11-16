"""Generated PostgREST types package for ``mydb``."""

from . import models, query_builder
from .client_async import MydbAsyncClient
from .client_sync import MydbSyncClient

SCHEMA_HASH = "0c071ce8ed978870de92d6b47044fe223adf2e9951571c71a3645aa18e724e6d"

__all__ = [
    "SCHEMA_HASH",
    "MydbAsyncClient",
    "MydbSyncClient",
    "models",
    "query_builder",
]
