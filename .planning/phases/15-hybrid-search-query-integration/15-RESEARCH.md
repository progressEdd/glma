# Phase 15: Hybrid Search & Query Integration - Research

**Researched:** 2026-05-09
**Status:** Complete

## Research Question

What do I need to know to PLAN Phase 15 (Hybrid Search & Query Integration) well?

---

## 1. Architecture Integration Points

### 1.1 Existing Code That Directly Feeds Search

| Component | File | What It Provides |
|-----------|------|-----------------|
| `EmbeddingProvider` protocol | `embedding/providers.py` | `embed(texts: list[str]) -> list[list[float]]` — ready to embed the query string |
| `OpenAIEmbeddingProvider` | `embedding/providers.py` | Concrete implementation using OpenAI-compatible API |
| `SearchConfig` | `models.py` | `similarity_threshold`, `hybrid_keyword_weight`, `hybrid_vector_weight`, `vector_dimensions`, `embedding_provider`, `embedding_model`, `embedding_base_url` — all config fields already exist |
| `load_search_config()` | `config.py` | Loads `[search]` section from `.glma.toml` + CLI overrides + resolves provider presets |
| `LadybugStore` | `db/ladybug_store.py` | DB connection, `get_all_chunks_with_summaries()`, chunk schema with `embedding FLOAT[768]` column |
| `EMBEDDING_PROVIDER_PRESETS` | `models.py` | `embed-ollama`, `embed-lmstudio`, `embed-vllm`, `embed-llamacpp`, `embed-local` |
| `ExportFormat` enum | `models.py` | `MARKDOWN_KV`, `MARKDOWN`, `JSON`, `YAML` — search results should support all four |
| CLI embed command | `cli.py` | Reference for how to structure a new CLI command with provider instantiation |
| Output formatters | `query/formatter.py` | `format_json_output`, `format_kv_output`, `format_compact_output`, `format_yaml_output` — patterns to follow |

### 1.2 What Must Be Added

1. **New `glma search` command** in `cli.py` — new `@app.command()` function
2. **Hybrid search engine** — new module (likely `src/glma/search/` or `src/glma/search.py`)
3. **LadybugStore vector search methods** — new methods on existing `LadybugStore`:
   - `ensure_vector_index()` — `INSTALL vector; LOAD vector; CALL CREATE_VECTOR_INDEX(...)`
   - `vector_search(query_vec, k)` — `CALL QUERY_VECTOR_INDEX(...)`
   - `check_vector_index_exists()` — `CALL SHOW_INDEXES()`
4. **Fuzzy keyword scoring** — `fuzzywuzzy` or `rapidfuzz` dependency
5. **Search result formatters** — new functions following existing formatter patterns

---

## 2. LadybugDB Vector Search (HNSW)

### 2.1 Reference Documentation

LadybugDB vector search: https://volodymyrpavlyshyn.substack.com/p/vector-search-in-ladybugdb

### 2.2 Key API Calls

**Index Creation:**
```sql
INSTALL vector;
LOAD vector;

CALL CREATE_VECTOR_INDEX(
    'Chunk',                     -- table name
    'chunk_embedding_index',     -- index name
    'embedding',                 -- property (must be FLOAT[] or DOUBLE[])
    metric := 'cosine'           -- cosine similarity for text embeddings
);
```

**Vector Search (K nearest neighbors):**
```sql
CALL QUERY_VECTOR_INDEX(
    'Chunk',
    'chunk_embedding_index',
    $query_vector,
    10,                          -- K nearest neighbors
    efs := 200                   -- expand candidate set (default 200)
)
RETURN node.id, node.file_path, node.name, node.content, node.summary, distance
ORDER BY distance;
```

**Index Management:**
```sql
CALL SHOW_INDEXES() RETURN *;
CALL DROP_VECTOR_INDEX('Chunk', 'chunk_embedding_index');
```

### 2.3 Key Design Decisions for Vector Search

1. **Index creation timing**: CONTEXT.md D-15 says "during `glma embed` or as a separate step." Best approach: **create lazily on first search** (or during `glma embed`). The index should be created after embeddings exist — creating on empty table is wasteful.

2. **Index parameters**: Defaults (`mu=30, ml=60, pu=0.05, efc=200, efs=200`) are fine for codebase-scale datasets (hundreds to low thousands of chunks). No tuning needed.

3. **Distance metric**: `cosine` — correct for normalized text embeddings. Distance is 0 (identical) to 2 (opposite). Need to convert to similarity score: `similarity = 1 - distance`.

