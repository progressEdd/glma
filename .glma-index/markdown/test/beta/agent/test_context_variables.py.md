# test/beta/agent/test_context_variables.py

10 function(s): test_config, test_ask_variables, test_agent_variables, test_mixed_variables, test_variable_alias, test_variable_by_name, test_variable_with_default, test_variable_with_default_factory, test_set_variable_by_tool, test_variable_with_default_factory_called_once.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_config | function |  |
| test_ask_variables | function |  |
| test_agent_variables | function |  |
| test_mixed_variables | function |  |
| test_variable_alias | function |  |
| test_variable_by_name | function |  |
| test_variable_with_default | function |  |
| test_variable_with_default_factory | function |  |
| test_set_variable_by_tool | function |  |
| test_variable_with_default_factory_called_once | function |  |

## Chunks

### test_config (function, L16-L20)

> *Summary: Creates and returns a `TestConfig` instance, initializing it with a specific tool call event named "my\_tool" and the string "result". This function serves to provide a predefined configuration object for testing purposes.*


### test_ask_variables (function, L24-L40)

> *Summary: This test verifies that an agent correctly passes provided context variables to its registered tools during execution. It asserts that the mock function was called exactly once with the value supplied for the `"dep"` variable in the input prompt.*


### test_agent_variables (function, L44-L61)

> *Summary: This test verifies that an `Agent` correctly accesses and uses predefined context variables when executing a tool. It asserts that the mock function was called exactly once with the value provided for the "dep" variable in the agent's configuration.*


### test_mixed_variables (function, L65-L82)

> *Summary: This test verifies that an agent correctly merges its initial context variables with any additional variables provided during a query. It asserts that the mock function receives a dictionary containing both the pre-set and runtime variables.*


### test_variable_alias (function, L86-L102)

> *Summary: This test verifies that an agent correctly resolves a variable alias defined in its configuration when calling a tool. It asserts that the mock function receives the value bound to the `dep` variable ("1").*


### test_variable_by_name (function, L106-L122)

> *Summary: This test verifies that an agent correctly retrieves and uses a specific variable value when invoking a tool. It initializes an agent with predefined variables, calls the agent's `ask` method, and asserts that the mock function was called exactly once with the expected variable content.*


### test_variable_with_default (function, L126-L141)

> *Summary: This test verifies that an agent correctly uses a default value when a tool dependency is not explicitly provided during execution. It asserts that the mock function was called with the predefined default string, "1".*


### test_variable_with_default_factory (function, L145-L160)

> *Summary: This test verifies that an agent correctly initializes a tool dependency using a `default_factory` when the input is not provided. It asserts that the mock function receives an empty dictionary as its argument after the agent executes a query.*


### test_set_variable_by_tool (function, L164-L186)

> *Summary: This test verifies that an agent correctly updates and utilizes context variables when executing tools. It asserts that the value set by `my_tool` ("1") is subsequently passed as an argument to `another_tool` via a mock call.*


### test_variable_with_default_factory_called_once (function, L190-L222)

> *Summary: This test verifies that a default factory function is executed exactly once when initializing variables within an agent's tools. It asserts specific call counts and arguments for mock methods based on how the agent interacts with tools using stateful `Variable` dependencies.*

