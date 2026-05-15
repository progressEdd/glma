# test/agentchat/group/test_group_utils.py

9 function(s): create_mock_agent, agent1, agent2, agent3, user_proxy, context_vars, mock_group_chat, mock_group_chat_manager, mock_tool_executor. 1 class(es): TestHelperFunctions. 24 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| create_mock_agent | function |  |
| agent1 | function |  |
| agent2 | function |  |
| agent3 | function |  |
| user_proxy | function |  |
| context_vars | function |  |
| mock_group_chat | function |  |
| mock_group_chat_manager | function |  |
| mock_tool_executor | function |  |
| TestHelperFunctions | class |  |

## Chunks

### create_mock_agent (function, L56-L86)

> *Summary: Generates a fully mocked `ConversableAgent` instance configured for testing group interactions. It accepts an optional `Handoffs` object to configure specific handoff behaviors, returning the mock agent ready for simulation.*


### agent1 (function, L90-L91)

> *Summary: Creates and returns a mock object representing an agent named "agent1" using the `create_mock_agent` utility. This function is used for testing purposes to simulate agent behavior.*


### agent2 (function, L95-L96)

> *Summary: This function generates and returns a mock object configured to represent "agent2" using the `create_mock_agent` utility. It serves as a standardized test fixture for simulating this specific agent's behavior.*


### agent3 (function, L100-L101)

> *Summary: This function generates and returns a mock object configured to represent an agent named "agent3". It serves as a utility for testing scenarios involving this specific agent.*


### user_proxy (function, L105-L117)

> *Summary: Creates and configures a mock object simulating a `UserProxyAgent` for testing purposes. This proxy is initialized with specific attributes like name, context variables, and mocked chat initiation capabilities.*


### context_vars (function, L121-L122)

> *Summary: Creates and returns a `ContextVariables` object initialized with a specific starting data dictionary. This function provides a standardized initial state for context management within the agent chat system.*


### mock_group_chat (function, L126-L132)

> *Summary: Creates and returns a mock object simulating a `GroupChat` instance, pre-configured with empty lists for messages and agents. This mock also sets up specific return values and side effects for methods like speaker selection and agent lookup.*


### mock_group_chat_manager (function, L136-L148)

> *Summary: Creates a fully mocked instance of the `GroupChatManager` for testing purposes. This mock is pre-configured with specific attributes like a test LLM configuration and mockable methods for initiating or resuming chats.*


### mock_tool_executor (function, L152-L162)

> *Summary: Creates and returns a mock implementation of `GroupToolExecutor` with predefined attributes and mocked methods for simulating tool execution behavior in tests. This setup allows testing logic that interacts with the group's tooling without actual external calls.*


### TestHelperFunctions (class, L165-L890)

> *Summary: This code chunk contains a suite of unit tests for utility functions managing agent handoffs, group chat setup, and message processing within an AI agent framework. It verifies behaviors such as conditional function updates, establishing group agent hooks, validating target agents in groups, and correctly filtering transit messages during conversation flow.*


### test_update_conditional_functions (method, L166-L205, parent: TestHelperFunctions)

> *Summary: This test verifies the logic of updating agent functions based on condition availability. It simulates an agent with a conditional function, checks that the tool is removed and the function is added when the condition is met, and confirms no function is added when the condition fails.*


### test_establish_group_agent (method, L207-L222, parent: TestHelperFunctions)

> *Summary: This test verifies that the `establish_group_agent` function correctly configures an input agent by registering specific hooks and replies, and subsequently sets internal state flags on the agent object. It asserts that the agent has a display name method and that its group establishment status is set to true after setup.*


### test_link_agents_to_group_manager (method, L224-L232, parent: TestHelperFunctions)

> *Summary: This test verifies that a utility function correctly associates provided agents with the group chat manager. It asserts that both input agents have their internal `_group_manager` attribute set to the passed-in mock manager object.*


### test_run_oncontextconditions_triggered (method, L234-L257, parent: TestHelperFunctions)

> *Summary: This test verifies that an `OnContextCondition` correctly triggers a handoff when its associated condition evaluates to true and it is available. It calls the internal runner function with an agent configured with this condition, asserting that the target agent receives a call to set its next target.*


### test_run_oncontextconditions_not_triggered (method, L259-L275, parent: TestHelperFunctions)

> *Summary: This test verifies that an `OnContextCondition` does not trigger when its associated context condition evaluates to false. It mocks the necessary conditions and agent state, then asserts that the execution function returns failure and confirms the context evaluation method was called once with the agent's context variables.*


### test_create_on_condition_handoff_function (method, L277-L282, parent: TestHelperFunctions)

> *Summary: This test verifies that a utility function correctly generates and returns a callable handoff function. It takes an `AgentTarget` object as input and asserts the resulting function is callable and returns the original target upon execution.*


### test_create_on_condition_handoff_functions (method, L284-L300, parent: TestHelperFunctions)

> *Summary: This test verifies that a function correctly generates and registers handler functions for multiple `OnCondition` triggers on an agent. It takes two mock agents as input, configures the first agent with conditions targeting different entities, and asserts that the necessary internal methods were called exactly twice with the correct condition details.*


### test_validate_handoff_target_agent_target_valid (method, L302-L305, parent: TestHelperFunctions)

