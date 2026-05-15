# glma Index — ag2 *(beta)*

This directory contains the glma index for the `ag2` codebase. If the source
code has been updated and the index is stale, re-run indexing to refresh it.

## Setting up the glma worktree

This index relies on the `glma` branch being checked out as a worktree. If you
don't have it yet, from the **project root**:

```bash
git worktree add 02-worktrees/glma glma
```

Then build the uv environment:

```bash
cd 02-worktrees/glma && uv sync && cd ../..
```

See `02-worktrees/README.md` for the full worktree setup guide.

## Full indexing workflow

All commands are run from the **project root** (the folder containing `02-worktrees/`).

### 1. Index the codebase

```bash
uv run 02-worktrees/glma/src/glma index 02-worktrees/ag2
```

To also regenerate AI-powered summaries (requires a running local model):

```bash
uv run 02-worktrees/glma/src/glma index 02-worktrees/ag2 --summarize
```

### 2. Generate embeddings

After indexing (and optionally summarizing), build the vector index for semantic
search. Requires a running embedding model at the endpoint configured in
`.glma.toml`:

```bash
uv run 02-worktrees/glma/src/glma embed 02-worktrees/ag2
```

Force re-embed all chunks even if unchanged:

```bash
uv run 02-worktrees/glma/src/glma embed 02-worktrees/ag2 --force
```

### 3. Search the index

Query the indexed codebase with natural language. Supports hybrid (keyword +
vector + graph), vector-only, and keyword-only modes:

```bash
# Hybrid search (default)
uv run 02-worktrees/glma/src/glma search "how does agent group chat work" -r 02-worktrees/ag2

# 3-way hybrid with graph traversal
uv run 02-worktrees/glma/src/glma search "how does agent group chat work" -r 02-worktrees/ag2 --graph

# Vector-only or keyword-only
uv run 02-worktrees/glma/src/glma search "agent group chat" -r 02-worktrees/ag2 --search-mode vector
uv run 02-worktrees/glma/src/glma search "agent group chat" -r 02-worktrees/ag2 --search-mode keyword
```

If results are too sparse, lower the similarity threshold to return more matches
(default is `0.5`; try `0.3` for broader results):

```bash
uv run 02-worktrees/glma/src/glma search "agent group chat" -r 02-worktrees/ag2 --similarity-threshold 0.3
```

## What gets updated

| Directory | Updated by | Contents |
|-----------|-----------|----------|
| `db/` | `index` | Ladybug graph database with parsed chunks and relationships |
| `markdown/` | `index` | Per-file companion markdown documentation |
| `db/` (vectors) | `embed` | Embedding vectors for semantic search |

## Configuration

Index settings live in `.glma.toml` in this directory (languages, summarizer
model, embedding provider, etc.). Edit that file to change behavior.
