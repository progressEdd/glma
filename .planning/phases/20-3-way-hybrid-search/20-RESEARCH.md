# Phase 20: 3-Way Hybrid Search - Research

**Date:** 2026-05-12
**Phase:** 20 — 3-Way Hybrid Search
**Status:** Research Complete

---

## Research Objective

Investigate the implementation path for unifying graph relationship traversal with existing keyword and vector search into a 3-way hybrid scoring system for `glma search --graph`.

---

## Current Architecture

### Search Engine (`src/glma/search/engine.py`)

- **`HybridSearchEngine`** class: combines HNSW vector search with fuzzy keyword matching
- **`SearchResult`** dataclass: `chunk_id`, `file_path`, `chunk_name`, `chunk_type`, `content`, `summary`, `start_line`, `end_line`, `keyword_score`, `vector_score`, `combined_score`
- **`search(query, mode)`** method: runs vector and/or keyword search, merges candidates, computes weighted combined score, filters by threshold
- Current scoring: `kw_weight × kw_score + vec_weight × vec_score`

### Graph Traversal (`src/glma/db/ladybug_store.py`)

- **`traverse_relationships(chunk_ids, max_depth)`**: BFS on RELATES_TO edges (bidirectional: outgoing + incoming)
  - Returns list of edge dicts with added `depth` field (1-indexed)
  - Uses visited set to prevent cycles
  - Returns edges, NOT chunks — planner must design chunk extraction from edge results
  - Self-referential edges: current code appends them to results but doesn't follow them
- **`get_outgoing_relationships(chunk_id)`**: returns edge dicts with `target_id`, `target_name`, `rel_type`, `confidence`
- **`get_incoming_relationships(chunk_id)`**: returns edge dicts with `source_id`, `source_name`, `rel_type`, `confidence`
- **RELATES_TO schema**: `(FROM Chunk TO Chunk, rel_type STRING, confidence STRING, source_line INT64, target_name STRING)`

### Config & Models (`src/glma/models.py`, `src/glma/config.py`)

- **`SearchConfig`** Pydantic model (line 176):
  - `similarity_threshold: float = 0.5`
  - `hybrid_keyword_weight: float = 0.5`
  - `hybrid_vector_weight: float = 0.5`
  - `_validate_hybrid_weights()`: checks `abs(total - 1.0) > 0.05`
  - Needs: `graph_weight`, `graph_depth`, `graph_fanout` fields
  - Validator needs updating for 3-weight sum

### Formatter (`src/glma/search/formatter.py`)

- Four format functions: `format_search_markdown`, `format_search_kv`, `format_search_json`, `format_search_yaml`
- JSON/YAML: include `scores` dict with `keyword`, `vector`, `combined`
- Markdown: lean — no scores, just file heading + code blocks + summary annotation
- Markdown-KV: has `score: {combined_score:.3f}` line
- `format_search_output()` dispatches by format string

### CLI (`src/glma/cli.py`)

- **`search` command** (line 675): arguments for query, search-mode, format, output, embedding params, similarity_threshold, raw/rewriting flags
- Build `search_overrides` dict from CLI flags, pass to `load_search_config()`
- Instantiates `LadybugStore`, `OpenAIEmbeddingProvider`, `HybridSearchEngine`
- Calls `engine.search(effective_query, mode=search_mode)`
- Calls `format_search_output()` with results and query info
- Needs: `--graph`, `--graph-depth`, `--graph-fanout` flags

---

## Key Design Decisions to Implement

### 1. Graph Score Computation
- Inverse depth decay: `1/depth` (direct neighbor = 1.0, 2 hops = 0.5, 3 hops = 0.33)
- Minimum depth (shortest path) determines score when chunk discovered via multiple paths
- BFS visited set ensures first discovery = shortest path
- Self-referential edges (source_id == target_id) should be skipped during graph search

### 2. Chunk Extraction from Edge Results
`traverse_relationships()` returns edges. Need to:
1. Collect unique `target_id` from outgoing edges and `source_id` from incoming edges
2. Track minimum depth per chunk (first BFS visit = min depth)
3. Fetch chunk metadata for all discovered IDs (need a batch lookup — may need new store method or reuse existing `get_chunks_with_summaries_for_keyword()`)

