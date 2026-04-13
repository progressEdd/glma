---
created: 2026-04-13T20:30:00Z
title: Add markdown key-value export format as default with multi-format support
area: api
files:
  - src/glma/export.py
  - src/glma/cli.py
  - src/glma/models.py
---

## Problem

Currently `glma export` only outputs structured markdown with sections, tables, and relationship graphs. The default export format should be a compact markdown key-value representation that's easy for LLMs to parse and humans to scan. Users should also be able to select other formats.

## Solution

### New default: `markdown-kv`

Make `markdown-kv` the default export format. Each nesting level maps to a markdown heading, leaf key-value pairs render as `key: value` lines.

Given structured data like:
```json
{
  "resource": {
    "aws_subnet": {
      "api-12": {
        "vpc_id": "${aws_instance.main-12.id}",
        "availability_zone": "us-east-1c",
        "tags": {
          "Environment": "development",
          "Project": "api-service",
          "CostCenter": "CC-1106"
        }
      }
    }
  }
}
```

The markdown-kv output would be:
```markdown
# resource

## aws_subnet

### api-12

vpc_id: ${aws_instance.main-12.id}
availability_zone: us-east-1c

#### tags

Environment: development
Project: api-service
CostCenter: CC-1106
```

For glma's indexed data, this means each file's chunks become a key-value hierarchy:
```markdown
# cli.py

language: python
last_indexed: 2026-04-13T20:15:23
chunk_count: 8

## version_callback

type: function
lines: L21-L24
summary: Prints the current application version to the console...
calls: []

## index

type: function
lines: L38-L140
summary: Indexes a repository's source files into a database...
calls: load_config, run_index, summarize_chunks
```

### Multi-format support

Add `--format` / `-f` flag to `glma export`:

| Format | Description |
| ------ | ----------- |
| `markdown-kv` | **Default**. Hierarchical key-value headings (compact, LLM-friendly) |
| `markdown` | Current table-based format (sections, tables, relationship graphs) |
| `json` | Raw JSON export |
| `yaml` | YAML export |

### Implementation steps

1. Add `ExportFormat` enum to `models.py` with values: `markdown_kv`, `markdown`, `json`, `yaml`
2. Add `format` field to `ExportConfig` with default `markdown_kv`
3. Add `--format` / `-f` CLI option to `glma export` command
4. Implement `_format_export_file_kv()` in `export.py` — converts file data to markdown-kv
5. Implement `_format_export_file_json()` / `_format_export_file_yaml()` for other formats
6. Route `export_index()` through format-specific formatters based on config
7. Format applies to **all** output files, not just per-file exports:
   - `INDEX.md`: files table becomes `markdown-kv` headings by default, or stays as table when `--format markdown`
   - `ARCHITECTURE.md`: module tables become kv headings by default
   - `RELATIONSHIPS.md`: dependency tables become kv headings by default
   - Per-file exports: chunk data as kv headings by default
8. Update tests

### Concrete example — config.py.md relationships section

**markdown-kv (default):**
```markdown
### load_config

type: function
lines: L24-L43
summary: Initializes an `IndexConfig` object...
calls: IndexConfig (INFERRED, L43), cli_overrides.items (INFERRED, L39), merged.update (INFERRED, L37)...
```

**markdown (current table format):**
```markdown
### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| load_config | ? (IndexConfig) | INFERRED | L43 |
| load_config | ? (cli_overrides.items) | INFERRED | L39 |
...
```

**json:**
```json
{"calls": [{"from": "load_config", "to": "IndexConfig", "confidence": "INFERRED", "line": 43}]}
```

**yaml:**
```yaml
calls:
  - from: load_config
    to: IndexConfig
    confidence: INFERRED
    line: 43
```

This applies to ALL tabular output: relationships, key exports, module tables in ARCHITECTURE.md, file listing in INDEX.md, etc.
