# test/beta/test_compact.py

6 class(es): TestTailWindowCompact, TestCompactionSummary, TestCompactTrigger, TestCompactionWiredOnAgent, _RaisingCompact, TestCompactionLifecycleEvents. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTailWindowCompact | class |  |
| TestCompactionSummary | class |  |
| TestCompactTrigger | class |  |
| TestCompactionWiredOnAgent | class |  |
| _RaisingCompact | class |  |
| TestCompactionLifecycleEvents | class |  |

## Chunks

### TestTailWindowCompact (class, L26-L65)

> *Summary: This test suite verifies the behavior of a window compaction mechanism by simulating event processing with varying input sizes and target limits. It asserts that the function correctly truncates events above the target size, retains all events below it, and optionally persists dropped events to a provided knowledge store.*


### test_no_op_below_target (method, L28-L33, parent: TestTailWindowCompact)

> *Summary: This test verifies that when the target size is set to 10 and only five input events are provided, no compaction operations occur. It asserts that the returned result contains all five original events unchanged.*


### test_truncates_above_target (method, L36-L42, parent: TestTailWindowCompact)

> *Summary: When provided with a list of ten input events and a target size of three, this test verifies that the compaction process returns only the last three events. The output confirms the resulting list has a length of 3, specifically containing the event corresponding to index 7.*


### test_persists_dropped_to_store (method, L45-L57, parent: TestTailWindowCompact)

> *Summary: This test verifies that when a `TailWindowCompact` processes a batch of input events, any events deemed too old or outside the target window are correctly persisted to the underlying knowledge store. It asserts that exactly one dropped event is recorded in the store after compaction completes.*


### test_no_persist_without_store (method, L60-L65, parent: TestTailWindowCompact)

> *Summary: This test verifies that a `TailWindowCompact` instance with a target of 3 correctly processes 10 input events without persisting state to storage. It asserts that the compaction process yields exactly 3 resulting compacted items.*


### TestCompactionSummary (class, L68-L72)

> *Summary: Verifies that a `CompactionSummary` object correctly initializes and stores provided string summaries and integer event counts. It confirms the internal state matches the input parameters during instantiation.*


### test_is_base_event (method, L69-L72, parent: TestCompactionSummary)

> *Summary: Verifies that a `CompactionSummary` object correctly stores and exposes its initial string summary and integer event count upon instantiation. It confirms the state matches the provided input values.*


### TestCompactTrigger (class, L75-L89)

> *Summary: This test suite verifies the initialization and configuration of a `CompactTrigger` object. It confirms that default values are set correctly and validates that custom inputs for maximum events, tokens, and characters per token are properly applied upon instantiation.*


### test_defaults (method, L76-L80, parent: TestCompactTrigger)

> *Summary: This test verifies the default configuration of a `CompactTrigger` instance. It asserts that the initial settings for maximum events and tokens are zero, while characters per token is set to four.*


### test_custom_values (method, L82-L85, parent: TestCompactTrigger)

> *Summary: This test verifies that a `CompactTrigger` instance correctly initializes with the provided maximum event and token limits. It asserts that the internal attributes match the input values (100 for events, 50000 for tokens).*


### test_custom_chars_per_token (method, L87-L89, parent: TestCompactTrigger)

> *Summary: Verifies that a `CompactTrigger` instance correctly stores the specified character limit per token when initialized with `chars_per_token=2`. The test confirms the internal state matches the input configuration.*


### TestCompactionWiredOnAgent (class, L92-L146)

> *Summary: Tests verify that an Agent configured with compaction emits a `CompactionCompleted` event when the event count exceeds a specified trigger threshold, and conversely, it does not emit such an event if the threshold is not crossed. The tests use in-memory stores and streams to simulate agent interactions and assert on the resulting compaction events.*


### test_fires_when_threshold_crossed (method, L97-L126, parent: TestCompactionWiredOnAgent)

> *Summary: This test verifies that a compaction process is triggered when the event count exceeds a defined threshold. It initializes an agent with a memory store and stream, then simulates four turns of interaction to ensure at least one `CompactionCompleted` event is emitted by the compactor strategy.*


### test_does_not_fire_below_threshold (method, L129-L146, parent: TestCompactionWiredOnAgent)

> *Summary: This test verifies that compaction events are not triggered when the event count remains below a specified threshold. It initializes an agent with a compacting knowledge store and asserts that no `CompactionCompleted` events are emitted after a single query.*


### _RaisingCompact (class, L149-L155)

> *Summary: This class implements a compaction strategy designed to fail intentionally. When its `compact` method is called with event data and storage objects, it immediately raises a `RuntimeError`.*


### compact (method, L154-L155, parent: _RaisingCompact)

> *Summary: This method is intended to process a list of `events` using provided `context` and `store`, but currently raises an error indicating it is unimplemented. It is expected to return a list upon successful execution.*


### TestCompactionLifecycleEvents (class, L159-L219)

> *Summary: This test suite verifies that compaction lifecycle events are correctly emitted to a stream. It asserts that the `CompactionStarted` event fires before processing begins and confirms that a `CompactionFailed` event is emitted when the configured compacting strategy raises an exception during execution.*


### test_started_event_fires_before_strategy_runs (method, L163-L189, parent: TestCompactionLifecycleEvents)

> *Summary: This test verifies that a `CompactionStarted` event is emitted immediately when an agent begins processing, even before the compaction strategy itself executes. It initializes an agent with specific knowledge and triggers multiple turns to confirm the event fires correctly for the designated compactor.*


### test_failed_event_fires_when_strategy_raises (method, L191-L219, parent: TestCompactionLifecycleEvents)

> *Summary: This test verifies that a `CompactionFailed` event is emitted when the configured compaction strategy raises an exception during agent execution. It initializes an agent with a failing compactor and asserts that exactly one failure event, containing specific error details, is captured while no completion events occur.*

