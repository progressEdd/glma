# autogen/code_utils.py

15 function(s): content_str, infer_lang, extract_code, timeout_handler, get_powershell_command, _cmd, is_docker_running, in_docker_container, decide_use_docker, check_can_use_docker_or_throw and 5 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| content_str | function |  |
| infer_lang | function |  |
| extract_code | function |  |
| timeout_handler | function |  |
| get_powershell_command | function |  |
| _cmd | function |  |
| is_docker_running | function |  |
| in_docker_container | function |  |
| decide_use_docker | function |  |
| check_can_use_docker_or_throw | function |  |
| _sanitize_filename_for_docker_tag | function |  |
| execute_code | function |  |
| _remove_check | function |  |
| eval_function_completions | function |  |
| create_virtual_env | function |  |

## Chunks

### content_str (function, L52-L106)

> *Summary: Converts OpenAI message content, which can be a string or a list of structured parts, into a single string representation. It processes text directly, replaces image URLs with `<image>`, and formats other types like function calls or shell commands into descriptive tokens.*


### infer_lang (function, L109-L122)

> *Summary: Determines the programming language of an input string by checking for specific prefixes or attempting to compile it as Python. It returns `"sh"` if certain shell-like prefixes are found, `"python"` if compilation succeeds, and `UNKNOWN` otherwise.*


### extract_code (function, L127-L163)

> *Summary: This utility extracts structured code snippets from input text, which can be a string or list. It uses regular expressions to find blocks, optionally supporting single-line inline code extraction and returning a list of (language, code) tuples.*


### timeout_handler (function, L166-L167)

> *Summary: When a signal is received, this handler immediately raises a `TimeoutError`. It serves to abruptly terminate execution upon detecting a time limit breach.*


### get_powershell_command (function, L170-L195)

> *Summary: Determines the available PowerShell executable by first attempting to run `powershell` to check its version; if that fails, it tries `pwsh`, raising specific errors if neither command can be found or executed. Returns `"powershell"` or `"pwsh"` based on which interpreter is successfully invoked.*


### _cmd (function, L198-L211)

> *Summary: This utility maps various language strings to standardized command executables. It translates inputs like `"python"` variants, `"javascript"`, and different PowerShell notations into their corresponding system commands (`"python"`, `"node"`, or a specific PowerShell string).*


### is_docker_running (function, L214-L228)

> *Summary: Checks for the presence and operational status of a running Docker daemon by attempting to connect via `docker.from_env()` and pinging the client. Returns `True` if the connection succeeds, or `False` if the package is missing or the daemon is unreachable.*


### in_docker_container (function, L231-L237)

> *Summary: Determines if the current execution environment is within a Docker container by checking for the existence of the `/.dockerenv` file in the filesystem. It returns a boolean indicating the presence or absence of this marker.*


### decide_use_docker (function, L240-L262)

> *Summary: Determines the Docker usage preference by checking an optional input; if `None`, it reads and parses the `AUTOGEN_USE_DOCKER` environment variable, returning a boolean or `None` based on recognized string values. It raises a `ValueError` if the environment variable contains an unrecognized value.*


### check_can_use_docker_or_throw (function, L265-L276)

> *Summary: Validates the ability to use Docker for code execution based on configuration. It raises a `RuntimeError` if Docker is required but neither running nor available when executing outside a container.*


### _sanitize_filename_for_docker_tag (function, L279-L299)

> *Summary: This utility function transforms an arbitrary filename string into a valid Docker tag by replacing disallowed characters with underscores, ensuring it doesn't start with a period or dash, and truncating the result to 128 characters. It takes one string input (the filename) and returns a sanitized string suitable for use as a Docker image tag.*


### execute_code (function, L302-L488)

> *Summary: Executes provided or file-based code either natively or within a Docker container, depending on configuration. It accepts code/filename, timeout, working directory, Docker image specification, and language as inputs, returning the execution status code, output/error logs, and the used Docker image name if applicable.*


### _remove_check (function, L503-L509)

> *Summary: This utility strips out a specific "check" function definition from a given string response. It searches for `"def check("` and returns the portion of the string preceding that occurrence, or the original string if no such pattern is found.*


### eval_function_completions (function, L512-L591)

> *Summary: Evaluates a list of generated function responses against provided definitions and optional tests or assertion filters. It executes the code in an isolated environment (potentially Docker) to determine success metrics, returning a dictionary containing selection index, success status, and generation cost.*


### create_virtual_env (function, L605-L619)

> *Summary: This function constructs a Python virtual environment at the specified directory path, using provided arguments to configure its creation. It returns an object containing the necessary context for interacting with the newly created environment.*

