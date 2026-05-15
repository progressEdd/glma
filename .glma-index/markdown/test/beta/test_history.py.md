# test/beta/test_history.py

3 function(s): test_repeated_user_message_is_persisted_each_time, test_repeated_assistant_response_is_persisted_each_time, test_history_preserves_user_assistant_alternation.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_repeated_user_message_is_persisted_each_time | function |  |
| test_repeated_assistant_response_is_persisted_each_time | function |  |
| test_history_preserves_user_assistant_alternation | function |  |

## Chunks

### test_repeated_user_message_is_persisted_each_time (function, L13-L35)

> *Summary: This test verifies that repeated user inputs are correctly persisted in the conversation history, ensuring subsequent turns are recorded even if they have identical content to previous ones. It confirms that a sequence of three interactions—two repetitions and one variation—results in all three distinct user messages being present in the final event stream.*


### test_repeated_assistant_response_is_persisted_each_time (function, L39-L55)

> *Summary: This test verifies that identical responses from the LLM are correctly persisted across multiple turns within a conversation history. It asserts that when an agent receives two consecutive identical answers, both instances are recorded in the event stream.*


### test_history_preserves_user_assistant_alternation (function, L59-L72)

> *Summary: This test verifies that the agent's conversation history correctly alternates between user and assistant turns. It sends three sequential prompts to an agent instance and asserts that the recorded events strictly follow a `ModelRequest`, `ModelResponse` pattern for each interaction.*

