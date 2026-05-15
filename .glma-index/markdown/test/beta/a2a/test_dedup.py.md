# test/beta/a2a/test_dedup.py

2 function(s): test_text_accumulates_across_input_required_polling, test_text_accumulates_across_input_required_streaming. 1 class(es): _MultiTurnTextExecutor. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _MultiTurnTextExecutor | class |  |
| test_text_accumulates_across_input_required_polling | function |  |
| test_text_accumulates_across_input_required_streaming | function |  |

## Chunks

### _MultiTurnTextExecutor (class, L17-L38)

> *Summary: This executor processes incoming messages by either initiating a new task with a submitted state and requesting continuation input, or completing an existing task based on the provided user reply. It manages task lifecycle updates using a `TaskUpdater` instance tied to the event queue.*


### execute (method, L18-L35, parent: _MultiTurnTextExecutor)

> *Summary: This method processes an incoming message from a request context, generating unique IDs if they are missing. It either submits a new task and initiates work with initial artifacts or completes the current task by incorporating the user's reply into a final agent message.*


### cancel (method, L37-L38, parent: _MultiTurnTextExecutor)

> *Summary: This asynchronous method accepts a `RequestContext` and an `EventQueue`, performing no operations and returning nothing. It serves as a placeholder or hook for cancellation logic within the class instance.*


### test_text_accumulates_across_input_required_polling (function, L42-L50)

> *Summary: This test verifies that text accumulates across multiple interactions when using a multi-turn executor with a human-in-the-loop hook. It sends an initial prompt and asserts the resulting response contains concatenated content from the interaction flow.*


### test_text_accumulates_across_input_required_streaming (function, L54-L62)

> *Summary: This test verifies that text accumulates correctly across multiple inputs when using a streaming executor configured with a human-in-the-loop hook. It sends an initial prompt and asserts the resulting response contains concatenated content, including the expected feedback from the `hitl` function.*

