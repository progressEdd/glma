---
wave: 1
depends_on: []
files_modified:
  - src/glma/db/ladybug_store.py
  - src/glma/search/__init__.py
  - src/glma/search/engine.py
  - pyproject.toml
requirements:
  - SRCH-01
  - SRCH-02
  - SRCH-03
  - SRCH-04
  - SRCH-05
  - SRCH-06
autonomous: true
---

# Plan 01: Hybrid Search Engine + Vector DB Layer

## Objective

Build the core hybrid search engine with LadybugDB HNSW vector search, fuzzy keyword scoring via rapidfuzz, hybrid score combination, threshold filtering, and the `glma search` CLI command with all output formatters. This is the complete Phase 15 implementation in a single plan.

---

## Task 1: Add rapidfuzz dependency

<objective>Add rapidfuzz as a project dependency for fuzzy string matching.</objective>

<read_first>
- 02-worktrees/glma/pyproject.toml (current dependencies list)
</read_first>

<action>
In `02-worktrees/glma/pyproject.toml`, add `"rapidfuzz>=3.0"` to the `dependencies` list (after the `pyyaml` entry). The line should be:
```toml
    "rapidfuzz>=3.0",
```

Then run:
```bash
cd 02-worktrees/glma && uv sync
```
</action>

<acceptance_criteria>
- `02-worktrees/glma/pyproject.toml` contains `"rapidfuzz>=3.0"` in the dependencies list
- `cd 02-worktrees/glma && uv sync` exits 0
- `cd 02-worktrees/glma && python -c "from rapidfuzz import fuzz; print(fuzz.token_sort_ratio('hello world', 'world hello'))"` prints `100`
</acceptance_criteria>

---

## Task 2: Add vector search methods to LadybugStore

<objective>Add HNSW vector index creation, search, and management methods to the existing LadybugStore class.</objective>

<read_first>
- 02-worktrees/glma/src/glma/db/ladybug_store.py (full file — understand existing schema, connection pattern, and method style)
- .planning/phases/15-hybrid-search-query-integration/15-CONTEXT.md (decisions D-11 through D-22 for vector search behavior)
- .planning/phases/15-hybrid-search-query-integration/15-RESEARCH.md (sections 2 and 5 for LadybugDB vector API)
</read_first>

<action>
Add the following methods to the `LadybugStore` class in `02-worktrees/glma/src/glma/db/ladybug_store.py`:

### 2a. `ensure_vector_extension(self) -> None`

```python
def ensure_vector_extension(self) -> None:
    """Install and load the LadybugDB vector extension for HNSW search."""
    self.conn.execute("INSTALL vector;")
    self.conn.execute("LOAD vector;")
```

### 2b. `create_vector_index(self, dimensions: int = 768) -> None`

Creates the HNSW vector index on the Chunk table's `embedding` property. Drops existing index first (if any) to handle staleness. Uses cosine metric.

```python
def create_vector_index(self, dimensions: int = 768) -> None:
    """Create or recreate the HNSW vector index on chunk embeddings.
    
    Drops existing index first to handle staleness after re-embedding.
    Idempotent — safe to call multiple times.
    
    Args:
        dimensions: Embedding vector dimensions (for future use / validation).
    """
    self.ensure_vector_extension()
    # Drop existing index if it exists
    try:
        self.conn.execute("CALL DROP_VECTOR_INDEX('Chunk', 'chunk_embedding_index');")
    except Exception:
        pass  # Index doesn't exist yet — expected
    # Create fresh HNSW index with cosine metric
    self.conn.execute("""
        CALL CREATE_VECTOR_INDEX(
            'Chunk',
            'chunk_embedding_index',
            'embedding',
            metric := 'cosine'
        );
    """)
```

### 2c. `has_embeddings(self) -> bool`

```python
def has_embeddings(self) -> bool:
    """Check if any chunks in the database have embeddings."""
    result = self.conn.execute(
        "MATCH (c:Chunk) WHERE c.embedding IS NOT NULL RETURN COUNT(c) LIMIT 1"
    )
    rows = list(result)
    return rows[0][0] > 0 if rows else False
```

### 2d. `vector_search(self, query_vector: list[float], k: int = 20) -> list[dict]`

