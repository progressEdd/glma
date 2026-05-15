# autogen/beta/tools/builtin/mcp_server.py

2 class(es): MCPServerToolSchema, MCPServerTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MCPServerToolSchema | class |  |
| MCPServerTool | class |  |

## Chunks

### MCPServerToolSchema (class, L21-L29)

> *Summary: Defines the structure for an MCP server tool by specifying required parameters like `server_url`, optional authentication tokens and headers, and lists of allowed or blocked internal tools. This schema dictates how a tool connecting to an external Minecraft Protocol (MCP) server should be configured.*


### MCPServerTool (class, L32-L82)

> *Summary: This class defines a tool for interacting with an MCP server, initialized with connection details like URL and label, along with optional configuration such as authorization tokens or allowed tools. It provides methods to generate schemas based on the provided parameters and registers itself to handle specific tool call events within a given execution context.*


### __init__ (method, L38-L64, parent: MCPServerTool)

> *Summary: Initializes a server tool by accepting configuration parameters such as the server URL, label, and optional authentication or filtering settings. It stores these inputs internally in a dictionary for later use when interacting with the defined external service.*


### schemas (method, L66-L68, parent: MCPServerTool)

> *Summary: Generates a list of `MCPServerToolSchema` objects by resolving all internal parameters against the provided execution context. This method transforms stored parameter definitions into structured schema representations suitable for tool definition.*


### register (method, L70-L82, parent: MCPServerTool)

> *Summary: This method sets up event filtering within a provided stack to intercept specific tool call events named `MCP_SERVER_TOOL_NAME`. It registers an asynchronous execution handler that will be invoked when the targeted event occurs.*

