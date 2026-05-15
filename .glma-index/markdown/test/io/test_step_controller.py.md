# test/io/test_step_controller.py

4 class(es): TestStepController, TestAsyncStepController, TestRunIterResponse, TestAsyncRunIterResponse. 28 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestStepController | class |  |
| TestAsyncStepController | class |  |
| TestRunIterResponse | class |  |
| TestAsyncRunIterResponse | class |  |

## Chunks

### TestStepController (class, L22-L127)

> *Summary: This test suite verifies the behavior of a controller responsible for managing event flow control within a step process. It asserts that blocking logic correctly filters events based on configured types, handles termination states, and manages thread synchronization when waiting for specific steps or upon receiving a terminate signal.*


### test_should_block_no_filter_blocks_all_events (method, L25-L34, parent: TestStepController)

> *Summary: When initialized with `yield_on` set to `None`, the controller's `should_block` method returns `True` for any input event, regardless of its specific type (e.g., text or termination). This test verifies that no filtering occurs when `yield_on` is unset.*


### test_should_block_with_filter_only_blocks_specified_types (method, L36-L52, parent: TestStepController)

> *Summary: This test verifies that the `StepController` correctly blocks only event types explicitly listed in its `yield_on` configuration. It asserts that events matching specified types return `True` for blocking, while unlisted event mocks return `False`.*


### test_should_block_after_terminate_returns_false (method, L54-L64, parent: TestStepController)

> *Summary: This test verifies that once a `StepController` has been terminated, its `should_block` method consistently returns `False`, regardless of the input event. It confirms the state change after calling the `terminate()` method on an initialized controller instance.*


### test_step_unblocks_wait_for_step (method, L66-L88, parent: TestStepController)

> *Summary: This test verifies that calling `step()` on a controller unblocks a thread blocked by `wait_for_step()`. It spawns a thread that waits for a step event and asserts the thread completes only after `controller.step()` is called.*


### test_wait_for_step_skips_non_matching_events (method, L90-L103, parent: TestStepController)

> *Summary: This test verifies that the `StepController` immediately returns when presented with an event type not included in its configured `yield_on` list. It asserts that calling `wait_for_step` with a non-matching `TextEvent` takes negligible time.*


### test_terminate_unblocks_waiting_producer (method, L105-L127, parent: TestStepController)

> *Summary: This test verifies that calling `terminate()` on a controller releases any thread blocked by `wait_for_step()`. It starts a producer thread waiting on the controller and asserts that termination successfully unblocks this thread, allowing it to complete its execution.*


### TestAsyncStepController (class, L130-L221)

> *Summary: These tests verify the behavior of an asynchronous controller responsible for managing event flow based on specified filters. It confirms that blocking logic correctly handles `None` or specific event types, and ensures methods like `step()` and `terminate()` properly unblock waiting asynchronous tasks.*


### test_should_block_no_filter_blocks_all_events (method, L133-L141, parent: TestAsyncStepController)

> *Summary: When initialized with `yield_on` set to `None`, the controller's `should_block` method returns `True` for any input event, including both text and termination events. This test verifies that no filtering occurs when the yield mechanism is disabled.*


### test_should_block_with_filter_only_blocks_specified_types (method, L143-L152, parent: TestAsyncStepController)

> *Summary: This test verifies that an `AsyncStepController` configured with a specific type filter (`yield_on`) correctly returns `True` only when the input event matches one of the specified types, and `False` otherwise. It asserts blocking behavior for a mocked `TextEvent` while ensuring other arbitrary events are not blocked.*


### test_should_block_after_terminate_returns_false (method, L154-L161, parent: TestAsyncStepController)

> *Summary: Verifies that after calling `terminate()` on an `AsyncStepController`, the `should_block` method consistently returns `False`, regardless of any input event. This confirms the controller stops blocking operations post-termination.*


### test_step_unblocks_wait_for_step (method, L164-L186, parent: TestAsyncStepController)

> *Summary: This test verifies that calling `step()` on an `AsyncStepController` unblocks a task waiting via `wait_for_step()`. It sets up a producer coroutine that blocks until the controller signals completion, asserting that the block is released and the task finishes successfully.*


### test_wait_for_step_skips_non_matching_events (method, L189-L200, parent: TestAsyncStepController)

> *Summary: This test verifies that the `wait_for_step` method returns instantly when provided with an event type not configured for yielding (like a `TextEvent`). It asserts that the execution time is very short, confirming it skips non-matching events immediately.*


### test_terminate_unblocks_waiting_producer (method, L203-L221, parent: TestAsyncStepController)

> *Summary: This test verifies that calling `terminate()` on an `AsyncStepController` unblocks any producer task currently suspended by `wait_for_step()`. It achieves this by starting a waiting producer and asserting that the producer completes after termination is called.*


### TestRunIterResponse (class, L224-L450)

> *Summary: This code defines a test class for verifying the behavior of an iterator-based response object that simulates event streaming from a run. It provides helper methods to construct this response using predefined events and includes numerous tests covering yielding, error handling, termination conditions (break/exception), lazy startup, filtering, and property population upon completion.*


### _create_run_iter_response (method, L227-L263, parent: TestRunIterResponse)

