# autogen/agentchat/groupchat.py

2 class(es): GroupChat, GroupChatManager. 44 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GroupChat | class |  |
| GroupChatManager | class |  |

## Chunks

### GroupChat (class, L50-L1180)

> *Summary: Manages a multi-agent conversation flow by tracking messages and controlling speaker turns based on various configuration options. It supports manual, random, round-robin, or automated (LLM-driven) selection of the next agent, while also enforcing eligibility policies and transition rules between participants.*


### __post_init__ (method, L190-L319, parent: GroupChat)

> *Summary: This method validates the configuration of a group chat instance after initialization, ensuring agent names are unique and that speaker transition rules are logically consistent. It computes an internal `allowed_speaker_transitions_dict` based on provided constraints and performs extensive checks on message templates, retry limits, and eligibility policies before finalizing setup.*


### _apply_eligibility_policies (method, L321-L360, parent: GroupChat)

> *Summary: Filters a list of candidate agents based on registered eligibility policies, which must all pass (AND semantics). It takes the current agent list, the last speaker, and the round index as input, returning only those agents that satisfy every defined policy or raising an error if none are eligible.*


### agent_names (method, L363-L365, parent: GroupChat)

> *Summary: Retrieves a list of strings containing the names of all agents participating in the current group chat session. It iterates over the internal `self.agents` collection to build and return this list.*


### reset (method, L367-L369, parent: GroupChat)

> *Summary: Clears all stored messages within the group chat instance, effectively resetting its conversation history for a fresh start.*


### append (method, L371-L384, parent: GroupChat)

> *Summary: Adds a message to the chat history, ensuring its content is converted to a string format suitable for text-based models and assigning the speaker's name if the message role isn't "function". The method takes a message dictionary and an `Agent` object as input and appends the processed message to the internal list.*


### agent_by_name (method, L386-L394, parent: GroupChat)

> *Summary: Retrieves a specific agent by its name, optionally searching through nested teams recursively. It returns the matching `Agent` object or `None`, raising an error if multiple agents share the same name and conflict checking is enabled.*


### nested_agents (method, L396-L403, parent: GroupChat)

> *Summary: Retrieves a complete list of all participating agents by recursively traversing any embedded `GroupChatManager` instances within the current group chat structure. It returns a flat list containing every agent found across all nested groups.*


### next_agent (method, L405-L427, parent: GroupChat)

> *Summary: Determines the subsequent agent in a defined sequence, either within all known agents or a specified subset. It calculates the next agent by advancing one position cyclically from the input agent's index within the relevant list.*


### select_speaker_msg (method, L429-L438, parent: GroupChat)

> *Summary: Generates the system prompt used to determine the next speaker in a group chat session. It takes an optional list of agents and constructs a message template containing the roles and names of all participants.*


### select_speaker_prompt (method, L440-L454, parent: GroupChat)

> *Summary: Generates a system prompt string used to determine the next speaker in a group chat. It takes an optional list of `Agent` objects, formats them into a comma-separated list, and injects this list into a predefined template.*


### introductions_msg (method, L456-L465, parent: GroupChat)

> *Summary: Generates the initial system message for group chat, which dictates speaker selection. It combines a predefined introductory message with a formatted string detailing the roles of all provided agents.*


### manual_select_speaker (method, L467-L496, parent: GroupChat)

> *Summary: This method prompts the user to manually select the next agent in a group chat by displaying available agents and accepting an index input. It handles invalid or missing inputs, eventually defaulting to `None` if selection fails after three attempts.*


### random_select_speaker (method, L498-L502, parent: GroupChat)

> *Summary: Selects a random agent from a provided list or the instance's internal list of agents. It returns one `Agent` object chosen uniformly at random.*


### _prepare_and_select_agents (method, L504-L676, parent: GroupChat)

> *Summary: Determines the next speaker in a group chat by first processing custom selection logic or applying eligibility policies based on function calls. It takes the `last_speaker` as input and outputs the chosen agent, the list of all eligible agents, and optional messages for API context.*


### select_speaker (method, L678-L689, parent: GroupChat)

> *Summary: Determines the next participant in a group conversation based on predefined logic. It first attempts to select an agent using internal preparation; if that fails and manual selection is active, it cycles to the next agent; otherwise, it uses automatic speaker selection for two-agent chats.*


