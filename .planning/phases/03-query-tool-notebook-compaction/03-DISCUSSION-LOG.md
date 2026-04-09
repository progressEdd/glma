# Phase 3: Query Tool & Notebook Compaction - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-09
**Phase:** 3-query-tool-notebook-compaction
**Areas discussed:** Query output format, Notebook compaction strategy, Dependency depth, Query UX and flags

---

## Query Output Format

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Summary + signatures only | File summary, function/class signatures with docstrings, dependency list. No chunk code bodies. `--verbose` adds full code. | ✓ |
| Reformat existing markdown | Use current per-file markdown as base, slice it. Default = everything except code blocks. | |
| Fresh output from DB | Query DB directly and build output from scratch. More flexible but duplicates formatting logic. | |

**User's choice:** Summary + signatures only
**Notes:** Compact default, `--verbose` adds full code bodies.

**Follow-up: What counts as a "signature"?**

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| def line + docstring | Function signature line plus docstring. No body. | |
| def line + docstring + relationship hints | Same as above plus compact one-liner like `→ calls: authenticate(), create_session()`. | ✓ |

**User's choice:** def line + docstring + relationship hints
**Notes:** Gives dependency context at a glance without needing `--verbose`.

---

## Notebook Compaction Strategy

**Follow-up: How granular is variable tracking?**

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Per-cell | List variables defined/referenced per cell. Simple AST scan. | |
| Per-statement | Track each assignment individually within a cell. More precise but noisier. | ✓ |

**User's choice:** Per-statement
**Notes:** More precise, shows exactly where each variable originates.

**Follow-up: How to visualize cross-cell variable flow?**

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Inline per-cell | Under each cell: `defines: [vars]` and `references: [vars (defined cell N)]`. | |
| Inline + dependency summary | Same inline per-cell, plus `## Variable Flow` summary table at end. | ✓ |

**User's choice:** Inline + dependency summary
**Notes:** Inline tracking per cell plus overview table showing whole notebook data flow.

**Follow-up: How to handle markdown cells?**

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Include as-is | Render as blockquotes between code cells. | ✓ |
| Strip them | Only output code cells with variable metadata. | |
| Include as section headers | Use markdown content as organizational headings. | |

**User's choice:** Include as-is
**Notes:** Preserves narrative context (explanations, headings, observations).

---

## Dependency Depth

**Follow-up: How many hops of relationships?**

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Direct only (1-hop) | What file X directly calls/imports/inherits. | |
| Direct + expandable | Default 1-hop, `--depth N` flag for deeper traversal. | ✓ |
| Full transitive with cutoff | Follow graph until configurable limit (e.g., 3 hops). | |

**User's choice:** Direct + expandable
**Notes:** Clean default, flexible for power users via `--depth N`.

**Follow-up: What relationship types to show by default?**

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| All types | calls, imports, inherits, includes. | ✓ |
| Calls + imports only | Skip inherits and includes by default. | |

**User's choice:** All types
**Notes:** Simple and complete. No filtering by default.

---

## Query UX and Flags

**Follow-up: What flags beyond `--verbose` and `--depth N`?**

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Minimal | `--verbose`, `--depth N`, `--no-relationships`. 3 flags. | |
| Standard | All of minimal + `--format json` + `--output -`. 5 flags. | |
| Extended | All of standard + `--rel-types` + `--summary-only`. 7 flags. | ✓ |

**User's choice:** Extended
**Notes:** Full flag set: `--verbose`, `--depth N`, `--no-relationships`, `--format json`, `--output -`, `--rel-types`, `--summary-only`.

**Follow-up: How should errors surface?**

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Structured errors | Semantic exit codes (1=not found, 2=not indexed, 3=stale, 4=query error). Stderr for messages, stdout clean. | ✓ |
| Simple errors | Exit 0 with error in output markdown. Exit 1 only for CLI failures. | |

**User's choice:** Structured errors
**Notes:** Clean for piping, clear for programmatic agent use.

---

## Agent's Discretion

- Exact layout/spacing of compact query output
- Variable Flow table column order and sort order
- nbformat parsing and AST variable extraction implementation
- JSON output schema for `--format json`
- Whether `--depth N` has a hard cap
- Stale index detection approach
- Index metadata display format

## Deferred Ideas

None — discussion stayed within phase scope.
