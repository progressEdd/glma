# test/beta/observer/test_builtin.py

4 class(es): TestTokenMonitor, TestLoopDetector, _SelfAwareObserver, TestObserverLifecycleSelfVisibility. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTokenMonitor | class |  |
| TestLoopDetector | class |  |
| _SelfAwareObserver | class |  |
| TestObserverLifecycleSelfVisibility | class |  |

## Chunks

### TestTokenMonitor (class, L28-L218)

> *Summary: This test suite verifies the `TokenMonitor`'s behavior by simulating token usage events through a streaming context. It asserts that the monitor correctly tracks cumulative tokens from various inputs (like `ModelResponse` and `TaskCompleted`), emits appropriate severity alerts (WARNING, CRITICAL) based on configured thresholds, handles resets, and ignores events lacking usage data.*


### test_no_signal_below_threshold (method, L29-L44, parent: TestTokenMonitor)

> *Summary: This test verifies that no alerts are generated when the token count remains below a specified warning threshold. It sends a response with 50 tokens to a stream monitored by `TokenMonitor` and asserts that zero signals were recorded while confirming the monitor correctly tracked the total tokens sent.*


### test_warning_at_threshold (method, L46-L60, parent: TestTokenMonitor)

> *Summary: This test verifies that a `TokenMonitor` correctly emits a warning signal when the token usage crosses a predefined threshold. It sends a response with 110 tokens to a stream monitored by the setup, asserting exactly one warning signal is received.*


### test_critical_at_threshold (method, L62-L77, parent: TestTokenMonitor)

> *Summary: This test verifies that a `TokenMonitor` correctly emits a `CRITICAL` alert when the input usage exceeds both warning and alert thresholds. It sends data exceeding 200 tokens to a stream monitored by the setup, asserting that exactly one critical signal is generated.*


### test_reset_clears_counter_and_allows_rewarning (method, L79-L98, parent: TestTokenMonitor)

> *Summary: This test verifies that calling `reset()` on a token monitor clears its accumulated usage count while preserving the ability to trigger subsequent alerts and warnings. It sends two data points, asserts the first one triggers an alert, resets the monitor, and then confirms the second point correctly increments the signal count after the reset.*


### test_task_completed_usage (method, L100-L124, parent: TestTokenMonitor)

> *Summary: This test verifies that a `TokenMonitor` correctly processes a `TaskCompleted` event containing usage data. It sends the event to a stream and asserts that the monitor's token count is updated while no alerts are triggered.*


### test_task_completed_triggers_warning (method, L126-L150, parent: TestTokenMonitor)

> *Summary: This test verifies that sending a `TaskCompleted` event with usage below the alert threshold but above the warning threshold correctly triggers a `WARNING` signal from the token monitor. It uses an in-memory stream and context to simulate the monitoring process and asserts one warning signal was generated.*


### test_cumulative_across_model_and_task (method, L152-L178, parent: TestTokenMonitor)

> *Summary: This test verifies that token usage from both `ModelResponse` and `TaskCompleted` events correctly accumulates within a monitoring context. It asserts the total tokens sum to 110 and confirms one warning alert was generated based on the configured thresholds.*


### test_empty_usage_ignored (method, L180-L202, parent: TestTokenMonitor)

> *Summary: This test verifies that the monitoring system correctly ignores events lacking usage data. It sends a `ModelResponse` and a `TaskCompleted` event with default (empty) usage to an observer registered on a memory stream, asserting that the total token count remains zero.*


### test_warning_only_emitted_once (method, L204-L218, parent: TestTokenMonitor)

> *Summary: This test verifies that a `TokenMonitor` emits its warning alert only once, even when multiple events are sent to the stream. It asserts that exactly one signal is captured after sending two distinct usage updates.*


### TestLoopDetector (class, L222-L293)

> *Summary: These asynchronous tests verify the `LoopDetector`'s behavior by simulating event streams. It confirms that a signal is emitted only when an identical sequence of events repeats beyond a specified threshold, and also validates that calling `reset()` clears history to allow subsequent detection.*


### test_no_signal_below_threshold (method, L223-L237, parent: TestLoopDetector)

> *Summary: This test verifies that no alerts are generated when the number of identical events falls below a specified threshold. It sends two identical `ToolCallEvent`s to a stream configured with a detector set to require three repetitions before signaling.*


### test_signals_on_loop (method, L239-L255, parent: TestLoopDetector)

> *Summary: This test verifies that a `LoopDetector` correctly emits a single warning signal when three identical tool calls are sent sequentially through a stream context. It confirms the resulting alert contains specific severity and message content related to loop detection.*


### test_different_calls_no_signal (method, L257-L272, parent: TestLoopDetector)

> *Summary: This test verifies that a `LoopDetector` with a threshold of 3 does not emit any alerts when three distinct, non-looping tool calls are sent through a stream. It confirms the absence of signals by asserting an empty list after sending sequential `ToolCallEvent`s.*


### test_reset_clears_history_and_allows_redetection (method, L274-L293, parent: TestLoopDetector)

> *Summary: This test verifies that calling `reset()` on a detector clears its internal history while preserving the ability to detect subsequent events. It confirms that sending the same sequence of input events before and after resetting results in two separate detection alerts being recorded.*


### _SelfAwareObserver (class, L296-L310)

> *Summary: This observer monitors its own lifecycle events (`ObserverStarted` and `ObserverCompleted`). It accepts a name during initialization and records the names of itself when these specific start or completion events occur within its processing loop.*


### __init__ (method, L299-L302, parent: _SelfAwareObserver)

> *Summary: Initializes an observer instance with a given name and automatically subscribes it to `ObserverStarted` and `ObserverCompleted` events. It also sets up internal lists to track which start and completion events have been observed.*


### process (method, L304-L310, parent: _SelfAwareObserver)

> *Summary: Iterates through a list of events to track observer lifecycle states. It appends the name of an event to either `started_seen` or `completed_seen` lists based on whether it is an `ObserverStarted` or `ObserverCompleted` instance.*


### TestObserverLifecycleSelfVisibility (class, L314-L347)

> *Summary: This test suite verifies that an observer correctly receives its own lifecycle events, specifically `ObserverStarted` after registration and `ObserverCompleted` before unregistration. It also confirms that external subscribers attached to the agent's stream receive notifications when the agent starts processing.*


### test_observer_sees_own_started_and_completed (method, L322-L332, parent: TestObserverLifecycleSelfVisibility)

> *Summary: This test verifies that a self-aware observer correctly records its own start and completion events when an agent is executed. It asserts that the observer's tracking lists contain the identifier "self-aware" after the agent completes its task.*


### test_external_subscriber_also_sees_started (method, L334-L347, parent: TestObserverLifecycleSelfVisibility)

> *Summary: This test verifies that an external subscriber attached to a `MemoryStream` receives lifecycle events emitted by an `Agent`. It asserts that the external observer captures exactly one event, confirming the agent's internal observers are also visible externally.*

