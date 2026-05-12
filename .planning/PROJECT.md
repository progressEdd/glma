# glma

## What This Is

A CLI tool that indexes codebases into a lightweight graph database and generates companion markdown documentation. AI agents (pi, Cursor, VS Code) query it to get compacted, relevant code context instead of grepping raw files. Designed to work both as a live index that stays in sync with code changes and as static markdown for air-gapped environments with no runtime dependencies.

## Core Value

Agents can call a single command and get exactly the code context they need to implement features — no grepping, no raw file parsing, no guesswork.

## Requirements

### Validated (v1.0)

- ✓ Tree-sitter chunking of C and Python source files (Phase 1)
- ✓ Loading parsed chunks into Ladybug graph database with Chunk/File/CONTAINS schema (Phase 1)
- ✓ File extension detection and classification (Phase 1)
- ✓ CLI entry point with `glma index`, `glma query`, `glma watch`, `glma export` commands (Phases 1-4)
- ✓ Configuration from `.glma.toml` with CLI overrides (Phase 1)
- ✓ Directory walking with exclusion filtering (.git, venvs, node_modules, hidden files) (Phase 1)
- ✓ Comment attachment via AST post-processing (docstrings + proximity heuristic) (Phase 1)
- ✓ Per-file markdown output in layered summary format (Phase 1)
- ✓ Content hashing for incremental re-indexing (BLAKE2b) (Phase 1)
- ✓ Progress display during indexing (Rich progress bar) (Phase 1)
- ✓ Relationship extraction: calls, imports, inheritance, includes (Phase 2)
- ✓ Import alias resolution and self.method() resolution (Phase 2)
- ✓ Cross-file relationship resolution with 3-pass pipeline (Phase 2)
- ✓ Confidence tagging (DIRECT vs INFERRED) for all relationships (Phase 2)
- ✓ CLI query tool with layered markdown: summary → signatures → full code (Phase 3)
- ✓ Jupyter notebook compaction with per-statement variable tracking (Phase 3)
- ✓ Cross-cell variable flow table (Phase 3)
- ✓ BFS relationship traversal with configurable depth (Phase 3)
- ✓ JSON output format for programmatic consumption (Phase 3)
- ✓ File watching with watchfiles, incremental re-indexing (Phase 4)
- ✓ Air-gapped markdown export (directory, tar.gz, stdout) (Phase 4)
- ✓ Rule-based file summaries (deterministic, no LLM) (Phase 4)
- ✓ Optional AI summaries via OpenAI-compatible local model (Phase 4)
- ✓ 211 tests, all passing (Phase 1-4)

## Current Milestone: v1.4 Hardening & Expansion

**Goal:** Fix reliability gaps, add LLM-powered search rewriting, extend language support, and unify graph + semantic + keyword into a 3-way hybrid.

