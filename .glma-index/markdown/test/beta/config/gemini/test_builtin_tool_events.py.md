# test/beta/config/gemini/test_builtin_tool_events.py

4 function(s): _candidate, _response, client, memory_context. 7 class(es): TestFactoryFromExecutableCode, TestFactoryFromCodeExecutionResult, TestFactoryFromGrounding, TestGroundingToolName, TestProcessResponseEmitsBuiltinEvents, TestProcessStreamEmitsBuiltinEvents, TestResultParts. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _candidate | function |  |
| _response | function |  |
| client | function |  |
| memory_context | function |  |
| TestFactoryFromExecutableCode | class |  |
| TestFactoryFromCodeExecutionResult | class |  |
| TestFactoryFromGrounding | class |  |
| TestGroundingToolName | class |  |
| TestProcessResponseEmitsBuiltinEvents | class |  |
| TestProcessStreamEmitsBuiltinEvents | class |  |
| TestResultParts | class |  |

## Chunks

### _candidate (function, L24-L29)

> *Summary: Constructs a `SimpleNamespace` object representing a candidate response. It takes a list of content parts and optional grounding metadata as input to structure the output.*


### _response (function, L32-L33)

> *Summary: This helper function constructs a response object by wrapping the provided list of candidates. It initializes the `usage_metadata` field to `None`.*


### client (function, L37-L39)

> *Summary: This function creates and returns a configured `GeminiClient` instance, using a mocked version of the underlying Google AI client for testing purposes. It initializes the client with the "gemini-2.5-flash" model and a placeholder API key.*


### memory_context (function, L43-L45)

> *Summary: This function initializes and returns a `Context` object containing a new `MemoryStream`, along with the stream itself. It sets up the necessary context for tracking memory within a test environment.*


### TestFactoryFromExecutableCode (class, L48-L62)

> *Summary: This test verifies that a specific factory method correctly generates a `GeminiServerToolCallEvent` when provided with executable code within a `types.Part`. It also asserts that the method returns `None` if the input part does not contain executable code.*


### test_returns_event_for_executable_code_part (method, L49-L59, parent: TestFactoryFromExecutableCode)

> *Summary: This test verifies that providing a part containing executable code results in the correct `GeminiServerToolCallEvent`. It asserts that the generated event accurately reflects the input code and language within its arguments.*


### test_returns_none_for_non_code_part (method, L61-L62, parent: TestFactoryFromExecutableCode)

> *Summary: Asserts that attempting to create a `GeminiServerToolCallEvent` from a text-only part, which lacks executable code, results in a `None` return value. This verifies the event parsing logic correctly handles non-code content.*


### TestFactoryFromCodeExecutionResult (class, L65-L79)

> *Summary: This test verifies that a factory method correctly constructs a `GeminiServerToolResultEvent` when provided with a code execution result part, and returns `None` if the input part does not contain a code execution result. It ensures the resulting event accurately reflects the outcome and output from the provided execution data.*


### test_returns_event_for_result_part (method, L66-L76, parent: TestFactoryFromCodeExecutionResult)

> *Summary: This test verifies that a `GeminiServerToolResultEvent` is correctly constructed from a code execution result part. It asserts the resulting event matches an expected structure containing the input output and outcome metadata.*


### test_returns_none_for_non_result_part (method, L78-L79, parent: TestFactoryFromCodeExecutionResult)

> *Summary: Verifies that attempting to create a `GeminiServerToolResultEvent` from a non-result part, like a simple text part, returns `None`. This confirms the event constructor correctly handles inputs that do not represent execution results.*


### TestFactoryFromGrounding (class, L82-L105)

> *Summary: This test suite verifies the correct construction of `GeminiServerToolCallEvent` and `GeminiServerToolResultEvent` from grounding metadata. It ensures that tool call events correctly embed search queries in arguments, while result events link back to a parent call ID.*


### test_call_carries_queries_in_arguments (method, L83-L93, parent: TestFactoryFromGrounding)

> *Summary: This test verifies that a `GeminiServerToolCallEvent` correctly encapsulates web search queries when created from grounding metadata. It asserts the resulting event's arguments string matches the expected JSON structure containing the input queries.*


### test_result_links_to_call_via_parent_id (method, L95-L105, parent: TestFactoryFromGrounding)

> *Summary: This test verifies that a `GeminiServerToolResultEvent` correctly constructs itself when initialized from grounding metadata and a parent ID. It asserts the resulting event matches an expected instance containing the provided metadata and identifiers.*


### TestGroundingToolName (class, L108-L117)

> *Summary: This test verifies the `grounding_tool_name` function's behavior based on input metadata. It asserts that if web search queries are present in the `GroundingMetadata`, it returns the `WEB_SEARCH_TOOL_NAME`; otherwise, it returns the `WEB_FETCH_TOOL_NAME`.*


### test_web_search_when_queries_present (method, L109-L112, parent: TestGroundingToolName)

