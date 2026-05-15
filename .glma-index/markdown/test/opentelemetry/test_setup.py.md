# test/opentelemetry/test_setup.py

2 class(es): TestDropNoiseSampler, TestGetTracer. 18 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestDropNoiseSampler | class |  |
| TestGetTracer | class |  |

## Chunks

### TestDropNoiseSampler (class, L22-L109)

> *Summary: This test suite verifies the behavior of a sampler designed to filter noisy spans based on their name. It asserts that spans prefixed with `a2a.` are marked as `RECORD_ONLY`, while other spans are fully sampled (`RECORD_AND_SAMPLE`), and it also checks correct handling of trace state and attribute passing.*


### setup_method (method, L25-L26, parent: TestDropNoiseSampler)

> *Summary: Initializes a `DropNoiseSampler` instance and assigns it to the test object's sampler attribute before each test execution. This sets up the sampling mechanism for subsequent tests.*


### test_a2a_span_is_record_only (method, L28-L35, parent: TestDropNoiseSampler)

> *Summary: This test verifies that spans prefixed with "a2a." are configured to be recorded but not exported by the sampler. It checks if calling `should_sample` with a specific trace ID and name returns a decision of `RECORD_ONLY`.*


### test_a2a_dot_prefix_is_record_only (method, L37-L43, parent: TestDropNoiseSampler)

> *Summary: This test verifies that when a trace name starts with "a2a.", the sampling decision returned is strictly `RECORD_ONLY`. It achieves this by calling the sampler's `should_sample` method with a specific trace ID and the prefixed name.*


### test_non_a2a_span_is_record_and_sample (method, L45-L52, parent: TestDropNoiseSampler)

> *Summary: This test verifies that a span lacking an upstream context is always fully exported by asserting the sampler returns `RECORD_AND_SAMPLE`. It achieves this by calling `should_sample` with no parent context and providing a trace ID and name.*


### test_invoke_agent_span_is_record_and_sample (method, L54-L60, parent: TestDropNoiseSampler)

> *Summary: This test verifies that a specific span invocation results in the `RECORD_AND_SAMPLE` decision when passed to the sampler with predefined trace and name information. It asserts the output of the sampling logic against this expected recording behavior.*


### test_chat_span_is_record_and_sample (method, L62-L68, parent: TestDropNoiseSampler)

> *Summary: This test verifies that a specific span name ("chat gpt-4") is configured to be recorded and sampled by the sampler. It calls `should_sample` with predefined trace ID and context, asserting the returned decision matches `Decision.RECORD_AND_SAMPLE`.*


### test_empty_name_is_record_and_sample (method, L70-L76, parent: TestDropNoiseSampler)

> *Summary: This test verifies that when an empty string is provided as the name in a sampling request, the sampler returns a decision to both record and sample the trace. It asserts that the `should_sample` method yields `Decision.RECORD_AND_SAMPLE` for this specific input.*


### test_a2a_without_dot_is_record_and_sample (method, L78-L85, parent: TestDropNoiseSampler)

> *Summary: This test verifies that an operation name lacking a trailing dot is not filtered by the sampler. It asserts that calling `should_sample` with `"a2a_something"` returns a decision to both record and sample.*


### test_trace_state_is_passed_through (method, L87-L95, parent: TestDropNoiseSampler)

> *Summary: This test verifies that the provided `TraceState` is correctly preserved when passed to a sampling decision function. It asserts that the output's trace state matches the input trace state after calling `should_sample`.*


### test_attributes_not_passed_through (method, L97-L106, parent: TestDropNoiseSampler)

> *Summary: When sampling a span with provided input attributes, this test asserts that the resulting `SamplingResult` object does not contain those attributes. It verifies that the sampler correctly discards or ignores incoming attribute data during the decision process.*


### test_get_description (method, L108-L109, parent: TestDropNoiseSampler)

> *Summary: Asserts that the description returned by the sampler contains the substring "a2a" when converted to lowercase, verifying expected metadata.*


### TestGetTracer (class, L115-L180)

> *Summary: These tests validate the `get_tracer` factory function by ensuring it returns a valid tracer instance configured with correct metadata (module name, version, schema URL) based on an input `TracerProvider`. It further verifies that tracers from different providers are distinct while those from the same provider yield equivalent instrumentation scopes, and confirms proper sampling behavior using `DropNoiseSampler`.*


### test_returns_tracer (method, L118-L122, parent: TestGetTracer)

> *Summary: This test verifies that the `get_tracer` function successfully returns a non-null tracer object when initialized with a `TracerProvider`. It confirms the basic functionality of obtaining an active tracing instrument.*


### test_tracer_has_correct_instrumenting_module (method, L124-L128, parent: TestGetTracer)

> *Summary: Verifies that the tracer's internal instrumentation scope is correctly set to match a predefined module name. It achieves this by initializing a `TracerProvider`, obtaining a tracer, and asserting the scope's name attribute.*


### test_tracer_has_correct_version (method, L130-L134, parent: TestGetTracer)

> *Summary: Verifies that the version exposed by an OpenTelemetry tracer matches a predefined constant. It achieves this by creating a `TracerProvider`, obtaining a tracer, and asserting the version attribute of its instrumentation scope.*


### test_tracer_has_correct_schema_url (method, L136-L140, parent: TestGetTracer)

> *Summary: This test verifies that the instrumentation scope associated with a tracer possesses the expected OpenTelemetry schema URL. It achieves this by initializing a `TracerProvider`, obtaining a tracer, and asserting the `schema_url` matches the predefined constant `OTEL_SCHEMA`.*


### test_different_providers_return_different_tracers (method, L142-L148, parent: TestGetTracer)

> *Summary: This test verifies that instantiating two separate `TracerProvider` instances results in distinct tracer objects when retrieving tracers from each provider. It asserts that the returned tracer instances are not the same object reference.*


### test_same_provider_returns_equivalent_tracer (method, L150-L155, parent: TestGetTracer)

> *Summary: Verifies that retrieving a tracer twice from the same `TracerProvider` yields tracers with identical instrumentation scopes. It confirms consistency by asserting equality between the internal scope attributes of both returned tracers.*


### test_tracer_used_with_drop_noise_sampler (method, L157-L180, parent: TestGetTracer)

> *Summary: This test verifies that a `DropNoiseSampler` correctly filters spans when used with an OpenTelemetry tracer setup. It asserts that a specific non-A2A span is exported while a designated A2A span is suppressed by the sampler.*

