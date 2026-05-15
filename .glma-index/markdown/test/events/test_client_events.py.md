# test/events/test_client_events.py

1 function(s): test__change_usage_summary_format. 2 class(es): TestUsageSummaryEvent, TestStreamEvent. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test__change_usage_summary_format | function |  |
| TestUsageSummaryEvent | class |  |
| TestStreamEvent | class |  |

## Chunks

### test__change_usage_summary_format (function, L70-L76)

> *Summary: This test verifies that a specific transformation function correctly restructures usage data. It takes actual and total usage summaries as input and asserts the resulting dictionary matches a predefined expected format.*


### TestUsageSummaryEvent (class, L79-L316)

> *Summary: This test suite verifies the serialization and printing behavior of a `UsageSummaryEvent` by testing various combinations of actual and total usage summaries (including `None`). It asserts that the event correctly serializes to a specific dictionary structure and that its `print` method outputs expected formatted strings based on the input data.*


### test_usage_summary_print_same_actual_and_total (method, L105-L176, parent: TestUsageSummaryEvent)

> *Summary: This test verifies that an event object correctly serializes its usage data into a specific JSON structure and that its `print` method outputs a predefined sequence of formatted strings to a mocked stream. It accepts actual and total usage summaries, along with a UUID, as inputs for this validation.*


### test_usage_summary_print_different_actual_and_total (method, L203-L276, parent: TestUsageSummaryEvent)

> *Summary: This test verifies that an event object correctly serializes its usage data into a specific JSON structure and also confirms that its `print` method outputs the expected formatted summary to a mocked stream. It takes actual and total usage summaries, along with a UUID, as inputs to perform these assertions.*


### test_usage_summary_print_none_actual_and_total (method, L287-L316, parent: TestUsageSummaryEvent)

> *Summary: This test verifies that when provided with `None` for both actual and total usage summaries, the event correctly serializes to a specific structure containing null values. Furthermore, it asserts that calling the print method on this event results in a specific warning message being logged.*


### TestStreamEvent (class, L319-L345)

> *Summary: This test verifies the behavior of a `StreamEvent` instance by asserting its structure matches an expected dictionary representation and confirming that its `print` method outputs specific ANSI-colored strings to a mocked file stream. It ensures the event correctly serializes and prints formatted content.*


### test_print (method, L320-L345, parent: TestStreamEvent)

> *Summary: This test verifies that a `StreamEvent` object correctly serializes its data into a specific dictionary structure and that its `print` method outputs predefined ANSI-colored strings to a mocked file stream. It asserts the exact sequence of calls made to the mock object during printing.*

