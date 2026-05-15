# autogen/beta/tools/toolkits/mcp_server/toolkit.py

6 function(s): _mcp_session, _wrap_middleware, _extract_content, _kind_from_mime, _resolve_value, _resolve_config. 2 class(es): _MCPProxyTool, MCPServer. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _mcp_session | function |  |
| _MCPProxyTool | class |  |
| MCPServer | class |  |
| _wrap_middleware | function |  |
| _extract_content | function |  |
| _kind_from_mime | function |  |
| _resolve_value | function |  |
| _resolve_config | function |  |

## Chunks

### _mcp_session (function, L63-L98)

> *Summary: This asynchronous generator establishes a temporary client session for an MCP server based on the provided configuration type. It either spawns a subprocess using `stdio_client` or uses HTTP requests via `httpx` to create and yield a ready-to-use `ClientSession`.*


### _MCPProxyTool (class, L101-L157)

> *Summary: This class acts as a proxy tool that forwards function calls to a remote MCP server based on provided configuration and raw tool definitions. It accepts a `ToolCallEvent` and context, communicates with the remote service via an asynchronous session, and returns either a successful result or a detailed error event.*


### __init__ (method, L106-L121, parent: _MCPProxyTool)

> *Summary: Initializes a toolkit by storing configuration and middleware, then sets the tool's name and generates a function schema based on the provided raw tool definition. This prepares the toolkit for use by encapsulating its metadata and structure.*


### schemas (method, L123-L124, parent: _MCPProxyTool)

> *Summary: Returns a list containing the toolkit's defined schema when provided with a `Context` object. This allows external systems to understand the available functions and their structures.*


### register (method, L126-L143, parent: _MCPProxyTool)

> *Summary: This method wraps the tool's core execution logic with a chain of provided and internal middleware hooks. It then registers an asynchronous handler within the event stream to intercept specific `ToolCallEvent` instances, executing the wrapped logic upon receipt.*


### __call__ (method, L145-L157, parent: _MCPProxyTool)

> *Summary: This method executes a tool call by first resolving configuration and establishing an MCP session. It takes a `ToolCallEvent` and `Context`, returning either a successful `ToolResultEvent` containing extracted content or a `ToolErrorEvent` upon failure during execution or result processing.*


### MCPServer (class, L160-L228)

> *Summary: This class wraps an MCP server connection—either via URL or local stdin/stdout—to expose its remote tools as standard local functions to an agent. Upon the first call to `schemas`, it performs an MCP handshake, discovers available tools based on configuration rules, and registers proxies for them without exposing the underlying MCP nature.*


### __init__ (method, L178-L194, parent: MCPServer)

> *Summary: Initializes the toolkit by accepting a server configuration (string URL or config object) and optional middleware. It sets up internal state, converts string inputs to configurations, and calls the parent constructor with a derived name based on the server's label.*


### schemas (method, L196-L198, parent: MCPServer)

> *Summary: After discovering available tools within the provided context, this method returns an iterable collection of `FunctionToolSchema` objects. It delegates the actual schema retrieval to its parent class after performing tool discovery.*


### _discover_tools (method, L200-L228, parent: MCPServer)

> *Summary: This method asynchronously fetches a list of available tools from an MCP server based on the provided configuration and context. It filters these raw tools against allowed and blocked lists before instantiating and storing them as proxied tool objects within the instance's internal dictionary.*


### _wrap_middleware (function, L231-L235)

> *Summary: This function wraps an execution handler by creating a new asynchronous callable. It takes the original middleware and inner execution logic as input, returning a wrapper that delegates calls to the provided `hook` with the necessary event and context.*


### _extract_content (function, L238-L286)

> *Summary: Transforms a `CallToolResult` containing various content blocks into a typed `ToolResult`. It iterates through the result's content, mapping different block types (text, image, audio, resource links, embedded resources) to appropriate structured inputs like `TextInput`, `BinaryInput`, or `UrlInput`.*


### _kind_from_mime (function, L297-L300)

> *Summary: Determines the `BinaryType` from a provided MIME type string; if the input is null or the MIME type is unrecognized in the internal map, it defaults to `BinaryType.BINARY`.*


### _resolve_value (function, L303-L313)

> *Summary: Resolves a `Variable` object by first checking the provided context's variables for its name. If not found, it attempts to return a predefined default value or instantiate a factory function; otherwise, it raises a `KeyError`.*


### _resolve_config (function, L316-L344)

> *Summary: This function processes an MCP configuration object by recursively resolving values within it using a provided context. It handles two main types: one for standard I/O server configurations and another for general server URL configurations, applying necessary transformations like injecting authorization headers if a token is present.*

