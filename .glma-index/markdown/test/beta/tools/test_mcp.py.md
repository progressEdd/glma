# test/beta/tools/test_mcp.py

6 function(s): patch_mcp_session, test_tool_registered_from_http_mcp_server, test_tool_registered_from_stdio_mcp_server, test_allowed_and_blocked_tools_are_filtered, test_mcp_tool_result_is_returned_to_agent, test_extract_maps_content_blocks_to_typed_inputs. 1 class(es): _FakeMCPSession. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| patch_mcp_session | function |  |
| test_tool_registered_from_http_mcp_server | function |  |
| test_tool_registered_from_stdio_mcp_server | function |  |
| test_allowed_and_blocked_tools_are_filtered | function |  |
| test_mcp_tool_result_is_returned_to_agent | function |  |
| test_extract_maps_content_blocks_to_typed_inputs | function |  |
| _FakeMCPSession | class |  |

## Chunks

### patch_mcp_session (function, L36-L52)

> *Summary: This function returns a patcher that replaces the `_mcp_session` attribute in a module with a controllable mock session factory. It accepts tools and optional call results to construct and return a specific `MCPSessionPatch` object upon execution.*


### test_tool_registered_from_http_mcp_server (function, L56-L87)

> *Summary: This test verifies that a tool registered via an `MCPSessionPatch` is correctly exposed by an HTTP MCP server. It asserts that the retrieved schema accurately reflects the defined function name, description, and input parameters.*


### test_tool_registered_from_stdio_mcp_server (function, L91-L112)

> *Summary: This test verifies that a tool registered via an MCP server configured to use standard I/O is correctly exposed in the schemas. It asserts that the resulting schema contains the expected function name and description for the registered "ping" tool.*


### test_allowed_and_blocked_tools_are_filtered (function, L116-L135)

> *Summary: This test verifies that a server correctly filters available tools based on explicit allow and block lists provided in its configuration. It asserts that only the "keep" tool is present when both an allowed and blocked tool are configured.*


### test_mcp_tool_result_is_returned_to_agent (function, L139-L160)

> *Summary: This test verifies that a tool's execution result is correctly relayed back to the agent. It simulates an agent calling an "echo" tool and asserts that the final response from the agent indicates completion, while also confirming the tool call was recorded in the session.*


### test_extract_maps_content_blocks_to_typed_inputs (function, L164-L230)

> *Summary: This test verifies that various MCP content block types (text, image, audio, resource link, embedded resources) are correctly mapped to their corresponding typed input structures when processed by the server proxy. It simulates a tool call with mixed content and asserts the resulting list of structured inputs matches expectations.*


### _FakeMCPSession (class, L233-L253)

> *Summary: This class simulates an in-memory session for testing MCP interactions. It accepts a list of tools and optional predefined call results, allowing it to record tool calls made during execution while returning mock responses based on the provided configuration.*


### __init__ (method, L236-L243, parent: _FakeMCPSession)

> *Summary: Initializes the object by storing a list of `MCPTool` instances and an optional dictionary of previous tool call results. It also initializes an empty list to track subsequent calls made during its operation.*


### list_tools (method, L245-L246, parent: _FakeMCPSession)

> *Summary: Retrieves all available tools from the instance's internal storage and wraps them into a `ListToolsResult` object for output.*


### call_tool (method, L248-L253, parent: _FakeMCPSession)

> *Summary: Records the tool call details and immediately returns a predefined success result if no specific result for the given name is cached; otherwise, it retrieves the stored result.*

