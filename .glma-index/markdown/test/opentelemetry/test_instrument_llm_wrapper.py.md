# test/opentelemetry/test_instrument_llm_wrapper.py

2 function(s): otel_setup, _restore_openai_wrapper_create. 8 class(es): FakeUsage, FakeMessage, FakeChoice, FakeResponse, TestInstrumentLlmWrapperBasic, TestLlmSpanCreation, TestLlmWrapperSpanWithMocking, TestTracedCreateEndToEnd. 28 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| otel_setup | function |  |
| _restore_openai_wrapper_create | function |  |
| FakeUsage | class |  |
| FakeMessage | class |  |
| FakeChoice | class |  |
| FakeResponse | class |  |
| TestInstrumentLlmWrapperBasic | class |  |
| TestLlmSpanCreation | class |  |
| TestLlmWrapperSpanWithMocking | class |  |
| TestTracedCreateEndToEnd | class |  |

## Chunks

### otel_setup (function, L21-L26)

> *Summary: Initializes and configures OpenTelemetry tracing by creating an in-memory span exporter and a tracer provider. It returns both the configured exporter and the provider for capturing telemetry data.*


### _restore_openai_wrapper_create (function, L30-L34)

> *Summary: This function restores the original `OpenAIWrapper.create` method after tests by saving and then replacing the patched version with the stored original reference. It acts as a cleanup mechanism to undo monkey-patching applied during testing.*


### FakeUsage (class, L41-L43)

> *Summary: Provides a mock implementation for usage metrics, defaulting to 10 prompt tokens and 20 completion tokens. This class serves as a placeholder for testing telemetry instrumentation without real external calls.*


### FakeMessage (class, L47-L53)

> *Summary: This class provides a mock message structure, initializing it with default content and an empty list for tool calls if none are provided during instantiation. It serves as a placeholder object for testing purposes within the OpenTelemetry context.*


### __post_init__ (method, L51-L53, parent: FakeMessage)

> *Summary: Ensures the `tool_calls` attribute is initialized as an empty list if it was not provided during object creation. This guarantees that subsequent operations can safely iterate over or append to this collection.*


### FakeChoice (class, L57-L63)

> *Summary: This class simulates a model's choice, initializing with default values for the message and finish reason. If no `FakeMessage` is provided during initialization, it automatically creates one.*


### __post_init__ (method, L61-L63, parent: FakeChoice)

> *Summary: After initialization, this method ensures the `message` attribute is set to a default `FakeMessage` instance if no message was provided during object creation. This guarantees that the object always has a valid message payload.*


### FakeResponse (class, L67-L77)

> *Summary: This class simulates an API response object, pre-populating it with default values for model name, cost, and a list containing one mock choice. It ensures that `usage` and `choices` attributes are initialized if they are not provided upon instantiation.*


### __post_init__ (method, L73-L77, parent: FakeResponse)

> *Summary: After initialization, this method ensures that `usage` and `choices` attributes are set to default mock objects if they were not provided during instantiation. This guarantees the object has necessary structures for subsequent operations.*


### TestInstrumentLlmWrapperBasic (class, L83-L97)

> *Summary: This test suite verifies that the `instrument_llm_wrapper` correctly wraps the `OpenAIWrapper.create` method with OpenTelemetry instrumentation. It asserts both that the wrapping occurs and that subsequent calls to the wrapper are idempotent, preventing multiple re-wrapping of the same function object.*


### test_wraps_create_method (method, L86-L89, parent: TestInstrumentLlmWrapperBasic)

> *Summary: This test verifies that the `instrument_llm_wrapper` function successfully wraps the `OpenAIWrapper.create` method by asserting the presence of a specific attribute on it. It uses an OpenTelemetry provider setup to perform this instrumentation check.*


### test_idempotency (method, L91-L97, parent: TestInstrumentLlmWrapperBasic)

> *Summary: This test verifies that wrapping the `OpenAIWrapper.create` method with instrumentation does not create a new wrapper instance upon subsequent calls. It asserts that the reference to the wrapped function remains identical after being instrumented twice.*


### TestLlmSpanCreation (class, L103-L164)

