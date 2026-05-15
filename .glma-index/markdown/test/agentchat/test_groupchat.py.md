# test/agentchat/test_groupchat.py

45 function(s): test_groupchat_init, test_groupchat_duplicate_agent_names, test_groupchat_multiple_duplicate_agent_names, test_groupchat_unique_agent_names, test_func_call_groupchat, test_chat_manager, _test_selection_method, test_speaker_selection_method, _test_n_agents_less_than_3, test_invalid_allow_repeat_speaker and 35 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_groupchat_init | function |  |
| test_groupchat_duplicate_agent_names | function |  |
| test_groupchat_multiple_duplicate_agent_names | function |  |
| test_groupchat_unique_agent_names | function |  |
| test_func_call_groupchat | function |  |
| test_chat_manager | function |  |
| _test_selection_method | function |  |
| test_speaker_selection_method | function |  |
| _test_n_agents_less_than_3 | function |  |
| test_invalid_allow_repeat_speaker | function |  |
| test_n_agents_less_than_3 | function |  |
| test_plugin | function |  |
| test_agent_mentions | function |  |
| test_termination | function |  |
| test_next_agent | function |  |
| test_send_intros | function |  |
| test_selection_helpers | function |  |
| test_init_default_parameters | function |  |
| test_graph_parameters | function |  |
| test_graceful_exit_before_max_round | function |  |
| test_clear_agents_history | function |  |
| test_get_agent_by_name | function |  |
| test_get_agent_by_name_duplicate_in_nested | function |  |
| test_get_nested_agents_in_groupchat | function |  |
| test_nested_teams_chat | function |  |
| test_custom_speaker_selection | function |  |
| test_custom_speaker_selection_with_transition_graph | function |  |
| test_custom_speaker_selection_overrides_transition_graph | function |  |
| test_role_for_select_speaker_messages | function |  |
| test_select_speaker_message_and_prompt_templates | function |  |
| test_speaker_selection_agent_name_match | function |  |
| test_role_for_reflection_summary | function |  |
| test_speaker_selection_auto_process_result | function |  |
| test_speaker_selection_validate_speaker_name | function |  |
| test_select_speaker_auto_messages | function |  |
| test_manager_messages_to_string | function |  |
| test_manager_messages_from_string | function |  |
| test_manager_resume_functions | function |  |
| test_manager_resume_returns | function |  |
| test_manager_resume_messages | function |  |
| test_custom_model_client | function |  |
| test_select_speaker_transform_messages | function |  |
| test_manager_resume_message_assignment | function |  |
| test_groupchat_with_deepseek_reasoner | function |  |
| test_groupchatmanager_no_llm_config | function |  |

## Chunks

### test_groupchat_init (function, L31-L41)

> *Summary: Verifies that a `GroupChat` instance initializes correctly, either with an empty message history or by accepting and storing initial messages provided during construction. It confirms the internal `messages` list accurately reflects the input state.*


### test_groupchat_duplicate_agent_names (function, L45-L59)

> *Summary: This test verifies that instantiating a `GroupChat` with two agents sharing the same name raises a `ValueError`. It confirms the system correctly prevents duplicate agent identifiers during group chat setup.*


### test_groupchat_multiple_duplicate_agent_names (function, L63-L73)

> *Summary: This test verifies that the `GroupChat` initialization raises a `ValueError` when provided with multiple agents sharing the same name (e.g., two "bob"s and two "alice"s). It confirms the system correctly detects and rejects duplicate agent identifiers during setup.*


### test_groupchat_unique_agent_names (function, L77-L93)

> *Summary: Verifies that a `GroupChat` instance correctly initializes and stores agents with distinct, predefined names ("writer" and "reviewer"). It confirms the agent count and verifies the specific name assigned to each agent within the chat structure.*


### test_func_call_groupchat (function, L96-L145)

> *Summary: This test verifies function calling behavior within group chats by simulating interactions between multiple agents. It asserts that the system correctly executes a specified function call from an initiating agent and records the resulting messages in the chat history, demonstrating both auto-speaker selection and round-robin speaker rotation.*


