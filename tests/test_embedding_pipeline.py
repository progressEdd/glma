"""Tests for embedding pipeline logic."""

import pytest
from unittest.mock import MagicMock

from glma.db.ladybug_store import LadybugStore
from glma.embedding.pipeline import (
    _compute_summary_hash,
    _batch_chunks_by_char_budget,
    embed_chunks,
    EmbeddingProgress,
    CHAR_BUDGET_PER_BATCH,
)
from glma.models import (
    Chunk, ChunkType, FileRecord, Language, SearchConfig,
)


@pytest.fixture
def store(tmp_path):
    """Create a LadybugStore with test data."""
    s = LadybugStore(tmp_path / "test.lbug")
    yield s
    s.close()


@pytest.fixture
def config():
    """Create a SearchConfig for testing."""
    return SearchConfig(
        enabled=True,
        vector_dimensions=768,
        embedding_provider="embed-local",
        embedding_model="test",
        embedding_base_url="http://localhost:1234/v1",
    )


def _make_chunk(id, file_path="test.py", summary="A test function", content_hash="hash1"):
    return Chunk(
        id=id, file_path=file_path, chunk_type=ChunkType.FUNCTION,
        name="func", content="def func(): pass", summary=summary,
        start_line=1, end_line=1, content_hash=content_hash,
    )


def _seed_chunks(store, chunks):
    """Insert chunks into the store with a file record."""
    file_paths = set(c.file_path for c in chunks)
    for fp in file_paths:
        store.upsert_file(FileRecord(
            path=fp, language=Language.PYTHON, content_hash="fhash",
            last_indexed="2026-01-01", chunk_count=len([c for c in chunks if c.file_path == fp]),
        ))
    for fp in file_paths:
        file_chunks = [c for c in chunks if c.file_path == fp]
        store.upsert_chunks(fp, file_chunks)


class TestSummaryHash:
    def test_deterministic(self):
        assert _compute_summary_hash("hello") == _compute_summary_hash("hello")

    def test_different_inputs_different_hashes(self):
        assert _compute_summary_hash("hello") != _compute_summary_hash("world")

    def test_empty_string(self):
        h = _compute_summary_hash("")
        assert isinstance(h, str) and len(h) > 0


class TestBatching:
    def test_single_batch_under_budget(self):
        chunks = [_make_chunk(f"c{i}", summary="short") for i in range(5)]
        batches = _batch_chunks_by_char_budget(chunks, char_budget=1000)
        assert len(batches) == 1
        assert len(batches[0]) == 5

    def test_splits_at_budget(self):
        chunks = [_make_chunk(f"c{i}", summary="x" * 100) for i in range(5)]
        batches = _batch_chunks_by_char_budget(chunks, char_budget=250)
        # 5 chunks × 100 chars each. Budget 250 → batches of 2, 2, 1
        assert len(batches) >= 2

    def test_empty_input(self):
        batches = _batch_chunks_by_char_budget([])
        assert batches == []


class TestEmbedChunks:
    def test_embeds_chunks_without_embedding(self, store, config):
        """Chunks with summaries but no embedding should be embedded."""
        chunks = [_make_chunk("c1"), _make_chunk("c2", content_hash="hash2")]
        _seed_chunks(store, chunks)

        provider = MagicMock()
        provider.embed.return_value = [[0.1] * 768, [0.5] * 768]

        result = embed_chunks(store, provider, config)
        assert result.embedded == 2
        assert result.failed == 0
        assert result.skipped == 0
        provider.embed.assert_called_once()

    def test_skips_already_embedded(self, store, config):
        """Chunks with matching embedding should be skipped."""
        chunks = [_make_chunk("c1")]
        _seed_chunks(store, chunks)
        # Embed it first
        store.update_chunk_embedding("c1", [0.1] * 768, _compute_summary_hash("A test function"), 768)

        provider = MagicMock()
        result = embed_chunks(store, provider, config)
        # Chunk is fully embedded → 0 candidates from DB → nothing to do
        assert result.embedded == 0
        assert result.total_chunks == 0
        provider.embed.assert_not_called()

    def test_force_re_embeds(self, store, config):
        """--force should re-embed even when hash matches."""
        chunks = [_make_chunk("c1")]
        _seed_chunks(store, chunks)
        store.update_chunk_embedding("c1", [0.1] * 768, _compute_summary_hash("A test function"), 768)

        provider = MagicMock()
        provider.embed.return_value = [[0.9] * 768]

        result = embed_chunks(store, provider, config, force=True)
        assert result.embedded == 1
        provider.embed.assert_called_once()

    def test_handles_batch_failure_gracefully(self, store, config):
        """Failed batches should be recorded, not crash the pipeline."""
        chunks = [_make_chunk(f"c{i}", content_hash=f"h{i}") for i in range(2)]
        _seed_chunks(store, chunks)

        provider = MagicMock()
        provider.embed.side_effect = RuntimeError("API error")

        result = embed_chunks(store, provider, config)
        assert result.failed == 2
        assert result.embedded == 0
        assert result.failed_chunk_ids == ["c0", "c1"]

    def test_empty_database(self, store, config):
        """No chunks in DB → nothing to embed."""
        provider = MagicMock()
        result = embed_chunks(store, provider, config)
        assert result.embedded == 0
        assert result.skipped == 0
        assert result.failed == 0

    def test_progress_callback_called(self, store, config):
        """Progress callback should be called after each batch."""
        chunks = [_make_chunk("c1")]
        _seed_chunks(store, chunks)

        provider = MagicMock()
        provider.embed.return_value = [[0.1] * 768]

        callback = MagicMock()
        embed_chunks(store, provider, config, progress_callback=callback)
        callback.assert_called()

    def test_dimension_mismatch_triggers_reembed(self, store):
        """Chunks with wrong dimensions should be re-embedded regardless of hash."""
        config_768 = SearchConfig(vector_dimensions=768, embedding_provider="embed-local")
        # Use a different dimension that won't actually be stored (just to verify detection)
        # Since FLOAT[768] is fixed in schema, we test that dim mismatch triggers re-embed
        # but the actual store will fail for non-768 dims. So we test the detection logic.
        config_384 = SearchConfig(vector_dimensions=384, embedding_provider="embed-local")

        chunks = [_make_chunk("c1")]
        _seed_chunks(store, chunks)

        # Embed with dims=768 (matches schema)
        provider = MagicMock()
        provider.embed.return_value = [[0.1] * 768]
        embed_chunks(store, provider, config_768)
        assert provider.embed.call_count == 1

        # Now change dims to 384 → should be detected as needing re-embed
        needs = store.get_chunks_needing_embedding(384)
        assert len(needs) == 1
        assert needs[0].id == "c1"
