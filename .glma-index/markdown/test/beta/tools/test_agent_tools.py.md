# test/beta/tools/test_agent_tools.py

6 function(s): test_agent_with_function, test_agent_with_tool, test_agent_with_tool_decorator, test_agent_with_tool_decorator_options_override, test_final_tool, test_concurrent_tool_execution.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_agent_with_function | function |  |
| test_agent_with_tool | function |  |
| test_agent_with_tool_decorator | function |  |
| test_agent_with_tool_decorator_options_override | function |  |
| test_final_tool | function |  |
| test_concurrent_tool_execution | function |  |

## Chunks

### test_agent_with_function (function, L43-L50)

> *Summary: This test verifies that an `Agent` initialized with a custom tool correctly registers the tool's schema against a default structure. It instantiates an agent using a mock configuration and a simple function, then asserts the resulting tool schema matches expectations.*


### test_agent_with_tool (function, L53-L61)

> *Summary: This test verifies that an agent correctly initializes with a provided tool. It instantiates the `Agent` using a mock configuration and asserts that the schema of the first registered tool matches a predefined default structure.*


### test_agent_with_tool_decorator (function, L64-L72)

> *Summary: This test verifies that applying the `@agent.tool` decorator correctly registers a function as an available tool for an `Agent` instance, asserting its schema matches a predefined default structure. It initializes an agent with a mock configuration and then checks the registered tools against expected specifications.*


### test_agent_with_tool_decorator_options_override (function, L75-L89)

> *Summary: This test verifies that custom options provided to the `@agent.tool` decorator correctly override default tool metadata when registering a function with an agent instance. It asserts that the resulting tool schema reflects the specified name and description from the decorator arguments.*


### test_final_tool (function, L93-L107)

> *Summary: This test verifies an agent's interaction with a predefined tool by simulating a query and asserting the resulting output structure matches the expected data model. It initializes an agent with a mock tool, sends it a prompt, and validates that the response body contains the correct result from the executed tool.*


### test_concurrent_tool_execution (function, L111-L177)

> *Summary: This test verifies that an agent executes multiple provided tools concurrently rather than sequentially. It sets up three simulated slow tools and asserts that their execution markers appear in the correct interleaved order, specifically ensuring all starts precede all ends to confirm concurrent operation.*

