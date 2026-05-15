# test/beta/config/anthropic/tools/test_mcp_server.py

6 function(s): test_defaults, test_extract_mcp_servers_defaults, test_with_auth_token, test_allowed_tools, test_blocked_tools, test_extract_mcp_servers_skips_non_mcp.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_defaults | function |  |
| test_extract_mcp_servers_defaults | function |  |
| test_with_auth_token | function |  |
| test_allowed_tools | function |  |
| test_blocked_tools | function |  |
| test_extract_mcp_servers_skips_non_mcp | function |  |

## Chunks

### test_defaults (function, L14-L22)

> *Summary: This test verifies that the `MCPServerTool` correctly generates a specific API schema when provided with a context. It asserts that the resulting structure matches an expected dictionary format containing the toolset type and server name.*


### test_extract_mcp_servers_defaults (function, L26-L37)

> *Summary: This test verifies that the `extract_mcp_servers` function correctly parses server configuration from a tool instance. It takes a context, calls the tool to retrieve schemas, and asserts the output matches the expected list of structured server definitions.*


### test_with_auth_token (function, L41-L57)

> *Summary: This test verifies that an `MCPServerTool` correctly exposes its configuration when initialized with an authorization token. It calls the tool's schema retrieval method and asserts that the resulting list of schemas accurately reflects the provided server URL, label, and authentication token.*


### test_allowed_tools (function, L61-L78)

> *Summary: This test verifies that an `MCPServerTool` correctly generates a specific API schema based on its configuration. It asserts the output structure matches expectations, confirming which tools are enabled for the defined server.*


### test_blocked_tools (function, L82-L97)

> *Summary: This test verifies that a tool configured to block specific functions correctly exposes its schema. It asserts the resulting API structure shows the blocked tool (`delete_all`) is disabled within the configuration.*


### test_extract_mcp_servers_skips_non_mcp (function, L101-L111)

> *Summary: This test verifies that a server extraction function correctly identifies only the MCP server schema from a list containing both an MCP and a WebSearch tool schema. It asserts that the output contains exactly one entry corresponding to the configured MCP server.*

