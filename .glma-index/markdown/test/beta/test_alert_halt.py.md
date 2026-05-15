# test/beta/test_alert_halt.py

1 function(s): echo_tool. 5 class(es): _RecordingClient, _RecordingConfig, TestAlertPolicyUnit, TestHaltCheckMiddleware, TestAlertPolicyOrdering. 21 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| echo_tool | function |  |
| _RecordingClient | class |  |
| _RecordingConfig | class |  |
| TestAlertPolicyUnit | class |  |
| TestHaltCheckMiddleware | class |  |
| TestAlertPolicyOrdering | class |  |

## Chunks

### echo_tool (function, L41-L43)

> *Summary: This function takes a string as input and returns a new string prefixed with "echo: ". It serves as a simple utility to reflect the provided value.*


### _RecordingClient (class, L46-L67)

> *Summary: This client intercepts LLM calls by recording the input messages and context. It then returns pre-configured canned responses or a "done" signal based on an internal counter, simulating controlled interaction for testing purposes.*


### __init__ (method, L49-L52, parent: _RecordingClient)

> *Summary: Initializes an object to track responses and tool calls, storing any provided arguments as a list of `_responses` and setting the initial call count to zero. It also initializes an empty structure to record past invocation details.*


### __call__ (method, L54-L67, parent: _RecordingClient)

> *Summary: This method processes a sequence of events and context to return a model response. It retrieves a predefined response based on an internal call count, returning either a string wrapped in `ModelMessage`, a `ToolCallEvent` wrapped in `ModelResponse`, or the raw response object itself.*


### _RecordingConfig (class, L70-L82)

> *Summary: This configuration object holds a collection of responses or tool calls and provides methods to initialize and generate a recording client instance from those inputs. It allows for creating a copy of the current configuration state.*


### __init__ (method, L73-L75, parent: _RecordingConfig)

> *Summary: Initializes the object by storing a variable number of inputs, which can be model responses, tool call events, or strings. It also initializes an optional client reference to `None`.*


### copy (method, L77-L78, parent: _RecordingConfig)

> *Summary: This method returns a reference to the current instance, effectively creating a shallow copy of the object. It ensures that operations intended to modify the state are performed on a new object if necessary, though here it just returns itself.*


### create (method, L80-L82, parent: _RecordingConfig)

> *Summary: Instantiates and returns a `_RecordingClient` object using the stored responses from the instance's internal state. This method effectively finalizes the client setup based on prior test data.*


### TestAlertPolicyUnit (class, L85-L279)

> *Summary: This test suite verifies the behavior of an alert policy by simulating its application to prompts and events within isolation. It confirms that non-fatal alerts are injected into prompts, fatal alerts trigger a `HaltEvent` via context sending, and the system correctly handles deduplication across multiple calls based on alert content.*


### test_no_alerts_is_noop (method, L89-L101, parent: TestAlertPolicyUnit)

> *Summary: When provided with no `ObserverAlert` events, the policy applies without modification to the input prompts and events. It ensures that the context's send method is never called during this operation.*


### test_single_warning_injected (method, L104-L119, parent: TestAlertPolicyUnit)

> *Summary: This test verifies that when a single `WARNING` alert is injected, the policy processes it by embedding the alert details into the subsequent prompt text. It asserts that exactly two prompts are returned and that the second prompt contains the specific warning message and severity level, while confirming no halt event was triggered.*


### test_multiple_severities_formatted (method, L122-L140, parent: TestAlertPolicyUnit)

> *Summary: This test verifies that an `AlertPolicy` correctly processes and formats multiple alerts with varying severities. It inputs a list of different severity alerts and prompts, asserting that the resulting formatted text contains messages from all provided alerts.*


### test_fatal_emits_halt_event (method, L143-L167, parent: TestAlertPolicyUnit)

> *Summary: This test verifies that a fatal alert triggers the emission of a `HaltEvent` when processed by an `AlertPolicy`. It asserts that exactly one event was sent, confirming it is a `HaltEvent` containing the correct reason and source, and also checks for a corresponding halt notification in the returned prompts.*


### test_mixed_fatal_and_nonfatal (method, L170-L195, parent: TestAlertPolicyUnit)

> *Summary: This test verifies that an alert policy correctly processes a mix of fatal and non-fatal alerts. It asserts that the non-fatal warning is included in the resulting prompts while the fatal error triggers a `HaltEvent` being sent.*


