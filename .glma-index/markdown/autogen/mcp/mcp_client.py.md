# autogen/mcp/mcp_client.py

2 function(s): _sanitize_resource_filename, create_toolkit. 8 class(es): SessionConfigProtocol, BasicSessionConfig, SseConfig, StdioConfig, MCPConfig, MCPClient, MCPClientSessionManager, ResultSaved. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _sanitize_resource_filename | function |  |
| SessionConfigProtocol | class |  |
| BasicSessionConfig | class |  |
| SseConfig | class |  |
| StdioConfig | class |  |
| MCPConfig | class |  |
| MCPClient | class |  |
| MCPClientSessionManager | class |  |
| create_toolkit | function |  |
| ResultSaved | class |  |

## Chunks

### _sanitize_resource_filename (function, L43-L55)

> *Summary: This function converts a remote URI into a safe, local `Path` object within a specified download directory. It extracts the base name from the URI, appends a timestamp, and rigorously checks to prevent path traversal attacks before returning the final file location.*


### SessionConfigProtocol (class, L58-L69)

> *Summary: Defines a contract for configuration objects capable of establishing MCP sessions. It requires a `server_name` and an asynchronous method (`create_session`) that yields a `ClientSession` within an async context manager.*


### create_session (method, L64-L69, parent: SessionConfigProtocol)

> *Summary: This method yields an iterator representing a client session, designed to be managed by an `AsyncExitStack`. Currently, it only provides a placeholder yield and raises `NotImplementedError` upon any exception.*


### BasicSessionConfig (class, L72-L93)

> *Summary: This configuration object provides a method to establish and initialize an asynchronous client session. It takes an async context manager and an exit stack as input, returning a fully configured `ClientSession` instance ready for communication.*


### initialize (method, L77-L93, parent: BasicSessionConfig)

> *Summary: This method sets up a client session by acquiring asynchronous reader and writer streams from the provided context manager. It then instantiates and returns a fully configured `ClientSession` object using those streams.*


### SseConfig (class, L96-L117)

> *Summary: Defines configuration parameters for an SSE MCP server, including URL, headers, and various timeouts. It provides a context manager method to establish and yield an active `ClientSession` connected to the specified endpoint.*


### create_session (method, L105-L117, parent: SseConfig)

> *Summary: Establishes a new client session to an MCP server via SSE transport. It takes an `AsyncExitStack` for resource management and yields the initialized `ClientSession`.*


### StdioConfig (class, L120-L154)

> *Summary: Defines configuration parameters for an MCP server communicating via standard I/O, including the executable command, arguments, and environment settings. It provides a context manager method to establish and yield an active client session based on these specifications.*


### create_session (method, L135-L154, parent: StdioConfig)

> *Summary: Establishes a new client session to an MCP server via stdio transport by configuring the connection with provided command and environment details. It yields the initialized `ClientSession` object after setting up the underlying stdio client.*


### MCPConfig (class, L157-L161)

> *Summary: Defines a configuration structure for managing multiple MCP sessions via standard I/O transport. It requires an input list containing either `StdioConfig` or `SseConfig` objects to specify the connection endpoints.*


### MCPClient (class, L164-L296)

> *Summary: This class provides methods to translate MCP-specific definitions into a standardized AG2 toolkit format. It converts MCP tools by calling session functions and handles resource templates by creating callable tools that can read or save external resources based on URI templates. The main entry point loads both available tools and resources from a client session into a `Toolkit` object.*


### _convert_call_tool_result (method, L166-L184, parent: MCPClient)

> *Summary: Transforms a `CallToolResult` object into structured output by separating text and non-text contents. It returns the extracted text (as a string or list) and any associated non-text content, raising an error if the result indicates a failure.*


### convert_tool (method, L188-L209, parent: MCPClient)

> *Summary: Transforms an `MCPTool` instance into a standard `Tool` object suitable for use within the AutoGen framework. It wraps the tool's execution logic by creating an asynchronous callable that uses the provided `ClientSession` to invoke the underlying MCP service.*


### convert_resource (method, L213-L254, parent: MCPClient)

> *Summary: Creates a callable `Tool` object from a provided `ResourceTemplate`, which encapsulates logic to fetch and optionally save resources. It takes the template, an active session, and an optional download folder as input, returning a tool ready for execution that resolves to either resource data or a saved file path.*


### load_mcp_toolkit (method, L258-L286, parent: MCPClient)

> *Summary: This asynchronous method aggregates available tools and resources from a client session into an AG2 Toolkit object. It conditionally fetches and converts MCP tools and resource templates based on boolean flags, optionally downloading resources to a specified folder.*


### get_unsupported_reason (method, L289-L296, parent: MCPClient)

> *Summary: Checks if the required `mcp` library is available; returns an installation instruction string if the import fails, otherwise returns `None`.*


### MCPClientSessionManager (class, L299-L325)

> *Summary: Manages multiple active connections to an MCP server by providing an asynchronous context manager for session lifecycle. It accepts a configuration object and yields a fully initialized `ClientSession` while tracking it internally using the server name as a key.*


### __init__ (method, L304-L307, parent: MCPClientSessionManager)

> *Summary: Initializes a client session manager by setting up an asynchronous exit stack and creating an empty dictionary to hold active `ClientSession` instances keyed by their names.*


### open_session (method, L310-L325, parent: MCPClientSessionManager)

> *Summary: Establishes a new connection to an MCP server using provided configuration, initializes the resulting client session, stores it internally, and yields the active session for use.*


### create_toolkit (function, L329-L356)

> *Summary: This function constructs a `Toolkit` object by interacting with an MCP client session. It optionally creates a specified download directory and then loads the toolkit, controlling whether MCP tools and resources are included in the final output.*


### ResultSaved (class, L360-L364)

> *Summary: Represents the outcome of saving results, containing a textual explanation and the `Path` object pointing to where the data was stored. This structure is used to communicate successful persistence operations.*

