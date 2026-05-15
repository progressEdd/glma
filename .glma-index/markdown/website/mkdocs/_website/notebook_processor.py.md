# website/mkdocs/_website/notebook_processor.py

17 function(s): path, check_quarto_bin, require_quarto_bin, load_metadata, skip_reason_or_none_if_ok, extract_title, start_thread_to_terminate_when_parent_process_dies, fmt_skip, fmt_ok, fmt_error and 7 more. 3 class(es): NotebookError, NotebookSkip, Result. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| NotebookError | class |  |
| NotebookSkip | class |  |
| Result | class |  |
| path | function |  |
| check_quarto_bin | function |  |
| require_quarto_bin | function |  |
| load_metadata | function |  |
| skip_reason_or_none_if_ok | function |  |
| extract_title | function |  |
| start_thread_to_terminate_when_parent_process_dies | function |  |
| fmt_skip | function |  |
| fmt_ok | function |  |
| fmt_error | function |  |
| test_notebook | function |  |
| get_timeout_info | function |  |
| get_error_info | function |  |
| collect_notebooks | function |  |
| process_notebook | function |  |
| create_base_argument_parser | function |  |
| process_notebooks_core | function |  |

## Chunks

### NotebookError (class, L40-L44)

> *Summary: Represents an error encountered during notebook processing, storing the error name and value, along with the full traceback and the source code of the problematic cell. This class serves as a structured container for detailed failure information.*


### NotebookSkip (class, L48-L49)

> *Summary: This class holds a string attribute to specify the reason why a notebook should be skipped during processing. It acts as a simple marker for exclusion logic elsewhere in the system.*


### Result (class, L55-L59)

> *Summary: This class encapsulates the outcome of an external process execution by storing its exit code, standard output, and standard error streams. It serves as a structured container for capturing command execution results.*


### __init__ (method, L56-L59, parent: Result)

> *Summary: Initializes an object to store the results of a process execution. It accepts and saves the exit code, standard output string, and standard error string as instance attributes.*


### path (function, L62-L64)

> *Summary: Converts an input string representing a file path into a `Path` object. This utility function ensures the path is represented using Python's standard `pathlib` structure for consistent filesystem operations.*


### check_quarto_bin (function, L68-L76)

> *Summary: Determines if the Quarto command-line tool is available and meets a minimum version requirement of 1.5.23 by executing `quarto --version` and parsing the output. Returns `True` only if the executable is found and the installed version is sufficiently recent.*


### require_quarto_bin (function, L82-L92)

> *Summary: This decorator wraps a function to ensure the Quarto binary is available before execution. If `check_quarto_bin()` returns false, it replaces the original function with one that raises an `ImportError` upon invocation.*


### load_metadata (function, L95-L98)

> *Summary: Reads a JSON notebook file and extracts its metadata section. It takes a `Path` object pointing to the notebook as input and returns the parsed metadata dictionary.*


### skip_reason_or_none_if_ok (function, L101-L150)

> *Summary: Determines if a notebook should be skipped by checking its file type, existence, and metadata. It returns a specific reason string or `None` if the notebook is valid for processing after validating required front matter fields like tags and description.*


### extract_title (function, L153-L171)

> *Summary: Reads a notebook file, parses its JSON content, and inspects the source code of the first cell to find and return the string following the initial `# ` marker as the document's title. It handles cases where the title might contain an opening brace `{` by truncating it.*


### start_thread_to_terminate_when_parent_process_dies (function, L174-L186)

> *Summary: Initiates a background thread that periodically checks the parent process's existence by sending a signal to it. If the parent process terminates, this thread sends a termination signal to its own process ID.*


### fmt_skip (function, L190-L191)

> *Summary: Generates a formatted string indicating that a notebook should be skipped, incorporating the notebook's name and the provided reason into a colored output. It takes a `Path` object representing the notebook and a descriptive `str` as input to produce the final status message.*


### fmt_ok (function, L195-L196)

> *Summary: Formats a notebook file path into a styled string indicating success. It takes a `Path` object and returns a green "\[OK]" tag followed by the blue filename and a checkmark emoji.*


### fmt_error (function, L200-L206)

> *Summary: Formats an error message based on whether the input is a simple string or a structured `NotebookError` object, returning a colored string indicating the notebook name and the specific error details. It raises a `ValueError` if the provided error type is neither a string nor a `NotebookError`.*


### test_notebook (function, L211-L237)

> *Summary: Reads a Jupyter notebook file and attempts to execute its cells using a `NotebookClient` within a temporary directory. It returns the original path along with either an execution/timeout error object or `None` if successful, respecting a "skip\_test" metadata flag first.*


### get_timeout_info (function, L242-L256)

> *Summary: Checks a notebook node's code cells to determine if any execution reply metadata is missing. If a code cell lacks `"shell.execute_reply"`, it returns a `NotebookError` indicating a timeout; otherwise, it returns `None`.*


### get_error_info (function, L260-L274)

> *Summary: This function iterates through a notebook's code cells to find the last recorded error. If an error is found in any cell, it constructs and returns a `NotebookError` object containing the error name, value, traceback, and source code of that specific cell; otherwise, it returns `None`.*


### collect_notebooks (function, L277-L280)

> *Summary: Gathers all `.ipynb` files from both a specified notebook directory and the website's build output directory. It returns a list containing the full paths to every found Jupyter notebook file.*


### process_notebook (function, L285-L377)

> *Summary: Renders a single source notebook into an output file by invoking the Quarto binary. It accepts source and build paths, handles metadata extraction, checks for file staleness, and optionally runs a post-processing callback on successful rendering.*


### create_base_argument_parser (function, L380-L410)

> *Summary: Constructs a command-line argument parser that supports two main subcommands: `render` and `test`. It accepts global options like notebook/website directories and flags for forcing builds or dry runs, while the subcommands handle specific inputs such as lists of notebooks and worker counts.*


### process_notebooks_core (function, L413-L494)

> *Summary: Gathers and filters notebooks based on command-line arguments, then executes either a parallel testing or rendering process depending on the subcommand. It uses `ProcessPoolExecutor` for tests or `ThreadPoolExecutor` for rendering, ultimately returning the list of processed notebook paths.*

