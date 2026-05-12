---
plan: 17-01
phase: 17
phase_name: Config Relocation
status: complete
started: "2026-05-12T18:15:00Z"
completed: "2026-05-12T18:25:00Z"
requirements:
  - CONF-01
key-files:
  modified:
    - src/glma/config.py
    - src/glma/cli.py
    - tests/test_config.py
  created: []
self-check: PASSED
---

# Plan 01: Config Path Relocation and Migration — Summary

## What was built

Moved `.glma.toml` config file from repo root to `.glma-index/` directory with automatic migration, backward-compatible detection, and functional `--config` flag wiring.

## Changes Made

### `src/glma/config.py`
- Added `_resolve_config_path()` helper that centralizes all config location logic
- Auto-migration: root `.glma.toml` → `.glma-index/.glma.toml` with Rich notice
- Priority: explicit config > new location > old location (auto-move) > default path
- All 5 loader functions (`load_config`, `load_watch_config`, `load_export_config`, `load_summarize_config`, `load_search_config`) now accept `config_file: Optional[Path] = None`
- Updated all docstrings to reference `.glma-index/.glma.toml`

### `src/glma/cli.py`
- Wired `--config` flag into all 6 loader calls across `index`, `watch`, and `export` commands
- Fixes pre-existing bug where `--config` was accepted but never used

### `tests/test_config.py`
- Updated all 14 test configs to use `tmp_path / ".glma-index" / ".glma.toml"`
- Added `config_dir` fixture
- Added `TestConfigMigration` class with 5 tests:
  - `test_auto_migrate_root_config` — root config auto-moves to new location
  - `test_new_location_takes_priority` — dual-location precedence
  - `test_no_config_no_error` — defaults without config
  - `test_explicit_config_skips_migration` — `--config` bypasses migration
  - `test_migration_creates_index_dir` — `.glma-index/` created during migration

## Verification

- 398 tests pass (38 config tests + 360 other tests)
- Zero old-location references remain in loaders (only in `_resolve_config_path` migration helper)
- All 5 loader functions have `config_file` parameter
- CLI `--config` flag functional on `index`, `watch`, `export` commands

## Issues Encountered

None. Implementation was straightforward — config.py and cli.py changes were already partially in place from prior work. Only test updates and migration tests needed to be added.
