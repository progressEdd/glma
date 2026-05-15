# test/beta/config/gemini/test_tool_call_id.py

5 function(s): _part, _function_call, _response, client, context. 2 class(es): TestProcessResponseToolCallIds, TestProcessStreamToolCallIds. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _part | function |  |
| _function_call | function |  |
| _response | function |  |
| client | function |  |
| context | function |  |
| TestProcessResponseToolCallIds | class |  |
| TestProcessStreamToolCallIds | class |  |

## Chunks

### _part (function, L20-L26)

> *Summary: Constructs a data structure holding optional components like function calls, text content, and internal thought processes. It accepts these elements as keyword arguments and returns them packaged in a `SimpleNamespace` object.*


### _function_call (function, L29-L30)

> *Summary: Creates a structured object representing a function call by accepting the function's name, its arguments dictionary, and an optional function call ID. This object encapsulates all necessary details for subsequent processing or execution.*


### _response (function, L33-L43)

> *Summary: Constructs a mock response object containing candidate data derived from the input list of parts. This function wraps the provided `parts` into a structured output mimicking an API response structure.*


### client (function, L47-L49)

> *Summary: This function creates and returns a `GeminiClient` instance configured with the "gemini-2.5-flash" model and a hardcoded test API key, while mocking the underlying `genai.Client`.*


### context (function, L53-L54)

> *Summary: Creates and returns a `Context` object, initializing its stream attribute with an asynchronous mock for testing purposes.*


### TestProcessResponseToolCallIds (class, L58-L80)

> *Summary: This test suite verifies how the system handles tool call identification when processing responses from a `GeminiClient`. It asserts that parallel calls to the same tool receive unique IDs, and that explicitly provided provider IDs are correctly preserved in the resulting processed response.*


### test_parallel_calls_to_same_tool_get_unique_ids (method, L59-L71, parent: TestProcessResponseToolCallIds)

> *Summary: This test verifies that concurrent requests to the same tool without a provider ID generate distinct identifiers. It sends two parallel function calls and asserts that the resulting list of call IDs contains only unique values.*


### test_provider_supplied_id_is_preserved (method, L73-L80, parent: TestProcessResponseToolCallIds)

> *Summary: This test verifies that a tool call ID supplied by the provider is correctly preserved during response processing. It sends a mock response containing a specific function call ID and asserts that the resulting processed object retains that exact ID in its list of tool calls.*


### TestProcessStreamToolCallIds (class, L84-L109)

> *Summary: This test suite verifies the correct handling of tool call IDs when processing streamed responses from a Gemini client. It asserts that parallel calls to the same tool receive unique IDs and that provider-supplied IDs are accurately preserved in the final result.*


### test_parallel_calls_to_same_tool_get_unique_ids (method, L85-L97, parent: TestProcessStreamToolCallIds)

> *Summary: This test verifies that when multiple parallel calls are made to the same tool, each invocation receives a unique ID. It streams two distinct function call requests and asserts that all resulting tool call IDs in the response set are unique.*


### test_provider_supplied_id_is_preserved (method, L99-L109, parent: TestProcessStreamToolCallIds)

> *Summary: This test verifies that a tool call ID supplied by the provider is correctly preserved through the processing pipeline. It sends a request containing a specific `fc_id` and asserts that the resulting processed output retains that exact ID in its list of tool calls.*

