# test/beta/middleware/builtins/test_approval.py

10 function(s): make_context, tool_call, test_accepts_various_affirmative_inputs, test_denies_on_no, test_custom_message, test_custom_timeout, test_custom_denied_message, test_always_sets_bypass_flag, test_always_is_per_tool, test_always_ignored_when_disabled.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| make_context | function |  |
| tool_call | function |  |
| test_accepts_various_affirmative_inputs | function |  |
| test_denies_on_no | function |  |
| test_custom_message | function |  |
| test_custom_timeout | function |  |
| test_custom_denied_message | function |  |
| test_always_sets_bypass_flag | function |  |
| test_always_is_per_tool | function |  |
| test_always_ignored_when_disabled | function |  |

## Chunks

### make_context (function, L15-L22)

> *Summary: Creates a mock object representing request context by initializing it with an asynchronous input mock returning a specified response string and setting up optional variable storage. This function returns the configured `AsyncMock` instance for testing purposes.*


### tool_call (function, L26-L27)

> *Summary: Generates a `ToolCallEvent` object specifying the "calculator" tool with predefined arguments for inputs 'a' and 'b'. This simulates an outgoing request to invoke a specific external function.*


### test_accepts_various_affirmative_inputs (function, L32-L44)

> *Summary: This test verifies that the approval mechanism correctly accepts various affirmative inputs by simulating a successful tool call response. It asserts that the resulting event matches an expected `ToolResultEvent` after invoking the hook with mock context and next function.*


### test_denies_on_no (function, L48-L57)

> *Summary: This test verifies that a tool call is rejected when the approval status is "no". It simulates an incoming `ToolCallEvent` and asserts that the hook returns a specific denial result without executing the next middleware in the chain.*


### test_custom_message (function, L61-L73)

> *Summary: This test verifies that a custom approval message is correctly presented when an action requires user confirmation. It simulates the middleware hook being called with a specific `ToolCallEvent` and asserts that the underlying input mechanism was invoked with the expected formatted prompt.*


### test_custom_timeout (function, L77-L86)

> *Summary: This test verifies that a custom timeout is correctly applied when using the `approval_required` middleware. It asserts that the provided timeout value (60 seconds) is passed into the arguments of the underlying tool call context.*


### test_custom_denied_message (function, L90-L98)

> *Summary: This test verifies that a custom denial message is correctly returned when an approval hook rejects a tool call. It simulates the rejection process using `approval_required` and asserts the resulting event contains the specified "Rejected by user" message.*


### test_always_sets_bypass_flag (function, L102-L116)

> *Summary: This test verifies that an approval middleware configured to always allow bypass sets a specific flag after the first invocation. Subsequent calls using the same context will skip prompting and immediately proceed with the allowed result.*


### test_always_is_per_tool (function, L120-L131)

> *Summary: This test verifies that when `allow_always=True` is set for approval, a specific tool call results in an immediate success response (`ToolResultEvent`). It confirms that even with bypassing enabled, if the tool name isn't explicitly listed in the bypass configuration, the system still prompts for user input.*


### test_always_ignored_when_disabled (function, L135-L144)

> *Summary: When approval is disabled via `approval_required(allow_always=False)`, this test verifies that the hook immediately returns a denial result without executing the next middleware in the chain. It takes a `ToolCallEvent` as input and asserts the output matches a user-denied tool call result.*

