---
created: 2026-04-11T00:00:00Z
title: Include cell outputs in LLM summarization context
area: api
status: resolved
files:
  - src/glma/query/notebook.py
  - tests/test_notebook.py
---

## Problem

When generating per-cell AI summaries, the LLM only saw the cell source code and metadata (notebook name, cell index, section name). It couldn't see what the cell actually produced — outputs, errors, display data. This led to summaries that described the code but missed the result, which is often the most informative part.

## Solution

### Changes made

1. **New `_cell_content_hash_with_outputs()`** — BLAKE2b hash that includes both source and output text. Used for cache invalidation so changing outputs (e.g., re-running a cell with different data) triggers re-summarization.

2. **New `_format_outputs_for_context()`** — Formats cell outputs as text for the LLM prompt, with configurable `max_chars` truncation (default 1500 chars). Handles stream, execute_result, error, and display_data output types. Truncation marker shows total char count.

3. **Updated summarization block** — When calling `provider.summarize()`, outputs are appended to the source code as:
   ```
   <cell source code>

   # Output:
   <formatted, truncated outputs>
   ```

4. **Cache uses output-aware hash** — Cache invalidates when outputs change, not just source.

### Context window protection

- Outputs truncated to 1500 chars per cell before sending to LLM
- Truncation marker: `... (truncated, N chars total)`
- Errors always included (never truncated, typically short)
- Display data shown as `[Display output]` placeholder

### Tests added (3 new)

- `test_hash_changes_when_outputs_change` — cache invalidation
- `test_format_outputs_truncation` — truncation logic
- `test_outputs_included_in_summarization_context` — spy provider verifies outputs reach LLM

## Resolved

2026-04-11 — Implemented in notebook.py, 273/273 tests passing.
