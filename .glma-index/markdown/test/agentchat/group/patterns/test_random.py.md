# test/agentchat/group/patterns/test_random.py

1 class(es): TestRandomPattern. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestRandomPattern | class |  |

## Chunks

### TestRandomPattern (class, L16-L244)

> *Summary: This test suite verifies the functionality of a random pattern implementation for group chats. It uses mock objects to simulate various agents and context variables, asserting correct initialization, handoff generation logic (ensuring all participants are targeted), and proper interaction with parent class methods during chat preparation.*


### mock_agent (method, L18-L28, parent: TestRandomPattern)

> *Summary: This method constructs and returns a fully configured `MagicMock` object that simulates a `ConversableAgent`. It initializes the mock with specific attributes like a name, empty function maps, and predefined handoff structures for testing purposes.*


### mock_agent2 (method, L31-L41, parent: TestRandomPattern)

> *Summary: Constructs a mock object conforming to `ConversableAgent` specifications for testing purposes. This mock is initialized with specific attributes like a name and empty lists/mocks for handoff conditions, returning the fully configured test double.*


### mock_initial_agent (method, L44-L54, parent: TestRandomPattern)

> *Summary: This method constructs and returns a mock object simulating an initial conversational agent for testing purposes. It configures the mock with specific attributes like name, empty function maps, and predefined handoff structures.*


### mock_user_agent (method, L57-L66, parent: TestRandomPattern)

> *Summary: Generates a mock object conforming to the `ConversableAgent` interface for testing purposes. This mock is pre-configured with specific attributes like name, empty function maps, and initialized handoff structures.*


### context_variables (method, L69-L71, parent: TestRandomPattern)

> *Summary: Generates a `ContextVariables` object populated with predefined test data, specifically setting `"test_key"` to `"test_value"`. This method is used internally to establish the necessary context for testing scenarios.*


### test_init (method, L73-L88, parent: TestRandomPattern)

> *Summary: Verifies the correct setup of a `RandomPattern` instance by asserting that it correctly stores the provided initial and group agents, sets default configuration values like `user_agent` to `None`, and initializes internal structures as expected. This test confirms the pattern's state immediately after instantiation using mock agent objects.*


### test_generate_handoffs (method, L90-L113, parent: TestRandomPattern)

> *Summary: This test verifies that an instance of `RandomPattern` correctly configures handoffs for all provided agents. It asserts that each agent's `after_work` is set to a `RandomAgentTarget` containing references to every other agent in the group.*


### test_generate_handoffs_with_user_agent (method, L115-L140, parent: TestRandomPattern)

> *Summary: This test verifies that when generating handoffs using a `RandomPattern` with a user agent, every involved agent and the user agent are configured to pass control to another random agent after their work is done. It asserts that each agent's `set_after_work` method was called once, setting a target that includes all other participants in the pattern.*


### test_prepare_group_chat (method, L143-L193, parent: TestRandomPattern)

> *Summary: This test verifies the `prepare_group_chat` method's behavior when initializing a random pattern for group chat scenarios. It asserts that the superclass preparation, handoff generation, and final return structure match expected values based on provided mock inputs.*


### test_prepare_group_chat_with_user_agent (method, L196-L244, parent: TestRandomPattern)

> *Summary: This test verifies the `prepare_group_chat` method's behavior when a user agent is provided. It sets up mocks for agents and context, then calls the method to ensure it correctly invokes superclass methods and internal handoff generation logic with the specified inputs. The expected output structure is validated by checking the length of the returned tuple.*

