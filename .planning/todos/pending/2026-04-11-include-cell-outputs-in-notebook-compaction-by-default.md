---
created: 2026-04-11T00:00:00Z
title: Include cell outputs in notebook compaction by default
area: api
status: open
files:
  - src/glma/query/notebook.py
  - src/glma/cli.py
---

## Problem

When running `glma query notebook.ipynb`, cell outputs (print statements, DataFrames, errors, display data) are excluded by default (`include_outputs=False`). Users must pass `--include-outputs` to see them. For a tool meant to give agents full context about a codebase, the outputs are often the most valuable part of a notebook — they show what the code actually produced, caught errors, and intermediate results.

The compacted markdown should include cell outputs by default, since the whole point is to give a reader (or agent) enough context to understand what the notebook does without running it.

## Current Behavior

```python
def compact_notebook(
    filepath: str | Path,
    include_outputs: bool = False,  # ← off by default
    include_code: bool = False,
) -> str:
```

CLI: `glma query notebook.ipynb` → no outputs shown.
Must run: `glma query notebook.ipynb --include-outputs`

## Proposed Change

1. **Flip the default**: `include_outputs=True` in `compact_notebook()`
2. **Flip the CLI default**: `--include-outputs` becomes `--no-outputs` (or just remove the flag and always include)
3. **Keep output rendering concise**: Truncate large outputs (e.g., DataFrame reprs > 50 lines) with a `... (N lines truncated)` marker
4. **Include output type labels**: Show `[stream]`, `[result]`, `[error]` tags so readers know what kind of output it is

### Considerations

- Some notebooks have very large outputs (HTML tables, images, huge DataFrames). Without truncation, the compacted markdown could blow up in size.
- Image outputs can't be rendered in markdown text — show `[Image: {dimensions}]` placeholder.
- Error outputs are especially valuable for understanding notebook state — always include these.
- The `--include-outputs` flag already exists and works. The change is just flipping the default + adding truncation.

## Acceptance Criteria

- `glma query notebook.ipynb` includes cell outputs by default
- Large outputs are truncated to a reasonable size (e.g., 50 lines)
- Errors are always included (never truncated)
- `--no-outputs` flag available to opt out
- Existing tests updated to match new default
- Test with develop.ipynb (88 cells, many with large DataFrame outputs)
