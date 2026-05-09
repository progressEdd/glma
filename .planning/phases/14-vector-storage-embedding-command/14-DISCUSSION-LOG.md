# Phase 14: Vector Storage & Embedding Command - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-09
**Phase:** 14-vector-storage-embedding-command
**Areas discussed:** Embedding Storage Model, CLI Design, Incremental Logic, Batching & Error Handling

---

## Embedding Storage Model

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Columns on Chunk table | Add `embedding FLOAT[N]`, `summary_hash STRING`, `vector_dimensions INT64` to existing Chunk node table. Simple queries, no JOINs. | ✓ |
| Separate ChunkEmbedding table | New node table with HAS_EMBEDDING relationship. Clean separation but extra JOINs. | |
| Embedding on relationship | Variant of separate table, less conventional. | |

**User's choice:** Columns on Chunk table (Option A)
**Notes:** User agreed with the recommendation — codebase scale doesn't justify a separate table, and simpler queries benefit Phase 15 hybrid search.

---

## `glma embed` CLI Design

### Config auto-detection

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Auto-detect from `[search]` config | Read `.glma.toml` `[search]` section, CLI flags override. Follows `load_search_config()` pattern. | ✓ |
| Always require explicit flags | Must pass provider/model every time. | |

**User's choice:** Auto-detect (Option A)
**Notes:** Follows established pattern. No disagreement.

### `--force` behavior

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Re-embed everything | Full rebuild, ignores all existing embeddings. | |
| Re-embed only where summary changed | Skip chunks with unchanged summaries, re-embed where summary hash differs. | ✓ |

**User's choice:** Re-embed only where summary changed (Option B)
**Notes:** User explicitly chose this over full rebuild. `--force` ignores the hash match check but still respects the "only if summary exists" rule.

### Progress display

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Rich progress bar (IndexProgress pattern) | Follow existing `glma index` progress UX. | ✓ |

**User's choice:** Rich progress bar, standard pattern
**Notes:** "yep follow the standard"

### Auto-embedding during indexing

**User raised:** "Is it possible to also do index creation as summaries are generated?"

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| `--embed` flag on `glma index` | Explicit opt-in alongside `--summarize`. | (deferred) |
| Auto when `[search] enabled` | Automatic if config has search enabled. | (deferred) |

**User's choice:** Deferred to future feature after discussion
**Notes:** User initially asked about auto-embedding during `glma index --summarize`. After discussing the two approaches, user decided to defer it: "actually let's not do that, make it a future feature."

---

## Incremental Embedding Logic

### Dimension/provider change detection

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Store dimensions in DB, detect mismatch | Add `vector_dimensions INT64` column, re-embed if stored dims ≠ config dims. | ✓ |
| Just use `--force` when changing models | User's responsibility to know they changed something. | |

**User's choice:** Store dimensions in DB (Option A)
**Notes:** Prevents subtle bugs with mismatched vector lengths at query time.

### Chunks without summaries

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Skip if no summary | Only embed chunks with non-empty summaries. | ✓ |

**User's choice:** Only embed if summary exists
**Notes:** Direct user confirmation.

---

## Batching & Error Handling

### Batch size strategy

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Fixed batch size (32 or 64) | Simple, predictable. | |
| Dynamic based on text length | Character budget per batch, shorter summaries → larger batches. | ✓ |
| One at a time | Simplest code but slowest. | |

**User's choice:** Dynamic based on text length (Option B)
**Notes:** User explicitly chose Option B over the recommended Option A.

### Failure mid-batch

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Skip failed batch, continue | Log warning, continue to next batch. | ✓ |
| Abort on first failure | Fail fast. | |
| Retry once, then skip | One retry per failed batch. | |

**User's choice:** Skip failed batch, continue (Option A)
**Notes:** User chose simpler skip-without-retry over the recommended retry-once approach.

### Exit code behavior

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Exit 0 only if all embedded successfully | Strict success criterion. | ✓ |
| Exit 0 if nothing to embed | Also success (no work needed). | ✓ (combined) |

**User's choice:** Exit 0 if all chunks embedded (or nothing to do), exit 1 if any failures
**Notes:** User specified "if all chunks embedded successfully" — combined with the nothing-to-do case as success.

---

## Agent's Discretion

- Dynamic batching formula/character budget threshold
- Summary hash algorithm (BLAKE2b to match content_hash, or simpler)
- Schema migration strategy for existing databases
- Error message wording
- Test structure and coverage specifics
- Whether to create `embedding/pipeline.py` or add to existing module

## Deferred Ideas

- **Auto-embedding during `glma index --summarize --embed`** — user requested future feature
- **Hugging Face embedding provider** — from Phase 13 context
- **LLM-based query rewriting** (SRCH-07) — from REQUIREMENTS.md
- **Graph relationship traversal + semantic search** (SRCH-08) — from REQUIREMENTS.md
