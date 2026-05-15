# test/beta/config/gemini/test_empty_text_parts.py

4 function(s): _candidate, _response, client, memory_context. 2 class(es): TestProcessStreamSkipsEmptyTextParts, TestProcessResponseSkipsEmptyTextParts. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _candidate | function |  |
| _response | function |  |
| client | function |  |
| memory_context | function |  |
| TestProcessStreamSkipsEmptyTextParts | class |  |
| TestProcessResponseSkipsEmptyTextParts | class |  |

## Chunks

### _candidate (function, L23-L28)

> *Summary: Constructs a basic response object containing the provided list of text parts. It initializes other fields like `finish_reason` and `grounding_metadata` to `None`.*


### _response (function, L31-L32)

> *Summary: Constructs a response object containing the provided list of candidates and sets the usage metadata to `None`. This helper function wraps candidate data into a standardized output structure.*


### client (function, L36-L38)

> *Summary: This function mocks the underlying `genai.Client` dependency and returns a configured instance of `GeminiClient`, specifically using the "gemini-2.5-flash" model with a test API key. It serves to provide a controlled, mocked client object for testing purposes.*


### memory_context (function, L42-L53)

> *Summary: Creates a testing context by initializing a `MemoryStream` and an empty list to capture events. It configures the stream to record all incoming `BaseEvent`s into the provided list before returning the necessary components for simulation.*


### TestProcessStreamSkipsEmptyTextParts (class, L57-L92)

> *Summary: This test suite verifies that the streaming processing logic correctly filters out empty text parts from model responses. It asserts that both message chunks and reasoning events are only recorded when they contain non-empty content.*


### test_empty_text_chunks_dropped (method, L58-L76, parent: TestProcessStreamSkipsEmptyTextParts)

> *Summary: This test verifies that empty text parts within a streamed response are correctly filtered out during processing. It feeds the client a sequence of chunks, including one with an empty string part, and asserts that only non-empty content is retained in the final message objects.*


### test_empty_thought_text_dropped (method, L78-L92, parent: TestProcessStreamSkipsEmptyTextParts)

> *Summary: This test verifies that empty text parts are ignored during stream processing. It feeds a sequence of message chunks containing both an empty and a non-empty "thought" part to the client and asserts that only the non-empty thought is captured in the resulting reasoning events.*


### TestProcessResponseSkipsEmptyTextParts (class, L96-L107)

> *Summary: This test verifies that processing a response containing an empty text part does not generate any `ModelMessage` events. It simulates receiving a candidate with an empty text part and asserts the resulting event stream remains empty of model messages.*


### test_empty_text_part_does_not_emit_model_message (method, L97-L107, parent: TestProcessResponseSkipsEmptyTextParts)

> *Summary: When processing a response containing an empty text part from the model, this test asserts that no `ModelMessage` events are emitted. It uses a mock client and context to verify this behavior during message processing.*

