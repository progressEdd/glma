"""Tests for summarization infrastructure — protocol, DB update, pipeline."""

import tempfile
from datetime import datetime, timezone
from pathlib import Path

import pytest

from glma.db.ladybug_store import LadybugStore
from glma.models import Chunk, ChunkType, FileRecord, Language
from glma.summarize.providers import SummarizerProvider
from glma.summarize.pipeline import summarize_chunks


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


class MockProvider:
    """Mock SummarizerProvider for testing."""

    def __init__(self, responses: dict[str, str] | None = None):
        self.calls: list[tuple[str, str]] = []
        self.responses = responses or {}

    def summarize(self, code: str, context: str) -> str:
        self.calls.append((code, context))
        # Return specific response if registered, else generic
        return self.responses.get(
            code,
            f"Summary of: {context.split(chr(10))[1] if chr(10) in context else 'chunk'}",
        )


class FailingProvider:
    """Provider that always raises an exception."""

    def summarize(self, code: str, context: str) -> str:
        raise RuntimeError("Provider unavailable")


class TestSummarizerProviderProtocol:
    """Verify the SummarizerProvider protocol works with duck typing."""

    def test_mock_satisfies_protocol(self):
        """MockProvider should satisfy SummarizerProvider without inheritance."""
        provider: SummarizerProvider = MockProvider()
        result = provider.summarize("def foo(): pass", "File: test.py")
        assert "Summary" in result

    def test_failing_provider_satisfies_protocol(self):
        """FailingProvider should satisfy SummarizerProvider protocol."""
        provider: SummarizerProvider = FailingProvider()
        with pytest.raises(RuntimeError):
            provider.summarize("code", "context")


class TestUpdateChunkSummary:
    """Test LadybugStore.update_chunk_summary()."""

    def test_update_summary(self, store, sample_file_record, sample_chunks):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)

        # Update summary for first chunk
        store.update_chunk_summary("src/main.c::function::add::5", "Adds two integers")

        # Verify summary was persisted
        chunks = store.get_chunks_for_file("src/main.c")
        assert chunks[0].summary == "Adds two integers"
        assert chunks[1].summary is None  # Unchanged

    def test_update_summary_overwrite(self, store, sample_file_record, sample_chunks):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)

        store.update_chunk_summary("src/main.c::function::add::5", "First summary")
        store.update_chunk_summary("src/main.c::function::add::5", "Updated summary")

        chunks = store.get_chunks_for_file("src/main.c")
        assert chunks[0].summary == "Updated summary"

    def test_update_summary_nonexistent_chunk(self, store, sample_file_record):
        """Updating a nonexistent chunk should not raise (Cypher SET is idempotent)."""
        store.upsert_file(sample_file_record)
        # This should not raise — MATCH finds nothing, SET does nothing
        store.update_chunk_summary("nonexistent::chunk::id::1", "Some summary")


class TestSummaryPreservation:
    """Test that upsert_chunks preserves summaries for unchanged content."""

    def test_preserves_summary_on_reindex(self, store, sample_file_record, sample_chunks):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)

        # Simulate AI summarization
        store.update_chunk_summary("src/main.c::function::add::5", "AI-generated summary")
        store.update_chunk_summary("src/main.c::function::main::10", "Another AI summary")

        # Re-index same file (same content, same hashes)
        store.upsert_chunks("src/main.c", sample_chunks)

        # Summaries should be preserved
        chunks = store.get_chunks_for_file("src/main.c")
        assert chunks[0].summary == "AI-generated summary"
        assert chunks[1].summary == "Another AI summary"

    def test_preserves_summary_when_content_changes_partially(
        self, store, sample_file_record, sample_chunks
    ):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)

        # Summarize both chunks
        store.update_chunk_summary("src/main.c::function::add::5", "Kept summary")
        store.update_chunk_summary("src/main.c::function::main::10", "Lost summary")

        # Re-index with one chunk changed (different content_hash)
        changed_chunks = [
            sample_chunks[0],  # Same content_hash — summary preserved
            Chunk(
                id="src/main.c::function::main::10",
                file_path="src/main.c",
                chunk_type=ChunkType.FUNCTION,
                name="main",
                content="int main() { return add(2, 3); }",  # Changed content
                summary=None,
                start_line=10,
                end_line=10,
                content_hash="new_hash2",  # Different hash
                parent_id=None,
            ),
        ]
        store.upsert_chunks("src/main.c", changed_chunks)

        chunks = store.get_chunks_for_file("src/main.c")
        assert chunks[0].summary == "Kept summary"  # Preserved — same content_hash
        assert chunks[1].summary is None  # Lost — different content_hash


class TestSummarizeChunksPipeline:
    """Test the summarize_chunks() pipeline function."""

    def test_summarize_unsummarized_chunks(
        self, store, sample_file_record, sample_chunks
    ):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)

        provider = MockProvider()
        result = summarize_chunks(store, sample_chunks, provider)

        assert len(result) == 2
        assert result[0].summary is not None
        assert result[1].summary is not None
        assert provider.calls  # Provider was called

    def test_skip_already_summarized(self, store, sample_file_record, sample_chunks):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)

        # Pre-summarize first chunk
        store.update_chunk_summary("src/main.c::function::add::5", "Existing summary")
        sample_chunks[0].summary = "Existing summary"

        provider = MockProvider()
        result = summarize_chunks(store, sample_chunks, provider)

        # First chunk should be skipped (already has summary)
        assert result[0].summary == "Existing summary"
        assert len(provider.calls) == 1  # Only second chunk was processed

    def test_handles_provider_failure_gracefully(
        self, store, sample_file_record, sample_chunks
    ):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)

        provider = FailingProvider()
        # Should not raise — failed chunks are skipped
        result = summarize_chunks(store, sample_chunks, provider)

        assert len(result) == 2
        assert result[0].summary is None  # Failed — no summary
        assert result[1].summary is None  # Failed — no summary

    def test_persists_summaries_to_db(self, store, sample_file_record, sample_chunks):
        store.upsert_file(sample_file_record)
        store.upsert_chunks("src/main.c", sample_chunks)

        provider = MockProvider()
        summarize_chunks(store, sample_chunks, provider)

        # Verify summaries were written to DB (not just in-memory)
        db_chunks = store.get_chunks_for_file("src/main.c")
        assert db_chunks[0].summary is not None
        assert db_chunks[1].summary is not None

    def test_empty_chunk_list(self, store):
        provider = MockProvider()
        result = summarize_chunks(store, [], provider)
        assert result == []
        assert len(provider.calls) == 0
