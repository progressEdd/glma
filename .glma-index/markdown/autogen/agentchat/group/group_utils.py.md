# autogen/agentchat/group/group_utils.py

21 function(s): update_conditional_functions, establish_group_agent, link_agents_to_group_manager, _evaluate_after_works_conditions, _run_oncontextconditions, _create_on_condition_handoff_function, create_on_condition_handoff_functions, _validate_handoff_target, ensure_handoff_agents_in_group, ensure_guardrail_agents_in_group and 11 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| update_conditional_functions | function |  |
| establish_group_agent | function |  |
| link_agents_to_group_manager | function |  |
| _evaluate_after_works_conditions | function |  |
| _run_oncontextconditions | function |  |
| _create_on_condition_handoff_function | function |  |
| create_on_condition_handoff_functions | function |  |
| _validate_handoff_target | function |  |
| ensure_handoff_agents_in_group | function |  |
| ensure_guardrail_agents_in_group | function |  |
| prepare_exclude_transit_messages | function |  |
| prepare_group_agents | function |  |
| wrap_agent_handoff_targets | function |  |
| process_initial_messages | function |  |
| setup_context_variables | function |  |
| cleanup_temp_user_messages | function |  |
| get_last_agent_speaker | function |  |
| determine_next_agent | function |  |
| create_group_transition | function |  |
| create_group_manager | function |  |
| make_remove_function | function |  |

## Chunks

### update_conditional_functions (function, L36-L56)

> *Summary: This utility dynamically manages an agent's available tools by iterating through its handoff conditions. It removes any function associated with a condition and then re-adds it only if the condition evaluates to true given the current agent state and message history.*


### establish_group_agent (function, L59-L79)

> *Summary: This function configures an existing conversational agent to operate within a group context by registering specific hooks and reply functions. It customizes the agent's string representation, sets internal flags, and prioritizes running on-context condition checks before standard replies.*


### link_agents_to_group_manager (function, L82-L90)

> *Summary: Assigns a `GroupChatManager` instance to every provided `Agent` object, enabling them to access shared resources like the tool executor. This operation is used to establish communication pathways between agents and the central chat manager.*


### _evaluate_after_works_conditions (function, L93-L135)

> *Summary: Checks an agent's defined "after works" conditions against the current group chat state and context variables. If a matching condition is found, it resolves the target speaker selection, emits a transition event, and returns the resulting speaker choice; otherwise, it returns `None`.*


### _run_oncontextconditions (function, L138-L162)

> *Summary: Checks an agent's defined context conditions against the current state (messages and configuration) to determine if a handoff should occur. If any condition is met, it activates the target agent, emits a transition event, and returns `True` along with a status message.*


### _create_on_condition_handoff_function (function, L165-L178)

> *Summary: Generates a callable function that returns a specified `TransitionTarget`. This factory is used to define the action taken when a predefined condition triggers a handoff within an agent interaction.*


### create_on_condition_handoff_functions (function, L181-L197)

> *Summary: This utility populates an agent's handoff mechanisms by generating specific functions for each defined `OnCondition`. It iterates through the agent's conditions and registers a corresponding function that executes when the condition is met, using the target specified in the condition.*


### _validate_handoff_target (function, L200-L214)

> *Summary: Ensures that any specified agent or set of agents within a handoff transition actually exists among the provided group members. It raises an error if the target references an unknown agent name, using context for detailed error reporting.*


### ensure_handoff_agents_in_group (function, L217-L226)

> *Summary: Validates that all agents specified as handoff targets within an input list of agents are actually present in that same group. It checks targets across LLM conditions, context conditions, and after-work triggers to ensure they belong to the provided set.*


### ensure_guardrail_agents_in_group (function, L229-L238)

> *Summary: Validates that any agents referenced as targets within an agent's input or output guardrails are actually present in the provided list of agents. It raises a `ValueError` if a targeted agent is missing from the group.*


### prepare_exclude_transit_messages (function, L241-L256)

> *Summary: This function identifies all tool names associated with an agent's handoff conditions and then registers a cleanup hook on every provided agent. This hook is designed to automatically filter out messages related to those identified transit functions before agents generate replies.*


### prepare_group_agents (function, L259-L306)

> *Summary: This function initializes a group by validating and configuring a list of agents. It establishes group agent status for all provided agents, ensures specific handoff and guardrail agents are included, creates a `GroupToolExecutor`, wraps necessary agents, registers their functions with the executor using context variables, and returns the tool executor along with the wrapped agents.*


### wrap_agent_handoff_targets (function, L309-L337)

> *Summary: This function modifies an agent's handoff targets by wrapping specific targets—those based on LLM conditions and context conditions—into new wrapper agents. It returns `None` but populates the provided list with these newly created wrapper agents, redirecting the original handoffs to point to them.*


### process_initial_messages (function, L340-L388)

> *Summary: Validates and processes initial input messages, converting a string to a message dictionary if necessary. It determines the final speaker by checking for agent names within the first message against known agents or defaulting to a user proxy if no specific agent is identified. The function returns the processed messages, the last speaking agent, all group agent names, and any temporary user proxies created.*


### setup_context_variables (function, L391-L408)

> *Summary: Assigns a shared `ContextVariables` object to the tool executor, all group agents, the chat manager, and an optional user agent. This ensures all participants in the group conversation reference the same set of contextual data.*


### cleanup_temp_user_messages (function, L411-L419)

> *Summary: This function modifies a `ChatResult` object by iterating through its history and removing the `"name"` key if it is set to `"_User"` for any message. It performs an in-place cleanup of temporary user proxy identifiers before the result is returned.*


### get_last_agent_speaker (function, L422-L436)

> *Summary: Retrieves the most recent speaking agent from a chat history, excluding any tool executor messages. It iterates backward through the messages to find the latest participant whose name matches one of the provided agent names.*


### determine_next_agent (function, L439-L535)

> *Summary: Determines the next participant in a group conversation based on the last speaker, message content (e.g., tool calls), and predefined transition logic. It evaluates conditions like forced transitions, tool execution outcomes, user input handoffs, or group-level "after work" rules to return the appropriate next agent or selection method.*


### create_group_transition (function, L538-L575)

> *Summary: Generates a transition function for managing agent turns within a group chat. This function uses provided agents and configuration to determine the next speaker after each turn, ensuring the initial designated agent speaks first.*


### create_group_manager (function, L578-L623)

> *Summary: Constructs a `GroupChatManager` instance from a provided `GroupChat`, optional arguments, a list of participating agents, and a transition target. It validates that if any agent handoffs or the overall after-work mechanism uses a `GroupManagerTarget`, an LLM configuration must be supplied in the input arguments.*


### make_remove_function (function, L626-L673)

> *Summary: Generates a callable function that filters a list of messages by removing specific tool call and corresponding tool response entries. It takes a list of message dictionaries as input and returns a new list with the specified tool-related content purged.*

