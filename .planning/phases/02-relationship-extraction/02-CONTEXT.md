# Phase 2: Relationship Extraction - Context

**Gathered:** 2026-04-08
**Status:** Ready for planning

<domain>
## Phase Boundary

The index contains structural relationships (function calls, imports, inheritance) that agents can follow to understand how code connects across files. After indexing, querying a function shows what it calls and what calls it. Import aliases are resolved, `self.method()` calls resolve to the correct class method, and each relationship is tagged DIRECT or INFERRED based on analysis confidence.

This phase delivers: relationship data model in Ladybug, C relationship extraction, Python relationship extraction, import alias resolution, self.method() resolution, aggressive cross-file resolution with linter validation, confidence tagging, and relationship markdown output (both inline per-chunk and summary section).

</domain>

<decisions>
## Implementation Decisions

### Relationship Data Model
- **D-01:** Generic `RELATES_TO` edge table in Ladybug — not separate typed tables. Properties: `rel_type` ("calls", "imports", "inherits"), `confidence` ("DIRECT", "INFERRED"). Consistent with existing `CONTAINS` edge pattern but extensible without schema changes for future relationship types (e.g., Phase 3 variable references).
- **D-02:** Edges connect Chunk nodes to Chunk nodes (function calls function, class inherits class). Import relationships may connect File nodes to File nodes or Chunk nodes depending on resolution depth.

### Cross-File Resolution
- **D-03:** Aggressive resolution via tree-sitter AST extraction — attempt all resolution paths including multi-hop import chains, function pointers, and dynamic dispatch.
- **D-04:** Linter/type-checker validation as a second pass — validates tree-sitter extractions and upgrades INFERRED → DIRECT where the linter confirms resolution. Primary candidates: mypy/pyright for Python, clang-tidy/libclang for C.
- **D-05:** Resolution only targets chunks that are already indexed. If target is not in the index, relationship is INFERRED with whatever partial info is available.
- **D-06:** Import alias resolution handles: `from X import Y`, `import X; X.y()`, `from X.Y import Z`, relative imports (if target indexed), `self.method()` (resolve to class method).

### Confidence Tagging
- **D-07:** Boundary between DIRECT and INFERRED:
  - DIRECT: Same-file calls, resolved imports where target is indexed, `self.method()` resolved to class method, any relationship confirmed by linter pass
  - INFERRED: Unresolved import targets (not indexed), function pointers (unless linter resolves), dynamic dispatch / duck typing, C macro expansions (unless linter resolves), multi-hop import chains (unless linter confirms)
- **D-08:** Linter pass can upgrade INFERRED → DIRECT but never downgrades DIRECT → INFERRED.

### Markdown Output
- **D-09:** Dual format for relationships in per-file markdown:
  - **Inline per-chunk:** Under each chunk heading, show a small table of what it calls and what calls it. Keeps context localized — see a function and its connections together.
  - **Summary section:** New `## Relationships` section after `## Chunks`, subdivided by type (`### Calls`, `### Called By`, `### Imports`, `### Imported By`, `### Inherits`). Provides cross-file overview.
- **D-10:** Both formats serve different consumers — inline for scanning a specific function, summary for understanding file-level dependencies. Phase 3 query tool slices from both.

### Agent's Discretion
- Which specific linter/type-checker to use (mypy vs pyright vs pyflakes for Python, clang-tidy vs libclang for C)
- How to invoke the linter (subprocess, internal API, compilation database for C)
- Performance optimization — whether linter runs per-file or batched
- Exact `RELATES_TO` edge schema details (additional properties like `source_line`, `import_alias`, etc.)
- Error handling when linter is not installed or fails
- How to represent unresolved relationships in markdown

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project-level context
- `.planning/codebase/ARCHITECTURE.md` - Repository architecture, worktree pattern, data flow
- `.planning/codebase/STRUCTURE.md` - Directory layout, where glma code lives (`02-worktrees/glma/`)
- `.planning/codebase/CONVENTIONS.md` - Code style, naming patterns, uv for package management
- `.planning/codebase/STACK.md` - Technology stack (tree-sitter, Ladybug, Python 3.13, uv)

### Phase 1 implementation (directly extends this code)
- `02-worktrees/glma/src/glma/db/ladybug_store.py` - Existing LadybugStore with Chunk/File nodes, CONTAINS edges, upsert patterns. New `RELATES_TO` edge table goes here.
- `02-worktrees/glma/src/glma/models.py` - Chunk, FileRecord, IndexConfig models. May need Relationship model additions.
- `02-worktrees/glma/src/glma/index/parser.py` - Tree-sitter parser configs, LanguageConfig. Relationship extraction will use same AST infrastructure.
- `02-worktrees/glma/src/glma/index/chunks.py` - Chunk extraction pipeline. Relationship extraction parallels this — walks same AST nodes.
- `02-worktrees/glma/src/glma/index/pipeline.py` - Main indexing orchestrator. Relationship extraction is a new pipeline stage after chunk extraction.
- `02-worktrees/glma/src/glma/index/writer.py` - Markdown output writer. Needs new `## Relationships` section and inline per-chunk relationship tables.

