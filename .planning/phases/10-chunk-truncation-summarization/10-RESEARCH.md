# Phase 10: Chunk Truncation for Summarization - Research

**Researched:** 2026-04-14
**Status:** Complete
**Phase Goal:** `glma index --summarize` completes without errors regardless of chunk sizes or model context window

---

## Research Question

*"What do I need to know to PLAN this phase well?"*

---

## 1. Current Pipeline Architecture

### Summarization Flow (Source Files)

```
cli.py::index() --summarize flag
  → load_summarize_config() → SummarizeConfig
  → instantiate provider (OpenAICompatibleProvider | PiProvider)
  → for each file: store.get_chunks_for_file() → summarize_chunks(store, chunks, provider)
  → pipeline.py::summarize_chunks()
      → for each chunk without summary:
          → provider.summarize(chunk.content, context)
          → store.update_chunk_summary(chunk.id, summary)
      → on exception: log warning, skip chunk, continue
```

### Key Integration Point

`summarize_chunks()` in `pipeline.py` is the **sole entry point** for source file summarization. It already has:
- Per-chunk try/except (line 48-55)
- Failure logging with chunk ID (line 54)
- Skip-and-continue on failure (line 55)
- No awareness of chunk relationships (parent_id)

### Summarization Flow (Notebooks)

```
cli.py::query() --summarize on .ipynb file
  → compact_notebook() in query/notebook.py
  → for each code cell with ≥3 lines:
      → provider.summarize(cell.source + truncated_outputs, context)
  → on exception: pass (fail open, no summary)
```

Notebook cells are typically small (< 500 chars). The `_format_outputs_for_context()` already truncates outputs to 1500 chars. **Notebook path does NOT need protection** — cells rarely exceed context limits.

---

## 2. Provider Error Patterns

### OpenAI-Compatible API Error

The original error from the todo:
```
Error code: 400 - {'error': 'The number of tokens to keep from the initial prompt
is greater than the context length (n_keep: 8312>= n_ctx: 4096).'}
```

The OpenAI Python client raises `openai.BadRequestError` for 400 responses. This is a subclass of `openai.APIStatusError`.

**Detection strategy:** Catch the exception, check if it's a context-length/token-limit error by inspecting the error message string. Key patterns:
- `"context length"` (case-insensitive)
- `"context_length"`
- `"n_keep"` (llama.cpp specific)
- `"max.*token"` 
- Status code 400

**Important:** The current code catches ALL exceptions generically (`except Exception as e`). The decomposition strategy needs to:
1. Catch the specific error type for context-length failures
2. Attempt decomposition
3. If decomposition also fails, fall through to the existing skip behavior

### PiProvider Error

The PiProvider calls `agent.run(prompt, model=self._model)`. Error patterns are unknown but likely similar API-level errors. The same try/decompose/skip pattern applies.

---

## 3. Chunk Hierarchy (parent_id) in LadybugStore

### How parent_id Works

From `chunks.py::_walk_chunks()`:
- For Python `class_definition` nodes: tree-sitter extracts the full class (including all method bodies) as one `CLASS` chunk
- Each method inside the class is extracted as a separate `METHOD` chunk with `parent_id = class_chunk.id`
- Both class and method chunks are stored in LadybugStore

### LadybugStore Access Patterns

Available queries:
- `get_chunks_for_file(file_path)` → returns ALL chunks (class + method) ordered by start_line
- `update_chunk_summary(chunk_id, summary)` → updates a single chunk's summary
- **No existing method** to query chunks by `parent_id`

**Gap:** To find method children of a class chunk, the pipeline must:
1. Load all chunks for the file via `get_chunks_for_file()`
2. Filter in-memory by `parent_id == class_chunk.id`

This is acceptable because `summarize_chunks()` already receives the full chunk list per file (passed from `cli.py` line ~137).

### AgentBuilder Example (from CONTEXT.md)