### 3. Two-Phase Search
1. Run keyword+vector search (existing logic) → get results
2. Take top-K results by combined score as BFS seeds (K = `graph_fanout`)
3. Call `store.traverse_relationships(seed_ids, max_depth=graph_depth)`
4. Extract discovered chunks with depths
5. Compute graph scores, merge with existing results
6. Normalize all three dimensions
7. Combine with 3-way weights

### 4. Min-Max Normalization
- Per dimension across the result set
- Formula: `(score - min) / (max - min + epsilon)`
- Epsilon for edge case when all scores in a dimension are identical
- Graph-only chunks get `keyword_score=0.0, vector_score=0.0`

### 5. Score Display
- Markdown/Markdown-KV: inline annotation `> *Scores: graph=0.7, keyword=0.4, vector=0.9, combined=0.67*` (only when `--graph` active)
- JSON/YAML: add `graph` key to `scores` dict
- When `--graph` is off: output matches v1.3 exactly

---

## Implementation Approach

### Extension Point: `HybridSearchEngine.search()`
The cleanest approach is to extend the existing `search()` method with an optional graph phase. When `--graph` is enabled:
1. After existing keyword+vector merge, take top-K seeds
2. Run graph traversal
3. Merge graph-discovered chunks into results
4. Normalize all three dimensions
5. Recombine with 3-way weights

### SearchResult Extension
Add `graph_score: float = 0.0` field to `SearchResult` dataclass.

### New Store Method Needed
Need a method to fetch chunk metadata by a list of IDs (batch lookup). Current code has `get_chunks_with_summaries_for_keyword()` but that returns ALL chunks. Could:
- Add a `get_chunks_by_ids(ids: list[str]) -> list[dict]` method to `LadybugStore`
- Or filter the results of existing methods

A dedicated batch lookup by IDs is more efficient.

### Config Extension
Add to `SearchConfig`:
```python
graph_weight: float = Field(default=0.4, ge=0.0, le=1.0)
graph_depth: int = Field(default=2, ge=1, le=5)
graph_fanout: int = Field(default=10, ge=1, le=100)
```
Update validator to check 3-weight sum.

### CLI Extension
Add to `search` command:
```python
graph: bool = typer.Option(False, "--graph", help="Enable 3-way hybrid search with graph traversal.")
graph_depth: Optional[int] = typer.Option(None, "--graph-depth", help="Max graph traversal depth (default: 2).")
graph_fanout: Optional[int] = typer.Option(None, "--graph-fanout", help="Number of seed chunks for graph traversal (default: 10).")
```

### Formatter Extension
Pass `graph_enabled: bool` flag through to formatters. When true:
- JSON/YAML: add `graph` key to scores dict
- Markdown/Markdown-KV: add `> *Scores: ...*` annotation after summary annotation

---

## Dependencies & Risks

### Dependencies
- Phase 15 (hybrid search) — complete ✓
- Phase 19 (query rewriting) — complete ✓ (rewrites run before engine, no interaction)
- `traverse_relationships()` — exists and works ✓

### Risks
- **Performance**: Graph traversal on large codebases with deep depth could be slow. Mitigated by default depth=2 and fanout=10 limits.
- **Edge extraction**: `traverse_relationships()` returns edges not chunks. Need careful extraction logic and a batch chunk lookup method.
- **Backward compatibility**: When `--graph` is off, behavior must be identical. `graph_score` defaults to 0.0 and is ignored.

---

## File Change Summary

| File | Change |
|------|--------|
| `src/glma/models.py` | Add `graph_weight`, `graph_depth`, `graph_fanout` to `SearchConfig`; update validator |
| `src/glma/db/ladybug_store.py` | Add `get_chunks_by_ids()` batch lookup method |
| `src/glma/search/engine.py` | Add `graph_score` to `SearchResult`; extend `search()` with graph phase |
| `src/glma/search/formatter.py` | Add graph scores to output when enabled |
| `src/glma/cli.py` | Add `--graph`, `--graph-depth`, `--graph-fanout` flags |
| Tests | New test file for graph search integration |

---

## RESEARCH COMPLETE

All implementation paths identified. Ready for planning.
