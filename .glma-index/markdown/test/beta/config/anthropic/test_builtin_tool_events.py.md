# test/beta/config/anthropic/test_builtin_tool_events.py

2 function(s): _process, test_process_response_routes_all_block_types. 1 class(es): TestResultParts. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _process | function |  |
| test_process_response_routes_all_block_types | function |  |
| TestResultParts | class |  |

## Chunks

### _process (function, L61-L75)

> *Summary: This asynchronous function simulates processing a message by initializing an Anthropic client and constructing a `Message` object from the input iterable. It then uses the client to process this message against a memory stream context, returning the resulting model response along with any captured events.*


### test_process_response_routes_all_block_types (function, L79-L130)

> *Summary: This test verifies the system's ability to correctly process a sequence of mixed block types, including text, server tool calls, and their corresponding results. It asserts that the final response reflects the initial text while capturing all emitted events for web search, bash execution (including an error), and a user-defined tool call.*


### TestResultParts (class, L134-L491)

> *Summary: This class contains multiple asynchronous test methods that verify the correct event generation when processing tool use calls and their corresponding results for various tools (web search, web fetch, code execution, text editor). It asserts that input blocks correctly translate into specific `AnthropicServerToolCallEvent` and `AnthropicServerToolResultEvent` structures based on success or error scenarios.*


### test_web_search_success_url_inputs (method, L135-L161, parent: TestResultParts)

> *Summary: This test verifies that processing a tool call request and subsequent search results correctly generates specific Anthropic server events. It asserts the output contains both the initial tool invocation event and the final result event containing structured URL inputs derived from the provided search hits.*


### test_web_search_error_text_input (method, L163-L185, parent: TestResultParts)

> *Summary: This test verifies the system's response when a web search tool returns an error. It simulates sending a tool call followed by an error result and asserts that the processing yields specific `AnthropicServerToolCallEvent` and `AnthropicServerToolResultEvent` objects containing the error details.*


### test_web_fetch_pdf_binary_input (method, L187-L208, parent: TestResultParts)

> *Summary: This test verifies the event generation when a web fetch tool is used with binary PDF input. It simulates processing a tool call and its corresponding result to assert that the correct `ServerToolCallEvent` and `ServerToolResultEvent` are emitted, correctly packaging the URL and binary data.*


### test_web_fetch_plain_text_input (method, L210-L231, parent: TestResultParts)

> *Summary: This test verifies the event generation when processing a server tool call and its corresponding result. It simulates fetching plain text from a web source and asserts that the system emits both a `ServerToolCallEvent` and a subsequent `ServerToolResultEvent`.*


### test_web_fetch_error_text_input (method, L233-L255, parent: TestResultParts)

> *Summary: This test verifies the event stream generated when a `web_fetch` tool call fails with a specific error. It asserts that processing the initial tool use request followed by an error result produces both a `ServerToolCallEvent` and a subsequent `ServerToolResultEvent` containing structured error details in the input text.*


### test_code_execution_success_emits_stdout_and_files (method, L257-L279, parent: TestResultParts)

> *Summary: This test verifies that successful code execution results in specific events being emitted. It simulates a tool call and its corresponding result containing standard output and file outputs, asserting the resulting event stream matches expected `AnthropicServerToolCallEvent` and `AnthropicServerToolResultEvent`.*


### test_code_execution_encrypted_emits_files_only (method, L281-L306, parent: TestResultParts)

> *Summary: This test verifies that processing a code execution tool call followed by an encrypted result emits specific events. It asserts the sequence includes both the initial server tool call event and the subsequent server tool result event containing file ID information.*


### test_code_execution_error_text_input (method, L308-L330, parent: TestResultParts)

> *Summary: This test verifies that processing a tool call followed by an error result correctly generates specific Anthropic events. It asserts the sequence includes both a `ServerToolCallEvent` and a subsequent `ServerToolResultEvent` containing the error details as text input.*


### test_bash_code_execution_success (method, L332-L357, parent: TestResultParts)

> *Summary: This test verifies the expected sequence of events when a successful bash code execution tool call is processed. It simulates sending a tool use request and receiving a result with stdout, stderr, and a zero return code to assert the resulting stream of `ToolCallEvent` and `ToolResultEvent`.*


### test_bash_code_execution_error (method, L359-L381, parent: TestResultParts)

> *Summary: This test verifies the event stream generated when a server tool execution fails. It simulates sending a tool call followed by an error result and asserts that the system emits both a `ServerToolCallEvent` and a subsequent `ServerToolResultEvent` containing the specific error details.*


### test_text_editor_view_returns_content_text (method, L383-L410, parent: TestResultParts)

> *Summary: This test verifies that processing a tool call and its corresponding result generates the correct sequence of events. It asserts that an `AnthropicServerToolCallEvent` is followed by an `AnthropicServerToolResultEvent`, correctly packaging the provided text content and metadata within the result event.*


### test_text_editor_create_empty_parts (method, L412-L431, parent: TestResultParts)

> *Summary: This test verifies the event stream generated when a server tool call for text editor code execution is immediately followed by its result. It asserts that the processing yields both a `ServerToolCallEvent` and a corresponding `ServerToolResultEvent`.*


### test_text_editor_str_replace_lines_text (method, L433-L460, parent: TestResultParts)

> *Summary: This test verifies the event stream generated when a text editor string replacement tool is called and subsequently returns a result. It asserts that the processing yields both a `ServerToolCallEvent` for the initial request and a corresponding `ServerToolResultEvent` containing the replacement details.*


### test_text_editor_error_text_input (method, L462-L491, parent: TestResultParts)

> *Summary: This test verifies that when a text editor tool execution returns an error result, the system correctly emits both a tool call event and a subsequent tool result event containing the detailed error information. It simulates processing a tool use block followed by a corresponding error result block to assert the resulting stream of events.*

