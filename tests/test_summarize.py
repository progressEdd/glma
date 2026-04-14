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


class ContextLengthError(Exception):
    """Simulates an OpenAI-compatible context length error."""
    def __init__(self, msg: str = "Error code: 400 - context_length_exceeded"):
        super().__init__(msg)
        self.status_code = 400


class OversizedChunkProvider:
    """Provider that raises context-length error for chunks > threshold chars."""

    def __init__(self, threshold: int = 500, response_prefix: str = "Summary of"):
        self.calls: list[tuple[str, str]] = []
        self.threshold = threshold
        self.response_prefix = response_prefix

    def summarize(self, code: str, context: str) -> str:
        self.calls.append((code, context))
        if len(code) > self.threshold:
            raise ContextLengthError(
                f"Error code: 400 - The number of tokens exceeds the context length ({len(code)} chars)"
            )
        return f"{self.response_prefix}: {context.split(chr(10))[1] if chr(10) in context else 'chunk'}"


class TestIsContextLengthError:
    """Test the _is_context_length_error helper."""

    def test_detects_context_length(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(RuntimeError("context length exceeded")) is True

    def test_detects_n_ctx(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(RuntimeError("n_keep: 8312 >= n_ctx: 4096")) is True

    def test_detects_token_limit(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(RuntimeError("token limit exceeded")) is True

    def test_rejects_connection_error(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(ConnectionError("connection refused")) is False

    def test_rejects_generic_500(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(RuntimeError("internal server error")) is False


class TestExtractClassHeader:
    """Test the _extract_class_header helper."""

    def test_extracts_header_before_methods(self):
        from glma.summarize.pipeline import _extract_class_header
        content = "class Foo:\n    \"\"\"Docstring.\"\"\"\n    x = 1\n\n    def bar(self):\n        pass\n\n    def baz(self):\n        pass"
        header = _extract_class_header(content)
        assert "class Foo:" in header
        assert "Docstring" in header
        assert "x = 1" in header
        assert "def bar" not in header
        assert "def baz" not in header

    def test_handles_class_with_no_methods(self):
        from glma.summarize.pipeline import _extract_class_header
        content = "class Foo:\n    x = 1\n    y = 2"
        header = _extract_class_header(content)
        assert header == content

    def test_truncates_at_1500_chars(self):
        from glma.summarize.pipeline import _extract_class_header
        content = "class Foo:\n" + "    x = 1\n" * 200  # ~2000+ chars
        header = _extract_class_header(content)
        assert len(header) <= 1560  # 1500 + truncation marker


class TestMapReduceSummarize:
    """Test the _map_reduce_summarize helper."""

    def test_splits_and_combines(self):
        from glma.summarize.pipeline import _map_reduce_summarize
        provider = MockProvider()
        content = "x" * 300  # Small enough that each segment fits
        result = _map_reduce_summarize(content, "File: test.py", provider, segment_chars=200, overlap_chars=50)
        assert result  # Got a summary
        assert len(provider.calls) >= 2  # At least 2 segment calls + 1 combine

    def test_returns_empty_on_total_failure(self):
        from glma.summarize.pipeline import _map_reduce_summarize
        provider = FailingProvider()
        result = _map_reduce_summarize("some content", "context", provider)
        assert result == ""


class TestDecompositionIntegration:
    """Integration tests for the full decomposition pipeline in summarize_chunks."""

    def test_class_decomposition_on_context_error(
        self, store, sample_file_record
    ):
        """Oversized class chunk triggers class decomposition when method children exist."""
        store.upsert_file(sample_file_record)

        # Create a class chunk with oversized content
        class_content = "class BigClass:\n    \"\"\"A big class.\"\"\"\n" + "    x = 1\n" * 200
        class_chunk = Chunk(
            id="src/main.c::class::BigClass::5",
            file_path="src/main.c",
            chunk_type=ChunkType.CLASS,
            name="BigClass",
            content=class_content,
            summary=None,
            start_line=5,
            end_line=210,
            content_hash="class_hash",
            parent_id=None,
        )
        # Create method children (small, should summarize fine)
        method_chunk = Chunk(
            id="src/main.c::method::do_thing::10",
            file_path="src/main.c",
            chunk_type=ChunkType.METHOD,
            name="do_thing",
            content="def do_thing(self):\n    return 42",
            summary=None,
            start_line=10,
            end_line=11,
            content_hash="method_hash",
            parent_id="src/main.c::class::BigClass::5",
        )
        store.upsert_chunks("src/main.c", [class_chunk, method_chunk])

        # Provider that fails for large content, succeeds for small
        provider = OversizedChunkProvider(threshold=100)
        result = summarize_chunks(
            store, [class_chunk, method_chunk], provider, max_chunk_chars=100,
        )

        # Class chunk should have a summary via decomposition
        assert result[0].summary is not None
        # Method chunk should have a direct summary
        assert result[1].summary is not None

    def test_map_reduce_for_standalone_oversized(
        self, store, sample_file_record
    ):
        """Oversized standalone chunk (no children) triggers map-reduce."""
        store.upsert_file(sample_file_record)

        big_content = "def huge_function():\n" + "    x = 1\n" * 300
        big_chunk = Chunk(
            id="src/main.c::function::huge_function::5",
            file_path="src/main.c",
            chunk_type=ChunkType.FUNCTION,
            name="huge_function",
            content=big_content,
            summary=None,
            start_line=5,
            end_line=310,
            content_hash="big_hash",
            parent_id=None,
        )
        store.upsert_chunks("src/main.c", [big_chunk])

        # Provider fails for content > threshold, but map-reduce splits into
        # segments of ~2000 chars. Use threshold > 2000 so segments pass.
        provider = OversizedChunkProvider(threshold=2500)
        result = summarize_chunks(
            store, [big_chunk], provider, max_chunk_chars=100,
        )

        assert result[0].summary is not None

    def test_graceful_failure_when_decomposition_also_fails(
        self, store, sample_file_record
    ):
        """If both direct and decomposed summarization fail, chunk is skipped."""
        store.upsert_file(sample_file_record)

        big_chunk = Chunk(
            id="src/main.c::function::big::5",
            file_path="src/main.c",
            chunk_type=ChunkType.FUNCTION,
            name="big",
            content="x" * 1000,
            summary=None,
            start_line=5,
            end_line=10,
            content_hash="hash_big",
            parent_id=None,
        )
        store.upsert_chunks("src/main.c", [big_chunk])

        # Provider that always fails (even for small segments)
        provider = FailingProvider()
        result = summarize_chunks(
            store, [big_chunk], provider, max_chunk_chars=100,
        )

        assert result[0].summary is None  # Failed gracefully
        assert len(result) == 1  # Didn't crash

    def test_max_chunk_chars_default(self):
        """Verify default max_chunk_chars is 3000."""
        from glma.models import SummarizeConfig
        cfg = SummarizeConfig()
        assert cfg.max_chunk_chars == 3000

    def test_max_chunk_chars_from_config(self):
        """Verify max_chunk_chars loads from config dict."""
        from glma.models import SummarizeConfig
        cfg = SummarizeConfig(max_chunk_chars=5000)
        assert cfg.max_chunk_chars == 5000
