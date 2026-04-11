# Phase 9: Notebook Cell Summarization - Context

**Gathered:** 2026-04-11
**Status:** Ready for planning

<domain>
## Phase Boundary

Notebook cells get AI-generated summaries via the existing summarization pipeline. When a user runs `glma query notebook.ipynb --summarize`, each code cell is sent through the configured LLM provider and the summary is embedded in the compacted markdown output. No LadybugStore schema changes — notebook summarization is query-time only, using the existing `SummarizerProvider` protocol.

This phase delivers: `--summarize` flag on the `query` command for notebooks, cell-level LLM summarization threaded through `compact_notebook()`, and cached summaries via a lightweight sidecar file.

</domain>

<decisions>
## Implementation Decisions

### Approach: Query-time summarization (Option B from todo)
- **D-01:** Notebook cells are NOT stored in LadybugStore. Notebooks bypass the indexing pipeline by design (Phase 3 decision). Instead, `compact_notebook()` accepts an optional `provider` parameter and summarizes cells inline during query.
- **D-02:** Summaries are cached in a `.glma-index/notebook-cache/<hash>.json` sidecar file. Keyed on content hash of each cell. Avoids re-running LLM on unchanged cells.
- **D-03:** Cache is invalidated by cell content hash (BLAKE2b, same as chunk hashing). If a cell's source changes, its summary is regenerated.

### CLI Integration
- **D-04:** `glma query notebook.ipynb --summarize` triggers summarization. Uses the same `--summarize-provider` and `--summarize-model` flags as `glma index --summarize`.
- **D-05:** When `--summarize` is not passed, `compact_notebook()` works exactly as before (rule-based only, no LLM calls).
- **D-06:** No changes to `glma index` — notebooks are still not indexed into LadybugStore.

### Output Format
- **D-07:** Summaries appear as blockquote lines above the cell's code/summary block: `> *Summary: <1-2 sentence LLM summary>*`
- **D-08:** Summaries are shown in both code-visible and code-hidden modes.

### Cache Design
- **D-09:** Cache location: `<repo_root>/.glma-index/notebook-cache/<notebook-stem>-<file-hash>.json`
- **D-10:** Cache format: `{"cells": [{"index": 0, "content_hash": "abc...", "summary": "..."}]}`
- **D-11:** Cache is per-notebook, not global. One JSON file per notebook queried with `--summarize`.

### Agent's Discretion
- Exact system prompt for cell summarization
- Whether to summarize markdown cells (probably not — they're already prose)
- Cache eviction policy (if any)
- Whether empty cells (< 3 lines) should be skipped
- Error handling when provider is unavailable (fail open with rule-based, or fail closed?)

</decisions>

<canonical_refs>
## Canonical References

### Must read before planning
- `02-worktrees/glma/src/glma/query/notebook.py` — `compact_notebook()`, `_format_cell()` — the integration point
- `02-worktrees/glma/src/glma/summarize/providers.py` — `SummarizerProvider` protocol, `OpenAICompatibleProvider`
- `02-worktrees/glma/src/glma/cli.py` — `query` command, notebook dispatch, existing `--summarize-*` flags
- `02-worktrees/glma/src/glma/config.py` — `load_summarize_config()` for provider/model config loading
- `02-worktrees/glma/src/glma/models.py` — `SummarizeConfig`, `SummarizeProvider` models

### Reference
- `02-worktrees/glma/src/glma/summarize/pipeline.py` — `summarize_chunks()` pattern (but we won't reuse it directly — cells aren't `Chunk` objects)
- `02-worktrees/glma/src/glma/index/pipeline.py` — `file_content_hash()` for content hashing pattern

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`SummarizerProvider` protocol** — `summarize(code: str, context: str) -> str` — exactly what we need per cell
- **`OpenAICompatibleProvider`** — ready to use, already handles Ollama/LM Studio/llama.cpp
- **`PiProvider`** — works inside pi environment
- **`load_summarize_config()`** in config.py — reads `.glma.toml` [summarize] section + CLI overrides
- **`file_content_hash()`** in pipeline.py — BLAKE2b pattern for content hashing

### Integration Points
- **`compact_notebook()`** — add optional `provider: SummarizerProvider` and `cache_dir: Path` parameters
- **`_format_cell()`** — add optional `summary: str` parameter, render as blockquote when present
- **CLI `query` command** — when `--summarize` passed + notebook path: load provider config, instantiate provider, create cache dir, pass to `compact_notebook()`
- **Cache** — new helper in notebook.py or separate cache module

### Established Patterns
- **Provider instantiation** (from cli.py `index` command): `OpenAICompatibleProvider(base_url=..., model=...)`
- **Config loading**: `load_summarize_config(repo_root, overrides)` returns `SummarizeConfig`
- **Content hashing**: `hashlib.blake2b(content, digest_size=32).hexdigest()`

</code_context>

<specifics>
## Specific Ideas

- The cell context string should include: notebook filename, cell index, cell type, and the section heading the cell belongs to. This gives the LLM enough context to produce a meaningful summary without seeing the entire notebook.
- Skip summarization for cells shorter than 3 non-empty lines — they're usually just imports or variable assignments that the rule-based annotator already handles.
- The cache should be lazy-created — don't create the notebook-cache directory until the first `--summarize` call for a notebook.

</specifics>

<deferred>
## Deferred Ideas

- Storing notebook cells as `Chunk` objects in LadybugStore (Option A from todo) — would enable `glma index --summarize` to cover notebooks, but requires schema changes and a notebook→chunk bridge. Defer to v2.
- Notebook-level relationship extraction (cross-notebook imports, function calls between notebooks) — out of scope.
- Streaming summaries (show partial output as cells are processed) — nice-to-have, not needed for v1.

</deferred>

---

*Phase: 09-notebook-cell-summarization*
*Context gathered: 2026-04-11*