> *Summary: This test suite verifies that instrumenting an LLM wrapper correctly generates OpenTelemetry spans and sets appropriate attributes on those spans. It achieves this by patching the `OpenAIWrapper`'s creation method to assert span existence and then directly testing a helper function responsible for setting model-specific response attributes.*


### test_creates_llm_span (method, L106-L137, parent: TestLlmSpanCreation)

> *Summary: This test verifies that instrumenting an LLM wrapper correctly adds OpenTelemetry tracing capabilities. It achieves this by patching and inspecting the `OpenAIWrapper.create` method to assert the presence of an internal instrumentation flag (`__otel_wrapped__`).*


### test_span_attributes_with_model (method, L139-L164, parent: TestLlmSpanCreation)

> *Summary: This test verifies that the LLM wrapper correctly sets span attributes by calling a private helper function with a mock span and a fake response object. It asserts that the `set_attribute` method on the mock span is called with the expected model name, `"gen_ai.response.model": "gpt-4"`.*


### TestLlmWrapperSpanWithMocking (class, L167-L354)

> *Summary: This test class verifies the functionality of a helper function that populates OpenTelemetry span attributes based on an LLM response object. It uses mocked spans and fake response objects to assert correct attribute setting for model name, token usage, finish reasons, cost, and message content capture.*


### _call_traced_create (method, L170-L195, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This helper method sets up OpenTelemetry tracing by clearing an exporter and instrumenting the LLM wrapper using a provided tracer provider. It then returns all finished spans captured during the instrumentation process, effectively testing the span recording mechanism.*


### test_set_llm_response_attributes_model (method, L197-L204, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that the `_set_llm_response_attributes` function correctly sets the LLM response model attribute on an OpenTelemetry span. It takes a mock span and a fake response object containing the model name as input, asserting that the correct attribute is set on the span.*


### test_set_llm_response_attributes_token_usage (method, L206-L215, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that a utility function correctly sets OpenTelemetry span attributes based on token usage data from an LLM response object. It asserts that the input and output token counts are recorded as specific attributes on the provided mock span.*


### test_set_llm_response_attributes_finish_reasons (method, L217-L230, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that the `_set_llm_response_attributes` function correctly extracts and sets the finish reasons from a mock LLM response onto an OpenTelemetry span. It asserts that the resulting attribute, when parsed as JSON, contains all expected finish reason strings ("stop" and "length").*


### test_set_llm_response_attributes_cost (method, L232-L239, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that the `_set_llm_response_attributes` function correctly sets the cost attribute on an OpenTelemetry span. It takes a mock span and a fake response object containing a cost, asserting that the span's set\_attribute method was called with the correct cost value.*


### test_set_llm_response_attributes_no_usage (method, L241-L252, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that the attribute setting function handles a response object lacking usage data without error. It asserts that the model name is correctly set on the span while confirming that input token metrics are absent when `resp.usage` is `None`.*


### test_set_llm_response_attributes_no_choices (method, L254-L263, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that when an LLM response has no choices, the attribute `gen_ai.response.finish_reasons` is not set on the OpenTelemetry span. It achieves this by mocking a span and a fake response with an empty `choices` list before calling the attribute setting function.*


### test_set_llm_response_attributes_capture_messages (method, L265-L277, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that when `capture_messages` is true, the provided span receives an attribute containing a JSON list of messages from the LLM response. It asserts that this captured message list includes at least one entry with the role set to "assistant".*


### test_set_llm_response_attributes_no_capture_messages (method, L279-L287, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that when `capture_messages` is set to false, the provided function does not record message details as attributes on the OpenTelemetry span. It asserts that the specific attribute key `"gen_ai.output.messages"` is absent from all recorded span attributes.*


### test_set_llm_response_attributes_with_tool_calls (method, L289-L321, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that the response attribute setting function correctly captures and serializes tool call information from a mock LLM response. It asserts that the resulting span attributes contain the expected structure, including a specific tool call named "get\_weather".*


