# test/oai/test_openai_streaming_structured_output.py

6 class(es): TestAddStreamingUsageToParams, TestStructuredOutputDisablesStreaming, TestStreamingCapturesUsage, TestStreamingHandlesInvalidChunks, SimpleResponse, TestStreamingStructuredOutputIntegration. 23 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestAddStreamingUsageToParams | class |  |
| TestStructuredOutputDisablesStreaming | class |  |
| TestStreamingCapturesUsage | class |  |
| TestStreamingHandlesInvalidChunks | class |  |
| SimpleResponse | class |  |
| TestStreamingStructuredOutputIntegration | class |  |

## Chunks

### TestAddStreamingUsageToParams (class, L32-L79)

> *Summary: This test suite verifies the behavior of a static method that modifies request parameters based on streaming status. It asserts that `include_usage` is added to `stream_options` only when `stream=True`, while ensuring no modifications occur if streaming is false or absent, and preserving existing options otherwise.*


### test_adds_stream_options_when_streaming (method, L35-L41, parent: TestAddStreamingUsageToParams)

> *Summary: When streaming is enabled for an OpenAI request, this test verifies that the `stream_options` dictionary is correctly added to the parameters and specifically sets `include_usage` to `True`. It takes a parameter dictionary as input and asserts the resulting structure contains these specific stream options.*


### test_does_not_modify_when_not_streaming (method, L43-L48, parent: TestAddStreamingUsageToParams)

> *Summary: This test verifies that the input parameters remain unmodified when streaming is disabled. It asserts that no `stream_options` key is added to the parameter dictionary after calling a function designed to handle streaming usage.*


### test_does_not_modify_when_stream_not_present (method, L50-L55, parent: TestAddStreamingUsageToParams)

> *Summary: This test verifies that the `_add_streaming_usage_to_params` method does not alter input parameters when no streaming configuration is provided. It asserts that the resulting parameter dictionary remains unchanged, specifically lacking a `"stream_options"` key.*


### test_preserves_existing_stream_options (method, L57-L67, parent: TestAddStreamingUsageToParams)

> *Summary: This test verifies that custom stream options provided during an API call are correctly preserved after internal usage tracking is added to the request parameters. It asserts that a specific option from the input dictionary remains unchanged and that `include_usage` is set to `True`.*


### test_does_not_override_existing_include_usage (method, L69-L79, parent: TestAddStreamingUsageToParams)

> *Summary: This test verifies that a specific parameter within the request configuration remains unchanged when an internal function attempts to set a default value. It asserts that `include_usage` stays as `False` even after calling a method designed to add streaming usage information.*


### TestStructuredOutputDisablesStreaming (class, L83-L158)

> *Summary: This test suite verifies that when structured output is requested via the `response_format` parameter, any explicit streaming requests (`stream=True`) are automatically disabled during the API call. It uses mocked OpenAI clients to assert that the underlying client method is called without the `stream` or `stream_options` arguments present in the input parameters.*


### mock_oai_client (method, L87-L112, parent: TestStructuredOutputDisablesStreaming)

> *Summary: This method constructs a mocked OpenAI client instance configured to simulate a successful chat completion response. It sets up the mock so that calling `chat.completions.create()` returns a predefined `ChatCompletion` object containing structured JSON content in its message.*


### test_structured_output_removes_stream_param (method, L114-L139, parent: TestStructuredOutputDisablesStreaming)

> *Summary: This test verifies that when a structured output schema is provided via `response_format`, the underlying API call automatically disables streaming and removes any associated stream options from the request parameters. It achieves this by calling the client's create method with both `stream: True` and a defined JSON schema, then asserting those streaming parameters are absent in the mock call arguments.*


### test_structured_output_via_params_removes_stream (method, L141-L158, parent: TestStructuredOutputDisablesStreaming)

> *Summary: When a request includes `response_format` parameters, this test verifies that the underlying API client is called without streaming enabled, even if `stream: True` was initially passed. It asserts that both `"stream"` and `"stream_options"` are absent from the final arguments sent to the mock OpenAI client.*


### TestStreamingCapturesUsage (class, L162-L289)

> *Summary: This test suite verifies how a client accumulates usage statistics from the final chunk of an OpenAI streaming response. It mocks the OpenAI API to simulate content and usage chunks, asserting that the resulting object correctly aggregates token counts and reconstructs the full message content.*


### mock_oai_client (method, L166-L171, parent: TestStreamingCapturesUsage)

> *Summary: This method constructs and returns a `MagicMock` object simulating an OpenAI client instance. It configures this mock to represent the necessary structure for handling streaming chat completions responses.*


### _create_content_chunk (method, L173-L189, parent: TestStreamingCapturesUsage)

> *Summary: Constructs a `ChatCompletionChunk` object representing a segment of streamed content. It takes identifiers, model name, creation time, and the actual text content as inputs to build the chunk structure.*


### _create_final_chunk_with_finish_reason (method, L191-L207, parent: TestStreamingCapturesUsage)

> *Summary: Constructs the final chunk object for a streaming response by packaging it with a `finish_reason` set to "stop". It takes identifiers like the chunk ID, model name, and creation timestamp as inputs to build the complete output structure.*


