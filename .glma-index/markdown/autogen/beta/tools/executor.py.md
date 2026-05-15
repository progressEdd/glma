# autogen/beta/tools/executor.py

2 function(s): _execute_call, _tool_not_found. 1 class(es): ToolExecutor. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ToolExecutor | class |  |
| _execute_call | function |  |
| _tool_not_found | function |  |

## Chunks

### ToolExecutor (class, L32-L105)

> *Summary: Manages the execution of registered tools by subscribing to tool call events within a given context. It concurrently runs requested tools, serializes data inputs as needed, and outputs either model responses or aggregated tool results based on the execution outcome.*


### __init__ (method, L33-L34, parent: ToolExecutor)

> *Summary: Initializes the executor by storing a provided `SerializerProto` instance for serialization operations. This sets up the necessary component to handle data encoding and decoding within the execution context.*


### register (method, L36-L53, parent: ToolExecutor)

> *Summary: This method sets up the execution environment by entering a scope that listens for `ToolCallsEvent` and then iterates through provided tools to register them within the current context and stack. It also establishes a fallback subscription to raise a "Not Found" event if no known tool matches an incoming `ToolCallEvent`.*


### execute_tools (method, L55-L105, parent: ToolExecutor)

> *Summary: This method concurrently executes a list of requested tools and processes the outcomes. It aggregates results, sending back model responses if a tool returns final content or sends a batch of collected tool results/client calls otherwise.*


### _execute_call (function, L108-L117)

> *Summary: This asynchronous function sends a `ToolCallEvent` to the streaming context and waits for the corresponding response, which can be an error, result, or client confirmation event. It effectively executes the requested tool call within the provided conversational context.*


### _tool_not_found (function, L120-L132)

> *Summary: Creates and returns an asynchronous handler that intercepts tool calls; if the requested tool name is not present in a provided list of known tools, it generates and sends a `ToolNotFoundEvent` back to the system.*

