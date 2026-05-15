# test/beta/policies/test_sliding_window.py

2 function(s): _tool_response, _tool_results. 3 class(es): TestNoTrimming, TestTrimming, TestOrphanedToolResults. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _tool_response | function |  |
| _tool_results | function |  |
| TestNoTrimming | class |  |
| TestTrimming | class |  |
| TestOrphanedToolResults | class |  |

## Chunks

### _tool_response (function, L20-L24)

> *Summary: Generates a standardized `ModelResponse` object simulating a tool execution result. It constructs the response to contain a single `ToolCallEvent` matching the provided `call_id` and `name`.*


### _tool_results (function, L27-L30)

> *Summary: Constructs a `ToolResultsEvent` containing a single successful tool result. It accepts optional parent and tool names to populate the event's data structure.*


### TestNoTrimming (class, L33-L51)

> *Summary: This test suite verifies that a `SlidingWindowPolicy` correctly retains all input events when the number of events does not exceed the defined maximum limit. It asserts that the resulting event list matches the original input and no prompts are generated in these scenarios.*


### test_events_within_limit_are_unchanged (method, L35-L42, parent: TestNoTrimming)

> *Summary: When applying a `SlidingWindowPolicy` with a limit of 5 to two input events, the function asserts that the resulting output matches the original input events and no prompts were generated. This confirms that events within the defined window size are passed through unmodified.*


### test_events_at_exact_limit (method, L45-L51, parent: TestNoTrimming)

> *Summary: This test verifies that a `SlidingWindowPolicy` correctly retains all input events when the maximum allowed limit is exactly met. It applies the policy to two events with a configured window size of two and asserts the output matches the input list.*


### TestTrimming (class, L54-L76)

> *Summary: This test suite verifies the behavior of a sliding window policy by applying it to a sequence of input events. It asserts that the policy correctly retains only the most recent $N$ events, and also tests a transparent mode where existing context is preserved while new events are added.*


### test_keeps_last_n_events (method, L56-L64, parent: TestTrimming)

> *Summary: This test verifies that a `SlidingWindowPolicy` correctly retains only the most recent $N$ events. It applies the policy to five input events with a maximum window size of two, asserting the output contains exactly the last two events (events 3 and 4).*


### test_transparent_adds_prompt (method, L67-L76, parent: TestTrimming)

> *Summary: This test verifies that a transparent sliding window policy correctly processes a sequence of five input events. It asserts that the resulting output contains two elements, with the first retaining an existing prompt and the second incorporating data from both the second and fifth input events.*


### TestOrphanedToolResults (class, L79-L202)

> *Summary: This test suite verifies the behavior of a sliding window policy when handling orphaned `ToolResultsEvents`. It asserts that events lacking a corresponding tool use are correctly dropped, whether they appear at the beginning, middle, or end of the input stream, while ensuring paired events remain intact.*


### test_leading_orphaned_tool_result_is_skipped (method, L83-L97, parent: TestOrphanedToolResults)

> *Summary: This test verifies that an orphaned tool result event is skipped when applying a sliding window policy with a maximum size of three. It asserts the resulting event list contains only two items: the initial `ModelRequest` and the final `ModelRequest`.*


### test_multiple_leading_orphaned_tool_results_are_skipped (method, L100-L114, parent: TestOrphanedToolResults)

> *Summary: When processing a sequence of events with a sliding window of size three, this test verifies that multiple initial tool results lacking corresponding requests are ignored. The function expects the final output to contain only the single `ModelRequest` event after filtering out the leading orphaned tool result events.*


### test_non_leading_tool_result_is_kept (method, L117-L133, parent: TestOrphanedToolResults)

> *Summary: This test verifies that a sliding window policy correctly retains the most recent three events when processing a sequence containing tool responses and requests. It asserts that after applying the policy to a specific event stream, the resulting list contains exactly three elements with expected types at each position.*


### test_transparent_count_reflects_skipped_orphans (method, L136-L149, parent: TestOrphanedToolResults)

> *Summary: This test verifies that a transparent sliding window policy correctly reflects the count of events, even when some are skipped orphans. It applies the policy to a sequence of mixed tool responses and model requests, asserting the final prompt contains specific counts derived from the processed events.*


### test_mid_window_orphaned_tool_result_is_dropped (method, L152-L166, parent: TestOrphanedToolResults)

> *Summary: This test verifies that an orphaned `ToolResultsEvent` occurring within the sliding window is correctly dropped by the policy. It processes a sequence of events, including one orphan inside the window, asserting that only valid requests remain in the final output.*


### test_paired_tool_call_and_result_within_window_are_kept (method, L169-L182, parent: TestOrphanedToolResults)

> *Summary: This test verifies that a tool call and its corresponding results remain within the sliding window when the window size is set to three. It asserts that the resulting event list contains all three input events, specifically confirming the presence of the `ToolResultsEvent`.*


### test_orphan_results_at_multiple_positions_are_dropped (method, L185-L202, parent: TestOrphanedToolResults)

> *Summary: This test verifies that orphaned tool results scattered throughout a sequence are correctly dropped when applying a sliding window policy with a maximum event limit of 5. It asserts the resulting list contains only model requests, specifically those corresponding to inputs "a" and "b".*

