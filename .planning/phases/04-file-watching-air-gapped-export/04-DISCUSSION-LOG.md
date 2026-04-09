# Phase 4: File Watching & Air-Gapped Export - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-09
**Phase:** 04-file-watching-air-gapped-export
**Areas discussed:** Watch Behavior, Dual Output Sync, Export Format & Structure, Export Completeness

---

## Watch Behavior

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Foreground process | Ctrl+C to stop, user sees output | ✓ |
| Background daemon | PID file, `glma watch --stop` to halt | |
| Foreground + `--daemon` flag | Both modes available | |

**User's choice:** Foreground process with Ctrl+C
**Notes:** Simple and predictable. No daemon complexity needed.

### Debounce / Batch Strategy

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Debounce 1 second | Wait 1s after last change | |
| Debounce 500ms | More responsive, may double-fire on atomic saves | |
| Batch window | Collect all changes over fixed window, process together | ✓ |

**User's choice:** Batch window
**Notes:** Handles bulk operations like `git checkout` or `git pull` cleanly. Exact duration is agent's discretion.

### File Events

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Create + modify + delete | Renames caught as delete+create pair | |
| Create + modify + delete + rename | Explicit rename tracking | ✓ |
| Modify only | Simplest, misses new/deleted files | |

**User's choice:** All events including rename
**Notes:** Explicit rename allows single-operation path updates instead of delete+re-parse.

### Watch Output

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Minimal | Only show when re-indexing fires | ✓ (default) |
| Live dashboard | Rich live display with stats | |
| Verbose | Every file event logged | ✓ (with `--verbose`) |

**User's choice:** Minimal by default, verbose with `--verbose` flag
**Notes:** `[12:34:56] Re-indexing 3 files... Done.` normally. Full event log with flag.

---

## Dual Output Sync

### Incremental Update Strategy

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Reuse `run_index` with file filter | Pass changed files to existing pipeline | ✓ |
| Targeted update per file | New `run_incremental()` for single files | |
| Full `run_index` on every batch | Re-run entire pipeline each time | |

**User's choice:** Reuse `run_index` with a file filter
**Notes:** Leverages existing pipeline that already handles upserts, relationship extraction, cross-file rewrites.

### Write Atomicity

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| DB-first, best-effort markdown | Log warning on markdown failure | |
| Atomic-ish: buffer, write, verify, commit | Roll back DB if markdown fails | ✓ |
| Don't worry about it | Re-run `glma index` to fix inconsistencies | |

**User's choice:** Atomic-ish with rollback
**Notes:** Buffer all changes, write DB + markdown, verify both, roll back on failure.

---

## Export Format & Structure

### Directory Structure

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Nested mirror | Exact source directory structure | |
| Flat with index | All files flat, master INDEX.md | |
| Nested mirror + master index | Both structures | ✓ |

**User's choice:** Nested mirror + INDEX.md + RELATIONSHIPS.md
**Notes:** Nested for browsing, index for quick overview.

### Cross-File References

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Inline relationship sections | Per-file relationships only | |
| Inline + cross-reference links | Add relative path links in tables | |
| Inline + dedicated RELATIONSHIPS.md | Per-file + root-level full graph | ✓ |

**User's choice:** Inline + dedicated RELATIONSHIPS.md
**Notes:** Per-file for local context, one root file for the full dependency picture.

---

## Export Completeness

### Additional Content

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Same as current markdown | Copy of .glma-index/markdown/ | |
| Enriched with file summaries | Add LLM/rule-based summaries | |
| Enriched with summaries + metadata headers | Metadata block + summary + existing content | ✓ |

**User's choice:** Metadata headers + file summaries + existing content
**Notes:** Headers (path, language, timestamp, chunk count, hash) + summary + chunks + relationships.

### Summary Generation

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Rule-based extraction | Deterministic, no LLM, fast | |
| LLM-generated | Natural language, needs API | |
| Rule-based default, `--ai-summaries` optional | Both, local models supported | ✓ |

**User's choice:** Rule-based default, optional AI summaries with local model support
**Notes:** Must support LM Studio, llama.cpp, Ollama — local models via OpenAI-compatible API. No cloud dependency.

### Output Format

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Directory path only | `--output ./dir` | |
| Directory or archive | `--output ./dir` or `--output export.tar.gz` | |
| Directory, archive, or stdout | Add `--output -` for streaming tar pipe | ✓ |

**User's choice:** All three modes
**Notes:** Enables `glma export . | ssh remote 'tar -x'` workflow for air-gapped machines.

---

## the agent's Discretion

- Exact batch window duration
- File watching library choice
- Rule-based summary format and detail level
- Local model API integration details (OpenAI-compatible endpoint)
- Atomic rollback implementation details
- Archive format (tar.gz vs zip)
- INDEX.md and RELATIONSHIPS.md exact schema

## Deferred Ideas

None — discussion stayed within phase scope.