### a_select_speaker (method, L691-L701, parent: GroupChat)

> *Summary: Determines the next participant in a group conversation based on predefined logic. It first attempts to select an agent using internal preparation; if that fails and manual mode is active, it advances to the subsequent agent; otherwise, it invokes an automatic speaker selection process for two-agent chats.*


### _finalize_speaker (method, L703-L719, parent: GroupChat)

> *Summary: Determines the next active agent after a turn concludes based on whether the conversation is finished and how many agents were mentioned in the final response. If the conversation isn't ending, it cycles to the next agent; otherwise, it attempts to resolve the speaker name from mentions or defaults to cycling if resolution fails.*


### _register_client_from_config (method, L721-L751, parent: GroupChat)

> *Summary: This method configures an agent by registering a specific model client class based on configuration input. It validates the provided `model_client_cls` against existing registered classes, either selecting the first match from a list or using a single predefined class before calling `agent.register_model_client`.*


### _register_custom_model_clients (method, L753-L762, parent: GroupChat)

> *Summary: If automatic LLM selection is enabled, this method registers custom model clients for a given agent based on the configuration provided in `select_speaker_auto_llm_config`. It handles both single and list-based configurations to populate the client registry.*


### _create_internal_agents (method, L764-L797, parent: GroupChat)

> *Summary: This method constructs two specialized agents: a `checking_agent` for validating speaker names and a `speaker_selection_agent` responsible for choosing one agent from the group. It configures these agents using provided messages, validation functions, and an LLM configuration derived from either the class instance or an optional selector.*


### _auto_select_speaker (method, L799-L880, parent: GroupChat)

> *Summary: This method automatically determines the next speaker by initiating a nested two-agent chat between a selector and validator agent. It feeds current group messages into this internal chat, iteratively prompting until a single agent is nominated or all selection attempts are exhausted, at which point it defaults to the next agent in sequence.*


### a_auto_select_speaker (method, L882-L961, parent: GroupChat)

> *Summary: This method asynchronously determines the next speaker in a group chat by initiating a nested two-agent conversation between a selector and validator agent. It iteratively refines the selection based on LLM responses up to a maximum number of attempts; otherwise, it defaults to the next agent in the provided list.*


### _validate_speaker_name (method, L963-L1055, parent: GroupChat)

> *Summary: Determines if a speaker name mentioned in the latest message is valid by checking for single mentions among provided agents. It outputs success or failure events based on the number of mentions and returns either the selected agent's name (on success) or a prompt to re-query the chat with specific instructions (on failure, depending on remaining attempts).*


### _process_speaker_selection_result (method, L1057-L1076, parent: GroupChat)

> *Summary: This method interprets the output from a speaker selection process to determine which agent should speak next. It returns the selected agent if the result indicates success, or it defaults to the subsequent agent in the sequence if the selection fails.*


### _participant_roles (method, L1078-L1090, parent: GroupChat)

> *Summary: Generates a formatted string listing the names and descriptions of provided or registered agents. It warns if any agent has an empty description, returning all entries separated by newlines.*


### _mentioned_agents (method, L1092-L1130, parent: GroupChat)

> *Summary: Calculates how many times each agent is referenced within a given message content by using regular expressions that account for exact matches, underscores replaced by spaces, and escaped underscores. It accepts either a string or list of strings as input and returns a dictionary mapping agent names to their mention counts.*


### _run_input_guardrails (method, L1132-L1144, parent: GroupChat)

> *Summary: This method executes input safety checks on an agent using provided messages. It returns the guardrail's reply if a check triggers, otherwise it returns `None`.*


### _run_output_guardrails (method, L1146-L1156, parent: GroupChat)

> *Summary: This method executes output validation checks on an agent's generated response, accepting the agent and its reply as input. It returns the modified reply if a guardrail check passes, or `None` otherwise.*


### _run_inter_agent_guardrails (method, L1158-L1180, parent: GroupChat)

> *Summary: Checks configured policy-driven guardrails against an incoming message between two agents. If any guardrail triggers a response, it returns the replacement content; otherwise, it returns nothing.*


### GroupChatManager (class, L1184-L1940)

> *Summary: Manages a group conversation among multiple agents, handling the flow of messages between participants. It provides synchronous and asynchronous methods to run chats, supports resuming conversations from saved states, and includes logic for clearing agent histories based on specific commands within replies.*


