# test/beta/providers/agent/test_extensibility.py

9 function(s): test_custom_middleware_on_turn, test_custom_middleware_on_llm_call, test_logging_middleware_doesnt_crash, test_add_middleware_at_runtime, test_insert_middleware_outermost, test_hitl_hook_provides_input, test_plugin_contributes_tool_and_prompt, test_plugin_with_dependencies_and_variables, test_multiple_plugins_compose.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_custom_middleware_on_turn | function |  |
| test_custom_middleware_on_llm_call | function |  |
| test_logging_middleware_doesnt_crash | function |  |
| test_add_middleware_at_runtime | function |  |
| test_insert_middleware_outermost | function |  |
| test_hitl_hook_provides_input | function |  |
| test_plugin_contributes_tool_and_prompt | function |  |
| test_plugin_with_dependencies_and_variables | function |  |
| test_multiple_plugins_compose | function |  |

## Chunks

### test_custom_middleware_on_turn (function, L22-L40)

> *Summary: This test verifies that custom middleware correctly intercepts and logs events during an agent's turn execution. It injects a `TraceMiddleware` to record the start and end of model request/response cycles when the agent is prompted.*


### test_custom_middleware_on_llm_call (function, L43-L67)

> *Summary: This test verifies that custom middleware correctly intercepts and counts all LLM interactions during an agent's execution. It injects a counting middleware into an agent configured with a simple arithmetic tool and asserts the total number of calls is at least two.*


### test_logging_middleware_doesnt_crash (function, L70-L78)

> *Summary: This test verifies that the `LoggingMiddleware` integrates without causing runtime errors when processing an agent's request. It initializes an agent with the middleware and asserts that a response body is successfully returned after asking it to say "ok".*


### test_add_middleware_at_runtime (function, L81-L94)

> *Summary: This test verifies that adding middleware dynamically to an `Agent` instance correctly injects the new layer into the execution chain. It confirms that a custom middleware's `on_turn` method is executed when the agent processes a request.*


### test_insert_middleware_outermost (function, L97-L123)

> *Summary: This test verifies that inserting a middleware using `insert_middleware` places it as the outermost wrapper in the execution chain. It asserts that the call sequence reflects this, with the newly inserted middleware executing its pre and post logic around the existing middleware's execution.*


### test_hitl_hook_provides_input (function, L126-L158)

> *Summary: This test verifies that a registered human-in-the-loop hook is correctly invoked when an agent requests input via `ctx.input(...)`. It sets up an agent with a specific tool and hook, then asserts that the hook captures the requested input and the final response reflects the tool's outcome.*


### test_plugin_contributes_tool_and_prompt (function, L161-L176)

> *Summary: This test verifies that a plugin can successfully inject both tools and prompts into an agent's execution context. It instantiates an agent with a custom plugin containing a tool, then queries the agent to confirm it correctly invokes the provided tool and returns its output.*


### test_plugin_with_dependencies_and_variables (function, L179-L205)

> *Summary: This test verifies that a plugin correctly propagates injected dependencies and configured variables to an agent during execution. It asserts that the agent's response reflects values sourced from both hardcoded dependencies ("alice") and defined variables ("admin").*


### test_multiple_plugins_compose (function, L208-L227)

> *Summary: This test verifies that an agent correctly composes functionality from multiple plugins without one plugin overriding another's contributions. It initializes an agent with two distinct plugins, each containing a specific tool, and asserts the final response includes the results from both tools when prompted to retrieve them.*

