# Phase 1: Core Indexing Pipeline - Research

**Researched:** 2026-04-08
**Status:** Complete

## Research Question

What do I need to know to PLAN Phase 1 (Core Indexing Pipeline) well?

---

## 1. Storage Engine: Ladybug vs LanceDB

### Decision Context

CONTEXT.md (D-Init) chose **Ladybug (package: `real_ladybug`)** over LanceDB. Prior research (`.planning/research/STACK.md`) recommended LanceDB. This section validates the Ladybug decision for Phase 1 scope.

### Ladybug (real_ladybug) — Current State

| Attribute | Value |
|-----------|-------|
| PyPI package | `real_ladybug` |
| Latest version | 0.15.3 |
| Python support | cp310–cp314 (confirmed cp313 wheels) |
| No runtime deps | ✓ (core has zero required deps) |
| Description | "Highly scalable, extremely fast, easy-to-use embeddable graph database" |
| Docs | https://docs.ladybugdb.com/ |
| GitHub | https://github.com/lbugdb/lbug |

**Key capabilities:**
- Embedded graph database (no server process, like Kuzu before it)
- Cypher-like query language (directly reusable from hackathon Kuzu code)
- Native vector indices (new since Kuzu fork)
- Full-text search
- Node/edge table model with strict schema

**Ladybug IS Kuzu's successor** — same API patterns, same Cypher dialect. The hackathon `develop.ipynb` code using `kuzu.Database()`, `conn.execute()`, and Cypher queries translates directly to `ladybug.Database()`, `conn.execute()` with near-zero code changes.

### LanceDB — Current State

| Attribute | Value |
|-----------|-------|
| PyPI package | `lancedb` |
| Latest version | 0.30.2 |
| Heavy deps | pyarrow, pydantic, numpy, tqdm, deprecation, overrides, packaging, lance-namespace |
| Model | Serverless, column-oriented (Arrow-based), vector + metadata |

### Assessment for Phase 1

**Phase 1 does NOT need semantic search, vector indices, or full-text search.** Phase 1 needs:
1. Store code chunks with structured metadata (file_path, chunk_type, name, content, line ranges)
2. Write companion markdown files
3. Content hashing for incremental re-indexing

Both databases can do this trivially. The deciding factors:

| Factor | Ladybug | LanceDB |
|--------|---------|---------|
| Phase 1 needs | ✓ Structured storage of chunks | ✓ Same |
| Phase 2 needs | ✓ Native graph edges for relationships | ✗ Needs join tables for relationships |
| Phase 3 needs | ✓ Built-in vector search + FTS | ✓ Built-in vector search |
| Weight / deps | Lightweight, no required deps | Heavy: pyarrow, pydantic, numpy chain |
| Hackathon reuse | Direct (Kuzu → Ladybug API compatible) | Rewrite needed |
| Query model | Graph-native for "who calls X" | Must simulate via metadata joins |
| Single DB for all phases | ✓ | Partial (relationships are awkward) |

**Conclusion: Ladybug is the right choice.** It unifies all four phases in one DB, has lighter dependencies, and hackathon code is directly reusable. LanceDB would have worked for Phase 1 but created friction in Phase 2 (relationship extraction is inherently graph-shaped).

### Ladybug Schema for Phase 1

```cypher
-- Node table: code chunks
CREATE NODE TABLE Chunk (
    id STRING,
    file_path STRING,
    chunk_type STRING,      -- 'function', 'class', 'method', 'module'
    name STRING,
    content STRING,
    summary STRING,         -- nullable, for Phase 3 semantic search
    start_line INT64,
    end_line INT64,
    content_hash STRING,    -- for incremental re-indexing
    parent_id STRING,       -- nullable, links method→class
    PRIMARY KEY (id)
);

-- Node table: files (for file-level metadata)
CREATE NODE TABLE File (
    path STRING,
    language STRING,
    content_hash STRING,
    last_indexed STRING,    -- ISO timestamp
    chunk_count INT64,
    PRIMARY KEY (path)
);

-- Edge table: containment
CREATE REL TABLE CONTAINS (FROM File TO Chunk);
```

### Ladybug API Pattern (from hackathon, adapted)

```python
import ladybug

db = ladybug.Database("./.glma-index/db")
conn = ladybug.Connection(db)

# Create schema
conn.execute("CREATE NODE TABLE Chunk (...)")

# Insert
conn.execute("CREATE (c:Chunk {id: $id, file_path: $fp, ...})", {"id": "...", "fp": "..."})

# Query
result = conn.execute("MATCH (c:Chunk {file_path: $fp}) RETURN c.*")
```

---

## 2. Tree-Sitter Parsing Pipeline

### Current Versions

| Package | Version in hackathon | Latest on PyPI |
|---------|---------------------|----------------|
| tree-sitter | 0.24.0 | 0.25.2 |
| tree-sitter-c | 0.24.1 | 0.24.1 |
| tree-sitter-python | 0.23.6 | 0.25.0 |

