# Phase 20: 3-Way Hybrid Search - Context

**Gathered:** 2026-05-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Unify graph relationship traversal with existing keyword and vector search into a single configurable 3-way hybrid scoring system for `glma search --graph`. Graph BFS from seed chunks (found by keyword+vector) traverses RELATES_TO edges to discover additional relevant chunks. All three scores are min-max normalized and combined with configurable weights. Includes score breakdown in output when 3-way mode is active.

Requirements: HYBR-01 through HYBR-06.

No changes to existing `glma query` command. No changes to the 2-way hybrid search behavior when `--graph` is not specified. No new CLI commands — extends the existing `glma search` command.

</domain>

<decisions>
## Implementation Decisions

### Graph Scoring Model
- **D-01:** Inverse depth decay (`1/depth`) — direct neighbor = 1.0, 2 hops = 0.5, 3 hops = 0.33. Simple, predictable, naturally lands in [0,1].
- **D-02:** Flat scoring — no edge-type weighting. All RELATES_TO edges (calls, imports, inherits, includes, implements) treated equally. Depth is the only signal for graph relevance.
- **D-03:** Ignore confidence tags (DIRECT vs INFERRED) in scoring. Both edge types contribute equally to graph score.
- **D-04:** Include graph-only chunks (not found by keyword or vector) with `keyword_score=0.0, vector_score=0.0`. Their combined score is `graph_weight × graph_score`. Graph traversal's purpose is discovering code the text/vector search missed.
- **D-05:** Minimum depth (shortest path) determines a chunk's graph score when discovered via multiple BFS paths. BFS visited set naturally ensures first discovery = shortest path.

### Score Normalization & Combination
- **D-06:** Three explicit weights (`graph_weight`, `keyword_weight`, `vector_weight`) that must sum to ~1.0 (within 0.05 tolerance), matching existing validator pattern. Defaults: 0.4, 0.3, 0.3 per ROADMAP.
- **D-07:** Min-max normalize per dimension across the result set before combining with weights. Satisfies HYBR-03. Formula: `(score - min) / (max - min + epsilon)`.
- **D-08:** Smoothing constant (epsilon) for min==max edge case in normalization. Standard numerical approach — single-result dimensions get ~0.99, not 1.0 or division-by-zero.
- **D-09:** Combined score formula: `graph_weight × normalized_graph_score + keyword_weight × normalized_keyword_score + vector_weight × normalized_vector_score`.

### Score Breakdown Display
- **D-10:** Inline annotation in markdown and markdown-kv formats when `--graph` is active: `> *Scores: graph=0.7, keyword=0.4, vector=0.9, combined=0.67*`. Mirrors the existing summary annotation pattern (`> *Summary: ...*`). When `--graph` is off, markdown output is identical to today.
- **D-11:** JSON and YAML output add a `graph` key to the existing `scores` dict: `{"keyword": 0.4, "vector": 0.9, "graph": 0.7, "combined": 0.67}`. Shows normalized scores only — no raw pre-normalization scores.
- **D-12:** When `--graph` is not specified, output matches v1.3 format exactly. No `graph` key in scores, no score annotations in markdown.

### Graph Traversal Behavior
- **D-13:** Two-phase approach: run keyword+vector search first, take top-K chunks from combined results as BFS seeds, then traverse RELATES_TO edges to discover additional candidates. K is controlled by `graph_fanout` config.
- **D-14:** Bidirectional traversal — follow both outgoing and incoming RELATES_TO edges. Leverages existing `traverse_relationships()` behavior. If `login()` is found, both `authenticate()` (called by login) and `login_handler()` (calls login) are discovered.
- **D-15:** Config + CLI flags for `graph_depth` and `graph_fanout`. Defaults: depth=2, fanout=10. `--graph-depth` and `--graph-fanout` CLI flags override `[search]` config section. Follows existing config+CLI override pattern.
- **D-16:** `--graph` flag is opt-in to preserve existing `glma search` behavior. When present, enables 3-way hybrid mode with graph traversal + score breakdown. When absent, search runs exactly as Phase 15 (keyword+vector only).

### Agent's Discretion
- Exact epsilon value for normalization smoothing
- How to extract discovered chunks from `traverse_relationships()` edge results (it returns edges, not chunks)
- How to handle self-referential edges (unresolved targets) during graph search — skip them
- Whether `graph_fanout` limits seeds (top-K from 2-way results) or per-node fan-out in BFS, or both
- How to structure the graph search module (extend `engine.py` or new `graph.py`)
- Exact `SearchConfig` validator update for 3-way weight sum
- Test structure and coverage specifics

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Search infrastructure (being extended)
- `src/glma/search/engine.py` — `HybridSearchEngine` with `search()` method, `SearchResult` dataclass. The 3-way logic extends this class.
- `src/glma/search/formatter.py` — `format_search_output()` and per-format functions. Needs `graph` score added to scores dict and markdown annotation.
- `src/glma/search/rewriter.py` — `rewrite_query()` function. No changes needed, runs before engine.

