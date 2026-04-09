# Phase 2: Relationship Extraction - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-08
**Phase:** 2-relationship-extraction
**Areas discussed:** Relationship data model, Cross-file resolution depth, Confidence boundary, Markdown output

---

## Relationship Data Model

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Typed edge tables (CALLS, IMPORTS, INHERITS) | Separate Ladybug rel tables per type. Consistent with existing CONTAINS pattern. Type-specific Cypher queries. | |
| Generic RELATES_TO table | One edge table with `rel_type` and `confidence` properties. Flexible — new types without schema changes. Single Cypher pattern with WHERE filter. | ✓ |

**User's choice:** Generic RELATES_TO — more flexible, easy to extend without schema migrations.
**Notes:** User preferred extensibility over the consistency with the existing CONTAINS pattern.

---

## Cross-File Resolution Depth

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Conservative | Same-file only, plus direct imports where target is already indexed. No multi-hop. | |
| Moderate | Resolve `from X import Y`, `import X; X.y()`, `self.method()`. Skip function pointers and dynamic dispatch. | |
| Aggressive + linter validation | Full multi-hop import chains, function pointers, dynamic dispatch via tree-sitter. Linter/type-checker as second pass to validate and upgrade INFERRED → DIRECT. | ✓ |

**User's choice:** Aggressive resolution with linter/type-checker validation pass.
**Notes:** User suggested leveraging linters (mypy, clang-tidy) to handle the hard cases (function pointers, dynamic dispatch) that tree-sitter alone can't resolve confidently. Linter is a validation layer, not the primary extraction mechanism. Pipeline: tree-sitter aggressive extraction → linter validation pass.

---

## Confidence Boundary

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Narrow DIRECT | Only same-file and fully resolved with indexed target. Everything else INFERRED. | |
| Table-based boundary | Explicit mapping of scenarios to DIRECT/INFERRED tags. Linter can upgrade but never downgrade. | ✓ |

**User's choice:** Approved the proposed confidence table mapping specific scenarios to DIRECT/INFERRED.
**Notes:** DIRECT = same-file, resolved imports, self.method(), linter-confirmed. INFERRED = unresolved targets, function pointers, dynamic dispatch, macros. Linter can upgrade INFERRED → DIRECT, never downgrades.

---

## Markdown Output

| Option | Description | Selected |
| ------ | ----------- | -------- |
| New `## Relationships` section only | Summary section at bottom with calls/called-by/imports/imports-by/inherits subsections. | |
| Per-chunk inline only | Relationship tables directly under each chunk heading. Context stays localized. | |
| Both (inline + summary) | Inline per-chunk for scanning a function, summary section for cross-file overview. More complete but more verbose. | ✓ |

**User's choice:** Both — inline per-chunk and summary section.
**Notes:** Dual format serves both scanning a specific function (inline) and understanding file-level dependencies (summary). Phase 3 query tool will slice from both formats.

---

## Agent's Discretion

- Which specific linter/type-checker to use (mypy vs pyright vs pyflakes for Python, clang-tidy vs libclang for C)
- How to invoke the linter (subprocess, internal API)
- Performance optimization — per-file vs batched linter runs
- Exact RELATES_TO edge schema properties beyond rel_type and confidence
- Error handling when linter is not installed
- How unresolved relationships appear in markdown

## Deferred Ideas

- Linter integration could be expanded to support more languages when new tree-sitter grammars are added
- Call graph visualization (v2 ADVN-01) will consume the relationship data model
