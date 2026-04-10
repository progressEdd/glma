# Phase 7: CLI Integration & Providers - Research

**Date:** 2026-04-10
**Phase:** 7 - CLI Integration & Providers
**Status:** Complete

## Research Question
What do I need to know to PLAN this phase well?

---

## 1. Existing Infrastructure (Phase 6 deliverables)

### SummarizerProvider Protocol
- **File:** `summarize/providers.py`
- Protocol with single method: `summarize(code: str, context: str) -> str`
- No base class — uses Python `Protocol` (structural typing)
- Phase 7 needs two concrete implementations: `OpenAICompatibleProvider` and `PiProvider`

### Summarization Pipeline
- **File:** `summarize/pipeline.py`
- `summarize_chunks(store, chunks, provider)` — fully functional
- Iterates chunks, skips already-summaried (incremental), calls provider, writes to DB
- Returns updated chunks list with summaries populated
- Logs stats: summarized, skipped, failed counts
- Ready to call from CLI — just needs a provider instance

### DB Layer
- **File:** `db/ladybug_store.py`
- `update_chunk_summary(chunk_id, summary)` — targeted SET query, no delete/recreate
- `upsert_chunks()` preserves existing summaries via content_hash matching
- Summary field: `STRING` on Chunk table, defaults to empty string

### What's Missing (Phase 7 Scope)
- No concrete provider implementations
- No CLI flags (`--summarize`, `--summarize-provider`, `--summarize-model`)
- No `[summarize]` config section in `.glma.toml`
- No `SummarizeConfig` Pydantic model
- No `load_summarize_config()` function
- Chunk summaries not rendered in export/query/writer output
- Export still has `generate_ai_summary()` for on-the-fly generation (to be replaced)
- No `[ai]` optional dependency group in pyproject.toml

---

## 2. CLI Integration Points

### `cli.py:index` command (primary target)
Current flow:
1. Parse args → build CLI overrides
2. `load_config()` → IndexConfig
3. `run_index()` → indexing result
4. Print summary

**Required changes:**
- Add flags: `--summarize` (bool), `--summarize-provider` (str: "local"|"pi"), `--summarize-model` (str)
- After `run_index()`, if summarize enabled: load SummarizeConfig, instantiate provider, call `summarize_chunks()`
- Need to pass store from `run_index()` to summarization step
- Progress display during summarization (Rich spinner/progress bar)

