# test/beta/test_plugin/test_plugin.py

1 function(s): test_plugin_middleware_is_invoked. 7 class(es): MockClient, TestPluginTools, TestPluginPrompts, TestPluginObservers, TestPluginDependenciesAndVariables, TestPluginHITLHook, TestMultiplePlugins. 21 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MockClient | class |  |
| TestPluginTools | class |  |
| TestPluginPrompts | class |  |
| TestPluginObservers | class |  |
| TestPluginDependenciesAndVariables | class |  |
| TestPluginHITLHook | class |  |
| test_plugin_middleware_is_invoked | function |  |
| TestMultiplePlugins | class |  |

## Chunks

### MockClient (class, L19-L38)

> *Summary: This class simulates an LLM client by recording the prompt provided in the `Context` object during invocation. It always returns a fixed `ModelResponse` containing a predefined reply message, regardless of the input messages or context details.*


### __init__ (method, L22-L23, parent: MockClient)

> *Summary: Initializes the object by storing a provided `MagicMock` instance as an internal attribute for later use in tests.*


### copy (method, L25-L26, parent: MockClient)

> *Summary: Returns a reference to the current instance, effectively creating a shallow copy of the object. This method allows for cloning the state of the mock client.*


### create (method, L28-L29, parent: MockClient)

> *Summary: This method returns the instance itself, effectively acting as a factory or constructor for creating a mock client object. It takes no arguments and outputs an object of type `MockClient`.*


### __call__ (method, L31-L38, parent: MockClient)

> *Summary: This asynchronous method simulates a plugin's execution by mocking the provided prompt within the context. It accepts a sequence of events and a context object, returning a fixed `ModelResponse` containing a "reply" message.*


### TestPluginTools (class, L42-L88)

> *Summary: These asynchronous test methods verify the functionality of tool invocation within an `Agent` by simulating interactions with a mock object. They demonstrate three scenarios: passing tools via the constructor, using a decorator to register tools on a plugin, and combining tools registered both in plugins and directly on the agent.*


### test_via_constructor (method, L43-L54, parent: TestPluginTools)

> *Summary: This test verifies that an agent correctly invokes a tool defined within a plugin when prompted. It initializes the agent with a specific configuration and asserts that the mocked function inside the tool was called exactly once after the agent processes the input query.*


### test_decorator (method, L56-L68, parent: TestPluginTools)

> *Summary: This test verifies that an agent correctly invokes a registered tool when prompted. It sets up a plugin with a decorated function and asserts that the provided mock is called exactly once during the agent's execution.*


### test_combined_with_agent_tools (method, L70-L88, parent: TestPluginTools)

> *Summary: This test verifies that tools from both plugins and the agent itself are correctly registered within an `Agent` instance. It executes a query, asserting that only the plugin tool is invoked while the agent's internal tool remains uncalled under specific configuration conditions.*


### TestPluginPrompts (class, L92-L117)

> *Summary: These asynchronous tests verify how an `Agent` interacts with registered plugins by calling a mocked client. They demonstrate scenarios for static prompts, dynamically defined prompts via decorators, and sequential execution across multiple plugins.*


### test_static (method, L93-L98, parent: TestPluginPrompts)

> *Summary: This test verifies that an `Agent` correctly invokes a specified plugin when asked a question. It asserts that the underlying mock client was called exactly once with the plugin's defined prompt.*


### test_dynamic (method, L100-L109, parent: TestPluginPrompts)

> *Summary: This test verifies that an agent correctly invokes a dynamically defined prompt within a plugin when asked a question. It asserts that the underlying mock client receives the expected string output from the plugin's prompt function.*


### test_multiple_plugins_ordered (method, L111-L117, parent: TestPluginPrompts)

> *Summary: This test verifies that an agent processes multiple plugins in the order they are provided. It initializes an agent with two distinct plugins and asserts that the underlying mock client is called exactly once, passing a list containing the prompts of both plugins sequentially.*


### TestPluginObservers (class, L121-L142)

> *Summary: This class contains asynchronous tests demonstrating how to hook into plugin events using two methods: passing observers during plugin instantiation and decorating a method on the plugin instance. Both tests verify that an observer callback is triggered when an `Agent` processes a request, asserting that a provided mock function was called exactly once.*


### test_via_constructor (method, L122-L129, parent: TestPluginObservers)

