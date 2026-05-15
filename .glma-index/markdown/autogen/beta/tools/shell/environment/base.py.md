# autogen/beta/tools/shell/environment/base.py

2 function(s): matches, check_ignore. 1 class(es): ShellEnvironment. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| matches | function |  |
| check_ignore | function |  |
| ShellEnvironment | class |  |

## Chunks

### matches (function, L48-L58)

> *Summary: Checks if a given command string begins with a specified pattern, ensuring the match is either exact or followed by a space to qualify as a whole word prefix. Returns `True` if the command starts with the pattern and the remainder is empty or starts with whitespace.*


### check_ignore (function, L61-L99)

> *Summary: Determines if any path specified in a shell command matches a list of exclusion patterns, resolving paths relative to a working directory. It returns an "Access denied" string with the matching path if a match is found, or `None` otherwise.*


### ShellEnvironment (class, L103-L107)

> *Summary: Defines a protocol for an environment capable of providing a working directory path and executing shell commands to return their output. This structure dictates that any implementing class must expose these two methods/properties.*


### workdir (method, L105-L105, parent: ShellEnvironment)

> *Summary: Returns the current working directory as a `Path` object for the agent's execution context. This method provides access to the designated operational folder.*


### run (method, L107-L107, parent: ShellEnvironment)

> *Summary: Executes a shell command string and returns the resulting output as a string. It serves as the core execution mechanism for running external system commands within the environment.*

