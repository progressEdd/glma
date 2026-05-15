# test/a2a/chats/test_streaming.py

6 function(s): _make_request, _collect_responses, test_streaming_chunks_emitted, test_non_streaming_unchanged, test_streaming_through_executor, test_streaming_with_tool_calls.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_request | function |  |
| _collect_responses | function |  |
| test_streaming_chunks_emitted | function |  |
| test_non_streaming_unchanged | function |  |
| test_streaming_through_executor | function |  |
| test_streaming_with_tool_calls | function |  |

## Chunks

### _make_request (function, L34-L35)

> *Summary: Constructs a `RequestMessage` object containing a single user message with the provided text as content. It defaults to sending "Say hi" if no text is supplied.*


### _collect_responses (function, L38-L42)

> *Summary: This asynchronous function consumes a stream of `ServiceResponse` objects yielded by an `AgentService` given a `RequestMessage`. It aggregates all received responses into a list and returns that complete collection.*


### test_streaming_chunks_emitted (function, L46-L74)

> *Summary: This test verifies that an agent correctly yields streaming text chunks when its reply mechanism is mocked to emit sequential `StreamEvent`s. It asserts that the collected responses contain both the concatenated stream of individual chunks and a final complete message object.*


### test_non_streaming_unchanged (function, L78-L92)

> *Summary: This test verifies that when an agent produces no streaming events, the service returns a single non-streamed response containing the expected initial message content. It asserts that zero responses have `streaming_text` and exactly one response has a standard `message`.*


### test_streaming_through_executor (function, L96-L168)

> *Summary: This test verifies that streaming replies from an agent are correctly emitted as `TaskArtifactUpdateEvent`s rather than `TaskStatusUpdateEvent`s when executed through an executor. It mocks a streaming response, runs the execution, collects all resulting events, and asserts that multiple artifact updates were generated with correct chunking flags, alongside exactly one initial working status event.*


### test_streaming_with_tool_calls (function, L172-L218)

> *Summary: This test verifies that an agent correctly handles a sequence involving both a non-streaming tool call followed by streaming text output. It mocks the LLM response to first return a tool call structure and then stream subsequent content chunks, asserting that both streamed data and message history are captured as expected.*