4. **`efs` tuning**: Default 200 is fine for search quality. Could expose as config option later but YAGNI for v1.

5. **Index existence check**: Before searching, check if index exists via `SHOW_INDEXES()`. If not, create it (if embeddings exist) or error with actionable message.

6. **Index staleness**: If embeddings are added/updated after index creation, the index is stale. LadybugDB HNSW index is built once from current data. After `glma embed` runs, the index should be rebuilt. Strategy: drop + recreate index after embedding, or create lazily on first search and accept potential staleness.

### 2.4 Vector Search Result Handling

- `distance` from `QUERY_VECTOR_INDEX` is cosine distance (0 = identical, 2 = opposite)
- Convert to similarity: `vector_score = 1 - distance` (range: -1 to 1, but typically 0 to 1 for similar embeddings)
- Normalize to 0-1 range for hybrid scoring

---

## 3. Fuzzy Keyword Matching

### 3.1 Library Choice

CONTEXT.md D-17 specifies `fuzzywuzzy`. Options:

| Library | Pros | Cons |
|---------|------|------|
| `fuzzywuzzy` | Proven, well-known, `token_sort_ratio` | Requires `python-Levenshtein` for speed |
| `rapidfuzz` | Drop-in replacement, faster, pure Python | Slightly different API in edge cases |

**Recommendation**: Use `rapidfuzz` (dependency `rapidfuzz>=3.0`) — it's a faster, actively maintained drop-in for fuzzywuzzy. Import: `from rapidfuzz import fuzz`. Functions: `fuzz.token_sort_ratio()`, `fuzz.partial_ratio()`, etc.

### 3.2 Fuzzy Function Selection

For matching natural language queries against chunk summaries:

- **`fuzz.token_sort_ratio(query, summary)`**: Best for queries where word order doesn't matter ("find authentication logic" vs "logic for authentication"). Splits into tokens, sorts, compares. Range 0-100.
- **`fuzz.partial_ratio(query, summary)`**: Best for short queries in long summaries. Finds best matching substring.
- **`fuzz.WRatio(query, summary)`**: Weighted combination of multiple approaches. Most robust but slower.

**Recommendation**: Use `fuzz.token_sort_ratio` as default — good balance of accuracy and speed for natural language queries vs summary text. Score normalized to 0-1 by dividing by 100.

### 3.3 Performance Consideration

For a codebase with ~1000 chunks with summaries, computing fuzzy similarity for all chunks takes:
- ~1000 × `fuzz.token_sort_ratio` calls
- Each call is ~0.1ms
- Total: ~100ms — acceptable for codebase scale

No need for indexing or pre-filtering for keyword component. Brute-force in Python is fine.

---

## 4. Hybrid Scoring Algorithm

### 4.1 Scoring Formula

From CONTEXT.md D-07:
```
combined_score = keyword_weight × keyword_score + vector_weight × vector_score
```

Where:
- `keyword_score` = `fuzz.token_sort_ratio(query, chunk.summary) / 100` → range 0-1
- `vector_score` = `1 - cosine_distance` from `QUERY_VECTOR_INDEX` → range ~0-1
- `keyword_weight` = `SearchConfig.hybrid_keyword_weight` (default 0.5)
- `vector_weight` = `SearchConfig.hybrid_vector_weight` (default 0.5)

### 4.2 Search Mode Behavior

From CONTEXT.md D-08:
- `hybrid` (default): Use config weights (0.5/0.5)
- `vector`: keyword_weight=0.0, vector_weight=1.0 — only vector search
- `keyword`: keyword_weight=1.0, vector_weight=0.0 — only fuzzy matching

### 4.3 Threshold Filtering

From CONTEXT.md D-09:
- After computing combined scores, filter out results where `combined_score < similarity_threshold`
- Default threshold: 0.5 from SearchConfig

### 4.4 Result Ranking

- Sort by `combined_score` descending
- Group by file path for output formatting
- No explicit limit on number of results — return all above threshold

---

## 5. Vector Index Lifecycle

### 5.1 Index Creation Strategy

**Option A**: Create during `glma embed` (after all embeddings stored)
- Pro: Index always ready when search runs
- Con: Requires modifying Phase 14 code, couple embed and search

**Option B**: Create lazily on first `glma search`
- Pro: Decoupled, search handles its own infrastructure
- Con: First search is slower, need to check every time

**Option C**: Create during `glma embed` AND check/recreate lazily on search
- Pro: Best of both worlds — fast search, handles stale indexes
- Con: More code

