# Phase 8: ARCHITECTURE.md & Export Polish - Research

**Researched:** 2026-04-10
**Status:** Complete

## Research Question

"What do I need to know to PLAN this phase well?"

## Summary

Phase 8 adds `generate_architecture_md()` to `export.py`, following the exact same pattern as `generate_index_md()` and `generate_relationships_md()`. The function receives the pre-assembled `file_data` dict and produces a markdown string. Integration requires updating 3 call sites: `export_index()`, `_write_files_to_dir()`, and `_write_tar_to_stream()`. The core algorithm has 4 sub-problems: module grouping, entry point detection, module dependency graph, and key interface identification.

## 1. Existing Export Pipeline Architecture

### Data Flow (confirmed from `export.py`)

```
export_index(repo_root, config, store, console)
  ├── store.get_indexed_files() → {path: content_hash}
  ├── For each file: store.get_file_record/get_chunks_for_file/get_file_relationships
  ├── file_data = {path: {record, chunks, relationships, summary}}  ← SHARED DATA STRUCTURE
  ├── Per-file: _format_export_file(path, record, chunks, rels, config) → markdown
  ├── generate_index_md(indexed_files, file_data) → INDEX.md string
  ├── generate_relationships_md(file_data) → RELATIONSHIPS.md string
  └── Route to output:
      ├── "-" → _write_tar_to_stream(stdout.buffer, file_exports, index_md, rels_md)
      ├── "*.tar.gz" → _write_tar_to_stream(file, file_exports, index_md, rels_md)
      └── dir → _write_files_to_dir(output_dir, file_exports, index_md, rels_md)
```

**Key insight:** `file_data` dict is fully assembled before any root file generation. `generate_architecture_md(file_data)` gets everything it needs — no new store queries required.

### Function Signatures (must match pattern)

```python
# Existing pattern:
def generate_index_md(indexed_files: dict, file_data: dict[str, dict]) -> str:
def generate_relationships_md(file_data: dict[str, dict]) -> str:

# New function follows same pattern:
def generate_architecture_md(file_data: dict[str, dict]) -> str:
```

### Writer Integration Points (3 call sites)

**`export_index()`** (line ~456):
```python
index_md = generate_index_md(indexed_files, file_data)
rels_md = generate_relationships_md(file_data)
# ADD: arch_md = generate_architecture_md(file_data)
```

**`_write_files_to_dir()`** (line ~484):
```python
def _write_files_to_dir(output_dir, file_exports, index_md, rels_md):  # ADD: arch_md
    ...
    (output_dir / "INDEX.md").write_text(index_md, ...)
    (output_dir / "RELATIONSHIPS.md").write_text(rels_md, ...)
    # ADD: (output_dir / "ARCHITECTURE.md").write_text(arch_md, ...)
```

**`_write_tar_to_stream()`** (line ~512):
```python
def _write_tar_to_stream(stream, file_exports, index_md, rels_md):  # ADD: arch_md
    ...
    # ADD tar entry for ARCHITECTURE.md
```

## 2. Module Grouping Algorithm

### Directory-Based Grouping

The glma codebase itself shows the expected grouping pattern:
```
src/glma/
  ├── cli.py              → module: cli (root)
  ├── config.py           → module: config (root)
  ├── export.py           → module: export (root)
  ├── models.py           → module: models (root)
  ├── summaries.py        → module: summaries (root)
  ├── watch.py            → module: watch (root)
  ├── db/
  │   └── ladybug_store.py → module: db
  ├── index/
  │   ├── chunks.py       → module: index
  │   ├── comments.py     → module: index
  │   ├── detector.py     → module: index
  │   ├── parser.py       → module: index
  │   ├── pipeline.py     → module: index
  │   ├── relationships.py → module: index
  │   ├── resolver.py     → module: index
  │   ├── walker.py       → module: index
  │   └── writer.py       → module: index
  ├── query/
  │   ├── formatter.py    → module: query
  │   ├── notebook.py     → module: query
  │   └── variables.py    → module: query
  └── summarize/
      ├── pipeline.py     → module: summarize
      └── providers.py    → module: summarize
```

**Algorithm:**
1. For each file path in `file_data`, extract the directory segment between source root and filename
2. Group by directory path (files in same directory = same module)
3. Root-level files (no subdirectory) form individual modules or a "root" module

**Edge case:** Files like `src/glma/__init__.py` — these should be grouped with the root module, not treated separately.

### Merge Strategy (D-06)

For tightly-coupled directories, compute cross-module relationship density:
```python
# Pseudocode
for each pair of modules (A, B):
    cross_rels = count relationships where source in A and target in B (or vice versa)
    if cross_rels > threshold:
        merge A and B into single module
```

