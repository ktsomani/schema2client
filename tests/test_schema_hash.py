from pathlib import Path

from schema2client.emitter import compute_schema_hash

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "sample_spec.json"


def test_schema_hash_is_stable() -> None:
    data = FIXTURE.read_bytes()
    assert compute_schema_hash(data) == compute_schema_hash(data)
    assert len(compute_schema_hash(data)) == 64
