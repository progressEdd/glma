# Roadmap: glma v1.2 — Robustness & Export Formats

## Overview

Make summarization robust for real-world codebases (large chunks, any context window size) and add a compact markdown key-value export format as the new default. Three focused phases: one bug fix, one new feature, one architectural integration.

## Phases

**Phase Numbering:**
- Continues from v1.1 (Phases 5-9)
- v1.2 starts at Phase 10

- [x] **Phase 10: Chunk Truncation for Summarization** - Handle oversized chunks that exceed model context windows
- [x] **Phase 11: Markdown Key-Value Export Format** - New default export format with multi-format support
- [x] **Phase 12: Pi Agent Integration** - Pi extension for summarization with model hint resolution ✓ Complete (2026-04-19)

## Phase Details

### Phase 10: Chunk Truncation for Summarization
**Goal**: `glma index --summarize` completes without errors regardless of chunk sizes or model context window
**Depends on**: v1.1 complete (Phase 7 summarization pipeline)
**Requirements**: TRUNC-01
**Success Criteria** (what must be TRUE):
  1. Chunks exceeding a configurable character limit are truncated before being sent to the summarization provider
  2. Truncated chunks still receive a valid summary (covering their first N characters)
  3. A warning is logged when truncation occurs, including chunk ID and original vs truncated size
  4. The truncation threshold defaults to 3000 characters (~750 tokens) and is configurable via `.glma.toml` `[summarize] max_chunk_chars`
  5. A full summarization run against a large codebase (e.g., ag2-framework) completes without 400 errors
  6. All 274 existing tests still pass

### Phase 11: Markdown Key-Value Export Format
**Goal**: `glma export` outputs a compact, LLM-friendly key-value markdown format by default, with option to select other formats
**Depends on**: v1.1 complete (Phase 8 export infrastructure)
**Requirements**: KV-01, KV-02
**Success Criteria** (what must be TRUE):
  1. `glma export` without format flag outputs markdown-kv format (hierarchical headings, `key: value` pairs)
  2. `--format markdown` produces the current table-based format (backward compatible)
  3. `--format json` produces raw JSON export
  4. `--format yaml` produces YAML export
  5. All export output files (INDEX.md, ARCHITECTURE.md, RELATIONSHIPS.md, per-file .md) respect the selected format
  6. `ExportFormat` enum exists in models.py with values: `markdown_kv`, `markdown`, `json`, `yaml`
  7. Existing `--format` flag alias `-f` works
  8. All existing tests pass; new tests cover each format

### Phase 12: Pi Agent Integration
**Goal**: Pi extension can generate summaries using pi's model registry — no separate LLM server needed
**Depends on**: Phase 10 (robust summarization), Phase 11 (export format stable)
**Requirements**: PI-01, PI-02
**Success Criteria** (what must be TRUE):
  1. A pi extension exists at `~/.pi/agent/extensions/glma-summarize.ts` (or project-local)
  2. Extension registers a `glma_summarize` tool that reads chunks needing summaries from glma DB
  3. `model_hint` in `.glma.toml` resolves to an actual model via pi's registry (`fast` → cheapest, `capable` → strongest, exact ID → use that)
  4. Summaries are written back to the glma database after generation
  5. Fallback chain works: pi extension → local LLM endpoint → rule-based (no model)
  6. Named provider presets work: `--ai-provider ollama`, `--ai-provider lmstudio`, etc. with correct default URLs
  7. All existing tests pass

## Progress

**Execution Order:**
Phases execute in numeric order: 10 → 11 → 12

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 10. Chunk Truncation | 1/1 | ✓ Complete | 2026-04-14 |
| 11. Markdown Key-Value Export | 0/? | Complete    | 2026-04-14 |
| 12. Pi Agent Integration | 2/2 | ✓ Complete | 2026-04-19 |

## Notes

- Phase 10 is scoped from `.Complete/todos/Complete/2026-04-11-truncate-oversized-chunks-before-summarization.md`
- Phase 11 is scoped from `.Complete/todos/Complete/2026-04-13-add-markdown-key-value-export-format.md`
- Phase 12 is scoped from `.Complete/todos/Complete/2026-04-10-pi-agent-integration-for-summarization.md`
- The stale todo `2026-04-10-per-chunk-ai-summaries-from-local-llm.md` should be resolved (Phase 9 already shipped notebook cell summarization)