```python
def vector_search(self, query_vector: list[float], k: int = 20) -> list[dict]:
    """Run HNSW vector similarity search against chunk embeddings.
    
    Args:
        query_vector: Embedding vector for the search query.
        k: Number of nearest neighbors to return.
        
    Returns:
        List of dicts with keys: id, file_path, name, chunk_type, content, summary, 
        start_line, end_line, vector_score (1 - cosine_distance).
    """
    self.ensure_vector_extension()
    result = self.conn.execute("""
        CALL QUERY_VECTOR_INDEX(
            'Chunk',
            'chunk_embedding_index',
            $query_vec,
            $k
        )
        RETURN node.id, node.file_path, node.name, node.chunk_type,
               node.content, node.summary, node.start_line, node.end_line,
               distance
        ORDER BY distance
    """, {"query_vec": query_vector, "k": k})
    results = []
    for row in result:
        distance = row[8]
        vector_score = 1.0 - distance  # cosine distance to similarity
        results.append({
            "id": row[0],
            "file_path": row[1],
            "name": row[2],
            "chunk_type": row[3],
            "content": row[4],
            "summary": row[5] or "",
            "start_line": row[6],
            "end_line": row[7],
            "vector_score": max(0.0, vector_score),  # clamp negative similarities
        })
    return results
```

### 2e. `get_chunks_with_summaries_for_keyword(self) -> list[dict]`

```python
def get_chunks_with_summaries_for_keyword(self) -> list[dict]:
    """Get all chunks with non-empty summaries for fuzzy keyword matching.
    
    Returns lightweight dicts — only fields needed for search + scoring,
    not full Chunk objects.
    """
    result = self.conn.execute("""
        MATCH (c:Chunk)
        WHERE c.summary <> ""
        RETURN c.id, c.file_path, c.name, c.chunk_type,
               c.content, c.summary, c.start_line, c.end_line
        ORDER BY c.file_path, c.start_line
    """)
    return [
        {
            "id": row[0],
            "file_path": row[1],
            "name": row[2],
            "chunk_type": row[3],
            "content": row[4],
            "summary": row[5],
            "start_line": row[6],
            "end_line": row[7],
        }
        for row in result
    ]
```
</action>

<acceptance_criteria>
- `02-worktrees/glma/src/glma/db/ladybug_store.py` contains method `ensure_vector_extension` that executes `INSTALL vector;` and `LOAD vector;`
- `02-worktrees/glma/src/glma/db/ladybug_store.py` contains method `create_vector_index` that calls `CALL CREATE_VECTOR_INDEX('Chunk', 'chunk_embedding_index', 'embedding', metric := 'cosine')`
- `02-worktrees/glma/src/glma/db/ladybug_store.py` contains method `has_embeddings` that returns bool
- `02-worktrees/glma/src/glma/db/ladybug_store.py` contains method `vector_search` that returns `list[dict]` with `vector_score` key (computed as `1.0 - distance`)
- `02-worktrees/glma/src/glma/db/ladybug_store.py` contains method `get_chunks_with_summaries_for_keyword` that returns chunks with non-empty summaries
- All existing tests pass: `cd 02-worktrees/glma && uv run pytest tests/ -x -q`
</acceptance_criteria>

---

## Task 3: Create search engine module

<objective>Create the `src/glma/search/` package with the hybrid search engine that combines HNSW vector search with fuzzy keyword matching.</objective>

<read_first>
- 02-worktrees/glma/src/glma/db/ladybug_store.py (LadybugStore methods from Task 2)
- 02-worktrees/glma/src/glma/embedding/providers.py (EmbeddingProvider protocol, OpenAIEmbeddingProvider)
- 02-worktrees/glma/src/glma/models.py (SearchConfig, Chunk)
- 02-worktrees/glma/src/glma/embedding/pipeline.py (pattern for provider + store + config integration)
- .planning/phases/15-hybrid-search-query-integration/15-CONTEXT.md (scoring decisions D-07 through D-10, search modes D-19 through D-22)
</read_first>

<action>
Create the following files:

### 3a. `02-worktrees/glma/src/glma/search/__init__.py`

```python
"""Hybrid semantic + keyword search for code chunks."""

from glma.search.engine import HybridSearchEngine, SearchResult

__all__ = ["HybridSearchEngine", "SearchResult"]
```

