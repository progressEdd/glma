# Pitfalls Research

**Domain:** Adding AI summarization to an existing codebase indexer
**Researched:** 2026-04-10
**Confidence:** HIGH

## Critical Pitfalls

### Pitfall 1: Summaries Lost on Re-index

**What goes wrong:**
`LadybugStore.upsert_chunks()` does `DETACH DELETE` + re-create for all chunks. When a file is re-indexed (even if just a whitespace change), all chunk summaries are destroyed.

**Warning signs:**
- Users run `glma index`, summarize, then `glma watch` triggers re-index → summaries gone
- Incremental re-index during watch mode is the most common trigger

**Prevention:**
- Add `update_chunk_summary()` method that does targeted UPDATE instead of full delete+recreate
- Before `upsert_chunks()` deletes, read existing summaries and re-attach to new chunks where content_hash matches
- Phase to address: Summarization infrastructure phase (first phase that writes summaries)

### Pitfall 2: Local Model Rate Limiting / Timeouts

**What goes wrong:**
Small local models (3-7B params) can only handle 1-2 concurrent requests. If you batch 50 chunks at a model running on CPU, it either OOMs or times out. The existing `generate_ai_summary()` has a 10-second timeout — too short for larger code chunks on slow hardware.

**Warning signs:**
- Timeout exceptions on first real codebase test (>100 files)
- Model server crashes mid-summarization
- Half-summarized codebase with no resume capability

**Prevention:**
- Default to sequential processing (batch_size=1), not parallel
- Increase timeout to 30s+ for per-chunk summarization
- Resume capability: only summarize chunks where summary IS NULL
- Log failures per-chunk, don't abort entire run
- Phase to address: CLI integration phase

### Pitfall 3: Summary Token Limits

**What goes wrong:**
Sending a 500-line function as context to a small model produces truncated or garbage summaries. The existing `generate_ai_summary()` sends `chunk.content` but truncates at 20 chunks — it doesn't truncate individual chunk size.

**Warning signs:**
- Garbage summaries for large functions/classes
- Token limit errors from local models
- Inconsistent summary quality (short functions fine, large classes terrible)

**Prevention:**
- Truncate individual chunk content to ~2000 chars before sending to LLM
- For very large chunks, send signature + first N lines only
- Keep the prompt focused: "What does this function do?" not "Summarize everything"
- Phase to address: Summarization infrastructure phase

### Pitfall 4: Pi Provider Assumption

**What goes wrong:**
Building PiAgentProvider before understanding pi's API surface. If pi's agent API doesn't expose a simple "summarize this text" endpoint, the provider needs a different approach (e.g., calling pi as a subprocess, or using pi's SDK).

**Warning signs:**
- Pi provider is stubbed out with TODO comments
- HTTP 401/403 errors because pi requires auth
- Provider works in dev but breaks in production pi environment

**Prevention:**
- Research pi's actual API/SDK before implementing PiAgentProvider
- Keep provider protocol simple so pi backend can be any shape
- Fallback: if pi provider fails, gracefully degrade to rule-based summaries
- Phase to address: Provider implementations phase

### Pitfall 5: Notebook Truncation Regression

**What goes wrong:**
The notebook cell source truncation bug affects list comprehensions — they get stripped. Fixing this requires understanding the exact nbformat parsing code. A naive fix (e.g., stripping by regex) could break other cell types or introduce new truncation for dict comprehensions, generator expressions, etc.

**Warning signs:**
- Fix works for `[x for x in y]` but breaks `{k: v for k, v in d.items()}`
- Markdown cells lose formatting
- Cell outputs disappear

**Prevention:**
- Add specific test cases for: list comp, dict comp, set comp, generator expression, ternary expression
- Check existing tests — 211 tests should catch regressions
- Read notebook.py carefully before touching it
- Phase to address: Bug fixes phase (first phase)

### Pitfall 6: ARCHITECTURE.md Becomes Stale

**What goes wrong:**
ARCHITECTURE.md is generated during export. If the index is stale (files changed since last `glma index`), the architecture summary is wrong. Unlike per-file markdown (which has stale warnings), ARCHITECTURE.md looks authoritative.

**Warning signs:**
- Users trust ARCHITECTURE.md as "the truth" even when index is outdated
- Architecture shows deleted files as active components

**Prevention:**
- Add timestamp header to ARCHITECTURE.md: "Generated from index at [timestamp]"
- Add stale check: compare file count in index vs on disk, warn if mismatch
- Phase to address: Export enhancement phase

## Integration Pitfalls

### Importing openai as Hard Dependency

The codebase currently imports openai conditionally (`try: from openai import OpenAI`). Making it a hard dependency would break installs for users who only want rule-based summaries.

**Prevention:** Keep openai as optional dependency. Add `[ai]` extra to pyproject.toml: `pip install glma[ai]`.

### Config Breaking Change

Adding `[summarize]` section to `.glma.toml` should be backward-compatible — old configs without it should work fine (summarization disabled by default).

---
*Pitfalls research for: per-chunk AI summarization with pluggable providers*
*Researched: 2026-04-10*