> *Summary: Constructs a `RunIterResponse` object designed to stream provided events into an input stream via a background thread. It accepts a list of events and an optional filter for event types (`yield_on`).*


### test_iteration_yields_events_until_completion (method, L265-L285, parent: TestRunIterResponse)

> *Summary: This test verifies that an iteration response yields a sequence of events until a completion signal is received. It mocks a `TextEvent` and a `RunCompletionEvent`, then asserts the resulting list contains exactly one event, which must be the initial text event.*


### test_iteration_raises_on_error_event (method, L287-L298, parent: TestRunIterResponse)

> *Summary: This test verifies that iterating over a response containing an `ErrorEvent` correctly propagates the underlying exception. It mocks an event with a specific `ValueError` and asserts that attempting to iterate over the resulting response raises that exact error.*


### test_break_terminates_step_controller (method, L300-L322, parent: TestRunIterResponse)

> *Summary: This test verifies that an early `break` from iterating over a generated response causes the internal step controller to terminate. It passes a list of mock events, including one completion event, and asserts the controller's termination status after the loop exits prematurely.*


### test_exception_terminates_step_controller (method, L324-L345, parent: TestRunIterResponse)

> *Summary: This test verifies that an injected `ValueError` during iteration causes the step controller to terminate immediately. It asserts that the internal state of the response object confirms the controller has been stopped after the exception is raised.*


### test_lazy_start (method, L347-L369, parent: TestRunIterResponse)

> *Summary: This test verifies that a background thread only initiates when the iterator is first consumed. It asserts that the internal state remains unstarted and thread-less before iteration, but becomes started with an active thread after the first call to `list()`.*


### test_yield_on_filters_events (method, L371-L397, parent: TestRunIterResponse)

> *Summary: This test verifies that an iterator response yields only those events specified in the `yield_on` filter. It takes a list of mixed event types as input and asserts that the resulting iteration contains exactly one element, which must be the designated `TerminationEvent`.*


### test_input_request_always_yielded (method, L399-L425, parent: TestRunIterResponse)

> *Summary: This test verifies that an `InputRequestEvent` is always yielded by the run iterator, even when filtering is configured to only yield specific events like `TerminationEvent`. It asserts that the resulting iterable contains exactly one event, which must be the mocked input request.*


### test_properties_populated_after_completion (method, L427-L450, parent: TestRunIterResponse)

> *Summary: This test verifies that an iterator's properties are correctly populated after full consumption. It simulates a run completion event containing specific data and asserts that the resulting response object reflects this data (e.g., summary, message count) post-iteration.*


### TestAsyncRunIterResponse (class, L453-L643)

> *Summary: This test suite verifies the behavior of an asynchronous iterator response mechanism, which uses internal threads to process and yield events from a queue. It tests scenarios including successful event yielding until completion, error propagation during iteration, proper thread termination upon breaking or exception, lazy thread startup, and filtering yielded events based on specified types.*


### _create_async_run_iter_response (method, L460-L496, parent: TestAsyncRunIterResponse)

> *Summary: Constructs an `AsyncRunIterResponse` designed to stream a provided list of events. It initializes a background thread that pumps these events into a specified input stream while pausing execution until the step controller signals continuation for each event.*


### test_iteration_yields_events_until_completion (method, L499-L519, parent: TestAsyncRunIterResponse)

> *Summary: This test verifies that an asynchronous run iterator yields a sequence of events, specifically asserting it produces exactly one `TextEvent` before the iteration concludes. It achieves this by mocking both a `TextEvent` and a final `RunCompletionEvent` to control the stream's output.*


### test_iteration_raises_on_error_event (method, L522-L533, parent: TestAsyncRunIterResponse)

> *Summary: This test verifies that iterating over a response containing an `ErrorEvent` correctly raises the underlying exception specified within that event's content. It simulates an error scenario by providing a mocked `ErrorEvent` with a `ValueError` and asserts that attempting to iterate through the resulting asynchronous sequence triggers this specific error.*


### test_break_terminates_step_controller (method, L536-L560, parent: TestAsyncRunIterResponse)

> *Summary: This test verifies that explicitly closing an asynchronous iterator terminates the associated step controller. It feeds a sequence of mock events into a run response and asserts that the controller's termination flag is set after calling `aclose()` on the iterator.*


### test_exception_terminates_step_controller (method, L563-L589, parent: TestAsyncRunIterResponse)

> *Summary: This test verifies that an unexpected `ValueError` raised during iteration causes the step controller to terminate gracefully. It achieves this by manually iterating over a mocked asynchronous response and asserting that the internal controller state reflects termination after explicitly closing the iterator.*


### test_lazy_start (method, L592-L614, parent: TestAsyncRunIterResponse)

> *Summary: This test verifies that an asynchronous run process only initiates its background thread upon the first iteration of the returned iterator. It asserts that the internal state reflects no thread activity before consumption and confirms thread activation after at least one loop execution.*


### test_yield_on_filters_events (method, L617-L643, parent: TestAsyncRunIterResponse)

> *Summary: This test verifies that an asynchronous iterator only yields events matching a specified filter. It takes a list of mixed events and a `yield_on` list, asserting that the resulting sequence contains exactly one event: the `TerminationEvent`.*

