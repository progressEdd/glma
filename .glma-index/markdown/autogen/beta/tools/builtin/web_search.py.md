# autogen/beta/tools/builtin/web_search.py

3 class(es): UserLocation, WebSearchToolSchema, WebSearchTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| UserLocation | class |  |
| WebSearchToolSchema | class |  |
| WebSearchTool | class |  |

## Chunks

### UserLocation (class, L22-L26)

> *Summary: This class serves as a data structure to hold geographical information about the user. It accepts and stores optional values for city, region, country, and timezone strings.*


### WebSearchToolSchema (class, L30-L37)

> *Summary: Defines the structure for a web search tool, accepting optional parameters like context size, usage limits, user location, and lists of allowed/blocked domains. It enforces specific versions for the underlying web search implementation.*


### WebSearchTool (class, L40-L88)

> *Summary: This class implements a tool for performing web searches, configurable via parameters like context size, domain restrictions, and usage limits passed during initialization. It exposes its configuration as schemas and registers itself to intercept specific tool call events within the execution stack.*


### __init__ (method, L46-L70, parent: WebSearchTool)

> *Summary: Initializes a web search tool by accepting optional configuration parameters such as context size, usage limits, location, and domain restrictions. These inputs are stored internally to define the specific behavior of the search functionality.*


### schemas (method, L72-L74, parent: WebSearchTool)

> *Summary: Generates a list containing a `WebSearchToolSchema` instance by resolving any variable references within the tool's parameters using the provided execution context. This method prepares the schema definition for external use based on internal configuration and runtime context.*


### register (method, L76-L88, parent: WebSearchTool)

> *Summary: This method registers a handler to intercept specific `ToolCallEvent`s matching the web search tool name within an asynchronous context stack. It sets up a scope where the provided `execute` function will be called when such an event occurs, allowing for custom processing of the request.*

