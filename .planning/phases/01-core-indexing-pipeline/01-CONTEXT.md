# Phase 1: Core Indexing Pipeline - Context

**Gathered:** 2026-04-08
**Status:** Ready for planning

<domain>
## Phase Boundary

User can point `glma index` at any repo and get a fully parsed index of all C and Python files, stored in LanceDB with companion markdown files. Re-running only re-processes changed files. Progress is visible during indexing. Binary files, .git, venvs, and node_modules are automatically skipped.

This phase delivers: CLI entry point, directory walking, language detection, tree-sitter parsing, chunk extraction with comment attachment, LanceDB storage, markdown output, content hashing for incremental re-indexing, and progress display.

</domain>

<decisions>
## Implementation Decisions

### Project Scaffolding
- **D-01:** `glma` package lives in a new worktree at `02-worktrees/glma/`, on branch `glma`, forked from the `00-experiments` template branch
- **D-02:** Follows existing worktree pattern — own `pyproject.toml`, `.venv/`, isolated from other experiments
- **D-03:** Existing worktrees (linux_kernel, notebook-compression) remain as reference material, untouched

### Chunk Extraction
- **D-04:** Nested chunks with parent references — functions, classes, AND methods inside classes all become separate chunks
- **D-05:** Each chunk stores a `parent_id` linking back to its containing chunk (e.g., method → class)
- **D-06:** Chunk types include: function, class, method, module-level code
- **D-07:** Chunk schema should include a `summary` text field (empty in Phase 1) for Phase 3 semantic search use — LLM-summarized intent will be embedded for hybrid search

### Markdown Output
- **D-08:** Per-file markdown uses layered summary format with markdown headings for organization
- **D-09:** Structure: `# filename` (heading) → file summary paragraph → `## Key Exports` (table: name, type, description) → `## Chunks` → `### chunk_name (type, Lstart-Lend)` (heading per chunk with content)
- **D-10:** Heading-based organization enables Phase 3 query tool to slice layers (summary only, signatures only, full detail)

### CLI Behavior
- **D-11:** `glma index /path/to/repo` (positional path) or `glma index` (defaults to current directory)
- **D-12:** Progress always shown by default; `--quiet` flag to silence output
- **D-13:** Config via `.glma.toml` file in the target repo, with CLI flag overrides (flags take precedence over config)
- **D-14:** Config options should include: include/exclude patterns, languages, output directory

### Progress Display
- **D-15:** Rich progress bar showing files processed count, elapsed time, and estimated time remaining
- **D-16:** Uses `rich` or `tqdm` library for terminal UI

### Agent's Discretion
- Exact `rich` vs `tqdm` choice (whichever integrates better with the CLI framework)
- Specific `.glma.toml` config key names and structure
- Ladybug (graph) schema details — node/edge table definitions, Cypher query patterns
- Error message wording and formatting
- Exact comment attachment heuristic details (AST post-processing pass)

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project-level context
- `.planning/codebase/ARCHITECTURE.md` - Repository architecture, worktree pattern, data flow patterns
- `.planning/codebase/STRUCTURE.md` - Directory layout, where to add new code, naming conventions
- `.planning/codebase/CONVENTIONS.md` - Code style, naming patterns, environment configuration
- `.planning/codebase/STACK.md` - Technology stack, key dependencies (tree-sitter, Python 3.13, uv)

### Reference implementation
- `02-worktrees/linux_kernel/develop.ipynb` - Working tree-sitter parsing pipeline, chunk extraction patterns, Kuzu graph DB usage (directly reusable — Ladybug is Kuzu's successor)
- `02-worktrees/linux_kernel/pyproject.toml` - Existing dependency versions for tree-sitter, tree-sitter-c, tree-sitter-python

### Requirements
- `.planning/REQUIREMENTS.md` - Full requirements list; Phase 1 covers: IDXC-01 through IDXC-10, STOR-01, STOR-03, STOR-05, CLIF-01
- `.planning/ROADMAP.md` §Phase 1 - Success criteria, plan breakdown (01-01 through 01-04)

### Storage decision
- `.planning/research/STACK.md` - Prior research comparing databases (NOTE: Ladybug vector index capability was missed in original research — Ladybug now has native vector indices + full-text search + graph traversal in one embedded DB)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **tree-sitter pipeline** (`02-worktrees/linux_kernel/develop.ipynb`): Working tree-sitter parsing for C files with chunk extraction. Patterns for tree-sitter Language setup, query definitions, and node traversal are directly reusable.
- **tree-sitter dependencies**: `pyproject.toml` already specifies tree-sitter 0.24.0, tree-sitter-c 0.24.1, tree-sitter-python 0.23.6 — proven compatible versions.
- **Environment configuration**: python-dotenv + pathlib pattern for path resolution across worktrees.
- **Directory tree walking**: `get_directory_tree()` function in develop.ipynb provides reference for recursive directory traversal with depth limiting.

### Established Patterns
- **Worktree-based development**: Each experiment lives in `02-worktrees/<branch>/` with its own `pyproject.toml` and `.venv/`. The `glma` worktree follows this pattern.
- **uv for package management**: All worktrees use `uv` (not pip). Dependencies via `pyproject.toml` + `uv.lock`.
- **Numbered directory prefixes**: `00-` for foundational, `01-` for onboarding, `02-` for active development.

### Integration Points
- **Fork point**: New worktree forks from `00-experiments` branch, which provides template `pyproject.toml` and `sandbox.ipynb`
- **Reference data**: Linux kernel source at `00-supporting-files/data/linux-kernel/` available for testing large-repo indexing
- **Shared config**: `.env` at `00-supporting-files/data/` for any LLM API keys (not needed in Phase 1, but available)

### Key Continuity from Hackathon
- **Storage**: Ladybug (ex-Kuzu, package: `real_ladybug`) — graph relationships, vector indices, and full-text search in one embedded DB. Prior research missed that Ladybug added native vector indices. The original LanceDB rationale ("unifies everything in one DB") actually applies better to Ladybug now. Hackathon Kuzu patterns are directly reusable.
- **Package manager**: `uv` for all dependency management (not pip). `uv add real_ladybug` etc.

</code_context>

<specifics>
## Specific Ideas

- Chunk schema must include a `summary` field (text, nullable) for Phase 3 semantic search — LLM will summarize user intent, embed it, and do hybrid (semantic + keyword) search against embedded chunk summaries
- Markdown heading structure should be designed to support Phase 3's layered query output (summary → signatures → details → full code) so the static markdown and query output share a consistent format

</specifics>

<deferred>
## Deferred Ideas

- **Semantic search with LLM-summarized intent + hybrid search** — Phase 3 (Query Tool). Phase 1 just needs to ensure schema supports it via `summary` field on chunks.
- **Notebook parsing (.ipynb)** — Phase 3 (Jupyter Compaction). How notebooks are handled as input files is a separate discussion.
- **File watching / incremental updates** — Phase 4. Phase 1 does content hashing for change detection only.

</deferred>

---

*Phase: 01-core-indexing-pipeline*
*Context gathered: 2026-04-08*
