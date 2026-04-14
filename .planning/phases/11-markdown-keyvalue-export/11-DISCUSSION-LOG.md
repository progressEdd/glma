# Phase 11: Markdown Key-Value Export Format - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-14
**Phase:** 11-markdown-keyvalue-export
**Areas discussed:** KV Format Structure, Root File Rendering, Backward Compatibility, Format Routing Architecture

---

## KV Format Structure

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Flat inline | `calls: target1, target2` — all in one line, confidence/line as parentheticals | ✓ |
| Sub-heading per type | `#### calls` heading with individual `key: value` per target | |
| Skip relationships | Per-file KV only shows metadata + summary, no relationship data | |

**User's choice:** Flat inline — matching the todo reference example style. "Go with the one closer to the reference in the todo."
**Notes:** User wants maximum compactness. Full relationship detail lives in root file (CODEBASE.md or RELATIONSHIPS.md), not per-file.

---

## Root File Rendering

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Full KV conversion | All three root files become KV hierarchies | |
| Mixed format | Tables for tabular data, KV for detail sections | |
| Root files stay as-is | KV only applies to per-file exports | |
| Consolidate to one file | Merge INDEX + ARCHITECTURE + RELATIONSHIPS into single file | ✓ |

**User's choice:** Consolidate into one file. "Simplify it down to 1 file if they are already overlapping."

Follow-up on naming:

| Option | Description | Selected |
| ------ | ----------- | -------- |
| INDEX.md | Keep existing name | |
| CODEBASE.md | New name signaling "everything about this codebase" | ✓ |

**Notes:** User chose `CODEBASE.md` for the consolidated KV root file. Markdown format keeps the three separate files unchanged.

---

## Backward Compatibility

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Align both commands | Shared `--format` flag, same format names | |
| Export gets own flag | `--export-format` to avoid confusion with query | |
| Shared `--format` + shared enum | One `ExportFormat` enum used by both commands | ✓ |

**User's choice:** Shared `--format` + shared `ExportFormat` enum. Different defaults per command (`markdown-kv` for export, `markdown` for query).
**Notes:** User asked "what's the difference between 1/2" — options 1 and 3 were functionally identical (shared flag + shared enum). User confirmed the unified approach.

---

## Format Routing Architecture

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Strategy pattern | `FormatRenderer` protocol with per-format implementations | ✓ |
| Dispatch in existing functions | Branch inside `_format_export_file()` with format parameter | |
| Separate module per format | `export_kv.py`, `export_json.py`, `export_yaml.py` | |

**User's choice:** Strategy pattern — cleanest separation, renderer per format.

---

## Agent's Discretion

- Exact `FormatRenderer` method signatures and protocol shape
- JSON/YAML output structure and file extensions
- CODEBASE.md internal structure (module groupings, entry points in KV form)
- Whether CODEBASE.md includes per-chunk detail or file-level only
- Test organization for new format renderers

## Deferred Ideas

- Pi/agent integration for code summarization — Phase 12
- Chunk truncation — already completed in Phase 10
