# test/beta/tools/test_toolkit.py

15 function(s): test_toolkit_schemas, test_toolkit_executes_tool, test_toolkit_multiple_tools, test_toolkit_mixed_with_standalone_tool, test_toolkit_with_context, test_toolkit_with_plain_functions, test_toolkit_mixed_functions_and_tools, test_toolkit_tool_decorator, test_toolkit_tool_decorator_with_options, test_toolkit_empty and 5 more. 1 class(es): TestMerger. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_toolkit_schemas | function |  |
| test_toolkit_executes_tool | function |  |
| test_toolkit_multiple_tools | function |  |
| test_toolkit_mixed_with_standalone_tool | function |  |
| test_toolkit_with_context | function |  |
| test_toolkit_with_plain_functions | function |  |
| test_toolkit_mixed_functions_and_tools | function |  |
| test_toolkit_tool_decorator | function |  |
| test_toolkit_tool_decorator_with_options | function |  |
| test_toolkit_empty | function |  |
| test_toolkit_middleware_applied_to_all_tools | function |  |
| test_toolkit_middleware_applied_to_decorator_tools | function |  |
| test_toolkit_middleware_ordering | function |  |
| test_tool_name_conflict | function |  |
| test_unsafe_override | function |  |
| TestMerger | class |  |

## Chunks

### test_toolkit_schemas (function, L19-L35)

> *Summary: This function verifies that a `Toolkit` correctly generates schema definitions for registered tools. It takes an asynchronous mock, creates a toolkit with addition and multiplication functions, and asserts the resulting list of schemas contains exactly two entries corresponding to those functions.*


### test_toolkit_executes_tool (function, L39-L56)

> *Summary: This test verifies that an agent correctly invokes a registered tool when prompted. It simulates the agent receiving a specific `ToolCallEvent` and asserts that the underlying mock function was called with the expected arguments (`a=2`, `b=3`) before returning the final completion status.*


### test_toolkit_multiple_tools (function, L60-L83)

> *Summary: This test verifies an agent's ability to use a specific tool from a toolkit when prompted. It configures the agent to execute a `multiply` call with inputs 4 and 5, asserting that only the multiplication function was invoked on the mock object.*


### test_toolkit_mixed_with_standalone_tool (function, L87-L110)

> *Summary: This test verifies an agent's ability to correctly invoke a specific tool when presented with mixed tool configurations. It initializes an agent with both bundled and standalone tools, then asserts that only the intended standalone tool was called with the correct arguments during execution.*


### test_toolkit_with_context (function, L114-L132)

> *Summary: This test verifies an agent's ability to use a tool that requires context by mocking external dependencies. It configures and runs an agent, asserting that the mocked language dependency was called with the expected value during tool execution.*


### test_toolkit_with_plain_functions (function, L136-L151)

> *Summary: This test verifies that an agent correctly invokes a provided tool when prompted. It passes a simple addition function wrapped in a `Toolkit` to the agent and asserts that the underlying mock was called with the expected arguments derived from the input configuration.*


### test_toolkit_mixed_functions_and_tools (function, L155-L177)

> *Summary: This test verifies an agent's behavior when provided with a mix of decorated and plain functions within its toolset. It asserts that the agent correctly invokes only the specified plain function (`plain`) based on the input configuration, while ignoring the decorated one.*


### test_toolkit_tool_decorator (function, L181-L197)

> *Summary: This test verifies that an agent correctly invokes a decorated tool when prompted. It sets up an agent with a toolkit containing a `greet` function and asserts that the mock dependency within the tool was called exactly once with the expected argument.*


### test_toolkit_tool_decorator_with_options (function, L201-L217)

> *Summary: This test verifies that an agent correctly invokes a decorated tool when prompted. It sets up an agent with a custom greeting tool and asserts that the mock function within the tool is called exactly once with the expected argument derived from the initial configuration.*


### test_toolkit_empty (function, L221-L228)

> *Summary: This test verifies that an agent configured with a toolkit correctly responds with the predefined "done" status when prompted. It initializes the necessary components and asserts the final output matches the configuration's termination signal.*


### test_toolkit_middleware_applied_to_all_tools (function, L232-L268)

> *Summary: This test verifies that a custom logging middleware correctly wraps all registered tools within a `Toolkit`. It executes an agent using the toolkit, asserting that the middleware's before and after hooks are called exactly once for each tool execution.*


### test_toolkit_middleware_applied_to_decorator_tools (function, L272-L300)

> *Summary: This test verifies that middleware correctly wraps tools decorated with `@toolkit.tool`. It sets up an agent using a toolkit containing logging middleware and asserts that the mock's `before` and `after` hooks are called when executing the decorated tool.*


### test_toolkit_middleware_ordering (function, L304-L339)

> *Summary: This test verifies the execution order of middleware by asserting that toolkit middleware runs before tool-specific middleware when an agent invokes a decorated function. It sets up a `Toolkit` with both types of middleware and checks if the recorded call sequence matches the expected precedence: `toolkit_mw`, then `tool_mw`, followed by the core `tool` execution.*


### test_tool_name_conflict (function, L342-L351)

> *Summary: This test verifies that the `Toolkit` raises a `ToolConflictError` when attempting to register two tools with the same name, either during initialization or via the `tool()` method call. It uses an inner function as the tool implementation for testing this conflict detection.*


### test_unsafe_override (function, L354-L361)

> *Summary: This test verifies that an existing function can be added to the toolkit using an unsafe override mechanism. It initializes a `Toolkit` with a placeholder function and then explicitly adds it again as an override, asserting the tool count remains one.*


### TestMerger (class, L364-L393)

> *Summary: This class tests the merging behavior of `Toolkit` objects and individual tools. It verifies that combining toolkits or mixing toolkits with standalone tools results in a unified collection, while duplicate tools are correctly overridden to maintain uniqueness.*


### test_merge_toolkits (method, L365-L374, parent: TestMerger)

> *Summary: This test verifies that merging two `Toolkit` instances correctly combines their constituent tools. It asserts that the resulting merged toolkit contains both the tools from the input toolkits, identified by their names.*


### test_merge_toolkit_and_tool (method, L376-L385, parent: TestMerger)

> *Summary: This test verifies that merging a `Toolkit` with another function correctly incorporates both functions into the resulting toolkit's list of tools. It asserts that the merged toolkit contains entries corresponding to both input functions, `add1` and `add2`.*


### test_merged_toolkit_overrides_tool (method, L387-L393, parent: TestMerger)

> *Summary: This test verifies that merging a `Toolkit` with an existing function results in the merged toolkit containing only the original function. It initializes a toolkit with a placeholder function and then merges it with the same function to assert the final tool list contains just that single entry.*