### 3b. `02-worktrees/glma/src/glma/search/engine.py`

```python
"""Hybrid search engine combining HNSW vector search with fuzzy keyword matching."""

import logging
from dataclasses import dataclass, field

from rapidfuzz import fuzz

from glma.db.ladybug_store import LadybugStore
from glma.embedding.providers import EmbeddingProvider
from glma.models import SearchConfig

logger = logging.getLogger(__name__)


@dataclass
class SearchResult:
    """A single search result with scores."""
    chunk_id: str
    file_path: str
    chunk_name: str
    chunk_type: str
    content: str
    summary: str
    start_line: int
    end_line: int
    keyword_score: float = 0.0
    vector_score: float = 0.0
    combined_score: float = 0.0


class HybridSearchEngine:
    """Combines LadybugDB HNSW vector search with fuzzy keyword matching.
    
    Scoring: keyword_weight × keyword_score + vector_weight × vector_score
    Both scores normalized to 0-1 range before combining.
    """

    def __init__(
        self,
        store: LadybugStore,
        provider: EmbeddingProvider,
        config: SearchConfig,
    ):
        self._store = store
        self._provider = provider
        self._config = config

    def search(self, query: str, mode: str = "hybrid") -> list[SearchResult]:
        """Run hybrid search and return ranked, filtered results.
        
        Args:
            query: Natural language search query.
            mode: Search strategy — 'hybrid', 'vector', or 'keyword'.
            
        Returns:
            List of SearchResult sorted by combined_score descending,
            filtered by similarity_threshold.
            
        Raises:
            ValueError: If vector mode requested but no embeddings exist.
        """
        # Determine effective weights based on mode
        if mode == "vector":
            kw_weight, vec_weight = 0.0, 1.0
        elif mode == "keyword":
            kw_weight, vec_weight = 1.0, 0.0
        else:  # hybrid
            kw_weight = self._config.hybrid_keyword_weight
            vec_weight = self._config.hybrid_vector_weight

        # Validate vector availability
        needs_vector = vec_weight > 0
        if needs_vector:
            if not self._store.has_embeddings():
                raise ValueError(
                    "No embeddings found. Run `glma embed` first."
                )
            # Ensure vector index exists (lazy creation)
            self._store.create_vector_index(self._config.vector_dimensions)

        # Run vector search if needed
        vector_results: dict[str, dict] = {}
        if needs_vector:
            query_vecs = self._provider.embed([query])
            if not query_vecs:
                raise ValueError("Failed to embed query string.")
            query_vec = query_vecs[0]
            raw_vec = self._store.vector_search(query_vec, k=100)
            vector_results = {r["id"]: r for r in raw_vec}

        # Run keyword search if needed
        keyword_results: dict[str, float] = {}
        if kw_weight > 0:
            chunks = self._store.get_chunks_with_summaries_for_keyword()
            keyword_results = self._fuzzy_score_all(query, chunks)

        # Merge candidates from both sources
        all_chunk_ids = set(vector_results.keys()) | set(keyword_results.keys())
        
        # For keyword-only mode, we need chunk metadata from keyword results
        # For vector-only mode, metadata comes from vector results
        # For hybrid, merge both
        chunk_meta: dict[str, dict] = {}
        for cid in vector_results:
            chunk_meta[cid] = vector_results[cid]
        for cid, score in keyword_results.items():
            if cid not in chunk_meta:
                # Need to get metadata for keyword-only results
                pass  # handled below

        # If keyword mode, build metadata from keyword chunks
        if kw_weight > 0 and not vector_results:
            chunks = self._store.get_chunks_with_summaries_for_keyword()
            for c in chunks:
                chunk_meta[c["id"]] = c

        # Build search results with combined scores
        results: list[SearchResult] = []
        for cid in all_chunk_ids:
            meta = chunk_meta.get(cid, {})
            if not meta:
                continue
            kw_score = keyword_results.get(cid, 0.0)
            vec_score = vector_results[cid].get("vector_score", 0.0) if cid in vector_results else 0.0
            combined = kw_weight * kw_score + vec_weight * vec_score
            
            results.append(SearchResult(
                chunk_id=cid,
                file_path=meta.get("file_path", ""),
                chunk_name=meta.get("name", ""),
                chunk_type=meta.get("chunk_type", ""),
                content=meta.get("content", ""),
                summary=meta.get("summary", ""),
                start_line=meta.get("start_line", 0),
                end_line=meta.get("end_line", 0),
                keyword_score=kw_score,
                vector_score=vec_score,
                combined_score=combined,
            ))

        # Sort by combined score descending
        results.sort(key=lambda r: r.combined_score, reverse=True)

        # Filter by threshold
        threshold = self._config.similarity_threshold
        filtered = [r for r in results if r.combined_score >= threshold]
        
        logger.info(
            "Search '%s' (mode=%s): %d candidates, %d above threshold %.2f",
            query, mode, len(results), len(filtered), threshold,
        )
        
        return filtered

    @staticmethod
    def _fuzzy_score_all(
        query: str,
        chunks: list[dict],
    ) -> dict[str, float]:
        """Compute fuzzy keyword scores for all chunks.
        
        Uses rapidfuzz.token_sort_ratio, normalized to 0-1.
        
        Args:
            query: Search query string.
            chunks: List of chunk dicts with 'id' and 'summary' keys.
            
        Returns:
            Dict mapping chunk_id to keyword score (0-1).
        """
        scores: dict[str, float] = {}
        for chunk in chunks:
            summary = chunk.get("summary", "")
            if not summary:
                continue
            raw = fuzz.token_sort_ratio(query, summary)
            scores[chunk["id"]] = raw / 100.0
        return scores
```

