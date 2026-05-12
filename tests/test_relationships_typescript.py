"""Tests for TypeScript relationship extraction."""

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


def _make_ts_file(tmp_path, filename, content):
    src = tmp_path / filename
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(content)
    return src


class TestTsImports:
    def test_import_from_module(self, tmp_path, store):
        src = _make_ts_file(tmp_path, "app.ts", """\
import { User } from './user';
import type { Config } from './config';

function main(): void {}
""")
        chunks = extract_chunks(src, Language.TYPESCRIPT, tmp_path)
        store.upsert_file(FileRecord(
            path="app.ts", language=Language.TYPESCRIPT,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("app.ts", chunks)

        rels = extract_relationships(src, Language.TYPESCRIPT, tmp_path, chunks, store)
        imports = [r for r in rels if r.rel_type == RelType.IMPORTS]
        assert len(imports) >= 1
        import_targets = [r.target_name for r in imports]
        assert any("./user" in t for t in import_targets)


class TestTsCalls:
    def test_direct_call(self, tmp_path, store):
        src = _make_ts_file(tmp_path, "app.ts", """\
function helper(): number {
    return 42;
}

function main(): void {
    helper();
}
""")
        chunks = extract_chunks(src, Language.TYPESCRIPT, tmp_path)
        store.upsert_file(FileRecord(
            path="app.ts", language=Language.TYPESCRIPT,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("app.ts", chunks)

        rels = extract_relationships(src, Language.TYPESCRIPT, tmp_path, chunks, store)
        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        assert len(calls) >= 1
        assert any("helper" in r.target_name for r in calls)


class TestTsInheritance:
    def test_extends(self, tmp_path, store):
        src = _make_ts_file(tmp_path, "app.ts", """\
class Animal {
    speak(): string { return "..."; }
}

class Dog extends Animal {
    speak(): string { return "woof"; }
}
""")
        chunks = extract_chunks(src, Language.TYPESCRIPT, tmp_path)
        store.upsert_file(FileRecord(
            path="app.ts", language=Language.TYPESCRIPT,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("app.ts", chunks)

        rels = extract_relationships(src, Language.TYPESCRIPT, tmp_path, chunks, store)
        inherits = [r for r in rels if r.rel_type == RelType.INHERITS]
        assert len(inherits) >= 1
        assert any("Animal" in r.target_name for r in inherits)

    def test_implements(self, tmp_path, store):
        src = _make_ts_file(tmp_path, "app.ts", """\
interface Printable {
    print(): void;
}

class Report implements Printable {
    print(): void {}
}
""")
        chunks = extract_chunks(src, Language.TYPESCRIPT, tmp_path)
        store.upsert_file(FileRecord(
            path="app.ts", language=Language.TYPESCRIPT,
            content_hash="abc", last_indexed="2026-01-01T00:00:00",
            chunk_count=len(chunks),
        ))
        store.upsert_chunks("app.ts", chunks)

        rels = extract_relationships(src, Language.TYPESCRIPT, tmp_path, chunks, store)
        implements = [r for r in rels if r.rel_type == RelType.IMPLEMENTS]
        assert len(implements) >= 1
        assert any("Printable" in r.target_name for r in implements)


class TestTsxRelationships:
    def test_tsx_uses_same_extractor(self, tmp_path, store):
        src = _make_ts_file(tmp_path, "app.tsx", """\
function greet(name: string): string {
    return name;
}
""")
        chunks = extract_chunks(src, Language.TSX, tmp_path)
        assert len(chunks) >= 1
