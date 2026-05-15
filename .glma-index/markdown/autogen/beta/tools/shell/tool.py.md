# autogen/beta/tools/shell/tool.py

1 class(es): LocalShellTool. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LocalShellTool | class |  |

## Chunks

### LocalShellTool (class, L19-L89)

> *Summary: Provides a mechanism to execute shell commands within a specified execution environment, which can be a local directory or a temporary one by default. It takes an optional `environment` argument (path or existing environment object) and exposes the command execution via a registered tool function.*


### __init__ (method, L51-L72, parent: LocalShellTool)

> *Summary: Initializes a tool wrapper that executes shell commands by setting up a local environment and wrapping the execution function with metadata like name and description. It accepts an optional environment configuration to determine where the command will run, storing the resulting working directory for later use.*


### workdir (method, L75-L77, parent: LocalShellTool)

> *Summary: Returns the `Path` object representing the current working directory of the execution environment. This method provides direct access to where the tool is operating.*


### schemas (method, L79-L80, parent: LocalShellTool)

> *Summary: Retrieves the schema definitions for the tool by calling an internal method on the underlying tool object, passing along the current execution context. It returns a list containing these schema definitions.*


### register (method, L82-L89, parent: LocalShellTool)

> *Summary: This method delegates the registration of a tool to an underlying object using provided stack, context, and optional middleware. It serves as a wrapper to pass these parameters down for tool setup.*

