# Phase 11: Markdown Key-Value Export Format - Research

**Researched:** 2026-04-14
**Phase Goal:** `glma export` outputs a compact, LLM-friendly key-value markdown format by default, with option to select other formats

## RESEARCH COMPLETE

---

## 1. Current Export Architecture

### Entry Point
- **`cli.py` §`export()`** (line ~418): Typer command with `--output`/`-o`, `--ai-summaries`, `--include-code`, `--config` flags. No `--format` flag currently.
- Builds `export_overrides` dict → `load_export_config()` → `ExportConfig` → `export_index()`
- Uses `LadybugStore` for data access

### Orchestration
- **`export.py` §`export_index()`** (line ~816): Master orchestrator
  1. `store.get_indexed_files()` → dict of {path: content_hash}
  2. Loop: loads record, chunks, relationships, summary per file → `file_data` dict
  3. Loop: calls `_format_export_file()` per file → `file_exports` dict
  4. Generates root files: `generate_index_md()`, `generate_relationships_md()`, `generate_architecture_md()`
  5. Routes to output: `_write_files_to_dir()`, `_write_tar_to_stream()`, or stdout

### Per-File Formatting
- **`export.py` §`_format_export_file()`** (line ~21): Current markdown formatter
  - YAML frontmatter → `## Summary` → `## Key Exports` table → `## Chunks` (with `### chunk_name` sub-sections) → `## Relationships` (grouped tables: Outgoing Calls, Incoming Calls, Imports, Includes, Inherits)
  - Consumes: `file_path`, `file_record`, `chunks`, `relationships`, `config`
  - Returns complete markdown string

### Root File Generators
- **`generate_index_md()`**: File listing table + statistics
- **`generate_relationships_md()`**: Cross-file dependency graph + per-file dependency summary
- **`generate_architecture_md()`**: Module grouping + dependency table + entry points + key interfaces
  - Helper functions: `_get_module_name()`, `_group_by_module()`, `_detect_entry_points()`, `_compute_key_interfaces()`, `_module_from_import_name()`

### Writers
- **`_write_files_to_dir()`**: Writes per-file .md + INDEX.md + RELATIONSHIPS.md + ARCHITECTURE.md
- **`_write_tar_to_stream()`**: Same files into tar.gz
- Both take `file_exports`, `index_md`, `rels_md`, `arch_md` as separate parameters

### Data Models
- **`ExportConfig`**: `output_path`, `include_code`, `ai_summaries`, `ai_base_url`, `ai_model` — **no `format` field**
- **`QueryConfig`**: Has `output_format: str` (default `"markdown"`, values `"markdown"` or `"json"`)
- **No `ExportFormat` enum exists** yet

### Config Loading
- **`config.py` §`load_export_config()`**: Reads `[export]` from `.glma.toml`, merges CLI overrides, returns `ExportConfig`

## 2. Key Data Structures

### `file_data` dict (built in `export_index()`)
```python
{
    "src/cli.py": {
        "record": FileRecord,      # path, language, content_hash, last_indexed, chunk_count, file_summary
        "chunks": [Chunk, ...],    # id, file_path, chunk_type, name, content, summary, start_line, end_line, parent_id, attached_comments
        "relationships": [dict, ...],  # source_id, target_id, target_name, rel_type, confidence, source_line, direction, source_name, target_name_resolved
        "summary": str,            # Composed from AI summaries or rule-based
    }
}
```

### `indexed_files` dict
```python
{"src/cli.py": "hash123", "src/models.py": "hash456"}
```

### Chunk fields used by formatters
- `chunk.name`, `chunk.chunk_type.value`, `chunk.start_line`, `chunk.end_line`
- `chunk.content` (only when `config.include_code`)
- `chunk.summary` (AI-generated, may be None)
- `chunk.parent_id` (None = top-level)
- `chunk.attached_comments` (docstrings)
- `chunk.id` (format: `{file_path}::{chunk_type}::{name}::{start_line}`)

