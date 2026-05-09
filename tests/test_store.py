"""Tests for LadybugStore."""

import tempfile
from datetime import datetime, timezone
from pathlib import Path

import pytest

from glma.db.ladybug_store import LadybugStore
from glma.models import Chunk, ChunkType, FileRecord, Language


@pytest.fixture
def store(tmp_path):
    """Create a LadybugStore in a temp directory."""
    db_path = tmp_path / "db" / "test.lbug"
    s = LadybugStore(db_path)
    yield s
    s.close()


@pytest.fixture
def sample_file_record():
    return FileRecord(
        path="src/main.c",
        language=Language.C,
        content_hash="abc123",
        last_indexed=datetime.now(timezone.utc).isoformat(),
        chunk_count=2,
    )


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


class TestSchemaInit:
    """Test database initialization creates schema."""

    def test_creates_schema(self, store):
        """Schema creation should not raise errors."""
        # Re-initialize to verify IF NOT EXISTS works
        store._init_schema()

    def test_db_parent_directory_created(self, tmp_path):
        db_path = tmp_path / "new-dir" / "test.lbug"
        assert not db_path.parent.exists()
        s = LadybugStore(db_path)
        assert db_path.parent.exists()
        s.close()


class TestFileOperations:
    """Test file record insert and retrieval."""

    def test_insert_file(self, store, sample_file_record):
        store.upsert_file(sample_file_record)
        hash_val = store.get_file_hash("src/main.c")
        assert hash_val == "abc123"

    def test_upsert_replaces_file(self, store, sample_file_record):
        store.upsert_file(sample_file_record)
        updated = FileRecord(
            path="src/main.c",
            language=Language.C,
            content_hash="new_hash",
            last_indexed=datetime.now(timezone.utc).isoformat(),
            chunk_count=3,
        )
        store.upsert_file(updated)
        hash_val = store.get_file_hash("src/main.c")
        assert hash_val == "new_hash"

    def test_get_hash_unknown_file(self, store):
        result = store.get_file_hash("nonexistent.py")
        assert result is None

    def test_get_indexed_files(self, store, sample_file_record):
        store.upsert_file(sample_file_record)
        files = store.get_indexed_files()
        assert "src/main.c" in files
        assert files["src/main.c"] == "abc123"

    def test_get_indexed_files_empty(self, store):
        files = store.get_indexed_files()
        assert files == {}


class TestChunkOperations:
    """Test chunk insert and retrieval."""

    def test_insert_chunks(self, store, sample_file_record, sample_chunks):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)
        # Verify by checking file hash still exists
        assert store.get_file_hash("src/main.c") == "abc123"

    def test_upsert_replaces_chunks(self, store, sample_file_record, sample_chunks):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)
        # Replace with different chunks
        new_chunks = [
            Chunk(
                id="src/main.c::function::new_func::1",
                file_path="src/main.c",
                chunk_type=ChunkType.FUNCTION,
                name="new_func",
                content="void new_func() {}",
                summary=None,
                start_line=1,
                end_line=1,
                content_hash="new_hash",
                parent_id=None,
            ),
        ]
        store.upsert_chunks("src/main.c", new_chunks)
        # Should not raise


class TestDeleteOperations:
    """Test file and chunk deletion."""

    def test_delete_file(self, store, sample_file_record, sample_chunks):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)
        store.delete_file("src/main.c")
        assert store.get_file_hash("src/main.c") is None

    def test_delete_nonexistent_file(self, store):
        """Deleting a nonexistent file should not raise."""
        store.delete_file("nonexistent.py")


