# test/beta/middleware/builtins/test_token_limiter.py

6 function(s): test_token_limiter_passes_events_through_when_within_budget, test_token_limiter_keeps_first_request_while_trimming, test_token_limiter_trims_from_front_without_initial_request, test_token_limiter_drops_tool_results_without_parent_message, test_token_limiter_drops_tool_results_without_parent_message_and_no_initial_request, test_token_limiter_rejects_invalid_limits.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_token_limiter_passes_events_through_when_within_budget | function |  |
| test_token_limiter_keeps_first_request_while_trimming | function |  |
| test_token_limiter_trims_from_front_without_initial_request | function |  |
| test_token_limiter_drops_tool_results_without_parent_message | function |  |
| test_token_limiter_drops_tool_results_without_parent_message_and_no_initial_request | function |  |
| test_token_limiter_rejects_invalid_limits | function |  |

## Chunks

### test_token_limiter_passes_events_through_when_within_budget (function, L25-L38)

> *Summary: This test verifies that the token limiter allows events to pass through when the budget is sufficient. It initializes a `TokenLimiter` and then calls its `on_llm_call` method, asserting that the underlying LLM call function receives all provided events.*


### test_token_limiter_keeps_first_request_while_trimming (function, L42-L60)

> *Summary: This test verifies that a token limiter retains the initial request while trimming subsequent responses to meet a maximum token limit. It asserts that the underlying LLM call is made only with the first input and the last retained response from the provided event sequence.*


### test_token_limiter_trims_from_front_without_initial_request (function, L64-L78)

> *Summary: This test verifies that the token limiter correctly trims tokens from the front of a message history when no initial request is present. It asserts that only the last, non-dropped message remains in the history passed to the mocked LLM call.*


### test_token_limiter_drops_tool_results_without_parent_message (function, L82-L104)

> *Summary: This test verifies that a token limiter correctly omits tool results when they lack an associated parent message in the event history. It simulates a sequence of model requests, tool calls, and responses to assert which events are passed to the underlying LLM call.*


### test_token_limiter_drops_tool_results_without_parent_message_and_no_initial_request (function, L108-L126)

> *Summary: This test verifies that the token limiter discards tool results when they lack a preceding parent message and no initial request is present. It asserts that the underlying LLM call only receives the final model response, effectively ignoring the intermediate tool result event.*


### test_token_limiter_rejects_invalid_limits (function, L129-L134)

> *Summary: This test verifies that the `TokenLimiter` constructor raises a `ValueError` when provided with non-positive values for its token or character limits. It specifically asserts failure for setting `max_tokens` to zero and for setting `chars_per_token` to zero.*

