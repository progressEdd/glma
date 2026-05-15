# test/beta/agent/test_hitl.py

6 function(s): test_config, test_sync_hitl, test_async_hitl, test_hitl_decorator, test_hitl_decorator_override, test_hitl_not_set.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_config | function |  |
| test_sync_hitl | function |  |
| test_async_hitl | function |  |
| test_hitl_decorator | function |  |
| test_hitl_decorator_override | function |  |
| test_hitl_not_set | function |  |

## Chunks

### test_config (function, L16-L20)

> *Summary: This function constructs and returns a `TestConfig` object, initializing it with a specific tool call event named "my\_tool" and the string "result". It serves to set up test configurations for agent interactions.*


### test_sync_hitl (function, L24-L46)

> *Summary: This test verifies the synchronous Human-in-the-Loop (HITL) functionality of an agent by mocking tool execution and HITL hooks. It asserts that the mock was called with the expected final answer and that the HITL hook was triggered with the input prompt from the tool call.*


### test_async_hitl (function, L50-L70)

> *Summary: This test verifies asynchronous Human-in-the-Loop (HITL) functionality by instantiating an Agent with a mock tool and a custom HITL hook. When the agent is asked a question, it calls the mocked input function within the tool execution path, asserting that the expected response from the HITL hook was used.*


### test_hitl_decorator (function, L74-L94)

> *Summary: This test verifies the behavior of a human-in-the-loop (HITL) hook within an agent execution. It sets up an agent with a tool that prompts for input and asserts that the HITL hook correctly intercepts the process to return a predefined answer when the agent is asked a question.*


### test_hitl_decorator_override (function, L98-L124)

> *Summary: This test verifies that a decorator override takes precedence when multiple HITL hooks are defined on an agent. It asserts that the final executed hook's return value is used, specifically checking if the mock was called with the expected output from the overriding hook.*


### test_hitl_not_set (function, L128-L147)

> *Summary: This test verifies that an agent correctly invokes a mock function when a provided tool fails to receive human input within the specified timeout. It sets up an agent with a tool designed to catch `HumanInputNotProvidedError` and asserts that the mock was called exactly once during execution.*