class TestEmbeddingFields:
    """Test embedding column schema, migration, and storage."""

    def test_embedding_columns_added_on_init(self, tmp_path):
        """Embedding columns should be added to existing Chunk table via migration."""
        # Create DB without embedding columns
        store = LadybugStore(tmp_path / "test.lbug")
        # Verify columns exist (would error on query if not)
        result = store.conn.execute("MATCH (c:Chunk) RETURN c.embedding IS NULL, c.summary_hash IS NULL, c.vector_dimensions IS NULL")
        rows = list(result)
        assert len(rows) == 0  # No chunks, but query succeeds = columns exist
        store.close()

    def test_update_chunk_embedding(self, tmp_path):
        """update_chunk_embedding should set embedding, summary_hash, and vector_dimensions."""
        store = LadybugStore(tmp_path / "test.lbug")
        # Insert a chunk first
        chunk = Chunk(id="test.py::function::foo::1", file_path="test.py", chunk_type=ChunkType.FUNCTION,
                      name="foo", content="def foo(): pass", summary="A test function",
                      start_line=1, end_line=1, content_hash="abc123")
        store.upsert_file(FileRecord(path="test.py", language=Language.PYTHON, content_hash="fhash",
                                     last_indexed="2026-01-01", chunk_count=1))
        store.upsert_chunks("test.py", [chunk])

        vec = [0.1] * 768
        store.update_chunk_embedding("test.py::function::foo::1", vec, "hash_val", 768)

        chunks = store.get_chunks_for_file("test.py")
        assert chunks[0].embedding is not None
        assert len(chunks[0].embedding) == 768
        assert chunks[0].summary_hash == "hash_val"
        assert chunks[0].vector_dimensions == 768
        store.close()

    def test_embedding_preserved_on_reindex(self, tmp_path):
        """Embedding data should survive re-indexing when content_hash unchanged."""
        store = LadybugStore(tmp_path / "test.lbug")
        # Index file, add summary, add embedding
        chunk1 = Chunk(id="test.py::function::foo::1", file_path="test.py", chunk_type=ChunkType.FUNCTION,
                       name="foo", content="def foo(): pass", summary="A function",
                       start_line=1, end_line=1, content_hash="hash1")
        store.upsert_file(FileRecord(path="test.py", language=Language.PYTHON, content_hash="fhash1",
                                     last_indexed="2026-01-01", chunk_count=1))
        store.upsert_chunks("test.py", [chunk1])
        store.update_chunk_summary("test.py::function::foo::1", "A great function")
        vec = [0.5] * 768
        store.update_chunk_embedding("test.py::function::foo::1", vec, "embed_hash", 768)

        # Re-index same file (same content_hash)
        chunk2 = Chunk(id="test.py::function::foo::1", file_path="test.py", chunk_type=ChunkType.FUNCTION,
                       name="foo", content="def foo(): pass", content_hash="hash1",
                       start_line=1, end_line=1)
        store.upsert_chunks("test.py", [chunk2])

        # Summary and embedding should be preserved
        chunks = store.get_chunks_for_file("test.py")
        assert chunks[0].summary is not None  # Preserved via summary_map
        assert chunks[0].embedding is not None  # Preserved via embedding_map
        assert chunks[0].summary_hash == "embed_hash"
        assert chunks[0].vector_dimensions == 768
        store.close()

    def test_get_chunks_needing_embedding(self, tmp_path):
        """Should return chunks with summaries but no embedding or stale embedding."""
        store = LadybugStore(tmp_path / "test.lbug")
        store.upsert_file(FileRecord(path="a.py", language=Language.PYTHON, content_hash="h1",
                                     last_indexed="2026-01-01", chunk_count=1))
        # Chunk with summary but no embedding → needs embedding
        c1 = Chunk(id="a.py::function::f::1", file_path="a.py", chunk_type=ChunkType.FUNCTION,
                   name="f", content="def f(): pass", summary="A function",
                   start_line=1, end_line=1, content_hash="ch1")
        store.upsert_chunks("a.py", [c1])
        # Embed it
        store.update_chunk_embedding("a.py::function::f::1", [0.1]*768, "hash_f", 768)
        # Now it should NOT need embedding (dims match, has embedding)
        needs = store.get_chunks_needing_embedding(768)
        assert len(needs) == 0
        # But with wrong dimensions → needs re-embedding
        needs = store.get_chunks_needing_embedding(384)
        assert len(needs) == 1
        assert needs[0].id == "a.py::function::f::1"
        store.close()
