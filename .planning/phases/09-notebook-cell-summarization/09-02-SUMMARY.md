---
plan: 09-02
phase: 09-notebook-cell-summarization
status: complete
tasks_total: 3
tasks_complete: 3
autonomous: true
---

# Summary: CLI --summarize Flags for Notebook Queries

## What was built

Wired `--summarize`, `--summarize-provider`, and `--summarize-model` flags into the `query` command for notebook paths. When a user runs `glma query notebook.ipynb --summarize`, the CLI loads the provider config, instantiates the appropriate provider, creates the cache directory, and passes both to `compact_notebook()`.

## Key changes

- **Query command flags**: Added `--summarize`, `--summarize-provider`, `--summarize-model` options mirroring the `index` command's flags
- **Notebook dispatch rewrite**: When `--summarize` is active, builds overrides dict → calls `load_summarize_config()` → instantiates provider (OpenAI-compatible or pi) → creates `.glma-index/notebook-cache/` directory → passes to `compact_notebook()`
- **Rich markup fix**: Added `markup=False` to `_write_output()` console.print call — Rich was interpreting `[code]` in cell headings as markup tags and stripping them
- **3 new CLI tests**: help flag presence, notebook without summarize unchanged, graceful failure with summarize but no provider

## Files modified

- `src/glma/cli.py` — query command flags + notebook dispatch block + Rich markup fix
- `tests/test_cli.py` — 3 new test functions in TestQuerySummarizeFlags class

## Self-Check: PASSED

- [x] All 3 tasks executed and committed
- [x] 8/8 CLI tests pass (5 existing + 3 new)
- [x] 270/270 total tests pass (no regressions)
- [x] `glma query --help` shows all 3 flags

## key-files.created

- `src/glma/cli.py` (modified — flags + dispatch + markup fix)
- `tests/test_cli.py` (modified — 3 new tests)
