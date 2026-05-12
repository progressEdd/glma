"""Tests for C++ relationship extraction."""

from pathlib import Path

import pytest

from glma.db.ladybug_store import LadybugStore
from glma.index.chunks import extract_chunks
from glma.index.relationships import extract_relationships
from glma.models import FileRecord, ChunkType, Language, RelType, Confidence

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def store(tmp_path):
    db_path = tmp_path / "db" / "test.lbug"
    s = LadybugStore(db_path)
    yield s
    s.close()


def _make_cpp_file(tmp_path, filename, content):
    src = tmp_path / filename
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(content)
    return src


class TestCppCalls:
    def test_direct_call(self, tmp_path, store):
        src = _make_cpp_file(tmp_path, "main.cpp", """\
int helper() {
    return 42;
}

int main() {
    return helper();
}
""")
        chunks = extract_chunks(src, Language.CPP, tmp_path)
        store.upsert_file(FileRecord(
            path="main.cpp", language=Language.CPP,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.cpp", chunks)

        rels = extract_relationships(src, Language.CPP, tmp_path, chunks, store)
        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        assert len(calls) >= 1
        direct = [r for r in calls if r.confidence == Confidence.DIRECT]
        assert len(direct) >= 1
        assert "helper" in direct[0].target_name


class TestCppInheritance:
    def test_class_inheritance(self, tmp_path, store):
        src = _make_cpp_file(tmp_path, "main.cpp", """\
class Base {
public:
    virtual void foo() {}
};

class Derived : public Base {
public:
    void foo() override {}
};
""")
        chunks = extract_chunks(src, Language.CPP, tmp_path)
        store.upsert_file(FileRecord(
            path="main.cpp", language=Language.CPP,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.cpp", chunks)

        rels = extract_relationships(src, Language.CPP, tmp_path, chunks, store)
        inherits = [r for r in rels if r.rel_type == RelType.INHERITS]
        assert len(inherits) >= 1
        assert any("Base" in r.target_name for r in inherits)


class TestCppUsing:
    def test_using_declaration(self, tmp_path, store):
        src = _make_cpp_file(tmp_path, "main.cpp", """\
using namespace std;

int main() {
    return 0;
}
""")
        chunks = extract_chunks(src, Language.CPP, tmp_path)
        store.upsert_file(FileRecord(
            path="main.cpp", language=Language.CPP,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.cpp", chunks)

        rels = extract_relationships(src, Language.CPP, tmp_path, chunks, store)
        using = [r for r in rels if r.rel_type == RelType.IMPORTS]
        assert len(using) >= 1
        assert any("std" in r.target_name for r in using)


class TestCppIncludes:
    def test_include(self, tmp_path, store):
        src = _make_cpp_file(tmp_path, "main.cpp", """\
#include <vector>
#include "helper.h"

int main() {
    return 0;
}
""")
        chunks = extract_chunks(src, Language.CPP, tmp_path)
        store.upsert_file(FileRecord(
            path="main.cpp", language=Language.CPP,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("main.cpp", chunks)

        rels = extract_relationships(src, Language.CPP, tmp_path, chunks, store)
        includes = [r for r in rels if r.rel_type == RelType.INCLUDES]
        assert len(includes) >= 1
