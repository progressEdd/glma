# Phase 17: Config Relocation - Context

**Gathered:** 2026-05-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Move `.glma.toml` config file from repo root into `.glma-index/` directory, reducing repo pollution and keeping all glma artifacts in one place.

Requirements: CONF-01 only.

No changes to indexing, search, export, embed, or watch behavior. No new CLI commands. Config format and sections remain unchanged — only the file location changes.

</domain>

<decisions>
## Implementation Decisions

### Migration behavior
- **D-01:** When `.glma.toml` exists in repo root but not in `.glma-index/`, auto-move the file and print a notice: `[moved] .glma.toml → .glma-index/.glma.toml`. User doesn't need to do anything manually.
- **D-02:** After auto-move, continue execution normally using the new location.
- **D-03:** If config exists in both locations, `.glma-index/.glma.toml` wins (new location takes priority). Root-level one is ignored (but not deleted — user may have it in git and want to keep it temporarily).

### `--config` flag interaction
- **D-04:** When `--config` is explicitly provided, skip the root-level deprecation check entirely. No warning, no migration attempt. The user is pointing at a specific file — that's the only config that matters.

### Agent's Discretion
- Exact warning message wording for the auto-move notice
- Whether to log the migration or just print to console
- How to handle edge cases (e.g., `.glma-index/` doesn't exist yet when root config found)
- Whether `glma init` (if it exists) should also create config in new location

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Config loading
- `02-worktrees/glma/src/glma/config.py` — All 5 `load_*_config()` functions hardcode `repo_root / ".glma.toml"`. This is the PRIMARY file — every function needs the path updated.
- `02-worktrees/glma/src/glma/models.py` — `IndexConfig` with `output_dir` default (`.glma-index`). Defines the relationship between config and index directory.

### CLI entry points
- `02-worktrees/glma/src/glma/cli.py` — Auto-detection logic at lines ~290 and ~712 checks for `.glma.toml` to find repo root. Also has `--config` flag at lines ~46, ~430, ~487.

### Requirements
- `.planning/REQUIREMENTS.md` — CONF-01
- `.planning/ROADMAP.md` — Phase 17 success criteria and key implementation notes

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **5 config loaders** (`config.py`): `load_config`, `load_watch_config`, `load_export_config`, `load_summarize_config`, `load_search_config` — all follow identical pattern: `repo_root / ".glma.toml"`. Easy to change in one pass.
- **`--config` flag**: Already exists on `index`, `watch`, and `export` commands. Provides explicit override path.

### Established Patterns
- **Config load pattern**: Each `load_*_config()` opens `config_path`, parses TOML, extracts section, merges CLI overrides. Only the `config_path` line needs changing.
- **Auto-detection**: CLI walks up from CWD looking for `.glma-index/` OR `.glma.toml` to find repo root. This check needs updating to only look for `.glma-index/` (or check new config location).

### Integration Points
- **`config.py` line 22** (and equivalents in each loader): `config_path = repo_root / ".glma.toml"` → change to `repo_root / config.output_dir / ".glma.toml"` or similar.
- **`cli.py` auto-detection** (~lines 290, 712): Remove `.glma.toml` from repo root detection, or keep as fallback for migration prompt.
- **`cli.py` `--config` handling**: When `config_file` is provided, use it directly (already works this way).

</code_context>

<specifics>
## Specific Ideas

- The auto-move notice should be a single Rich-styled line, not a multi-line warning — this is a helpful migration, not an error.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 17-config-relocation*
*Context gathered: 2026-05-12*