Key design notes:
- `_fuzzy_score_all` uses `fuzz.token_sort_ratio` (word-order independent matching), normalized to 0-1 by dividing by 100
- `vector_score` comes from `1 - cosine_distance` (clamped to 0)
- `search()` accepts mode parameter and adjusts weights accordingly
- Lazy vector index creation — `create_vector_index()` is called only when vector search is needed
- Results filtered by `SearchConfig.similarity_threshold` after scoring
- Error raised with actionable message if vector search requested but no embeddings exist
</action>

<acceptance_criteria>
- `02-worktrees/glma/src/glma/search/__init__.py` exists and exports `HybridSearchEngine` and `SearchResult`
- `02-worktrees/glma/src/glma/search/engine.py` exists with class `HybridSearchEngine`
- `HybridSearchEngine.search()` accepts `query: str` and `mode: str` parameters
- `_fuzzy_score_all` uses `fuzz.token_sort_ratio` and normalizes by dividing by 100
- `search()` raises `ValueError` with message containing "No embeddings found" when mode requires vectors but none exist
- `search()` calls `self._store.create_vector_index()` before vector search (lazy creation)
- `search()` filters results by `self._config.similarity_threshold`
- `search()` returns results sorted by `combined_score` descending
- `cd 02-worktrees/glma && uv run python -c "from glma.search import HybridSearchEngine, SearchResult"` exits 0
</acceptance_criteria>

---

## Task 4: Create search result formatters

<objective>Create output formatters for search results in all four formats: markdown (lean code blocks), markdown-kv, JSON, and YAML.</objective>

<read_first>
- 02-worktrees/glma/src/glma/query/formatter.py (existing formatter patterns — follow same style)
- 02-worktrees/glma/src/glma/models.py (ExportFormat enum)
- .planning/phases/15-hybrid-search-query-integration/15-CONTEXT.md (decisions D-04, D-05, D-06 for lean output format)
</read_first>

<action>
Create `02-worktrees/glma/src/glma/search/formatter.py`:

