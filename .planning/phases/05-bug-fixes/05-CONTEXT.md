# Phase 5: Bug Fixes - Context

**Gathered:** 2026-04-10
**Status:** Ready for planning

<domain>
## Phase Boundary

Fix three specific v1.0 bugs: (1) export defaults to summaries-only instead of including full code, (2) notebook cell source preserves comprehension expressions instead of truncating them, (3) writer output shows the actual rule-based summary instead of a stale Phase 3 placeholder. No new features — purely closing known gaps.

</domain>

<decisions>
## Implementation Decisions

### Export Default & CLI Flag
- **D-01:** `ExportConfig.include_code` defaults to `False` in `models.py` (was `True`)
- **D-02:** CLI flag changes from `--no-code` to `--include-code` — positive opt-in to include full source code. Old `--no-code` flag removed (no backward compat concern — v1.0 users are the developer only)

### Summary Function Location
- **D-03:** `generate_rule_summary()` moves from `export.py` to a new shared module (e.g., `glma/summaries.py`). Both `export.py` and `writer.py` import from there. Avoids coupling writer → export.

### Notebook Truncation (FIX-02)
- **D-04:** Root cause needs investigation during research/planning — the code path in `notebook.py` reads `cell.source` directly from nbformat, which looks correct. Truncation of list/dict/set comprehensions may be in the AST statement extraction in `variables.py` or in how nbformat handles multi-line expressions. Planner should add a test case with comprehensions first, then diagnose.

### Placeholder Replacement (FIX-03)
- **D-05:** `writer.py:274` replaces the hardcoded `"*(File summary not yet generated — available after Phase 3.)*"` with a call to `generate_rule_summary()` (now in the shared module). Writer output for `glma index` per-file markdown will show the same deterministic summary format as exports.

### the agent's Discretion
- Exact shared module name (`summaries.py` vs putting in an existing module)
- How to handle the comprehension truncation root cause once diagnosed
- Whether `--no-code` should remain as a hidden alias for backward compat or be fully removed
- Test case specifics for comprehension scenarios

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Bug locations (must-read)
- `02-worktrees/glma/src/glma/models.py` §L96-117 — `ExportConfig` class with `include_code` field (FIX-01 target)
- `02-worktrees/glma/src/glma/cli.py` §L265-326 — `export` command with `--no-code` flag (FIX-01 target)
- `02-worktrees/glma/src/glma/index/writer.py` §L273-274 — Placeholder string in `format_file_markdown()` (FIX-03 target)
- `02-worktrees/glma/src/glma/export.py` §L18-62 — `generate_rule_summary()` function to be moved to shared module
- `02-worktrees/glma/src/glma/query/notebook.py` — Notebook compaction, reads `cell.source` from nbformat (FIX-02 investigation)
- `02-worktrees/glma/src/glma/query/variables.py` — AST statement extraction for notebook cells (FIX-02 investigation)

### Test files to extend
- `02-worktrees/glma/tests/test_notebook.py` — Existing notebook tests, needs comprehension test case
- `02-worktrees/glma/tests/test_writer.py` — Writer tests, needs summary placeholder test
- `02-worktrees/glma/tests/test_cli.py` — CLI tests, export flag test

### Project context
- `.planning/codebase/CONVENTIONS.md` — Code style, naming patterns
- `.planning/codebase/STRUCTURE.md` — Source lives in `02-worktrees/glma/src/glma/`
- `.planning/codebase/STACK.md` — Technology stack (Python 3.13, Typer, Rich)

### Prior phase decisions
- `.planning/phases/04-file-watching-air-gapped-export/04-CONTEXT.md` — Phase 4 decisions: rule-based summaries by default, Typer CLI pattern, export modes

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`generate_rule_summary()`** (`export.py:18-62`): Deterministic file summary from chunks + relationships. Already works, just needs to move to shared location.
- **`load_export_config()`** (`config.py:67-85`): Merges `.glma.toml [export]` section with CLI overrides. Already handles the `include_code` field.
- **`format_file_markdown()`** (`writer.py`): Generates per-file markdown during indexing. Currently has the placeholder at line 274.
- **Existing test suite**: 211 tests, all passing. Tests for notebook, writer, and CLI already exist to extend.

### Established Patterns
- **Typer CLI with Rich**: `@app.command()`, `typer.Option()`, Rich console for output
- **Pydantic config models**: `ExportConfig(BaseModel)` with `Field(default=...)` pattern
- **uv for package management**: `uv run`, `uv add`, `uv sync`

### Integration Points
- **`export.py`** imports `generate_rule_summary` — will change to import from shared module
- **`writer.py`** will gain a new import from shared module (replacing hardcoded placeholder)
- **`cli.py`** export command flag changes from `--no-code` to `--include-code`

</code_context>

<specifics>
## Specific Ideas

- The `--include-code` flag is a simple positive opt-in: `glma export --include-code` gives you full source. Without it, you get signatures/summaries only. Matches user mental model.
- For FIX-02, the planner should start by creating a test notebook with list/dict/set comprehensions (e.g., `[x*2 for x in items]`, `{k: v for k, v in pairs}`, `{x for x in items}`), run it through `compact_notebook()`, and observe what gets truncated before fixing.
- The rule-based summary in writer output is the same function as exports — consistency across all output paths.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 05-bug-fixes*
*Context gathered: 2026-04-10*