```
AgentBuilder class chunk: 32,475 chars
├── Class-level: 4,896 chars (docstring, prompt templates, class vars)
└── 11 method chunks (parent_id = AgentBuilder's chunk id)
    ├── build_from_library: 6,965 chars
    ├── build: 5,325 chars
    └── ... 9 more (71-4,936 chars each)
```

The class chunk contains **all method bodies redundantly** (tree-sitter captures the full class text). The methods are also separate chunks. This means:
- Class chunk: 32,475 chars (redundant — methods are duplicated)
- Sum of method chunks: 27,579 chars (unique per-method content)

---

## 4. Decomposition Strategy Analysis

### Strategy A: Class Decomposition (for chunks with method children)

**When:** Provider returns context-length error AND chunk has children with `parent_id == chunk.id`

**How:**
1. Find method children from the in-memory chunk list
2. Summarize each method child individually (these are smaller, should fit)
3. Extract "class header" from the class chunk (everything before first method, or first N lines)
4. Send class header + method summaries to provider: "Summarize this class based on its component summaries"
5. Store the result as the class chunk's summary

**Risk:** If a single method is also too large, it needs map-reduce (Strategy B). This creates recursion.

### Strategy B: Map-Reduce (for standalone oversized chunks)

**When:** Provider returns context-length error AND chunk has NO method children (or is itself a method)

**How:**
1. Split chunk content into overlapping segments (e.g., 2000 chars with 200 char overlap)
2. Summarize each segment individually
3. Combine segment summaries and send to provider for final summary

**Risk:** Each segment still needs to fit in context. If segments are too large, this fails recursively.

### Strategy Selection

CONTEXT.md decisions D-03 specify:
- Class with method children → class decomposition
- Standalone oversized chunk → map-reduce

This is clean. The pipeline should:
1. Try sending chunk as-is
2. On context-length error:
   a. Check if chunk has method children → class decompose
   b. No method children → map-reduce
3. If decomposition also fails → skip (existing behavior)

---

## 5. Token Estimation Approaches

### Auto Mode (tiktoken available)

**Prerequisite:** tiktoken installed (optional, not currently in dependencies)

The CONTEXT.md specifies adding tiktoken as an optional dependency alongside openai in the `[ai]` extras. When available:
1. Query the provider's `/models` endpoint for max context length
2. Tokenize the chunk + system prompt to count tokens
3. If chunk fits → send as-is (proactive, saves an API call)
4. If chunk doesn't fit → decompose directly without trying

**Implementation note:** tiktoken's `cl100k_base` encoding is the most common. For non-OpenAI models (Ollama, LM Studio), the tokenizer may differ, but cl100k_base is a reasonable approximation.

### Manual Mode (tiktoken unavailable)

Use character-based estimation: `estimated_tokens = len(content) // 4`
Compare against `max_chunk_chars` config value (default 3000 chars ≈ 750 tokens).

**This mode is advisory only** — it logs warnings but still sends the chunk. The actual hard limit is the provider's rejection.

### tiktoken Dependency

Currently `pyproject.toml` has:
```toml
[project.optional-dependencies]
ai = ["openai"]
```

To add tiktoken: change to `ai = ["openai", "tiktoken"]`. This is backward-compatible — users who already have `glma[ai]` will get tiktoken on next `uv sync`. During development, use `uv add --optional ai tiktoken` to add it to the extras group.

---

## 6. Config Surface

### SummarizeConfig Addition

Current `SummarizeConfig` in `models.py`:
```python
class SummarizeConfig(BaseModel):
    enabled: bool = Field(default=False, ...)
    provider: SummarizeProvider = Field(default=SummarizeProvider.LOCAL, ...)
    model: str = Field(default="default", ...)
    base_url: str = Field(default="http://localhost:1234/v1", ...)
```

**New field:** `max_chunk_chars: int = Field(default=3000, description="Max chars per chunk before decomposition triggers")`

### CLI Flag Addition

