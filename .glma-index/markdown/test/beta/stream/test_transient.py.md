# test/beta/stream/test_transient.py

4 class(es): TestTransientFlag, TestTransientDelivery, TestTransientNotPersisted, TestPersistAll. 23 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTransientFlag | class |  |
| TestTransientDelivery | class |  |
| TestTransientNotPersisted | class |  |
| TestPersistAll | class |  |

## Chunks

### TestTransientFlag (class, L35-L78)

> *Summary: This test suite verifies the `__transient__` attribute across various event types. It asserts that certain events, like base or request/response messages, are marked as non-transient (`False`), while others, such as message chunks and progress updates, are correctly marked as transient (`True`).*


### test_base_event_not_transient (method, L38-L39, parent: TestTransientFlag)

> *Summary: Verifies that the `BaseEvent` class is explicitly marked as non-transient by asserting its `__transient__` attribute is `False`. This confirms the expected behavior for base event types.*


### test_model_request_not_transient (method, L41-L42, parent: TestTransientFlag)

> *Summary: Verifies that the `ModelRequest` object is explicitly marked as non-transient by asserting its internal `__transient__` attribute is `False`. This confirms the expected persistence behavior for this request type.*


### test_model_response_not_transient (method, L44-L45, parent: TestTransientFlag)

> *Summary: Verifies that the `ModelResponse` object is explicitly marked as non-transient by asserting its internal `__transient__` attribute is `False`. This confirms the expected persistence behavior for model responses.*


### test_tool_call_event_not_transient (method, L47-L48, parent: TestTransientFlag)

> *Summary: Verifies that the `ToolCallEvent` object is explicitly marked as non-transient. This assertion confirms the event's persistence status within the system.*


### test_task_started_not_transient (method, L50-L51, parent: TestTransientFlag)

> *Summary: Verifies that the `TaskStarted` event type is explicitly marked as non-transient by asserting its `__transient__` attribute is `False`. This confirms the expected persistence behavior for this specific task state.*


### test_task_completed_not_transient (method, L53-L54, parent: TestTransientFlag)

> *Summary: Verifies that the `TaskCompleted` state is explicitly marked as non-transient by asserting its `__transient__` attribute is `False`. This confirms the expected persistence behavior for this specific task completion status.*


### test_model_message_chunk_transient (method, L56-L57, parent: TestTransientFlag)

> *Summary: Verifies that the `ModelMessageChunk` class has its `__transient__` attribute set to `True`. This confirms the expected transient state for message chunks during testing.*


### test_model_message_transient (method, L59-L60, parent: TestTransientFlag)

> *Summary: Verifies that the `ModelMessage` class has its `__transient__` attribute set to `True`. This confirms the expected transient state for model messages during testing.*


### test_model_reasoning_transient (method, L62-L63, parent: TestTransientFlag)

> *Summary: Verifies that the `ModelReasoning` object has its transient flag set to `True`. This assertion confirms a specific state configuration for the model reasoning component.*


### test_task_progress_transient (method, L65-L66, parent: TestTransientFlag)

> *Summary: Verifies that the `TaskProgress` object correctly identifies itself as transient. This assertion checks a boolean flag set on the class instance.*


### test_observer_started_transient (method, L68-L69, parent: TestTransientFlag)

> *Summary: Verifies that the `ObserverStarted` state correctly flags itself as transient. This assertion confirms a specific internal property of the observer's lifecycle state.*


### test_observer_completed_transient (method, L71-L72, parent: TestTransientFlag)

> *Summary: Verifies that the `ObserverCompleted` state correctly flags itself as transient. This assertion confirms the expected behavior for handling temporary or non-final states within an observer pattern implementation.*


### test_compaction_completed_transient (method, L74-L75, parent: TestTransientFlag)

> *Summary: Verifies that the `CompactionCompleted` state correctly flags itself as transient. This assertion confirms the expected temporary nature of this specific completion status.*


### test_aggregation_completed_transient (method, L77-L78, parent: TestTransientFlag)

