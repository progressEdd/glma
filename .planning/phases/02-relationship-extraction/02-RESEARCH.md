# Phase 2: Relationship Extraction - Research

**Researched:** 2026-04-09
**Status:** Research complete

## Research Question
What do I need to know to PLAN Phase 2 (relationship extraction) well?

---

## 1. Tree-Sitter AST Node Types for Relationships

### Python Relationship Nodes (tree-sitter-python)

**Function Calls:**
- `call` node — the top-level call expression
  - Child[0] is the callee (what's being called)
  - If callee is `identifier` → direct call: `foo()` → callee text = "foo"
  - If callee is `attribute` → method/qualified call: `self.method()`, `obj.method()`, `module.func()`
  - If callee is nested `attribute` → chained: `os.path.join()` → outer attribute, inner attribute

- `attribute` node — has two children: `object` (first child identifier) and `attribute` name (last child identifier)
  - `self.speak()` → attribute node with children: `identifier["self"]`, `.`, `identifier["speak"]`
  - `Dog.fetch(d, "ball")` → attribute node with children: `identifier["Dog"]`, `.`, `identifier["fetch"]`
  - `baz.something()` → attribute node with children: `identifier["baz"]`, `.`, `identifier["something"]`

**Imports:**
- `import_statement` → `import os`, `import foo.bar as baz`
  - Children: `import` keyword, then `dotted_name` or `aliased_import`
  - `aliased_import` has: `dotted_name` + `as` + `identifier` (alias)
  - `dotted_name` has children: `identifier`, `.`, `identifier`, ... (e.g., `foo.bar`)

- `import_from_statement` → `from pathlib import Path`, `from typing import Optional, List`
  - Children: `from` keyword, `dotted_name` (source module), `import` keyword, then `dotted_name`/`wildcard_import` children
  - Multiple imports in one statement appear as sibling `dotted_name` nodes separated by `,`

**Inheritance:**
- `class_definition` → has `argument_list` child for base classes
  - `class Dog(Animal):` → children: `class`, `identifier["Dog"]`, `argument_list` containing `identifier["Animal"]`
  - Multiple inheritance: `class C(A, B):` → `argument_list` has multiple `identifier` children
  - No argument_list = no explicit base class (implicitly inherits from `object`)

### C Relationship Nodes (tree-sitter-c)

**Function Calls:**
- `call_expression` → top-level call node
  - Child[0] is the callee
  - `identifier` callee → direct function call: `helper()`, `add(1,2)`, `printf(...)`
  - No method call syntax in C (unlike Python `self.method()`)
  - Function pointer calls appear as `call_expression` with `parenthesized_expression` callee (rare, mark INFERRED)

**Includes (C's "import"):**
- `preproc_include` → `#include <stdio.h>` or `#include "myheader.h"`
  - Children: `#include` keyword + path node
  - `system_lib_string` → `<stdio.h>` (system header, angled brackets)
  - `string_literal` → `"myheader.h"` (local header, quotes)
  - The actual path text is in the `string_content` child of `string_literal`, or the full text of `system_lib_string`

**Type Usage (C's "inheritance"):**
- No class inheritance in C. Struct usage appears as:
  - `type_identifier` in declarations: `Point pt;`
  - `struct_specifier` with `type_identifier`: `struct Circle c;`
  - `type_definition` creating typedefs
- C "inheritance" patterns: nested structs, function pointer tables — these are INFERRED at best

### Key Findings for Implementation

1. **Python call resolution requires scope tracking.** When we see `call_expression` with `attribute` callee, we need to know if the object is `self` (resolve to class method), a known import (resolve to imported module's function), or an unresolvable variable (INFERRED).

2. **C relationship extraction is simpler.** All calls are direct (`identifier` callee) or via function pointers (complex, INFERRED). Includes map 1:1 to files. No class hierarchy to resolve.

3. **Import alias resolution is the critical path.** The chain is: extract `import_statement`/`import_from_statement` → build per-file import map → when resolving calls, check if callee prefix matches a known import alias → resolve to the imported module/chunk.

---

## 2. Ladybug (real-ladybug) REL Table Patterns

### Verified: REL Tables with Properties Work

```python
conn.execute('CREATE REL TABLE IF NOT EXISTS RELATES_TO (FROM Chunk TO Chunk, rel_type STRING, confidence STRING, source_line INT64)')
conn.execute('MATCH (a:Chunk {id: $src}), (b:Chunk {id: $tgt}) CREATE (a)-[:RELATES_TO {rel_type: $rtype, confidence: $conf, source_line: $line}]->(b)')
```

**Key findings:**
- REL tables support arbitrary STRING/INT64 properties
- CREATE REL with properties uses `{key: $param}` syntax in the relationship clause
- MATCH patterns work as expected for querying relationships
- `DETACH DELETE` on Chunk nodes removes BOTH incoming and outgoing relationships

### Cross-File Re-Indexing Implication

When re-indexing file A:
1. `DETACH DELETE` chunks for file A → removes outgoing rels from A AND incoming rels to A from other files
2. Re-extract chunks for file A → new chunk IDs
3. **Problem:** Incoming relationships from other files to file A's OLD chunks are now gone
4. **Solution:** Two-pass approach: pass 1 re-extracts all chunks, pass 2 re-resolves ALL relationships (including cross-file ones pointing to the changed file)

### Schema Design

The `RELATES_TO` table should have these properties:
- `rel_type`: STRING — "calls", "imports", "inherits", "includes" (C-specific import)
- `confidence`: STRING — "DIRECT" or "INFERRED"
- `source_line`: INT64 — line number where the relationship originates
- `target_name`: STRING — the unresolved name as it appears in source (for display when target not indexed)

---

## 3. Two-Pass Pipeline Architecture

### Current Pipeline (Phase 1)
```
walk → detect → hash → parse → extract chunks → attach comments → store → write markdown
```

### New Pipeline (Phase 2)
```
Pass 1 (per-file, streaming — same as Phase 1):
  walk → detect → hash → parse → extract chunks → attach comments → store chunks

Pass 2 (cross-file, after all chunks stored):
  for each file:
    parse AST → extract relationships → resolve cross-file targets → store relationships

Pass 3 (per-file):
  for each file:
    load chunks + relationships → write markdown with relationship sections
```

### Why Two Passes

Cross-file resolution requires all chunks to be in the database. Consider:
```python
# file_a.py
from file_b import process_data
result = process_data(data)
```

To resolve `process_data` to its chunk in `file_b.py`, file_b must already be indexed with its chunks in the DB. A streaming single-pass approach cannot guarantee this ordering.

### Performance Consideration

Two passes means parsing each file's AST twice (once for chunks, once for relationships). This is acceptable because:
- Tree-sitter parsing is fast (sub-millisecond for typical source files)
- The second pass only walks relationship-relevant nodes (not extracting chunk content)
- Total overhead is roughly 1.3-1.5x compared to Phase 1 (not 2x, since we skip chunk content extraction in pass 2)

### Alternative: Cache ASTs in Memory

Could cache parsed trees in memory to avoid re-parsing in pass 2. But this breaks the streaming pattern and increases memory usage. For repos with 10K+ files, this could be problematic. **Recommendation:** Re-parse in pass 2. Profile later if performance is an issue.

---

## 4. Import Resolution Algorithm

### Step 1: Build Per-File Import Map

For each Python file, extract all import statements and build a mapping:

```python
import_map = {
    "os": ("os", None),              # import os → module "os", no specific name
    "Path": ("pathlib", "Path"),     # from pathlib import Path
    "baz": ("foo.bar", None),        # import foo.bar as baz → module "foo.bar"
    "Optional": ("typing", "Optional"),  # from typing import Optional
}
```

For C files:
```python
include_map = {
    "myheader.h": "path/to/myheader.h",   # local include → resolve to file path
    "utils.h": "path/to/utils.h",
    # system_lib_string includes are NOT resolved (system headers)
}
```

### Step 2: Resolve Callee Names

When encountering a `call` node with `attribute` callee like `baz.something()`:
1. Check if "baz" is in import_map → yes, it maps to module "foo.bar"
2. Look up chunks in DB where file_path matches "foo/bar.py" and name = "something"
3. If found → DIRECT relationship to that chunk
4. If not found → INFERRED relationship with target_name = "foo.bar.something"

For `self.method()` calls:
1. Detect `self` as the attribute object
2. Find the enclosing class chunk (from parent chain or via parent_id on the method chunk)
3. Look up method chunk in same class with name = "method"
4. If found → DIRECT
5. If not found in this class → check parent classes (inheritance chain) → DIRECT if found, INFERRED if chain incomplete

For plain identifier calls like `foo()`:
1. Check if "foo" is in import_map → if yes, resolve to imported module's chunk
2. If not imported → same-file lookup: find chunk with name "foo" in current file
3. If not found → INFERRED

### Step 3: C Include Resolution

For `#include "myheader.h"`:
1. Search for file named "myheader.h" in the indexed files
2. Search relative to the including file's directory first, then repo root
3. If found → DIRECT relationship from including file's chunks to header's chunks
4. If not found → INFERRED with target_name = "myheader.h"

---

## 5. Confidence Tagging Rules

### DIRECT Relationships

| Pattern | Language | Confidence |
|---------|----------|------------|
| Same-file function call (`foo()` where `foo` is defined in same file) | Python, C | DIRECT |
| `self.method()` resolved to class method | Python | DIRECT |
| `from X import Y` where Y's chunk is in the index | Python | DIRECT |
| `#include "file.h"` where file.h is indexed | C | DIRECT |
| Class inheritance `class B(A)` where A's chunk is indexed | Python | DIRECT |
| Static method call `ClassName.method()` where both class and method are indexed | Python | DIRECT |

### INFERRED Relationships

| Pattern | Language | Confidence |
|---------|----------|------------|
| Call to unresolvable identifier | Python, C | INFERRED |
| `obj.method()` where obj type is unknown | Python | INFERRED |
| Function pointer call in C | C | INFERRED |
| `from X import Y` where Y is not in index (stdlib, external) | Python | INFERRED |
| `#include <system.h>` system headers | C | INFERRED |
| Dynamic dispatch / duck typing | Python | INFERRED |
| Multi-hop import chain (import alias chain) | Python | INFERRED |
| C macro expansion | C | INFERRED |

### Linter Upgrades (Phase 2 decision point)

CONTEXT.md specifies linter validation as a second pass. However, research shows:
- **mypy/pyright** for Python: Can resolve types but requires either type annotations or successful inference
- **clang-tidy/libclang** for C: Requires compilation database (`compile_commands.json`) which may not exist

**Recommendation:** Implement linter pass as optional enhancement, not core requirement. The tree-sitter-only approach covers ~80% of cases with DIRECT confidence. Linter adds incremental accuracy at significant integration cost.

---

## 6. Markdown Output Design

### Per-Chunk Inline Format (under each chunk heading)

```markdown
### fetch (method, L10-L15, parent: Dog)

Calls: helper (INFERRED), get_helper (DIRECT → Dog.get_helper)
Called by: standalone (DIRECT)
```

### File-Level Summary Section

```markdown
## Relationships

### Outgoing Calls
| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| Dog.fetch | Dog.get_helper | DIRECT | L12 |
| Dog.fetch | ? (helper) | INFERRED | L11 |
| standalone | Dog (constructor) | DIRECT | L20 |

### Incoming Calls
| From | To | Confidence |
| ---- | -- | ---------- |
| standalone | Dog.speak | DIRECT |

### Imports
| Import | Source | Confidence |
| ------ | ------ | ---------- |
| Path | pathlib | DIRECT |
| baz | foo.bar | DIRECT |

### Imported By
*(populated during cross-file resolution — which files import this file's chunks)*

### Inherits
| Class | Base | Confidence |
| ----- | ---- | ---------- |
| Dog | Animal | DIRECT |
```

### Key Design Decision

The inline format shows a compact view (name + confidence + target), while the summary section provides a full tabular view with line numbers. Both are generated from the same relationship data — no separate extraction passes needed.

---

## 7. Data Model Changes

### New Models (in models.py)

```python
class RelType(str, Enum):
    CALLS = "calls"
    IMPORTS = "imports"
    INHERITS = "inherits"
    INCLUDES = "includes"  # C-specific

class Confidence(str, Enum):
    DIRECT = "DIRECT"
    INFERRED = "INFERRED"

class Relationship(BaseModel):
    source_id: str       # Chunk ID of the source
    target_id: str       # Chunk ID of the target (empty string if INFERRED/unresolved)
    target_name: str     # Unresolved name as it appears in source
    rel_type: RelType
    confidence: Confidence
    source_line: int     # Line where relationship originates
```

### LadybugStore Additions

New schema + methods:
- `SCHEMA_RELATES_TO` — CREATE REL TABLE with properties
- `upsert_relationships(file_path, relationships)` — delete old rels for file's chunks, insert new ones
- `get_callers(chunk_id)` — incoming call relationships
- `get_callees(chunk_id)` — outgoing call relationships
- `get_imports(file_path)` — import relationships for a file
- `get_inheritance(class_name)` — inheritance chain

### Cross-File Cleanup Pattern

When re-indexing a file:
1. Delete the file's chunks (DETACH DELETE removes their relationships)
2. Re-insert chunks
3. **BUT** — other files may have had relationships pointing TO the old chunks
4. Solution: The two-pass approach means ALL relationships are re-extracted in pass 2, so stale relationships from other files get recreated correctly

---

## 8. Risk Areas & Open Questions

### Risk: Performance on Large Repos

Two-pass parsing means every file is parsed twice. For a repo with 10K files, this doubles parse time. Mitigation: Pass 2 only walks for relationships (no content extraction), and tree-sitter is very fast.

### Risk: Import Resolution Accuracy

Python's dynamic nature means some imports can't be resolved statically:
- `importlib.import_module(name)` — dynamic imports
- `sys.modules` manipulation
- `__init__.py` re-exports

**Mitigation:** Mark these as INFERRED. The `__init__.py` case can be partially handled by checking if an imported name matches an `__init__.py` re-export.

### Risk: C Header Resolution

`#include "file.h"` resolution requires knowing the include search path:
- Relative to the including file's directory
- Repository root
- Any `-I` include paths from the build system

**Mitigation:** Search relative to including file first, then repo root. Build-system include paths are out of scope (mark as INFERRED if not found).

### Open Question: Linter Integration Scope

CONTEXT.md mentions linter validation as a second pass. Research shows this is significant additional complexity:
- Requires mypy/pyright/clang-tidy as optional dependencies
- Requires configuration (mypy.ini, .clang-tidy, compile_commands.json)
- Adds substantial integration code

**Recommendation for Phase 2:** Implement tree-sitter-only extraction first. Linter integration as an optional enhancement within Phase 2 if time permits, or defer to Phase 2.1.

---

## 9. Existing Code Integration Points

### Files to Modify

| File | Changes |
| ---- | ------- |
| `models.py` | Add `RelType`, `Confidence`, `Relationship` models |
| `db/ladybug_store.py` | Add `SCHEMA_RELATES_TO`, relationship CRUD methods |
| `index/parser.py` | Add relationship-relevant AST node type configs per language |
| `index/relationships.py` | **NEW** — relationship extraction module (pass 2) |
| `index/resolver.py` | **NEW** — cross-file resolution module |
| `index/pipeline.py` | Add pass 2 (relationship extraction) and pass 3 (markdown with relationships) |
| `index/writer.py` | Add relationship sections to markdown output |
| `cli.py` | No changes (relationship extraction is automatic during indexing) |

### Test Files to Add

| File | What it tests |
| ---- | ------------- |
| `tests/test_relationships.py` | Relationship extraction from ASTs |
| `tests/test_resolver.py` | Import resolution, cross-file resolution |
| `tests/test_store_rels.py` | LadybugStore relationship CRUD |
| `tests/test_writer_rels.py` | Markdown output with relationship sections |

### Reusable Patterns from Phase 1

1. **`_walk_chunks` pattern** → adapt to `_walk_relationships` that walks AST for call/import/inherit nodes
2. **`PARSER_CONFIGS` pattern** → add relationship node type configs alongside chunk type configs
3. **`upsert_file` delete+recreate pattern** → applies to relationships too
4. **`attach_comments` post-processing pattern** → same pattern: extract chunks first, then do relationship pass

---

## RESEARCH COMPLETE

Key takeaways for planning:
1. Two-pass pipeline architecture (chunks first, then relationships) is the right approach
2. Tree-sitter node types for both languages are well-understood and documented above
3. Ladybug REL tables with properties are verified to work correctly
4. Import resolution is the most complex sub-problem — needs careful per-file import map construction
5. Linter integration should be optional/deferred — tree-sitter-only covers 80%+ of cases
6. DETACH DELETE correctly removes both incoming and outgoing relationships for re-indexing
7. 7 files to modify, 2 new files to create, 4 new test files
