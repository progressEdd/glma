# Codebase Structure

**Analysis Date:** 2026-04-08

## Directory Layout

```
glma/                                # Repository root (master branch)
├── 00-dev-log/                      # Daily development logs (Foam)
├── 00-supporting-files/             # Shared reference data
│   └── data/
│       ├── linux-kernel/           # Linux kernel source (submodule)
│       ├── ag2-framework/          # AG2 agent framework (submodule)
│       ├── graphs/                 # Generated visualizations
│       └── sample.env.file         # Environment variable template
├── 01-dev-onboarding/              # Dev onboarding submodule
├── 02-worktrees/                   # Git worktrees (parallel branches)
│   ├── 00-experiments/             # Base experiment template branch
│   ├── linux_kernel/               # Linux kernel analysis branch
│   ├── notebook-compression/       # Notebook compression experiment
│   └── README.md                   # Worktree usage documentation
├── .foam/                          # Foam note-taking templates
│   └── templates/                  # daily-note.md, new-template.md
├── .gitignore                      # Global gitignore
├── .gitmodules                     # Submodule definitions
├── LICENSE                         # Project license
└── README.md                       # Project overview
```

## Directory Purposes

**00-dev-log/**
- Purpose: Daily development logs tracking progress and decisions
- Contains: Markdown files named by date (YYYY-MM-DD.md), plus a template
- Key files:
  - `00-template.md` - Foam template for daily logs
  - `2025-07-15.md` - File extension analysis progress, tree-sitter exploration
  - `2025-07-17.md` - Tree-sitter limitations, LLM summarization tests
- Naming: Date-based (YYYY-MM-DD.md)

**00-supporting-files/**
- Purpose: Shared data and configuration used by all worktrees
- Contains: Git submodules for reference codebases, generated outputs, env config
- Key files:
  - `data/linux-kernel/` - Full Linux kernel source (~35K .c files, ~27K .h files)
  - `data/ag2-framework/` - AG2 multi-agent framework (reference for agent patterns)
  - `data/graphs/ag2_graph.html` - Interactive graph visualization
  - `data/sample.env.file` - Template for API keys (Azure OpenAI, NVIDIA NIMs)
- Subdirectories: Each data submodule is independently versioned

**01-dev-onboarding/**
- Purpose: Developer onboarding content (separate submodule repo)
- Contains: Git submodule pointing to progressEdd/dev-onboarding
- Status: Appears empty/uninitialized at this path

**02-worktrees/**
- Purpose: Parallel development branches as separate working directories
- Contains: Git worktrees, each on its own branch
- Key files:
  - `README.md` - Instructions for creating/managing worktrees
- Subdirectories: One directory per active branch

**02-worktrees/linux_kernel/**
- Purpose: Active experiment - Linux kernel codebase analysis with AI
- Contains: Jupyter notebook, Python project config
- Key files:
  - `develop.ipynb` - Main analysis notebook (tree printing, Kuzu queries, file analysis)
  - `pyproject.toml` - Python 3.13, full dependency list (tree-sitter, kuzu, openai, etc.)
  - `uv.lock` - Locked dependencies
  - `README.md` - Experiment description and status
- Virtual env: `.venv/` (gitignored)

**02-worktrees/00-experiments/**
- Purpose: Base template for creating new experiment branches
- Contains: Minimal Python project setup
- Key files:
  - `sandbox.ipynb` - Empty notebook
  - `pyproject.toml` - Minimal deps (openai, python-dotenv, ipykernel)
- Status: Template, branches fork from here

**02-worktrees/notebook-compression/**
- Purpose: Experiment branch (not yet customized from template)
- Contains: Same template structure as 00-experiments
- Key files: `sandbox.ipynb`, `pyproject.toml` (template-repo)
- Status: Inactive/template state

**.foam/**
- Purpose: VS Code Foam note-taking configuration
- Contains: Templates for daily notes and new notes
- Key files:
  - `templates/daily-note.md` - Foam template with date variables
  - `templates/new-template.md` - Generic new note template

## Key File Locations

**Entry Points:**
- `02-worktrees/linux_kernel/develop.ipynb`: Main analysis notebook
- `02-worktrees/00-experiments/sandbox.ipynb`: Generic experiment notebook

**Configuration:**
- `02-worktrees/linux_kernel/pyproject.toml`: Python project definition with all deps
- `02-worktrees/linux_kernel/.python-version`: Python 3.13 pin
- `00-supporting-files/data/sample.env.file`: API key template
- `.gitignore`: Global ignore rules (worktrees, venvs, caches, kuzu_db/)
- `.gitmodules`: Submodule definitions (3 submodules)

**Core Logic:**
- `02-worktrees/linux_kernel/develop.ipynb`: All analysis code (tree printing, data loading)

**Documentation:**
- `README.md`: Project overview, setup instructions, active experiments table
- `02-worktrees/README.md`: Worktree management guide
- `00-dev-log/`: Daily progress logs

**Reference Data:**
- `00-supporting-files/data/linux-kernel/`: ~80K source files (C, H, DTS, etc.)
- `00-supporting-files/data/ag2-framework/`: Multi-agent AI framework
- `00-supporting-files/data/graphs/`: Generated visualizations

## Naming Conventions

**Files:**
- `*.ipynb`: Jupyter notebooks (develop.ipynb, sandbox.ipynb)
- `*.md`: Markdown documentation (README.md, dev logs)
- `pyproject.toml`: Python project config (standard uv/pip convention)
- `uv.lock`: Dependency lockfile

**Directories:**
- `NN-<name>/`: Numbered prefix for ordering (00-, 01-, 02-)
- kebab-case for all directory names
- Git submodule directories match their source repo name

**Special Patterns:**
- `00-` prefix: Foundational/shared resources
- `01-` prefix: Onboarding
- `02-` prefix: Active development (worktrees)
- Date-based log files: `YYYY-MM-DD.md`

## Where to Add New Code

**New Experiment:**
```bash
git worktree add 02-worktrees/<name> -b <name> 00-experiments
```
- Creates new branch from template with `sandbox.ipynb` and `pyproject.toml`

**New Analysis Code:**
- Primary code: `02-worktrees/linux_kernel/` (or new worktree)
- Notebook cells: Add to existing `develop.ipynb` or create new notebook

**New Dependencies:**
- Run: `cd 02-worktrees/<worktree> && uv add <package>`
- Updates `pyproject.toml` and `uv.lock` in that worktree

**New Reference Data:**
- Add as git submodule: `git submodule add <url> 00-supporting-files/data/<name>`
- Update `.gitmodules` automatically

**New Dev Log:**
- Use Foam: "Foam: Create New Note From Template" → daily-note template
- Or manually: `00-dev-log/YYYY-MM-DD.md`

## Special Directories

**02-worktrees/:**
- Purpose: Git worktrees for parallel development
- Source: `git worktree add` creates directories
- Committed: Only `README.md` is tracked; worktree contents are ignored via `.gitignore`
- Pattern: `02-worktrees/*` in gitignore, with `!02-worktrees/README.md` exception

**00-supporting-files/data/linux-kernel/ and ag2-framework/:**
- Purpose: Git submodules with reference codebases
- Source: Cloned from external repos (torvalds/linux, ag2ai/ag2)
- Committed: Only the submodule pointer (commit SHA), not the actual files
- Size: linux-kernel is very large (~40GB+)

**.venv/ (in each worktree):**
- Purpose: Python virtual environment managed by uv
- Source: Created by `uv sync`
- Committed: No (gitignored)

**kuzu_db/ (in linux_kernel worktree):**
- Purpose: Kuzu graph database storage for codebase indexing
- Source: Created at runtime when indexing kernel structure
- Committed: No (gitignored)

---

*Structure analysis: 2026-04-08*
*Update when directory structure changes*
