# test/beta/agent/test_tools_di.py

10 function(s): test_config, test_call_tool_with_injected_object, test_call_tool_with_agent_dependency, test_call_tool_with_mixed_dependencies, test_inject_alias, test_inject_by_custom_name, test_inject_with_default, test_miss_injection, test_depends_override, test_depends_override_toolkit.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_config | function |  |
| test_call_tool_with_injected_object | function |  |
| test_call_tool_with_agent_dependency | function |  |
| test_call_tool_with_mixed_dependencies | function |  |
| test_inject_alias | function |  |
| test_inject_by_custom_name | function |  |
| test_inject_with_default | function |  |
| test_miss_injection | function |  |
| test_depends_override | function |  |
| test_depends_override_toolkit | function |  |

## Chunks

### test_config (function, L17-L21)

> *Summary: Creates and returns a `TestConfig` instance, initializing it with a specific tool call event named "my\_tool" and the string "result". This function serves to provide mock configuration data for testing purposes.*


### test_call_tool_with_injected_object (function, L25-L43)

> *Summary: This test verifies that an agent correctly calls a registered tool, ensuring the provided dependency is injected into the tool's execution context. It asserts that the mock object was called exactly once with the specific dependency instance passed during the `ask` method invocation.*


### test_call_tool_with_agent_dependency (function, L47-L66)

> *Summary: This test verifies that an `Agent` correctly invokes a registered tool while injecting its specified dependencies. It asserts that the mock object was called exactly once with the provided dependency instance when the agent processes an input query.*


### test_call_tool_with_mixed_dependencies (function, L70-L87)

> *Summary: This test verifies that an agent correctly passes a merged set of dependencies to its tools when the agent itself has some and the incoming request provides others. It asserts that the mock dependency function was called exactly once with all combined dependencies.*


### test_inject_alias (function, L91-L111)

> *Summary: This test verifies that an `Agent` correctly injects a provided dependency into a tool's function signature during execution. It asserts that the mock object was called exactly once with the specific dependency instance passed to the agent configuration.*


### test_inject_by_custom_name (function, L115-L135)

> *Summary: This test verifies that an `Agent` correctly injects a specific dependency into a tool function when the dependency is registered with a custom name. It asserts that the provided mock object was called exactly once with the intended dependency instance during agent execution.*


### test_inject_with_default (function, L139-L156)

> *Summary: This test verifies that an `Agent` correctly injects a default value when a tool dependency is specified with one. It calls the agent, expecting the mocked dependency to be called exactly once with the provided default value (which is 1).*


### test_miss_injection (function, L160-L173)

> *Summary: This test verifies that an `Agent` fails with a `ValidationError` when its injected tool (`my_tool`) is provided without the necessary dependency configuration. It instantiates an agent using a mock configuration and asserts that calling it raises the expected validation error during execution.*


### test_depends_override (function, L177-L200)

> *Summary: This test verifies that dependency overrides correctly substitute a failing dependency with a successful one during tool execution. It configures an agent to use a tool whose input depends on a function, then overrides the dependency provider to return a specific value instead of raising an error when the agent runs.*


### test_depends_override_toolkit (function, L204-L226)

> *Summary: This test verifies that dependency overriding works by injecting a mocked value into a tool's dependency during an agent's execution. It sets up a scenario where a failing dependency is replaced with a successful return value, ensuring the tool executes correctly with the overridden input.*

