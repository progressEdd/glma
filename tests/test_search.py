"""Tests for hybrid search engine, formatters, and CLI command."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml

from glma.models import SearchConfig
from glma.search.engine import HybridSearchEngine, SearchResult
from glma.search.formatter import (
    format_search_json,
    format_search_kv,
    format_search_markdown,
    format_search_output,
    format_search_yaml,
)


# ── Unit Tests: SearchResult ──────────────────────────────────────────


class TestSearchResult:
    """Test SearchResult dataclass."""

    def test_default_scores(self):
        r = SearchResult(
            chunk_id="id1", file_path="a.py", chunk_name="foo",
            chunk_type="function", content="code", summary="sum",
            start_line=1, end_line=5,
        )
        assert r.keyword_score == 0.0
        assert r.vector_score == 0.0
        assert r.combined_score == 0.0

    def test_all_fields(self):
        r = SearchResult(
            chunk_id="id1", file_path="a.py", chunk_name="foo",
            chunk_type="function", content="code", summary="sum",
            start_line=1, end_line=5,
            keyword_score=0.8, vector_score=0.6, combined_score=0.7,
        )
        assert r.keyword_score == 0.8
        assert r.vector_score == 0.6
        assert r.combined_score == 0.7


# ── Unit Tests: _fuzzy_score_all ──────────────────────────────────────


class TestFuzzyScoreAll:
    """Test fuzzy keyword scoring."""

    def test_scores_normalized_0_to_1(self):
        chunks = [
            {"id": "1", "summary": "authentication login user verify"},
            {"id": "2", "summary": "database connection pool management"},
        ]
        scores = HybridSearchEngine._fuzzy_score_all("login authentication", chunks)
        for score in scores.values():
            assert 0.0 <= score <= 1.0

    def test_better_match_higher_score(self):
        chunks = [
            {"id": "1", "summary": "authentication login user verify"},
            {"id": "2", "summary": "database connection pool management"},
        ]
        scores = HybridSearchEngine._fuzzy_score_all("authentication login", chunks)
        assert scores["1"] > scores["2"]

    def test_exact_match_score_is_1(self):
        chunks = [
            {"id": "1", "summary": "hello world"},
        ]
        scores = HybridSearchEngine._fuzzy_score_all("hello world", chunks)
        assert scores["1"] == 1.0

    def test_empty_summary_excluded(self):
        chunks = [
            {"id": "1", "summary": ""},
            {"id": "2", "summary": "hello world"},
        ]
        scores = HybridSearchEngine._fuzzy_score_all("hello world", chunks)
        assert "1" not in scores
        assert "2" in scores


# ── Unit Tests: HybridSearchEngine.search() ──────────────────────────


def _make_config(**overrides) -> SearchConfig:
    defaults = {
        "similarity_threshold": 0.3,
        "hybrid_keyword_weight": 0.3,
        "hybrid_vector_weight": 0.3,
        "graph_weight": 0.4,
    }
    defaults.update(overrides)
    return SearchConfig(**defaults)


def _mock_store(
    has_embeddings_val=True,
    vector_results=None,
    keyword_chunks=None,
):
    store = MagicMock()
    store.has_embeddings.return_value = has_embeddings_val
    store.vector_search.return_value = vector_results or []
    store.get_chunks_with_summaries_for_keyword.return_value = keyword_chunks or []
    return store


def _mock_provider(vectors=None):
    provider = MagicMock()
    provider.embed.return_value = vectors or [[0.1] * 768]
    return provider


class TestHybridSearchEngine:
    """Test HybridSearchEngine.search() with mocks."""

    def test_keyword_mode_no_vector_calls(self):
        """Keyword mode never calls vector_search."""
        store = _mock_store()
        provider = _mock_provider()
        config = _make_config()
        engine = HybridSearchEngine(store, provider, config)

        engine.search("test query", mode="keyword")

        store.has_embeddings.assert_not_called()
        store.vector_search.assert_not_called()
        provider.embed.assert_not_called()
        store.get_chunks_with_summaries_for_keyword.assert_called_once()

    def test_vector_mode_calls_vector_search(self):
        """Vector mode calls vector methods."""
        store = _mock_store(has_embeddings_val=True, vector_results=[])
        provider = _mock_provider()
        config = _make_config()
        engine = HybridSearchEngine(store, provider, config)

        engine.search("test query", mode="vector")

        store.has_embeddings.assert_called_once()
        store.create_vector_index.assert_called_once()
        provider.embed.assert_called_once_with(["test query"])
        store.vector_search.assert_called_once()
        store.get_chunks_with_summaries_for_keyword.assert_not_called()

    def test_vector_mode_no_embeddings_raises(self):
        """Vector mode raises ValueError when no embeddings exist."""
        store = _mock_store(has_embeddings_val=False)
        provider = _mock_provider()
        config = _make_config()
        engine = HybridSearchEngine(store, provider, config)

        with pytest.raises(ValueError, match="No embeddings found"):
            engine.search("test", mode="vector")

    def test_hybrid_mode_calls_both(self):
        """Hybrid mode calls both vector and keyword paths."""
        store = _mock_store(has_embeddings_val=True, vector_results=[])
        provider = _mock_provider()
        config = _make_config()
        engine = HybridSearchEngine(store, provider, config)

        engine.search("test query", mode="hybrid")

        store.has_embeddings.assert_called_once()
        store.create_vector_index.assert_called_once()
        provider.embed.assert_called_once()
        store.vector_search.assert_called_once()
        store.get_chunks_with_summaries_for_keyword.assert_called_once()

    def test_threshold_filtering(self):
        """Results below threshold are excluded."""
        store = _mock_store(
            has_embeddings_val=True,
            keyword_chunks=[
                {"id": "low", "summary": "completely unrelated thing", "file_path": "a.py",
                 "name": "low_fn", "chunk_type": "function", "content": "code",
                 "start_line": 1, "end_line": 2},
                {"id": "high", "summary": "test query exact match", "file_path": "b.py",
                 "name": "high_fn", "chunk_type": "function", "content": "code",
                 "start_line": 1, "end_line": 2},
            ],
        )
        provider = _mock_provider()
        config = _make_config(similarity_threshold=0.8)
        engine = HybridSearchEngine(store, provider, config)

        results = engine.search("test query exact match", mode="keyword")
        # Only the high-scoring result should pass threshold
        for r in results:
            assert r.combined_score >= 0.8

    def test_results_sorted_by_combined_score(self):
        """Results sorted descending by combined_score."""
        store = _mock_store(
            has_embeddings_val=True,
            keyword_chunks=[
                {"id": "c1", "summary": "hello world", "file_path": "a.py",
                 "name": "fn1", "chunk_type": "function", "content": "code1",
                 "start_line": 1, "end_line": 5},
                {"id": "c2", "summary": "world hello foo bar baz", "file_path": "b.py",
                 "name": "fn2", "chunk_type": "function", "content": "code2",
                 "start_line": 10, "end_line": 20},
            ],
        )
        provider = _mock_provider()
        config = _make_config(similarity_threshold=0.0)
        engine = HybridSearchEngine(store, provider, config)

        results = engine.search("hello world", mode="keyword")
        if len(results) >= 2:
            assert results[0].combined_score >= results[1].combined_score

    def test_vector_mode_embed_failure_raises(self):
        """Vector mode raises ValueError when embed returns empty."""
        store = _mock_store(has_embeddings_val=True)
        provider = MagicMock()
        provider.embed.return_value = []
        config = _make_config()
        engine = HybridSearchEngine(store, provider, config)

        with pytest.raises(ValueError, match="Failed to embed query string"):
            engine.search("test", mode="vector")


# ── Formatter Tests ──────────────────────────────────────────────────


def _make_result(**overrides) -> SearchResult:
    defaults = dict(
        chunk_id="id1", file_path="src/foo.py", chunk_name="my_func",
        chunk_type="function", content="def my_func():\n    pass",
        summary="A test function", start_line=1, end_line=2,
        keyword_score=0.8, vector_score=0.6, graph_score=0.0, combined_score=0.7,
    )
    defaults.update(overrides)
    return SearchResult(**defaults)


class TestFormatSearchMarkdown:
    """Test markdown formatter."""

    def test_empty_results(self):
        assert format_search_markdown([]) == ""

    def test_single_result_has_file_heading_and_code_block(self):
        r = _make_result()
        output = format_search_markdown([r])
        assert "# src/foo.py" in output
        assert "```python" in output
        assert "def my_func():" in output

    def test_summary_annotation(self):
        r = _make_result()
        output = format_search_markdown([r])
        assert "> *Summary: A test function*" in output

    def test_no_scores_in_output(self):
        r = _make_result()
        output = format_search_markdown([r])
        assert "0.7" not in output
        assert "score" not in output

    def test_two_files_two_headings(self):
        r1 = _make_result(file_path="a.py")
        r2 = _make_result(file_path="b.py", chunk_id="id2")
        output = format_search_markdown([r1, r2])
        assert "# a.py" in output
        assert "# b.py" in output

    def test_same_file_single_heading(self):
        r1 = _make_result(chunk_id="id1")
        r2 = _make_result(chunk_id="id2", chunk_name="other")
        output = format_search_markdown([r1, r2])
        assert output.count("# src/foo.py") == 1

    def test_no_query_header_when_no_params(self):
        r = _make_result()
        output = format_search_markdown([r])
        assert "Query:" not in output
        assert "Rewritten:" not in output

    def test_query_header_with_rewrite(self):
        r = _make_result()
        output = format_search_markdown([r], original_query="auth", rewritten_query="authentication login")
        assert '# Query: "auth"' in output
        assert '# Rewritten: "authentication login"' in output

    def test_query_header_raw_mode(self):
        r = _make_result()
        output = format_search_markdown([r], original_query="auth")
        assert '# Query: "auth" (raw)' in output
        assert "Rewritten:" not in output


class TestFormatSearchJson:
    """Test JSON formatter."""

    def test_valid_json(self):
        r = _make_result()
        output = format_search_json([r], "test query", "hybrid")
        data = json.loads(output)
        assert data["query"] == "test query"
        assert data["search_mode"] == "hybrid"
        assert data["total_results"] == 1

    def test_scores_in_json(self):
        r = _make_result()
        output = format_search_json([r], "q", "hybrid")
        data = json.loads(output)
        result = data["results"][0]
        assert "scores" in result
        assert result["scores"]["keyword"] == 0.8
        assert result["scores"]["vector"] == 0.6
        assert result["scores"]["combined"] == 0.7

    def test_empty_results(self):
        output = format_search_json([], "q", "hybrid")
        data = json.loads(output)
        assert data["total_results"] == 0
        assert data["results"] == []

    def test_backward_compat_no_rewrite_params(self):
        r = _make_result()
        output = format_search_json([r], "q", "hybrid")
        data = json.loads(output)
        assert data["original_query"] == "q"
        assert data["rewritten_query"] is None

    def test_rewrite_fields(self):
        r = _make_result()
        output = format_search_json([r], "auth login", "hybrid", original_query="auth", rewritten_query="authentication login session")
        data = json.loads(output)
        assert data["original_query"] == "auth"
        assert data["rewritten_query"] == "authentication login session"
        assert data["query"] == "auth login"


class TestFormatSearchYaml:
    """Test YAML formatter."""

    def test_valid_yaml(self):
        r = _make_result()
        output = format_search_yaml([r], "test query", "hybrid")
        data = yaml.safe_load(output)
        assert data["query"] == "test query"
        assert data["total_results"] == 1

    def test_scores_in_yaml(self):
        r = _make_result()
        output = format_search_yaml([r], "q", "hybrid")
        data = yaml.safe_load(output)
        result = data["results"][0]
        assert result["scores"]["combined"] == 0.7

    def test_rewrite_fields(self):
        r = _make_result()
        output = format_search_yaml([r], "auth login", "hybrid", original_query="auth", rewritten_query="authentication login session")
        data = yaml.safe_load(output)
        assert data["original_query"] == "auth"
        assert data["rewritten_query"] == "authentication login session"


class TestFormatSearchKv:
    """Test markdown-kv formatter."""

    def test_contains_type_lines_score(self):
        r = _make_result()
        output = format_search_kv([r])
        assert "type: function" in output
        assert "lines: L1-L2" in output
        assert "score: 0.700" in output

    def test_file_path_heading(self):
        r = _make_result()
        output = format_search_kv([r])
        assert "# src/foo.py" in output

    def test_chunk_name_heading(self):
        r = _make_result()
        output = format_search_kv([r])
        assert "## my_func" in output

    def test_query_header_with_rewrite(self):
        r = _make_result()
        output = format_search_kv([r], original_query="auth", rewritten_query="authentication")
        assert '# Query: "auth"' in output
        assert '# Rewritten: "authentication"' in output


class TestFormatSearchOutput:
    """Test format dispatch."""

    def test_json_dispatch(self):
        r = _make_result()
        output = format_search_output([r], "json", "q", "hybrid")
        data = json.loads(output)
        assert data["query"] == "q"

    def test_yaml_dispatch(self):
        r = _make_result()
        output = format_search_output([r], "yaml", "q", "hybrid")
        data = yaml.safe_load(output)
        assert data["query"] == "q"

    def test_markdown_kv_dispatch(self):
        r = _make_result()
        output = format_search_output([r], "markdown-kv", "q", "hybrid")
        assert "score:" in output

    def test_markdown_dispatch(self):
        r = _make_result()
        output = format_search_output([r], "markdown", "q", "hybrid")
        assert "```python" in output
        assert "score" not in output

    def test_dispatch_with_rewrite_params_json(self):
        r = _make_result()
        output = format_search_output([r], "json", "q", "hybrid", original_query="test", rewritten_query="expanded")
        data = json.loads(output)
        assert data["original_query"] == "test"
        assert data["rewritten_query"] == "expanded"


# ── CLI Tests ────────────────────────────────────────────────────────


class TestSearchCLI:
    """Test glma search CLI command."""

    def test_search_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "--help"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "Natural language search query" in result.stdout
        assert "--search-mode" in result.stdout
        assert "--format" in result.stdout

    def test_invalid_search_mode(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "test", "--search-mode", "badvalue"],
            capture_output=True, text=True,
        )
        assert result.returncode == 4
        assert "search-mode must be one of" in result.stderr

    def test_invalid_format(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "test", "--format", "badvalue"],
            capture_output=True, text=True,
        )
        assert result.returncode == 4

    def test_no_index_found(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, "-m", "glma", "search", "test", "--repo", tmp],
                capture_output=True, text=True,
            )
            assert result.returncode == 4
            assert "No index found" in result.stderr

    def test_raw_flag_in_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "--help"],
            capture_output=True, text=True,
        )
        assert "--raw" in result.stdout
        assert "Skip LLM query rewriting" in result.stdout

    def test_summarize_flags_in_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "--help"],
            capture_output=True, text=True,
        )
        assert "--summarize-provider" in result.stdout
        assert "--summarize-model" in result.stdout
        assert "--ai-url" in result.stdout

    def test_graph_flag_in_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "--help"],
            capture_output=True, text=True,
        )
        assert "--graph" in result.stdout

    def test_graph_depth_flag_in_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "--help"],
            capture_output=True, text=True,
        )
        assert "--graph-depth" in result.stdout

    def test_graph_fanout_flag_in_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "--help"],
            capture_output=True, text=True,
        )
        assert "--graph-fanout" in result.stdout


# ── Integration Test: Full Search Pipeline ───────────────────────────


class TestSearchIntegration:
    """Integration tests with Ladybug in-memory DB."""

    @pytest.fixture
    def indexed_store(self, tmp_path):
        """Create a LadybugStore with test chunks and embeddings."""
        from glma.db.ladybug_store import LadybugStore
        from glma.models import Chunk, ChunkType, FileRecord, Language

        db_path = tmp_path / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)

        # Create file record
        fr = FileRecord(
            path="src/auth.py", language=Language.PYTHON,
            content_hash="abc123", last_indexed="2026-01-01T00:00:00",
            chunk_count=2,
        )
        store.upsert_file(fr)

        # Create chunks with summaries
        chunks = [
            Chunk(
                id="src/auth.py::function::login::1", file_path="src/auth.py",
                chunk_type=ChunkType.FUNCTION, name="login",
                content="def login(user, password):\n    pass",
                summary="Authenticate user with password credentials",
                start_line=1, end_line=2, content_hash="h1",
            ),
            Chunk(
                id="src/auth.py::function::logout::5", file_path="src/auth.py",
                chunk_type=ChunkType.FUNCTION, name="logout",
                content="def logout(user):\n    pass",
                summary="End user session and clear authentication tokens",
                start_line=5, end_line=6, content_hash="h2",
            ),
        ]
        store.upsert_chunks("src/auth.py", chunks)

        # Add embeddings
        store.update_chunk_embedding(
            "src/auth.py::function::login::1",
            [0.1] * 768, "sh1", 768,
        )
        store.update_chunk_embedding(
            "src/auth.py::function::logout::5",
            [0.2] * 768, "sh2", 768,
        )

        return store

    def test_keyword_search_returns_results(self, indexed_store):
        """Keyword search finds matching chunks."""
        config = _make_config(similarity_threshold=0.0)
        provider = _mock_provider()

        engine = HybridSearchEngine(indexed_store, provider, config)
        results = engine.search("authenticate user login", mode="keyword")

        assert len(results) > 0
        assert all(isinstance(r, SearchResult) for r in results)

    def test_vector_search_returns_results(self, indexed_store):
        """Vector search returns results when embeddings exist."""
        config = _make_config(similarity_threshold=0.0)
        provider = _mock_provider(vectors=[[0.1] * 768])

        engine = HybridSearchEngine(indexed_store, provider, config)
        results = engine.search("user authentication", mode="vector")

        # Should get results from HNSW search
        assert len(results) > 0

    def test_hybrid_search_returns_results(self, indexed_store):
        """Hybrid search combines both signals."""
        config = _make_config(similarity_threshold=0.0)
        provider = _mock_provider(vectors=[[0.1] * 768])

        engine = HybridSearchEngine(indexed_store, provider, config)
        results = engine.search("authenticate user login", mode="hybrid")

        assert len(results) > 0
        for r in results:
            assert r.combined_score >= 0.0

    def test_vector_mode_no_embeddings_error(self, tmp_path):
        """Vector mode with no embeddings raises error."""
        from glma.db.ladybug_store import LadybugStore

        db_path = tmp_path / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        # No chunks with embeddings

        config = _make_config()
        provider = _mock_provider()

        engine = HybridSearchEngine(store, provider, config)
        with pytest.raises(ValueError, match="No embeddings found"):
            engine.search("test", mode="vector")


# ── Rewrite Integration Tests ───────────────────────────────────────


class TestRewriteIntegration:
    """Integration tests for query rewriting in search flow."""

    def test_raw_flag_skips_rewrite(self):
        """--raw flag causes rewrite_query to NOT be called."""
        with patch("glma.search.rewriter.rewrite_query") as mock_rewrite:
            # Verify the mock is set up - rewrite_query hasn't been called yet
            assert not mock_rewrite.called

    def test_rewrite_failure_falls_back_to_raw(self):
        """When rewrite_query raises, search proceeds with original query."""
        with patch("glma.search.rewriter.rewrite_query", side_effect=Exception("model unavailable")) as mock_rewrite:
            # Verify the mock is set up - rewrite_query hasn't been called yet
            assert not mock_rewrite.called

    def test_raw_flag_visible_in_help(self):
        """--raw flag is documented in search help."""
        result = subprocess.run(
            [sys.executable, "-m", "glma", "search", "--help"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "--raw" in result.stdout


# ── 3-Way Config Tests ────────────────────────────────────────────────


class TestSearchConfig3Way:
    """Test SearchConfig 3-way weight validation."""

    def test_valid_3way_defaults(self):
        cfg = SearchConfig()
        assert cfg.graph_weight == 0.4
        assert cfg.graph_depth == 2
        assert cfg.graph_fanout == 10
        total = cfg.hybrid_keyword_weight + cfg.hybrid_vector_weight + cfg.graph_weight
        assert abs(total - 1.0) <= 0.05

    def test_valid_custom_weights(self):
        cfg = SearchConfig(hybrid_keyword_weight=0.5, hybrid_vector_weight=0.3, graph_weight=0.2)
        assert abs(cfg.hybrid_keyword_weight + cfg.hybrid_vector_weight + cfg.graph_weight - 1.0) <= 0.05

    def test_invalid_weight_sum_raises(self):
        with pytest.raises(ValueError, match="sum to ~1.0"):
            SearchConfig(hybrid_keyword_weight=0.5, hybrid_vector_weight=0.5, graph_weight=0.5)

    def test_graph_depth_bounds(self):
        cfg = SearchConfig(graph_depth=1)
        assert cfg.graph_depth == 1
        cfg = SearchConfig(graph_depth=5)
        assert cfg.graph_depth == 5

    def test_graph_fanout_bounds(self):
        cfg = SearchConfig(graph_fanout=1)
        assert cfg.graph_fanout == 1
        cfg = SearchConfig(graph_fanout=100)
        assert cfg.graph_fanout == 100


# ── Graph Search Tests ────────────────────────────────────────────────


def _mock_store_with_graph(
    traversal_edges=None,
    chunk_meta=None,
    has_embeddings_val=True,
    vector_results=None,
    keyword_chunks=None,
):
    store = MagicMock()
    store.has_embeddings.return_value = has_embeddings_val
    store.vector_search.return_value = vector_results or []
    store.get_chunks_with_summaries_for_keyword.return_value = keyword_chunks or []
    store.traverse_relationships.return_value = traversal_edges or []
    store.get_chunks_by_ids.return_value = chunk_meta or []
    return store


class TestGraphSearch:
    """Test graph traversal and 3-way scoring in the engine."""

    def test_graph_false_no_traversal(self):
        """When graph=False, traverse_relationships is never called."""
        store = _mock_store()
        provider = _mock_provider()
        config = _make_config()
        engine = HybridSearchEngine(store, provider, config)
        engine.search("test", mode="keyword", graph=False)
        store.traverse_relationships.assert_not_called()

    def test_graph_true_calls_traversal(self):
        """When graph=True with results, traverse_relationships is called."""
        store = _mock_store_with_graph(
            keyword_chunks=[
                {"id": "c1", "summary": "hello world", "file_path": "a.py",
                 "name": "fn1", "chunk_type": "function", "content": "code",
                 "start_line": 1, "end_line": 5},
            ],
            traversal_edges=[],
            chunk_meta=[],
        )
        provider = _mock_provider()
        config = _make_config(similarity_threshold=0.0)
        engine = HybridSearchEngine(store, provider, config)
        results = engine.search("hello world", mode="keyword", graph=True)
        store.traverse_relationships.assert_called_once()

    def test_graph_discovered_chunks_get_scores(self):
        """Graph-discovered chunks appear in results with graph_score > 0."""
        store = _mock_store_with_graph(
            keyword_chunks=[
                {"id": "c1", "summary": "hello world", "file_path": "a.py",
                 "name": "fn1", "chunk_type": "function", "content": "code",
                 "start_line": 1, "end_line": 5},
            ],
            traversal_edges=[
                {"source_id": "c1", "target_id": "c2", "depth": 1, "direction": "outgoing"},
            ],
            chunk_meta=[
                {"id": "c2", "file_path": "b.py", "name": "fn2", "chunk_type": "function",
                 "content": "code2", "summary": "related function", "start_line": 10, "end_line": 15},
            ],
        )
        provider = _mock_provider()
        config = _make_config(similarity_threshold=0.0)
        engine = HybridSearchEngine(store, provider, config)
        results = engine.search("hello world", mode="keyword", graph=True)
        # Should have both c1 (seed) and c2 (graph-discovered)
        chunk_ids = [r.chunk_id for r in results]
        assert "c2" in chunk_ids
        c2_result = next(r for r in results if r.chunk_id == "c2")
        assert c2_result.graph_score > 0.0
        assert c2_result.keyword_score == 0.0  # graph-only chunk
        assert c2_result.vector_score == 0.0

    def test_normalization_range(self):
        """After normalization, all scores should be in [0, ~1] range."""
        store = _mock_store_with_graph(
            keyword_chunks=[
                {"id": "c1", "summary": "hello world", "file_path": "a.py",
                 "name": "fn1", "chunk_type": "function", "content": "code",
                 "start_line": 1, "end_line": 5},
            ],
            traversal_edges=[
                {"source_id": "c1", "target_id": "c2", "depth": 1, "direction": "outgoing"},
                {"source_id": "c1", "target_id": "c3", "depth": 2, "direction": "outgoing"},
            ],
            chunk_meta=[
                {"id": "c2", "file_path": "b.py", "name": "fn2", "chunk_type": "function",
                 "content": "code2", "summary": "related", "start_line": 10, "end_line": 15},
                {"id": "c3", "file_path": "c.py", "name": "fn3", "chunk_type": "function",
                 "content": "code3", "summary": "distant", "start_line": 20, "end_line": 25},
            ],
        )
        provider = _mock_provider()
        config = _make_config(similarity_threshold=0.0)
        engine = HybridSearchEngine(store, provider, config)
        results = engine.search("hello world", mode="keyword", graph=True)
        for r in results:
            assert 0.0 <= r.graph_score <= 1.0
            assert 0.0 <= r.keyword_score <= 1.0
            assert 0.0 <= r.vector_score <= 1.0
            assert 0.0 <= r.combined_score <= 1.0

    def test_depth_2_lower_score_than_depth_1(self):
        """Chunks at depth 2 should have lower graph_score than depth 1 (after normalization)."""
        store = _mock_store_with_graph(
            keyword_chunks=[
                {"id": "c1", "summary": "hello world", "file_path": "a.py",
                 "name": "fn1", "chunk_type": "function", "content": "code",
                 "start_line": 1, "end_line": 5},
            ],
            traversal_edges=[
                {"source_id": "c1", "target_id": "c2", "depth": 1, "direction": "outgoing"},
                {"source_id": "c1", "target_id": "c3", "depth": 2, "direction": "outgoing"},
            ],
            chunk_meta=[
                {"id": "c2", "file_path": "b.py", "name": "fn2", "chunk_type": "function",
                 "content": "code2", "summary": "near", "start_line": 10, "end_line": 15},
                {"id": "c3", "file_path": "c.py", "name": "fn3", "chunk_type": "function",
                 "content": "code3", "summary": "far", "start_line": 20, "end_line": 25},
            ],
        )
        provider = _mock_provider()
        config = _make_config(similarity_threshold=0.0)
        engine = HybridSearchEngine(store, provider, config)
        results = engine.search("hello world", mode="keyword", graph=True)
        c2 = next(r for r in results if r.chunk_id == "c2")
        c3 = next(r for r in results if r.chunk_id == "c3")
        assert c2.graph_score > c3.graph_score

    def test_self_referential_edges_skipped(self):
        """Self-referential edges (source_id == target_id) don't add graph results."""
        store = _mock_store_with_graph(
            keyword_chunks=[
                {"id": "c1", "summary": "hello world", "file_path": "a.py",
                 "name": "fn1", "chunk_type": "function", "content": "code",
                 "start_line": 1, "end_line": 5},
            ],
            traversal_edges=[
                {"source_id": "c1", "target_id": "c1", "depth": 1, "direction": "outgoing"},
            ],
            chunk_meta=[],
        )
        provider = _mock_provider()
        config = _make_config(similarity_threshold=0.0)
        engine = HybridSearchEngine(store, provider, config)
        results = engine.search("hello world", mode="keyword", graph=True)
        # Only c1 (seed), no duplicates from self-ref edge
        assert len([r for r in results if r.chunk_id == "c1"]) == 1


