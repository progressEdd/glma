# Phase 16: Pipeline Reliability - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-12
**Phase:** 16-pipeline-reliability
**Areas discussed:** Chunk ID format, Resume strategy, Signal handling, Summarization progress

---

## Chunk ID Format

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Force re-index | Change format, old DB incompatible, user re-runs `glma index` | ✓ |
| Migration script | `glma migrate` rehashes chunk IDs, updates foreign keys | |
| Auto-detect and rebuild | On startup, check format version, warn and rebuild automatically | |

**User's choice:** Force re-index
**Notes:** User confirmed that re-indexing is acceptable because the time-consuming part (LLM summaries) is preserved via existing `upsert_chunks` content_hash matching. User also confirmed chunk IDs are internal-only — users never see them in search/query/export output. Format drops `chunk_type` from the ID string, matching ROADMAP spec: `{file_path}::{name}::{line}::{hash8}`.

---

## Resume Strategy

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| 4 stages, summarization separate | `discovered → chunked → relationships_extracted → complete`. Summarization is post-index pass. | ✓ |
| 5 stages, summarization included | Add `summarized` as final stage. Couples indexing to summarization. | |
| Stage tracking per-pass only | Track which of 3 passes completed. Less granular. | |

**User's choice:** 4 stages, summarization separate
**Notes:** User specified summarization flow: check which files already have summaries, regenerate markdown for those first (so markdown is current), then continue summarizing remaining chunks. Content_hash matching used to skip re-summarizing unchanged chunks.

---

## Signal Handling

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Finish current file, then stop | Complete in-progress file, exit. Fast response to Ctrl+C. | ✓ |
| Finish current stage, then stop | Complete current pipeline stage for ALL files. Potentially long wait. | |
| Immediate stop with rollback | Abort immediately, rollback partial writes. Complex. | |

**User's choice:** Finish current file, then stop
**Notes:** User asked for clarification on current file vs current stage. After understanding that "finish current stage" means completing the stage for ALL remaining files (potentially minutes on large codebases), chose "finish current file" for fast Ctrl+C response. Per-file stage tracking makes resume precise enough that finishing the whole stage is unnecessary.

---

## Summarization Progress Display

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Per-chunk status with counts | Rich progress bar: file+chunk name, done/skipped/failed counts | ✓ |
| Per-file progress | Simpler: just file count, no chunk-level detail | |
| Dual progress | Outer bar files, inner bar chunks. Most info but busy. | |

**User's choice:** Per-chunk status with counts
**Notes:** User specified the description should show both file AND chunk name (e.g., `auth/login.py → verify_token`) to match the indexing progress pattern that shows the current file. Running counts of done/skipped/failed.

---

## Agent's Discretion

Areas where the agent has flexibility during planning/implementation:
- Exact Rich progress bar column layout for summarization
- Whether to extend `IndexProgress` or create separate `SummarizeProgress`
- Signal handler implementation details (signal.signal vs asyncio)
- Whether to add `--force-reindex` flag
- Whether `pipeline_stage` uses string enum or plain string
- Shutdown message on interrupt

## Deferred Ideas

None — discussion stayed within phase scope.
