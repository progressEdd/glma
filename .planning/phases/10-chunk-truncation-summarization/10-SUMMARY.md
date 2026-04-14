---
plan: 10-01
phase: 10-chunk-truncation-summarization
status: complete
executor: gsd-executor
completed: "2026-04-14"
---

# Plan 01: Decomposition Pipeline for Oversized Chunks — Summary

## Objective
Add try-first, decompose-on-failure logic to the summarization pipeline so oversized chunks are summarized via decomposition instead of failing.

## What Was Built

### 1. Config Field (`src/glma/models.py`)
- Added `max_chunk_chars: int = Field(default=3000, ge=100)` to `SummarizeConfig`
- Configurable via `.glma.toml` `[summarize]` section or `--max-chunk-chars` CLI flag

### 2. CLI Flag (`src/glma/cli.py`)
- Added `--max-chunk-chars` optional integer flag to `index()` command
- Wired into `summarize_overrides` dict, merged with file config via `load_summarize_config()`
- Passes `max_chunk_chars=summ_cfg.max_chunk_chars` to `summarize_chunks()` call site

### 3. Decomposition Helpers (`src/glma/summarize/pipeline.py`)
- `_is_context_length_error(exc)` — detects context-length errors from OpenAI-compatible APIs
- `_extract_class_header(content)` — extracts class docstring/vars before first method def
- `_map_reduce_summarize(content, context, provider)` — splits oversized content into overlapping segments, summarizes each, combines
- `_decompose_class_chunk(chunk, children, ...)` — summarizes method children individually, then composes class summary
- `_attempt_decomposition(chunk, ...)` — routes to class decomposition or map-reduce based on children

### 4. Pipeline Integration (`src/glma/summarize/pipeline.py`)
- `summarize_chunks()` now catches context-length errors and attempts decomposition
- Logs advisory warning for chunks exceeding `max_chunk_chars` threshold
- Builds `children_by_parent` lookup for efficient class decomposition
- Reports decomposed count alongside summarized/skipped/failed counts

### 5. Tests (`tests/test_summarize.py`)
- 15 new tests across 4 test classes:
  - `TestIsContextLengthError` (5 tests) — positive/negative error detection
  - `TestExtractClassHeader` (3 tests) — header extraction, no-methods, truncation
  - `TestMapReduceSummarize` (2 tests) — splitting+combining, total failure
  - `TestDecompositionIntegration` (5 tests) — class decomposition, map-reduce, graceful failure, config defaults

## Key Decisions
- **Try-first approach**: Always attempt direct summarization first, only decompose on context-length error. This avoids unnecessary complexity for chunks that fit.
- **Two decomposition strategies**: Class chunks with method children use hierarchical decomposition; standalone chunks use map-reduce.
- **Graceful degradation**: Decomposition failures are logged but don't crash the pipeline — chunk is skipped.

## Verification Results
- All 289 tests pass (274 existing + 15 new)
- `glma index --help` shows `--max-chunk-chars` flag
- All 5 helper functions present in pipeline.py
- Config field and CLI wiring verified

## Files Modified
- `src/glma/models.py` — Added `max_chunk_chars` field
- `src/glma/cli.py` — Added `--max-chunk-chars` flag, updated call site
- `src/glma/summarize/pipeline.py` — Added decomposition helpers and integrated into pipeline
- `tests/test_summarize.py` — Added 15 tests

## must_haves
- [x] `summarize_chunks()` catches context-length errors and attempts decomposition
- [x] Class chunks with method children are decomposed via method summaries → class summary
- [x] Standalone oversized chunks are decomposed via map-reduce
- [x] Decomposition failures are logged and the chunk is skipped (no crash)
- [x] `max_chunk_chars` config field exists with default 3000
- [x] `--max-chunk-chars` CLI flag works
- [x] All 274 existing tests still pass
- [x] New tests cover decomposition paths
