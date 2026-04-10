---
created: 2026-04-10T00:00:00Z
title: Generate codebase architecture summary file
area: api
files:
  - 02-worktrees/glma/src/glma/export.py:309
  - 02-worktrees/glma/src/glma/export.py:377
  - 02-worktrees/glma/src/glma/index/writer.py:252
---

## Problem

The markdown export already generates three things:
1. **Per-file `.md`** — individual file summaries with chunks and code (from `_format_export_file()`)
2. **`INDEX.md`** — file listing table with summaries and stats (from `generate_index_md()`)
3. **`RELATIONSHIPS.md`** — cross-file dependency graph tables (from `generate_relationships_md()`)

But there's no **top-level synthesis** — a single file that explains the codebase as a coherent whole. The existing output is structured data (tables, listings, edges), not a narrative. An agent (or human) reading the export has to manually piece together:
- What the codebase *does*
- What the main modules are and their roles
- How data flows through the system
- Entry points vs internal modules
- Layered architecture / dependency layers

For the air-gapped export use case (agent needs full context without the actual code), a synthesized architecture overview is the highest-value artifact.

## Solution

### Generate an `ARCHITECTURE.md` as part of export

This is a new file generated alongside `INDEX.md` and `RELATIONSHIPS.md`. It synthesizes the per-file summaries and relationship data into a human-readable architecture narrative.

#### What it should contain

1. **Overview** — 2-3 sentence description of what the codebase does (could be AI-generated from file summaries, or a rule-based synthesis from module structure)
2. **Module Map** — group files by directory/package, describe each module's role
3. **Dependency Layers** — derive layers from the relationship graph (files that import nothing → core → utils → entry points)
4. **Entry Points** — files with main(), CLI commands, API endpoints, or nothing importing them
5. **Data Flow** — trace how data moves through the system using cross-file call/import edges
6. **Mermaid Diagram** (optional) — auto-generated dependency graph visualization

#### Rule-based approach (no LLM needed)

The relationship data already has enough structure to derive most of this:
- Group files by top-level directory → module map
- Files with no incoming imports → likely entry points
- Topological sort of import edges → dependency layers
- Cluster by import density → identify core vs peripheral modules

Example output:
```markdown
# Architecture: glma

## Overview
A code indexing tool that parses Python and C files, stores chunks in a Ladybug DB,
and exports static markdown for air-gapped agent consumption.

## Module Map
- `index/` — File parsing, chunk extraction, AST walking, relationship resolution
- `db/` — Ladybug DB storage layer (LadybugStore)
- `query/` — Query formatting, notebook compaction, variable tracking
- `export.py` — Markdown export pipeline (file, index, relationships)
- `watch.py` — File system watcher for incremental re-indexing
- `cli.py` — Typer CLI entry point

## Dependency Layers
1. **Core**: `db/ladybug_store.py`, `models.py` (imported by everything, import nothing external)
2. **Indexing**: `index/parser.py`, `index/writer.py`, `index/resolver.py` (depend on core)
3. **Query/Export**: `query/formatter.py`, `export.py` (depend on core + indexing)
4. **Entry Points**: `cli.py`, `watch.py` (depend on everything above)

## Entry Points
- `cli.py` — Typer CLI (`glma index`, `glma query`, `glma export`, `glma watch`)
- `__main__.py` — `python -m glma` entry
```

#### AI-enhanced approach (with pi or local LLM)

Same structure, but the overview section and module descriptions are AI-generated from the per-file summaries. Uses the same model ownership model as the summarization todo (pi extension or `--ai-summaries`).

### Implementation

1. Add `generate_architecture_md()` to `export.py` alongside `generate_index_md()` and `generate_relationships_md()`
2. Derive module map from directory grouping of indexed files
3. Derive dependency layers from topological sort of cross-file import edges
4. Derive entry points from files with no incoming cross-file imports
5. Add `ARCHITECTURE.md` to the export output (directory mode, tar mode, stdout)
6. Optionally AI-generate the overview narrative when `--ai-summaries` is enabled
