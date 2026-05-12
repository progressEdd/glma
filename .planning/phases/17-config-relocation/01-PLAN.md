---
wave: 1
depends_on: []
files_modified:
  - src/glma/config.py
  - src/glma/cli.py
  - tests/test_config.py
autonomous: true
requirements_addressed:
  - CONF-01
---

# Plan 01: Config Path Relocation and Migration

**Objective:** Move `.glma.toml` config location from repo root to `.glma-index/` directory with auto-migration, backward-compatible detection, and functional `--config` flag wiring.

## Context

- 5 config loaders in `config.py` all hardcode `repo_root / ".glma.toml"`
- 2 auto-detection sites in `cli.py` already check `.glma-index/` first
- `--config` CLI flag exists on 3 commands but is **never wired into loader calls** (pre-existing bug)
- 25+ tests in `test_config.py` place config at `tmp_path / ".glma.toml"` (root)

---

## Task 1: Add centralized config path resolver to `config.py`

<read_first>
- `src/glma/config.py` — All 5 loader functions and their current path resolution
- `src/glma/models.py` — `IndexConfig` with `output_dir` default (`.glma-index`)
</read_first>

<action>
1. Add `import shutil` to the top of `config.py` (needed for migration move).
2. Add a module-level Rich console import: `from rich.console import Console` and `_console = Console(stderr=True)` for migration notices.
3. Add a new helper function `_resolve_config_path`:

```python
def _resolve_config_path(repo_root: Path, explicit_config: Optional[Path] = None) -> Path:
    """Resolve config file path with auto-migration from legacy root location.

    Priority:
      1. explicit_config (from --config flag) — used as-is, no migration
      2. .glma-index/.glma.toml (new location) — used if exists
      3. .glma.toml (root, legacy) — auto-moved to new location with notice
      4. Neither — return new location path (used if config is later created)
    """
    if explicit_config:
        return explicit_config

    new_path = repo_root / ".glma-index" / ".glma.toml"
    if new_path.exists():
        return new_path

    old_path = repo_root / ".glma.toml"
    if old_path.exists():
        new_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_path), str(new_path))
        _console.print("[yellow][moved][/yellow] .glma.toml → .glma-index/.glma.toml")
        return new_path

    return new_path
```

4. Update all 5 loader functions to use `_resolve_config_path` instead of `repo_root / ".glma.toml"`:
   - `load_config(repo_root, cli_overrides=None)` → add parameter `config_file: Optional[Path] = None`, replace `config_path = repo_root / ".glma.toml"` with `config_path = _resolve_config_path(repo_root, config_file)`
   - `load_watch_config(repo_root, cli_overrides=None)` → add parameter `config_file: Optional[Path] = None`, replace line with `config_path = _resolve_config_path(repo_root, config_file)`
   - `load_export_config(repo_root, cli_overrides=None)` → add parameter `config_file: Optional[Path] = None`, replace line with `config_path = _resolve_config_path(repo_root, config_file)`
   - `load_summarize_config(repo_root, cli_overrides=None)` → add parameter `config_file: Optional[Path] = None`, replace line with `config_path = _resolve_config_path(repo_root, config_file)`
   - `load_search_config(repo_root, cli_overrides=None)` → add parameter `config_file: Optional[Path] = None`, replace line with `config_path = _resolve_config_path(repo_root, config_file)`

The function signatures gain an optional kwarg with default `None` — backward-compatible for all existing callers.
</action>

<acceptance_criteria>
- `config.py` contains `def _resolve_config_path` function
- `config.py` contains `import shutil`
- `grep -n "_resolve_config_path" src/glma/config.py` shows 6 lines (1 definition + 5 calls)
- `grep -n 'repo_root / ".glma.toml"' src/glma/config.py` returns 0 results
- All 5 loader functions have `config_file: Optional[Path] = None` parameter
</acceptance_criteria>

---

## Task 2: Wire `--config` flag into CLI loader calls

<read_first>
- `src/glma/cli.py` — The `index`, `watch`, and `export` command functions
- `src/glma/config.py` — Updated loader signatures with `config_file` parameter
</read_first>

<action>
1. In the `index` command function, pass `config_file` to `load_config`:
   Change: `cfg = load_config(repo_path, cli_overrides)`
   To: `cfg = load_config(repo_path, cli_overrides, config_file=config_file)`

2. In the `watch` command function, pass `config_file` to both loaders:
   Change: `index_config = load_config(repo_path)`
   To: `index_config = load_config(repo_path, config_file=config_file)`
   Change: `watch_config = load_watch_config(repo_path, watch_overrides)`
   To: `watch_config = load_watch_config(repo_path, watch_overrides, config_file=config_file)`

3. In the `export` command function, pass `config_file` to both loaders:
   Change: `index_config = load_config(repo_path)`
   To: `index_config = load_config(repo_path, config_file=config_file)`
   Change: `export_config = load_export_config(repo_path, export_overrides)`
   To: `export_config = load_export_config(repo_path, export_overrides, config_file=config_file)`

