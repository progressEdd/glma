# test/beta/test_watch.py

8 class(es): TestEventWatch, TestCadenceWatch, TestIntervalWatch, TestDelayWatch, TestAllOf, TestAnyOf, TestSequence, TestCronWatchExpressions. 38 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestEventWatch | class |  |
| TestCadenceWatch | class |  |
| TestIntervalWatch | class |  |
| TestDelayWatch | class |  |
| TestAllOf | class |  |
| TestAnyOf | class |  |
| TestSequence | class |  |
| TestCronWatchExpressions | class |  |

## Chunks

### TestEventWatch (class, L25-L90)

> *Summary: This test suite verifies the functionality of an `EventWatch` mechanism, which monitors a data stream for specific events. It confirms that the watch fires only when matching events are sent to the stream and stops firing immediately after being disarmed.*


### test_fires_on_matching_event (method, L27-L42, parent: TestEventWatch)

> *Summary: This test verifies that an `EventWatch` triggers its callback when a specific event type arrives on the stream. It sends a `ToolCallEvent` to a memory stream and asserts that the registered callback receives exactly one matching event.*


### test_does_not_fire_on_non_matching (method, L45-L57, parent: TestEventWatch)

> *Summary: This test verifies that an `EventWatch` does not trigger when the input message content does not match the watched event type. It sends a non-matching message to a memory stream and asserts that no events are received by the registered callback.*


### test_condition_filter (method, L60-L73, parent: TestEventWatch)

> *Summary: This test verifies that an `EventWatch` correctly filters incoming events based on a specified condition. It sends a mix of tool call events to a memory stream and asserts that only the event matching the "search" name is captured by the provided callback.*


### test_disarm_stops_firing (method, L76-L90, parent: TestEventWatch)

> *Summary: This test verifies that an `EventWatch` stops receiving events after being disarmed. It arms the watcher, immediately disarms it, and then sends a `ToolCallEvent`, asserting that no events are captured in the callback.*


### TestCadenceWatch (class, L93-L320)

> *Summary: This test suite verifies the behavior of a batching mechanism that triggers based on either reaching a specified event count (`n`) or exceeding a maximum waiting time (`max_wait`). It tests various scenarios including successful triggering by count, timeout-based flushing, disarming, and complex interactions between concurrent events and callbacks.*


### test_fires_after_n_events (method, L95-L111, parent: TestCadenceWatch)

> *Summary: This test verifies that a `CadenceWatch` triggers its callback only after accumulating a specified number of events. It sends five `ToolCallEvent`s to the watch, asserting that exactly one batch containing three events is recorded when the threshold ($n=3$) is met.*


### test_multiple_batches (method, L114-L128, parent: TestCadenceWatch)

> *Summary: This test verifies that a `CadenceWatch` instance configured for two batches correctly processes multiple incoming messages from a memory stream. It sends four distinct model messages and asserts that the callback receives exactly two resulting event batches.*


### test_disarm_clears_buffer (method, L131-L144, parent: TestCadenceWatch)

> *Summary: This test verifies that disarming a `CadenceWatch` instance clears any buffered events. It sends messages to the watch, then calls `disarm()`, asserting that no callbacks were executed and thus no batches were recorded.*


### test_fires_on_timeout (method, L147-L164, parent: TestCadenceWatch)

> *Summary: This test verifies that a `CadenceWatch` triggers after a specified timeout if the target condition is not met within the allotted time. It sends two events to a stream and waits longer than the watch's configured maximum wait period, asserting that the callback receives both events in a single batch.*


### test_n_wins_when_reached_before_timeout (method, L167-L183, parent: TestCadenceWatch)

> *Summary: This test verifies that a `CadenceWatch` triggers immediately when the required number of events (`n=2`) is received, even if the configured maximum wait time has not elapsed. It sends two messages to an in-memory stream and asserts that the callback receives both events in a single batch.*


### test_timeout_wins_when_n_not_reached (method, L186-L201, parent: TestCadenceWatch)

> *Summary: This test verifies that a timeout mechanism correctly triggers when the expected number of events is not received within the allotted time. It sends one message to a stream and asserts that only one batch containing that single event is captured by the watcher after a delay longer than the configured `max_wait`.*


### test_requires_at_least_one_trigger (method, L203-L205, parent: TestCadenceWatch)

> *Summary: Asserts that instantiating `CadenceWatch` without providing either an `'n'` or `'max_wait'` argument raises a `ValueError`. This confirms the class requires at least one trigger parameter upon initialization.*


### test_rejects_non_positive_n (method, L207-L209, parent: TestCadenceWatch)

> *Summary: Asserts that instantiating `CadenceWatch` with a non-positive value for the `n` parameter raises a `ValueError` containing the specific message "'n' must be positive". This verifies input validation for the watch object.*


### test_rejects_non_positive_max_wait (method, L211-L213, parent: TestCadenceWatch)