### test_dedup_across_calls (method, L198-L213, parent: TestAlertPolicyUnit)

> *Summary: This test verifies that the alerting policy prevents duplicate notifications when `apply()` is called multiple times with the same set of input events. It asserts that subsequent calls yield fewer prompts than the initial call because identical alerts are deduplicated across invocations.*


### test_new_alerts_delivered_after_dedup (method, L216-L232, parent: TestAlertPolicyUnit)

> *Summary: This test verifies that new alerts are delivered even if a previously seen alert has been deduplicated. It simulates applying an alert policy with two alerts, asserting that the second call delivers only the non-deduplicated alert while suppressing the first one.*


### test_dedup_survives_history_replacement (method, L235-L252, parent: TestAlertPolicyUnit)

> *Summary: This test verifies that content-based deduplication persists even when alerts are reconstructed from storage. It confirms that two distinct alert objects with identical source, severity, and message are correctly identified as duplicates by the policy application.*


### test_multiple_fatals_uses_first_for_halt (method, L255-L279, parent: TestAlertPolicyUnit)

> *Summary: When provided with multiple `FATAL` alerts, this test verifies that the policy generates a single `HaltEvent` based on the first alert received. It confirms the resulting halt event correctly captures the source and reason of the initial fatal alert while including all input alerts in its details.*


### TestHaltCheckMiddleware (class, L282-L440)

> *Summary: This test suite verifies the behavior of a middleware that short-circuits an LLM process upon receiving a `FATAL` alert from observers. It tests scenarios including normal execution, halting after the first LLM call due to a fatal event, stream observation of halt events, and ensuring non-fatal alerts allow subsequent LLM calls.*


### test_no_halt_passes_through (method, L286-L295, parent: TestHaltCheckMiddleware)

> *Summary: This test verifies that when no fatal alerts are present, the agent processes the request normally by calling the LLM once and returning the expected body content. It asserts that the configuration client was successfully called exactly one time during this process.*


### test_halt_short_circuits_second_llm_call (method, L298-L339, parent: TestHaltCheckMiddleware)

> *Summary: This test verifies that a fatal alert triggered by the first Language Model response successfully halts subsequent processing. It confirms that only one LLM call occurs when an observer fires a `FATAL` alert after the initial tool execution.*


### test_halt_event_on_stream (method, L342-L375, parent: TestHaltCheckMiddleware)

> *Summary: This test verifies that a fatal observer triggers a `HaltEvent` when an agent processes a stream. It configures an agent with a specific tool call and a fatal observer, then asserts that at least one halt event is emitted during the interaction.*


### test_nonfatal_does_not_halt (method, L378-L408, parent: TestHaltCheckMiddleware)

> *Summary: This test verifies that a non-fatal warning alert does not cause the agent execution to halt. It initializes an agent with a warning observer and asserts that the process completes normally, resulting in two total LLM calls.*


### test_concurrent_fatal_from_two_observers (method, L411-L440, parent: TestHaltCheckMiddleware)

> *Summary: This test verifies that the system gracefully handles concurrent fatal alerts originating from two different observers during an agent interaction. It configures an agent with two custom observers, each designed to emit a `FATAL` alert upon processing events, and asserts the final response body contains "HALTED".*


### TestAlertPolicyOrdering (class, L443-L463)

> *Summary: Validates the correct ordering of `AlertPolicy` relative to other policies like `SlidingWindowPolicy` when passed to an assembler middleware. It asserts that placing alert before reduction yields no warnings, while placing reduction before alert generates a specific warning.*


### test_alert_before_reduction_no_warning (method, L446-L453, parent: TestAlertPolicyOrdering)

> *Summary: This test verifies that when an `AlertPolicy` precedes a `SlidingWindowPolicy`, the system produces no validation warnings. It achieves this by passing a list containing both policies to `AssemblerMiddleware.validate_order()` and asserting the returned warning list is empty.*


### test_reduction_before_alert_warns (method, L455-L463, parent: TestAlertPolicyOrdering)

> *Summary: This test verifies that placing a `SlidingWindowPolicy` before an `AlertPolicy` generates exactly one warning during middleware validation. The function asserts the presence of "alert" within this generated warning to confirm policy ordering constraints are enforced.*