> *Summary: Verifies that the `AggregationCompleted` state correctly flags itself as transient. This assertion confirms the expected temporary nature of this specific aggregation completion status.*


### TestTransientDelivery (class, L81-L111)

> *Summary: Verifies that transient events, such as `ModelMessageChunk` and `TaskProgress`, are successfully delivered to subscribed handlers within a memory stream. It tests sending specific event types through the stream and asserts that the correct number and content of events are received by the subscriber callback.*


### test_chunk_delivered_to_subscriber (method, L85-L94, parent: TestTransientDelivery)

> *Summary: This test verifies that a sent message chunk is correctly delivered to an attached subscriber callback. It sends a `ModelMessageChunk` into a memory stream and asserts that the subscriber receives exactly one event containing the original content.*


### test_task_progress_delivered_to_subscriber (method, L97-L111, parent: TestTransientDelivery)

> *Summary: This test verifies that task progress events are correctly delivered to a subscriber. It sends a `TaskProgress` object into an in-memory stream and asserts that the subscriber receives exactly one event with the expected content.*


### TestTransientNotPersisted (class, L114-L210)

> *Summary: This test suite verifies that a `MemoryStream` correctly filters and retains only persistent events in its history, excluding transient types like message chunks, lifecycle markers, task progress updates, and compaction/aggregation completion signals. It confirms that core conversation events (like requests and responses) are always persisted while ephemeral events are discarded.*


### test_chunk_not_in_history (method, L118-L132, parent: TestTransientNotPersisted)

> *Summary: This test verifies that the stream history correctly captures initial requests and final responses while excluding intermediate chunk messages. It sends a sequence of request, chunks, and response events to assert that only `ModelRequest` and `ModelResponse` are present in the recorded event history.*


### test_lifecycle_events_not_in_history (method, L135-L149, parent: TestTransientNotPersisted)

> *Summary: This test verifies that specific lifecycle events, like `ObserverStarted` and `ObserverCompleted`, are excluded from the stream's history. It sends a sequence of events to an in-memory stream and asserts that only operational messages (`ModelRequest`, `ModelResponse`) remain in the recorded event log.*


### test_task_progress_not_in_history (method, L152-L183, parent: TestTransientNotPersisted)

> *Summary: This test verifies that intermediate progress updates are excluded from the event history. It sends a sequence of `TaskStarted`, two `TaskProgress` messages, and a final `TaskCompleted` message to a stream, asserting that only start and completion events remain in the retrieved history.*


### test_compaction_aggregation_not_in_history (method, L186-L197, parent: TestTransientNotPersisted)

> *Summary: This test verifies that specific completion events, `CompactionCompleted` and `AggregationCompleted`, are not recorded in the stream's history after being sent. It sends a sequence of requests and completions to a memory stream and asserts the absence of these event types in the retrieved history.*


### test_non_transient_events_all_persisted (method, L200-L210, parent: TestTransientNotPersisted)

> *Summary: This test verifies that all sent conversation events—including text input, tool calls, and model responses—are correctly persisted within the stream's history. It asserts that exactly three distinct events are retrieved after sending them sequentially to a `MemoryStream`.*


### TestPersistAll (class, L213-L245)

> *Summary: This test suite verifies that when `persist_all` is enabled on a stream, all event types—including message chunks and lifecycle events like `ObserverStarted` and `TaskProgress`—are correctly recorded in the stream's history. It asserts the presence of specific expected event types after sending various data through the stream context.*


### test_chunks_persisted_when_persist_all (method, L217-L229, parent: TestPersistAll)

> *Summary: This test verifies that when `persist_all` is enabled on a stream, all sent chunks are recorded in the history. It sends a sequence of requests and message chunks, then asserts that exactly two `ModelMessageChunk` events were captured by the stream's event log.*


### test_lifecycle_persisted_when_persist_all (method, L232-L245, parent: TestPersistAll)

> *Summary: This test verifies that when a stream is configured to persist all events, sending an `ObserverStarted` and a `TaskProgress` event results in both being recorded in the stream's history. It asserts that the collected list of historical events contains instances of both expected types.*

