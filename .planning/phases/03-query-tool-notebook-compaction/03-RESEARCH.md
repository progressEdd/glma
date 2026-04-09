# Phase 3: Query Tool & Notebook Compaction - Research

**Researched:** 2026-04-09
**Status:** Complete

## RESEARCH COMPLETE

---

## 1. Current Codebase State

### What's Built (Phase 1-2)

The glma tool has a working indexing pipeline that:

1. **Walks** source directories → **detects** C/Python files → **hashes** for incremental updates
2. **Parses** with tree-sitter → **extracts** chunks (functions, classes, methods, module code)
3. **Attaches** comments to chunks via AST post-processing
4. **Stores** chunks in Ladybug (real_ladybug) graph DB with File → Chunk → RELATES_TO schema
5. **Extracts** relationships: calls, imports, includes, inheritance (Phase 2)
6. **Writes** layered markdown per file (Phase 1-2 writer.py)
7. **Resolves** cross-file relationships with 3-pass pipeline

### Key Files to Extend

| File | Role | Phase 3 Changes |
|------|------|-----------------|
| `cli.py` | Typer CLI with `index` command | Add `query` command with flags |
| `db/ladybug_store.py` | LadybugStore with chunk/file/relationship queries | Add `get_file_by_path()`, `get_chunks_for_file()`, `get_index_metadata()` |
| `models.py` | Chunk, FileRecord, Relationship, IndexConfig | May add QueryConfig, QueryResult models |
| `index/writer.py` | Full markdown writer | NOT reused — query output is a different compact format |
| `index/pipeline.py` | 3-pass indexing orchestrator | Read-only — query reads from its output |

### Database Schema (Ladybug Cypher)

```
Node: File    {path PK, language, content_hash, last_indexed, chunk_count}
Node: Chunk   {id PK, file_path, chunk_type, name, content, summary, start_line, end_line, content_hash, parent_id}
Edge: CONTAINS  (File → Chunk)
Edge: RELATES_TO (Chunk → Chunk) {rel_type, confidence, source_line, target_name}
```

Chunk ID format: `{file_path}::{chunk_type}::{name}::{start_line}`

### Existing Query Methods in LadybugStore

- `get_outgoing_relationships(chunk_id)` → list of rel dicts with target info
- `get_incoming_relationships(chunk_id)` → list of rel dicts with source info
- `get_file_relationships(file_path)` → all outgoing rels for a file's chunks
- `get_indexed_files()` → dict of path → content_hash
- `get_file_hash(file_path)` → content hash or None

**Missing methods needed:**
- `get_file_by_path(file_path)` → FileRecord or None
- `get_chunks_for_file(file_path)` → list[Chunk] (currently done via raw Cypher in pipeline.py `_load_chunks_from_store`)
- `get_index_metadata(file_path)` → last_indexed, chunk_count, content_hash

---

## 2. Query Tool Architecture

### Command Structure

```
glma query <filepath> [OPTIONS]
```

The query command:
1. Resolves the repo root (look for `.glma-index/` or `.glma.toml`)
2. Opens LadybugStore in read-only mode
3. Looks up the file by path
4. Loads chunks and relationships
5. Generates compact markdown output
6. Outputs to stdout (or file via `--output`)

### Read-Only Store Access

Ladybug's `Database` + `Connection` can be opened without writing. No special read-only mode needed — the query command simply doesn't call any write methods. No schema initialization needed either (tables already exist from indexing).

### Layered Output Format

Per CONTEXT.md D-01 through D-04, the default compact output:

```
# src/auth/login.py
*Last indexed: 2026-04-09T10:30:00Z | 5 chunks*

## Summary
(Synopsis from available comments/chunk names)

## Signatures
- `authenticate(username: str, password: str) -> Token` — Validates credentials
  → calls: hash_password(), create_session()
  → called by: login_handler()

- `create_session(user_id: int) -> Session` — Creates user session
  → calls: generate_token()
  → called by: authenticate()

## Dependencies
### Incoming
- login_handler() in src/api/routes.py
### Outgoing
- hash_password() in src/crypto/utils.py
- generate_token() in src/auth/tokens.py

## Index Metadata
- File hash: abc123...
- Last indexed: 2026-04-09T10:30:00Z
- Chunks: 5
```

`--verbose` adds `## Full Code` section with all chunk contents in code blocks.

### New Query-Specific Methods for LadybugStore

