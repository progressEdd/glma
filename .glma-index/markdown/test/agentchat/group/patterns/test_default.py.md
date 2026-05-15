# test/agentchat/group/patterns/test_default.py

1 class(es): TestDefaultPattern. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestDefaultPattern | class |  |

## Chunks

### TestDefaultPattern (class, L16-L120)

> *Summary: This test suite verifies the initialization and core behavior of a default chat pattern implementation. It uses various mock agents and context variables as inputs to assert correct setup parameters, particularly ensuring that the pattern's configured `group_after_work` target overrides any value returned by its parent class during group preparation.*


### mock_agent (method, L18-L28, parent: TestDefaultPattern)

> *Summary: This method constructs and returns a mock object conforming to the `ConversableAgent` interface for testing purposes. It initializes various attributes like name, function maps, and handoff structures with default or empty values.*


### mock_initial_agent (method, L31-L41, parent: TestDefaultPattern)

> *Summary: This method constructs and returns a mock object simulating an initial conversational agent for testing purposes. It configures the mock with specific attributes like name, empty function maps, and predefined handoff structures.*


### mock_user_agent (method, L44-L53, parent: TestDefaultPattern)

> *Summary: Generates a mock object conforming to the `ConversableAgent` interface for testing purposes. This mock is pre-configured with specific attributes like name, empty function maps, and initialized handoff structures.*


### context_variables (method, L56-L58, parent: TestDefaultPattern)

> *Summary: Generates a `ContextVariables` object populated with predefined test data, specifically setting `"test_key"` to `"test_value"`. This method is used internally to establish the necessary context for testing purposes.*


### test_init (method, L60-L75, parent: TestDefaultPattern)

> *Summary: Verifies that a `DefaultPattern` instance initializes correctly with provided initial and group agents. It asserts the internal state matches the inputs, including default values for context variables, termination logic, and message summary methods.*


### test_prepare_group_chat (method, L78-L120, parent: TestDefaultPattern)

> *Summary: This test verifies the `prepare_group_chat` logic of a default pattern by mocking dependencies and asserting the structure of the returned tuple. It specifically confirms that the pattern correctly overrides or substitutes certain return values from its superclass implementation, such as ensuring the `group_after_work` object is the instance's own attribute rather than the mocked input.*

