# Phase 1: Core Indexing Pipeline - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in 01-CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-08
**Phase:** 1-core-indexing-pipeline
**Areas discussed:** Project Scaffolding, Chunk Extraction Granularity, Markdown Output Format, CLI Behavior, Progress Display

---

## Project Scaffolding

| Option | Description | Selected |
|--------|-------------|----------|
| New top-level `src/glma/` | Clean break from exploratory stuff, standard Python layout | |
| Replace existing worktree | Convert linux_kernel worktree into real package | |
| New worktree `02-worktrees/glma/` | Follows existing experiment pattern, forking from 00-experiments | ✓ |

**User's choice:** Option 3 — new worktree at `02-worktrees/glma/`
**Notes:** Branch named `glma`, forked from `00-experiments` template branch. Keeps existing worktrees as reference material.

---

## Chunk Extraction Granularity

| Option | Description | Selected |
|--------|-------------|----------|
| Top-level only | Functions, classes, module-level code. Methods inside class chunks. | |
| Nested too | Functions, classes, AND methods as separate chunks (overlapping) | |
| Nested with parent reference | Methods get own chunks with parent_id linking to class | ✓ |
| Leaf-node only | Only finest-grained nodes, no class-level chunks | |

**User's choice:** Option 3 — nested with parent reference
**Notes:** User mentioned future semantic search design — LLM summarizes user intent, embeds the summary, hybrid (semantic + keyword) search against embedded chunk summaries. This means chunk schema needs a `summary` field for Phase 3.

---

## Markdown Output Format

| Option | Description | Selected |
|--------|-------------|----------|
| Reference-style | Auto-generated API docs style, hierarchical sections | |
| Flat catalog | Flat list of all chunks, sequential, easy to grep | |
| Layered summary | File summary → key exports table → full chunk details with markdown headings | ✓ |

**User's choice:** Option 3 — layered summary with markdown headings
**Notes:** Headings delimit and organize sections. Format designed to support Phase 3's layered query output (summary → signatures → details → full code).

---

## CLI Behavior

### Path argument

| Option | Description | Selected |
|--------|-------------|----------|
| Positional only | `glma index /path/to/repo` | |
| Named flag only | `glma index --path /path/to/repo` | |
| Either positional or default | `glma index /path` or `glma index` (cwd) | ✓ |

### Output verbosity

| Option | Description | Selected |
|--------|-------------|----------|
| Quiet by default | --verbose for progress | |
| Always shows progress | --quiet to silence | ✓ |
| Summary only | Stats at end | |

### Configuration

| Option | Description | Selected |
|--------|-------------|----------|
| Flags only | --include, --exclude, etc. | |
| Config file only | .glma.toml | |
| Both | Config file with flag overrides | ✓ |

**User's choice:** Either positional or default cwd; progress always shown with --quiet to silence; `.glma.toml` config with flag overrides

---

## Progress Display

| Option | Description | Selected |
|--------|-------------|----------|
| Rich progress bar | Full terminal UI with file count, elapsed, ETA | ✓ |
| Simple counter | In-place updating count, no external library | |
| Spinner + counter | Spinner animation plus file count | |

**User's choice:** Option 1 — Rich progress bar via `rich` or `tqdm`

---

## Agent's Discretion

- Exact `rich` vs `tqdm` choice
- `.glma.toml` config key names and structure
- LanceDB table schema details beyond required fields
- Error message wording and formatting
- Comment attachment heuristic details

## Deferred Ideas

- Semantic search with LLM-summarized intent + hybrid search — Phase 3
- Notebook (.ipynb) parsing behavior — Phase 3
- File watching / incremental updates — Phase 4