### `cli.py:export` command (refactor target)
Current: `--ai-summaries` triggers `generate_ai_summary()` at export time.
**Change:** Export reads chunk.summary from DB. The `--ai-summaries` flag becomes "include AI summaries from index" (reading what's there). Remove `--ai-url` and `--ai-model` flags (superseded by `[summarize]` config).

### `config.py` patterns
Three existing `load_*` functions follow identical pattern:
1. Read `.glma.toml` → extract section
2. Merge with `cli_overrides` dict
3. Return Pydantic model

New function: `load_summarize_config(repo_root, cli_overrides)` → `SummarizeConfig`

### `models.py` additions needed
- `SummarizeProvider` enum: `LOCAL = "local"`, `PI = "pi"`
- `SummarizeConfig` Pydantic model: `enabled`, `provider`, `model`, `base_url` fields

---

## 3. Output Path Rendering Changes

### Current behavior (no chunk summaries shown)
All three output paths currently ignore `chunk.summary`:

**`export.py:_format_export_file()`**
- Chunks section: shows code or "Code omitted" — no summary rendering
- Summary section: uses `generate_rule_summary()` or `generate_ai_summary()` for file-level summary only

**`query/formatter.py:_format_signature_block()`**
- Shows: name, type, line range, docstring from comments, relationships
- Missing: chunk.summary rendering

**`query/formatter.py:_format_verbose_code()`**
- Shows: name + full code block
- Missing: chunk.summary above code block

**`index/writer.py:format_file_markdown()`**
- Shows: chunk heading + comments + code block + inline relationships
- Missing: chunk.summary rendering

### Required rendering pattern (from CONTEXT.md D-08, D-09)
- **With code** (`--include-code`/`--verbose`): `> *Summary: ...*` italic blockquote above code block
- **Without code** (default): chunk summary in heading section, replacing/supplementing "Code omitted" line
- Consistent across all three output formats

### Specific insertion points

**export.py `_format_export_file()` line ~130-150 (Chunks section):**
```python
# After chunk heading, before code/omitted line:
if chunk.summary:
    lines.append(f"> *Summary: {chunk.summary}*")
    lines.append("")
```
And in the "code omitted" branch:
```python
else:
    if chunk.summary:
        lines.append(chunk.summary)
    else:
        lines.append(f"*(Code omitted. Signature: L{chunk.start_line}-L{chunk.end_line})*")
```

**formatter.py `_format_signature_block()`:**
After docstring display, before relationships:
```python
if chunk.summary:
    lines.append(f"> *Summary: {chunk.summary}*")
    lines.append("")
```

**formatter.py `_format_verbose_code()`:**
After chunk name heading, before code block:
```python
if chunk.summary:
    lines.append(f"> *Summary: {chunk.summary}*")
    lines.append("")
```

**writer.py `format_file_markdown()` in chunk loop:**
After chunk heading, before comments/code:
```python
if chunk.summary:
    lines.append(f"> *Summary: {chunk.summary}*")
    lines.append("")
```

---

## 4. Provider Implementations

### OpenAI-Compatible Provider (PROV-02)
- Uses `openai` Python package (optional dep)
- Works with Ollama (`http://localhost:11434/v1`), LM Studio (`http://localhost:1234/v1`), llama.cpp server
- Pattern already exists in `export.py:generate_ai_summary()` — adapt for per-chunk use
- Constructor: `OpenAICompatibleProvider(base_url: str, model: str, api_key: str = "not-needed")`
- System prompt for chunk summarization (hardcoded, per D-04/agent's discretion)
- Needs `try/except ImportError` for openai package

### Pi Provider (PROV-03)
- Uses pi's SDK/API directly when glma runs inside pi
- Not a subprocess — pi extension model
- Registers as a SummarizerProvider when pi environment detected
- No `[pi]` extras group — extension handles its own deps
- Implementation details: agent's discretion (CONTEXT.md D-05, D-06)
- Minimal stub for now: detect pi environment, use pi API

---

## 5. Configuration Design

### `.glma.toml` [summarize] section
```toml
[summarize]
enabled = false
provider = "local"          # "local" or "pi"
model = "default"
base_url = "http://localhost:1234/v1"
```

### SummarizeConfig model
```python
class SummarizeConfig(BaseModel):
    enabled: bool = False
    provider: str = "local"     # or use SummarizeProvider enum
    model: str = "default"
    base_url: str = "http://localhost:1234/v1"
```

### Config resolution priority
CLI flags > `.glma.toml` [summarize] > defaults
Same pattern as existing `load_config()`, `load_watch_config()`, `load_export_config()`

---

## 6. Optional Dependency Handling

### pyproject.toml addition
```toml
[project.optional-dependencies]
ai = ["openai"]
```
No separate `[pi]` group (D-11).

### Import guard pattern (already used in export.py)
```python
try:
    from openai import OpenAI
except ImportError:
    # Error message + exit
```

Applied to: `OpenAICompatibleProvider` instantiation, not import time.
Provider module can import without openai, but provider instantiation checks.

---

## 7. Export Command Refactoring

### Current export AI flow
1. `--ai-summaries` flag triggers `generate_ai_summary()` during export
2. `generate_ai_summary()` calls OpenAI API for file-level summary
3. `--ai-url` and `--ai-model` configure the API

### New export flow
1. `--ai-summaries` flag means "include chunk summaries from DB in output" (reading, not generating)
2. File-level summary: still uses `generate_rule_summary()` + optionally reads chunk summaries for richer context
3. Remove `--ai-url` and `--ai-model` from export command (superseded by [summarize] config)
4. `generate_ai_summary()` function: remove or convert to read chunk summaries from DB
5. Per-chunk summaries flow through `_format_export_file()` rendering

---

## 8. Testing Strategy

### Existing test files to extend
- `test_config.py` — add `load_summarize_config()` tests
- `test_cli.py` — add `--summarize` flag tests
- `test_export.py` — update for summary rendering, remove AI generation tests
- `test_query_formatter.py` — add chunk summary rendering tests
- `test_writer.py` — add chunk summary rendering tests
- `test_summarize.py` — add provider tests (OpenAI-compatible mock)

### New test files
- `test_providers.py` — provider instantiation, ImportError handling, summarize method

### Test patterns
- Mock OpenAI client for provider tests
- Create chunks with `.summary` set for rendering tests
- Test config merge: file config + CLI overrides

---

## 9. Risk Assessment

### Low Risk
- Config loading (established pattern, 3 existing examples)
- Output rendering (inserting a blockquote line in 4 locations)
- CLI flag addition (simple typer.Option additions)

### Medium Risk
- Export command refactoring (removing `generate_ai_summary()`, changing flag semantics)
- Pi provider stub (needs research on pi SDK, but can be minimal for Phase 7)

### Dependencies
- Phase 6 complete ✓ — all infrastructure in place
- `openai` package is optional — only needed for `local` provider
- No breaking changes to DB schema (summary field already exists)

---

## RESEARCH COMPLETE

Phase 7 is well-scoped with clear integration points. The Phase 6 infrastructure (`SummarizerProvider` protocol, `summarize_chunks()` pipeline, `update_chunk_summary()` DB method) provides a solid foundation. Main work is wiring (CLI flags → config → provider instantiation → pipeline call) and rendering (chunk.summary in 4 output locations).