> *Summary: This test verifies that when `GroundingMetadata` is initialized with web search queries, the associated tool name correctly resolves to the predefined web search constant. It asserts that the function returns the expected tool identifier given the input metadata containing a query like "bitcoin".*


### test_web_fetch_when_no_queries (method, L114-L117, parent: TestGroundingToolName)

> *Summary: Verifies that the `grounding_tool_name` function correctly identifies the web fetch tool when provided with an empty `GroundingMetadata` object. It asserts that the returned name matches the predefined constant for the web fetch tool.*


### TestProcessResponseEmitsBuiltinEvents (class, L121-L199)

> *Summary: These tests verify that processing specific response types correctly emits corresponding built-in tool events to the stream history. It asserts that code execution results generate both a `GeminiServerToolCallEvent` and a subsequent `GeminiServerToolResultEvent`, while grounding metadata triggers web search or web fetch tool calls.*


### test_code_execution_pair (method, L122-L147, parent: TestProcessResponseEmitsBuiltinEvents)

> *Summary: This test verifies the event stream generated when a code execution request and its result are processed by the client. It asserts that the history contains a sequence of `GeminiServerToolCallEvent` followed by a corresponding `GeminiServerToolResultEvent`.*


### test_grounding_synthesises_call_result_pair (method, L149-L173, parent: TestProcessResponseEmitsBuiltinEvents)

> *Summary: This test verifies that processing a response containing grounding metadata triggers specific tool call and result events in the stream history. It asserts that the sequence of events correctly reflects a web search tool invocation with predefined queries and subsequent result reporting.*


### test_url_context_uses_web_fetch_name (method, L175-L199, parent: TestProcessResponseEmitsBuiltinEvents)

> *Summary: This test verifies that when processing a response containing a URL context, the client correctly emits a sequence of tool events. It asserts that the emitted events include a `GeminiServerToolCallEvent` followed by a corresponding `GeminiServerToolResultEvent`, both using the predefined web fetch tool name.*


### TestProcessStreamEmitsBuiltinEvents (class, L203-L261)

> *Summary: This test suite verifies that the processing stream emits specific built-in tool events when handling code execution and grounding metadata. It asserts that a pair of `GeminiServerToolCallEvent` and `GeminiServerToolResultEvent` are emitted for both code execution and web search operations, ensuring correct event sequencing and data inclusion.*


### test_code_execution_pair_across_chunks (method, L204-L232, parent: TestProcessStreamEmitsBuiltinEvents)

> *Summary: This test verifies the end-to-end flow of code execution by streaming a request containing executable code followed by its expected result to a Gemini client. It asserts that the resulting event stream correctly contains both a `GeminiServerToolCallEvent` for the input and a corresponding `GeminiServerToolResultEvent` for the output.*


### test_grounding_emitted_once_after_stream_completes (method, L234-L261, parent: TestProcessStreamEmitsBuiltinEvents)

> *Summary: This test verifies that a grounding event is emitted exactly once after a streaming response completes. It simulates sending streamed chunks containing specific content and asserts the resulting history contains one tool call followed by one tool result event, both carrying the expected grounding metadata.*


### TestResultParts (class, L265-L372)

> *Summary: These asynchronous test methods verify how the system processes and emits events for various tool interactions with a Gemini client. They simulate responses containing code execution results or grounding metadata (like web search inputs/outputs) to assert that the correct sequence of `ToolCallEvent` and `ToolResultEvent` are recorded in the stream history.*


### test_code_execution_result_emits_output_text (method, L266-L290, parent: TestResultParts)

> *Summary: This test verifies that processing a response containing both executable code and its result correctly emits two sequential events: a `GeminiServerToolCallEvent` for the execution request and a subsequent `GeminiServerToolResultEvent` detailing the output. It uses a mock client and memory context to assert the exact sequence of emitted tool events.*


### test_code_execution_result_no_output_empty_parts (method, L292-L316, parent: TestResultParts)

> *Summary: This test verifies the event stream generated when a code execution tool is called with no output. It sends a request containing executable code and an empty result, then asserts that the history contains sequential `GeminiServerToolCallEvent` followed by a `GeminiServerToolResultEvent`.*


### test_grounding_emits_url_inputs_per_chunk (method, L318-L345, parent: TestResultParts)

> *Summary: This test verifies that when a grounding chunk containing a URL is processed, the system emits both a tool call event requesting web search queries and a subsequent tool result event providing the specific URL input. It asserts the sequence of these events matches the expected structure using provided client and memory context objects.*


### test_grounding_url_context_no_chunks_empty_parts (method, L347-L372, parent: TestResultParts)

> *Summary: This test verifies the event sequence when a response contains only URL context without any grounding chunks. It asserts that processing a response with an empty query list triggers both a `GeminiServerToolCallEvent` and a subsequent `GeminiServerToolResultEvent` for the web fetch tool, while maintaining the provided grounding metadata.*

