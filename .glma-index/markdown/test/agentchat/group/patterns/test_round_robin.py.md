# test/agentchat/group/patterns/test_round_robin.py

1 class(es): TestRoundRobinPattern. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestRoundRobinPattern | class |  |

## Chunks

### TestRoundRobinPattern (class, L16-L336)

> *Summary: This test suite verifies the functionality of a Round Robin pattern implementation for agent group chats. It uses mock objects to test initialization, handoff generation logic (including single-agent, multi-agent, and user-agent scenarios), and the overall `prepare_group_chat` method by mocking its parent class behavior.*


### mock_agent1 (method, L18-L28, parent: TestRoundRobinPattern)

> *Summary: This method constructs and returns a mock object conforming to the `ConversableAgent` interface for testing purposes. It initializes key attributes like name, function maps, and handoff structures with default or empty values.*


### mock_agent2 (method, L31-L41, parent: TestRoundRobinPattern)

> *Summary: Constructs a mock object conforming to the `ConversableAgent` interface for testing purposes. This mock is pre-configured with specific attributes like name, empty function maps, and initialized handoff structures.*


### mock_agent3 (method, L44-L54, parent: TestRoundRobinPattern)

> *Summary: Constructs a mock object conforming to `ConversableAgent` for testing purposes. This mock is pre-configured with specific attributes like name, empty function maps, and initialized handoff structures.*


### mock_initial_agent (method, L57-L67, parent: TestRoundRobinPattern)

> *Summary: This method constructs and returns a mock object conforming to the `ConversableAgent` interface for testing purposes. It initializes several attributes on this mock, including setting its name and configuring various handoff-related properties to default or empty states.*


### mock_user_agent (method, L70-L79, parent: TestRoundRobinPattern)

> *Summary: This method constructs and returns a mock object conforming to the `ConversableAgent` interface for testing purposes. It initializes the mock with specific attributes like name, empty function maps, and predefined handoff structures.*


### context_variables (method, L82-L84, parent: TestRoundRobinPattern)

> *Summary: Generates a `ContextVariables` object populated with predefined test data, specifically setting `"test_key"` to `"test_value"`. This method is used internally to establish the necessary context for testing scenarios.*


### test_init (method, L86-L101, parent: TestRoundRobinPattern)

> *Summary: This test verifies the correct initialization of a `RoundRobinPattern` instance. It asserts that the provided initial agent and list of agents are correctly stored, along with verifying default settings for context variables, termination logic, and message handling.*


### test_generate_handoffs_with_single_agent (method, L103-L120, parent: TestRoundRobinPattern)

> *Summary: Verifies that when a `RoundRobinPattern` is initialized with only one agent, the internal handoff generation method causes the initial agent to schedule a self-handoff after its work completes. It asserts that the resulting handoff target correctly points back to the same agent.*


### test_generate_handoffs_with_multiple_agents (method, L122-L156, parent: TestRoundRobinPattern)

> *Summary: This test verifies that a `RoundRobinPattern` correctly sequences handoffs among multiple agents. It asserts that each agent, when processing, calls its `set_after_work` method to pass control sequentially to the next agent in the defined rotation, looping back to the first agent upon completion.*


### test_generate_handoffs_with_user_agent (method, L158-L193, parent: TestRoundRobinPattern)

> *Summary: This test verifies that the `RoundRobinPattern` correctly generates a cyclical handoff sequence when a user agent is involved. It asserts that the initial agent hands off to the first agent, which then hands off to the user agent, and finally the user agent hands back to the initial agent.*


### test_generate_handoffs_with_initial_agent_not_first (method, L195-L232, parent: TestRoundRobinPattern)

> *Summary: Verifies that the `RoundRobinPattern` correctly generates a cyclical handoff chain when the specified initial agent is not the first element in the provided list of agents. It asserts that each agent sequentially hands off to the next agent in the reordered sequence, ultimately looping back to the starting agent.*


### test_prepare_group_chat (method, L235-L285, parent: TestRoundRobinPattern)

> *Summary: This test verifies the `prepare_group_chat` method of a round-robin pattern, ensuring it correctly initializes and calls its superclass preparation logic with specified inputs like maximum rounds and messages. It then asserts that internal methods are called with the correct agent configurations and validates the structure and integrity of the returned result tuple.*


### test_prepare_group_chat_with_user_agent (method, L288-L336, parent: TestRoundRobinPattern)

> *Summary: This test verifies the `prepare_group_chat` method's behavior when a user agent is provided. It sets up mocks for agents and context, then calls the method to ensure it correctly invokes superclass methods and internal handoff generation logic with the specified inputs.*