### _create_usage_chunk (method, L209-L224, parent: TestStreamingCapturesUsage)

> *Summary: Constructs a `ChatCompletionChunk` object specifically for streaming responses that contains usage statistics but no choice data. It accepts identifiers, model name, creation timestamp, and token counts for the prompt and completion.*


### test_usage_captured_from_last_chunk (method, L226-L260, parent: TestStreamingCapturesUsage)

> *Summary: This test simulates an OpenAI streaming API call by providing a sequence of mock chunks, including a final usage chunk. It verifies that the resulting client response correctly aggregates and exposes the token counts (prompt, completion, total) from the last received chunk, alongside the fully assembled content.*


### test_stream_options_added_to_params (method, L262-L289, parent: TestStreamingCapturesUsage)

> *Summary: This test verifies that when streaming is enabled, the `stream_options` parameter, specifically setting `include_usage` to true, is correctly passed to the underlying OpenAI client's completion creation method. It simulates a streaming response containing content and usage chunks to assert this configuration.*


### TestStreamingHandlesInvalidChunks (class, L293-L410)

> *Summary: This test suite verifies that the streaming client gracefully handles non-`ChatCompletionChunk` objects received from an OpenAI API stream. It asserts that valid content and usage data are correctly accumulated while ensuring invalid chunks are skipped or logged as debug messages, preventing runtime exceptions.*


### mock_oai_client (method, L297-L302, parent: TestStreamingHandlesInvalidChunks)

> *Summary: This method constructs and returns a fully mocked instance of the OpenAI client, specifically configuring it to include a mock for chat completions functionality. This allows tests to simulate API interactions without making actual network calls.*


### _create_content_chunk (method, L304-L318, parent: TestStreamingHandlesInvalidChunks)

> *Summary: Constructs a `ChatCompletionChunk` object representing a segment of streamed content. It takes identifiers, model name, creation timestamp, and the actual text content as inputs to build the structured output.*


### _create_final_chunk_with_finish_reason (method, L320-L334, parent: TestStreamingHandlesInvalidChunks)

> *Summary: Constructs the final chunk object for a streaming response by packaging the provided ID, model name, and creation timestamp. It sets the `finish_reason` to "stop" within the choice delta, signaling the end of the generation process.*


### _create_usage_chunk (method, L336-L345, parent: TestStreamingHandlesInvalidChunks)

> *Summary: Generates a `ChatCompletionChunk` object specifically for usage reporting when no choices are present in the response stream. It takes a chunk ID, model name, and creation timestamp as inputs to construct the final chunk structure.*


### test_skips_non_chunk_objects (method, L347-L380, parent: TestStreamingHandlesInvalidChunks)

> *Summary: When streaming responses from an OpenAI client, this test verifies that the system gracefully ignores non-chunk objects (like dictionaries or strings) received in the stream iterator. It ensures that valid content chunks and usage data are correctly accumulated despite the presence of invalid data types.*


### test_logs_debug_for_invalid_chunks (method, L382-L410, parent: TestStreamingHandlesInvalidChunks)

> *Summary: This test verifies that the client emits a debug log when processing an invalid chunk during streaming responses from the OpenAI API. It simulates receiving a mix of valid, invalid, finish, and usage chunks to confirm logging occurs for unexpected types.*


### SimpleResponse (class, L414-L418)

> *Summary: Defines a data structure to represent a simple test response, requiring both a string answer and a floating-point confidence score. This model is used specifically for validating structured outputs from an AI service.*


### TestStreamingStructuredOutputIntegration (class, L422-L524)

> *Summary: These tests verify the integration of streaming with structured output when interacting with the OpenAI API. They confirm that requesting structured output (via Pydantic or JSON schema) automatically disables streaming while ensuring a valid, parsed response is returned; they also validate standard streaming behavior captures usage metrics when no structure is requested.*


### test_streaming_with_structured_output_pydantic (method, L430-L458, parent: TestStreamingStructuredOutputIntegration)

> *Summary: This test verifies that when requesting streaming with a Pydantic model for structured output, the underlying mechanism correctly disables streaming and returns a complete, parsable response object. It sends a prompt to an OpenAI client configured for streaming and then asserts that the resulting content can be successfully validated against the expected Pydantic schema.*


### test_streaming_with_structured_output_json_schema (method, L461-L494, parent: TestStreamingStructuredOutputIntegration)

> *Summary: This test verifies that when streaming is enabled alongside a JSON schema for structured output, the underlying mechanism disables streaming and returns a complete, valid JSON response. It sends a prompt to an OpenAI client configured with both `stream=True` and a specific JSON schema, then asserts the resulting content conforms to the expected structure (containing "answer" and "confidence").*


### test_streaming_without_structured_output_captures_usage (method, L497-L524, parent: TestStreamingStructuredOutputIntegration)

> *Summary: This test verifies that when streaming is enabled without specifying a structured output format, the resulting response correctly captures usage metrics. It initializes an OpenAI client with streaming enabled and asserts that the final response object contains non-zero token counts for prompt, completion, and total usage.*