> *Summary: This test verifies that the handoff validation function accepts an `AgentTarget` when it belongs to a group. It asserts that calling the validation with a valid target and group context does not raise an exception.*


### test_validate_handoff_target_agent_target_invalid (method, L307-L311, parent: TestHelperFunctions)

> *Summary: This test verifies that attempting to validate a handoff target agent not present in the provided group list raises a `ValueError`. It asserts that the validation function correctly rejects an unknown agent name.*


### test_validate_handoff_target_random_valid (method, L313-L316, parent: TestHelperFunctions)

> *Summary: This test verifies that the handoff validation passes when a `RandomAgentTarget` is configured with all agents present in the provided group list. It asserts that calling the validation function with this setup does not result in an exception.*


### test_validate_handoff_target_random_invalid (method, L318-L324, parent: TestHelperFunctions)

> *Summary: This test verifies that `_validate_handoff_target` raises a `ValueError` when a target agent specified in a `RandomAgentTarget` is not present in the provided group list. It uses mock agents to simulate an invalid handoff scenario where one agent is outside the allowed group members.*


### test_validate_handoff_target_other_target_types (method, L326-L329, parent: TestHelperFunctions)

> *Summary: This test verifies that the handoff validation function correctly ignores non-agent target types. It asserts that calling the validator with `StayTarget` and `TerminateTarget` objects does not raise an exception when provided a list of agents and a test identifier.*


### test_ensure_handoff_agents_in_group (method, L331-L356, parent: TestHelperFunctions)

> *Summary: This test verifies that all target agents specified within an agent's handoff conditions (both LLM and context) are present in the provided group of agents. It asserts that a `ValueError` is raised if any referenced agent name does not exist within the input list.*


### test_ensure_handoff_random_agent_target_in_group (method, L358-L396, parent: TestHelperFunctions)

> *Summary: This test verifies that handoff targets specified by `RandomAgentTarget` only include agents present within a given group. It asserts correct behavior for valid configurations and raises a `ValueError` when the target includes an agent outside the provided group list across LLM, context, and after-works conditions.*


### test_ensure_guardrail_agents_in_group (method, L398-L421, parent: TestHelperFunctions)

> *Summary: This test verifies that an agent's handoff configurations correctly reference only agents present within a provided group. It asserts that attempting to use non-existent agents in `OnCondition` or `OnContextCondition` triggers a `ValueError`.*


### test_prepare_exclude_transit_messages (method, L424-L441, parent: TestHelperFunctions)

> *Summary: This test verifies the setup for excluding transit messages by ensuring a specific removal function is registered as a hook on both agents. It confirms that the necessary condition and handoff logic are correctly configured before applying the message filtering mechanism.*


### test_wrap_agent_handoff_targets (method, L443-L497, parent: TestHelperFunctions)

> *Summary: This test verifies how agent handoff targets are wrapped by checking if `OnCondition` and `OnContextCondition` targets are correctly replaced with `AgentTarget` instances after calling a wrapping utility function. It sets up two agents and configures them with nested chat targets for testing the wrapping mechanism.*


### test_process_initial_messages (method, L499-L561, parent: TestHelperFunctions)

> *Summary: This test verifies the `process_initial_messages` function's behavior when initializing group conversations. It checks how the function handles various inputs—such as string messages, pre-existing message lists, and the presence or absence of a user proxy—to correctly determine the initial message sequence, the last speaking entity, and any temporary agents created.*


### test_setup_context_variables (method, L563-L581, parent: TestHelperFunctions)

> *Summary: This test verifies that a shared `ContextVariables` object is correctly assigned to the `context_variables` attribute of multiple mocked agents, the tool executor, group chat manager, and user proxy. It asserts that all these components reference the exact same instance of the provided context variables.*


### test_cleanup_temp_user_messages (method, L583-L605, parent: TestHelperFunctions)

> *Summary: This test verifies that a utility function correctly removes the temporary `"_User"` name from user messages within a chat history structure. It asserts that only messages explicitly marked with this temporary name are modified, leaving other entries untouched.*


### test_get_last_agent_speaker (method, L607-L639, parent: TestHelperFunctions)

> *Summary: This test verifies a utility function that determines the last speaking agent from a list of chat messages. It takes a mocked chat object containing messages and a list of target agent names as input, returning the corresponding agent mock if found, or raising an error otherwise.*


### test_determine_next_agent (method, L642-L781, parent: TestHelperFunctions)

> *Summary: This test suite verifies the logic for selecting the next active agent in a group chat based on various conversational states. It simulates scenarios such as initial responses, tool execution handoffs, user input, and post-response transitions (like staying or terminating).*


### test_create_group_transition (method, L783-L831, parent: TestHelperFunctions)

> *Summary: This test verifies the logic of a group transition function by simulating two sequential calls. It asserts that the first call correctly uses an initial agent determination, while the subsequent call bypasses this initial logic to select the next agent based on the mocked return value.*


### test_make_remove_function (method, L833-L890, parent: TestHelperFunctions)

> *Summary: Given a list of chat messages and a set of tool names to exclude, this code tests the utility's ability to filter out specific tool calls and their corresponding responses from the message history. It asserts that messages containing specified tools are entirely removed or modified as expected in the resulting list.*