**Recommendation:** Pin to latest versions (0.25.x). The API changed between 0.24 and 0.25 — the `Language` construction pattern changed. Use the 0.25 API:

```python
import tree_sitter_c as tsc
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

C_LANGUAGE = Language(tsc.language())
PY_LANGUAGE = Language(tspython.language())

parser = Parser(C_LANGUAGE)
tree = parser.parse(source_bytes)
root = tree.root_node
```

### Chunk Extraction Strategy

Based on hackathon exploration (cells 73–82 in `develop.ipynb`) and CONTEXT.md decisions:

**Node types to extract:**

| Language | Chunk Type | Tree-sitter Node Type |
|----------|-----------|----------------------|
| C | function | `function_definition` |
| C | struct | `struct_specifier` (with body) |
| C | enum | `enum_specifier` (with body) |
| C | typedef | `type_definition` |
| C | module | top-level nodes not in above |
| Python | function | `function_definition` |
| Python | class | `class_definition` |
| Python | method | `function_definition` inside `class_definition` |
| Python | module | top-level nodes not in above |

**Nested extraction (D-04, D-05):**
```
class_definition → class chunk (parent_id=None)
  └── function_definition → method chunk (parent_id=class_id)
```

Walk `root_node.children` recursively. For each child:
1. Check if `node.type` matches a chunk type
2. If yes: create chunk with `start_point` → `end_point` (0-indexed line/col)
3. If node has children matching chunk types, recurse (nested extraction)
4. Remaining top-level nodes that aren't recognized → module-level chunk

### Comment Attachment (D-05, IDXC-05)

**The hackathon problem:** Single-line comments (`//`) and block comments (`/* */`) are separate AST nodes, not attached to function/class nodes. They appear as siblings or preceding nodes.

**Solution approach (AST post-processing pass):**
1. After chunk extraction, iterate all comment nodes (types: `comment`, `block_comment`)
2. For each comment, find the nearest following code chunk by line proximity
3. **Heuristic:** A comment is "attached" to a chunk if:
   - It immediately precedes the chunk (gap ≤ 1 blank line)
   - OR it's a docstring (Python: first child `expression_statement` → `string` inside `function_definition`/`class_definition`)

**Python docstrings** are easier — they're the first statement in a function/class body:
```python
# Inside a function_definition node:
body = node.child_by_field_name("body")
if body and body.children:
    first = body.children[0]
    if first.type == "expression_statement" and first.children[0].type == "string":
        # This is the docstring
```

**C comments** require the proximity heuristic:
```python
# Collect all top-level nodes with their line ranges
# For each comment node, find the nearest non-comment sibling below it
# If gap <= 1 line, attach comment to that chunk
```

---

## 3. CLI Framework

### Options

| Framework | Latest | Pros | Cons |
|-----------|--------|------|------|
| Typer | 0.24.1 | Type-hint driven, modern, built on Click | Slightly more magic |
| Click | 8.x | Battle-tested, explicit | More boilerplate |
| argparse | stdlib | No dependency | Verbose for subcommands |

**Recommendation: Typer** — aligns with modern Python practices, gives clean subcommand structure with minimal code. CONTEXT.md (D-13, D-14) specifies `.glma.toml` config file with CLI flag overrides — `tomllib` (stdlib in 3.13) for reading config.

### CLI Structure

```
glma index [PATH] [--quiet] [--config FILE]
glma query <FILEPATH> [--verbose]   # Phase 3
glma watch [PATH]                    # Phase 4
glma export [PATH]                   # Phase 4
```

Phase 1 only implements `glma index`. The app structure should be:

```
glma/
├── __init__.py
├── __main__.py          # entry point: python -m glma
├── cli.py               # Typer app with subcommands
├── config.py            # .glma.toml loading + merge with CLI flags
├── index/               # Indexing subsystem
│   ├── __init__.py
│   ├── walker.py        # Directory walking, skip patterns
│   ├── detector.py      # Language detection from file extension
│   ├── parser.py        # Tree-sitter parsing pipeline
│   ├── chunks.py        # Chunk extraction + comment attachment
│   └── writer.py        # Ladybug storage + markdown output
├── db/                  # Database abstraction
│   ├── __init__.py
│   └── ladybug_store.py # Ladybug connection, schema, CRUD
└── models.py            # Pydantic models for Chunk, File, IndexConfig
```

### Config File (.glma.toml)

```toml
[index]
languages = ["c", "python"]        # Which languages to index
output_dir = ".glma-index"         # Index output directory
include = []                        # Glob patterns to include (empty = all)
exclude = [".git", "venv", "node_modules", "__pycache__", ".tox", "build", "dist"]
```

---

## 4. Directory Walking & File Filtering

### Skip Patterns (IDXC-02)