```python
"""Search result formatters for all output types.

Lean output design (per CONTEXT.md D-04/05/06):
- Markdown: file path heading + code blocks with summary annotations. No scores, no metadata.
- JSON: full metadata including scores, line ranges, chunk names.
- YAML: same structure as JSON.
- Markdown-KV: key-value style with score, type, lines.
"""

import json
from typing import Optional

from glma.search.engine import SearchResult


def _get_lang_hint(file_path: str) -> str:
    """Get language hint for markdown code block."""
    if file_path.endswith(".py"):
        return "python"
    elif file_path.endswith(".c") or file_path.endswith(".h"):
        return "c"
    return ""


def format_search_markdown(results: list[SearchResult]) -> str:
    """Format search results as lean markdown — file heading + code blocks + summary annotations.
    
    No scores, no line numbers, no chunk names in output.
    Consumers who need metadata use glma query <file> or JSON format.
    """
    if not results:
        return ""
    
    lines: list[str] = []
    current_file = None
    
    for result in results:
        # File path heading (only when file changes)
        if result.file_path != current_file:
            if current_file is not None:
                lines.append("")  # blank line between files
            lines.append(f"# {result.file_path}")
            lines.append("")
            current_file = result.file_path
        
        # Code block with summary annotation
        lang = _get_lang_hint(result.file_path)
        lines.append(f"```{lang}")
        lines.append(result.content)
        lines.append("```")
        if result.summary:
            lines.append(f"> *Summary: {result.summary}*")
        lines.append("")
    
    return "\n".join(lines)


def format_search_kv(results: list[SearchResult]) -> str:
    """Format search results as key-value markdown."""
    if not results:
        return ""
    
    lines: list[str] = []
    current_file = None
    
    for result in results:
        if result.file_path != current_file:
            if current_file is not None:
                lines.append("")
            lines.append(f"# {result.file_path}")
            lines.append("")
            current_file = result.file_path
        
        lines.append(f"## {result.chunk_name}")
        lines.append("")
        lines.append(f"type: {result.chunk_type}")
        lines.append(f"lines: L{result.start_line}-L{result.end_line}")
        lines.append(f"score: {result.combined_score:.3f}")
        if result.summary:
            lines.append(f"summary: {result.summary}")
        lang = _get_lang_hint(result.file_path)
        lines.append("")
        lines.append(f"```{lang}")
        lines.append(result.content)
        lines.append("```")
        lines.append("")
    
    return "\n".join(lines)


def format_search_json(
    results: list[SearchResult],
    query: str,
    search_mode: str,
) -> str:
    """Format search results as JSON with full metadata."""
    data = {
        "query": query,
        "search_mode": search_mode,
        "total_results": len(results),
        "results": [
            {
                "file_path": r.file_path,
                "chunk_name": r.chunk_name,
                "chunk_type": r.chunk_type,
                "start_line": r.start_line,
                "end_line": r.end_line,
                "summary": r.summary,
                "content": r.content,
                "scores": {
                    "keyword": round(r.keyword_score, 4),
                    "vector": round(r.vector_score, 4),
                    "combined": round(r.combined_score, 4),
                },
            }
            for r in results
        ],
    }
    return json.dumps(data, indent=2)


def format_search_yaml(
    results: list[SearchResult],
    query: str,
    search_mode: str,
) -> str:
    """Format search results as YAML with full metadata."""
    import yaml
    data = {
        "query": query,
        "search_mode": search_mode,
        "total_results": len(results),
        "results": [
            {
                "file_path": r.file_path,
                "chunk_name": r.chunk_name,
                "chunk_type": r.chunk_type,
                "start_line": r.start_line,
                "end_line": r.end_line,
                "summary": r.summary,
                "content": r.content,
                "scores": {
                    "keyword": round(r.keyword_score, 4),
                    "vector": round(r.vector_score, 4),
                    "combined": round(r.combined_score, 4),
                },
            }
            for r in results
        ],
    }
    return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)


def format_search_output(
    results: list[SearchResult],
    output_format: str,
    query: str,
    search_mode: str,
) -> str:
    """Dispatch to the appropriate formatter based on output format string.
    
    Args:
        results: Search results to format.
        output_format: One of 'markdown', 'markdown-kv', 'json', 'yaml'.
        query: Original search query (for JSON/YAML metadata).
        search_mode: Search mode used (for JSON/YAML metadata).
        
    Returns:
        Formatted string.
    """
    if output_format == "json":
        return format_search_json(results, query, search_mode)
    elif output_format == "yaml":
        return format_search_yaml(results, query, search_mode)
    elif output_format == "markdown-kv":
        return format_search_kv(results)
    else:  # markdown (default)
        return format_search_markdown(results)