### Database layer (graph traversal)
- `src/glma/db/ladybug_store.py` — `LadybugStore.traverse_relationships(chunk_ids, max_depth)` does BFS on RELATES_TO edges (lines ~567-620). Returns relationship edges with `depth` field. **Key: returns edges, not discovered chunks — planner must design chunk extraction.**
- `src/glma/db/ladybug_store.py` — `LadybugStore.get_outgoing_relationships()` and `get_incoming_relationships()` used by BFS.
- `src/glma/db/ladybug_store.py` — RELATES_TO schema: `(FROM Chunk TO Chunk, rel_type STRING, confidence STRING, source_line INT64, target_name STRING)`.

### Config and models (being extended)
- `src/glma/models.py` — `SearchConfig` model (line ~176) with `hybrid_keyword_weight`, `hybrid_vector_weight`, `similarity_threshold`. Needs `graph_weight`, `graph_depth`, `graph_fanout` fields and updated weight validator.
- `src/glma/config.py` — `load_search_config()` for file config + CLI override merging. Needs new fields threaded through.
- `src/glma/cli.py` — `search` command (line ~675). Add `--graph`, `--graph-depth`, `--graph-fanout` flags.

### Prior phase decisions (constraints)
- `.planning/phases/15-hybrid-search-query-integration/15-CONTEXT.md` — Search result format: lean markdown, scores in JSON/YAML only, no scores in markdown (D-04). Note: Phase 20's D-10/D-11 modify this for `--graph` mode only.
- `.planning/phases/19-llm-query-rewriting/19-CONTEXT.md` — Rewrite happens before engine call. Graph search receives the rewritten (or raw) query string. No interaction between rewrite and graph.

### LadybugDB vector search reference
- `.planning/todos/resolved/ladybug-vector.md` — HNSW index creation, querying, combining with graph traversals. Covers `QUERY_VECTOR_INDEX`, pre-filtering with `PROJECT_GRAPH`, post-filtering.

### Requirements
- `.planning/REQUIREMENTS.md` — HYBR-01 through HYBR-06 (3-way hybrid search requirements)
- `.planning/ROADMAP.md` — Phase 20 success criteria and key implementation notes

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`LadybugStore.traverse_relationships(chunk_ids, max_depth)`**: BFS already implemented, returns depth-annotated relationship edges. Bidirectional (outgoing + incoming). Uses visited set to prevent cycles. Directly usable as the graph traversal engine.
- **`HybridSearchEngine`**: 2-way keyword+vector engine with `search()` method returning `list[SearchResult]`. Extension point for 3-way logic — either extend this class or add a graph layer.
- **`SearchResult` dataclass**: Has `keyword_score`, `vector_score`, `combined_score`. Needs `graph_score` field added.
- **`SearchConfig`**: Pydantic model with weight validator. Needs graph fields and 3-way validator update.
- **`format_search_output()`**: Dispatch to per-format functions. Already threads `original_query`/`rewritten_query`. Need to thread `graph_enabled` flag or similar for conditional score display.

### Established Patterns
- **Weight validation**: `SearchConfig._validate_hybrid_weights()` checks `abs(total - 1.0) > 0.05`. Extend to sum 3 weights.
- **Config + CLI overrides**: `load_search_config(repo_path, overrides_dict)`. CLI flags populate overrides dict, function merges with file config.
- **Output format dispatch**: `--format` flag selects formatter. All formatters receive same data, produce different output. Graph scores follow same pattern.
- **Score combination**: `kw_weight × kw_score + vec_weight × vec_score`. Extends naturally to 3-way.

### Integration Points
- **`cli.py` `search` command**: Add `--graph` flag (bool), `--graph-depth` (int), `--graph-fanout` (int). When `--graph` is true, pass flag through to engine and formatter.
- **`search/engine.py` `HybridSearchEngine.search()`**: Add graph traversal phase after keyword+vector merge. When graph is enabled: extract top-K seeds from 2-way results, call `store.traverse_relationships()`, extract discovered chunks with depths, compute graph scores, normalize all three dimensions, combine with 3-way weights.
- **`search/engine.py` `SearchResult`**: Add `graph_score: float = 0.0` field.
- **`search/formatter.py`**: Add graph score to scores dict in JSON/YAML. Add inline annotation in markdown formats when graph is active.
- **`models.py` `SearchConfig`**: Add `graph_weight: float`, `graph_depth: int = 2`, `graph_fanout: int = 10`. Update validator to check 3-weight sum.

</code_context>

<specifics>
## Specific Ideas

- The `traverse_relationships()` method returns edges, not chunks. The planner needs to design how to extract the unique discovered chunks and their minimum depths from the edge list.
- Self-referential edges (unresolved targets: source_id == target_id) should be skipped during graph search — they don't lead anywhere useful.
- The `graph_fanout` config should limit the number of seed chunks taken from 2-way results (top-K by combined score), not per-node BFS branching. This keeps the initial seed set focused.
- When `--graph` is off, zero code changes should be visible in output or behavior — exact backward compatibility.

</specifics>

<deferred>
## Deferred Ideas

None - discussion stayed within phase scope.

</deferred>

---

*Phase: 20-3-way-hybrid-search*
*Context gathered: 2026-05-12*
