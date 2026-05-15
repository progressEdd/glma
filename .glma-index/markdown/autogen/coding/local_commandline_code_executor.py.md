# autogen/coding/local_commandline_code_executor.py

1 class(es): LocalCommandLineCodeExecutor. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LocalCommandLineCodeExecutor | class |  |

## Chunks

### LocalCommandLineCodeExecutor (class, L40-L341)

> *Summary: This class executes or saves LLM-generated code blocks locally using system commands, supporting languages like Python and various shell scripts. It takes configuration for timeouts, working directories, available functions, and execution policies as input, returning a result containing the exit code, combined output logs, and the path to the first executed file.*


### __init__ (method, L74-L143, parent: LocalCommandLineCodeExecutor)

> *Summary: Initializes a local code executor capable of running or saving LLM-generated code in a specified working directory, respecting language-specific execution policies and supporting optional virtual environments. It accepts configuration for timeouts, available functions, and defines the operational environment before any code is processed.*


### format_functions_for_prompt (method, L145-L162, parent: LocalCommandLineCodeExecutor)

> *Summary: Takes a prompt template and substitutes placeholders with the module name and a list of function stubs. It returns a fully formatted string ready to be used as an AI prompt, separating each function stub with double newlines.*


### functions_module (method, L165-L167, parent: LocalCommandLineCodeExecutor)

> *Summary: Returns the internal string representing the module name used to execute defined functions. This method provides access to the specific module identifier configured within the executor instance.*


### functions (method, L170-L174, parent: LocalCommandLineCodeExecutor)

> *Summary: Returns a list containing all callable functions and structured function definitions accessible by the code execution environment. This provides the executor with the set of tools it can invoke during code generation or testing.*


### timeout (method, L177-L179, parent: LocalCommandLineCodeExecutor)

> *Summary: Retrieves the configured time limit, which is stored internally as an integer representing the maximum duration allowed for code execution.*


### work_dir (method, L182-L184, parent: LocalCommandLineCodeExecutor)

> *Summary: Returns the current working directory used for executing code, which is stored internally as a `Path` object. This method provides access to the environment where code operations take place.*


### code_extractor (method, L187-L189, parent: LocalCommandLineCodeExecutor)

> *Summary: Provides access to a `MarkdownCodeExtractor` instance, allowing agents to extract code blocks from markdown content. This method returns the configured extractor object for external use.*


### sanitize_command (method, L192-L210, parent: LocalCommandLineCodeExecutor)

> *Summary: Checks a provided code string against a list of regex patterns to prevent execution of harmful shell commands like `rm -rf` or disk manipulation. If the input language is Bash/Shell and any forbidden pattern is found, it raises a `ValueError`.*


### _setup_functions (method, L212-L242, parent: LocalCommandLineCodeExecutor)

> *Summary: This method generates a Python file containing defined functions based on internal configuration, then installs any necessary dependencies using `pip` within the execution environment. Finally, it executes this generated code to validate syntax and imports before marking the setup as complete.*


### execute_code_blocks (method, L244-L255, parent: LocalCommandLineCodeExecutor)

> *Summary: This method executes a list of provided `CodeBlock` objects after ensuring necessary functions are set up. It returns a `CommandLineCodeResult` containing the outcome of the execution.*


### _execute_code_dont_check_setup (method, L257-L337, parent: LocalCommandLineCodeExecutor)

> *Summary: Executes a list of provided code blocks by sanitizing and writing them to temporary files based on their specified language. It then runs these files using the appropriate command-line interpreter, handling virtual environments and timeouts, and returns a result containing the combined output and final exit code.*


### restart (method, L339-L341, parent: LocalCommandLineCodeExecutor)

> *Summary: This method signals an intent to restart the local code executor but currently does nothing, issuing a warning instead because this functionality is experimental and unsupported.*

