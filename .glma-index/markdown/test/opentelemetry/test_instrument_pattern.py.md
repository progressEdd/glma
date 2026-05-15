# test/opentelemetry/test_instrument_pattern.py

4 function(s): otel_setup, _make_mock_agent, _make_mock_groupchat, _make_mock_pattern. 8 class(es): TestInstrumentPatternBasic, TestInstrumentPatternIdempotency, TestInstrumentPatternPrepareGroupChat, TestInstrumentGroupchatBasic, TestInstrumentGroupchatIdempotency, TestCreateInternalAgentsTraced, TestSyncAutoSelectSpeaker, TestAsyncAutoSelectSpeaker. 30 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| otel_setup | function |  |
| _make_mock_agent | function |  |
| _make_mock_groupchat | function |  |
| _make_mock_pattern | function |  |
| TestInstrumentPatternBasic | class |  |
| TestInstrumentPatternIdempotency | class |  |
| TestInstrumentPatternPrepareGroupChat | class |  |
| TestInstrumentGroupchatBasic | class |  |
| TestInstrumentGroupchatIdempotency | class |  |
| TestCreateInternalAgentsTraced | class |  |
| TestSyncAutoSelectSpeaker | class |  |
| TestAsyncAutoSelectSpeaker | class |  |

## Chunks

### otel_setup (function, L22-L27)

> *Summary: This function configures and returns an in-memory OpenTelemetry exporter and tracer provider. It sets up the system to capture spans by attaching a simple span processor to the provided exporter.*


### _make_mock_agent (function, L30-L34)

> *Summary: Creates and returns a `MagicMock` object configured to simulate an OpenTelemetry agent, setting its `.name` attribute based on the provided string input. This mock allows testing code that expects an agent object with a specific name property.*


### _make_mock_groupchat (function, L37-L49)

> *Summary: Generates a mock `GroupChat` object populated with mocked methods to simulate the target interface for instrumentation testing. It specifically ensures that certain internal methods lack the OpenTelemetry wrapping attribute (`__otel_wrapped__`) before returning the configured mock.*


### _make_mock_pattern (function, L52-L58)

> *Summary: Generates a mock object configured to simulate an OpenTelemetry `Pattern` with a specific `prepare_group_chat` method. This mock allows testing by optionally setting the return value for the chat preparation step and ensuring it appears unwrapped for instrumentation checks.*


### TestInstrumentPatternBasic (class, L64-L78)

> *Summary: This test suite verifies the behavior of `instrument_pattern` by ensuring it returns the original pattern object and correctly wraps specific methods within that pattern with an OpenTelemetry marker. It uses a mock pattern and tracer provider setup for execution.*


### test_returns_same_pattern_object (method, L67-L71, parent: TestInstrumentPatternBasic)

> *Summary: Verifies that the `instrument_pattern` function returns a reference to the exact same pattern object passed into it. It uses a mock pattern and an OpenTelemetry provider setup for this assertion.*


### test_marks_prepare_group_chat_as_wrapped (method, L73-L78, parent: TestInstrumentPatternBasic)

> *Summary: This test verifies that an instrumentation function correctly wraps a target method with OpenTelemetry tracing capabilities. It takes a mock pattern and a tracer provider as input, asserting that the specific method within the pattern now has an `__otel_wrapped__` attribute set to `True`.*


### TestInstrumentPatternIdempotency (class, L84-L100)

> *Summary: Verifies that applying the instrumentation function multiple times to a pattern does not create duplicate wrappers or return different instances. It ensures idempotency by asserting that subsequent calls yield the exact same prepared object and returned reference.*


### test_double_instrument_does_not_double_wrap (method, L87-L93, parent: TestInstrumentPatternIdempotency)

> *Summary: This test verifies that applying an instrumentation pattern twice does not result in nested wrapping of the target method. It instruments a mock pattern and then asserts that the reference to the prepared function remains unchanged after the second instrumentation call.*


### test_double_instrument_returns_same_pattern (method, L95-L100, parent: TestInstrumentPatternIdempotency)

> *Summary: Verifies that calling the instrumentation function twice with the same pattern and provider yields identical object references. This confirms idempotency in the returned pattern instance when using the provided OpenTelemetry setup.*


### TestInstrumentPatternPrepareGroupChat (class, L106-L263)

> *Summary: These tests verify that wrapping a `prepare_group_chat` method correctly instruments agents and group chats using OpenTelemetry. The code asserts that the original function is called, checks the correct number of agent instrumentations based on inputs (including managers), and confirms instrumentation occurs for copied GroupChat objects within the manager's reply functions.*


### test_wrapped_prepare_group_chat_calls_original (method, L109-L167, parent: TestInstrumentPatternPrepareGroupChat)

> *Summary: This test verifies that the `prepare_group_chat` method correctly wraps its underlying logic using OpenTelemetry instrumentation. It sets up mock agents and a group chat, then calls the instrumented function to assert that the original method was called as expected after wrapping.*


### test_wrapped_prepare_group_chat_instruments_groupchat_agents (method, L169-L210, parent: TestInstrumentPatternPrepareGroupChat)