In `cli.py::index()`, add:
```python
max_chunk_chars: Optional[int] = typer.Option(
    None,
    "--max-chunk-chars",
    help="Max chars per chunk for summarization (default: 3000). Triggers decomposition if exceeded.",
)
```

Wire it to `summarize_overrides["max_chunk_chars"] = max_chunk_chars` when set.

### Config Loading

`config.py::load_summarize_config()` already handles `[summarize]` section from `.glma.toml` with CLI overrides. Adding `max_chunk_chars` to the model is sufficient — no config.py changes needed.

---

## 7. Logging Requirements

From CONTEXT.md decisions D-13, D-14, D-15:

| Event | Level | Message Content |
|-------|-------|-----------------|
| Chunk triggers decomposition | WARNING | chunk_id, original size, strategy (class-decompose or map-reduce) |
| Decomposition succeeds | INFO | chunk_id, number of sub-summaries combined |
| Decomposition also fails | WARNING | chunk_id, failure reason |

---

## 8. Test Strategy

### Existing Tests (must not break)

- `test_summarize.py` — 8 tests covering pipeline protocol, DB persistence, skip-on-failure
- `test_providers.py` — 6 tests covering OpenAI and Pi providers
- `test_config.py` — tests SummarizeConfig loading
- 274 total tests across the project

### New Tests Needed

1. **Test context-length error detection** — Mock provider raises BadRequestError, verify decomposition triggers
2. **Test class decomposition** — Chunk with method children → methods summarized individually → class summary built from parts
3. **Test map-reduce** — Standalone large chunk → split, summarize segments, combine
4. **Test max_chunk_chars config** — Verify SummarizeConfig accepts and validates the field
5. **Test --max-chunk-chars CLI** — Verify CLI flag overrides config
6. **Test decomposition failure** — Sub-chunks also too large → graceful skip
7. **Test parent_id lookup** — Verify filtering chunks by parent_id finds method children

---

## 9. Files to Modify

| File | Changes |
|------|---------|
| `src/glma/summarize/pipeline.py` | Core decomposition logic: error detection, class-decompose, map-reduce |
| `src/glma/models.py` | Add `max_chunk_chars` field to `SummarizeConfig` |
| `src/glma/cli.py` | Add `--max-chunk-chars` flag, wire to config |
| `src/glma/summarize/providers.py` | No changes needed (protocol unchanged) |
| `pyproject.toml` | Add `tiktoken` to `[ai]` extras |
| `tests/test_summarize.py` | New tests for decomposition |
| `tests/test_config.py` | Test new config field |
| `tests/test_cli.py` | Test new CLI flag |

---

## 10. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Recursive decomposition (class→methods→map-reduce) | Set max recursion depth (1 level). If a single method is too large, map-reduce it. Don't go deeper. |
| tiktoken not matching non-OpenAI model tokenizers | Use tiktoken as proactive optimization only. The actual limit is enforced by the provider's rejection. |
| `/models` endpoint not available or doesn't return context length | Fall back to `max_chunk_chars` config value. Don't block summarization on auto-detection failure. |
| Decomposition adds significant latency for large classes | Acceptable trade-off: correctness > speed. The original behavior was to fail entirely. |
| Class "header" extraction is imprecise | Use a simple heuristic: everything before the first `def ` line at the class indent level, or first N lines if no methods found in text. |

---

## 11. Key Findings for Planner

1. **summarize_chunks() is the single integration point** — all decomposition logic goes here
2. **No LadybugStore method needed** — chunk list is already in memory, filter by parent_id
3. **Notebook path doesn't need changes** — cells are small, already has output truncation
4. **tiktoken is optional** — add to [ai] extras, auto mode activates when installed
5. **The class decomposition depends on method children already being separate chunks** — this is guaranteed by `_walk_chunks()` in chunks.py
6. **The decomposition is invisible to consumers** — same `chunk.summary` field, same DB update, same output

---

## RESEARCH COMPLETE
