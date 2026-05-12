---
status: pending
priority: medium
created: "2026-05-12"
scope: index
---

# Add Progress Display for Relationship Extraction Pass

## Problem

When running `glma index` on large codebases (e.g., Linux kernel with 21,657 files), the relationship extraction pass (Pass 2) has no progress indicator. The user sees a blank cursor with no feedback, making it appear that the process has hung.

The indexing pass (Pass 1) shows a Rich progress bar with file count and ETA. The summarization pass shows per-file status with counts. But relationship extraction runs silently.

## Proposed Solution

Add a Rich progress bar to the relationship extraction pass in `pipeline.py`, similar to the existing `IndexProgress` pattern used for Pass 1. Show:
- File currently being processed
- Files completed / total
- Elapsed time / ETA

## Files to Modify

- `src/glma/index/pipeline.py` — relationship extraction loop
- `src/glma/index/progress.py` — possibly extend with a relationship progress tracker

## Context

Discovered during Linux kernel indexing (21,657 C files). Relationship extraction took over 20 minutes with no visual feedback.
