# autogen/tools/experimental/shell/shell_tool.py

2 class(es): CmdResult, ShellExecutor. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CmdResult | class |  |
| ShellExecutor | class |  |

## Chunks

### CmdResult (class, L16-L22)

> *Summary: Represents the outcome of running a shell command, storing standard output, standard error, the process exit code, and whether the execution timed out. It serves as a structured container for capturing all relevant execution details.*


### ShellExecutor (class, L25-L279)

> *Summary: This class provides a secure execution environment for shell commands, enforcing strict sandboxing through command whitelisting/blacklisting, path restrictions, and regex-based filtering of dangerous operations. It accepts configuration parameters like timeouts, allowed paths, and custom security patterns to govern how commands are run within a specified working directory.*


### __init__ (method, L73-L124, parent: ShellExecutor)

> *Summary: Configures a shell executor by setting execution constraints such as a default timeout, working directory, and path/command whitelists or blacklists. It accepts various optional arguments to define sandboxing rules for command execution.*


### _validate_path (method, L126-L155, parent: ShellExecutor)

> *Summary: Determines if a given file path is permitted by checking it against configured `allowed_paths` patterns, while ensuring the path remains within the defined workspace directory. It returns `True` if the path matches any allowed pattern or if all paths are permitted due to the presence of "**" in the configuration.*


### _validate_command (method, L157-L201, parent: ShellExecutor)

> *Summary: This method validates a command string against predefined security rules, including whitelists, blacklists, dangerous pattern matching, and restricted file path access. It accepts a command string as input and raises a `ValueError` if any security restriction is violated.*


### run (method, L203-L240, parent: ShellExecutor)

> *Summary: Executes a specified shell command within a restricted working directory, preventing shell injection by using `shlex.split`. It returns a result object containing standard output, standard error, the process's exit code, and a flag indicating if a timeout occurred.*


### run_commands (method, L242-L279, parent: ShellExecutor)

> *Summary: Executes a list of shell commands sequentially, optionally with a per-command timeout. It returns a list containing structured output objects detailing the standard output, standard error, and execution outcome (success, failure, or timeout) for each command.*