> *Summary: This test verifies that the instrumentation pattern correctly wraps all involved entities when preparing a group chat. It asserts that `instrument_agent` is called three times—once for each agent and once for the manager—when calling `prepare_group_chat`.*


### test_wrapped_prepare_group_chat_instruments_manager_groupchat_copies (method, L212-L263, parent: TestInstrumentPatternPrepareGroupChat)

> *Summary: This test verifies that when a `GroupChat` copy is present in the manager's reply function list, it is also instrumented by OpenTelemetry. It mocks up a scenario where an agent interacts with both a primary and a copied `GroupChat` object to assert that the instrumentation function is called twice for the group chat.*


### TestInstrumentGroupchatBasic (class, L269-L297)

> *Summary: This test suite verifies the instrumentation of a group chat object by applying OpenTelemetry tracing wrappers to its methods. It confirms that the instrumented object returns itself and that specific internal methods like `create_internal_agents` and speaker selection functions are correctly wrapped with OTEL attributes.*


### test_returns_same_groupchat (method, L272-L276, parent: TestInstrumentGroupchatBasic)

> *Summary: This test verifies that the instrumentation function returns the exact same group chat object passed into it. It achieves this by calling `instrument_groupchat` with a mocked group chat and asserting identity equality on the return value.*


### test_wraps_create_internal_agents (method, L278-L283, parent: TestInstrumentGroupchatBasic)

> *Summary: This test verifies that the `instrument_groupchat` function successfully wraps the internal agent creation method of a mock group chat object. It asserts that the wrapped method now possesses an attribute indicating it has been instrumented by OpenTelemetry.*


### test_wraps_auto_select_speaker (method, L285-L290, parent: TestInstrumentGroupchatBasic)

> *Summary: This test verifies that the `instrument_groupchat` function correctly wraps the `_auto_select_speaker` method on a mock group chat object. It asserts that the wrapped method gains an attribute indicating it has been instrumented by OpenTelemetry.*


### test_wraps_a_auto_select_speaker (method, L292-L297, parent: TestInstrumentGroupchatBasic)

> *Summary: This test verifies that the `instrument_groupchat` function correctly wraps the `a_auto_select_speaker` method on a mock group chat object. It asserts that the wrapped method gains an attribute indicating it has been instrumented by OpenTelemetry.*


### TestInstrumentGroupchatIdempotency (class, L303-L328)

> *Summary: Verifies that applying instrumentation multiple times to a group chat object does not result in nested or double-wrapped functions. It achieves this by instrumenting methods like `create_internal_agents` and asserting that the function reference remains unchanged after subsequent calls to the instrumentation utility.*


### test_double_instrument_does_not_double_wrap_create_internal_agents (method, L306-L312, parent: TestInstrumentGroupchatIdempotency)

> *Summary: This test verifies that applying instrumentation twice to a group chat object does not result in nested wrappers for its internal agent creation method. It asserts that the second call to `instrument_groupchat` leaves the original function reference intact on the target object.*


### test_double_instrument_does_not_double_wrap_auto_select_speaker (method, L314-L320, parent: TestInstrumentGroupchatIdempotency)

> *Summary: This test verifies that applying the instrumentation function twice to a group chat object does not result in nested wrapping of its `_auto_select_speaker` method. It asserts that the second application returns the original, un-wrapped function reference.*


### test_double_instrument_does_not_double_wrap_a_auto_select_speaker (method, L322-L328, parent: TestInstrumentGroupchatIdempotency)

> *Summary: This test verifies that applying instrumentation twice to a method does not result in nested wrappers. It instruments the `a_auto_select_speaker` method on a mock group chat object, then re-instruments it and asserts that the reference to the original function remains unchanged.*


### TestCreateInternalAgentsTraced (class, L334-L401)

> *Summary: These tests verify that wrapping a `GroupChat` object with OpenTelemetry instrumentation correctly instruments the agents returned by its internal creation method. They confirm that both the original function executes and that the newly created temporary agents are passed to the agent instrumentator, while also checking for correct argument passing like the `selector`.*


### test_create_internal_agents_calls_original_and_returns_agents (method, L337-L360, parent: TestCreateInternalAgentsTraced)

> *Summary: This test verifies that when an agent creation method is instrumented, it correctly calls the original implementation and returns the expected tuple of mocked agents. It asserts that the instrumentation wrapper was called exactly twice for the created agents.*


### test_create_internal_agents_passes_selector_kwarg (method, L362-L401, parent: TestCreateInternalAgentsTraced)

> *Summary: This test verifies that the `instrument_groupchat` function correctly passes a provided selector agent when calling internal agent creation methods. It mocks various components to assert that the original method receives the expected selector argument during execution.*


### TestSyncAutoSelectSpeaker (class, L407-L586)

> *Summary: This test suite verifies that instrumentation correctly captures speaker selection events by asserting the presence and content of OpenTelemetry spans generated when calling `_auto_select_speaker`. It checks for correct span naming, operation names, recording of candidate agents, and logging of the ultimately selected agent.*


### test_creates_speaker_selection_span (method, L410-L442, parent: TestSyncAutoSelectSpeaker)