> *Summary: This test verifies plugin functionality by instantiating a `Plugin` with an observer and then running an `Agent` query. It asserts that the provided mock object was called exactly once after the agent processes the input.*


### test_decorator (method, L131-L142, parent: TestPluginObservers)

> *Summary: This test verifies that a plugin observer correctly intercepts an event when an agent is queried. It sets up an agent with a configured plugin and asserts that the provided mock function was called exactly once upon receiving a `ModelResponse`.*


### TestPluginDependenciesAndVariables (class, L146-L186)

> *Summary: These asynchronous tests verify how an `Agent` resolves and injects values into tools via plugin configurations. It confirms that tool execution correctly accesses dependencies and variables provided by both the plugin and the agent itself, with agent-level definitions overriding plugin ones.*


### test_dependencies_available_in_tool (method, L147-L160, parent: TestPluginDependenciesAndVariables)

> *Summary: This test verifies that a plugin correctly accesses its declared dependencies when an agent executes a tool call. It sets up an agent with a plugin and asserts that the mock dependency is called exactly once during the agent's interaction.*


### test_variables_available_in_tool (method, L162-L173, parent: TestPluginDependenciesAndVariables)

> *Summary: This test verifies that variables defined in a plugin are accessible within the tool execution context. It initializes an agent with a plugin containing a mockable tool and asserts that the tool receives the expected variable value during execution.*


### test_agent_dependencies_override_plugin (method, L175-L186, parent: TestPluginDependenciesAndVariables)

> *Summary: This test verifies that an agent correctly overrides a dependency when both the plugin and the agent define it. It sets up an agent with a plugin, calls the agent's ask method, and asserts that the mock was called using the agent's specified dependency source.*


### TestPluginHITLHook (class, L190-L255)

> *Summary: These methods test the behavior of a plugin's human-in-the-loop (HITL) hooks when integrated with an agent, demonstrating how to set hooks via constructor or decorator. The tests verify that the specified hook is called during agent execution and confirm that an agent-level hook overrides any plugin-defined hook.*


### test_via_constructor (method, L191-L205, parent: TestPluginHITLHook)

> *Summary: This test verifies plugin execution by initializing an `Agent` with a custom `Plugin` containing a mockable tool and a human-in-the-loop hook. It then calls the agent, asserting that the mocked input function within the tool was called exactly once with the expected "answer" value from the HITL hook.*


### test_decorator (method, L207-L222, parent: TestPluginHITLHook)

> *Summary: This test verifies that a plugin's human-in-the-loop hook is triggered when an agent processes a request. It sets up an agent with a tool and asserts that the hook returns a specific message upon execution.*


### test_agent_hook_overrides_plugin (method, L224-L242, parent: TestPluginHITLHook)

> *Summary: This test verifies that an agent's direct `hitl_hook` overrides any hook defined within its associated plugins. It sets up a plugin with a hook and an agent configured to use it, then asserts the agent's custom hook is executed instead when the agent processes input.*


### test_warn_on_double_set (method, L244-L255, parent: TestPluginHITLHook)

> *Summary: This test verifies that a `RuntimeWarning` is issued when two separate functions are registered as HITL hooks on the same plugin instance. It achieves this by defining and subsequently registering a second hook after the first one has been set up.*


### test_plugin_middleware_is_invoked (function, L259-L270)

> *Summary: This test verifies that a custom tracking middleware is executed when an agent processes a request. It sets up an agent with the middleware and asserts that the mock function within the middleware was called exactly once after the agent runs `agent.ask("Hi!")`.*


### TestMultiplePlugins (class, L274-L315)

> *Summary: Tests verify plugin registration and conflict resolution within an `Agent`. Specifically, one test confirms that the first registered plugin's tool is called when multiple plugins are present, while another asserts that the first plugin defining a HITL hook takes precedence over subsequent ones.*


### test_tools_all_registered (method, L275-L292, parent: TestMultiplePlugins)

> *Summary: This test verifies that an agent correctly invokes only the necessary tools based on its configuration and provided plugins. It initializes two plugins, each containing a single mockable tool, then runs an agent query to assert which specific tool methods were called during execution.*


### test_first_plugin_hitl_wins_and_warns_on_conflict (method, L294-L315, parent: TestMultiplePlugins)

> *Summary: This test verifies that when multiple plugins define a HITL hook, the first one registered takes precedence while issuing a warning about the conflict. It initializes an agent with two plugins and asserts that the output reflects the hook from the first plugin (`hook1`).*

