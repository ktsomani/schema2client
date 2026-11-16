from pathlib import Path

from schema2client.parser import parse_spec_file

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "sample_spec.json"


def test_parse_fixture_tables() -> None:
    ir = parse_spec_file(FIXTURE)
    names = {table.name for table in ir.tables}
    assert names == {"posts", "users"}


def test_parse_fixture_users_columns() -> None:
    ir = parse_spec_file(FIXTURE)
    users = next(table for table in ir.tables if table.name == "users")
    by_name = {column.name: column for column in users.columns}

    assert users.columns[0].name == "avatar"
    assert by_name["id"].nullable is False
    assert by_name["id"].has_default is True
    assert by_name["email"].has_default is False
    assert by_name["display_name"].nullable is True
    assert by_name["kind"].enum == ("member", "admin", "guest")
    assert by_name["tags"].array_item is not None
    assert by_name["tags"].array_item.format == "text"


def test_parse_openapi3_components() -> None:
    spec: dict[str, object] = {
        "paths": {"/widgets": {"get": {}}},
        "components": {
            "schemas": {
                "widgets": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        "id": {"type": "integer", "format": "int4"},
                    },
                }
            }
        },
    }
    from schema2client.parser import parse_spec

    tables = parse_spec(spec)
    assert len(tables.tables) == 1
    assert tables.tables[0].name == "widgets"
    assert tables.tables[0].columns[0].name == "id"
