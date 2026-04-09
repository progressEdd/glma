"""Tests for C relationship extraction."""

import tempfile
from pathlib import Path

import pytest

from glma.db.ladybug_store import LadybugStore
from glma.index.chunks import extract_chunks
from glma.index.relationships import extract_relationships, extract_c_relationships
from glma.models import Chunk, ChunkType, Language, Relationship, RelType, Confidence


@pytest.fixture
def store(tmp_path):
    """Create a LadybugStore in a temp directory."""
    db_path = tmp_path / "db" / "test.lbug"
    s = LadybugStore(db_path)
    yield s
    s.close()


def _make_c_file(tmp_path, filename, content):
    """Write a C source file and return its path."""
    src = tmp_path / filename
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(content)
    return src


class TestCDirectCall:
    """Test direct function call extraction in C."""

    def test_c_direct_call(self, tmp_path, store):
        src = _make_c_file(tmp_path, "main.c", """\
int helper() {
    return 42;
}

int main() {
    return helper();
}
""")
        chunks = extract_chunks(src, Language.C, tmp_path)
        store.upsert_file(__import__("glma.models", fromlist=["FileRecord"]).FileRecord(
            path="main.c",
            language=Language.C,
            content_hash="abc",
            last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.c", chunks)

        rels = extract_relationships(src, Language.C, tmp_path, chunks, store)

        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        assert len(calls) >= 1
        direct_calls = [r for r in calls if r.confidence == Confidence.DIRECT]
        assert len(direct_calls) >= 1
        # Should be from main chunk, targeting helper
        call = direct_calls[0]
        assert "helper" in call.target_name
        assert call.target_id != ""  # Resolved

    def test_c_unresolved_call(self, tmp_path, store):
        src = _make_c_file(tmp_path, "main.c", """\
int main() {
    return unknown_func();
}
""")
        chunks = extract_chunks(src, Language.C, tmp_path)

        rels = extract_relationships(src, Language.C, tmp_path, chunks, store)

        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        assert len(calls) >= 1
        unresolved = [r for r in calls if r.target_id == "" and r.confidence == Confidence.INFERRED]
        assert len(unresolved) >= 1
        assert unresolved[0].target_name == "unknown_func"

    def test_c_system_include(self, tmp_path, store):
        src = _make_c_file(tmp_path, "main.c", """\
#include <stdio.h>

int main() {
    return 0;
}
""")
        chunks = extract_chunks(src, Language.C, tmp_path)

        rels = extract_relationships(src, Language.C, tmp_path, chunks, store)

        includes = [r for r in rels if r.rel_type == RelType.INCLUDES]
        assert len(includes) >= 1
        system_includes = [r for r in includes if r.confidence == Confidence.INFERRED]
        assert len(system_includes) >= 1
        assert "stdio.h" in system_includes[0].target_name

    def test_c_local_include(self, tmp_path, store):
        # Create a header file
        _make_c_file(tmp_path, "utils.h", """\
int helper();
""")
        src = _make_c_file(tmp_path, "main.c", """\
#include "utils.h"

int main() {
    return 0;
}
""")
        chunks = extract_chunks(src, Language.C, tmp_path)

        # Register the header file as indexed
        store.upsert_file(__import__("glma.models", fromlist=["FileRecord"]).FileRecord(
            path="utils.h",
            language=Language.C,
            content_hash="def456",
            last_indexed="2026-01-01T00:00:00",
            chunk_count=0,
        ))

        rels = extract_relationships(src, Language.C, tmp_path, chunks, store)

        includes = [r for r in rels if r.rel_type == RelType.INCLUDES]
        assert len(includes) >= 1
        local_includes = [r for r in includes if r.target_name == "utils.h"]
        assert len(local_includes) >= 1
        assert local_includes[0].confidence == Confidence.DIRECT

    def test_c_multiple_calls(self, tmp_path, store):
        src = _make_c_file(tmp_path, "main.c", """\
int foo() { return 1; }
int bar() { return 2; }
int baz() { return 3; }

int caller() {
    foo();
    bar();
    baz();
    return 0;
}
""")
        chunks = extract_chunks(src, Language.C, tmp_path)

        rels = extract_relationships(src, Language.C, tmp_path, chunks, store)

        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        # Should have at least 3 calls from caller
        caller_calls = [r for r in calls if "caller" in r.source_id]
        assert len(caller_calls) >= 3
