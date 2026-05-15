# test/agentchat/group/test_multi_agent_chat.py

10 function(s): create_mock_agent, agent1, agent2, agent3, user_proxy, context_vars, mock_group_chat, mock_group_chat_manager, mock_tool_executor, pattern.

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
| pattern | function |  |

## Chunks

### create_mock_agent (function, L20-L50)

> *Summary: Generates a mock object conforming to `ConversableAgent` specifications, allowing for isolated testing of multi-agent interactions. It accepts an optional `Handoffs` structure to configure specific handoff behaviors on the returned mock agent.*


### agent1 (function, L54-L55)

> *Summary: This function generates and returns a mock object representing "agent1" using the `create_mock_agent` utility. It serves to simulate an agent instance for testing purposes.*


### agent2 (function, L59-L60)

> *Summary: This function generates and returns a mock object representing "agent2" by calling `create_mock_agent`. It serves to simulate the behavior of a specific agent within tests.*


### agent3 (function, L64-L65)

> *Summary: This function generates and returns a mock object representing "agent3" by calling `create_mock_agent`. It serves to simulate the behavior of a specific agent within tests.*


### user_proxy (function, L69-L77)

> *Summary: Creates and configures a mock object simulating the `UserProxyAgent` for testing purposes. This proxy is set up to return a predefined `ChatResult` when its `initiate_chat` method is called.*


### context_vars (function, L81-L82)

> *Summary: Returns a `ContextVariables` object initialized with a specific starting data dictionary. This provides the initial state for multi-agent interactions within tests.*


### mock_group_chat (function, L86-L92)

> *Summary: Creates and returns a mock object conforming to the `GroupChat` interface, pre-configured with empty lists for messages and agents. This mock simulates group chat behavior by providing predefined return values for speaker selection prompts and agent lookups.*


### mock_group_chat_manager (function, L96-L108)

> *Summary: Creates a mocked instance of the `GroupChatManager` with predefined attributes for testing purposes. This mock simulates chat initiation and state management by returning controlled values for methods like `initiate_chat`.*


### mock_tool_executor (function, L112-L121)

> *Summary: Creates and configures a mock implementation of `GroupToolExecutor` for testing purposes. This mock object simulates tool execution capabilities, providing predefined return values for methods like `has_next_target` and `get_next_target`.*


### pattern (function, L125-L127)

> *Summary: Creates and returns a mock object conforming to the `Pattern` specification. This helper function is used to simulate or substitute a pattern object during testing.*

