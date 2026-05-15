# test/opentelemetry/test_instrument_agent_extras.py

2 function(s): otel_setup, _make_mock_agent_with_reply_func. 4 class(es): TestInstrumentCodeExecution, TestInstrumentCreateOrGetExecutor, TestInstrumentHumanInput, TestInstrumentRemoteReply. 31 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| otel_setup | function |  |
| _make_mock_agent_with_reply_func | function |  |
| TestInstrumentCodeExecution | class |  |
| TestInstrumentCreateOrGetExecutor | class |  |
| TestInstrumentHumanInput | class |  |
| TestInstrumentRemoteReply | class |  |

## Chunks

### otel_setup (function, L28-L33)

> *Summary: This function initializes and configures an OpenTelemetry tracing setup by creating an in-memory span exporter and a tracer provider. It returns both the configured exporter and the provider, allowing for capturing spans locally during testing.*


### _make_mock_agent_with_reply_func (function, L39-L46)

> *Summary: Constructs a minimal mock agent object configured to respond with a specific function. It takes a name and the actual reply function as input, returning an object containing that function within its response list.*


### TestInstrumentCodeExecution (class, L52-L278)

> *Summary: This test suite verifies the instrumentation logic for code execution within an agent, ensuring that reply functions are correctly wrapped with OpenTelemetry tracing. It validates various scenarios including successful/failed executions, output truncation, early returns when disabled, and proper handling of agents lacking relevant methods or configurations.*


### test_wraps_reply_func (method, L55-L73, parent: TestInstrumentCodeExecution)

> *Summary: This test verifies that the code execution reply function within a `ConversableAgent` is correctly instrumented with OpenTelemetry tracing. It asserts that specific functions, like `_generate_code_execution_reply_using_executor`, possess an `__otel_wrapped__` attribute after instrumentation.*


### test_code_execution_disabled_returns_early (method, L75-L99, parent: TestInstrumentCodeExecution)

> *Summary: When code execution is disabled in the agent configuration, the instrumented function immediately returns `(False, None)` without executing any logic or creating OpenTelemetry spans. This test verifies that setting `_code_execution_config` to `False` bypasses the actual reply function call entirely.*


### test_successful_code_execution_span (method, L101-L135, parent: TestInstrumentCodeExecution)

> *Summary: Verifies that a successful code execution results in an OpenTelemetry span with specific attributes, including `exit_code` set to 0 and the captured output text. It uses a mocked function to simulate the agent's reply process and then inspects the exported spans for correctness.*


### test_failed_code_execution_sets_error_type (method, L137-L165, parent: TestInstrumentCodeExecution)

> *Summary: This test verifies that when a simulated code execution fails (indicated by a non-zero exit code), the resulting OpenTelemetry span correctly records an `error.type` of "CodeExecutionError". It achieves this by mocking a function that returns failure output and then inspecting the exported spans for the expected attributes.*


### test_output_truncation (method, L167-L194, parent: TestInstrumentCodeExecution)

> *Summary: Verifies that code execution output exceeding 4096 characters is correctly truncated when instrumenting an agent's reply function. It asserts the resulting span attribute contains the expected truncation marker and length.*


### test_not_final_no_parsing (method, L196-L224, parent: TestInstrumentCodeExecution)

> *Summary: Verifies that when the execution function is marked as non-final, no exit code or output attributes are recorded on the resulting OpenTelemetry spans. It instruments a mock reply function and asserts that the generated code execution span lacks these specific attributes.*


### test_no_reply_func_list (method, L226-L233, parent: TestInstrumentCodeExecution)

> *Summary: When the provided agent lacks a `_reply_func_list`, this test verifies that the instrumentation process returns the original agent object unmodified. It achieves this by executing code against an agent instance specifically configured without that list.*


### test_no_code_exec_func_in_reply_list (method, L235-L251, parent: TestInstrumentCodeExecution)

> *Summary: This test verifies that when an agent's reply list contains a function without code execution capabilities, the instrumentation process leaves the agent unmodified. It calls `instrument_code_execution` with a mock function and asserts that the original function object remains in the agent's reply list after the call.*