```

Key design notes:
- Markdown format is maximally lean per CONTEXT.md: file heading + code blocks + summary annotations only. No scores, no metadata.
- JSON and YAML include full metadata including scores, line ranges, chunk names.
- Markdown-KV is a middle ground: includes score and metadata but in key-value style.
- All formatters group results by file path.
</action>

<acceptance_criteria>
- `02-worktrees/glma/src/glma/search/formatter.py` exists
- `format_search_markdown` produces output with `# file_path` headings and code blocks (no score metadata)
- `format_search_markdown` includes `> *Summary: ...*` annotations after code blocks
- `format_search_json` returns valid JSON with keys: `query`, `search_mode`, `total_results`, `results` (each result has `scores.keyword`, `scores.vector`, `scores.combined`)
- `format_search_yaml` returns valid YAML with same structure as JSON
- `format_search_kv` includes `type:`, `lines:`, `score:` key-value pairs
- `format_search_output` dispatches correctly for all four format values
- `cd 02-worktrees/glma && uv run python -c "from glma.search.formatter import format_search_output"` exits 0
</acceptance_criteria>

---

## Task 5: Add `glma search` CLI command

<objective>Add the new top-level `glma search` command to the CLI that wires together config loading, provider instantiation, the search engine, and output formatting.</objective>

<read_first>
- 02-worktrees/glma/src/glma/cli.py (full file — follow exact patterns from `embed` and `query` commands)
- 02-worktrees/glma/src/glma/search/engine.py (HybridSearchEngine, SearchResult)
- 02-worktrees/glma/src/glma/search/formatter.py (format_search_output)
- 02-worktrees/glma/src/glma/config.py (load_search_config)
- 02-worktrees/glma/src/glma/embedding/providers.py (OpenAIEmbeddingProvider)
- 02-worktrees/glma/src/glma/models.py (ExportFormat, SearchConfig)
- .planning/phases/15-hybrid-search-query-integration/15-CONTEXT.md (decisions D-01 through D-03, D-19 through D-22)
</read_first>

<action>
Add a new `search` command function to `02-worktrees/glma/src/glma/cli.py`. Place it after the `embed` command function.

The command should:

1. Accept positional `query_text: str` argument (the natural language search query)
2. Accept `--search-mode` option with choices `hybrid` (default), `vector`, `keyword`
3. Accept `--format` option with choices `markdown` (default), `markdown-kv`, `json`, `yaml`
4. Accept `--output` option for file output (default stdout)
5. Accept `--repo` option for repo root (same auto-detection as `query` command)
6. Accept `--embedding-provider`, `--embedding-model`, `--embedding-base-url`, `--vector-dimensions` options (same overrides as `embed` command)
7. Accept `--similarity-threshold` option (float, overrides config)
8. Accept `--quiet` flag

Exact function signature:
```python
@app.command()
def search(
    query_text: str = typer.Argument(..., help="Natural language search query."),
    search_mode: str = typer.Option("hybrid", "--search-mode", help="Search strategy: hybrid, vector, keyword."),
    output_format: str = typer.Option("markdown", "--format", "-f", help="Output format: markdown, markdown-kv, json, yaml."),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (default: stdout)."),
    repo_root: Optional[Path] = typer.Option(None, "--repo", "-r", help="Repo root directory (auto-detected)."),
    embedding_provider: Optional[str] = typer.Option(None, "--embedding-provider", help="Embedding provider preset name."),
    embedding_model: Optional[str] = typer.Option(None, "--embedding-model", help="Model name for embeddings."),
    embedding_base_url: Optional[str] = typer.Option(None, "--embedding-base-url", help="API base URL for embedding provider."),
    vector_dimensions: Optional[int] = typer.Option(None, "--vector-dimensions", help="Embedding vector dimensions."),
    similarity_threshold: Optional[float] = typer.Option(None, "--similarity-threshold", help="Minimum similarity score for results (0.0-1.0)."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Suppress progress output."),
) -> None:
```