4. In the `index` command's summarization section, `load_summarize_config` is called. Pass `config_file`:
   Change: `summ_cfg = load_summarize_config(repo_path, summarize_overrides)`
   To: `summ_cfg = load_summarize_config(repo_path, summarize_overrides, config_file=config_file)`
</action>

<acceptance_criteria>
- `grep -n "config_file=config_file" src/glma/cli.py` shows 5 matches (index load_config, watch load_config, watch load_watch_config, export load_config, export load_export_config)
- `grep -n "config_file=config_file" src/glma/cli.py` includes a match for `load_summarize_config`
- `grep -A2 "config_file: Optional" src/glma/cli.py | grep "help=" | wc -l` returns 3 (three --config flags documented)
</acceptance_criteria>

---

## Task 3: Update config docstrings to reflect new location

<read_first>
- `src/glma/config.py` — All docstrings referencing config location
</read_first>

<action>
1. Update module docstring from `"""Configuration loading from .glma.toml and CLI flags."""` to `"""Configuration loading from .glma-index/.glma.toml and CLI flags."""`

2. Update `load_config` docstring: Change "Load configuration from .glma.toml in repo root" to "Load configuration from .glma-index/.glma.toml (with auto-migration from root .glma.toml)"

3. Update priority comment from "CLI flags > .glma.toml > defaults" to "CLI flags > .glma-index/.glma.toml > defaults"

4. Update `load_watch_config` docstring: Change "from .glma.toml [watch] section" to "from .glma-index/.glma.toml [watch] section"

5. Update `load_export_config` docstring: Change "from .glma.toml [export] section" to "from .glma-index/.glma.toml [export] section"

6. Update `load_summarize_config` docstring: Change "from .glma.toml [summarize] section" to "from .glma-index/.glma.toml [summarize] section"

7. Update `load_search_config` docstring: Change "from .glma.toml [search] section" to "from .glma-index/.glma.toml [search] section"
</action>

<acceptance_criteria>
- `grep -c "\.glma-index/\.glma\.toml" src/glma/config.py` returns at least 6 (module + 5 loaders)
- `grep "\.glma\.toml" src/glma/config.py | grep -v "glma-index"` returns only lines inside `_resolve_config_path` (the migration logic that still references the old location)
</acceptance_criteria>

---

## Task 4: Update tests for new config location and migration

<read_first>
- `tests/test_config.py` — All 25+ test functions
- `src/glma/config.py` — New `_resolve_config_path` and updated loader signatures
</read_first>

<action>
1. Add a pytest fixture at the top of `test_config.py` (after imports):

```python
@pytest.fixture
def config_dir(tmp_path):
    """Create .glma-index/ directory for config file placement."""
    config_path = tmp_path / ".glma-index"
    config_path.mkdir()
    return config_path
```

2. Update every test that creates `config_file = tmp_path / ".glma.toml"` to use the new location:
   Change: `config_file = tmp_path / ".glma.toml"`
   To: `config_file = tmp_path / ".glma-index" / ".glma.toml"`
   
   This applies to these test methods (from grep results):
   - `TestFileConfig::test_load_languages` (line 34)
   - `TestFileConfig::test_load_python_only` (line 43)
   - `TestCliOverrides::test_cli_overrides_file` (line 54)
   - `TestCliOverrides::test_none_override_ignored` (line 64)
   - `TestInvalidConfig::test_invalid_language` (line 74)
   - `TestSummarizeConfig::test_load_from_file` (line 93)
   - `TestSummarizeConfig::test_cli_overrides_file` (line 104)
   - `TestSummarizeConfig::test_none_override_ignored` (line 111)
   - `TestProviderPresets::test_custom_provider_from_toml` (line 169)
   - `TestProviderPresets::test_new_custom_provider` (line 180)
   - `TestSearchConfigFile::test_load_from_file` (line 239)
   - `TestSearchConfigFile::test_cli_overrides_file` (line 250)
   - `TestSearchConfigFile::test_none_override_ignored` (line 257)
   - `TestSearchProviderPresets::test_custom_provider_from_toml` (line 295)

   For each, also ensure `.glma-index/` directory is created before writing:
   ```python
   (tmp_path / ".glma-index").mkdir(exist_ok=True)
   config_file = tmp_path / ".glma-index" / ".glma.toml"
   ```

3. Add new test class `TestConfigMigration`:

