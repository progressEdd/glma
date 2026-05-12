---
status: resolved
trigger: "glma embed with mismatched embedding dimensions silently wiped all chunks; decomposition fallback returned None"
created: 2026-05-11T00:00:00.000Z
updated: 2026-05-11T00:00:00.000Z
---

## Current Focus

hypothesis: Two distinct bugs — (1) `_rebuild_chunk_table()` drops only CONTAINS but not RELATES_TO, causing silent data loss, and (2) `_decompose_class_chunk()` returns None when all method summaries fail
test: `glma embed` against DB indexed at 768 dims with 1024-dim provider
expecting: Chunks preserved through rebuild, all chunks get some summary
next_action: N/A — all fixed and verified

## Symptoms

expected: `glma embed` with mismatched dimensions rebuilds Chunk table preserving data, and large class chunks always get a summary (even if decomposed methods fail)
actual: All chunks silently deleted (Embedded: 0, Skipped: 0, Failed: 0); some chunks receive no summary at all
errors: No runtime errors — silent data loss
reproduction: Index at 768 dims, change config to 1024 dims, run `glma embed`
started: First discovered during v1.3 Phase 14 testing

## Eliminated

- hypothesis: LadybugDB doesn't support dropping referenced tables
  evidence: LadybugDB supports it — the fix is simply dropping both relationship tables (RELATES_TO and CONTAINS) before dropping Chunk. The original code only dropped CONTAINS.
  timestamp: 2026-05-11T00:00:00Z

## Evidence

- timestamp: 2026-05-11T00:00:00Z
  checked: `_rebuild_chunk_table()` drop sequence in `ladybug_store.py`
  found: Only drops CONTAINS before Chunk. RELATES_TO also references Chunk but isn't dropped first → DROP TABLE Chunk fails → fallback `DETACH DELETE` wipes data → re-insert fails silently
  implication: Must drop both RELATES_TO and CONTAINS before dropping Chunk

- timestamp: 2026-05-11T00:00:00Z
  checked: `_decompose_class_chunk()` in `summarize/pipeline.py` with large class chunk (GPTAssistantAgent, 24K chars)
  found: When all child method summaries fail (due to 4096-token context limit), `method_summaries` is empty → function returns None → chunk gets no summary
  implication: Must add fallback — summarize just the class header when all methods fail

## Resolution

root_cause: (1) `_rebuild_chunk_table()` didn't drop RELATES_TO before dropping Chunk, causing silent data loss via fallback delete. (2) `_decompose_class_chunk()` had no fallback when all method summaries fail.

fix: (1) Updated `_rebuild_chunk_table()` to drop both RELATES_TO and CONTAINS before Chunk, ensuring clean rebuild with data preservation. (2) Added class-header-only fallback in `_decompose_class_chunk()` — when all method summaries fail, extracts docstring/decorators/class vars and summarizes that instead.

verification: 14 chunks preserved through 768→1024 dimension rebuild. Decomposition fallback produces header-based summary when methods fail. All tests pass.

files_changed:
  - 02-worktrees/glma/src/glma/db/ladybug_store.py
  - 02-worktrees/glma/src/glma/summarize/pipeline.py