Implementation flow:
1. Validate `--search-mode` is one of `hybrid`, `vector`, `keyword`. If invalid, write to stderr and exit 4.
2. Validate `--format` using `ExportFormat` enum (same pattern as `query` command). If invalid, write to stderr and exit 4.
3. Resolve repo root (same auto-detection logic as `query` command — walk up from CWD looking for `.glma-index/` or `.glma.toml`). Exit 4 if not found.
4. Validate index exists at `repo_root / ".glma-index" / "db" / "index.lbug"`. Exit 4 with "No index found. Run `glma index` first." if missing.
5. Build search CLI overrides dict from provided options (same pattern as `embed` command):
   ```python
   search_overrides = {}
   if embedding_provider: search_overrides["embedding_provider"] = embedding_provider
   if embedding_model: search_overrides["embedding_model"] = embedding_model
   if embedding_base_url: search_overrides["embedding_base_url"] = embedding_base_url
   if vector_dimensions is not None: search_overrides["vector_dimensions"] = vector_dimensions
   if similarity_threshold is not None: search_overrides["similarity_threshold"] = similarity_threshold
   ```
6. Load search config: `search_cfg = load_search_config(repo_root_path, search_overrides)`
7. Instantiate `OpenAIEmbeddingProvider` with `base_url=search_cfg.embedding_base_url`, `model=search_cfg.embedding_model`. Catch `ImportError` and exit 1 with error message.
8. Open `LadybugStore(db_path)`
9. Create `HybridSearchEngine(store, provider, search_cfg)`
10. Call `engine.search(query_text, mode=search_mode)`. Wrap in try/except for `ValueError` (no embeddings) — print error message to stderr and exit 1.
11. If results empty: print "No results above threshold {search_cfg.similarity_threshold}. Try lowering --similarity-threshold." to stderr, exit 0.
12. Format output using `format_search_output(results, output_format, query_text, search_mode)` from `glma.search.formatter`
13. Write to file or stdout using `_write_output()` helper (already exists in cli.py)
14. If not quiet, print "Found {N} results" to stderr before output.

Do NOT modify any existing CLI commands. Only add the new `search` function.
</action>

<acceptance_criteria>
- `02-worktrees/glma/src/glma/cli.py` contains function `search` decorated with `@app.command()`
- `glma search --help` exits 0 and shows `QUERY_TEXT` as positional argument
- `glma search --help` shows `--search-mode`, `--format`, `--output`, `--repo`, `--embedding-provider`, `--embedding-model`, `--embedding-base-url`, `--vector-dimensions`, `--similarity-threshold`, `--quiet` options
- Invalid `--search-mode badvalue` writes error to stderr and exits with code 4
- Invalid `--format badvalue` writes error to stderr and exits with code 4
- No index found → stderr contains "No index found" and exits 4
- Vector mode with no embeddings → stderr contains "No embeddings found" and exits 1
- Empty results → stderr contains "No results above threshold" and exits 0
- All existing tests pass: `cd 02-worktrees/glma && uv run pytest tests/ -x -q`
</acceptance_criteria>

---

## Task 6: Write tests for hybrid search

<objective>Write comprehensive tests for the search engine, formatters, and CLI command.</objective>

<read_first>
- 02-worktrees/glma/src/glma/search/engine.py (HybridSearchEngine, SearchResult)
- 02-worktrees/glma/src/glma/search/formatter.py (all formatters)
- 02-worktrees/glma/src/glma/cli.py (search command)
- 02-worktrees/glma/tests/ (existing test patterns)
</read_first>

<action>
Create `02-worktrees/glma/tests/test_search.py` with the following test structure:

### Unit Tests (no DB required)

```python
"""Tests for hybrid search engine, formatters, and CLI command."""

import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from glma.search.engine import HybridSearchEngine, SearchResult
from glma.search.formatter import (
    format_search_json,
    format_search_kv,
    format_search_markdown,
    format_search_output,
    format_search_yaml,
)
from glma.models import SearchConfig
```

**Test `SearchResult` construction:**
- Test creating a SearchResult with all fields
- Verify default scores are 0.0

**Test `_fuzzy_score_all`:**
- Test with two chunks where one summary matches the query better than the other
- Verify scores are normalized to 0-1 range (not 0-100)
- Test with empty summary → score should be absent (chunk excluded)
- Test exact match → score should be 1.0 (100/100)

**Test `HybridSearchEngine.search()` with mocks:**
- Mock `LadybugStore` and `EmbeddingProvider`
- Test `mode="keyword"`: only calls `get_chunks_with_summaries_for_keyword`, never calls `vector_search`
- Test `mode="vector"`: calls `has_embeddings()` → True, calls `create_vector_index()`, calls `vector_search()`, never calls `get_chunks_with_summaries_for_keyword`
- Test `mode="vector"` with no embeddings: raises `ValueError` with "No embeddings found"
- Test `mode="hybrid"`: calls both vector and keyword paths
- Test threshold filtering: results below threshold are excluded
- Test results sorted by combined_score descending