**Recommendation**: Option B (lazy creation on first search) — keeps Phase 15 self-contained, doesn't require modifying Phase 14's `glma embed`. The index creation is fast (O(n log n) with HNSW) and only happens once per session or when missing.

### 5.2 Index Staleness Handling

When `glma embed` runs after initial index creation:
- New embeddings are stored in DB but HNSW index is stale
- Options: drop+recreate, or just create on search and accept staleness

**Recommendation**: Drop and recreate on every `glma search` invocation if any embeddings have changed. Simpler than tracking staleness. Alternative: check index existence and create only if missing; add `--rebuild-index` flag for explicit rebuild.

Actually, the simplest approach: **create index on every search invocation** if vector mode is needed. For a codebase with ~1000 chunks, HNSW index creation takes <1 second. This guarantees freshness without complexity.

### 5.3 Vector Extension Loading

```python
conn.execute("INSTALL vector;")
conn.execute("LOAD vector;")
```

These are idempotent — safe to call every time. Should be called before index creation or search.

---

## 6. CLI Command Design

### 6.1 `glma search` Command Signature

Following the pattern from `glma embed` and `glma query`:

```python
@app.command()
def search(
    query: str = typer.Argument(..., help="Natural language search query."),
    search_mode: str = typer.Option("hybrid", "--search-mode", help="Search strategy: hybrid, vector, keyword."),
    format: str = typer.Option("markdown", "--format", "-f", help="Output format: markdown-kv, markdown, json, yaml."),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path."),
    repo_root: Optional[Path] = typer.Option(None, "--repo", "-r", help="Repo root directory."),
    embedding_provider: Optional[str] = typer.Option(None, "--embedding-provider", ...),
    embedding_model: Optional[str] = typer.Option(None, "--embedding-model", ...),
    embedding_base_url: Optional[str] = typer.Option(None, "--embedding-base-url", ...),
    vector_dimensions: Optional[int] = typer.Option(None, "--vector-dimensions", ...),
    similarity_threshold: Optional[float] = typer.Option(None, "--similarity-threshold", ...),
    quiet: bool = typer.Option(False, "--quiet", "-q", ...),
) -> None:
```

### 6.2 Repo Root Resolution

Same pattern as `glma query`:
1. Use `--repo` if provided
2. Walk up from CWD looking for `.glma-index/` or `.glma.toml`

### 6.3 Error Cases

| Condition | Error Message | Exit Code |
|-----------|---------------|-----------|
| No index found | "No index found. Run `glma index` first." | 4 |
| `--search-mode vector` but no embeddings | "No embeddings found. Run `glma embed` first." | 1 |
| `--search-mode hybrid` but no embeddings | Same as vector | 1 |
| `--search-mode keyword` but no summaries | "No chunk summaries found. Run `glma index --summarize` first." | 1 |
| Invalid `--search-mode` value | "search-mode must be hybrid, vector, or keyword" | 4 |
| Invalid `--format` value | "format must be one of: ..." | 4 |
| No results above threshold | "No results above threshold X. Try lowering --similarity-threshold." | 0 (not an error) |

---

## 7. Output Format Design

### 7.1 Markdown (default) — Lean Code Blocks

From CONTEXT.md D-04, D-05, D-06:

```markdown
# src/auth/login.py

```python
def authenticate(username, password):
    """Verify user credentials against stored hash."""
    ...
```
> *Summary: Verifies user credentials against stored hash*

```python
class LoginHandler:
    """Manages login sessions and token generation."""
    ...
```
> *Summary: Manages login sessions and token generation*

# src/middleware/auth.py

```python
def check_token(token):
    """Validate JWT token from request header."""
    ...
```
> *Summary: Validates JWT token from request header*
```

Key: file path as heading, code blocks with summaries. No scores, no line numbers, no metadata.

### 7.2 JSON Format

```json
{
  "query": "find authentication logic",
  "search_mode": "hybrid",
  "total_results": 3,
  "results": [
    {
      "file_path": "src/auth/login.py",
      "chunk_name": "authenticate",
      "chunk_type": "function",
      "summary": "Verifies user credentials against stored hash",
      "content": "def authenticate(username, password):\n    ...",
      "score": 0.82,
      "start_line": 15,
      "end_line": 28
    }
  ]
}
```

### 7.3 Key-Value Format

```markdown
# src/auth/login.py

name: authenticate
type: function
lines: L15-L28
score: 0.82

```python
def authenticate(username, password):
    ...
