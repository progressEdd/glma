# Stack Research

**Domain:** Codebase indexing CLI tool with graph database and semantic search
**Researched:** 2026-04-08
**Confidence:** MEDIUM

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Python | 3.13 | Primary language | Already established in project; excellent tree-sitter bindings, CLI tooling ecosystem |
| tree-sitter | 0.24+ | Code parsing and chunking | Already validated in hackathon; incremental parsing support; 40+ language grammars |
| LanceDB | 0.20+ | Vector storage + metadata | Serverless, embedded (no separate process), Python-native, supports both vector search AND structured metadata filtering in a single query — ideal for combining semantic search with structural relationships |
| Click or Typer | Latest | CLI framework | Click is battle-tested; Typer provides Click with modern type-hint ergonomics. Either gives clean subcommand structure (`glma index`, `glma query`, `glma watch`) |
| watchfiles | Latest | File watching | Rust-based, fast, cross-platform file change detection. Used by uvicorn and other Python tools for reliable watching |

### Database Decision: LanceDB over Ladybug

**Recommendation:** LanceDB

**Why LanceDB over Ladybug (Kuzu successor):**

| Criterion | LanceDB | Ladybug (ex-Kuzu) |
|-----------|---------|-------------------|
| Query model | Vector similarity + metadata filtering (hybrid) | Graph traversal (Cypher-like) |
| Embeddings | Built-in, manages embedding tables natively | Not supported natively |
| Schema flexibility | Semi-structured, add columns freely | Strict graph schema required |
| Zero-config | Yes — embedded, no server, single directory | Requires schema definition, DDL statements |
| Semantic search | First-class — this IS what it does | Not supported; would need separate vector store |
| Structural relationships | Via metadata tables + joins | Native graph edges |
| Python ergonomics | Excellent (PyArrow-based, pandas-like API) | Good but graph query overhead |

**The critical insight:** This tool needs BOTH structural relationships (what calls what) AND semantic search (find code by meaning). LanceDB handles semantic search natively and can represent structural relationships through metadata tables with foreign-key-like joins. A pure graph DB would need a separate vector store bolted on. LanceDB unifies both needs.

**How structural relationships work in LanceDB:**
- Each code chunk is a row with: `id`, `file_path`, `chunk_type` (function/class/module), `name`, `content`, `embedding`, `metadata` (JSON)
- Relationships stored in a separate `relationships` table: `source_id`, `target_id`, `rel_type` (calls, imports, contains, inherits)
- Query: "get function X" → get chunk → join relationships → get all callers/callees
- This isn't as elegant as graph traversal but covers the 80% case and avoids running two databases

### Supporting Libraries

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| tree-sitter-c | 0.24+ | C language grammar | Parsing C source files |
| tree-sitter-python | 0.23+ | Python language grammar | Parsing Python source files |
| sentence-transformers | Latest | Local embedding generation | Creating vector representations of code chunks for semantic search |
| nbformat | Latest | Jupyter notebook parsing | `.ipynb` compaction (read notebook JSON, extract cells, variables, references) |
| pygments | Latest | Syntax highlighting | Generating highlighted code in markdown output |
| rich | Latest | CLI output formatting | Progress bars, tables, colored output |
| pydantic | Latest | Data models | Typed schemas for chunks, relationships, index metadata |

### Embedding Strategy

| Approach | Pros | Cons | Recommendation |
|----------|------|------|----------------|
| Local embeddings (sentence-transformers) | No API cost, offline capable, air-gapped compatible | Lower quality than OpenAI embeddings | ✓ Recommended — aligns with air-gapped requirement |
| OpenAI embeddings | Higher quality | Requires API, not air-gapped compatible | Optional fallback |
| Code-specific models (CodeBERT, UniXcoder) | Better code understanding | Larger models, slower | Future optimization |

**Recommended model:** `all-MiniLM-L6-v2` (small, fast, good quality) or `jina-embeddings-v2-base-code` (code-optimized, slightly larger).

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Database | LanceDB | Ladybug/Kuzu | Needs separate vector store for semantic search; schema overhead for exploratory indexing |
| Database | LanceDB | SQLite + sqlite-vec | More manual work; LanceDB handles embeddings natively |
| Database | LanceDB | ChromaDB | ChromaDB requires a server process; LanceDB is truly embedded |
| CLI | Typer | Click | Click more verbose but more mature; Typer is fine either way |
| Parsing | tree-sitter | AST (per-language) | Tree-sitter is language-agnostic; per-language ASTs would mean N parsers |
| Parsing | tree-sitter | LSP (Language Server Protocol) | LSP requires running a language server per language; heavyweight for a CLI tool |
| Watching | watchfiles | watchdog | watchfiles is Rust-based and faster; watchdog has more edge cases |

## Installation

```bash
# Core
pip install tree-sitter tree-sitter-c tree-sitter-python lancedb
pip install click  # or typer
pip install sentence-transformers  # for embeddings

# Supporting
pip install nbformat pygments rich pydantic watchfiles

# Dev
pip install pytest pytest-cov ruff
```

## Sources

- LanceDB documentation and GitHub (lancedb/lancedb)
- tree-sitter documentation (tree-sitter.github.io)
- Existing project experience (hackathon validation)
- Confidence: MEDIUM — versions based on current knowledge, verify with pip/PyPI before pinning
