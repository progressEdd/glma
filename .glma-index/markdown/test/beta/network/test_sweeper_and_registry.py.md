# test/beta/network/test_sweeper_and_registry.py

7 function(s): _invoke, _agent, test_expectation_sweeper_fires_violations_in_background, test_custom_registry_does_not_leak_into_default, test_default_transition_registry_singleton_is_lazy, test_cross_tool_flow_exercises_all_six_tools, test_handlers_module_does_not_touch_hub_privates. 1 class(es): _CustomIsoTarget. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _invoke | function |  |
| _agent | function |  |
| test_expectation_sweeper_fires_violations_in_background | function |  |
| _CustomIsoTarget | class |  |
| test_custom_registry_does_not_leak_into_default | function |  |
| test_default_transition_registry_singleton_is_lazy | function |  |
| test_cross_tool_flow_exercises_all_six_tools | function |  |
| test_handlers_module_does_not_touch_hub_privates | function |  |

## Chunks

### _invoke (function, L63-L76)

> *Summary: This asynchronous function executes a provided tool with specific arguments and dependencies to retrieve its direct output. It constructs a `ToolCallEvent`, runs the tool against a new context, and then extracts either the content or data from the first part of the resulting event.*


### _agent (function, L79-L80)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `TestConfig`.*


### test_expectation_sweeper_fires_violations_in_background (function, L87-L142)

> *Summary: This test verifies that the background expectation sweeper correctly fires violation audits when running on real time, bypassing direct calls to `hub._expectation_tick()`. It sets up two agents in a conversation with an immediate manifest containing a "max\_silence" expectation and asserts that at least one corresponding audit record is generated after a short delay.*


### _CustomIsoTarget (class, L149-L154)

> *Summary: This class defines a target for an ISO transition, holding a descriptive label. Its `resolve` method dictates the next action by returning a decision to end the current turn with the specified reason.*


### resolve (method, L153-L154, parent: _CustomIsoTarget)

> *Summary: When called with a `state` and an `envelope`, this method immediately returns a `TransitionDecision` object indicating no next speaker and closing the current interaction based on the instance's label.*


### test_custom_registry_does_not_leak_into_default (function, L157-L185)

> *Summary: Verifies that registering custom types in a specific `TransitionRegistry` does not pollute or affect the default registry instance. It confirms that a graph can be successfully loaded using the custom registry while failing when the same data is loaded with a fresh default registry lacking the custom type definition.*


### test_default_transition_registry_singleton_is_lazy (function, L188-L197)

> *Summary: Verifies that the `TransitionRegistry` singleton is initialized lazily, meaning it's only created upon first access. It confirms subsequent calls return the same instance and successfully resolves a target from a provided dictionary input.*


### test_cross_tool_flow_exercises_all_six_tools (function, L204-L291)

> *Summary: This test verifies the interoperability of six network tools by simulating a multi-step interaction between two registered agents, Alice and Bob. It executes sequential calls to `peers`, `channels`, `say`, `tasks`, and `context` tools to confirm they function correctly within a shared hub environment.*


### test_handlers_module_does_not_touch_hub_privates (function, L297-L323)

> *Summary: This test verifies that the `handlers.py` module strictly avoids direct access to private attributes of the hub object. It reads the source code and asserts that none of a predefined list of forbidden private member names are present in the file's text.*

