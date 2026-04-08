# Technology Stack

**Analysis Date:** 2026-04-08

## Languages

**Primary:**
- Python 3.13 - All application code (notebooks, scripts, analysis logic)

**Secondary:**
- Markdown - Documentation, dev logs, templates (Foam-based note-taking)

## Runtime

**Environment:**
- Python 3.13 (pinned via `.python-version` in each worktree)
- Jupyter notebooks as primary development interface
- No server/runtime component currently

**Package Manager:**
- uv - Fast Python package manager (lockfile: `uv.lock` in each worktree)
- No pip/requirements.txt; all managed through `pyproject.toml` + `uv`

## Frameworks

**Core:**
- None yet (early exploratory phase, notebook-driven development)

**Data/Analysis:**
- pandas 2.2.3+ - Data manipulation (file extension counts, data analysis)
- pyarrow 20.0.0+ - Arrow format support (likely for Kuzu/Parquet)
- tabulate 0.9.0+ - Pretty-printing tables in markdown

**Code Parsing:**
- tree-sitter 0.24.0 - Incremental parsing framework
- tree-sitter-c 0.24.1 - C language grammar (primary target: Linux kernel)
- tree-sitter-python 0.23.6 - Python language grammar
- tree-sitter-cpp 0.23.4 - C++ language grammar

**Graph Database:**
- kuzu 0.10.0+ - Embedded graph database (used to index/query Linux kernel structure)
- yfiles-jupyter-graphs 1.10.6+ - Graph visualization in Jupyter
- yfiles-jupyter-graphs-for-kuzu 0.0.4+ - Kuzu-specific graph visualization

## Key Dependencies

**Critical:**
- openai 1.91.0+ - LLM API client (Azure OpenAI and potentially NVIDIA NIMs)
- tree-sitter 0.24.0 - Code parsing and chunking
- kuzu 0.10.0+ - Graph database for codebase indexing

**Infrastructure:**
- python-dotenv 1.1.0+ - Environment variable management
- ipykernel 6.29.5+ - Jupyter kernel support
- jupyter 1.1.1+ - Notebook environment

## Configuration

**Environment:**
- `.env` files loaded via python-dotenv (gitignored)
- Template: `00-supporting-files/data/sample.env.file`
- Required vars: `OPENAI_API_TYPE`, `OPENAI_API_VERSION`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `NIMS_BASE_URL`, `NIMS_API_KEY`

**Build:**
- `pyproject.toml` per worktree (uv-based project definition)
- No build step - notebooks run directly

## Platform Requirements

**Development:**
- Any platform with Python 3.13 support
- uv package manager installed
- Git (for submodule management)
- ~40GB+ disk for Linux kernel submodule

**Production:**
- Not applicable yet (no deployment target)
- Future: likely CLI tool or API service

---

*Stack analysis: 2026-04-08*
*Update after major dependency changes*
