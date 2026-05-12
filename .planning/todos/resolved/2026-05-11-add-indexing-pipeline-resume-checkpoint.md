---
created: 2026-05-11T00:00:00Z
title: Add resume/checkpoint support to indexing pipeline
area: core
status: resolved
files:
  - 02-worktrees/glma/src/glma/index/pipeline.py
  - 02-worktrees/glma/src/glma/db/ladybug_store.py
  - 02-worktrees/glma/src/glma/cli.py
---

## Problem

If `glma index` is interrupted (Ctrl+C, crash, OOM), re-running it may produce an incomplete index. The 3-pass pipeline (chunks → relationships → cross-file incoming) has no explicit tracking of which files have completed which passes. Specifically:

1. **No signal handling** — No SIGINT/SIGTERM handler in `run_index()` or the `index` CLI. Ctrl+C mid-file can leave partially-written data (chunks upserted but file content_hash not yet updated).

2. **Pass 2/3 relationship gap** — On re-run, files whose content hash matches are skipped in ALL passes, including Pass 2 (relationships) and Pass 3 (cross-file incoming). If the first run was interrupted during Pass 2, those files will have chunks but no relationships — permanently, until their source code changes.

3. **No progress persistence** — `IndexProgress` is in-memory only. On restart there's no way to know "we got through 500/1000 files" or "Pass 2 was never started."

4. **Embedding failures not retried** — Failed embedding batches are logged in `failed_chunk_ids` but there's no automatic retry on re-run.

### What already works

- Content hashing (BLAKE2b) correctly skips unchanged files in Pass 1
- Per-chunk summary persistence means summarization resumes naturally
- Embedding hash tracking means `glma embed` resumes naturally
- Watch mode is event-driven so doesn't need resume logic

## Solution

### Recommended: Pipeline stage tracking on File records

Add a `pipeline_stage` field to the `File` node in LadybugStore:

```
discovered → chunked → relationships_extracted → complete
```

**Changes:**

1. **Schema migration** — Add `pipeline_stage STRING` to File table, default `"discovered"`.

2. **Pass 1 (chunk extraction)** — After upserting chunks + file record, set `pipeline_stage = "chunked"`.

3. **Pass 2 (relationships)** — After extracting and storing relationships, set `pipeline_stage = "relationships_extracted"`.

4. **Pass 3 (cross-file incoming)** — After rewriting markdown with incoming rels, set `pipeline_stage = "complete"`.

5. **Re-run logic** — On `run_index()`:
   - Files at `"discovered"`: re-run Pass 1 (chunk extraction)
   - Files at `"chunked"`: skip to Pass 2 (relationships)
   - Files at `"relationships_extracted"`: skip to Pass 3 (cross-file)
   - Files at `"complete"` with matching hash: skip entirely

6. **Signal handling** — Register SIGINT/SIGTERM handler that sets a shutdown flag; check it between files for graceful exit. Don't interrupt mid-file writes.

### Alternative: Simpler hash-only approach

Just change Pass 2/3 to iterate ALL files (not just changed files), but skip relationship extraction for files that already have RELATES_TO edges. Less robust (doesn't handle partial relationship writes) but much simpler.

## Scope

- Files: `pipeline.py`, `ladybug_store.py`, `cli.py`
- Tests: `test_pipeline.py`, `test_incremental.py`, new `test_resume.py`
- Not in scope: embedding retry logic (separate concern)

## Priority

Medium — affects reliability on large codebases where indexing takes 10+ minutes and interruption is likely.