```
```

### 7.4 YAML Format

Follows same structure as JSON but in YAML.

---

## 8. Module Structure

### 8.1 Recommended Structure

```
src/glma/
├── search/
│   ├── __init__.py         # Public API: hybrid_search(), SearchResult
│   ├── engine.py           # HybridSearchEngine class
│   └── formatter.py        # Search result formatters
├── cli.py                  # Add search command
├── db/
│   └── ladybug_store.py    # Add vector search methods
└── ...
```

### 8.2 Key Classes

```python
@dataclass
class SearchResult:
    chunk_id: str
    file_path: str
    chunk_name: str
    chunk_type: str
    content: str
    summary: str
    start_line: int
    end_line: int
    keyword_score: float
    vector_score: float
    combined_score: float
```

```python
class HybridSearchEngine:
    def __init__(self, store: LadybugStore, provider: EmbeddingProvider, config: SearchConfig): ...
    def search(self, query: str, mode: str = "hybrid") -> list[SearchResult]: ...
    def _vector_search(self, query_vec: list[float], k: int) -> list[SearchResult]: ...
    def _keyword_search(self, query: str) -> list[tuple[str, float]]: ...
    def _combine_and_rank(self, keyword_results, vector_results) -> list[SearchResult]: ...
```

---

## 9. Test Strategy

### 9.1 Test Categories

1. **Unit tests** (no DB):
   - `SearchResult` dataclass construction
   - Fuzzy scoring with known inputs
   - Hybrid score computation (keyword_weight × kw + vector_weight × vec)
   - Threshold filtering
   - Search mode weight adjustment

2. **Integration tests** (with Ladybug in-memory DB):
   - Vector index creation
   - Vector search returns correct nearest neighbors
   - Hybrid search combines both scores
   - Search modes (hybrid, vector, keyword)
   - Error cases (no embeddings, no summaries)
   - Result formatting for all output types

3. **CLI tests** (typer.testing.CliRunner):
   - `glma search "test query"` basic invocation
   - `--search-mode vector/keyword/hybrid`
   - `--format json/yaml/markdown/markdown-kv`
   - Error messages for missing index, no embeddings

### 9.2 Test Fixtures

- Create in-memory Ladybug DB with known chunks + embeddings
- Use deterministic embedding vectors (not from a real model)
- Test queries with known expected results

---

## 10. Dependencies

### 10.1 New Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `rapidfuzz` | Fuzzy string matching for keyword scoring | `>=3.0` |

This is the only new dependency. Everything else (Ladybug, openai, typer, rich, pydantic) is already installed.

### 10.2 Existing Dependencies Used

- `real_ladybug` — vector index, HNSW search
- `openai` (optional) — query embedding via `OpenAIEmbeddingProvider`
- `typer` — CLI command
- `rich` — progress display, console output
- `pydantic` — `SearchConfig` validation
- `pyyaml` — YAML output format

---

## 11. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| LadybugDB vector extension API differs from documentation | High — core search won't work | Test vector index creation + search early in implementation (Wave 1) |
| HNSW index creation slow on large codebases | Medium — first search latency | Create lazily, document expected time, acceptable for codebase scale (<10k chunks) |
| Fuzzy matching too slow for large codebases | Low — brute-force is fine | ~100ms for 1000 chunks. If needed, pre-filter by file extension or limit candidates |
| Score normalization between keyword (0-100) and vector (0-1) | Medium — hybrid scoring incorrect | Normalize both to 0-1 before combining |
| Embedding dimension mismatch (stored vs query) | High — vector search fails | Validate query embedding dimensions match stored vector_dimensions before search |

---

## RESEARCH COMPLETE

**Key findings:**
1. LadybugDB HNSW vector search is well-documented and straightforward — `CREATE_VECTOR_INDEX` + `QUERY_VECTOR_INDEX`
2. All config infrastructure (`SearchConfig`, `load_search_config()`) already exists from Phase 13
3. `EmbeddingProvider` protocol is ready to embed query strings — no changes needed
4. Only one new dependency: `rapidfuzz` for fuzzy keyword matching
5. Best module structure: new `src/glma/search/` package with engine + formatter
6. Vector index creation should be lazy (on first search) to keep Phase 15 self-contained
7. Score normalization: keyword scores (0-100 from rapidfuzz) → divide by 100 → 0-1; vector scores → `1 - cosine_distance` → ~0-1
8. CONTEXT.md decisions are implementable as-is — no conflicts with technical reality
