# Architecture Research

**Domain:** Codebase indexing CLI tool with graph database and semantic search
**Researched:** 2026-04-08
**Confidence:** MEDIUM

## Recommended Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        CLI Layer                             │
│  glma index │ glma query │ glma watch │ glma export          │
├─────────────────────────────────────────────────────────────┤
│                      Pipeline Layer                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │ Language  │  │  Chunker │  │Relation  │  │ Embedder │     │
│  │ Detector  │  │          │  │Extractor │  │          │     │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘     │
│       │             │             │              │           │
├───────┴─────────────┴─────────────┴──────────────┴───────────┤
│                      Storage Layer                            │
│  ┌──────────────────┐  ┌────────────────────────────────┐    │
│  │   LanceDB        │  │   Markdown Files               │    │
│  │   ┌───────────┐  │  │   .glma-index/                 │    │
│  │   │ chunks    │  │  │     files/<path>.md            │    │
│  │   │ relations │  │  │     relationships/<path>.md    │    │
│  │   │ metadata  │  │  │     summary.md                 │    │
│  │   └───────────┘  │  │                                │    │
│  └──────────────────┘  └────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                    Output Layer                               │
│  Markdown (query results) │ JSON (machine) │ Summary         │
└─────────────────────────────────────────────────────────────┘
```

### Component Boundaries

| Component | Responsibility | Communicates With |
|-----------|---------------|-------------------|
| **CLI** | Parse commands, route to pipeline, format output | Pipeline Layer |
| **Language Detector** | Map file extensions to tree-sitter grammars | Chunker (provides grammar) |
| **Chunker** | Parse files with tree-sitter, extract semantic chunks (functions, classes, methods) | Language Detector, Relation Extractor, Storage |
| **Relation Extractor** | Walk AST to find calls, imports, inheritance, variable references between chunks | Chunker (needs AST), Storage |
| **Embedder** | Generate vector embeddings for chunks using sentence-transformers | Chunker (provides content), Storage |
| **Storage** | Persist chunks, relationships, embeddings to LanceDB + markdown | All pipeline components |
| **Query Engine** | Look up chunks by file path, follow relationships, rank results | Storage |
| **File Watcher** | Detect filesystem changes, trigger incremental re-index | Pipeline (re-runs changed files) |
| **Exporter** | Generate full markdown export for air-gapped use | Storage |

### Data Flow

**Indexing Pipeline:**

```
Repo Path
    │
    ▼
Walk directory (skip .git, node_modules, venvs)
    │
    ▼
For each file:
    Language Detector → what grammar?
    │
    ▼
    Chunker → parse with tree-sitter → extract chunks
    │   (function definitions, class definitions, module-level code)
    │
    ▼
    Relation Extractor → walk AST → find:
    │   - function calls (who calls whom)
    │   - imports (what depends on what)
    │   - class inheritance (extends/implements)
    │   - variable assignments (scope tracking)
    │
    ▼
    Embedder → generate vector for each chunk (optional, async)
    │
    ▼
    Storage → write to LanceDB + generate markdown
```

**Query Pipeline:**

```
glma query <filepath>
    │
    ▼
Look up file in LanceDB (all chunks for this path)
    │
    ▼
Follow relationships (what calls functions in this file?)
    │
    ▼
Format as markdown:
    - File summary
    - Functions/classes with their code
    - Incoming dependencies (who uses this)
    - Outgoing dependencies (what this uses)
    - Variables and references
    │
    ▼
Output to stdout (agent captures this)
```

## Patterns to Follow

### Pattern 1: Language Plugin Architecture
**What:** Each language is a plugin that provides grammar + relationship extraction rules
**When:** Adding new language support
**Example:**
```python
class LanguagePlugin(ABC):
    @abstractmethod
    def get_grammar(self) -> Language: ...
    
    @abstractmethod
    def extract_chunks(self, tree: Tree) -> list[Chunk]: ...
    
    @abstractmethod
    def extract_relations(self, tree: Tree, chunks: list[Chunk]) -> list[Relation]: ...

class CPlugin(LanguagePlugin): ...
class PythonPlugin(LanguagePlugin): ...
```

### Pattern 2: Dual Output (DB + Markdown)
**What:** Every piece of indexed data is written to both LanceDB and markdown simultaneously
**When:** After chunking and relationship extraction
**Why:** Markdown is the air-gapped fallback; DB is the queryable index. Writing both ensures they stay in sync.

### Pattern 3: Incremental Indexing via Content Hash
**What:** Track file content hashes; only re-process files whose hash changed
**When:** Re-indexing after file changes
**Why:** Full re-index of large repos is expensive; content hashing is cheap
```python
def should_reindex(file_path, stored_hash):
    current_hash = sha256(file_path.read_bytes())
    return current_hash != stored_hash
```

### Pattern 4: Notebook Compaction as Special Parser
**What:** Jupyter notebooks get their own parser (not tree-sitter) that extracts cells, variables, references
**When:** Processing `.ipynb` files
**Why:** Notebooks aren't regular code — they're JSON containers with code cells, markdown cells, outputs, and kernel metadata

## Anti-Patterns to Avoid

### Anti-Pattern 1: Monolithic Notebook
**What:** Putting all logic in a single Jupyter notebook
**Why bad:** Can't test, can't reuse, can't version properly (JSON diffs)
**Instead:** Extract into Python modules; use notebooks only for interactive exploration

### Anti-Pattern 2: One Big Index
**What:** Single database for all repos
**Why bad:** Cross-contamination, no isolation, can't clean up per-repo
**Instead:** One LanceDB instance per repo (stored in `.glma-index/` inside the repo)

### Anti-Pattern 3: Greedy Relationship Resolution
**What:** Trying to resolve all cross-file relationships in a single pass
**Why bad:** O(n²) complexity, fails on large repos, can't handle incremental updates
**Instead:** Per-file extraction, then global relationship resolution as a separate pass

### Anti-Pattern 4: Requiring Network for Core Functionality
**What:** Requiring API calls (LLM, embeddings) for basic indexing
**Why bad:** Violates air-gapped requirement
**Instead:** Core indexing (parse + chunk + relationships) works offline. Embeddings and LLM summaries are optional enhancements.

## Scalability Considerations

| Concern | Small repo (<1K files) | Medium (1K-10K) | Large (10K+ like Linux kernel) |
|---------|------------------------|------------------|--------------------------------|
| Indexing time | Seconds | Minutes | Tens of minutes |
| Storage | MBs | 100s MBs | GBs (especially with embeddings) |
| Query speed | Instant | <100ms | <500ms with proper indexing |
| Incremental update | Re-index all (fast enough) | Hash-based diff | Hash-based diff + parallel processing |

## Sources

- Existing hackathon architecture (Kuzu-based, notebook-driven)
- tree-sitter documentation (AST structure, query language)
- LanceDB documentation (schema design, vector + metadata queries)
- Code intelligence tools (Sourcegraph, Aider) for architecture patterns
- Confidence: MEDIUM — architecture is informed by domain knowledge, not production experience with LanceDB at scale
