from pathlib import Path

from schema2client.emitter import render_models, render_query_builder
from schema2client.parser import parse_spec_file

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "sample_spec.json"
MODELS = Path(__file__).resolve().parents[1] / "fixtures" / "generated" / "mydb" / "models.py"
QUERY_BUILDER = (
    Path(__file__).resolve().parents[1] / "fixtures" / "generated" / "mydb" / "query_builder.py"
)


def test_models_matches_committed_fixture() -> None:
    ir = parse_spec_file(FIXTURE)
    rendered = render_models(ir)
    committed = MODELS.read_text(encoding="utf-8")
    assert rendered == committed, "regenerate with emit_models_package and ruff format"


def test_query_builder_matches_committed_fixture() -> None:
    ir = parse_spec_file(FIXTURE)
    rendered = render_query_builder(ir)
    committed = QUERY_BUILDER.read_text(encoding="utf-8")
    assert rendered == committed, "regenerate with emit_models_package and ruff format"
