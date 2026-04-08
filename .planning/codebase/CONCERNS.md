# Codebase Concerns

**Analysis Date:** 2026-04-08

## Tech Debt

**All logic in Jupyter notebooks:**
- Issue: All analysis code lives in notebook cells with no module extraction
- Files: `02-worktrees/linux_kernel/develop.ipynb` (all code in one large notebook)
- Why: Hackathon-style exploratory development
- Impact: Can't reuse code between worktrees, can't write automated tests, code versioning is noisy (notebook JSON diffs)
- Fix approach: Extract reusable functions into Python modules (`src/` package), notebooks import and call them

**Tree-sitter language detection is manual:**
- Issue: Language for tree-sitter parsing must be specified manually; default was Python instead of C
- Files: `02-worktrees/linux_kernel/develop.ipynb` (tree-sitter configuration cells)
- Why: tree-sitter requires explicit language grammar registration
- Impact: Wrong language = wrong parse tree = wrong chunks; needs to be dynamic based on file extension
- Fix approach: Build a mapping from file extension to tree-sitter language, auto-detect from filename

**No shared code between worktrees:**
- Issue: Each worktree has its own `pyproject.toml` and virtual environment with no shared utilities
- Files: `02-worktrees/*/pyproject.toml` (each has independent dependency lists)
- Why: Worktree isolation by design, but no shared library layer
- Impact: Code duplication, dependency drift between worktrees
- Fix approach: Create a shared Python package at repository root or a common dependency worktree

## Known Bugs

**Single-line comments not merged with code chunks:**
- Symptoms: tree-sitter chunks don't include preceding single-line comments with their associated code
- Trigger: Parsing any C file with `//` style comments
- Files: Discussed in `00-dev-log/2025-07-17.md`
- Workaround: Could proceed with LLM summarization anyway, or build custom comment-merging logic
- Root cause: tree-sitter treats comments as separate AST nodes from code
- Blocks: Code summarization quality (missing context from comments)

**Path resolution assumes specific directory structure:**
- Symptoms: `supporting_files` path hardcoded using `current_dir.parents[1]`
- Trigger: Running notebook from a different location or renaming directories
- Files: `02-worktrees/linux_kernel/develop.ipynb` (cell 2)
- Workaround: The `__file__` check helps but doesn't solve the hardcoded parent navigation
- Root cause: Relative path assumption built into notebook setup
- Fix: Use environment variable or config file for repository root path

## Security Considerations

**API keys in .env files:**
- Risk: `.env` files with real API keys could accidentally be committed
- Files: `00-supporting-files/data/sample.env.file` (template with placeholder values)
- Current mitigation: `.env` is gitignored, sample file has `$INSERT_*` placeholders
- Recommendations: Verify `.env` is in all `.gitignore` files, consider using a secrets manager for shared team access

**Notebook output may contain code snippets:**
- Risk: Notebook cell outputs could contain proprietary or sensitive code snippets from the Linux kernel
- Current mitigation: Linux kernel is open source (GPLv2), so this is low risk
- Recommendations: Be cautious if analyzing proprietary codebases in the future

## Performance Bottlenecks

**Linux kernel submodule clone time:**
- Problem: Initial clone of Linux kernel submodule is extremely slow (~40GB+)
- Measurement: Can take hours on average connections
- Cause: Full git history of the Linux kernel is enormous
- Improvement path: Use shallow clone (`--depth 1`), or filter-tree for specific subsystems only

**Kuzu database rebuild:**
- Problem: Graph database needs to be rebuilt when kernel source changes
- Measurement: Unknown (not benchmarked)
- Cause: Full re-indexing of 35K+ C files
- Improvement path: Incremental indexing, or pre-built database artifacts

## Fragile Areas

**Worktree-relative paths:**
- Why fragile: Notebooks assume specific directory depth from repository root
- Common failures: Moving notebooks or renaming directories breaks all path resolution
- Files: `02-worktrees/linux_kernel/develop.ipynb` (path setup cells)
- Safe modification: Add a `PROJECT_ROOT` resolution function, use it consistently
- Test coverage: None (manual verification only)

**Git submodule state:**
- Why fragile: Submodules track specific commits, can fall out of sync
- Common failures: `git status` shows submodule modifications after updates
- Files: `.gitmodules`, submodule directories
- Safe modification: Use `git submodule update --init` after pulls, don't modify submodule contents
- Test coverage: N/A (git operations)

## Scaling Limits

**Single-machine execution:**
- Current capacity: One user, one notebook at a time
- Limit: Analysis speed bounded by single CPU core + local LLM inference
- Symptoms at limit: Long wait times for kernel-wide analysis
- Scaling path: Parallelize analysis across files, batch LLM calls, consider distributed processing

**LLM API rate limits:**
- Current capacity: Whatever Azure OpenAI tier allows
- Limit: Rate limits on completions endpoint
- Symptoms at limit: Throttling errors during batch summarization
- Scaling path: Implement rate limiting, retry logic, batch processing

## Dependencies at Risk

**yfiles-jupyter-graphs-for-kuzu (v0.0.4):**
- Risk: Very early version (0.0.4), could have breaking changes or be abandoned
- Impact: Graph visualization in notebooks breaks
- Migration plan: Fall back to yfiles-jupyter-graphs directly, or use matplotlib/plotly for graph viz

**Local Ollama dependency (implicit):**
- Risk: gemma2:9b model tested locally requires Ollama setup
- Impact: Can't reproduce local LLM experiments without Ollama installed
- Migration plan: Use cloud LLM endpoints exclusively for reproducibility

## Missing Critical Features

**No automated code chunking pipeline:**
- Problem: Tree-sitter chunking works but comment merging is unresolved
- Current workaround: Manual review of chunks, or proceeding without comments
- Blocks: Reliable code-to-documentation pipeline
- Implementation complexity: Medium (custom tree-sitter visitor for comment attachment)

**No structured output format for documentation:**
- Problem: LLM summaries are ad-hoc with no consistent schema
- Current workaround: Manual review of each summary
- Blocks: Automated documentation generation at scale
- Implementation complexity: Medium (define schema, use structured outputs)

**No progress tracking for batch operations:**
- Problem: No way to track progress when processing thousands of files
- Current workaround: Manual observation
- Blocks: Running full kernel analysis reliably
- Implementation complexity: Low (add tqdm progress bars, logging)

## Test Coverage Gaps

**All code is untested:**
- What's not tested: Everything - tree-sitter chunking, Kuzu queries, LLM pipeline, path resolution
- Risk: Any change could silently break the analysis pipeline
- Priority: Medium (exploratory phase, but growing code needs tests)
- Difficulty to test: Low for utility functions, medium for LLM integration (needs mocking)

---

*Concerns audit: 2026-04-08*
*Update as issues are fixed or new ones discovered*
