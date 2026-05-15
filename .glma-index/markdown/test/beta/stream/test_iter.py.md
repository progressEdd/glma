# test/beta/stream/test_iter.py

1 class(es): TestStreamSend. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestStreamSend | class |  |

## Chunks

### TestStreamSend (class, L14-L83)

> *Summary: This test suite verifies the behavior of a `MemoryStream` by simulating event sending and subscription via asynchronous iterators. It confirms that subscribers receive sent events correctly, respects message limits when configured, and filters messages based on type using stream methods like `.where()`.*


### test_send_event_to_iter_subscriber (method, L16-L36, parent: TestStreamSend)

> *Summary: This test verifies that an event sent to a stream is correctly received and processed by an iterator subscriber. It sends a `ToolCallEvent` into a `MemoryStream`, asserts the mock callback was called with the event, and confirms the mocked iteration method was subsequently called on that event.*


### test_iter_subscriber_max_msgs (method, L39-L59, parent: TestStreamSend)

> *Summary: This test verifies that a stream subscriber correctly limits the number of processed events to a specified maximum. It sends five messages into a memory stream configured for two events and asserts that the mock handler was only called twice.*


### test_iter_substream (method, L62-L83, parent: TestStreamSend)

> *Summary: This test verifies that a specific event type (`ToolCallEvent`) is correctly processed when sent into a stream filtered for that type. It sends both a `ModelMessage` and the target `ToolCallEvent`, asserting that the mock handler receives exactly one call with the expected `ToolCallEvent`.*

