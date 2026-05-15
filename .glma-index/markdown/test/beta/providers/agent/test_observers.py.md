# test/beta/providers/agent/test_observers.py

9 function(s): test_stream_observer_decorator_sees_responses, test_observer_sees_streamed_chunks, test_base_observer_event_watch_fires, test_base_observer_returns_alert_on_stream, test_token_monitor_builtin, test_loop_detector_builtin, test_alert_policy_fatal_halts_llm, test_observer_lifecycle_events_emitted, test_per_ask_observer_augments.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_stream_observer_decorator_sees_responses | function |  |
| test_observer_sees_streamed_chunks | function |  |
| test_base_observer_event_watch_fires | function |  |
| test_base_observer_returns_alert_on_stream | function |  |
| test_token_monitor_builtin | function |  |
| test_loop_detector_builtin | function |  |
| test_alert_policy_fatal_halts_llm | function |  |
| test_observer_lifecycle_events_emitted | function |  |
| test_per_ask_observer_augments | function |  |

## Chunks

### test_stream_observer_decorator_sees_responses (function, L32-L45)

> *Summary: This test verifies that an observer decorator correctly captures all `ModelResponse` events emitted by an `Agent`. It initializes the agent with a custom observer, sends a prompt, and asserts that at least one response event was recorded.*


### test_observer_sees_streamed_chunks (function, L48-L65)

> *Summary: This test verifies that an observer correctly receives and aggregates streamed content from an agent configured for streaming. It subscribes a callback to `ModelMessageChunk` events while the agent processes a request, asserting that all received chunks reconstruct the final response body.*


### test_base_observer_event_watch_fires (function, L68-L83)

> *Summary: This test verifies that an observer configured with `EventWatch(ModelResponse)` is triggered upon receiving a model response during an agent's interaction. It asserts that the observer's processing method was called at least once and received at least one event.*


### test_base_observer_returns_alert_on_stream (function, L86-L108)

> *Summary: This test verifies that a custom observer emits an `ObserverAlert` when processing events from the agent's stream. It configures an agent with a noisy observer and asserts that at least one warning alert is captured on the output stream.*


### test_token_monitor_builtin (function, L111-L125)

> *Summary: This test verifies that the `TokenMonitor` correctly tracks token usage and triggers alerts when an agent responds to a prompt. It initializes the monitor with low thresholds, runs an agent query, and asserts that both total tokens are counted and at least one alert is generated.*


### test_loop_detector_builtin (function, L128-L162)

> *Summary: This test verifies that the `LoopDetector` correctly emits an alert when a tool is called repeatedly. It simulates an agent interacting with a status function that returns "pending" for the first three calls, ensuring the detector fires despite the LLM eventually exiting its retry loop naturally.*


### test_alert_policy_fatal_halts_llm (function, L165-L212)

> *Summary: This test verifies that a `FATAL` observer alert, processed by an `AlertPolicy`, correctly halts the LLM execution flow. It sets up an agent with a custom observer that emits a fatal alert on the first response and asserts that the resulting reply either contains a "HALTED" marker or registers at least one `HaltEvent`.*


### test_observer_lifecycle_events_emitted (function, L215-L236)

> *Summary: This test verifies that the `Agent` emits lifecycle events for its registered observers during execution. It subscribes to `ObserverStarted` and `ObserverCompleted` events on a stream, then asserts that two instances of each event are emitted when running the agent with two observers.*


### test_per_ask_observer_augments (function, L239-L250)

> *Summary: This test verifies that observers provided to the `.ask()` method are only active for that specific turn. It initializes an agent, attaches a response observer that captures content, and asserts that the captured content is present after calling `agent.ask()`.*

