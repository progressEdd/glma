# Phase 7: CLI Integration & Providers - Context

**Gathered:** 2026-04-10
**Status:** Ready for planning

<domain>
## Phase Boundary

Wire up the Phase 6 summarization pipeline to the CLI. Add `--summarize` flag to `glma index`, implement two provider backends (OpenAI-compatible local LLM, pi agent extension), add `.glma.toml` [summarize] config section, and make per-chunk AI summaries flow into export/query/writer output. Export shifts from on-the-fly AI generation to reading summaries from the DB.

</domain>

<decisions>
## Implementation Decisions

### Provider Config & CLI Flags
- **D-01:** Single `[summarize]` config section in `.glma.toml` with fields: `enabled`, `provider`, `model`, `base_url` — used by both `glma index` and `glma export`. No separate export-specific AI config.
- **D-02:** `glma index --summarize` triggers the summarization pipeline after indexing, writing chunk summaries to DB via `summarize_chunks()`. `glma export` reads summaries from DB — no on-the-fly AI generation during export.
- **D-03:** Export's existing `generate_ai_summary()` function in `export.py` is replaced by DB lookups (chunk.summary field). The `--ai-summaries` flag on export becomes "include AI summaries from the index" rather than "generate now." Export's `--ai-url` and `--ai-model` flags are superseded by `[summarize]` config.
- **D-04:** One model/provider for everything — chunk summaries now, future query rewriting and embedding later. This is foundational for semantic search.

### Pi Provider
- **D-05:** Pi provider is a pi extension — it uses pi's SDK/API directly when glma runs inside the pi environment. Not a subprocess call.
- **D-06:** Pi provider is optional — glma works standalone with local LLM provider (Ollama, LM Studio, llama.cpp). Pi is the "works even better inside pi" path. The extension registers the pi backend as a `SummarizerProvider` implementation.

### Summaries in Output Paths
- **D-07:** DB `summary` field (STRING on Chunk table, from Phase 6) is the single source of truth. All three output paths read from it.
- **D-08:** When code is shown (`--include-code` / `verbose`): chunk summary appears as an italic blockquote above the code block. Pattern: `> *Summary: ...*`
- **D-09:** When summaries-only (default, no code): chunk summary appears in the heading section, replacing/supplementing the "Code omitted" / signature line.
- **D-10:** Same rendering pattern across all three output formats: export (`export.py`), query (`formatter.py`), writer (`writer.py`).

### Optional Dependency Handling
- **D-11:** `[ai]` optional dep group in pyproject.toml = `openai` package only. No separate `[pi]` group.
- **D-12:** Running `--summarize` with `local` provider without `openai` installed → clear error message: `"Summarization requires 'openai' package. Install with: pip install glma[ai]"` + exit code 1. Same pattern as existing `export.py` ImportError handling.
- **D-13:** Pi provider has no extras group — the pi extension handles its own dependency resolution. If running inside pi, it works; if not, the provider isn't available.

### Folded Todos
- **Per-chunk AI summaries from local LLM** — core Phase 7 deliverable: `--summarize` flag with local OpenAI-compatible provider
- **Pi/agent integration for code summarization** — core Phase 7 deliverable: `--summarize-provider pi` via pi extension

### Agent's Discretion
- Exact prompt template for chunk summarization (system message, max_tokens)
- Exact `[summarize]` config field names and defaults (as long as they cover enabled/provider/model/base_url)
- How to handle the export command's deprecated `--ai-summaries`/`--ai-url`/`--ai-model` flags (remove, keep as aliases, or show deprecation warning)
- Error retry logic for individual chunk summarization failures
- Progress display during summarization pass (Rich progress bar reuse, spinner, etc.)
- Exact formatting of the summary blockquote line in markdown output

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase 6 infrastructure (MUST read — this phase builds directly on it)
- `02-worktrees/glma/src/glma/summarize/providers.py` — `SummarizerProvider` protocol definition
- `02-worktrees/glma/src/glma/summarize/pipeline.py` — `summarize_chunks()` function (store, chunks, provider → updated chunks)
- `02-worktrees/glma/src/glma/summarize/__init__.py` — Package exports
- `02-worktrees/glma/src/glma/db/ladybug_store.py` §L169-180 — `update_chunk_summary()` method; also `upsert_chunks()` preserves summaries via content_hash matching

### CLI & Config (modification targets)
- `02-worktrees/glma/src/glma/cli.py` — `index` command (add `--summarize`, `--summarize-provider`, `--summarize-model` flags); `export` command (refactor `--ai-summaries`/`--ai-url` to use [summarize] config)
- `02-worktrees/glma/src/glma/config.py` — Add `load_summarize_config()` following existing pattern (`load_config`, `load_watch_config`, `load_export_config`)
- `02-worktrees/glma/src/glma/models.py` — Add `SummarizeConfig` model with provider enum; `ExportConfig` ai_* fields may be deprecated