### test_set_llm_response_attributes_no_model (method, L323-L331, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that when an LLM response lacks a model, the attribute setting function does not record the `gen_ai.response.model` attribute on the provided OpenTelemetry span. It achieves this by mocking a span and using a fake response where the model is explicitly set to `None`.*


### test_set_llm_response_attributes_no_cost (method, L333-L341, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that when an LLM response has no associated cost, the attribute `gen_ai.usage.cost` is not set on the OpenTelemetry span. It achieves this by mocking a span and providing a fake response object with `cost=None`.*


### test_set_llm_response_attributes_completion_tokens_none (method, L343-L354, parent: TestLlmWrapperSpanWithMocking)

> *Summary: This test verifies that when an LLM response's `completion_tokens` is `None`, the instrumentation correctly sets the corresponding OpenTelemetry attribute (`gen_ai.usage.output_tokens`) to zero on the provided span. It simulates a scenario using mock objects for the span, usage data, and response.*


### TestTracedCreateEndToEnd (class, L360-L543)

> *Summary: This test suite verifies the end-to-end tracing of an LLM creation call by mocking the underlying OpenAI wrapper and instrumenting it with OpenTelemetry. It asserts that various details, such as span existence, message capture (conditionally), request parameters, token usage, model names, and agent identification, are correctly recorded in the exported spans.*


### test_traced_create_produces_llm_span (method, L363-L383, parent: TestTracedCreateEndToEnd)

> *Summary: This test verifies that instrumenting the LLM wrapper correctly generates an OpenTelemetry span when `OpenAIWrapper.create` is called with a mocked response. It asserts that exactly one span of type "llm" is produced, named appropriately for GPT-4, and tagged with the correct provider name ("openai").*


### test_traced_create_captures_messages_when_enabled (method, L385-L408, parent: TestTracedCreateEndToEnd)

> *Summary: This test verifies that when message capturing is enabled, the instrumentation correctly records input and output messages within the generated OpenTelemetry spans for an LLM call. It mocks an OpenAI response and asserts that the resulting span attributes contain serialized lists of these messages.*


### test_traced_create_does_not_capture_messages_by_default (method, L410-L429, parent: TestTracedCreateEndToEnd)

> *Summary: This test verifies that the instrumentation, when configured with default settings, does not automatically capture message content from LLM calls. It mocks an OpenAI response and asserts that the resulting OpenTelemetry span lacks specific attributes for input or output messages.*


### test_traced_create_records_error_on_exception (method, L431-L451, parent: TestTracedCreateEndToEnd)

> *Summary: This test verifies that when the underlying LLM creation fails with a `ConnectionError`, the tracing instrumentation correctly captures this exception in the resulting OpenTelemetry spans. It asserts that exactly one LLM span is recorded and that its attributes indicate an error of type `ConnectionError`.*


### test_traced_create_sets_request_params (method, L453-L478, parent: TestTracedCreateEndToEnd)

> *Summary: This test verifies that the LLM instrumentation correctly captures request parameters when calling `OpenAIWrapper.create`. It asserts that a single "llm" span is generated and contains the expected values for temperature, max tokens, and top\_p from the input configuration.*


### test_traced_create_sets_response_token_usage (method, L480-L499, parent: TestTracedCreateEndToEnd)

> *Summary: This test verifies that the instrumentation correctly captures token usage from an LLM call. It mocks a response with specific input and output tokens, then asserts that the resulting OpenTelemetry span contains these exact values under `gen_ai.usage` attributes.*


### test_traced_create_sets_model_and_operation (method, L501-L521, parent: TestTracedCreateEndToEnd)

> *Summary: This test verifies that instrumenting an LLM wrapper correctly generates a single OpenTelemetry span when calling the `create` method with a specific model configuration. It asserts that the resulting span contains expected attributes detailing the operation name, request model, and response model.*


### test_traced_create_sets_agent_name (method, L523-L543, parent: TestTracedCreateEndToEnd)

> *Summary: This test verifies that the LLM instrumentation correctly captures and sets the agent's name in OpenTelemetry spans when calling `OpenAIWrapper.create`. It mocks an OpenAI response and asserts that a single span is generated with the expected `gen_ai.agent.name` attribute populated from the provided mock agent object.*

