# test/beta/providers/openai/test_openai_integration.py

7 function(s): openai_config, test_system_prompt, test_tool_use, test_structured_output_primitive, test_structured_output_dataclass, test_multi_turn, test_multi_turn_after_empty_args_tool_call.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| openai_config | function |  |
| test_system_prompt | function |  |
| test_tool_use | function |  |
| test_structured_output_primitive | function |  |
| test_structured_output_dataclass | function |  |
| test_multi_turn | function |  |
| test_multi_turn_after_empty_args_tool_call | function |  |

## Chunks

### openai_config (function, L15-L19)

> *Summary: Retrieves the `OPENAI_API_KEY` from environment variables; if missing, it skips testing. Otherwise, it constructs and returns an `OpenAIConfig` object using a specific model name and zero temperature.*


### test_system_prompt (function, L24-L36)

> *Summary: This test verifies an agent's adherence to a system prompt by instructing it to respond only in French. It sends a query and asserts that the resulting response body contains several common French words.*


### test_tool_use (function, L41-L56)

> *Summary: This test verifies an AI agent's ability to utilize a provided tool by sending it a query ("What's the weather in Paris?"). It asserts that the resulting response body contains expected information from the `get_weather` function, confirming successful tool invocation and result integration.*


### test_structured_output_primitive (function, L61-L72)

> *Summary: This test verifies that an agent configured with a specific response schema (an integer) correctly processes a math query and returns the expected numeric output. It takes an `OpenAIConfig` as input, executes a question via the agent, and asserts the resulting content matches the predefined integer answer.*


### test_structured_output_dataclass (function, L77-L96)

> *Summary: This test verifies that an agent correctly parses structured JSON output from OpenAI based on a provided dataclass schema. It sends a geographical query to the agent and asserts that the returned content is an instance of the expected `City` dataclass with correct field values.*


### test_multi_turn (function, L101-L113)

> *Summary: This test verifies multi-turn conversational capability by initializing an agent with OpenAI configuration and then sequentially querying it, asserting that the second response correctly recalls information from the first turn. It confirms the agent maintains context across multiple interactions.*


### test_multi_turn_after_empty_args_tool_call (function, L118-L136)

> *Summary: This test verifies that a multi-turn conversation remains stable after an initial tool call with no arguments. It initializes an agent equipped with a `discover_agents` tool and then sequentially queries it, asserting successful responses for both the initial and follow-up prompts.*

