# test/beta/a2a/test_terminal_states.py

1 function(s): _bootstrap_task. 4 class(es): _FailedExecutor, _RejectedExecutor, _AuthRequiredExecutor, TestTerminalStates. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _bootstrap_task | function |  |
| _FailedExecutor | class |  |
| _RejectedExecutor | class |  |
| _AuthRequiredExecutor | class |  |
| TestTerminalStates | class |  |

## Chunks

### _bootstrap_task (function, L23-L28)

> *Summary: This function initializes a new task by extracting or generating unique identifiers for the task and its associated context from an incoming request message. It returns these two IDs along with a `TaskUpdater` instance configured to manage updates via the provided event queue.*


### _FailedExecutor (class, L31-L41)

> *Summary: This executor handles failed execution scenarios by bootstrapping a task and immediately marking it as submitted before calling the updater's failure method. It accepts a `RequestContext` and an `EventQueue` to manage the lifecycle of this failed operation.*


### execute (method, L32-L38, parent: _FailedExecutor)

> *Summary: This method initiates a background task by bootstrapping it from the provided request context and event queue. It then enqueues the task in a "submitted" state and immediately triggers the associated updater to begin and subsequently fail its work.*


### cancel (method, L40-L41, parent: _FailedExecutor)

> *Summary: This method accepts a `RequestContext` and an `EventQueue` to immediately stop any ongoing process. It currently performs no action and returns nothing.*


### _RejectedExecutor (class, L44-L54)

> *Summary: This executor handles rejected tasks by first bootstrapping a task and submitting it to the event queue as "SUBMITTED." It then immediately initiates work on the updater object before calling its `reject()` method.*


### execute (method, L45-L51, parent: _RejectedExecutor)

> *Summary: This method initiates a background task by bootstrapping it from the provided request context and event queue. It then enqueues the task in a "submitted" state and immediately starts and rejects the associated updater.*


### cancel (method, L53-L54, parent: _RejectedExecutor)

> *Summary: This method immediately stops any ongoing process by returning `None`. It accepts a `RequestContext` and an `EventQueue` as inputs but produces no output.*


### _AuthRequiredExecutor (class, L57-L67)

> *Summary: This executor initiates a background task by bootstrapping it from the provided context and queue, then signals its submission status before requesting authentication via an updater. It provides no cancellation mechanism.*


### execute (method, L58-L64, parent: _AuthRequiredExecutor)

> *Summary: This method initiates a background task by bootstrapping it using the provided request and event queue. It then enqueues the task in a "submitted" state and starts the associated updater, followed by an authentication check.*


### cancel (method, L66-L67, parent: _AuthRequiredExecutor)

> *Summary: This method immediately stops any ongoing process by returning `None`. It accepts a `RequestContext` and an `EventQueue` as inputs but produces no output.*


### TestTerminalStates (class, L71-L100)

> *Summary: This test suite verifies that the client correctly raises specific exceptions when interacting with executors in terminal states (failed, rejected, or authentication required). It tests both streaming and polling modes by using mock executor pairs to simulate these error conditions during an `ask` operation.*


### test_failed_task_raises_failed_error_streaming (method, L72-L75, parent: TestTerminalStates)

> *Summary: This test verifies that when an executor fails, the client correctly raises an `A2ATaskFailedError` during a streaming request initiated by calling `"ping"`. It achieves this by setting up a pair using a deliberately failing executor.*


### test_failed_task_raises_failed_error_polling (method, L77-L80, parent: TestTerminalStates)

> *Summary: This test verifies that polling for a task raises an `A2ATaskFailedError` when the underlying executor is configured to fail. It achieves this by creating an executor pair with a failing executor and then calling the client's `ask` method.*


### test_rejected_task_raises_rejected_error_streaming (method, L82-L85, parent: TestTerminalStates)

> *Summary: This test verifies that attempting to send a request ("ping") to an executor configured for rejection will correctly raise an `A2ATaskRejectedError`. It uses a mock rejected executor instance to simulate the failure condition during streaming communication.*


### test_rejected_task_raises_rejected_error_polling (method, L87-L90, parent: TestTerminalStates)

> *Summary: This test verifies that attempting to poll a task with a rejected executor raises an `A2ATaskRejectedError`. It achieves this by setting up an executor pair using the `_RejectedExecutor` and calling the client's `ask` method.*


### test_auth_required_raises_auth_error_streaming (method, L92-L95, parent: TestTerminalStates)

> *Summary: This test verifies that attempting to call the `ask` method with an unauthenticated executor raises an `A2ATaskAuthRequiredError`. It achieves this by setting up a streaming execution pair using an `_AuthRequiredExecutor`.*


### test_auth_required_raises_auth_error_polling (method, L97-L100, parent: TestTerminalStates)

> *Summary: This test verifies that attempting to call the `ask` method on a client configured with an `_AuthRequiredExecutor` raises an `A2ATaskAuthRequiredError`. It achieves this by creating an executor pair and asserting the expected exception during the asynchronous ping request.*