> *Summary: Asserts that instantiating `CadenceWatch` with a non-positive `max_wait` value raises a `ValueError`. This verifies the input validation for the maximum waiting period.*


### test_count_trigger_cancels_pending_timer (method, L216-L234, parent: TestCadenceWatch)

> *Summary: This test verifies that when a count-based trigger fires, any pending timers are correctly canceled. It sends two messages to an armed watch, asserts the immediate batch is captured, and then waits longer than the maximum wait time to ensure no subsequent phantom batches are generated.*


### test_timer_restarts_after_count_flush (method, L237-L258, parent: TestCadenceWatch)

> *Summary: This test verifies that a `CadenceWatch` restarts its internal timer after a count-based flush. It sends two initial messages to trigger the first batch, then sends one more message and waits for a timeout to ensure a second, fresh batch is flushed.*


### test_events_during_slow_callback_are_not_stranded (method, L261-L295, parent: TestCadenceWatch)

> *Summary: This test verifies that events are not lost when a processing callback is slow. It simulates sending multiple waves of messages to a `CadenceWatch` while its callbacks are executing, asserting that all sent content eventually appears in the delivered list.*


### test_count_fires_after_timer_flush (method, L298-L320, parent: TestCadenceWatch)

> *Summary: This test verifies that a `CadenceWatch` correctly triggers after a timer flush, even if it has already fired once. It sends initial events to trigger the first batch, then sends subsequent events in a loop to ensure the watch fires again with all accumulated data.*


### TestIntervalWatch (class, L323-L357)

> *Summary: This test suite verifies the functionality of an `IntervalWatch` by asserting that it fires callbacks at a specified periodic interval when armed. It also confirms that calling `disarm()` immediately stops any further callback executions, even after a delay.*


### test_fires_periodically (method, L325-L341, parent: TestIntervalWatch)

> *Summary: This test verifies that an `IntervalWatch` triggers its callback periodically based on a set interval. It arms the watch, waits for a duration longer than several intervals, and asserts that the provided callback was invoked at least twice before disarming it.*


### test_disarm_stops_timer (method, L344-L357, parent: TestIntervalWatch)

> *Summary: This test verifies that calling `disarm()` on an `IntervalWatch` immediately stops its periodic callbacks. It initializes the watch, arms it to fire every 0.05 seconds, disarms it, and then asserts that no callback was executed after a short delay.*


### TestDelayWatch (class, L360-L391)

> *Summary: This test suite verifies the behavior of a `DelayWatch` mechanism by asserting that it fires its registered callback exactly once after a specified delay if left active, and conversely, it does not fire if explicitly disarmed before the delay elapses. It uses asynchronous testing with `MemoryStream` to simulate event streams for verification.*


### test_fires_once_after_delay (method, L362-L375, parent: TestDelayWatch)

> *Summary: This test verifies that a `DelayWatch` triggers its registered callback exactly once after a specified delay, even if the stream provides data earlier. It confirms the watcher automatically disarms itself upon firing.*


### test_disarm_before_fire (method, L378-L391, parent: TestDelayWatch)

> *Summary: This test verifies that a `DelayWatch` does not trigger its callback if it is disarmed before the specified delay elapses. It initializes the watch, arms it with a stream and callback, immediately disarms it, waits briefly, and asserts that the callback was never invoked.*


### TestAllOf (class, L394-L470)

> *Summary: These tests verify the behavior of an `AllOf` watch, ensuring it only triggers when all constituent event watches have fired. It confirms that upon triggering, the callback receives a combined list containing events from every sub-watch and that the watcher resets correctly for subsequent cycles.*


### test_fires_when_all_sub_watches_fired (method, L396-L416, parent: TestAllOf)

> *Summary: This test verifies that an `AllOf` watch only triggers when all its constituent event watches have been activated. It sends a sequence of events, asserting that the callback is not invoked after the first event but fires once after the second event completes both conditions.*


### test_collects_events_from_all_sub_watches (method, L419-L445, parent: TestAllOf)

> *Summary: This test verifies that an `AllOf` watch correctly aggregates all emitted events from its constituent sub-watches. It sends a sequence of distinct events through the stream and asserts that the callback receives a single collection containing both input events.*


### test_resets_after_firing (method, L448-L470, parent: TestAllOf)

> *Summary: This test verifies that an event watcher correctly captures events across multiple cycles of input streaming. It sends pairs of `ToolCallEvent` and `ModelMessage` sequentially, asserting that the callback receives a distinct list for each pair sent.*


### TestAnyOf (class, L473-L493)

> *Summary: This test verifies that an `AnyOf` watcher fires callbacks when either of its registered event types is received from a stream. It confirms the watcher correctly accumulates events from both `ToolCallEvent` and `ModelMessage` inputs.*


### test_fires_on_either_watch (method, L475-L493, parent: TestAnyOf)