### Relationship dict fields
- `source_id`, `target_id`, `target_name`, `target_name_resolved`
- `rel_type` (calls, imports, inherits, includes)
- `confidence` (DIRECT, INFERRED)
- `source_line`, `source_name`
- `direction` (incoming vs outgoing)

## 3. Strategy Pattern Insertion Points

### Where to select renderer
In `export_index()`, after building `file_data`:
```python
# Current:
for file_path, data in file_data.items():
    export_md = _format_export_file(file_path, data["record"], data["chunks"], data["relationships"], config)

# After: dispatch by config.format
renderer = get_renderer(config.format)  # returns MarkdownKVRenderer, MarkdownRenderer, etc.
for file_path, data in file_data.items():
    export_md = renderer.format_file(file_path, data["record"], data["chunks"], data["relationships"], config)
```

### Where to generate root files
```python
# Current:
index_md = generate_index_md(indexed_files, file_data)
rels_md = generate_relationships_md(file_data)
arch_md = generate_architecture_md(file_data)

# After: delegate to renderer
root_files = renderer.generate_root_files(indexed_files, file_data)
# Returns dict like {"INDEX.md": "..."} or {"CODEBASE.md": "..."}
```

### Where to write output
Writers need to handle variable root file sets:
```python
# Current: hardcoded INDEX.md + RELATIONSHIPS.md + ARCHITECTURE.md
# After: dict of root files from renderer
_write_files_to_dir(output_dir, file_exports, root_files)
```

## 4. Format-Specific Implementation Notes

### markdown_kv (new default)
- **Per-file**: Heading = filename, key-value lines for metadata, `## chunk_name` sub-headings with type/lines/summary/calls as key-value
- **Root**: Consolidated `CODEBASE.md` (merges INDEX + RELATIONSHIPS + ARCHITECTURE data into one KV file)
- Relationships in per-file: flat comma-separated `calls: func1, func2` (no confidence/line numbers)
- Full relationship detail in CODEBASE.md only

### markdown (existing, backward compatible)
- Current `_format_export_file()` becomes the markdown renderer
- Current `generate_index_md()`, `generate_relationships_md()`, `generate_architecture_md()` become the markdown root generators
- Zero changes to output — existing tests pass unchanged

### json
- Per-file: serialize the data dict (record fields, chunks, relationships) as JSON
- Root: single JSON object with all file data
- File extension: `.json` instead of `.md`
- `json.dumps(data, indent=2)` — straightforward serialization

### yaml
- Same structure as JSON but YAML serialization
- Requires `pyyaml` dependency (need to check if already available)
- File extension: `.yaml` instead of `.md`

## 5. Dependency Check

### YAML support
```bash
# Check if pyyaml is already a dependency
grep -i yaml pyproject.toml requirements.txt
```
**Result:** Not currently a dependency. Need to add `pyyaml` to project dependencies if YAML format is supported.

### Typer/Click
- Already using Typer with `typer.Option()` — adding `--format`/`-f` follows the same pattern as `--output`/`-o`

## 6. Changes Required by File

### `models.py`
1. Add `ExportFormat` enum: `markdown_kv`, `markdown`, `json`, `yaml`
2. Add `format: ExportFormat = Field(default=ExportFormat.MARKDOWN_KV)` to `ExportConfig`
3. Optionally update `QueryConfig.output_format` to use `ExportFormat` enum (but keep default `"markdown"`)

### `cli.py`
1. Add `format: str = typer.Option("markdown-kv", "--format", "-f", help="Export format: markdown-kv, markdown, json, yaml")` to `export()` command
2. Add `format` to `export_overrides` dict
3. Update `query()` command: add `yaml` as valid format option alongside `markdown`/`json`
4. Validate format value against `ExportFormat` enum

### `config.py`
1. No changes needed — `load_export_config()` already handles arbitrary fields via `ExportConfig` pydantic model

