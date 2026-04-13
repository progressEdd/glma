---
created: 2026-04-13T20:30:00Z
title: Add markdown key-value export format for structured data
area: api
files:
  - src/glma/export.py
  - src/glma/cli.py
---

## Problem

Currently `glma export` only outputs structured markdown with sections, tables, and relationship graphs. For some downstream consumers (Terraform-like configs, structured key-value data, LLM context windows), a flat markdown key-value format would be more useful and compact.

For example, given JSON like:
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

The desired markdown output would be:
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

## Solution

Add a new export format option (e.g., `--format kv` or `--format markdown-kv`) that converts the chunk/relationship data into a hierarchical markdown key-value representation:

- Each nesting level maps to a markdown heading (`#`, `##`, `###`, etc.)
- Leaf key-value pairs render as `key: value` lines
- Supports arbitrary nesting depth (up to heading level 6, then fallback to bold/indent)

Could be exposed via:
- `glma export --format kv` for the key-value markdown format
- Or as a separate output option on `glma query` for single files

This would be useful for exporting indexed data in a format that's easy for LLMs to parse and humans to scan quickly.
