# autogen/beta/tools/final/client_tool.py

1 class(es): ClientTool. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ClientTool | class |  |

## Chunks

### ClientTool (class, L18-L51)

> *Summary: This class wraps a function schema to expose it as an available tool within a system context. It registers the tool's execution handler against specific incoming tool call events and provides a method to convert incoming calls into a structured event response.*


### __init__ (method, L24-L26, parent: ClientTool)

> *Summary: Initializes the client tool by converting a provided dictionary schema into a structured `FunctionToolSchema` object and storing its name. This sets up the necessary metadata for the tool's operation.*


### schemas (method, L28-L29, parent: ClientTool)

> *Summary: Returns a list containing the tool's schema definition based on the provided execution context. This allows external systems to understand the structure and capabilities of the client tool.*


### register (method, L31-L48, parent: ClientTool)

> *Summary: This method hooks into a streaming context to intercept specific tool call events matching the object's schema name. It wraps the execution logic with provided middleware and sends the resulting output back through the context stream.*


### __call__ (method, L50-L51, parent: ClientTool)

> *Summary: This method takes a `ToolCallEvent` and a `Context`, then returns a new `ClientToolCallEvent` instance constructed directly from the input event. It acts as a simple wrapper to transform the incoming tool call event into its client-specific representation.*

