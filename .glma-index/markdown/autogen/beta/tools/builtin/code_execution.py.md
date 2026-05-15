# autogen/beta/tools/builtin/code_execution.py

2 class(es): CodeExecutionToolSchema, CodeExecutionTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CodeExecutionToolSchema | class |  |
| CodeExecutionTool | class |  |

## Chunks

### CodeExecutionToolSchema (class, L22-L26)

> *Summary: Defines a schema structure to represent the capability for executing code. It sets fixed values for the tool's type and version identifier.*


### CodeExecutionTool (class, L29-L64)

> *Summary: Provides a standardized interface for executing code, accepting context information to define its schema and register an event handler for tool calls. It acts as a provider-neutral wrapper that delegates API translation to the LLM client's mapper.*


### __init__ (method, L41-L47, parent: CodeExecutionTool)

> *Summary: Initializes the code execution tool by setting up a schema based on a specified version and assigning it a predefined name. This prepares the object for use as an executable tool within the system.*


### schemas (method, L49-L50, parent: CodeExecutionTool)

> *Summary: Returns a list containing the tool's schema definition based on the provided execution context. This allows external systems to understand the structure and capabilities of the code execution tool.*


### register (method, L52-L64, parent: CodeExecutionTool)

> *Summary: This method registers a handler for code execution tool calls within an asynchronous context stack. It sets up a scope that intercepts events matching the specific code execution tool name, allowing custom logic to be executed upon invocation.*

