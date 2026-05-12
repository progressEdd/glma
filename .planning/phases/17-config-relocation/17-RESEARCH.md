# Phase 17: Config Relocation — Research

**Researched:** 2026-05-12
**Phase Goal:** Move `.glma.toml` from repo root to `.glma-index/` directory

## Research Question

*"What do I need to know to PLAN this phase well?"*

---

## 1. Current Config Loading Architecture

### Config Loader (`config.py`)

All 5 config loader functions follow the identical pattern:

```python
config_path = repo_root / ".glma.toml"
```

Each function:
1. Constructs `config_path = repo_root / ".glma.toml"`
2. Checks `config_path.exists()`
3. Opens and parses TOML
4. Extracts relevant section (`index`, `watch`, `export`, `summarize`, `search`)
5. Merges with CLI overrides

**Functions to modify:**
| Function | Line | Section |
|----------|------|---------|
| `load_config()` | 22 | `[index]` |
| `load_watch_config()` | 48 | `[watch]` |
| `load_export_config()` | 69 | `[export]` |
| `load_summarize_config()` | 90 | `[summarize]` |
| `load_search_config()` | 136 | `[search]` |

**Key observation:** The `load_summarize_config()` and `load_search_config()` functions also read the raw TOML dict for custom provider resolution — they need the same path change plus access to the raw dict for provider preset merging.

### IndexConfig Default (`models.py`)

`IndexConfig.output_dir` defaults to `".glma-index"`. This is the directory where the config should now live. The new config path would be:

```python
config_path = repo_root / ".glma-index" / ".glma.toml"
```

**Circular dependency risk:** To know the output_dir, we need to load config. To load config, we need to know output_dir. Resolution:
- Use the **default** `output_dir` (`.glma-index`) for the config lookup path
- Only apply a custom `output_dir` from CLI overrides or from the config file itself (after loading)
- This means config file location is always `<repo_root>/.glma-index/.glma.toml` — it's fixed, not configurable relative to output_dir

---

## 2. CLI Auto-Detection Logic (`cli.py`)

### Two repo-root detection sites

**`query` command (line ~290):**
```python
for parent in [repo_root_path] + list(repo_root_path.parents):
    if (parent / ".glma-index").is_dir() or (parent / ".glma.toml").is_file():
        repo_root_path = parent
        found = True
        break
```

**`search` command (line ~712):**
```python
for parent in [repo_root_path] + list(repo_root_path.parents):
    if (parent / ".glma-index").is_dir() or (parent / ".glma.toml").is_file():
        repo_root_path = parent
        found = True
        break
```

**Migration consideration:** After this change, root-level `.glma.toml` should still trigger detection (for backward compatibility) but with a deprecation path. The new config is inside `.glma-index/`, so `.glma-index/.glma.toml` would also trigger detection via the `.glma-index` directory check.

**Recommended approach:**
- Keep `.glma.toml` as a detection trigger (backward compat)
- In config loading, check new location first, fall back to root with migration prompt
- Auto-detection in CLI doesn't need to change at all (`.glma-index/` dir is already the primary detection mechanism)

---

## 3. `--config` Flag Handling

Three commands accept `--config`:
- `index` (line 46): `config_file: Optional[Path]`
- `watch` (line 430): `config_file: Optional[Path]`
- `export` (line 490): `config_file: Optional[Path]`

**Current behavior:** The `--config` flag exists as a parameter but is **never wired into the loader calls**. Looking at the code:

- `index` command: calls `load_config(repo_path, cli_overrides)` — `config_file` is accepted but never passed
- `watch` command: calls `load_config(repo_path)` and `load_watch_config(repo_path, watch_overrides)` — same issue
- `export` command: calls `load_config(repo_path)` and `load_export_config(repo_path, export_overrides)` — same issue

**This is a pre-existing bug** — `--config` is documented but non-functional. CONTEXT.md decision D-04 says when `--config` is provided, skip the root-level deprecation check. We should actually wire this flag up during this phase since we're touching config loading anyway.

---

## 4. Test Coverage

### `test_config.py` — 25+ tests

