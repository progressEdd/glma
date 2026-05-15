# test/beta/providers/anthropic/test_anthropic_integration.py

7 function(s): anthropic_config, test_system_prompt, test_tool_use, test_structured_output_primitive, test_structured_output_dataclass, test_multi_turn, test_multi_turn_after_empty_args_tool_call.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| anthropic_config | function |  |
| test_system_prompt | function |  |
| test_tool_use | function |  |
| test_structured_output_primitive | function |  |
| test_structured_output_dataclass | function |  |
| test_multi_turn | function |  |
| test_multi_turn_after_empty_args_tool_call | function |  |

## Chunks

### anthropic_config (function, L15-L19)

> *Summary: Retrieves the API key from environment variables and returns a configured `AnthropicConfig` object. It skips execution if the required `ANTHROPIC_API_KEY` is not present in the environment.*


### test_system_prompt (function, L24-L35)

> *Summary: This test verifies that an agent configured with Anthropic settings adheres to a system prompt requiring French responses. It sends a query and asserts the resulting reply contains specific French keywords.*


### test_tool_use (function, L40-L55)

> *Summary: This test verifies an AI agent's ability to utilize a provided tool by sending it a query about the weather in Paris. It asserts that the resulting response body from the agent contains expected weather details, confirming successful tool invocation and integration.*


### test_structured_output_primitive (function, L60-L71)

> *Summary: This test verifies that an agent configured with Anthropic can correctly parse and return a primitive integer output from the model based on a specific prompt. It sends a math question to the agent and asserts the resulting content matches the expected numeric answer (105).*


### test_structured_output_dataclass (function, L76-L95)

> *Summary: This test verifies that an agent configured with Anthropic can correctly parse structured JSON output into a Python dataclass. It prompts the agent about Paris and asserts that the returned object matches the expected `City` structure with correct values for name and country.*


### test_multi_turn (function, L100-L112)

> *Summary: This test verifies multi-turn conversation capability by initializing an agent with Anthropic configuration and sequentially querying it twice. It asserts that the second response correctly recalls information provided in the first turn.*


### test_multi_turn_after_empty_args_tool_call (function, L117-L136)

> *Summary: This test verifies that a multi-turn conversation remains stable after an initial interaction involving a tool call with no arguments. It initializes an agent with a `discover_agents` tool and then checks for successful responses across two consecutive turns, ensuring the system doesn't crash during follow-up queries.*

