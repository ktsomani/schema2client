# schema2client

[![PyPI version](https://img.shields.io/pypi/v/schema2client.svg)](https://pypi.org/project/schema2client/)
[![mypy strict](https://img.shields.io/badge/mypy-strict-blue)](https://mypy-lang.org/)
[![types: zero ignores](https://img.shields.io/badge/types-zero%20ignores-blue)](https://github.com/soman/schema2client#the-receipt)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ci](https://github.com/soman/schema2client/actions/workflows/ci.yml/badge.svg)](https://github.com/soman/schema2client/actions/workflows/ci.yml)

Generate a typed PostgREST **client package** from an OpenAPI schema (`GET /rest/v1/`).

Supabase documents `supabase gen types typescript` and, in newer CLI releases, `supabase gen types --lang=python` from **database introspection**. The official runtime stack (`supabase-py` → `postgrest-py`) still returns `dict` / `list[dict]` from `.execute()` unless you wrap rows yourself. **schema2client** reads a **PostgREST OpenAPI document** and emits a package you instantiate: `Client` and `AsyncClient`, query builders, `TypedDict` row projections, and Pydantic write models. HTTP calls go through `postgrest-py`. `select("id")`, `select("id", "email")`, and `select("id", "email", "kind")` each return a different row type, and filters after `select` keep that type.

## What this is — and what it isn't

**schema2client generates the client you call.** `Client` and `AsyncClient` are the entry points. Query builders hang off `table("users")` or `users()`. Underneath, requests are performed by `postgrest-py` rather than a second HTTP stack. Supabase auth, realtime, and storage are not generated.

## The receipt

<a id="the-receipt"></a>

Recorded on the committed `fixtures/generated/mydb/` package plus `src/` (see `pyproject.toml` `files`).

```text
$ uv run mypy
Success: no issues found in 11 source files

$ grep -rn "type: ignore" fixtures/generated/mydb/ || true
$ echo "zero type: ignore in generated output"
zero type: ignore in generated output
```

## Column narrowing

`select` takes `"*"` or **one to three** column names as separate arguments. Each argument order is its own overload. The result type is one `TypedDict` per column set (names sorted in the class name), so `select("id", "email")` and `select("email", "id")` are both `list[Users_email_id]`. `.eq()` after `select` returns that same query, so `.execute()` stays narrowed.

```python
from mydb import Client

client = Client("https://example.supabase.co/rest/v1", "anon-key")
rows = client.table("users").select("id", "email").eq("is_active", True).execute()
reveal_type(rows)  # list[Users_email_id]
reveal_type(client.users().select("id").execute())  # list[Users_id]
reveal_type(client.users().select("*").execute())  # list[UsersRow]
# client.table("users").select("idd")  # mypy error: no matching overload
# client.table("users").select("id", "email", "kind", "score")  # four columns: no overload
```

Four or more columns are rejected. Generating an overload for every order of four names grows as `n! / (n-4)!` per table, which is the wrong default. A later version can raise the cap without changing `execute()`, because the query is already generic over the row `TypedDict`.

## Comparison

| | postgrest-py alone | hand-written types | schema2client |
| --- | --- | --- | --- |
| Return types | `dict` / `list[dict]` | Accurate until schema drifts | Generated from OpenAPI |
| Column typos | Runtime | Manual upkeep | `mypy` on `select("…")` |
| Write validation | None unless added | Manual Pydantic | Generated Insert/Update |
| Sync with DB | N/A | Manual | `SCHEMA_HASH` + regen |

## Prior art

| Tool | What it does | Gap vs schema2client |
| --- | --- | --- |
| [`datamodel-code-generator`](https://github.com/koxudaxi/datamodel-code-generator) | JSON Schema / OpenAPI → Pydantic (and other backends) | General-purpose; not PostgREST table/query shaped; no per-column `select()` overloads on a query builder; no committed `mydb.*` fixture contract in-repo |
| [`supabase gen types --lang=python`](https://supabase.com/docs/guides/api/rest/generating-python-types) | Supabase CLI types from **DB introspection** (not the root OpenAPI file alone in v0 here) | Tied to CLI/project workflow; documents wrapping `supabase-py` responses with generated models rather than static narrowing on `.select("column")` strings |
| [`castiron`](https://github.com/kmbhm1/castiron) | OpenAPI / migrations → typed Python (Pydantic today; typed client on roadmap) | Broader compiler; different IR/emit split; schema2client is intentionally narrower (PostgREST OpenAPI v0, `TypedDict` reads + Pydantic writes + overload narrowing) |
| `postgrest-py` / `supabase-py` | HTTP clients | No generated row types; returns mapping objects |

## CLI reference

```text
$ schema2client --help
Usage: schema2client [OPTIONS] COMMAND [ARGS]...

  Generate typed Python packages from PostgREST OpenAPI schemas.

Options:
  --help  Show this message and exit.

Commands:
  generate  Emit models, query builders, and HTTP clients from a schema...
```

```text
$ schema2client generate --help
Usage: schema2client generate [OPTIONS]

  Emit models, query builders, and HTTP clients from a schema file.

Options:
  --spec FILE      Path to a PostgREST OpenAPI JSON document.  [required]
  --out DIRECTORY  Output directory for the generated package tree.
                   [required]
  --package TEXT   Python package name for generated code (for example
                   ``mydb``).  [required]
  --help           Show this message and exit.
```

## Quickstart

From a committed OpenAPI JSON file:

```bash
schema2client generate \
  --spec path/to/openapi.json \
  --out ./generated \
  --package mydb
```

Export PostgREST OpenAPI (anon key only):

```bash
# curl -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY" \
#   "$SUPABASE_URL/rest/v1/" -o openapi.json
schema2client generate --spec openapi.json --out ./generated --package mydb
```

Use the **anon / public** key in examples only. Do not commit or pass service-role keys.

## Review it without running anything

- Input: [`fixtures/sample_spec.json`](fixtures/sample_spec.json)
- Generated package: [`fixtures/generated/mydb/`](fixtures/generated/mydb/)

## Roadmap

- `--source mgmt` for Supabase management API OpenAPI (not v0; v0 parses `definitions` / `paths` from a PostgREST export).
- `--url` to fetch root OpenAPI in the CLI (not implemented).
- `select` of four or more columns (the query type is already generic; the overload cap is 3).

## Versioning and stability

Each generated package exposes `SCHEMA_HASH` (SHA-256 of the input OpenAPI bytes). Regenerate and diff when the database changes; a hash mismatch means the committed types are stale.

Breaking generator changes bump the semver; regenerated output may change byte-for-byte even when your database did not.

## Development

```bash
uv sync --extra dev
uv run pytest
uv run mypy
uv run ruff check .
```

Canonical fixture regen:

```bash
uv run schema2client generate \
  --spec fixtures/sample_spec.json \
  --out fixtures/generated \
  --package mydb
```

Offline demo (no network): `uv run python scripts/demo_narrowing.py`. Blog outline: `docs/BLOG_DRAFT.md`.

## License

MIT