### `export.py`
1. Create `FormatRenderer` protocol/ABC with methods:
   - `format_file(file_path, record, chunks, relationships, config) -> str`
   - `generate_root_files(indexed_files, file_data) -> dict[str, str]`
   - `file_extension() -> str` (`.md` for markdown/kv, `.json` for json, `.yaml` for yaml)
2. Create `MarkdownRenderer` — wraps existing `_format_export_file()` + existing root generators
3. Create `MarkdownKVRenderer` — new KV formatting logic
4. Create `JsonRenderer` — serialize data dict
5. Create `YamlRenderer` — serialize data dict as YAML
6. Add `get_renderer(format: ExportFormat) -> FormatRenderer` factory
7. Update `export_index()` to use renderer
8. Update `_write_files_to_dir()` and `_write_tar_to_stream()` to accept variable root files

### `query/formatter.py`
1. No direct changes — query already has `format_json_output()` and `format_compact_output()`
2. CLI `query` command needs `yaml` format option added (new `format_yaml_output()` function or extend existing)

## 7. Risk Areas

### Breaking existing tests
- 454 lines of export tests in `test_export.py` — all assume markdown output
- Current tests call `_format_export_file()` directly → must still work unchanged for markdown renderer
- `ExportConfig()` default changes from no format to `markdown_kv` — any test constructing `ExportConfig()` without format will now default to KV instead of markdown
- **Mitigation:** Tests that rely on markdown output should explicitly set `format=ExportFormat.MARKDOWN`

### Writer signature changes
- `_write_files_to_dir()` and `_write_tar_to_stream()` currently take `index_md`, `rels_md`, `arch_md` as separate params
- Need to change to accept a dict of root files (variable keys)
- Existing tests call `_write_files_to_dir(tmp_path, file_exports, "# Index", "# Rels", "# Arch")` — these need updating
- **Mitigation:** Keep backward-compatible signature or update tests alongside

### YAML dependency
- Adding `pyyaml` as a new runtime dependency
- Need to update `pyproject.toml` dependencies section
- **Mitigation:** Low risk — pyyaml is ubiquitous and stable

### CODEBASE.md naming
- New consolidated root file for KV format — name could conflict if a source file is literally named `codebase.py`
- **Mitigation:** Uppercase `CODEBASE.md` distinguishes from source file exports

## 8. Test Strategy

### New test categories needed
1. **KV format tests**: Per-file KV output matches expected structure (headings, key-value pairs)
2. **JSON format tests**: Valid JSON output, correct field structure
3. **YAML format tests**: Valid YAML output, correct structure
4. **Renderer factory tests**: `get_renderer()` returns correct type for each format
5. **CODEBASE.md tests**: Consolidated root file has expected content
6. **CLI format flag tests**: `--format markdown-kv`, `--format markdown`, `--format json`, `--format yaml`
7. **Default format test**: `glma export` without `--format` produces KV output
8. **Query yaml tests**: `glma query --format yaml` works

### Existing tests to preserve
- All 454 lines of `test_export.py` should continue passing (markdown renderer unchanged)
- `TestFormatExportFile`, `TestGenerateIndexMd`, `TestDirectoryOutput`, etc.

## 9. Implementation Order Recommendation

1. **Models first**: Add `ExportFormat` enum + `ExportConfig.format` field
2. **CLI second**: Add `--format`/`-f` to export command, validate against enum
3. **Renderer protocol**: Define `FormatRenderer` ABC
4. **Markdown renderer**: Wrap existing functions (refactor, not rewrite)
5. **KV renderer**: New implementation with CODEBASE.md
6. **JSON renderer**: Straightforward serialization
7. **YAML renderer**: Add pyyaml dependency, serialize
8. **Wire up**: Update `export_index()`, `_write_files_to_dir()`, `_write_tar_to_stream()`
9. **Query yaml**: Add yaml support to query command
10. **Tests**: New format tests, update existing tests for new defaults

---

*Phase: 11-markdown-keyvalue-export*
*Research completed: 2026-04-14*
