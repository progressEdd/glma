# autogen/beta/tools/shell/environment/local.py

1 class(es): LocalShellEnvironment. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LocalShellEnvironment | class |  |

## Chunks

### LocalShellEnvironment (class, L15-L156)

> *Summary: This class manages local shell execution by wrapping `subprocess` calls within a controlled environment. It accepts configuration for the working directory, command whitelists/blacklists, file exclusion patterns, and read-only mode to govern what commands can run. The primary method executes a given command string, applying all security checks before returning its combined standard output and error as a string.*


### __init__ (method, L70-L103, parent: LocalShellEnvironment)

> *Summary: Initializes a local shell execution environment, setting up a working directory either from a provided path or by creating a temporary one. It configures operational constraints such as allowed/blocked commands, environment variables, and timeouts based on input parameters.*


### ensure_env (method, L106-L109, parent: LocalShellEnvironment)

> *Summary: If the provided environment input is already a `ShellEnvironment` instance, it is returned directly; otherwise, it constructs and returns a new `ShellEnvironment` using the input.*


### workdir (method, L112-L114, parent: LocalShellEnvironment)

> *Summary: Returns the current working directory as a `Path` object, which is stored internally within the instance. This provides access to the location where shell commands are executed.*


### run (method, L116-L156, parent: LocalShellEnvironment)

> *Summary: Executes a shell command after applying filtering rules for allowed, blocked, and ignored patterns. It returns the combined standard output and error as a string, truncating it if it exceeds a maximum length, or reports timeout/non-zero exit codes otherwise.*