```python
def get_file_record(self, file_path: str) -> Optional[FileRecord]:
    """Get file record by path."""

def get_chunks_for_file(self, file_path: str) -> list[Chunk]:
    """Get all chunks for a file, ordered by start_line."""

def get_all_relationships_for_file(self, file_path: str) -> dict:
    """Get all relationships (incoming + outgoing) for a file's chunks.
    Returns {chunk_id: {outgoing: [...], incoming: [...]}}"""
```

### Error Handling (CONTEXT.md D-15, D-16)

- Exit 1: file not found on disk → `sys.exit(1)`
- Exit 2: file not indexed → `sys.exit(2)`
- Exit 3: stale index (file modified since) → `sys.exit(3)` 
- Exit 4: query/DB error → `sys.exit(4)`
- Human messages to stderr, stdout stays clean

### Stale Index Detection

Compare file's current mtime or content hash against the stored `last_indexed` / `content_hash` in the File node. BLAKE2b hash comparison is the most reliable approach (already used by pipeline.py). For the query tool, we should:
1. Read the file's current hash using `file_content_hash()`
2. Compare against stored `content_hash` in the File record
3. If different, output a warning header and set exit code 3

---

## 3. Jupyter Notebook Compaction

### nbformat Integration

nbformat is the standard library for parsing `.ipynb` files. It's NOT currently in `pyproject.toml` dependencies — must be added.

**nbformat** is part of the Jupyter ecosystem. Key API:
```python
import nbformat

nb = nbformat.read(filepath, as_version=4)
for cell in nb.cells:
    if cell.cell_type == 'code':
        source = cell.source
        outputs = cell.outputs  # list of Output objects
    elif cell.cell_type == 'markdown':
        source = cell.source
```

**Dependency consideration:** nbformat pulls in few dependencies (traitlets, fastjsonschema). It's lightweight and stable.

### Per-Statement Variable Tracking (D-05)

This requires AST-level analysis of each code cell. Python's `ast` module (stdlib) can parse each cell's source:

```python
import ast

tree = ast.parse(cell_source)
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        # node.targets → names being defined
        # Walk body for Name nodes → names being referenced
    elif isinstance(node, ast.AugAssign):
        # target is being modified (counts as both def and ref)
    elif isinstance(node, ast.FunctionDef):
        # node.name → function defined
    elif isinstance(node, ast.ClassDef):
        # node.name → class defined
```

**Key insight:** We need an `ast.NodeVisitor` subclass that tracks:
- **Definitions:** `ast.Assign` targets, `ast.FunctionDef` names, `ast.ClassDef` names, `ast.Import`/`ast.ImportFrom` names
- **References:** `ast.Name` with `Load` context, `ast.Attribute` chains

**Per-statement granularity:** Walk `tree.body` (top-level statements) and process each individually. This gives "Cell 3 L1: defines `model`" vs "Cell 3 L5: defines `accuracy`".

### Variable Flow Summary (D-06)

After processing all cells, build a dict:
```python
variable_flow = {
    "model": {"defined_cell": 1, "defined_line": 3, "used_cells": [3, 5, 7]},
    "accuracy": {"defined_cell": 3, "defined_line": 5, "used_cells": [5, 6]},
}
```

Then render as:
```
## Variable Flow
| Variable | Defined (Cell) | Used (Cells) |
| -------- | -------------- | ------------ |
| model    | Cell 1, L3     | Cells 3, 5, 7 |
| accuracy | Cell 3, L5     | Cells 5, 6   |
```

### Notebook Pipeline

Notebooks are NOT indexed through the tree-sitter pipeline. They have a separate path:

```
.ipynb file → nbformat.read() → cell extraction → per-cell AST analysis → variable tracking → compacted markdown
```

This can be:
- **Option A:** A separate module `glma/query/notebook.py` that the query command calls when the file extension is `.ipynb`
- **Option B:** Integrated into the query formatter, detected by file extension

**Recommendation:** Option A — cleaner separation. The query command dispatches to `format_notebook_output()` when detecting `.ipynb`.

### Notebook Query Flow

1. User runs `glma query analysis.ipynb`
2. Query command detects `.ipynb` extension
3. Opens and parses notebook with nbformat
4. Extracts code/markdown cells with cell indices
5. For each code cell: AST parse → extract definitions and references per statement
6. Build cross-cell variable flow map
7. Render compacted markdown with:
   - Cell index + type indicator
   - Code content (syntax-highlighted)
   - Per-statement `defines:` / `references:` annotations
   - Cross-cell origin annotations
   - Markdown cells as blockquotes
   - `## Variable Flow` summary table
