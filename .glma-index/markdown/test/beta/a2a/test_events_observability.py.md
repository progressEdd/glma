# test/beta/a2a/test_events_observability.py

1 class(es): TestA2AEventsReachClientStream. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestA2AEventsReachClientStream | class |  |

## Chunks

### TestA2AEventsReachClientStream (class, L20-L88)

> *Summary: This test suite verifies the event delivery mechanisms when interacting with a client via streaming and polling modes. It asserts that various events, such as `A2AEvent`s, task status updates (`A2ATaskStatusUpdate`), and initial snapshots (`A2ATaskSnapshot`), are correctly published to the user stream based on the request type.*


### test_streaming_publishes_a2a_events_to_user_stream (method, L21-L34, parent: TestA2AEventsReachClientStream)

> *Summary: This test verifies that an asynchronous request publishes specific `A2AEvent` types to a provided memory stream. It asserts that the collected events match the expected type and that at least one event was successfully published during the operation.*


### test_streaming_carries_final_text_on_completion_status (method, L36-L55, parent: TestA2AEventsReachClientStream)

> *Summary: This test verifies that when a streaming request completes, the final text content is delivered within the `COMPLETED` status update message rather than in intermediate chunks. It asserts that the response body matches the expected text and that the collected completion event contains the full text payload.*


### test_streaming_emits_completed_status_update (method, L57-L68, parent: TestA2AEventsReachClientStream)

> *Summary: This test verifies that a streaming request emits a completion status update when the underlying task finishes. It sends a "ping" command to a paired client and asserts that the collected stream events contain at least one instance of the `TASK_STATE_COMPLETED` state.*


### test_polling_publishes_initial_task_snapshot (method, L70-L88, parent: TestA2AEventsReachClientStream)

> *Summary: This test verifies that when using polling mode, the initial `A2ATaskSnapshot` event is correctly published to the user stream via the bootstrap response. It confirms this by asserting that at least one `A2ATaskSnapshot` instance is present in the collected events after an asynchronous request.*

