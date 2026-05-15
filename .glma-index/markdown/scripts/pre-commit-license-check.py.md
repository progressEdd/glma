# scripts/pre-commit-license-check.py

7 function(s): get_github_pr_files, get_staged_files, list_git_untracked_files, should_check_file, check_file_header, get_files_to_check, main.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_github_pr_files | function |  |
| get_staged_files | function |  |
| list_git_untracked_files | function |  |
| should_check_file | function |  |
| check_file_header | function |  |
| get_files_to_check | function |  |
| main | function |  |

## Chunks

### get_github_pr_files (function, L23-L47)

> *Summary: Retrieves a list of Python file paths that have been modified, either by parsing the GitHub event payload for pull requests or by running `git diff` for push events. It returns an empty list if any error occurs during the process.*


### get_staged_files (function, L50-L60)

> *Summary: Executes a `git diff` command to retrieve names of all staged changes, filtering specifically for Python files (`.py`). It returns a list of `Path` objects representing these staged Python files or an empty list if the git command fails.*


### list_git_untracked_files (function, L63-L96)

> *Summary: Executes `git status --porcelain` to identify files not tracked by Git within the current repository. It returns a list of file paths for untracked items, an empty list if none are found or if not in a repo, or `None` upon execution errors.*


### should_check_file (function, L99-L102)

> *Summary: Determines whether a given file path should be processed by checking only for its existence on the filesystem. It currently ignores the logic to skip `__init__.py` files.*


### check_file_header (function, L105-L134)

> *Summary: Reads the first 500 bytes of a given file path to check for required license header patterns. It returns a list of regex patterns that were not found in the file's initial content, or an empty list if all requirements are met.*


### get_files_to_check (function, L137-L150)

> *Summary: This function gathers Python file paths by recursively searching the `autogen` and `test` directories. It returns a list of these `Path` objects, currently ignoring command-line arguments or environment variables for selection.*


### main (function, L153-L182)

> *Summary: This script iterates over Python files identified by `get_files_to_check()`, skipping untracked files, to verify the presence of required license headers using `check_file_header()`. It exits with a non-zero status if any file is found to have an incomplete or missing header.*

