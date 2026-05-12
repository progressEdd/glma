---
status: passed
phase: 17-config-relocation
verifier: inline
date: "2026-05-12"
---

# Phase 17: Config Relocation — Verification

## Phase Goal

Move `.glma.toml` config file from repo root into `.glma-index/` directory.

## Must-Haves

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Config found in new location | ✓ PASS | `load_config()` reads `.glma-index/.glma.toml` and applies settings |
| 2 | Backward compatibility with auto-migration | ✓ PASS | Root `.glma.toml` auto-moves to new location with Rich notice |
| 3 | Init/index creates config in correct location | ✓ PASS | No-config case returns defaults; path resolves to `.glma-index/.glma.toml` |
| 4 | `--config` flag functional | ✓ PASS | Explicit path bypasses migration logic, wired into 6 loader calls |
| 5 | All tests green | ✓ PASS | 398 tests pass (38 config + 360 other) |
| 6 | `_resolve_config_path` centralizes logic | ✓ PASS | 1 definition + 5 calls, zero direct `repo_root / ".glma.toml"` in loaders |
| 7 | Zero old-location references in loaders | ✓ PASS | Only in `_resolve_config_path` migration helper and CLI detection |

## Automated Tests

| Suite | Tests | Status |
|-------|-------|--------|
| test_config.py | 38 | ✓ All pass |
| Full suite | 398 | ✓ All pass |

## Manual Verification

| Test | Result |
|------|--------|
| Config reads from `.glma-index/.glma.toml` | ✓ Custom output_dir loaded correctly |
| Auto-migration moves root config to new location | ✓ File moved, old location empty |
| No-config case returns defaults | ✓ `output_dir == ".glma-index"` |
| Explicit `--config` path skips migration | ✓ Exact path returned |

## Requirements Coverage

| ID | Description | Status |
|----|-------------|--------|
| CONF-01 | `.glma.toml` config file lives in `.glma-index/` directory | ✓ Verified |

## Summary

- **Score:** 7/7 must-haves verified
- **Status:** passed
- **Gaps:** None