> *Summary: This test verifies that an `AnyOf` watch triggers callbacks when either of its constituent event types is received from a stream. It confirms the watcher correctly captures events sequentially as they are sent to the underlying memory stream.*


### TestSequence (class, L496-L547)

> *Summary: This test suite verifies the sequential firing behavior of an event watcher chain, ensuring events are processed only in the specified order. It uses a `MemoryStream` to feed events and asserts that callbacks fire correctly upon successful sequence completion or fail when events arrive out of order.*


### test_fires_in_order (method, L498-L522, parent: TestSequence)

> *Summary: This test verifies that an `EventWatch` sequence fires events strictly in the defined order, only when inputs arrive sequentially as expected. It confirms that sending events out of sequence (e.g., message before tool call) results in no firing, while correct sequencing triggers the callback upon completion.*


### test_resets_after_completion (method, L525-L547, parent: TestSequence)

> *Summary: This test verifies that an event watcher correctly captures events across multiple, sequential completions of a streaming context. It sends pairs of `ToolCallEvent` and `ModelMessage` events to the stream and asserts that the callback receives one distinct list for each completed sequence.*


### TestCronWatchExpressions (class, L550-L624)

> *Summary: These tests verify the `CronWatch` class's ability to accurately calculate the next execution time based on various cron expression syntaxes. They confirm correct behavior for ranges, lists, steps, specific values, and handling of invalid or malformed expressions by asserting expected output times or raised exceptions.*


### test_range_expression (method, L551-L555, parent: TestCronWatchExpressions)

> *Summary: This test verifies that a `CronWatch` initialized with the range expression "1-5 * * * *" correctly calculates the next firing time. It asserts that the minute component of this calculated time falls within the specified range (1 through 5).*


### test_list_expression (method, L557-L561, parent: TestCronWatchExpressions)

> *Summary: This test verifies that a `CronWatch` instance correctly calculates the next scheduled execution time based on a given current time. It asserts that the minute component of the returned next fire time matches one of the specified intervals (0, 15, 30, or 45).*


### test_step_with_range (method, L563-L567, parent: TestCronWatchExpressions)

> *Summary: This test verifies that a `CronWatch` instance configured for every 10 minutes correctly calculates the next firing time based on a given input datetime. It asserts that the minute component of the returned next fire time is one of the expected multiples of ten.*


### test_specific_hour_and_minute (method, L569-L574, parent: TestCronWatchExpressions)

> *Summary: This test verifies that a `CronWatch` instance correctly calculates the next scheduled execution time for a specific cron pattern ("30 14 * * *"). Given an input time, it asserts the resulting next fire time has the expected hour (14) and minute (30).*


### test_invalid_field_count_raises (method, L576-L579, parent: TestCronWatchExpressions)

> *Summary: This test verifies that attempting to calculate the next fire time for a cron schedule initialized with an incorrect number of fields raises a `ValueError`. It specifically asserts that the error message indicates "5 fields" were expected or encountered.*


### test_step_five_minutes (method, L581-L586, parent: TestCronWatchExpressions)

> *Summary: This test verifies the `CronWatch`'s ability to calculate the next execution time for a five-minute interval schedule. Given a specific datetime, it asserts that the returned next fire time correctly falls on the 5th minute of the specified hour.*


### test_day_of_week_name (method, L588-L595, parent: TestCronWatchExpressions)

> *Summary: This test verifies that a `CronWatch` instance configured for Monday at 9 AM correctly calculates the next firing time from a given input datetime. It asserts that the resulting time falls on the correct day (Monday) and matches the specified hour and minute.*


### test_invalid_expression_raises (method, L597-L600, parent: TestCronWatchExpressions)

> *Summary: This test verifies that attempting to calculate the next firing time for a `CronWatch` initialized with an invalid expression raises a `ValueError`. It asserts that the error message specifically contains "Invalid cron".*


### test_numeric_dow_sunday_zero (method, L602-L609, parent: TestCronWatchExpressions)

> *Summary: This test verifies that a `CronWatch` configured for Sunday at 9 AM correctly calculates the next firing time, given an input time on a Saturday. It asserts the resulting datetime object falls on the subsequent Sunday at the specified hour.*


### test_numeric_dow_saturday_six (method, L611-L618, parent: TestCronWatchExpressions)

> *Summary: This test verifies that a `CronWatch` configured for Saturday at 9 AM correctly calculates the next firing time when the current time is past the scheduled hour on the target day. It asserts the resulting datetime object falls on the subsequent Saturday and maintains the correct hour.*


### test_numeric_dow_seven_is_sunday_alias (method, L620-L624, parent: TestCronWatchExpressions)

> *Summary: This test verifies that the cron expression for day of week 7 (Sunday) resolves to the same next firing time as the expression for day of week 0 (Sunday). It achieves this by comparing the results of `_next_fire_time` methods on two initialized `CronWatch` objects using a specific datetime input.*

