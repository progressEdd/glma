# Architecture

**Analysis Date:** 2026-04-08

## Pattern Overview

**Overall:** Multi-worktree Exploratory Repository (research/prototype phase)

**Key Characteristics:**
- Git worktrees for parallel experiment branches
- Jupyter notebook-driven development (exploratory, not production)
- Git submodules for large reference codebases (Linux kernel, ag2 framework)
- Foam-based knowledge management (daily dev logs)
- No formal application architecture yet - pre-product stage

## Layers

**Repository Root (meta-layer):**
- Purpose: Orchestrate experiments, manage shared data, track dev logs
- Contains: `.gitmodules`, `.gitignore`, `README.md`, `00-dev-log/`, `00-supporting-files/`
- Depends on: Git worktree system
- Used by: All worktrees share the same git history and supporting files

**Supporting Files Layer:**
- Purpose: Store reference data used by experiments
- Contains: Linux kernel source (submodule), ag2 framework (submodule), sample configs, graph visualizations
- Location: `00-supporting-files/data/`
- Key subdirectories:
  - `linux-kernel/` - Full Linux kernel source (submodule from torvalds/linux)
  - `ag2-framework/` - AG2 agent framework (submodule from ag2ai/ag2)
  - `graphs/` - Generated visualizations (SVG, PDF, HTML)

**Worktree Layer (experiment branches):**
- Purpose: Isolated development environments for specific experiments
- Contains: Independent `pyproject.toml`, notebooks, virtual environments
- Location: `02-worktrees/<branch-name>/`
- Each worktree is a separate git branch checked out as its own directory
- Shared access to `00-supporting-files/` via relative paths (e.g., `current_dir.parents[1]`)

**Dev Log Layer:**
- Purpose: Track daily progress and decisions
- Contains: Foam-template markdown files
- Location: `00-dev-log/`
- Template: `00-dev-log/00-template.md`

## Data Flow

**Codebase Analysis Pipeline (linux_kernel worktree):**

1. Load environment config via python-dotenv (`00-supporting-files/data/.env`)
2. Navigate to Linux kernel source (`00-supporting-files/data/linux-kernel/`)
3. Use Kuzu graph database to index/query kernel structure
4. Use pandas to analyze file distributions, extension counts
5. Use tree-sitter to parse and chunk C source files
6. Send code chunks to LLM (Azure OpenAI / NVIDIA NIMs) for summarization
7. Results visualized via yfiles-jupyter-graphs or markdown tables

**State Management:**
- Kuzu database: Local graph database for codebase structure (stored in `kuzu_db/`, gitignored)
- File-based: Notebooks serve as both code and documentation
- No persistent state beyond notebooks and generated outputs

## Key Abstractions

**Worktree as Experiment:**
- Purpose: Each git worktree represents an isolated experiment or feature branch
- Examples: `02-worktrees/linux_kernel/` (kernel analysis), `02-worktrees/00-experiments/` (base template)
- Pattern: Branch-based isolation with shared repository root

**Notebook as Workflow:**
- Purpose: Jupyter notebooks define multi-step analysis workflows
- Examples: `02-worktrees/linux_kernel/develop.ipynb` (main analysis notebook)
- Pattern: Linear cell execution with markdown documentation

**Directory Tree Navigation:**
- Purpose: Custom tree-printing utility for visualizing codebase structure
- Examples: `get_directory_tree()` function in `develop.ipynb`
- Pattern: Recursive traversal with depth limiting and file type summarization

## Entry Points

**Notebook Execution:**
- Location: `02-worktrees/linux_kernel/develop.ipynb`
- Triggers: Manual Jupyter notebook execution
- Responsibilities: Initialize paths, load data, run analysis pipeline

**Git Worktree Branches:**
- `00-experiments` - Base template branch for new experiments
- `linux_kernel` - Active Linux kernel analysis experiment
- `notebook-compression` - Experiment (template, not yet customized)
- `master` - Main branch with repository structure and documentation

## Error Handling

**Strategy:** Ad hoc in notebooks (exploratory phase, no formal error handling)

**Patterns:**
- Print-based debugging in notebook cells
- Try-except around specific operations (e.g., tree-sitter language detection)
- Manual verification of results via visual inspection

## Cross-Cutting Concerns

**Environment Configuration:**
- python-dotenv loads `.env` from supporting files
- Multiple LLM providers supported (Azure OpenAI, NVIDIA NIMs)
- Path resolution via `pathlib.Path` with relative navigation from notebook location

**Code Parsing:**
- tree-sitter for multi-language code parsing
- Language detection needs manual configuration (bug discovered: default was Python instead of C)
- Comment merging with code chunks still unresolved

**Knowledge Management:**
- Foam templates for daily dev logs
- `.foam/templates/` contains daily-note and new-template patterns

---

*Architecture analysis: 2026-04-08*
*Update when major patterns change*