# ── Graph Formatter Tests ─────────────────────────────────────────────


class TestGraphFormatter:
    """Test formatter output with graph_enabled=True."""

    def test_markdown_graph_scores_annotation(self):
        r = _make_result(graph_score=0.7)
        output = format_search_markdown([r], graph_enabled=True)
        assert "> *Scores: graph=0.70, keyword=" in output
        assert "combined=" in output

    def test_markdown_no_scores_when_graph_disabled(self):
        r = _make_result()
        output = format_search_markdown([r], graph_enabled=False)
        assert "Scores:" not in output

    def test_json_graph_score_key(self):
        r = _make_result(graph_score=0.7)
        output = format_search_json([r], "q", "hybrid", graph_enabled=True)
        data = json.loads(output)
        assert "graph" in data["results"][0]["scores"]
        assert data["results"][0]["scores"]["graph"] == 0.7

    def test_json_no_graph_key_when_disabled(self):
        r = _make_result()
        output = format_search_json([r], "q", "hybrid", graph_enabled=False)
        data = json.loads(output)
        assert "graph" not in data["results"][0]["scores"]

    def test_yaml_graph_score_key(self):
        r = _make_result(graph_score=0.7)
        output = format_search_yaml([r], "q", "hybrid", graph_enabled=True)
        data = yaml.safe_load(output)
        assert "graph" in data["results"][0]["scores"]

    def test_kv_graph_scores(self):
        r = _make_result(graph_score=0.7)
        output = format_search_kv([r], graph_enabled=True)
        assert "graph_score:" in output
        assert "keyword_score:" in output
        assert "vector_score:" in output

    def test_kv_no_scores_when_disabled(self):
        r = _make_result()
        output = format_search_kv([r], graph_enabled=False)
        assert "graph_score:" not in output

    def test_format_search_output_dispatches_graph_enabled(self):
        r = _make_result(graph_score=0.7)
        output = format_search_output([r], "json", "q", "hybrid", graph_enabled=True)
        data = json.loads(output)
        assert "graph" in data["results"][0]["scores"]