### test_result_not_starting_with_exitcode (method, L253-L278, parent: TestInstrumentCodeExecution)

> *Summary: This test verifies that when a function's output does not begin with `"exitcode:"`, the instrumentation correctly records the result without adding an `ag2.code_execution.exit_code` attribute to the resulting span. It simulates code execution by mocking a reply function and asserts the final state of the recorded telemetry data.*


### TestInstrumentCreateOrGetExecutor (class, L284-L361)

> *Summary: This test suite verifies the behavior of a function that wraps an executor creation method. It ensures the wrapping correctly applies instrumentation, prevents double-wrapping, calls the provided instrumentator with the yielded executor, and gracefully handles agents lacking the target method.*


### test_wraps_create_or_get_executor (method, L287-L305, parent: TestInstrumentCreateOrGetExecutor)

> *Summary: This test verifies that the `_create_or_get_executor` method on an agent object is correctly wrapped by OpenTelemetry instrumentation. It mocks the original executor creation and asserts that the resulting function now possesses a specific wrapper attribute (`__otel_wrapped__`).*


### test_idempotency (method, L307-L327, parent: TestInstrumentCreateOrGetExecutor)

> *Summary: This test verifies that calling the executor creation function twice does not result in double wrapping. It mocks the executor retrieval and asserts that the returned callable remains the same instance across subsequent calls.*


### test_calls_instrumentator_on_executor (method, L329-L352, parent: TestInstrumentCreateOrGetExecutor)

> *Summary: This test verifies that the instrumentation logic correctly calls the provided instrumentator with the yielded executor object when an execution context is established. It mocks the executor creation process to assert this specific interaction occurs exactly once.*


### test_no_create_or_get_executor (method, L354-L361, parent: TestInstrumentCreateOrGetExecutor)

> *Summary: When an agent lacks a method to create or retrieve an executor, the function returns the original agent object unmodified. This test verifies that no changes occur when the provided agent structure does not support executor management.*


### TestInstrumentHumanInput (class, L367-L490)

> *Summary: This test suite verifies the `instrument_human_input` function's behavior when applying OpenTelemetry tracing to a conversational agent's human input methods. It confirms that both synchronous and asynchronous input methods are correctly wrapped, generate specific spans upon execution, handle idempotency during multiple calls, and properly forward arguments to the original underlying functions.*


### test_wraps_get_human_input (method, L370-L378, parent: TestInstrumentHumanInput)

> *Summary: This test verifies that the `get_human_input` method on a conversational agent is correctly instrumented with OpenTelemetry tracing. It achieves this by applying an instrumentation function and asserting the presence of a specific wrapper attribute on the target method.*


### test_wraps_a_get_human_input (method, L380-L388, parent: TestInstrumentHumanInput)

> *Summary: This test verifies that the `a_get_human_input` method on a conversational agent is correctly instrumented by OpenTelemetry. It achieves this by wrapping the agent with an instrumentation function and asserting the presence of a specific wrapper attribute on the target method.*


### test_sync_get_human_input_creates_span (method, L390-L414, parent: TestInstrumentHumanInput)

> *Summary: This test verifies that instrumenting an agent correctly creates a specific `await_human_input` OpenTelemetry span when the human input method is active. It mocks the input function, calls it, and then asserts that exactly one corresponding span exists with correct attributes detailing the prompt and response.*


### test_async_get_human_input_creates_span (method, L417-L442, parent: TestInstrumentHumanInput)

> *Summary: This test verifies that instrumenting a conversational agent correctly creates an OpenTelemetry span when its asynchronous human input method is called. It asserts the presence and specific attributes of this generated `await_human_input` span, including prompt and response details.*


### test_idempotency_sync (method, L444-L454, parent: TestInstrumentHumanInput)

> *Summary: This test verifies that instrumenting a conversational agent's `get_human_input` method multiple times does not result in nested wrappers. It asserts that the second instrumentation call returns the exact same wrapped function as the first.*


