# test/beta/middleware/telemetry/test_telemetry.py

16 function(s): otel_setup, test_turn_span_emitted, test_llm_span_with_usage, test_tool_span, test_tool_span_with_content_capture, test_tool_error_marks_span_error, test_span_parent_child_hierarchy, test_capture_content_false_omits_messages, test_capture_content_true_includes_messages, test_auto_detect_model_provider_from_response and 6 more. 1 class(es): _InMemorySpanExporter. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _InMemorySpanExporter | class |  |
| otel_setup | function |  |
| test_turn_span_emitted | function |  |
| test_llm_span_with_usage | function |  |
| test_tool_span | function |  |
| test_tool_span_with_content_capture | function |  |
| test_tool_error_marks_span_error | function |  |
| test_span_parent_child_hierarchy | function |  |
| test_capture_content_false_omits_messages | function |  |
| test_capture_content_true_includes_messages | function |  |
| test_auto_detect_model_provider_from_response | function |  |
| test_tool_span_has_tool_type | function |  |
| test_constructor_params_override_response | function |  |
| test_cache_token_usage_attributes | function |  |
| test_cache_read_tokens_when_nonzero | function |  |
| test_thinking_tokens_when_nonzero | function |  |
| test_thinking_tokens_omitted_when_zero | function |  |

## Chunks

### _InMemorySpanExporter (class, L20-L38)

> *Summary: This class acts as a mock exporter, storing incoming spans in memory for testing purposes. It accepts sequences of `ReadableSpan` objects via the `export` method and provides access to all collected spans through `get_finished_spans`.*


### __init__ (method, L23-L25, parent: _InMemorySpanExporter)

> *Summary: Initializes the telemetry object by setting up an empty list to store `ReadableSpan` objects and a thread lock for concurrent access control.*


### export (method, L27-L30, parent: _InMemorySpanExporter)

> *Summary: This method safely appends a sequence of `ReadableSpan` objects to an internal list while holding a lock. It returns a success result indicating the spans were successfully queued for export.*


### get_finished_spans (method, L32-L34, parent: _InMemorySpanExporter)

> *Summary: Retrieves a snapshot of all completed spans held internally. It returns these spans as a list of `ReadableSpan` objects while ensuring thread safety via a lock.*


### shutdown (method, L36-L38, parent: _InMemorySpanExporter)

> *Summary: Clears all recorded spans within a lock to ensure thread-safe state cleanup during application shutdown. This method takes no input and returns nothing.*


### otel_setup (function, L42-L46)

> *Summary: Initializes OpenTelemetry tracing by creating an in-memory span exporter and a tracer provider. It configures the provider to use the in-memory exporter via a simple span processor and returns both the exporter and the configured provider object.*


### test_turn_span_emitted (function, L50-L67)

> *Summary: This test verifies that a specific telemetry span is emitted when an agent processes a request. It initializes an agent with telemetry middleware, calls the `ask` method, and then asserts that exactly one span of type "agent" exists with expected names and attributes.*


### test_llm_span_with_usage (function, L71-L103)

> *Summary: This test verifies that an LLM interaction correctly generates OpenTelemetry spans containing usage metrics. It asserts the presence of a single "llm" span with specific attributes detailing the model, operation, and token counts (10 input, 5 output).*


### test_tool_span (function, L107-L139)

> *Summary: This test verifies that the telemetry middleware correctly captures a tool execution span when an agent calls a defined function. It asserts that exactly one tool span is recorded with specific attributes matching the executed tool and call ID, while confirming arguments are omitted due to configuration.*


### test_tool_span_with_content_capture (function, L143-L172)

> *Summary: This test verifies that when an agent uses a tool, the telemetry middleware correctly captures and reports the tool's arguments and return value within the resulting OpenTelemetry spans. It asserts that exactly one tool span is generated and contains the expected input arguments and output result.*


### test_tool_error_marks_span_error (function, L176-L204)

> *Summary: This test verifies that when a defined tool raises an error, the telemetry middleware correctly records the corresponding operation as an error span. It asserts that exactly one tool span is captured and its status code reflects an error state.*


### test_span_parent_child_hierarchy (function, L208-L227)

> *Summary: This test verifies that when an agent interacts with an LLM, the resulting telemetry spans correctly establish a parent-child relationship. It asserts that the LLM span's parent ID matches the agent's main interaction span ID after executing an `ask` operation.*


### test_capture_content_false_omits_messages (function, L231-L247)

> *Summary: When configured with `capture_content=False`, this test verifies that the telemetry middleware omits message content from the generated spans. It asserts that input and output messages are absent from the LLM span attributes after an agent interaction.*


### test_capture_content_true_includes_messages (function, L251-L270)

> *Summary: This test verifies that when content capture is enabled, the resulting OpenTelemetry span for LLM interactions includes both the input and output messages as attributes. It asserts that the agent's response to a prompt contains the expected message content within these captured spans.*


### test_auto_detect_model_provider_from_response (function, L274-L309)

> *Summary: This test verifies that the telemetry middleware correctly auto-detects model provider and details when no explicit configuration is provided to an agent. It simulates a response from an LLM, runs the agent's ask method, and asserts that the resulting OpenTelemetry spans contain accurate metadata like provider name, model ID, finish reason, and token usage.*


### test_tool_span_has_tool_type (function, L313-L340)

> *Summary: This test verifies that the telemetry middleware correctly records a span for a function call made by an agent. It asserts that exactly one tool span is generated and that its attributes correctly identify the tool type as "function".*


### test_constructor_params_override_response (function, L344-L377)

> *Summary: This test verifies that middleware configuration parameters override the model details provided in the agent's constructor response when tracing an LLM interaction. It asserts that the tracer captures the custom provider and model names from the middleware, while retaining the model name specified in the initial response message.*


### test_cache_token_usage_attributes (function, L381-L411)

> *Summary: This test verifies that LLM span attributes correctly capture token usage metrics from a simulated agent interaction. It asserts that specific values for prompt, completion, and cache creation tokens are present on the resulting OpenTelemetry span, while confirming zero-value fields are omitted.*


### test_cache_read_tokens_when_nonzero (function, L415-L442)

> *Summary: This test verifies that the telemetry middleware correctly records `cache_read_input_tokens` when a simulated cache hit occurs during an agent's interaction. It asserts that the resulting LLM span contains the expected read token count (75) and lacks any creation token data.*


### test_thinking_tokens_when_nonzero (function, L446-L471)

> *Summary: This test verifies that when a model response includes non-zero `thinking_tokens`, the OpenTelemetry span correctly records this value under the `gen_ai.usage.thinking_tokens` attribute. It simulates an agent interaction using a mock response with specific usage metrics and asserts the resulting telemetry data.*


### test_thinking_tokens_omitted_when_zero (function, L475-L500)

> *Summary: This test verifies that when the `thinking_tokens` usage metric is zero, it is omitted from the exported OpenTelemetry span attributes. It initializes an agent with a mock response containing zero thinking tokens and asserts the absence of the corresponding attribute on the resulting LLM span.*

