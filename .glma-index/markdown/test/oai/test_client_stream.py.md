# test/oai/test_client_stream.py

8 function(s): test_completion_stream, test_chat_completion_stream, test__update_dict_from_chunk, test__update_function_call_from_chunk, test__update_tool_calls_from_chunk, test__update_tool_calls_from_chunk_repeated_type, test_chat_functions_stream, test_chat_tools_stream.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_completion_stream | function |  |
| test_chat_completion_stream | function |  |
| test__update_dict_from_chunk | function |  |
| test__update_function_call_from_chunk | function |  |
| test__update_tool_calls_from_chunk | function |  |
| test__update_tool_calls_from_chunk_repeated_type | function |  |
| test_chat_functions_stream | function |  |
| test_chat_tools_stream | function |  |

## Chunks

### test_completion_stream (function, L31-L36)

> *Summary: This test verifies streaming behavior by initializing an OpenAI client with provided credentials and sending a simple prompt to generate a response. It then prints the raw streamed response object and extracts the final text completion from it.*


### test_chat_completion_stream (function, L41-L45)

> *Summary: This test verifies streaming chat completion by initializing an OpenAI client with provided credentials and sending a simple user prompt. It then prints the raw streamed response object and extracts the final text content from it for assertion.*


### test__update_dict_from_chunk (function, L49-L79)

> *Summary: This test verifies that the `_update_dict_from_chunk` method correctly updates a dictionary from attributes on a mock object. It asserts that non-primitive types raise an error and demonstrates sequential string concatenation for updating existing keys.*


### test__update_function_call_from_chunk (function, L84-L112)

> *Summary: This test verifies that a stream of partial `ChoiceDeltaFunctionCall` chunks can be correctly aggregated into a complete function call object. It iterates through predefined chunks, updating the state with each one to assert the final structure and token count match expectations.*


### test__update_tool_calls_from_chunk (function, L117-L185)

> *Summary: This test verifies the logic for aggregating partial tool call updates received in chunks. It iterates over a list of `ChoiceDeltaToolCall` objects, feeding each chunk sequentially into an update function to build complete tool calls and track token counts. The final state of the aggregated tool calls and total tokens is then asserted or used to construct a message object.*


### test__update_tool_calls_from_chunk_repeated_type (function, L189-L219)

> *Summary: This test verifies that when processing streamed chunks, the `type` field of a tool call remains correctly as `"function"` even if multiple chunks are received. It simulates receiving three sequential chunks and asserts the final assembled tool call has the correct type and arguments.*


### test_chat_functions_stream (function, L227-L251)

> *Summary: This test verifies streaming behavior when calling an OpenAI-like API with defined functions. It sends a user query requesting weather information and asserts that the streamed response can be fully extracted into text or a completion object.*


### test_chat_tools_stream (function, L259-L296)

> *Summary: This test verifies the streaming behavior when a model is prompted with a request requiring tool use. It sends a user query along with a defined weather function and asserts that the streamed response contains at least one tool call.*

