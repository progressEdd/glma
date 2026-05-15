# test/beta/agent/test_test_config.py

5 function(s): test_config, test_tool_raise_exc, test_tool_not_found, test_ask_with_explicit_config_option, test_ask_without_any_config.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_config | function |  |
| test_tool_raise_exc | function |  |
| test_tool_not_found | function |  |
| test_ask_with_explicit_config_option | function |  |
| test_ask_without_any_config | function |  |

## Chunks

### test_config (function, L16-L20)

> *Summary: Creates and returns a `TestConfig` instance, initializing it with a specific tool call event named "my\_tool" and the string "result". This function serves to provide a predefined configuration object for testing purposes.*


### test_tool_raise_exc (function, L24-L35)

> *Summary: This test verifies that an agent correctly propagates exceptions raised by its tools during execution. It initializes an agent with a tool that intentionally raises a `ValueError` and asserts that the main query call catches this specific exception.*


### test_tool_not_found (function, L39-L46)

> *Summary: This test verifies that an `Agent` raises a `ToolNotFoundError` when it attempts to use a non-existent tool during interaction. It initializes the agent with a specific configuration and asserts the expected exception is raised upon calling the `ask` method.*


### test_ask_with_explicit_config_option (function, L50-L58)

> *Summary: This test verifies that an agent correctly processes a query when provided with an explicit configuration object. It calls the `ask` method, passing a specific `TestConfig`, and asserts that the returned response body matches the configured value.*


### test_ask_without_any_config (function, L62-L66)

> *Summary: This test verifies that attempting to use an `Agent` initialized without any configuration will raise a `ConfigNotProvidedError` when the `ask` method is called with input. It asserts the expected exception occurs during the asynchronous call.*