### Output paths (must add chunk summary rendering)
- `02-worktrees/glma/src/glma/export.py` — `_format_export_file()` (add chunk summary to Chunks section); `generate_ai_summary()` to be removed/replaced by DB lookup
- `02-worktrees/glma/src/glma/query/formatter.py` — `_format_signature_block()` and `_format_verbose_code()` (add chunk summary)
- `02-worktrees/glma/src/glma/index/writer.py` — `format_file_markdown()` (add chunk summary above code block)

### Config & packaging
- `02-worktrees/glma/pyproject.toml` — Add `[project.optional-dependencies] ai = ["openai"]`
- `.glma.toml` (if example exists) — New `[summarize]` section pattern

### Project context
- `.planning/codebase/CONVENTIONS.md` — Typer CLI pattern, Pydantic config models
- `.planning/codebase/STRUCTURE.md` — Source in `02-worktrees/glma/src/glma/`
- `.planning/codebase/STACK.md` — Python 3.13, Typer, Rich, Pydantic

### Prior phase decisions
- `.planning/phases/04-file-watching-air-gapped-export/04-CONTEXT.md` — Export design, rule-based summaries, three output modes
- `.planning/phases/05-bug-fixes/05-CONTEXT.md` — `--include-code` flag pattern (positive opt-in), summaries.py shared module

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`SummarizerProvider` protocol** (`summarize/providers.py`): `summarize(code: str, context: str) -> str` — Phase 6 defined this, Phase 7 implements concrete providers
- **`summarize_chunks()`** (`summarize/pipeline.py`): Full pipeline — iterates chunks, skips already-summarized, calls provider, writes to DB, logs stats. Ready to call from CLI.
- **`LadybugStore.update_chunk_summary()`** (`db/ladybug_store.py:169`): DB update method working
- **`ExportConfig`** (`models.py`): Already has `ai_summaries`, `ai_base_url`, `ai_model` fields — can be refactored to pull from `[summarize]` config
- **`generate_ai_summary()`** (`export.py`): Working OpenAI-compatible file-level summarization — pattern to adapt for chunk-level provider, then remove
- **`load_export_config()`** (`config.py`): Config merge pattern to follow for `load_summarize_config()`

### Established Patterns
- **Config loading**: `tomllib` → `.glma.toml` section → merge with CLI overrides → Pydantic model. Three existing examples to follow.
- **CLI flags**: `typer.Option()` with defaults, Rich console for output
- **Optional deps**: `try: from openai import OpenAI` with `except ImportError` fallback (already in `export.py`)
- **Progress display**: Rich progress bar in `index/progress.py`, Rich console throughout

### Integration Points
- **`cli.py:index` command**: Add summarize flags, call `summarize_chunks()` after `run_index()` completes
- **`cli.py:export` command**: Refactor to read chunk summaries from DB instead of generating on-the-fly
- **`export.py:_format_export_file()`**: Add chunk.summary rendering in Chunks section
- **`formatter.py:_format_signature_block()`**: Add chunk.summary in signature output
- **`writer.py:format_file_markdown()`**: Add chunk.summary above code block
- **`config.py`**: New `load_summarize_config()` function
- **`models.py`**: New `SummarizeConfig` model, `SummarizeProvider` enum

</code_context>

<specifics>
## Specific Ideas

- The pi extension model: "glma works standalone with local LLMs, and works even better inside pi." The pi provider is an extension that registers itself as a SummarizerProvider when running in the pi environment. Not a subprocess, not a separate install.
- Export reading from DB instead of generating on-the-fly means: if you run `glma index --summarize`, summaries are persisted. Later `glma export` just reads them. No model needed at export time.
- Chunk summary rendering is consistent: italic blockquote above code (when code shown), or in the heading section (summaries-only mode). Same pattern across export, query, and writer.
- One model/provider for everything is strategic — future vector/hybrid search will use the same model for query rewriting, ensuring semantic consistency between how summaries were written and how queries are rephrased.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

### Reviewed Todos (not folded)
The following todos matched Phase 7 but belong to other phases (already completed or planned):
- **Default markdown export to summaries only** — completed in Phase 5 (FIX-01)
- **Fix notebook cell source truncation in compaction** — completed in Phase 5 (FIX-02)
- **Replace stale Phase 3 placeholder in writer markdown** — completed in Phase 5 (FIX-03)
- **Generate codebase architecture summary file** — belongs to Phase 8 (ARCH-01)

</deferred>

---

*Phase: 07-cli-integration-providers*
*Context gathered: 2026-04-10*