> *Summary: This test verifies that an OpenTelemetry span of type `SPEAKER_SELECTION` is generated when a group chat object's speaker selection method is called after instrumentation. It mocks the necessary agents and group chat behavior to isolate and assert the presence of this specific telemetry event in the exported spans.*


### test_span_name_is_speaker_selection (method, L444-L466, parent: TestSyncAutoSelectSpeaker)

> *Summary: This test verifies that the instrumentation correctly names the span generated when a group chat selects a speaker. It mocks the selection process and asserts that the resulting OpenTelemetry span has the expected name, `"speaker_selection"`.*


### test_span_sets_operation_name (method, L468-L487, parent: TestSyncAutoSelectSpeaker)

> *Summary: This test verifies that the `instrument_groupchat` function correctly sets the operation name attribute to `"speaker_selection"` on spans generated during a mock group chat's speaker selection process. It achieves this by mocking agents and using an exporter to inspect the resulting telemetry data.*


### test_span_records_candidate_agents (method, L489-L512, parent: TestSyncAutoSelectSpeaker)

> *Summary: This test verifies that instrumentation correctly captures the candidate agents during a speaker selection event within a group chat simulation. It asserts that the recorded span attributes contain all expected agent names as candidates.*


### test_span_records_selected_speaker (method, L514-L535, parent: TestSyncAutoSelectSpeaker)

> *Summary: This test verifies that instrumentation correctly records a span when the group chat's automatic speaker selection is called. It asserts that the resulting span attributes accurately reflect the selected agent ("writer") based on mocked inputs.*


### test_span_uses_groupchat_agents_when_agents_arg_is_none (method, L537-L560, parent: TestSyncAutoSelectSpeaker)

> *Summary: This test verifies that when the `agents` argument is `None`, an instrumented group chat object correctly populates the speaker selection span with all available agents from its internal list. It asserts that the resulting span's attributes contain a list of all initial agents ("alpha", "beta").*


### test_calls_original_auto_select_speaker (method, L562-L586, parent: TestSyncAutoSelectSpeaker)

> *Summary: This test verifies that instrumentation correctly wraps the `_auto_select_speaker` method on a group chat object. It asserts that when the wrapped method is called with specific agent and message inputs, it executes the original mock function exactly once with those same arguments.*


### TestAsyncAutoSelectSpeaker (class, L592-L763)

> *Summary: This test suite verifies that instrumenting a group chat's `a_auto_select_speaker` method correctly generates OpenTelemetry spans for speaker selection events. It asserts various aspects of these generated spans, including the correct span type, recorded candidate agents, selected speaker, and operation names under different input conditions.*


### test_creates_speaker_selection_span (method, L596-L617, parent: TestAsyncAutoSelectSpeaker)

> *Summary: This test verifies that instrumenting a group chat correctly generates a specific span when the auto-select speaker method is called. It mocks agents and the group chat, then asserts that exactly one `SPEAKER_SELECTION` type span is recorded by the exporter after execution.*


### test_span_records_candidate_agents (method, L620-L642, parent: TestAsyncAutoSelectSpeaker)

> *Summary: This test verifies that instrumentation correctly captures speaker selection events from a mock group chat interaction. It asserts that the resulting OpenTelemetry span attributes contain a list of all candidate agents involved in the selection process.*


### test_span_records_selected_speaker (method, L645-L666, parent: TestAsyncAutoSelectSpeaker)

> *Summary: This test verifies that an instrumentation correctly records a span when the `a_auto_select_speaker` method is called on a mock group chat object. It asserts that the resulting span attributes accurately reflect the selected speaker, which was mocked to be "bob".*


### test_span_uses_groupchat_agents_when_agents_arg_is_none (method, L669-L691, parent: TestAsyncAutoSelectSpeaker)

> *Summary: This test verifies that the instrumentation correctly records speaker selection spans when no specific agents are provided to the group chat object. It asserts that the recorded span attributes contain all expected agent IDs as candidates for selection.*


### test_calls_original_a_auto_select_speaker (method, L694-L717, parent: TestAsyncAutoSelectSpeaker)

> *Summary: This test verifies that OpenTelemetry instrumentation correctly wraps the `a_auto_select_speaker` method on a mock group chat object. It asserts that when called with specific agent and message inputs, the wrapped function executes the original logic and calls the underlying mocked function exactly once with the expected arguments.*


### test_async_span_name_is_speaker_selection (method, L720-L740, parent: TestAsyncAutoSelectSpeaker)

> *Summary: This test verifies that an asynchronous operation correctly instruments its span name when using the `instrument_groupchat` utility. It mocks a group chat and asserts that the resulting OpenTelemetry span for the speaker selection process is named `"speaker_selection"`.*


### test_async_span_sets_operation_name (method, L743-L763, parent: TestAsyncAutoSelectSpeaker)

> *Summary: This test verifies that the `instrument_groupchat` function correctly sets the operation name attribute to `"speaker_selection"` on spans generated during an asynchronous call to `a_auto_select_speaker`. It achieves this by mocking the necessary components and asserting the final span attributes after execution.*