### test_chat_manager (function, L148-L182)

> *Summary: This test verifies the basic functionality of a `GroupChatManager` by simulating a conversation between two agents without requiring LLM configuration. It asserts that messages are correctly exchanged during chat initiation and confirms proper state resetting after the interaction, while also ensuring it raises an error when presented with a function call message.*


### _test_selection_method (function, L185-L257)

> *Summary: Sets up three conversational agents and a `GroupChatManager` to test different speaker selection strategies (`round_robin`, `auto`, `random`, `manual`). It executes the chat based on the provided method string, asserting specific message counts and content sequences for each strategy.*


### test_speaker_selection_method (function, L260-L262)

> *Summary: Iterates through a predefined list of speaker selection strategies to test the core selection logic. For each strategy string provided as input, it calls a helper function with the method name and a `MonkeyPatch` object.*


### _test_n_agents_less_than_3 (function, L265-L304)

> *Summary: Tests the behavior of group chats with one or two agents by initializing a `GroupChat` and running an initiation chat via a `GroupChatManager`. It asserts that the correct number of messages are exchanged based on the specified speaker selection method, while also verifying that attempting to run the chat with zero agents raises a `ValueError`.*


### test_invalid_allow_repeat_speaker (function, L307-L331)

> *Summary: This test verifies that initializing a `GroupChat` with an invalid value for `allow_repeat_speaker` raises a `ValueError`. It uses two predefined agents as input to confirm the expected error message is thrown when the speaker repetition setting is incorrect.*


### test_n_agents_less_than_3 (function, L334-L336)

> *Summary: This function iterates over several chat distribution methods ("auto", "round\_robin", etc.) and executes a shared test case for scenarios involving fewer than three agents. It ensures the core logic functions correctly across these different scheduling strategies.*


### test_plugin (function, L339-L370)

> *Summary: This test verifies group chat functionality by setting up two agents and mocking speaker selection to force one agent to speak first. It then initiates a conversation via a manager, asserting that the resulting message counts match expectations after a limited number of rounds.*


### test_agent_mentions (function, L373-L441)

> *Summary: This test verifies the `_mentioned_agents` method of a `GroupChat` object by checking how it counts agent mentions within a given string. It asserts correct counting based on exact matches, substring presence, word boundaries, and handling of special characters in agent names.*


### test_termination (function, L444-L493)

> *Summary: This test verifies group chat termination logic by first running a simulation with no custom termination check and asserting a fixed number of messages. It then re-runs the simulation using a lambda function to detect "TERMINATE" in messages, asserting that the conversation stops after only three turns.*


### test_next_agent (function, L496-L534)

> *Summary: This test verifies the `next_agent` method of a `GroupChat` instance by asserting correct turn progression based on specified agents and participant lists. It confirms round-robin selection logic for various group compositions and raises an expected error when no valid next agent can be determined.*


### test_send_intros (function, L537-L638)

> *Summary: This test verifies the behavior of group chat introductions and message flow within an AutoGen setup. It asserts that `GroupChat` correctly generates introductory messages based on the provided agents, and then confirms that a `GroupChatManager` initiates conversations with expected message counts when introductions are enabled or disabled.*


### test_selection_helpers (function, L641-L680)

> *Summary: This test verifies the speaker selection logic within a `GroupChat` instance initialized with three defined agents. It asserts that the generated messages and prompts correctly incorporate agent descriptions and then tests manual speaker selection using mocking.*


### test_init_default_parameters (function, L683-L687)

> *Summary: This test verifies that the `GroupChat` initializes correctly with default parameters, ensuring all provided agents are allowed to speak within the chat structure. It confirms that the internal transition dictionary permits every agent to participate as a speaker.*


### test_graph_parameters (function, L690-L725)

> *Summary: This test verifies the validation logic of `GroupChat` initialization by asserting that certain invalid configurations, such as incorrect speaker transition definitions or parameter settings, raise a `ValueError`. It confirms successful instantiation when valid parameters are provided, ensuring agents are correctly registered within the chat object.*


