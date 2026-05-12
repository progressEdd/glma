"""Tests for LadybugStore relationship CRUD."""

from datetime import datetime, timezone

import pytest

from glma.db.ladybug_store import LadybugStore
from glma.models import Chunk, ChunkType, FileRecord, Language, Relationship, RelType, Confidence


@pytest.fixture
def store(tmp_path):
    """Create a LadybugStore in a temp directory."""
    db_path = tmp_path / "db" / "test.lbug"
    s = LadybugStore(db_path)
    yield s
    s.close()


@pytest.fixture
def sample_chunks():
    return [
        Chunk(
            id="src/main.c::function::add::5",
            file_path="src/main.c",
            chunk_type=ChunkType.FUNCTION,
            name="add",
            content="int add(int a, int b) { return a + b; }",
            summary=None,
            start_line=5,
            end_line=5,
            content_hash="hash1",
            parent_id=None,
        ),
        Chunk(
            id="src/main.c::function::main::10",
            file_path="src/main.c",
            chunk_type=ChunkType.FUNCTION,
            name="main",
            content="int main() { return add(1, 2); }",
            summary=None,
            start_line=10,
            end_line=10,
            content_hash="hash2",
            parent_id=None,
        ),
    ]


def _setup_file_with_chunks(store, chunks, file_path="src/main.c"):
    """Helper: create a file record and chunks in the store."""
    store.upsert_file(FileRecord(
        path=file_path,
        language=Language.C,
        content_hash="abc123",
        last_indexed=datetime.now(timezone.utc).isoformat(),
        chunk_count=len(chunks),
    ))
    store.upsert_chunks(file_path, chunks)


class TestCreateAndQueryRelationships:
    """Test creating and querying relationships."""

    def test_create_and_query_relationships(self, store, sample_chunks):
        _setup_file_with_chunks(store, sample_chunks)

        rel = Relationship(
            source_id="src/main.c::function::main::10",
            target_id="src/main.c::function::add::5",
            target_name="add",
            rel_type=RelType.CALLS,
            confidence=Confidence.DIRECT,
            source_line=10,
        )
        store.upsert_relationships("src/main.c", [rel])

        # Query outgoing from main
        outgoing = store.get_outgoing_relationships("src/main.c::function::main::10")
        assert len(outgoing) == 1
        assert outgoing[0]["rel_type"] == "calls"
        assert outgoing[0]["confidence"] == "DIRECT"
        assert outgoing[0]["target_name"] == "add"

        # Query incoming to add
        incoming = store.get_incoming_relationships("src/main.c::function::add::5")
        assert len(incoming) == 1
        assert incoming[0]["source_chunk_name"] == "main"


class TestUpsertReplacesRelationships:
    """Test that upsert replaces existing relationships."""

    def test_upsert_replaces_relationships(self, store, sample_chunks):
        _setup_file_with_chunks(store, sample_chunks)

        rel1 = Relationship(
            source_id="src/main.c::function::main::10",
            target_id="src/main.c::function::add::5",
            target_name="add",
            rel_type=RelType.CALLS,
            confidence=Confidence.DIRECT,
            source_line=10,
        )
        store.upsert_relationships("src/main.c", [rel1])

        # Now upsert new relationships (should delete old ones)
        rel2 = Relationship(
            source_id="src/main.c::function::main::10",
            target_id="",
            target_name="new_func",
            rel_type=RelType.CALLS,
            confidence=Confidence.INFERRED,
            source_line=11,
        )
        store.upsert_relationships("src/main.c", [rel2])

        outgoing = store.get_outgoing_relationships("src/main.c::function::main::10")
        assert len(outgoing) == 1
        assert outgoing[0]["target_name"] == "new_func"


class TestDeleteRelationships:
    """Test deleting relationships for a file."""

    def test_delete_relationships(self, store, sample_chunks):
        _setup_file_with_chunks(store, sample_chunks)

        rel = Relationship(
            source_id="src/main.c::function::main::10",
            target_id="src/main.c::function::add::5",
            target_name="add",
            rel_type=RelType.CALLS,
            confidence=Confidence.DIRECT,
            source_line=10,
        )
        store.upsert_relationships("src/main.c", [rel])

        store.delete_relationships("src/main.c")

        outgoing = store.get_outgoing_relationships("src/main.c::function::main::10")
        assert len(outgoing) == 0


class TestUnresolvedTarget:
    """Test storing relationships with unresolved targets."""

    def test_unresolved_target(self, store, sample_chunks):
        _setup_file_with_chunks(store, sample_chunks)

        rel = Relationship(
            source_id="src/main.c::function::main::10",
            target_id="",
            target_name="unknown_func",
            rel_type=RelType.CALLS,
            confidence=Confidence.INFERRED,
            source_line=10,
        )
        store.upsert_relationships("src/main.c", [rel])

        # Should still be queryable
        outgoing = store.get_outgoing_relationships("src/main.c::function::main::10")
        assert len(outgoing) == 1
        assert outgoing[0]["target_name"] == "unknown_func"


class TestGetFileRelationships:
    """Test getting all relationships for a file."""

    def test_get_file_relationships(self, store, sample_chunks):
        _setup_file_with_chunks(store, sample_chunks)

        rel1 = Relationship(
            source_id="src/main.c::function::main::10",
            target_id="src/main.c::function::add::5",
            target_name="add",
            rel_type=RelType.CALLS,
            confidence=Confidence.DIRECT,
            source_line=10,
        )
        rel2 = Relationship(
            source_id="src/main.c::function::main::10",
            target_id="",
            target_name="printf",
            rel_type=RelType.CALLS,
            confidence=Confidence.INFERRED,
            source_line=11,
        )
        store.upsert_relationships("src/main.c", [rel1, rel2])

        file_rels = store.get_file_relationships("src/main.c")
        assert len(file_rels) == 2
        names = {r["target_name"] for r in file_rels}
        assert "add" in names
        assert "printf" in names
