# test/beta/stream/test_stream.py

2 function(s): test_play_py_scenario, test_context_propagates_to_substream. 5 class(es): TestStreamSend, TestStreamWhereTypeFilter, TestStreamWhereConditionFilter, TestStreamChainedFilters, TestStreamSubscription. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestStreamSend | class |  |
| TestStreamWhereTypeFilter | class |  |
| TestStreamWhereConditionFilter | class |  |
| TestStreamChainedFilters | class |  |
| TestStreamSubscription | class |  |
| test_play_py_scenario | function |  |
| test_context_propagates_to_substream | function |  |

## Chunks

### TestStreamSend (class, L13-L49)

> *Summary: These tests verify the `MemoryStream`'s event broadcasting mechanism by simulating sending events to one or multiple registered subscribers. It confirms that each sent event is correctly delivered to all subscribed callbacks, regardless of whether it's a single or batch operation.*


### test_send_event_to_single_subscriber (method, L15-L22, parent: TestStreamSend)

> *Summary: This test verifies that an event sent to a stream is correctly delivered to its single registered subscriber. It initializes a `MemoryStream`, subscribes a mock function, sends a specific `ToolCallEvent`, and asserts the mock was called exactly once with that event.*


### test_send_event_to_multiple_subscribers (method, L25-L34, parent: TestStreamSend)

> *Summary: This test verifies that an event sent to a `MemoryStream` is correctly delivered to all registered subscribers. It asserts that both mocked listeners receive the exact same event object after the stream sends it.*


### test_send_multiple_events (method, L37-L49, parent: TestStreamSend)

> *Summary: This test verifies that a `MemoryStream` correctly relays multiple sequential events to a subscribed mock object. It sends three distinct events—two `ToolCallEvent`s and one `ModelMessage`—and asserts the mock received them in the exact order sent.*


### TestStreamWhereTypeFilter (class, L52-L93)

> *Summary: These tests verify the filtering behavior of a stream pipeline by applying type constraints to incoming events. It confirms that only events matching the specified types (single or union) are passed downstream to subscribed mocks, while non-matching events are ignored.*


### test_where_type_filter_by_type (method, L54-L67, parent: TestStreamWhereTypeFilter)

> *Summary: This test verifies that a type filter correctly processes events from a stream. It sends a sequence of mixed `ToolCallEvent` and `ModelMessage` objects into the stream and asserts that the subscribed mock only receives the `ToolCallEvent` instances.*


### test_where_type_filter_by_union_type (method, L70-L81, parent: TestStreamWhereTypeFilter)

> *Summary: This test verifies that a stream filter correctly processes events belonging to a union type (`ToolCallEvent | ModelMessage`). It sends both types of events into the stream and asserts that the subscribed mock receives all sent events in order.*


### test_where_type_filter_no_match (method, L84-L93, parent: TestStreamWhereTypeFilter)

> *Summary: This test verifies that no callbacks are triggered when a stream is filtered to only include `ToolCallEvent`s, but the sent messages do not match that type. It sends two generic `ModelMessage` responses and asserts that the subscribed mock handler remains uncalled.*


### TestStreamWhereConditionFilter (class, L96-L126)

> *Summary: This test suite verifies that a stream filter correctly processes events based on a specified condition, such as matching a tool call name. It sends various events into a `MemoryStream` and asserts that the subscribed mock handler only receives events meeting the defined criteria.*


### test_where_condition_filter_by_condition (method, L98-L112, parent: TestStreamWhereConditionFilter)

> *Summary: This test verifies that a stream filter correctly selects only events matching a specific condition (`ToolCallEvent.name == "func1"`). It sends a sequence of mixed events into the stream and asserts that the subscribed mock receives only the two events satisfying the filter criteria.*


### test_where_condition_filter_toolcall_name_no_match (method, L115-L126, parent: TestStreamWhereConditionFilter)

> *Summary: This test verifies that a subscription filtered for a specific tool call name (`"func1"`) receives no calls when the input stream contains events with different names (`"func2"` and `"func3"`). It confirms that the mock handler remains uncalled because none of the sent events match the filter criteria.*


### TestStreamChainedFilters (class, L129-L157)

> *Summary: This test verifies the behavior of chained filters on a data stream by sending various events and asserting which mock subscribers receive them. It demonstrates that only events matching all applied filter criteria are passed down the chain, including testing scenarios where no event matches the combined filters.*


### test_chained_type_and_condition_filters (method, L131-L145, parent: TestStreamChainedFilters)

> *Summary: This test verifies chained filtering on a stream by sending three events: two `ToolCallEvent`s and one `ModelMessage`. It asserts that the initial subscription receives all three, the intermediate filter for `ToolCallEvent` receives both tool calls, and the final filter specifically matching `"func1"` only receives the first tool call.*


### test_unreachable_filter_scenario (method, L148-L157, parent: TestStreamChainedFilters)

> *Summary: This test verifies that a stream configured with sequential filters (`ToolCallEvent` then `ModelMessage`) correctly ignores subsequent events not matching the final filter. It sends three events, but since only the second event matches both criteria, the mock subscriber should never be called for the first or third events.*


### TestStreamSubscription (class, L160-L185)

> *Summary: This test suite verifies the subscription and unsubscription mechanisms of a stream object. It confirms that multiple subscribers receive all sent events, and conversely, unsubscribing correctly stops a specific subscriber from receiving subsequent events.*


### test_multiple_subscribers_same_stream (method, L162-L172, parent: TestStreamSubscription)

> *Summary: This test verifies that multiple subscribers receive all emitted events from a single stream instance. It sends two distinct events to the `MemoryStream` and asserts that both registered mocks were called exactly twice.*


### test_unsubscribe_stops_receiving_events (method, L175-L185, parent: TestStreamSubscription)

> *Summary: This test verifies that unsubscribing from a stream halts event reception. It subscribes a mock callback, sends an initial event which is captured by the mock, then unsubscribes, and finally sends a second event that should not trigger the mock.*


### test_play_py_scenario (function, L189-L226)

> *Summary: This test verifies event propagation through a stream by sending specific `ToolCallEvent` and `ModelMessage` instances into a `MemoryStream`. It asserts that various subscribed listeners receive the correct number of events, specifically checking which specialized listeners are triggered based on event type and name.*


### test_context_propagates_to_substream (function, L230-L242)

> *Summary: This test verifies that a provided `Context` object is correctly passed down to downstream streams. It sends an event through a stream configured with a listener, asserting the listener receives the exact context sent during the send operation.*