### test_graceful_exit_before_max_round (function, L728-L770)

> *Summary: This test verifies that a group chat terminates gracefully before reaching its maximum round limit when using specific speaker transition rules. It initializes three agents and a `GroupChatManager`, then asserts the final message count is exactly three, indicating an early stop condition was met.*


### test_clear_agents_history (function, L773-L982)

> *Summary: This test verifies the functionality of clearing chat history within an `autogen.GroupChat` setup. It executes several scenarios by simulating user input containing "clear history," testing how different parameters (like specified agents or message counts) affect which messages are retained in agent and group histories.*


### test_get_agent_by_name (function, L985-L1024)

> *Summary: This test verifies the `agent_by_name` method on a `GroupChat` instance by creating various agents and teams. It asserts that the method correctly retrieves specified agents using both direct and recursive searches, while also confirming it returns `None` for non-existent names under different conflict handling modes.*


### test_get_agent_by_name_duplicate_in_nested (function, L1027-L1060)

> *Summary: This test verifies the behavior of recursively searching for an agent by name within a nested group chat structure containing duplicate names. It asserts that the search returns one of the matching agents and confirms that attempting to retrieve the agent while enforcing conflict detection raises an `AgentNameConflictError`.*


### test_get_nested_agents_in_groupchat (function, L1063-L1087)

> *Summary: This test verifies the ability to retrieve all agents within a nested group chat structure. It constructs a hierarchy involving a user agent and two teams, each containing multiple members, then asserts that the total count of discoverable agents is correct.*


### test_nested_teams_chat (function, L1090-L1139)

> *Summary: This test verifies chat functionality within a nested team structure by setting up multiple agents and groups. It initiates communication from an agent in "team1" to an agent in "team2" and asserts that the expected messages are correctly exchanged between them.*


### test_custom_speaker_selection (function, L1142-L1182)

> *Summary: This test verifies custom speaker control within an AutoGen group chat by defining a function that dictates the next agent based on the last speaker. It initializes three agents and uses the custom selection logic to ensure a specific sequence of interactions occurs during the initiated chat, asserting the final history length is three.*


### test_custom_speaker_selection_with_transition_graph (function, L1185-L1255)

> *Summary: This test verifies that a group chat adheres to a specific, custom speaker sequence ($\text{a} \to \text{u} \to \text{t} \to \text{o} \to \text{g} \to \text{e} \to \text{n}$) despite having 26 available agents. It configures the chat with a custom speaker selection function and allowed transitions to enforce this exact conversational flow, asserting that the resulting sequence matches the expected order.*


### test_custom_speaker_selection_overrides_transition_graph (function, L1258-L1311)

> *Summary: This test verifies that a custom speaker selection function overrides predefined transition graph constraints within a group chat simulation. It initializes agents and a `GroupChat` configured with both allowed transitions and the overriding custom selector, then asserts that the desired agent sequence occurs during the chat initiation.*


### test_role_for_select_speaker_messages (function, L1314-L1391)

> *Summary: This test verifies the behavior of `role_for_select_speaker_messages` within a `GroupChat` configuration. It asserts that the specified role (e.g., "system", "user", or custom strings) correctly overrides the message role when simulating speaker selection, and it confirms that empty or `None` values raise a `ValueError`.*


### test_select_speaker_message_and_prompt_templates (function, L1394-L1484)

> *Summary: This test verifies the behavior of custom speaker selection templates within a `GroupChat` by initializing agents and testing how provided message and prompt templates are rendered with valid or empty/`None` inputs. It asserts that non-empty templates override defaults, while specific validation errors are raised when the message template is empty or `None`, but allows the prompt template to be empty or `None`.*


### test_speaker_selection_agent_name_match (function, L1487-L1576)

> *Summary: This test verifies the speaker selection logic within a group chat by checking how agent names are matched against messages. It confirms that the matching function correctly handles exact matches, extra text, escaped underscores, and spaces in the message content while maintaining case sensitivity for proper identification.*


### test_role_for_reflection_summary (function, L1579-L1616)

