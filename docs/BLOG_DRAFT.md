# Draft: Typed PostgREST rows in Python without pretending to be an SDK

Working title only — not published copy.

## Outline

1. Problem: `supabase-py` / `postgrest-py` return `list[dict]`; typos surface in production.
2. What Supabase ships today: `supabase gen types typescript` vs no official Python equivalent.
3. Generator vs SDK: schema2client emits `mydb.*` types + thin httpx wrappers; keep your existing client.
4. Design choice: `TypedDict` for reads, Pydantic for writes; why not one model type.
5. v0 cut: single-column `select()` via `@overload`; honest statement on multi-column.
6. Receipt: link to README `#the-receipt` with real `mypy` CI output.
7. Try it: `fixtures/sample_spec.json` diffed against `fixtures/generated/mydb/` in the browser.

## Demo commands

```bash
uv sync --extra dev
uv run schema2client generate --spec fixtures/sample_spec.json --out fixtures/generated --package mydb
uv run python scripts/demo_narrowing.py
```