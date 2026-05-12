"""Tests for Rust relationship extraction."""

from pathlib import Path

import pytest

from glma.db.ladybug_store import LadybugStore
from glma.index.chunks import extract_chunks
from glma.index.relationships import extract_relationships
from glma.models import FileRecord, ChunkType, Language, RelType, Confidence


@pytest.fixture
def store(tmp_path):
    db_path = tmp_path / "db" / "test.lbug"
    s = LadybugStore(db_path)
    yield s
    s.close()


def _make_rust_file(tmp_path, filename, content):
    src = tmp_path / filename
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(content)
    return src


class TestRustUse:
    def test_use_declaration(self, tmp_path, store):
        src = _make_rust_file(tmp_path, "main.rs", """\
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
}
""")
        chunks = extract_chunks(src, Language.RUST, tmp_path)
        store.upsert_file(FileRecord(
            path="main.rs", language=Language.RUST,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.rs", chunks)

        rels = extract_relationships(src, Language.RUST, tmp_path, chunks, store)
        use_rels = [r for r in rels if r.rel_type == RelType.IMPORTS]
        assert len(use_rels) >= 1
        assert any("std" in r.target_name for r in use_rels)


class TestRustCalls:
    def test_direct_call(self, tmp_path, store):
        src = _make_rust_file(tmp_path, "main.rs", """\
fn helper() -> i32 {
    42
}

fn main() {
    helper();
}
""")
        chunks = extract_chunks(src, Language.RUST, tmp_path)
        store.upsert_file(FileRecord(
            path="main.rs", language=Language.RUST,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.rs", chunks)

        rels = extract_relationships(src, Language.RUST, tmp_path, chunks, store)
        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        assert len(calls) >= 1
        assert any("helper" in r.target_name for r in calls)


class TestRustImpl:
    def test_impl_for_trait(self, tmp_path, store):
        src = _make_rust_file(tmp_path, "main.rs", """\
trait Describe {
    fn describe(&self) -> String;
}

struct Point {
    x: f64,
    y: f64,
}

impl Describe for Point {
    fn describe(&self) -> String {
        format!("({}, {})", self.x, self.y)
    }
}
""")
        chunks = extract_chunks(src, Language.RUST, tmp_path)
        store.upsert_file(FileRecord(
            path="main.rs", language=Language.RUST,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.rs", chunks)

        rels = extract_relationships(src, Language.RUST, tmp_path, chunks, store)
        impl_rels = [r for r in rels if r.rel_type == RelType.INHERITS]
        assert len(impl_rels) >= 1
        assert any("Describe" in r.target_name for r in impl_rels)


class TestRustMod:
    def test_mod_declaration(self, tmp_path, store):
        src = _make_rust_file(tmp_path, "main.rs", """\
mod network;
mod utils;

fn main() {}
""")
        chunks = extract_chunks(src, Language.RUST, tmp_path)
        store.upsert_file(FileRecord(
            path="main.rs", language=Language.RUST,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.rs", chunks)

        rels = extract_relationships(src, Language.RUST, tmp_path, chunks, store)
        mod_rels = [r for r in rels if r.rel_type == RelType.INCLUDES]
        assert len(mod_rels) >= 1
        mod_names = [r.target_name for r in mod_rels]
        assert "network" in mod_names
        assert "utils" in mod_names