> *Summary: This test verifies the reflection summary mechanism within a group chat by mocking LLM responses. It initiates a conversation where one agent requests a summary using "reflection\_with\_llm," asserting that the underlying mock function is called with the specified `summary_role`.*


### test_speaker_selection_auto_process_result (function, L1619-L1674)

> *Summary: This test verifies the logic for determining the next speaker in a group chat based on a provided result message. It asserts that if the last message indicates success with an agent's name, that agent is returned; otherwise, it returns the subsequent agent in the predefined sequence.*


### test_speaker_selection_validate_speaker_name (function, L1677-L1841)

> *Summary: This test suite validates the logic for an internal function that processes LLM-returned speaker selections within a group chat context. It simulates various scenarios—single selection, multiple selections with/without retries, and no selections—to assert correct return values and message updates based on the number of attempts remaining.*


### test_select_speaker_auto_messages (function, L1844-L1936)

> *Summary: This test verifies the behavior of an `auto` speaker selection method within a group chat setup. It asserts that custom templates correctly override default messages for multiple or no-name scenarios and ensures that providing empty or `None` strings to these templates raises appropriate validation errors.*


### test_manager_messages_to_string (function, L1939-L1960)

> *Summary: This test verifies that a collection of message dictionaries can be correctly serialized into a JSON string format using the `GroupChatManager`. It takes an input list of structured messages and asserts that the resulting parsed JSON matches the original input structure exactly.*


### test_manager_messages_from_string (function, L1963-L1974)

> *Summary: This test verifies that a provided JSON string containing chat messages can be correctly parsed into a list of message dictionaries by the `GroupChatManager`. It asserts that the resulting Python structure matches the original input when serialized back to JSON.*


### test_manager_resume_functions (function, L1977-L2120)

> *Summary: This test suite verifies the resume functionality of a group chat manager, ensuring it correctly validates incoming messages against registered agents and processes termination signals. It specifically tests methods for stripping predefined or function-based termination strings from the last message while also logging warnings when termination criteria are met but not processed.*


### test_manager_resume_returns (function, L2123-L2152)

> *Summary: Verifies the `GroupChatManager`'s ability to resume a chat session by checking if it correctly returns the specified agent and the last message when provided with initial context. It also confirms that if no specific agent is identified in the input messages, the manager itself is returned as the active entity.*


### test_manager_resume_messages (function, L2155-L2180)

> *Summary: This test verifies that the `GroupChatManager` rejects invalid message inputs when calling its `resume` method. It asserts that exceptions are raised when attempting to resume with a number, an empty string, or a non-JSON formatted string.*


### test_custom_model_client (function, L2183-L2245)

> *Summary: This test defines and utilizes a mock `CustomModelClient` to simulate an LLM interaction within an `autogen.GroupChat`. It verifies that the group chat correctly instantiates this custom client for the speaker selection agent, ensuring both the correct class type and configuration are assigned.*


### test_select_speaker_transform_messages (function, L2248-L2284)

> *Summary: This test verifies the correct application and validation of speaker selection transforms within a `GroupChat`. It confirms that only a valid `TransformMessages` object can be set for automatic speaker selection, while also ensuring it correctly handles `None` or no input.*


### test_manager_resume_message_assignment (function, L2287-L2330)

> *Summary: This test verifies that a group chat manager correctly resumes a conversation by assigning incoming messages to the appropriate agents. It takes a list of historical messages as input and asserts that the returned agent and message are valid, while also confirming the internal state of an agent matches the provided history.*


### test_groupchat_with_deepseek_reasoner (function, L2340-L2381)

> *Summary: This test sets up a multi-agent group chat involving a user proxy and two assistants powered by DeepSeek for reasoning. It initiates a conversation about the stock market using an OpenAI mini configuration manager and asserts that the resulting summary is a string.*


### test_groupchatmanager_no_llm_config (function, L2384-L2404)

> *Summary: This test verifies that attempting to initiate a chat within a `GroupChatManager` without providing an LLM configuration raises a specific `ValueError`. It confirms the manager correctly enforces the requirement for an LLM setup when managing group conversations.*

