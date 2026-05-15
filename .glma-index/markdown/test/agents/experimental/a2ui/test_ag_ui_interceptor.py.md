# test/agents/experimental/a2ui/test_ag_ui_interceptor.py

2 function(s): _make_response, _collect_events. 1 class(es): TestA2UIEventInterceptor. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_response | function |  |
| _collect_events | function |  |
| TestA2UIEventInterceptor | class |  |

## Chunks

### _make_response (function, L14-L21)

> *Summary: Constructs and returns a mock object resembling a service response. It initializes this mock with the provided string content, encapsulating it within a `message` dictionary structure.*


### _collect_events (function, L24-L29)

> *Summary: This asynchronous function iterates over an event stream provided by an interceptor, using a response object as input. It collects all yielded events into a list and returns this collection.*


### TestA2UIEventInterceptor (class, L32-L138)

> *Summary: This test suite verifies the functionality of an event interceptor designed to parse and extract structured A2UI events from response text. It confirms that valid JSON content is correctly parsed into events, while also testing edge cases like missing or invalid JSON, custom delimiters, and message stripping behavior.*


### test_extracts_a2ui_and_yields_event (method, L34-L48, parent: TestA2UIEventInterceptor)

> *Summary: This test verifies that an interceptor correctly extracts a specific UI event from a mock HTTP response containing embedded JSON data. It asserts that exactly one `a2ui-surface` event is yielded, and validates the structure of its content, confirming the presence and ID of a created surface operation.*


### test_strips_a2ui_from_response_text (method, L51-L61, parent: TestA2UIEventInterceptor)

> *Summary: This test verifies that an interceptor correctly removes a specific marker and embedded JSON data from a simulated response text. It takes a raw string containing the marker and JSON, processes it through the interceptor, and asserts the resulting message content is clean of the marker and extra data.*


### test_nulls_message_when_text_only_is_empty (method, L64-L70, parent: TestA2UIEventInterceptor)

> *Summary: When an A2UI event interceptor processes a JSON-formatted response containing only deletion instructions and no text content, the resulting message should be `None`. This test verifies that empty text fields do not trigger a message output from the interceptor.*


### test_no_a2ui_passes_through (method, L73-L81, parent: TestA2UIEventInterceptor)

> *Summary: This test verifies that when a non-UI response is processed, the event interceptor captures zero events. It confirms the original message content is preserved in the final response object.*


### test_none_message_passes_through (method, L84-L90, parent: TestA2UIEventInterceptor)

> *Summary: This test verifies that when a `None` message is processed by the interceptor, no events are generated. It asserts that the collection of emitted events remains empty after processing the input.*


### test_invalid_json_skipped (method, L93-L99, parent: TestA2UIEventInterceptor)

> *Summary: When provided with a response containing malformed JSON data, this test verifies that the interceptor correctly skips processing and yields no events. It asserts that the collected list of events remains empty when encountering invalid JSON input.*


### test_custom_delimiter (method, L102-L108, parent: TestA2UIEventInterceptor)

> *Summary: This test verifies that an event interceptor correctly parses a custom delimiter string. It feeds the interceptor a specific input containing the defined delimiter and asserts that exactly one resulting event is collected.*


### test_custom_activity_type (method, L111-L117, parent: TestA2UIEventInterceptor)

> *Summary: This test verifies that an event interceptor correctly captures a specific custom activity type. It feeds a predefined JSON response to the interceptor and asserts that the first collected event matches the expected `"custom-a2ui"` type.*


### test_multiple_operations (method, L120-L132, parent: TestA2UIEventInterceptor)

> *Summary: This test verifies that an event interceptor correctly captures multiple sequential operations from a simulated API response. It asserts that the collected events contain exactly one entry, which in turn holds two distinct operations.*


### test_default_interceptor_import (method, L135-L138, parent: TestA2UIEventInterceptor)

> *Summary: This test verifies that the `a2ui_event_interceptor` module is correctly imported and is a callable object within the testing environment. It confirms the expected structure of the interceptor component before further use.*

