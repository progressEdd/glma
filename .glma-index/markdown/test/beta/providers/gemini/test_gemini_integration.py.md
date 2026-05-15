# test/beta/providers/gemini/test_gemini_integration.py

10 function(s): gemini_config, test_system_prompt, test_tool_use, test_structured_output_primitive, test_structured_output_dataclass, test_multi_turn, test_multi_turn_after_empty_args_tool_call, test_thinking_level_low_reports_thinking_tokens, test_thinking_budget_reports_thinking_tokens, test_history_round_trip_preserves_thought_signature.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| gemini_config | function |  |
| test_system_prompt | function |  |
| test_tool_use | function |  |
| test_structured_output_primitive | function |  |
| test_structured_output_dataclass | function |  |
| test_multi_turn | function |  |
| test_multi_turn_after_empty_args_tool_call | function |  |
| test_thinking_level_low_reports_thinking_tokens | function |  |
| test_thinking_budget_reports_thinking_tokens | function |  |
| test_history_round_trip_preserves_thought_signature | function |  |

## Chunks

### gemini_config (function, L17-L21)

> *Summary: Retrieves the necessary configuration for Gemini integration by reading the `GEMINI_API_KEY` environment variable. If the key is missing, it skips testing; otherwise, it returns a configured object specifying the model and API key.*


### test_system_prompt (function, L26-L37)

> *Summary: This test verifies that an agent configured with a strict system prompt correctly enforces language constraints. It sends a query to the agent and asserts that the resulting response body contains French keywords, confirming adherence to the instruction to always reply in French.*


### test_tool_use (function, L42-L57)

> *Summary: This test verifies an AI agent's ability to utilize a provided tool by sending it a query about the weather in Paris. It asserts that the resulting response body contains expected weather details, confirming successful tool invocation and integration.*


### test_structured_output_primitive (function, L62-L73)

> *Summary: This test verifies that an agent configured with a Gemini model correctly returns a primitive integer output when prompted with a math question. It initializes the agent to expect an `int` and asserts the final retrieved content matches the expected calculation result (105).*


### test_structured_output_dataclass (function, L78-L97)

> *Summary: This test verifies that an agent configured with a specific Gemini setup can correctly parse structured data from the model's response. It inputs a natural language query and asserts that the resulting object conforms to the defined `City` dataclass structure.*


### test_multi_turn (function, L102-L114)

> *Summary: This test verifies multi-turn conversational capability by initializing an agent with Gemini configuration and then sequentially querying it twice. It asserts that the second response correctly recalls information provided in the first turn, specifically confirming the name "Alice."*


### test_multi_turn_after_empty_args_tool_call (function, L119-L137)

> *Summary: This test verifies that a multi-turn conversation remains stable after an initial tool call with no arguments. It initializes an agent equipped with a `discover_agents` tool and then sequentially queries it, asserting successful responses for both the initial and follow-up prompts.*


### test_thinking_level_low_reports_thinking_tokens (function, L142-L157)

> *Summary: This test verifies that when an agent is configured with a low thinking level, the Gemini SDK correctly reports non-zero `thinking_tokens` in the response's usage statistics after processing a simple query. It asserts that the returned reply contains usage data indicating token consumption for thought processes.*


### test_thinking_budget_reports_thinking_tokens (function, L162-L176)

> *Summary: This test verifies that when using a specific Gemini model configured with a `thinking_budget`, the resulting response object contains non-zero `thinking_tokens` in its usage statistics after an agent query. It initializes an agent with a constrained thinking budget and asserts the presence of these tokens in the reply's usage data.*


### test_history_round_trip_preserves_thought_signature (function, L181-L208)

> *Summary: This test verifies that the thought signature of tool calls remains intact after a serialization/deserialization round trip within an agent's conversation history. It initializes an agent with a weather tool, queries it twice, and then checks the integrity of `thought_signature` bytes across the history events before making a second query.*

