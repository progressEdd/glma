# glma

**CLI tool that indexes codebases into a queryable graph database and generates companion markdown documentation.**

AI coding agents (pi, Cursor, VS Code) call `glma query` to get compacted, relevant code context instead of grepping raw files. Works as a live index that stays in sync with code changes, or as static markdown for air-gapped environments with no runtime dependencies.

## What It Does

```
glma index .          # Parse source files → Ladybug graph DB + per-file markdown
glma query src/foo.py # Get compacted context: summary → signatures → code
glma watch .          # Live file watching with incremental re-indexing
glma export .         # Air-gapped static markdown export (directory/tar.gz/stdout)
```

**Supported languages:** C, Python

**Relationship extraction:** function calls, imports, inheritance, includes — with confidence tagging (DIRECT/INFERRED) and cross-file resolution.

**Notebook compaction:** `.ipynb` files get per-statement variable tracking and cross-cell flow tables, bypassing the graph DB entirely.

## Install

```bash
cd 02-worktrees/glma
uv sync           # create venv and install dependencies
uv add <package>  # add new deps as needed
```

### Optional: AI Summarization

```bash
uv sync --extra ai    # install openai client for local model providers
```

Per-chunk AI summaries use pluggable providers:
- **`local`** — any OpenAI-compatible API (Ollama, LM Studio, etc.)
- **`pi`** — pi coding agent as summarization backend

## Quick Start

```bash
# Index a codebase
glma index ~/my-project

# Query a file (summary mode)
glma query src/main.py

# Query with full code and relationship traversal
glma query src/main.py --verbose --depth 3

# Get JSON output for programmatic consumption
glma query src/main.py --format json

# Index with AI-generated per-chunk summaries
glma index ~/my-project --summarize --summarize-provider local --summarize-model llama3

# Compact a Jupyter notebook
glma query analysis.ipynb --include-code

# Compact a notebook with per-cell AI summaries
glma query analysis.ipynb --summarize --summarize-provider local

# Watch for changes (incremental re-indexing)
glma watch ~/my-project

# Export as static markdown (air-gapped friendly)
glma export ~/my-project -o ./export-dir/
glma export ~/my-project -o export.tar.gz
glma export ~/my-project -o -  # stdout pipe
```

## Architecture

```
Source files ──→ Tree-sitter parser ──→ Chunks + Comments
                        │
                        ▼
               Ladybug graph DB ──→ Relationships (calls, imports, inheritance)
                        │
                        ▼
               Per-file markdown + AI summaries
```

**Key modules:**

| Module | Purpose |
|---|---|
| `glma.cli` | Typer CLI with `index`, `query`, `watch`, `export` commands |
| `glma.config` | `.glma.toml` config loading with CLI overrides |
| `glma.index/` | Parsing pipeline — walker, parser, chunks, comments, relationships, resolver, writer |
| `glma.db/` | Ladybug graph store (schema: Chunk/File nodes, CONTAINS/CALLS/IMPORTS edges) |
| `glma.query/` | Query formatter, notebook compaction, variable tracking |
| `glma.summarize/` | Provider protocol + OpenAI-compatible and pi backends |
| `glma.export` | Static markdown export (directory, tar.gz, stdout) |
| `glma.watch` | Async file watching via watchfiles |

## Configuration

Create `.glma.toml` in your repo root:

```toml
[languages]
languages = ["c", "python"]

[output]
output_dir = ".glma-index"

[summarize]
enabled = false
provider = "local"       # "local" (OpenAI-compatible) or "pi"
model = "llama3"
base_url = "http://localhost:11434/v1"
```

## Testing

```bash
uv run pytest                    # run all 274 tests
uv run pytest tests/test_cli.py  # run specific test file
uv run pytest --cov=glma        # coverage report
```

## Dependencies

See `pyproject.toml`. Key dependencies:
- **real-ladybug** — embedded graph database (ex-Kuzu)
- **tree-sitter** — source code parsing (C + Python grammars)
- **typer** — CLI framework
- **rich** — terminal output / progress bars
- **watchfiles** — async file system watching
- **nbformat** — Jupyter notebook parsing
- **pydantic** — data models
- **openai** *(optional)* — AI summarization client

## Status

**Version:** 0.1.0
**Milestone:** v1.1 complete — all phases shipped (274 tests passing)
**Languages:** C, Python
**Branch:** `glma`
