# test/beta/config/anthropic/test_anthropic_usage.py

13 function(s): _make_usage, _make_response, _make_context, test_process_response_normalizes_usage, test_process_response_includes_cache_creation_tokens, test_process_response_includes_cache_read_tokens, test_process_response_no_usage, test_process_stream_normalizes_usage, _async_iter, _call_context and 3 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_usage | function |  |
| _make_response | function |  |
| _make_context | function |  |
| test_process_response_normalizes_usage | function |  |
| test_process_response_includes_cache_creation_tokens | function |  |
| test_process_response_includes_cache_read_tokens | function |  |
| test_process_response_no_usage | function |  |
| test_process_stream_normalizes_usage | function |  |
| _async_iter | function |  |
| _call_context | function |  |
| _serializer | function |  |
| test_extra_body_lands_in_messages_create_kwargs | function |  |
| test_no_extra_body_means_no_extra_body_kwarg | function |  |

## Chunks

### _make_usage (function, L17-L31)

> *Summary: Generates a mock object simulating an Anthropic Usage response. It accepts token counts for input and output (including cache operations) as arguments and returns a `MagicMock` configured to return these values when its `model_dump()` method is called.*


### _make_response (function, L34-L49)

> *Summary: Constructs a mock Anthropic message response object using provided usage statistics and content text. It returns a `MagicMock` instance structured to mimic the API's expected response format, including content blocks and metadata.*


### _make_context (function, L52-L55)

> *Summary: Creates and returns a mock object configured with an asynchronous `send` method for simulating context interactions. This helper provides a standardized, controllable environment for testing asynchronous operations.*


### test_process_response_normalizes_usage (function, L59-L67)

> *Summary: This test verifies that the response processing correctly normalizes usage metrics from an Anthropic API simulation. It takes a mock response containing token counts and asserts that the resulting `ModelResponse` object contains the accurately calculated usage totals.*


### test_process_response_includes_cache_creation_tokens (function, L71-L84)

> *Summary: This test verifies that processing a response correctly incorporates cache creation tokens into the final usage statistics when `prompt_caching` is disabled. It asserts that the resulting usage object accurately reflects the input, completion, and specific cache creation token counts provided in the mock response.*


### test_process_response_includes_cache_read_tokens (function, L88-L101)

> *Summary: This test verifies that processing a response correctly incorporates cached read tokens into the final usage statistics when `prompt_caching` is disabled. It asserts that the resulting usage object accurately reflects the provided input, output, and cache read token counts.*


### test_process_response_no_usage (function, L105-L112)

> *Summary: This test verifies that processing a response with no usage data results in an output object where all token counts are zero. It initializes an Anthropic client and calls the internal response processor with a mock response lacking usage metrics.*


### test_process_stream_normalizes_usage (function, L116-L145)

> *Summary: This test verifies that the stream processing logic correctly normalizes usage metrics from an Anthropic API response. It simulates a streaming response containing one text delta and asserts that the resulting `ModelResponse` contains the expected, normalized token counts.*


### _async_iter (function, L148-L150)

> *Summary: This asynchronous generator iterates over an input collection, yielding each element sequentially. It provides a simple wrapper to allow synchronous or iterable inputs to be consumed asynchronously.*


### _call_context (function, L153-L157)

> *Summary: Creates and returns a mock context object configured with asynchronous send functionality and an empty prompt list for testing Anthropic interactions. This helper provides a standardized, controllable environment for simulating API call contexts.*


### _serializer (function, L160-L164)

> *Summary: Creates and returns a `PydanticSerializer` instance configured to allow arbitrary types during serialization. This serializer is initialized with specific settings for error handling and type flexibility.*


### test_extra_body_lands_in_messages_create_kwargs (function, L168-L188)

> *Summary: This test verifies that custom parameters passed in `extra_body` are correctly forwarded to the underlying API call when creating messages. It mocks the message creation endpoint and asserts that the provided extra body dictionary is present in the received keyword arguments.*


### test_no_extra_body_means_no_extra_body_kwarg (function, L192-L211)

> *Summary: This test verifies that when no explicit body parameters are provided during a client call, the underlying API request does not include an `extra_body` argument. It mocks the message creation endpoint to capture all received keyword arguments and asserts the absence of this specific key.*