### test_idempotency_async (method, L456-L466, parent: TestInstrumentHumanInput)

> *Summary: This test verifies that instrumenting a conversational agent's human input method twice does not result in nested wrappers. It asserts that the second instrumentation call returns the exact same wrapped function as the initial one.*


### test_agent_without_get_human_input (method, L468-L476, parent: TestInstrumentHumanInput)

> *Summary: This test verifies that when an agent lacks a `get_human_input` attribute, the instrumentation function returns the original agent object unmodified. It confirms that no new attributes are added to the input agent during this process.*


### test_prompt_forwarded_to_original (method, L478-L490, parent: TestInstrumentHumanInput)

> *Summary: This test verifies that instrumentation correctly forwards the prompt and any extra arguments to the original function when calling `get_human_input`. It asserts that the mocked original method receives the exact input provided by the agent.*


### TestInstrumentRemoteReply (class, L496-L746)

> *Summary: This test suite verifies the `instrument_remote_reply` function's behavior when applying OpenTelemetry instrumentation to an agent object. It confirms that functions are correctly wrapped, spans are generated for remote calls (including setting correct attributes based on URL presence), and auxiliary components like HTTP client factories are also traced.*


### test_wraps_reply_func (method, L499-L518, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that the `instrument_remote_reply` function correctly wraps a target reply function. It asserts that the provided mock function is replaced by a new, instrumented version within the agent's reply list after instrumentation.*


### test_remote_reply_creates_agent_span (method, L521-L553, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that invoking a traced remote reply correctly generates an `invoke_agent` span in OpenTelemetry. It mocks the agent and its reply function, then asserts that exactly one agent-type span is recorded with specific attributes detailing the operation, agent name, and server address.*


### test_remote_reply_without_url (method, L556-L580, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that when an agent lacks a configured URL, the resulting telemetry span does not contain a `server.address` attribute after instrumentation. It mocks the necessary components and executes the instrumented reply function to assert this absence.*


### test_remote_reply_with_empty_url (method, L583-L607, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that when an agent's URL is empty, the resulting OpenTelemetry span does not contain a `server.address` attribute after instrumentation and execution of the remote reply function. It mocks the necessary components to simulate this specific scenario for validation.*


### test_httpx_client_factory_wrapped (method, L609-L636, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that an HTTP client factory within an agent object is successfully replaced with a traced version using OpenTelemetry instrumentation. It asserts that the replacement occurs and confirms that calling the wrapped factory executes the original underlying factory function.*


### test_httpx_client_factory_injects_traceparent (method, L638-L666, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that an instrumentation wrapper correctly injects `traceparent` headers into outgoing HTTP requests made by a mocked client factory. It achieves this by wrapping a component and asserting that the trace context is propagated when the wrapped client is instantiated within an active span.*


### test_no_a_generate_remote_reply (method, L668-L679, parent: TestInstrumentRemoteReply)

> *Summary: When an agent lacks a `a_generate_remote_reply` method, the instrumentation function returns the original agent object unmodified. This test verifies that no changes occur to the agent when this specific reply generation capability is absent.*


### test_no_matching_func_in_reply_list (method, L681-L699, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that when an agent has a method for generating remote replies but that method isn't listed in the configured reply functions, the instrumentation function returns the original agent unchanged. It asserts that the provided mock reply function remains unmodified after calling `instrument_remote_reply`.*


### test_already_wrapped_does_not_rewrap (method, L701-L720, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that an instrumentation function does not re-wrap a target method if it has already been marked as wrapped. It mocks a pre-wrapped function and asserts that the wrapping logic preserves the original function reference in the agent's internal list.*


### test_remote_reply_forwards_args (method, L723-L746, parent: TestInstrumentRemoteReply)

> *Summary: This test verifies that arguments and keyword arguments are correctly passed through when an instrumented remote reply function is called. It mocks the original reply function and asserts it was invoked with the exact inputs provided during the call to the wrapped function.*

