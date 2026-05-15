# test/beta/tools/test_executor_builtin_passthrough.py

1 function(s): _not_found_events. 1 class(es): TestToolNotFoundFallback. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _not_found_events | function |  |
| TestToolNotFoundFallback | class |  |

## Chunks

### _not_found_events (function, L19-L20)

> *Summary: Filters a list of incoming events to return only those instances specifically typed as `ToolNotFoundEvent`. This function takes an event list and outputs a filtered list containing only the relevant not-found notifications.*


### TestToolNotFoundFallback (class, L24-L54)

> *Summary: This class tests the fallback mechanism for unknown tools within a `ToolExecutor`. It verifies that calling an unregistered tool triggers a `ToolNotFoundEvent`, while calling a known tool results in no such event being emitted.*


### test_regular_unknown_tool_triggers_not_found (method, L27-L44, parent: TestToolNotFoundFallback)

> *Summary: This test verifies that when a `ToolExecutor` receives a call for an unregistered tool, it correctly emits a `ToolNotFoundEvent`. It simulates sending an unknown tool call and asserts the resulting event stream contains the expected error notification.*


### test_regular_known_tool_is_skipped (method, L46-L54, parent: TestToolNotFoundFallback)

> *Summary: This test verifies that a registered tool executor correctly skips processing for known tools when provided with a `ToolCallEvent`. It asserts that no "not found" events are generated after sending a call to the predefined `"known_func"`.*

