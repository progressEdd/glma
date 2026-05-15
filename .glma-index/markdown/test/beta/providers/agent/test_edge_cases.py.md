# test/beta/providers/agent/test_edge_cases.py

9 function(s): test_long_conversation_with_compaction, test_unicode_and_emoji_pass_through, test_concurrent_tool_calls_via_run_subtasks, test_retry_middleware_happy_path, test_history_limiter_caps_context, test_response_schema_strict_validation, test_large_response, test_empty_string_user_message, test_concurrent_independent_asks.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_long_conversation_with_compaction | function |  |
| test_unicode_and_emoji_pass_through | function |  |
| test_concurrent_tool_calls_via_run_subtasks | function |  |
| test_retry_middleware_happy_path | function |  |
| test_history_limiter_caps_context | function |  |
| test_response_schema_strict_validation | function |  |
| test_large_response | function |  |
| test_empty_string_user_message | function |  |
| test_concurrent_independent_asks | function |  |

## Chunks

### test_long_conversation_with_compaction (function, L26-L63)

> *Summary: This test verifies that an agent successfully handles a long, multi-turn conversation while triggering knowledge base compaction. It feeds a series of questions to the agent and asserts that at least one compaction event occurs during the interaction without causing the chat to fail.*


### test_unicode_and_emoji_pass_through (function, L66-L83)

> *Summary: This test verifies that Unicode characters and emojis are correctly preserved when passed through an agent configured with a simple echo tool. It asserts that specific non-ASCII strings survive the round trip within the agent's response body.*


### test_concurrent_tool_calls_via_run_subtasks (function, L86-L126)

> *Summary: This test verifies that when an agent uses `run_subtasks` with `parallel=True`, multiple independent tasks are initiated concurrently within the same event loop tick. It asserts this concurrency by checking that the time difference between the start events of the three dispatched subtasks is very small (less than 0.5 seconds).*


### test_retry_middleware_happy_path (function, L129-L138)

> *Summary: This test verifies that the `RetryMiddleware` does not interfere with successful LLM interactions. It initializes an Agent configured with retry logic and asserts that a simple query returns a valid response containing the expected text.*


### test_history_limiter_caps_context (function, L141-L179)

> *Summary: This test verifies that a `HistoryLimiter` correctly caps the number of events sent to an LLM by wrapping the agent with a capture middleware. It executes a sequence of interactions and asserts that the final event list received by the LLM call is no more than three events long, confirming the trimming logic works as expected.*


### test_response_schema_strict_validation (function, L182-L206)

> *Summary: This test verifies that an agent strictly adheres to a predefined Pydantic schema when generating a response. It sends a prompt expecting a numeric answer and asserts that the resulting content is correctly typed as the expected model instance containing the calculated integer value.*


### test_large_response (function, L209-L218)

> *Summary: This test verifies that the agent correctly processes and returns a significantly large response without truncating it. It initializes an agent with a verbose prompt, asks for a multi-paragraph answer on photosynthesis, and asserts the resulting body content exceeds a threshold of 500 characters.*


### test_empty_string_user_message (function, L221-L230)

> *Summary: When an empty or near-empty string is passed as the user input to the agent, this test verifies that the resulting response body is non-null and contains actual content. It confirms the agent adheres to its prompt instructions even with minimal input.*


### test_concurrent_independent_asks (function, L233-L247)

> *Summary: This test verifies that concurrent, independent requests made to an agent do not interfere with each other. It concurrently calls `agent.ask()` twice with different prompts and asserts that both responses correctly contain their respective expected words.*