### __init__ (method, L1187-L1232, parent: GroupChatManager)

> *Summary: Initializes a chat manager instance by accepting a `GroupChat` object and configuration parameters like reply limits and input modes. It sets up internal state, enforces restrictions against tool/function calls in the LLM config, and registers callbacks for both synchronous and asynchronous group chat execution.*


### groupchat (method, L1235-L1237, parent: GroupChatManager)

> *Summary: Retrieves the internal `GroupChat` instance managed by the object. This method returns the active group conversation object.*


### chat_messages_for_summary (method, L1239-L1243, parent: GroupChatManager)

> *Summary: Retrieves all message dictionaries from the internal group chat state. This method returns the complete conversation history, ignoring any provided `Agent` input.*


### _prepare_chat (method, L1245-L1259, parent: GroupChatManager)

> *Summary: This method ensures all agents within a group chat are properly initialized for interaction. It resets the group chat history if requested and recursively calls `_prepare_chat` on every agent in the group, except potentially the recipient itself.*


### last_speaker (method, L1262-L1300, parent: GroupChatManager)

> *Summary: Retrieves the `Agent` object that originally sent the most recent message within a group chat context. This allows an agent receiving a relayed message from the manager to identify the true originator of the content.*


### run_chat (method, L1302-L1433, parent: GroupChatManager)

> *Summary: Executes a multi-agent group conversation loop, optionally starting with introductions and respecting round limits. It iteratively broadcasts messages between agents, handles guardrail checks on input and output, manages history clearing based on content, and terminates when conditions like message type or max rounds are met. Returns `(True, None)` upon completion.*


### a_run_chat (method, L1435-L1553, parent: GroupChatManager)

> *Summary: Executes an asynchronous group chat session by iteratively broadcasting messages between participating agents based on a defined round limit or termination conditions. It manages message flow, selects the next speaker, applies input/output guardrails, and handles history clearing before returning success status and no specific output.*


### resume (method, L1555-L1656, parent: GroupChatManager)

> *Summary: Restores a group chat session using prior messages provided as either a JSON string or a list of message dictionaries. It clears existing history across agents and the manager before loading the past conversation into the group chat state. The method returns the agent who spoke last and that final message, after optionally cleaning up termination strings from it.*


### a_resume (method, L1658-L1759, parent: GroupChatManager)

> *Summary: This method asynchronously restarts a group chat by loading historical messages, which can be provided as a JSON string or a list of message dictionaries. It clears existing histories across agents and the manager before populating the state, then returns the agent who spoke last and that final message.*


### _valid_resume_messages (method, L1761-L1783, parent: GroupChatManager)

> *Summary: Checks if a provided list of messages is valid for resuming a group chat session. It ensures the message list is non-empty and verifies that every agent mentioned in the messages actually exists within the current group chat configuration.*


### _process_resume_termination (method, L1785-L1821, parent: GroupChatManager)

> *Summary: This method modifies the last message in a list by optionally removing a specified termination string or applying a transformation function to its content. It then checks if the modified last message satisfies internal termination conditions, logging a warning if it does.*


### messages_from_string (method, L1823-L1837, parent: GroupChatManager)

> *Summary: Parses a JSON-formatted string representing saved chat history into a list of message dictionaries. It validates the input by catching `json.JSONDecodeError` and raises an exception if the string is malformed.*


### messages_to_string (method, L1839-L1849, parent: GroupChatManager)

> *Summary: This method serializes a list of message dictionaries into a JSON string. It takes a list of message objects as input and returns a single string representation suitable for chat state persistence.*


### _raise_exception_on_async_reply_functions (method, L1851-L1860, parent: GroupChatManager)

> *Summary: Ensures that no asynchronous reply functions are registered within the group chat or any of its constituent agents by recursively checking and raising a `RuntimeError` if such functions are found. This method enforces synchronous behavior across all participating agents in the group chat.*


### clear_agents_history (method, L1862-L1940, parent: GroupChatManager)

> *Summary: Analyzes a user's reply to determine if it contains a "clear history" command, extracting optional agent names or message counts. It then clears the chat history for specified agents or the entire groupchat based on the parsed arguments and returns the modified reply content without the command phrase.*

