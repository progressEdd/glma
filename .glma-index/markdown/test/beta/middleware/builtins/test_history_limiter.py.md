# test/beta/middleware/builtins/test_history_limiter.py

5 function(s): test_history_limiter, test_history_limiter_saves_first_turn, test_no_history_limiter, test_history_limiter_drops_overlapping_turns, test_history_limiter_drops_incomplete_tool_interaction.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_history_limiter | function |  |
| test_history_limiter_saves_first_turn | function |  |
| test_no_history_limiter | function |  |
| test_history_limiter_drops_overlapping_turns | function |  |
| test_history_limiter_drops_incomplete_tool_interaction | function |  |

## Chunks

### test_history_limiter (function, L25-L36)

> *Summary: This test verifies that a `HistoryLimiter` correctly restricts the number of events passed to an LLM call. It initializes the limiter with a maximum of three events and asserts that the underlying mock function is called exactly once with the initial request.*


### test_history_limiter_saves_first_turn (function, L40-L62)

> *Summary: This test verifies that the history limiter correctly retains the first turn when the maximum event count is set to three. It asserts that the underlying LLM call receives a sequence containing the initial request, the second response, and the final third request, effectively dropping the intermediate second turn's input.*


### test_no_history_limiter (function, L66-L84)

> *Summary: This test verifies that when a history limiter is configured with `max_events=1`, the middleware only passes the very first request to the underlying LLM call. It asserts that `llm_call` was invoked exactly once, receiving only the initial input event.*


### test_history_limiter_drops_overlapping_turns (function, L88-L111)

> *Summary: This test verifies that the history limiter correctly drops overlapping turns when processing a sequence of events. It asserts that the underlying LLM call is only made with a truncated set of events, specifically retaining only the last non-overlapping interactions.*


### test_history_limiter_drops_incomplete_tool_interaction (function, L115-L138)

> *Summary: This test verifies that the history limiter correctly discards incomplete tool interaction sequences when the maximum event count is reached. It asserts that only complete, valid interactions are passed to the underlying LLM call function.*

