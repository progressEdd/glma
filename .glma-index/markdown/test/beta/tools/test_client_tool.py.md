# test/beta/tools/test_client_tool.py

6 function(s): client_tool, test_client_tool_condition, test_client_tool_call_returns_client_tool_call, test_client_tool_register_execute_sends_to_stream, test_client_tool_register_with_middleware, test_function_tool_with_middleware_preserves_existing.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| client_tool | function |  |
| test_client_tool_condition | function |  |
| test_client_tool_call_returns_client_tool_call | function |  |
| test_client_tool_register_execute_sends_to_stream | function |  |
| test_client_tool_register_with_middleware | function |  |
| test_function_tool_with_middleware_preserves_existing | function |  |

## Chunks

### client_tool (function, L19-L20)

> *Summary: This function constructs and returns a `ClientTool` instance, initializing it with a specific schema defining a tool named "my\_client\_tool". This setup makes the defined client tool available for use.*


### test_client_tool_condition (function, L23-L26)

> *Summary: This test verifies that a specific condition correctly identifies `ClientToolCallEvent` instances with an ID of "1" while rejecting standard `ToolCallEvent` instances, even if they share the same ID and name. It asserts the boolean outcome for both event types against the defined predicate.*


### test_client_tool_call_returns_client_tool_call (function, L30-L37)

> *Summary: This test verifies that invoking a `ClientTool` with a `ToolCallEvent` returns a `ClientToolCallEvent`. It asserts that the returned event correctly wraps and mirrors the name and ID of the initial input call.*


### test_client_tool_register_execute_sends_to_stream (function, L41-L60)

> *Summary: This test verifies that the execution closure within a registered tool correctly sends a `ClientToolCallEvent` to the stream. It registers a client tool, manually sends an event via a memory stream context, and asserts that the final recorded event matches the sent call details.*


### test_client_tool_register_with_middleware (function, L64-L84)

> *Summary: This test verifies that a custom middleware intercepts and modifies the output of a registered client tool execution. It registers a `TagMiddleware` with a `ClientTool`, sends a tool call event, and asserts that the final received event has been tagged by the middleware.*


### test_function_tool_with_middleware_preserves_existing (function, L88-L126)

> *Summary: This test verifies that applying a second middleware layer to an existing tool correctly appends the new middleware without overwriting previous ones. It asserts that when executed, the execution order reflects all registered middlewares and the core tool logic in sequence.*

