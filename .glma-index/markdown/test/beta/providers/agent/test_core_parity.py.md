# test/beta/providers/agent/test_core_parity.py

16 function(s): test_basic_ask, test_static_system_prompt, test_dynamic_prompt_with_context, test_sync_tool_use, test_async_tool_use, test_multi_tool_dispatch, test_tool_error_propagates, test_structured_output_primitive, test_structured_output_dataclass, test_structured_output_pydantic and 6 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_basic_ask | function |  |
| test_static_system_prompt | function |  |
| test_dynamic_prompt_with_context | function |  |
| test_sync_tool_use | function |  |
| test_async_tool_use | function |  |
| test_multi_tool_dispatch | function |  |
| test_tool_error_propagates | function |  |
| test_structured_output_primitive | function |  |
| test_structured_output_dataclass | function |  |
| test_structured_output_pydantic | function |  |
| test_multi_turn_ask_chain | function |  |
| test_streaming_chunks_arrive | function |  |
| test_dependency_injection_into_tool | function |  |
| test_context_variables_injected_into_tool | function |  |
| test_per_ask_tool_injection | function |  |
| test_config_override_per_ask | function |  |

## Chunks

### test_basic_ask (function, L31-L35)

> *Summary: This test verifies basic functionality by initializing an `Agent` with provided configuration and sending it a prompt to receive a response. It asserts that the returned message body contains the expected word, "ping".*


### test_static_system_prompt (function, L38-L47)

> *Summary: This test verifies that an `Agent` initialized with a static system prompt correctly adheres to its instructions when queried. It asserts the response contains both the expected answer and the required prefix ("Answer:").*


### test_dynamic_prompt_with_context (function, L50-L62)

> *Summary: This test verifies that an agent's prompt dynamically incorporates context provided during the request. It configures an agent, defines a prompt function that reads a `role` from the input context, and asserts the resulting response contains the specified role.*


### test_sync_tool_use (function, L65-L82)

> *Summary: This test verifies that an agent correctly utilizes a provided `add` tool when prompted with an arithmetic question. It asserts that the agent's response body contains the correct result and that the underlying tool was called at least once.*


### test_async_tool_use (function, L85-L99)

> *Summary: This test verifies an agent's ability to asynchronously use a provided tool. It initializes an agent with a mock stock lookup function and asserts that the agent correctly calls this tool to generate a response containing the expected price information.*


### test_multi_tool_dispatch (function, L102-L125)

> *Summary: This test verifies that an AI agent correctly selects and uses the appropriate tool based on a user query. It initializes an agent with three distinct tools (time, weather, news) and asserts that asking about Seattle's weather results in a response containing relevant information.*


### test_tool_error_propagates (function, L128-L147)

> *Summary: This test verifies that an agent can gracefully handle a tool failure by producing a response instead of crashing. It passes a custom tool that intentionally raises a `RuntimeError` and asserts the resulting reply body is non-empty.*


### test_structured_output_primitive (function, L150-L159)

> *Summary: This test verifies that an agent configured to return a primitive integer type correctly processes a mathematical query. It asserts that the final extracted content from the agent's response matches the expected numeric calculation (132).*


### test_structured_output_dataclass (function, L162-L179)

> *Summary: This test verifies that an agent correctly parses structured output from a language model based on a defined dataclass schema. It inputs a prompt describing a book and asserts the resulting object conforms to the `Book` structure with correct data extracted.*


### test_structured_output_pydantic (function, L182-L199)

> *Summary: This test verifies that an agent correctly parses and returns structured data conforming to a Pydantic schema. It feeds the agent a natural language prompt, expects a response object containing a `Person` instance, and asserts the extracted fields match the expected values from the input text.*


### test_multi_turn_ask_chain (function, L202-L218)

> *Summary: This test verifies that an agent maintains conversational context over multiple interactions. It sends a sequence of prompts, asserting that the agent correctly recalls previously provided information across three distinct turns.*


### test_streaming_chunks_arrive (function, L221-L241)

> *Summary: This test verifies that streamed responses correctly emit `ModelMessageChunk` events while processing an agent request configured for streaming. It asserts that the collected content from these chunks perfectly reconstructs the final response body returned by the agent.*


### test_dependency_injection_into_tool (function, L244-L267)

> *Summary: This test verifies that an `Agent` correctly receives and utilizes a dependency (`UserService`) injected into one of its provided tools. It initializes the agent with a service instance, calls it via a prompt, and asserts the resulting response contains data retrieved from the injected service.*


### test_context_variables_injected_into_tool (function, L270-L283)

> *Summary: This test verifies that context variables are correctly injected into a tool's execution when an agent uses it. It initializes an agent with a custom tool that reads a role from the provided context and asserts the resulting response body contains the expected role value.*


### test_per_ask_tool_injection (function, L286-L303)

> *Summary: This test verifies that providing a specific tool during an `ask()` call overrides or augments the agent's default toolset for that turn. It asserts that the agent successfully invokes the provided `secret_word` tool and includes its output ("zephyr") in the response body.*


### test_config_override_per_ask (function, L306-L311)

> *Summary: This test verifies that providing a `config` parameter during an agent's `ask()` call successfully overrides the agent's default configuration. It asserts that the resulting response body contains the expected text, confirming the override took effect.*

