from schema2client.ir import ArrayItem, Column
from schema2client.typemap import enum_str_enum_name, py_type


def test_integers() -> None:
    col = Column(name="id", openapi_type="integer", format="int8", nullable=False)
    assert py_type(col) == "int"
    col_null = Column(name="author_id", openapi_type="integer", format="integer", nullable=True)
    assert py_type(col_null) == "int | None"


def test_numeric_and_float() -> None:
    assert py_type(Column("score", "number", "numeric", False)) == "decimal.Decimal"
    assert py_type(Column("views", "number", "float4", True)) == "float | None"


def test_text_bool_uuid() -> None:
    assert py_type(Column("email", "string", "text", False)) == "str"
    assert py_type(Column("flag", "boolean", "bool", False)) == "bool"
    assert py_type(Column("id", "string", "uuid", False)) == "uuid.UUID"


def test_temporal() -> None:
    assert py_type(Column("d", "string", "date", True)) == "datetime.date | None"
    assert py_type(Column("t", "string", "time without time zone", False)) == "datetime.time"
    assert (
        py_type(Column("ts", "string", "timestamp without time zone", False)) == "datetime.datetime"
    )
    assert (
        py_type(Column("tstz", "string", "timestamp with time zone", False)) == "datetime.datetime"
    )


def test_json_and_bytea() -> None:
    assert py_type(Column("meta", "object", "jsonb", True)) == "dict[str, object] | None"
    assert py_type(Column("raw", "string", "bytea", False)) == "bytes"


def test_enum_read_vs_write() -> None:
    col = Column(
        name="kind",
        openapi_type="string",
        format="public.user_kind",
        nullable=False,
        enum=("member", "admin", "guest"),
    )
    assert py_type(col) == "Literal['member', 'admin', 'guest']"
    assert py_type(col, for_write=True) == "str"
    assert enum_str_enum_name("users", col) == "Users_PublicUserKindEnum"


def test_array() -> None:
    col = Column(
        name="tags",
        openapi_type="array",
        format=None,
        nullable=True,
        array_item=ArrayItem(openapi_type="string", format="text"),
    )
    assert py_type(col) == "list[str] | None"
