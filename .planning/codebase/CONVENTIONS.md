# Coding Conventions

**Analysis Date:** 2026-04-08

## Naming Patterns

**Files:**
- `*.ipynb` for Jupyter notebooks (`develop.ipynb`, `sandbox.ipynb`)
- `*.md` for all documentation (kebab-case filenames: `daily-note.md`, `new-template.md`)
- `pyproject.toml` for Python project config (standard naming)
- Date-based dev logs: `YYYY-MM-DD.md`

**Functions (in notebooks):**
- snake_case for all Python functions (`get_directory_tree`, `print_tree`)
- Descriptive verb-noun pattern (`get_directory_tree`, not `tree`)

**Variables:**
- snake_case for all Python variables (`supporting_files`, `linux_dir`, `ag2_dir`)
- `UPPER_SNAKE_CASE` for environment variable keys in `.env` files (`OPENAI_API_TYPE`, `NIMS_BASE_URL`)
- Numbered prefix for directories (`00-dev-log`, `01-dev-onboarding`, `02-worktrees`)

**Types:**
- No custom types or classes defined yet (notebook-based scripting)

## Code Style

**Formatting:**
- No formatter configured (no black, ruff, or autopep8)
- 4-space indentation (Python standard)
- Long lines common in notebook cells (no line length enforcement)

**Linting:**
- No linter configured
- No CI/CD checks

**Import Style:**
```python
import os
from dotenv import load_dotenv
from pathlib import Path
```
- Standard library first, then third-party (implicit, not enforced)

## Import Organization

**Order:**
1. Standard library (`os`, `pathlib`)
2. Third-party packages (`dotenv`, `pandas`, `tree_sitter`)
3. Local modules (none yet)

**Grouping:**
- No explicit blank line separation between groups
- Imports typically at top of notebook cell, not centralized

## Error Handling

**Patterns:**
- Exploratory phase: minimal formal error handling
- Print-based debugging
- Manual correction when tree-sitter language was misconfigured (discovered Python default instead of C)

**Error Types:**
- Environment misconfiguration handled by checking outputs manually
- No custom exception classes
- No logging framework (print statements and notebook output)

## Logging

**Framework:**
- Notebook cell output (stdout/stderr)
- No structured logging

**Patterns:**
- Display variables by putting them alone in a cell (Jupyter auto-display)
- `print()` for explicit output in loops/conditionals
- No log levels or log files

## Comments

**When to Comment:**
- Markdown cells in notebooks serve as documentation (structured like section headers)
- Code comments rare - notebook cells are self-documenting via markdown headers above them
- Dev logs capture decisions and rationale

**JSDoc/TSDoc:**
- No docstrings observed on functions
- Function names are self-descriptive

## Function Design

**Size:**
- Functions tend to be larger (30-50+ lines) since they live in notebook cells
- The `get_directory_tree()` function is ~60 lines with recursion, depth limiting, and formatting

**Parameters:**
- Simple positional parameters: `get_directory_tree(directory_path, level=0, prefix='', max_depth=None)`
- Default values used for recursion state

**Return Values:**
- Functions return data structures (lists, dicts) for display in subsequent cells
- No explicit return type annotations

## Module Design

**Exports:**
- No module system - all code lives in notebook cells
- No `__init__.py` files or package structure
- No shared utility modules between worktrees

**Notebook Structure:**
```markdown
# Section Title (markdown cell)

[code cell with imports and setup]

## Subsection Title (markdown cell)

[code cell with analysis logic]

[code cell with output/display]
```

## Environment Configuration

**Pattern:**
```python
from dotenv import load_dotenv
from pathlib import Path

current_dir = Path(__file__).resolve().parent if '__file__' in locals() else Path.cwd()
supporting_files = os.path.join(current_dir.parents[1], "00-supporting-files")
```
- Path resolution navigates up from worktree to repository root
- `__file__` check for portability between notebook and script execution
- Environment variables loaded from shared `.env` in supporting files

## Workflow Conventions

**Git Branch Strategy:**
- `master` - Repository structure, documentation, shared resources
- `00-experiments` - Base template for forking new experiments
- Named branches - Individual experiments (`linux_kernel`, `notebook-compression`)

**Development Process:**
1. Create worktree from `00-experiments` branch
2. Customize `pyproject.toml` and `sandbox.ipynb`
3. Run `uv sync` to install dependencies
4. Work in notebook cells, document progress in dev logs

**Daily Logging:**
- Use Foam daily-note template
- Record overall progress at top, elaboration sections below
- Include code snippets, findings, and blockers

---

*Convention analysis: 2026-04-08*
*Update when patterns change*