8. Cell outputs stripped by default (D-08)

---

## 4. Dependency Traversal (--depth N)

### Implementation Strategy

The `--depth N` flag enables multi-hop relationship traversal:

- **Depth 1 (default):** Just the file's direct relationships
- **Depth 2:** Follow outgoing/incoming to get 2-hop relationships
- **Depth N:** BFS/DFS traversal up to N hops

Implementation:
```python
def traverse_relationships(store, chunk_ids, depth, visited=None):
    """BFS traversal of relationships up to `depth` hops."""
    if visited is None:
        visited = set()
    if depth == 0:
        return []
    
    results = []
    for chunk_id in chunk_ids:
        if chunk_id in visited:
            continue
        visited.add(chunk_id)
        outgoing = store.get_outgoing_relationships(chunk_id)
        incoming = store.get_incoming_relationships(chunk_id)
        # Follow targets/sources for next depth level
        next_ids = [r['target_id'] for r in outgoing] + [r['source_id'] for r in incoming]
        results.extend(outgoing + incoming)
        results.extend(traverse_relationships(store, next_ids, depth - 1, visited))
    return results
```

**Safety:** Cap depth at 10 (CONTEXT.md agent's discretion) to prevent runaway traversals on highly connected codebases.

---

## 5. JSON Output Format (--format json)

For programmatic consumption (agents piping to tools):

```json
{
  "file": "src/auth/login.py",
  "metadata": {
    "language": "python",
    "last_indexed": "2026-04-09T10:30:00Z",
    "chunk_count": 5,
    "content_hash": "abc123..."
  },
  "chunks": [
    {
      "name": "authenticate",
      "type": "function",
      "signature": "authenticate(username: str, password: str) -> Token",
      "docstring": "Validates credentials",
      "start_line": 15,
      "end_line": 32
    }
  ],
  "relationships": {
    "outgoing": [...],
    "incoming": [...]
  }
}
```

---

## 6. New Files to Create

| File | Purpose |
|------|---------|
| `glma/query/__init__.py` | Query module package |
| `glma/query/formatter.py` | Compact markdown formatter for source files |
| `glma/query/notebook.py` | Notebook parsing, variable tracking, compaction |
| `glma/query/variables.py` | AST-based variable extraction per statement |

Files to modify:
| File | Changes |
|------|---------|
| `glma/cli.py` | Add `query` command with all flags |
| `glma/db/ladybug_store.py` | Add `get_file_record()`, `get_chunks_for_file()`, `get_all_relationships_for_file()` |
| `glma/models.py` | Add `QueryConfig` model if needed |
| `pyproject.toml` | Add `nbformat` dependency |

---

## 7. Risk Assessment

| Risk | Mitigation |
|------|------------|
| Ladybug Cypher query limitations | Store methods are already proven in Phase 2; new queries follow same patterns |
| nbformat adds dependency weight | nbformat is lightweight (~200KB), only needed for notebook queries |
| AST parsing failures in notebook cells | Wrap in try/except; skip cells that fail to parse, include raw source |
| Variable tracking in complex Python (comprehensions, decorators, star imports) | Start with simple cases (Assign, FunctionDef, Import); handle edge cases incrementally |
| Stale index detection overhead | BLAKE2b hashing is fast; reuse `file_content_hash()` from pipeline.py |
| `--depth N` traversal performance on large graphs | Cap at depth 10, use BFS with visited set, skip self-referential edges |

---

## 8. Testing Strategy

- **Unit tests:** Query formatter output, notebook parser, variable tracker, CLI flags
- **Integration tests:** `glma query` against a real indexed repo (use test fixtures from Phase 1-2)
- **Error tests:** File not found, not indexed, stale index, corrupt notebook
- **Output validation:** Grep-verifiable acceptance criteria for all outputs

---

## 9. Key Patterns to Follow

1. **Typer CLI pattern:** `@app.command()` with typed parameters, Rich console for output
2. **LadybugStore pattern:** Parameterized Cypher queries, results as list of dicts
3. **Pydantic models:** All config/result objects use BaseModel
4. **Error handling:** `typer.Exit(code=N)` with console error messages to stderr
5. **Module organization:** New `query/` package mirrors existing `index/` package structure
