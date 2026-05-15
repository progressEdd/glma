# test/beta/agent/test_hooks_di.py

6 function(s): test_config, test_sync_hook_subscriber, test_async_hook_subscriber, test_hook_with_depends, test_hook_with_agent_dependency, test_hook_depends_override.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_config | function |  |
| test_sync_hook_subscriber | function |  |
| test_async_hook_subscriber | function |  |
| test_hook_with_depends | function |  |
| test_hook_with_agent_dependency | function |  |
| test_hook_depends_override | function |  |

## Chunks

### test_config (function, L16-L21)

> *Summary: This function constructs and returns a `TestConfig` object, initializing it with a specific `ModelResponse` containing the message "result". It serves to provide a predefined configuration for testing purposes.*


### test_sync_hook_subscriber (function, L25-L45)

> *Summary: This test verifies that a synchronous hook subscriber correctly intercepts and processes an agent's response when specific dependencies are met. It subscribes a callback to the agent's stream, which then calls mock methods based on input event content and dependency checks during execution.*


### test_async_hook_subscriber (function, L49-L66)

> *Summary: This test verifies that an asynchronous hook subscriber correctly intercepts and executes when the agent is asked a question with specific dependency values. It asserts that the mock function was called exactly once, confirming the subscription logic worked as expected during the execution flow.*


### test_hook_with_depends (function, L70-L90)

> *Summary: This test verifies dependency injection within an agent's execution flow by mocking a condition check. It subscribes a callback to the agent's response stream, asserting that a mock function is called exactly once with `True` when a specific dependency value is provided during the `ask` call.*


### test_hook_with_agent_dependency (function, L94-L111)

> *Summary: This test verifies an agent's behavior when it depends on a specific service injected via its configuration. It simulates the agent processing a request by subscribing a callback to the response stream and asserts that the mock dependency was called exactly once with `True`.*


### test_hook_depends_override (function, L115-L135)

> *Summary: This test verifies that overriding a dependency provider successfully substitutes the original function with a mock implementation during an agent's execution. It asserts that the mocked dependency is called exactly once with the expected overridden value ("1").*

