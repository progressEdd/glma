# autogen/beta/tools/builtin/memory.py

2 class(es): MemoryToolSchema, MemoryTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MemoryToolSchema | class |  |
| MemoryTool | class |  |

## Chunks

### MemoryToolSchema (class, L20-L24)

> *Summary: Defines a schema for the memory tool, providing a standardized, provider-agnostic way to describe its capabilities. It sets fixed values for the tool's type and version identifier.*


### MemoryTool (class, L27-L67)

> *Summary: Provides an interface for Claude to persist and retrieve information across sessions by managing files in a designated memory directory. It registers itself as a tool, expecting external handlers to implement the logic for creating, reading, updating, and deleting stored memories based on incoming tool calls.*


### __init__ (method, L44-L50, parent: MemoryTool)

> *Summary: Initializes the memory tool by setting up its schema using a specified version string. This establishes the internal structure and naming convention for the tool instance.*


### schemas (method, L52-L53, parent: MemoryTool)

> *Summary: Returns a list containing the tool's schema definition based on the provided execution context. This allows external systems to understand the structure and capabilities of the tool.*


### register (method, L55-L67, parent: MemoryTool)

> *Summary: This method registers a handler within an exit stack to intercept specific tool call events related to memory. It sets up an asynchronous execution context that will be triggered only when the incoming event matches the predefined memory tool name.*