### Formatter Tests

**Test `format_search_markdown`:**
- Test with two results from same file → single file heading
- Test with results from different files → multiple file headings
- Verify output contains code blocks (triple backticks)
- Verify output contains summary annotations (`> *Summary: ...*`)
- Verify output does NOT contain scores or line numbers
- Test with empty results → returns empty string

**Test `format_search_json`:**
- Test output is valid JSON
- Verify JSON has `query`, `search_mode`, `total_results`, `results` keys
- Verify each result has `scores.keyword`, `scores.vector`, `scores.combined`
- Test with empty results → `total_results: 0`, `results: []`

**Test `format_search_yaml`:**
- Test output is valid YAML (parse with yaml.safe_load)
- Verify same structure as JSON output

**Test `format_search_kv`:**
- Test output contains `type:`, `lines:`, `score:` keys
- Test output contains file path headings

**Test `format_search_output` dispatch:**
- Verify "json" → calls format_search_json
- Verify "yaml" → calls format_search_yaml
- Verify "markdown-kv" → calls format_search_kv
- Verify "markdown" → calls format_search_markdown

### CLI Tests

Use `typer.testing.CliRunner` (follow existing test patterns):

```python
from typer.testing import CliRunner
from glma.cli import app

runner = CliRunner()
```

**Test `search --help`:**
- Exits 0, output contains "Natural language search query", "--search-mode", "--format"

**Test invalid search mode:**
- `glma search "test" --search-mode badvalue` → exit code 4, stderr contains error

**Test invalid format:**
- `glma search "test" --format badvalue` → exit code 4

**Test no index found:**
- Run from temp directory with no index → stderr contains "No index found", exit 4

### Integration Test (with Ladybug in-memory DB)

**Test full search pipeline:**
1. Create temp directory with `LadybugStore` at `.glma-index/db/index.lbug`
2. Create a File record and several Chunk records with summaries and deterministic embeddings
3. Create a simple test provider that returns fixed vectors (not hitting a real API)
4. Run `HybridSearchEngine.search()` and verify results are returned and ranked correctly
5. Test all three modes (hybrid, vector, keyword)

For deterministic test embeddings:
```python
class MockEmbeddingProvider:
    def embed(self, texts: list[str]) -> list[list[float]]:
        # Return deterministic vectors based on text length
        return [[0.1] * 768 for _ in texts]
```

All tests should pass with: `cd 02-worktrees/glma && uv run pytest tests/test_search.py -v`
</action>

<acceptance_criteria>
- `02-worktrees/glma/tests/test_search.py` exists
- `cd 02-worktrees/glma && uv run pytest tests/test_search.py -v` passes all tests
- Tests cover: fuzzy scoring normalization, search mode weight behavior, threshold filtering, result sorting, all four formatters, CLI validation, no-embeddings error, no-index error
- `cd 02-worktrees/glma && uv run pytest tests/ -x -q` passes (all existing + new tests)
</acceptance_criteria>

---

## Verification

After all tasks complete, verify:

1. **All tests pass**: `cd 02-worktrees/glma && uv run pytest tests/ -v`
2. **CLI help works**: `cd 02-worktrees/glma && uv run glma search --help`
3. **Import works**: `cd 02-worktrees/glma && uv run python -c "from glma.search import HybridSearchEngine, SearchResult; from glma.search.formatter import format_search_output"`
4. **No regressions**: All pre-existing test files pass without modification

## must_haves

- `glma search "query"` returns hybrid-ranked results combining fuzzy keyword + HNSW vector similarity
- Results filtered by configurable similarity threshold
- `--search-mode hybrid|vector|keyword` forces specific strategy
- Vector mode errors cleanly when no embeddings exist (with actionable message)
- Output in all four formats (markdown, markdown-kv, json, yaml)
- Markdown output is lean: file heading + code blocks + summary annotations only
- Vector index created lazily on first search
- Only one new dependency: rapidfuzz