All tests place `.glma.toml` at `tmp_path / ".glma.toml"` (repo root). Key test classes:
- `TestDefaultConfig` (2 tests) — no config file exists
- `TestFileConfig` (2 tests) — config at root
- `TestCliOverrides` (3 tests) — override precedence
- `TestInvalidConfig` (1 test)
- `TestSummarizeConfig` (6 tests)
- `TestProviderPresets` (7 tests)
- `TestSearchConfigDefaults` (1 test)
- `TestSearchConfigValidation` (4 tests)
- `TestSearchConfigFile` (3 tests)
- `TestSearchProviderPresets` (5 tests)

**Migration approach for tests:**
- All tests should place config at `tmp_path / ".glma-index" / ".glma.toml"`
- Need to create `.glma-index/` directory in test setup
- Need new tests for: migration path (root → new), dual-location precedence, `--config` flag

### Other test files referencing config:
- `test_cli.py` — may have integration tests
- `test_watch.py` — uses `load_watch_config`
- `test_export.py` — uses `load_export_config`

---

## 5. Migration Path Design

### Scenarios

| Scenario | Current State | Expected Behavior |
|----------|---------------|-------------------|
| Fresh install | No config anywhere | Create `.glma-index/.glma.toml` on first index |
| Existing user (root config) | `.glma.toml` in root | Auto-move to `.glma-index/.glma.toml`, print notice |
| Already migrated | `.glma-index/.glma.toml` | Normal loading |
| Both locations | Root + `.glma-index/` | New location wins, root ignored |
| `--config` specified | Explicit path | Use that path, no migration logic |

### Auto-move flow (from CONTEXT.md D-01/D-02):

```
1. Check .glma-index/.glma.toml → exists? → use it
2. Check .glma.toml → exists? → 
   a. Move to .glma-index/.glma.toml
   b. Print "[moved] .glma.toml → .glma-index/.glma.toml"
   c. Use moved file
3. Neither exists → proceed with defaults (no config file created until write)
```

### Edge case: `.glma-index/` doesn't exist yet

If root `.glma.toml` exists but `.glma-index/` directory doesn't (user hasn't indexed yet), we need to create the directory before moving. This is safe — `.glma-index/` is just a data directory.

---

## 6. Implementation Approach

### Centralized config path resolution

Rather than updating 5 functions individually, extract a helper:

```python
def _resolve_config_path(repo_root: Path, explicit_config: Optional[Path] = None) -> Path:
    """Resolve config file path with migration support."""
    if explicit_config:
        return explicit_config
    
    new_path = repo_root / ".glma-index" / ".glma.toml"
    if new_path.exists():
        return new_path
    
    old_path = repo_root / ".glma.toml"
    if old_path.exists():
        # Auto-migrate
        new_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_path), str(new_path))
        console.print(f"[moved] .glma.toml → .glma-index/.glma.toml")
        return new_path
    
    # No config found — return new location (will be used if created)
    return new_path
```

This centralizes migration logic in one place. All 5 loaders call this instead of `repo_root / ".glma.toml"`.

### Files to modify

| File | Change |
|------|--------|
| `config.py` | Add `_resolve_config_path()`, update all 5 loaders |
| `cli.py` | Wire `--config` flag into loader calls (bug fix) |
| `cli.py` | Optionally update auto-detection comments/docs |
| `test_config.py` | Move all config file fixtures to new location, add migration tests |
| `test_cli.py` | Update any CLI tests that reference config location |

### Files NOT to modify

- `models.py` — no changes needed (IndexConfig.output_dir default stays `.glma-index`)
- `db/` — no database changes
- `index/`, `query/`, `export/`, `watch/` — no changes (they receive config objects, not paths)

---

## 7. Risk Assessment

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Circular dependency (output_dir → config path) | Low | Config location is hardcoded to `.glma-index/`, not derived from config |
| Breaking existing user workflows | Medium | Auto-migration with notice, backward-compatible detection |
| `--config` flag was never wired | High (already broken) | Fix during this phase — orthogonal to relocation |
| Test suite breaks | Low | Systematic update of test fixtures |
| `.glma-index/` doesn't exist during migration | Low | `mkdir -p` before move |

---

## RESEARCH COMPLETE

Key findings:
1. **5 config loaders** all hardcode `repo_root / ".glma.toml"` — need centralized path resolution
2. **2 auto-detection sites** in `cli.py` — already check `.glma-index/` dir first, minimal change needed
3. **`--config` flag is documented but non-functional** — should be wired up during this phase
4. **25+ config tests** all place config at root — need systematic fixture migration
5. **Auto-move migration** is safe and straightforward — create `.glma-index/` if needed, move file, print notice
