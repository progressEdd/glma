# glma

## What This Is

A CLI tool that indexes codebases into a lightweight graph database and generates companion markdown documentation. AI agents (pi, Cursor, VS Code) query it to get compacted, relevant code context instead of grepping raw files. Designed to work both as a live index that stays in sync with code changes and as static markdown for air-gapped environments with no runtime dependencies.

## Core Value

Agents can call a single command and get exactly the code context they need to implement features — no grepping, no raw file parsing, no guesswork.

## Requirements

### Validated

<!-- Shipped and confirmed valuable from hackathon work. -->

- ✓ Tree-sitter chunking of C source files - existing (hackathon: `develop.ipynb`)
- ✓ Tree-sitter chunking of Python source files - existing (grammar installed, tested)
- ✓ Loading parsed chunks into a graph database - existing (Kuzu)
- ✓ LLM summarization of code chunks - existing (Azure OpenAI, NVIDIA NIMs, local Ollama)
- ✓ File extension detection and classification - existing (pandas analysis)
- ✓ Jupyter notebook-based analysis pipeline - existing (88-cell notebook)
- ✓ Environment configuration for multiple LLM providers - existing (python-dotenv)

### Active

<!-- Current scope. Building toward these. -->

- [ ] Generalized indexer: point at any repo, parse all supported languages, store in graph DB
- [ ] Relationship extraction between code chunks (function calls, imports, class hierarchies, variable references)
- [ ] Semantic search layer on top of graph relationships
- [ ] CLI query tool: agents call `get_context <filepath>` and get compacted relevant chunks as markdown
- [ ] Jupyter notebook compaction: flatten `.ipynb` into readable markdown (cell index, code, variables, references)
- [ ] Markdown as first-class output: human-browsable, agent-readable repo documentation
- [ ] File watcher: detect codebase changes, incrementally update DB and markdown
- [ ] Air-gapped mode: markdown IS the database — shell-only agents can work from it with no Python/JS runtime
- [ ] Extensible language support (starting with C and Python, designed for any tree-sitter grammar)

### Out of Scope

- MCP server implementation — CLI-first for now, MCP could be a future layer
- Web UI or dashboard — agents and humans consume markdown, no visual interface needed
- Proprietary codebase handling — focused on open/accessible repos initially
- Real-time collaboration — single-user tool, no multi-user sync

## Context

**Origin:** Built during a hackathon to analyze the Linux kernel codebase (~35K C files, ~27K H files). The hackathon proved that tree-sitter chunking and database loading work, but relationship extraction between chunks was the unsolved wall — what calls what, what imports what, how functions relate.

**Existing infrastructure:** Multi-worktree git repo with exploratory Jupyter notebooks in `02-worktrees/linux_kernel/`. Uses tree-sitter for parsing, Kuzu for graph storage, and Azure OpenAI/NVIDIA NIMs for LLM summarization. The AG2 framework is available as a reference for multi-agent patterns.

**Key insight from hackathon:** Single-line comments don't merge with their associated code chunks in tree-sitter (separate AST nodes). Language detection was manual (default was Python instead of C). Both need to be solved for a generalized tool.

**Target users:** Developers using AI coding agents (pi, Cursor, VS Code) who want agents to understand large codebases without blind-grepping. Also useful for teams in restricted environments where agents can't install runtimes.

## Constraints

- **Languages (v1):** C and Python only — tree-sitter grammars already proven
- **Graph DB:** Evaluating Ladybug (graph DB) vs LanceDB (vector store) — need structural relationships + semantic search
- **Air-gapped compatibility:** All agent-facing output must be consumable as plain text/markdown with only shell tools
- **No runtime dependency for consumers:** Agents that query the tool shouldn't need Python installed (markdown output must be self-sufficient)

## Key Decisions

| Decision | Rationale | Outcome |
| --- | --- | --- |
| CLI-first, not MCP server | Matches pi-gsd-tools pattern, works with any agent that can run shell commands | - Pending |
| Graph DB for relationships, semantic search layered on top | Structural relationships (calls, imports) are the core value; semantic search is an enhancement | - Pending |
| Markdown as first-class output | Required for air-gapped environments; also human-browsable and directly consumable by any LLM | - Pending |
| Tree-sitter for parsing | Already proven in hackathon, supports 40+ languages, incremental parsing available | ✓ Good (hackathon validated) |
| Incremental updates via file watcher | Large repos can't be re-indexed from scratch on every change | - Pending |
| Start with C and Python | Both grammars tested, both relevant to the Linux kernel use case and general codebase analysis | ✓ Good (hackathon validated) |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check - still the right priority?
3. Audit Out of Scope - reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-08 after initialization*