**Target features:**
- Pipeline resume/checkpoint (don't lose work on interrupt)
- C duplicate chunk ID fix (support large C codebases like Linux kernel)
- Summarization progress display (visible feedback during long runs)
- Per-file markdown regeneration (don't batch at end)
- LLM query rewriting mode — rephrase user input to be codebase-relevant before search
- Extended language support — C++, TypeScript, Rust via tree-sitter grammars
- 3-way hybrid search — graph relationships + keyword + vector

**Key context:**
- Tree-sitter has built-in grammars for C++, TypeScript, Rust — mostly wiring, not new parsing
- LLM rewriting uses existing summarizer model/provider infrastructure
- 3-way hybrid builds on v1.3's keyword+vector foundation
- C duplicate chunk IDs need chunk ID format change (add content hash or byte offset)
- MCP server explicitly deferred to future milestone

### Active (v1.4)

- Pipeline reliability fixes (resume, chunk IDs, progress, per-file markdown)
- LLM query rewriting for semantic search
- Extended language support (C++, TypeScript, Rust)
- 3-way hybrid search (graph + keyword + vector)

### Validated (v1.3)

- ✓ EMB-01 through EMB-07: Embedding infrastructure — protocol, providers, presets, config (Phase 13)
- ✓ VEC-01 through VEC-05: Vector storage and `glma embed` command (Phase 14)
- ✓ SRCH-01 through SRCH-06: Hybrid search and query integration (Phase 15)

### Validated (v1.2)

- ✓ Chunk truncation before summarization (Phase 10)
- ✓ Markdown key-value export format as default (Phase 11)
- ✓ Multi-format export support — markdown-kv, markdown, json, yaml (Phase 11)
- ✓ Pi agent integration — /glma-summarize command, glma_summarize tool, model_hint resolution (Phase 12)
- ✓ Named provider presets — --summarize-provider ollama/lmstudio/llamacpp/vllm/aphrodite + custom providers via .glma.toml (Phase 12)

### Completed (v1.1)

- [x] Export defaults to summaries-only (include_code defaults False)
- [x] Notebook cell source truncation fix (list comprehensions preserved)
- [x] Stale Phase 3 placeholder removal from writer.py
- [x] Per-chunk AI summaries (generate, persist to DB, flow into export/query/markdown)
- [x] Pluggable model providers for summarization (local OpenAI-compatible + pi provider)
- [x] Architecture summary file (ARCHITECTURE.md in export)
- [x] Notebook cell AI summarization with caching

### Deferred

- [ ] MCP server interface for direct agent integration

### Out of Scope

- MCP server implementation — CLI-first for now, MCP could be a future layer
- Web UI or dashboard — agents and humans consume markdown, no visual interface needed
- Proprietary codebase handling — focused on open/accessible repos initially
- Real-time collaboration — single-user tool, no multi-user sync
- Cloud embedding providers — air-gapped philosophy, local models only
- Reranking stage — YAGNI for v1.3, hybrid scoring should suffice
- MCP server implementation — deferred to future milestone beyond v1.4

## Context

**Origin:** Built during a hackathon to analyze the Linux kernel codebase (~35K C files, ~27K H files). The hackathon proved that tree-sitter chunking and database loading work, but relationship extraction between chunks was the unsolved wall — what calls what, what imports what, how functions relate.

**Existing infrastructure:** Multi-worktree git repo with exploratory Jupyter notebooks in `02-worktrees/linux_kernel/`. Uses tree-sitter for parsing, Kuzu for graph storage, and Azure OpenAI/NVIDIA NIMs for LLM summarization. The AG2 framework is available as a reference for multi-agent patterns.

**Key insight from hackathon:** Single-line comments don't merge with their associated code chunks in tree-sitter (separate AST nodes). Language detection was manual (default was Python instead of C). Both need to be solved for a generalized tool.

**Target users:** Developers using AI coding agents (pi, Cursor, VS Code) who want agents to understand large codebases without blind-grepping. Also useful for teams in restricted environments where agents can't install runtimes.

## Constraints

- **Languages (v1):** C and Python only — tree-sitter grammars already proven
- **Graph DB:** Ladybug (ex-Kuzu, package: `real_ladybug`) — embedded graph DB with native vector indices + full-text search, replaces prior LanceDB evaluation
- **Air-gapped compatibility:** All agent-facing output must be consumable as plain text/markdown with only shell tools
- **No runtime dependency for consumers:** Agents that query the tool shouldn't need Python installed (markdown output must be self-sufficient)

## Key Decisions

| Decision | Rationale | Outcome |
| --- | --- | --- |
| CLI-first, not MCP server | Matches pi-gsd-tools pattern, works with any agent that can run shell commands | ✓ Good (Phase 1: `glma index` works) |
| Ladybug (real_ladybug) for storage | Embedded graph DB with native vector indices + full-text search + Cypher queries; ex-Kuzu so hackathon code directly reusable | ✓ Good (Phase 1: LadybugStore working) |
| Markdown as first-class output | Required for air-gapped environments; also human-browsable and directly consumable by any LLM | ✓ Good (Phase 1: layered markdown output) |
| Tree-sitter for parsing | Already proven in hackathon, supports 40+ languages, incremental parsing available | ✓ Good (Phase 1: C + Python parsing working) |
| Unresolved targets as self-referential edges | Preserves relationship data even when target chunk isn't indexed; display code handles detection | ✓ Works (Phase 2) |
| 3-pass pipeline: chunks → relationships → cross-file | Cross-file resolution needs all chunks in DB first; 3 passes ensure correct ordering | ✓ Works (Phase 2) |
| Import map uses first component for bare imports | `import os.path` → local_name="os" matches how Python actually uses it | ✓ Works (Phase 2) |
| Query output from DB, not markdown slices | Fresh query output is more compact and relevant than slicing full per-file markdown; decouples query format from storage format | ✓ Good (Phase 3: query formatter working) |
| Per-statement variable tracking for notebooks | Per-cell is too coarse; per-statement gives agents precise data flow understanding | ✓ Good (Phase 3: variable tracking working) |
| Notebooks bypass LadybugStore | .ipynb files are self-contained; no need to index into graph DB for compaction | ✓ Good (Phase 3: direct nbformat parsing) |
| watchfiles for async file watching | awatch provides OS-level event batching, rename detection via basename heuristic | ✓ Good (Phase 4: watch_and_index working) |
| Rule-based summaries for export | Deterministic file summaries from chunk + relationship data, no LLM needed | ✓ Good (Phase 4: generate_rule_summary) |
| Three export output modes | Directory, tar.gz, stdout — covers all consumption scenarios | ✓ Good (Phase 4: export_index) |
| Incremental pipeline params | changed_files/deleted_paths enable targeted re-indexing without full walk | ✓ Good (Phase 4: run_index extension) |
| Start with C and Python | Both grammars tested, both relevant to the Linux kernel use case and general codebase analysis | ✓ Good (Phase 1: both working) |
| Strategy pattern for export formats | Each format is a FormatRenderer subclass with factory dispatch; extensible without touching existing code | ✓ Good (Phase 11) |
| KV as default export format | Most token-efficient for LLM consumers; CODEBASE.md consolidates all root files | ✓ Good (Phase 11) |

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
*Last updated: 2026-05-12 after Phase 20 completion (3-Way Hybrid Search) — milestone v1.4 complete*