### Requirements
- `.planning/REQUIREMENTS.md` - Phase 2 covers: RELS-01 through RELS-07, STOR-02, STOR-04
- `.planning/ROADMAP.md` §Phase 2 - Success criteria, plan breakdown (02-01 through 02-03)

### Phase 1 context (prior decisions)
- `.planning/phases/01-core-indexing-pipeline/01-CONTEXT.md` - Phase 1 decisions including Ladybug schema, upsert patterns, markdown structure

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **LadybugStore** (`db/ladybug_store.py`): Already manages Chunk/File nodes with CONTAINS edges. Adding RELATES_TO follows the same `CREATE REL TABLE` pattern. The `upsert_file` method's delete-then-recreate pattern applies to relationships too.
- **Tree-sitter parser configs** (`index/parser.py`): `PARSER_CONFIGS` dict with `LanguageConfig` objects define chunk_types and container_types per language. Relationship extraction needs similar per-language config for relationship-relevant AST node types (call_expression, import_statement, etc.).
- **AST walker** (`index/chunks.py`): `_walk_chunks` recursively walks AST nodes. Relationship extraction parallels this — walk looking for call expressions, import statements, and inheritance instead of chunk boundaries.
- **Comment attachment** (`index/comments.py`): Demonstrates post-processing pattern — extract chunks first, then do a second AST pass to attach metadata. Same pattern works for relationships: extract chunks, then walk AST for relationships.
- **Pipeline orchestrator** (`index/pipeline.py`): `run_index()` is the main loop. Relationship extraction would be a new stage after `extract_chunks` and `attach_comments`.

### Established Patterns
- **Ladybug edge tables**: `CREATE REL TABLE IF NOT EXISTS REL_NAME (FROM NodeType TO NodeType)`. Relationships use Cypher for creation and querying.
- **Upsert = delete + recreate**: `upsert_file` deletes chunks first (DETACH DELETE), then re-inserts. Same pattern for relationship edges on re-index.
- **Streaming per-file processing**: Pipeline processes one file at a time (parse → extract → write → discard). Relationship extraction may need cross-file context, which requires a two-pass approach: pass 1 extracts chunks, pass 2 resolves cross-file relationships.
- **Markdown heading structure**: `# filename` → `## Key Exports` → `## Chunks` → `### chunk_name`. Relationships add after `## Chunks` and inline within each chunk.

### Integration Points
- **LadybugStore schema**: Add `RELATES_TO` rel table. May need new query methods: `get_callers(chunk_id)`, `get_callees(chunk_id)`, `get_imports(file_path)`.
- **Pipeline stages**: New relationship extraction stage in `run_index()` — after chunk extraction, before markdown write. Likely needs to be two-pass: first pass extracts all chunks to DB, second pass resolves cross-file relationships.
- **Markdown writer**: `write_markdown()` and `format_file_markdown()` need relationship data passed in. New helper functions for inline relationship tables and summary section.
- **CLI**: No new CLI commands in Phase 2 (that's Phase 3). But `glma index` should now also extract relationships as part of indexing.

</code_context>

<specifics>
## Specific Ideas

- Aggressive resolution + linter validation is a layered approach: tree-sitter gives you breadth (finds all potential relationships), linter gives you depth (confirms or rejects uncertain ones). This means the linter is an optional enhancement — indexing works without it, just with more INFERRED tags.
- The two-pass indexing pattern (extract all chunks first, then resolve cross-file relationships) is important for cross-file resolution — you can't resolve `import foo; foo.bar()` until `foo.py` has been processed and its chunks are in the DB.
- Linter integration may need to be configurable — not all environments will have mypy or clang-tidy installed. Should degrade gracefully.

</specifics>

<deferred>
## Deferred Ideas

- **Semantic search with vector embeddings** — Phase 3 (Query Tool). The `summary` field on chunks (empty since Phase 1) will be populated and embedded for hybrid search.
- **Variable reference tracking** — Potential future relationship type. The generic `RELATES_TO` table supports adding `"variable_ref"` as a `rel_type` without schema changes.
- **Call graph visualization** — Deferred to v2 (ADVN-01). The relationship data model supports it, but visualization output is out of scope.
- **LLM-powered code summaries** — Deferred to v2 (ADVN-03). Could enhance relationship descriptions but not needed for structural extraction.

</deferred>

---

*Phase: 02-relationship-extraction*
*Context gathered: 2026-04-08*
