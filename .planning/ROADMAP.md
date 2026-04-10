# Roadmap: glma v1.1 — Polish & Complete

## Overview

Close all v1.0 gaps — fix known bugs, complete unfinished features, and ship per-chunk AI summarization persisted to the database. Three trivial bug fixes, a new summarization pipeline with pluggable providers, and ARCHITECTURE.md generation for exports.

## Phases

**Phase Numbering:**
- Continues from v1.0 (Phases 1-4)
- v1.1 starts at Phase 5

- [ ] **Phase 5: Bug Fixes** - Fix export default, notebook truncation, stale placeholder
- [ ] **Phase 6: Summarization Infrastructure** - Provider protocol, DB update method, summarization pipeline
- [ ] **Phase 7: CLI Integration & Providers** - Wire up CLI flags, implement OpenAI-compatible and pi providers
- [ ] **Phase 8: ARCHITECTURE.md & Export Polish** - Generate codebase architecture summary, verify all outputs flow summaries

## Phase Details

### Phase 5: Bug Fixes
**Goal**: All three v1.0 bugs fixed — export defaults to summaries-only, notebook cells preserve comprehensions, writer output no longer shows stale placeholder
**Depends on**: Phase 4 (v1.0 complete)
**Requirements**: FIX-01, FIX-02, FIX-03
**Success Criteria** (what must be TRUE):
  1. Running `glma export` without `--no-code` produces markdown with signatures/summaries only (no full source code) — ExportConfig.include_code defaults to False
  2. Querying a Jupyter notebook containing list/dict/set comprehensions shows the full comprehension expression in the cell source — no truncation
  3. Running `glma index` produces per-file markdown where the file summary section shows the rule-based summary text, not "*(File summary not yet generated — available after Phase 3.)*"
  4. All 211 existing tests still pass after changes

### Phase 6: Summarization Infrastructure
**Goal**: Core summarization pipeline exists — provider protocol, LadybugStore update method, summarize_chunks function — ready for CLI wiring
**Depends on**: Phase 5 (bug fixes done, clean baseline)
**Requirements**: SUMM-01, SUMM-02, PROV-01
**Success Criteria** (what must be TRUE):
  1. `SummarizerProvider` protocol exists with `summarize(code: str, context: str) -> str` method
  2. `LadybugStore.update_chunk_summary(chunk_id, summary)` can update a single chunk's summary without deleting/recreating all chunks for the file
  3. `summarize_chunks(store, chunks, provider)` processes chunks, calls provider, writes summaries to DB, and returns updated chunks
  4. Re-indexing a file preserves existing summaries where content_hash hasn't changed (summaries survive upsert_chunks)
  5. Only chunks with NULL/empty summary are processed — already-summarized chunks are skipped
  6. Unit tests verify: provider protocol, DB update, incremental skip logic

### Phase 7: CLI Integration & Providers
**Goal**: Users can run `glma index --summarize` to generate per-chunk AI summaries, with configurable providers (local OpenAI-compatible or pi agent)
**Depends on**: Phase 6 (pipeline infrastructure in place)
**Requirements**: SUMM-03, PROV-02, PROV-03, PROV-04
**Success Criteria** (what must be TRUE):
  1. `glma index --summarize` runs the summarization pass after indexing, populating chunk.summary in the DB
  2. `--summarize-provider local` uses OpenAI-compatible API (Ollama, LM Studio, llama.cpp) — works with any base_url
  3. `--summarize-provider pi` uses pi's API for summarization
  4. `.glma.toml` supports `[summarize]` section with `enabled`, `provider`, `model`, `base_url` fields
  5. After summarization, `glma export` output includes per-chunk AI summaries in the markdown
  6. After summarization, `glma query <file>` output includes chunk summaries
  7. openai remains an optional dependency (`pip install glma[ai]`); non-AI installs still work
  8. Summaries appear in writer markdown output (per-file .md in .glma-index/)

### Phase 8: ARCHITECTURE.md & Export Polish
**Goal**: Exports include a codebase-level ARCHITECTURE.md derived from relationship data and summaries, giving agents instant high-level understanding
**Depends on**: Phase 7 (summaries available in DB)
**Requirements**: ARCH-01
**Success Criteria** (what must be TRUE):
  1. `glma export` generates ARCHITECTURE.md alongside INDEX.md and RELATIONSHIPS.md in the export output
  2. ARCHITECTURE.md contains: project structure overview, module dependency graph, entry points, and key interfaces derived from DB data
  3. ARCHITECTURE.md includes a timestamp header indicating when the index was generated
  4. Running export on the glma codebase itself produces a useful ARCHITECTURE.md (dogfood test)
  5. All existing tests pass; new tests cover ARCHITECTURE.md generation

## Progress

**Execution Order:**
Phases execute in numeric order: 5 → 6 → 7 → 8

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 5. Bug Fixes | 0/? | Pending | - |
| 6. Summarization Infrastructure | 0/? | Pending | - |
| 7. CLI Integration & Providers | 0/? | Pending | - |
| 8. ARCHITECTURE.md & Export Polish | 0/? | Pending | - |