**Default exclude list:**
```python
DEFAULT_EXCLUDE = {
    ".git", ".svn", ".hg",                    # VCS
    "venv", ".venv", "env",                    # Python virtualenvs
    "node_modules", "bower_components",         # JS
    "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",  # Python cache
    "build", "dist", "egg-info",               # Build artifacts
    ".tox", ".nox",                            # Test environments
    ".glma-index",                             # Our own output
}
```

**Binary detection:** Skip files without recognized source extensions. Don't try to detect binary by content — extension-based filtering is faster and sufficient for Phase 1.

```python
SUPPORTED_EXTENSIONS = {
    ".c": "c", ".h": "c",
    ".py": "python", ".pyw": "python",
}
```

**Walking strategy:** Use `pathlib.Path.rglob()` or `os.walk()` with prune-on-exclude. For 10K+ file repos, `os.walk()` with directory pruning is more memory-efficient than collecting all paths first.

---

## 5. Markdown Output Format

### Per-File Markdown (D-08, D-09)

```markdown
# path/to/file.py

Brief summary of what this file does (empty in Phase 1 — for Phase 3 LLM generation).

## Key Exports

| Name | Type | Description |
|------|------|-------------|
| MyClass | class | (empty in Phase 1) |
| my_func | function | (empty in Phase 1) |

## Chunks

### MyClass (class, L10-L50)

```python
class MyClass:
    """Docstring attached."""
    
    def __init__(self):
        ...
```

### MyClass.__init__ (method, L13-L16, parent: MyClass)

```python
    def __init__(self):
        ...
```

### my_func (function, L53-L70)

# Attached comment from above function
def my_func():
    ...
```
```

**Storage location:** `.glma-index/markdown/<relative-path>.md` — mirrors source tree structure.

---

## 6. Progress Display (D-15, D-16)

**Library choice: `rich`** (v14.3.3)
- Rich is already a de facto standard for Python CLI output
- Provides `Progress` with spinners, file counts, ETAs
- Integrates well with Typer (`typer.progressbar()` is limited; rich.progress is superior)

```python
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn

with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
) as progress:
    task = progress.add_task("Indexing...", total=len(files))
    for file in files:
        process_file(file)
        progress.advance(task)
```

---

## 7. Content Hashing & Incremental Re-Indexing (IDXC-06)

### Strategy

```python
import hashlib

def content_hash(content: bytes) -> str:
    return hashlib.blake2b(content, digest_size=32).hexdigest()
```

**BLAKE2b** — faster than SHA-256, built into hashlib, no external dependency.

### Incremental Logic

1. On `glma index /path`:
   - Walk directory, collect all source files
   - Load existing `File` nodes from Ladybug (their `content_hash` values)
   - For each file: compute hash, compare with stored hash
   - Only parse + store files whose hash changed OR are new
   - Delete chunks for files that no longer exist
   - Update `File` nodes with new hashes and timestamps

---

## 8. Memory Efficiency (IDXC-09)

**Streaming pipeline:** parse → extract → write → discard.

- Read one file at a time (don't load all files into memory)
- Parse with tree-sitter (returns a tree, but we extract chunks immediately)
- Write chunks to Ladybug and markdown to disk
- Discard the tree and raw content before moving to next file

For 10K+ files, this keeps memory bounded to ~1 file at a time rather than accumulating all parse trees.

---

## 9. Key Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Ladybug API differs from Kuzu enough to cause rework | Low | Medium | Ladybug is explicitly Kuzu's successor with compatible API — verify in Plan 01-01 with a smoke test |
| Tree-sitter 0.25 API changes break hackathon patterns | Medium | Low | Use 0.25 patterns documented above; API is well-documented |
| Comment attachment heuristic misses edge cases | Medium | Medium | Phase 1 heuristic doesn't need to be perfect — attach what we can, defer hard cases |
| Large repo performance (10K+ files) | Low | High | Streaming pipeline + incremental hashing; benchmark in Plan 01-04 |
| tree-sitter parse errors on malformed code | Medium | Low | Skip files with ERROR nodes at root, log warning, continue |

---

## 10. Dependencies for Phase 1

```toml
[project]
name = "glma"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "real_ladybug>=0.15.3",
    "tree-sitter>=0.25.2",
    "tree-sitter-c>=0.24.1",
    "tree-sitter-python>=0.25.0",
    "typer>=0.24.1",
    "rich>=14.0",
    "pydantic>=2.12",
]

[project.scripts]
glma = "glma.cli:app"

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov",
    "ruff",
]
```

**Install:** `uv add real_ladybug tree-sitter tree-sitter-c tree-sitter-python typer rich pydantic`

---

## RESEARCH COMPLETE

Phase 1 is well-bounded. The main technical components are:
1. **Ladybug** for storage (direct Kuzu migration, confirmed cp313 support)
2. **Tree-sitter 0.25** for parsing (updated API from hackathon's 0.24)
3. **Typer + Rich** for CLI and progress display
4. **BLAKE2b** for content hashing
5. **Streaming pipeline** for memory efficiency

No blocking unknowns. Ready for planning.