```python
class TestConfigMigration:
    """Test auto-migration from root .glma.toml to .glma-index/.glma.toml."""

    def test_auto_migrate_root_config(self, tmp_path):
        """Root .glma.toml is auto-moved to .glma-index/.glma.toml."""
        (tmp_path / ".glma.toml").write_text('[index]\noutput_dir = "custom-out"\n')
        cfg = load_config(tmp_path)
        assert cfg.output_dir == "custom-out"
        # File should now be in new location
        assert (tmp_path / ".glma-index" / ".glma.toml").exists()
        # Old file should be gone
        assert not (tmp_path / ".glma.toml").exists()

    def test_new_location_takes_priority(self, tmp_path):
        """If both locations exist, new location wins."""
        (tmp_path / ".glma-index").mkdir()
        (tmp_path / ".glma.toml").write_text('[index]\noutput_dir = "old-location"\n')
        (tmp_path / ".glma-index" / ".glma.toml").write_text('[index]\noutput_dir = "new-location"\n')
        cfg = load_config(tmp_path)
        assert cfg.output_dir == "new-location"
        # Old file should still exist (not deleted in dual-location case)
        assert (tmp_path / ".glma.toml").exists()

    def test_no_config_no_error(self, tmp_path):
        """No config anywhere returns defaults without error."""
        cfg = load_config(tmp_path)
        assert cfg.output_dir == ".glma-index"

    def test_explicit_config_skips_migration(self, tmp_path):
        """--config flag uses exact path, no migration logic."""
        custom = tmp_path / "custom-config.toml"
        custom.write_text('[index]\noutput_dir = "explicit"\n')
        from glma.config import _resolve_config_path
        result = _resolve_config_path(tmp_path, explicit_config=custom)
        assert result == custom

    def test_migration_creates_index_dir(self, tmp_path):
        """Migration creates .glma-index/ if it doesn't exist."""
        assert not (tmp_path / ".glma-index").exists()
        (tmp_path / ".glma.toml").write_text('[index]\noutput_dir = "migrated"\n')
        cfg = load_config(tmp_path)
        assert cfg.output_dir == "migrated"
        assert (tmp_path / ".glma-index").is_dir()
```
</action>

<acceptance_criteria>
- `pytest tests/test_config.py -x -q` exits 0 with all tests passing
- `grep -c "tmp_path / \".glma-index\" / \".glma.toml\"" tests/test_config.py` returns at least 14
- `grep -c "class TestConfigMigration" tests/test_config.py` returns 1
- `grep -c "def test_auto_migrate\|def test_new_location\|def test_no_config\|def test_explicit_config\|def test_migration_creates" tests/test_config.py` returns 5
- `grep 'tmp_path / ".glma.toml"' tests/test_config.py | grep -v "glma-index" | grep -v "custom-config" | grep -v "TestConfigMigration" | wc -l` returns 0 (no old-location config in non-migration tests)
</acceptance_criteria>

---

## Task 5: Verify end-to-end behavior

<read_first>
- `tests/test_config.py` — All tests including new migration tests
- `src/glma/config.py` — Final state with `_resolve_config_path`
</read_first>

<action>
1. Run the full test suite to ensure no regressions:
   ```bash
   cd 02-worktrees/glma && python -m pytest tests/test_config.py -v
   ```

2. Run any CLI integration tests:
   ```bash
   cd 02-worktrees/glma && python -m pytest tests/test_cli.py -v
   ```

3. Run the full test suite:
   ```bash
   cd 02-worktrees/glma && python -m pytest tests/ -x -q
   ```

4. Verify no references to old config location remain in source (excluding migration logic and docstrings explaining the old location):
   ```bash
   grep -rn 'repo_root / ".glma.toml"' src/glma/ | grep -v _resolve_config_path
   ```
   This should return 0 results.

5. Verify all loader functions accept `config_file` parameter:
   ```bash
   grep -n "def load_.*config" src/glma/config.py
   ```
   All 5 functions should show `config_file: Optional[Path] = None` in their signature.
</action>

<acceptance_criteria>
- `pytest tests/test_config.py -v` exits 0 — all config tests pass
- `pytest tests/test_cli.py -v` exits 0 — CLI tests unaffected
- `pytest tests/ -x -q` exits 0 — full suite green
- `grep -rn 'repo_root / ".glma.toml"' src/glma/ | grep -v _resolve_config_path` returns 0 results
- `grep "def load_" src/glma/config.py | grep -c "config_file"` returns 5
</acceptance_criteria>

---

## Verification Criteria

1. **Config found in new location:** Running any glma command reads `.glma-index/.glma.toml` when present
2. **Backward compatibility:** Root `.glma.toml` auto-migrates to new location with Rich notice
3. **Dual-location precedence:** `.glma-index/.glma.toml` takes priority when both exist
4. **`--config` flag works:** Explicit path bypasses migration logic entirely
5. **All tests green:** Full test suite passes with updated fixtures

## must_haves

- `_resolve_config_path` centralizes all location logic
- Auto-migration prints a single Rich-styled notice line
- `--config` flag actually works (fixes pre-existing bug)
- Zero old-location references remain in loaders (only in migration helper)
- All existing tests updated + 5 new migration tests added