**Recommendation:** Start simple — no merging. Only merge if a pair has > 50% of their relationships pointing to each other. This is unlikely for most codebases and adds complexity. The agent's discretion allows this.

## 3. Entry Point Detection

### Convention Checks (D-08)

From the `file_data` dict, check:

1. **`__main__.py` files:** Any file named `__main__.py` → detected entry point
2. **`if __name__ == "__main__"` blocks:** Need to check chunk content for this string → detected entry point
3. **`cli.py` / `main.py` filenames:** Files with these names → detected entry point

### Fan-In Analysis (D-09)

From `generate_relationships_md()`, we already extract per-file:
- `imports_from` — files this file imports
- `imported_by` — files that import this file

**Entry point = file with zero `imported_by` entries AND non-zero `imports_from` or `calls_to` entries.**

This is computable purely from the relationship data already in `file_data`.

```python
# Pseudocode
for each file:
    incoming = count relationships where direction == "incoming" and rel_type == "imports"
    outgoing = count relationships where direction != "incoming" and rel_type in ("imports", "calls")
    if incoming == 0 and outgoing > 0:
        → likely entry point
```

### Flagging (D-10)

Convention matches → "detected entry point"
Fan-in matches → "likely entry point"

## 4. Key Interface Identification

**Approach:** Chunks with many incoming relationships (imported/called by many other files) are key interfaces.

```python
# Count incoming edges per chunk across all files
interface_scores = {}
for path, data in file_data.items():
    for rel in data["relationships"]:
        if rel.get("direction") == "incoming" and rel.get("rel_type") in ("imports", "calls"):
            target_name = rel.get("target_name", "")
            interface_scores[target_name] = interface_scores.get(target_name, 0) + 1

# Top N by score = key interfaces
key_interfaces = sorted(interface_scores.items(), key=lambda x: -x[1])[:10]
```

## 5. Module Dependency Graph Computation

From the relationship data already extracted in `generate_relationships_md()`:

```python
# For each file, determine which module it belongs to
# Then aggregate: module A imports from module B → edge A→B in module graph
module_deps = defaultdict(set)
for path, data in file_data.items():
    my_module = get_module(path)
    for rel in data["relationships"]:
        if rel.get("rel_type") in ("imports", "calls"):
            target_file = rel.get("target_id", "").split("::")[0]
            target_module = get_module(target_file)
            if target_module and target_module != my_module:
                module_deps[my_module].add(target_module)
```

**Representation:** Adjacency table is simplest and matches the established markdown table pattern in RELATIONSHIPS.md. Mermaid would be nice but adds complexity — defer to agent's discretion.

## 6. Module Narrative Assembly

For each module, compose a description from chunk summaries:

```python
for module_name, files in module_groups.items():
    all_chunks = [c for f in files for c in file_data[f]["chunks"]]
    
    # Use AI summaries if available, otherwise rule-based
    summaries = []
    for chunk in all_chunks:
        if chunk.summary:
            summaries.append(f"{chunk.name}: {chunk.summary}")
        # else: generate_rule_summary provides fallback at file level
    
    module_description = "; ".join(summaries[:10])  # Truncate for readability
```

## 7. Test Patterns (from test_export.py)

Existing tests use:
- `_make_chunk()` helper for creating test chunks
- Direct function call testing (no store mocking needed for `generate_*_md()`)
- `tmp_path` fixture for directory output tests
- Typer `CliRunner` for integration tests

**New tests needed:**
- `TestGenerateArchitectureMd` class with tests for:
  - Basic generation with multiple modules
  - Entry point detection (convention + fan-in)
  - Module dependency graph
  - Key interfaces identification
  - Timestamp header present
  - Single-file codebase (edge case)
  - Chunks with/without AI summaries
- Update `TestDirectoryOutput` to verify ARCHITECTURE.md is written
- Update tar output test (if exists) to verify ARCHITECTURE.md in archive

## 8. Risk Assessment

| Risk | Likelihood | Mitigation |
| ---- | ---------- | ---------- |
| Module grouping too naive for complex codebases | Low | Directory-based grouping is standard; merge threshold is discretionary |
| Entry point detection false positives | Medium | Dual approach (convention + fan-in) with separate labels |
| ARCHITECTURE.md content overlaps with INDEX.md/RELATIONSHIPS.md | Medium | ARCHITECTURE.md focuses on module-level view, not file-level detail |
| Performance on large codebases | Low | All data pre-loaded in file_data dict; no new DB queries |

## RESEARCH COMPLETE

All technical questions resolved. Ready for planning.
