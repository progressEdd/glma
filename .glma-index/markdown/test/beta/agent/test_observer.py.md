# test/beta/agent/test_observer.py

14 function(s): test_config, test_observer_fires_on_matching_event, test_observer_does_not_fire_on_non_matching_event, test_multiple_observers, test_async_decorated, test_decorate_any_event, test_agent_decorator_style, test_agent_decorator_style_any_event, test_per_call_observers, test_constructor_and_ask_observers_both_fire and 4 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_config | function |  |
| test_observer_fires_on_matching_event | function |  |
| test_observer_does_not_fire_on_non_matching_event | function |  |
| test_multiple_observers | function |  |
| test_async_decorated | function |  |
| test_decorate_any_event | function |  |
| test_agent_decorator_style | function |  |
| test_agent_decorator_style_any_event | function |  |
| test_per_call_observers | function |  |
| test_constructor_and_ask_observers_both_fire | function |  |
| test_observer_with_context_injection | function |  |
| test_observer_with_inject | function |  |
| test_observer_with_depends | function |  |
| test_observer_with_variable | function |  |

## Chunks

### test_config (function, L16-L17)

> *Summary: Creates and returns a `TestConfig` instance, initializing it with the string `"response"`. This function serves to provide a standardized configuration object for testing purposes.*


### test_observer_fires_on_matching_event (function, L21-L35)

> *Summary: This test verifies that an observer is triggered when the agent processes a specific event type. It initializes an agent with an observer and asserts that the provided mock function was called exactly once with a `ModelResponse` object after the agent executes a query.*


### test_observer_does_not_fire_on_non_matching_event (function, L39-L51)

> *Summary: This test verifies that an observer attached to an agent does not trigger when the event fired during execution does not match its expected type. It initializes an agent with a specific observer and asserts that the mock callback remains uncalled after running a simple query.*


### test_multiple_observers (function, L55-L71)

> *Summary: This test verifies that an `Agent` correctly notifies multiple registered observers when it processes a request. It asserts that both the request and response mock objects were called exactly once after the agent is asked a question.*


### test_async_decorated (function, L75-L91)

> *Summary: This test verifies that an observer decorated with `@observer` is correctly triggered when the `Agent` processes a request. It asserts that the mock function, which receives the model response event, was called exactly once after calling `agent.ask("Hi!")`.*


### test_decorate_any_event (function, L95-L111)

> *Summary: This test verifies that an observer decorated with `@observer()` is correctly triggered when the `Agent` processes a request. It asserts that the mock function receives the event object passed to it during the execution of `agent.ask("Hi!")`.*


### test_agent_decorator_style (function, L115-L130)

> *Summary: This test verifies that an observer decorator correctly intercepts and logs events emitted by an `Agent` during a call. It asserts that the provided mock function is called exactly once when the agent processes a message.*


### test_agent_decorator_style_any_event (function, L134-L149)

> *Summary: This test verifies that an observer decorated method is triggered when the agent processes a request. It initializes an agent, decorates a logging function to capture events, calls `agent.ask()`, and asserts that the mock was called with the event data.*


### test_per_call_observers (function, L153-L164)

> *Summary: This test verifies that an observer is triggered exactly once when the agent processes a specific input query. It initializes an agent with a configuration and then calls `agent.ask`, passing in a mocked observer to assert its invocation count.*


### test_constructor_and_ask_observers_both_fire (function, L168-L181)

> *Summary: This test verifies that both the constructor and `ask` methods of an observer are triggered when an agent is initialized with observers and subsequently queried. It asserts that the provided mock functions were called exactly once for each respective method call.*


### test_observer_with_context_injection (function, L185-L204)

> *Summary: This test verifies that an observer correctly captures model responses and context during agent execution. It injects a mock to assert that the observer function was called exactly once with the `ModelResponse` event and the stream ID from the provided context.*


### test_observer_with_inject (function, L208-L224)

> *Summary: This test verifies that an observer correctly captures and uses dependency injection during an agent's execution. It asserts that the mock function was called exactly once with the specific value provided in the `dependencies` dictionary when the agent is asked a question.*


### test_observer_with_depends (function, L228-L247)

> *Summary: This test verifies that an observer correctly receives and uses a dependency injected into its handler when the agent is queried. It asserts that the mock function was called exactly once with the provided dependency value from the input context.*


### test_observer_with_variable (function, L251-L267)

> *Summary: This test verifies that an observer correctly captures a variable passed into the agent's execution context. It asserts that the mock function is called exactly once with the specific value provided for `"myvar"` during the `agent.ask()` call.*

