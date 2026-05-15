# autogen/beta/tools/builtin/web_fetch.py

2 class(es): WebFetchToolSchema, WebFetchTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WebFetchToolSchema | class |  |
| WebFetchTool | class |  |

## Chunks

### WebFetchToolSchema (class, L22-L29)

> *Summary: Defines the structure for a web fetching tool, specifying configuration parameters like allowed/blocked domains, citation requirements, and content token limits. It uses a fixed version identifier to manage different implementations of the web fetch functionality.*


### WebFetchTool (class, L32-L80)

> *Summary: This class provides a tool for fetching web content, configurable via parameters like allowed/blocked domains and token limits. It registers itself to intercept specific tool calls within an execution context, allowing asynchronous retrieval of external data.*


### __init__ (method, L38-L62, parent: WebFetchTool)

> *Summary: Initializes a web fetching tool by accepting optional configuration parameters such as domain lists, usage limits, and content token caps. These inputs are stored internally to define the tool's operational constraints before it is registered with its designated name.*


### schemas (method, L64-L66, parent: WebFetchTool)

> *Summary: Generates a list of `WebFetchToolSchema` objects by resolving any variable references within the tool's parameters using the provided execution context. This allows the schema to accurately reflect parameter values based on runtime context.*


### register (method, L68-L80, parent: WebFetchTool)

> *Summary: This method registers a handler for specific web fetch tool calls within an asynchronous context stack. It sets up a scope to intercept events matching the predefined `WEB_FETCH_TOOL_NAME` and executes a placeholder function upon interception.*

