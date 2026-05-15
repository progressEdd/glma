# autogen/agentchat/contrib/swarm_agent.py

23 function(s): _establish_swarm_agent, _link_agents_to_swarm_manager, _run_oncontextconditions, _modify_context_variables_param, _change_tool_context_variables_to_depends, _prepare_swarm_agents, _create_nested_chats, _process_initial_messages, _setup_context_variables, _cleanup_temp_user_messages and 13 more. 8 class(es): AfterWorkOption, AfterWork, AFTER_WORK, OnCondition, ON_CONDITION, OnContextCondition, SwarmResult, SwarmAgent. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AfterWorkOption | class |  |
| AfterWork | class |  |
| AFTER_WORK | class |  |
| OnCondition | class |  |
| ON_CONDITION | class |  |
| OnContextCondition | class |  |
| _establish_swarm_agent | function |  |
| _link_agents_to_swarm_manager | function |  |
| _run_oncontextconditions | function |  |
| _modify_context_variables_param | function |  |
| _change_tool_context_variables_to_depends | function |  |
| _prepare_swarm_agents | function |  |
| _create_nested_chats | function |  |
| _process_initial_messages | function |  |
| _setup_context_variables | function |  |
| _cleanup_temp_user_messages | function |  |
| _prepare_groupchat_auto_speaker | function |  |
| _determine_next_agent | function |  |
| create_swarm_transition | function |  |
| _create_swarm_manager | function |  |
| make_remove_function | function |  |
| initiate_swarm_chat | function |  |
| run_swarm | function |  |
| a_initiate_swarm_chat | function |  |
| a_run_swarm | function |  |
| SwarmResult | class |  |
| _set_to_tool_execution | function |  |
| register_hand_off | function |  |
| _update_conditional_functions | function |  |
| _generate_swarm_tool_reply | function |  |
| SwarmAgent | class |  |

## Chunks

### AfterWorkOption (class, L57-L61)

> *Summary: Defines an enumeration of possible actions to take after a task is completed. These options dictate the subsequent flow, such as terminating execution, returning control to the user, or continuing within the swarm manager context.*


### AfterWork (class, L66-L98)

> *Summary: This class manages the subsequent action in a conversation when no tool call or handoff is suggested by an agent. It accepts an `agent` (which can be an agent instance, name string, or callable) and an optional selection message for internal routing logic. The constructor validates inputs, converting string names to options and warning if the selection message is provided for non-swarm manager agents.*


### __post_init__ (method, L82-L98, parent: AfterWork)

> *Summary: This method validates and processes initial configuration after object instantiation. It ensures that if `agent` is a string, it's converted to an uppercase enum option, and it checks the type of `next_agent_selection_msg`, issuing a warning and discarding it if the agent isn't set as the swarm manager.*


### AFTER_WORK (class, L101-L110)

> *Summary: This class serves as a deprecated wrapper around `AfterWork`, issuing a warning upon instantiation to inform users that its swarm functionality has been merged into group chat. It inherits from `AfterWork` and immediately triggers a `DeprecationWarning`.*


### __init__ (method, L104-L110, parent: AFTER_WORK)

> *Summary: This constructor issues a `DeprecationWarning` because the `AFTER_WORK` parameter is obsolete, noting that swarm functionality has been moved to group chat. It then calls the parent class's initializer with all provided arguments.*


### OnCondition (class, L115-L160)

> *Summary: This class defines a transition rule for an agent system, specifying where to hand off execution and under what conditions. It accepts a `target` (agent or chat config), a `condition` evaluated by the LLM, and an optional `available` check based on context variables or a callable. The constructor validates that inputs conform to expected types for safe operation.*


### __post_init__ (method, L144-L160, parent: OnCondition)

> *Summary: Validates the initialized state of the agent by checking that `target` is either an agent or dictionary, ensuring `condition` is a non-empty string or valid type, and confirming `available` adheres to expected types. Raises `ValueError` if any input parameters do not meet these structural requirements.*


### ON_CONDITION (class, L163-L172)

> *Summary: This class acts as a deprecated wrapper around `OnCondition`, issuing a warning upon instantiation to inform users that it should be replaced by the standard `OnCondition` class. It inherits functionality from its parent while explicitly signaling its planned removal in future versions.*


### __init__ (method, L166-L172, parent: ON_CONDITION)

> *Summary: This constructor issues a `DeprecationWarning` if the `ON_CONDITION` argument is used, advising developers to switch to `OnCondition`. It then calls the parent class's initializer with all provided arguments.*


### OnContextCondition (class, L177-L226)

> *Summary: This class defines a rule for agent handoffs based on context variables, evaluating conditions without involving the LLM. It accepts a `target` (agent or nested chat config), a boolean-evaluable `condition`, and an optional `available` check to determine if the condition should even be considered.*


### __post_init__ (method, L206-L226, parent: OnContextCondition)

> *Summary: Validates the initialized state by ensuring `target` is an agent or dictionary, and that `condition` is either a non-empty string converted to a `ContextExpression` or already a `ContextExpression`. It also verifies that `available`, if present, conforms to being a callable, string, or `ContextExpression`.*


### _establish_swarm_agent (function, L229-L262)

> *Summary: Configures an existing conversational agent to function as part of a swarm by injecting specific attributes and registering hooks. It sets up internal state tracking for nested chats, conditional logic evaluation, and overrides the string representation for better logging during transitions.*


### _link_agents_to_swarm_manager (function, L265-L274)

> *Summary: Assigns a reference to the `group_chat_manager` to every provided `Agent` instance. This allows agents to programmatically control the flow of execution within the swarm system via the tool executor.*


### _run_oncontextconditions (function, L277-L311)

> *Summary: Checks a list of predefined context conditions against an agent's state and variables. If any condition is met, it sets the next target agent for tool execution and returns `True` along with a handover message; otherwise, it returns `False`.*


### _modify_context_variables_param (function, L314-L341)

> *Summary: This utility wraps a function to inject dependency management into its `context_variables` parameter. It modifies the function's signature by replacing the original annotation with one that uses `Annotated` and `Depends`, linking it to provided swarm context variables.*


### _change_tool_context_variables_to_depends (function, L344-L364)

> *Summary: This function modifies a registered tool by replacing it if its schema includes a `context_variables` parameter. It removes the old tool from the agent, reconstructs it using dependency injection for parameters, and then re-registers the modified version with the agent.*


### _prepare_swarm_agents (function, L367-L442)

> *Summary: Validates and configures a set of agents for swarm operation by establishing agent roles, creating a central tool executor, and setting up nested chat structures. It returns the specialized tool execution agent and a list of all involved nested chat agents after injecting context variables and aggregating tools.*


### _create_nested_chats (function, L445-L502)

> *Summary: This function constructs and registers specialized sub-agents for handling nested conversations based on predefined handoff configurations. It iterates through various internal agent structures to create these nested agents, registering them both as potential targets for incoming transfers and as handlers that report back to the parent agent upon completion.*


### _process_initial_messages (function, L505-L551)

> *Summary: Validates and processes initial input messages, converting a string to a message list if necessary. It determines the starting agent by checking for explicit names in the first message or defaulting to a provided/created user proxy, returning the processed messages along with the identified last speaker and lists of relevant agents.*


### _setup_context_variables (function, L554-L569)

> *Summary: Assigns a shared `ContextVariables` object to every participating agent, the tool executor, and the group chat manager within the swarm setup. This ensures all components operate with the same contextual state during interaction.*


### _cleanup_temp_user_messages (function, L572-L580)

> *Summary: This function modifies a `ChatResult` by iterating through its history and removing the temporary agent name `_User` from any messages that contain it. It performs an in-place cleanup of the chat log before the result is returned.*


### _prepare_groupchat_auto_speaker (function, L583-L637)

> *Summary: Modifies a `GroupChat` instance to prepare for auto speaker selection by setting its prompt template. It filters the available agents list to exclude tool executors and nested chats before applying the provided message—which can be a string, context-aware object, or callable function—to define how the next agent is chosen.*


### _determine_next_agent (function, L640-L742)

> *Summary: Determines the subsequent agent in a group conversation based on various conditions like tool execution results, user input, and predefined continuation logic. It processes inputs such as the last speaker, chat history, and configuration options to output the next `Agent` instance, `"auto"`, or `None`.*


### create_swarm_transition (function, L745-L782)

> *Summary: Generates a transition function for managing agent flow within a swarm chat. It takes initial agents, tool executors, and configuration options as input to return a callable that determines the next speaker based on the current state of the group chat.*


### _create_swarm_manager (function, L785-L815)

> *Summary: Constructs a `GroupChatManager` instance using a provided group chat, optional configuration arguments, and a list of agents. It validates that if any agent requires the Swarm Manager via an after-work option, the resulting manager must possess an LLM configuration.*


### make_remove_function (function, L818-L865)

> *Summary: Generates a callable function that filters a list of messages by removing specific tool call and corresponding tool response entries. It takes a list of message dictionaries as input and returns a new list with the specified tool-related content purged.*


### initiate_swarm_chat (function, L869-L976)

> *Summary: This deprecated function initializes and runs a multi-agent "swarm" conversation by setting up a `GroupChat` with specialized transition logic. It accepts initial agents, messages, and configuration parameters to manage the chat flow, ultimately returning the chat history, updated context variables, and the final speaking agent.*


### run_swarm (function, L980-L1041)

> *Summary: Executes a deprecated swarm chat simulation by initiating a multi-agent conversation using provided agents and initial messages. It streams the execution progress to an output stream and returns a `RunResponseProtocol` object that manages the asynchronous result.*


### a_initiate_swarm_chat (function, L1045-L1139)

> *Summary: This function orchestrates an asynchronous swarm conversation by setting up a `GroupChat` with multiple agents and a custom speaker selection method. It takes initial messages and a list of agents as input, managing context variables and defining how the chat proceeds after an agent fails to select the next participant. The output includes the final chat history, updated context variables, and the last speaking agent.*


### a_run_swarm (function, L1143-L1192)

> *Summary: Executes a multi-agent swarm chat simulation, taking an initial agent, messages, and a list of agents as input. It streams the execution results, including history, summary, cost, and final context variables, returning a response object that manages this asynchronous process.*


### SwarmResult (class, L1196-L1217)

> *Summary: This data structure holds the results from a swarm agent execution, containing output values, an associated agent or status indicator, and optional context variables. It automatically initializes context variables if none are provided upon instantiation and serializes agents to their names when converted to JSON.*


### serialize_agent (method, L1204-L1207, parent: SwarmResult)

> *Summary: If the input is an agent object, it returns the agent's name as a string; otherwise, it returns the provided input directly. This method serializes an agent or its identifier into a string representation.*


### model_post_init (method, L1209-L1212, parent: SwarmResult)

> *Summary: Ensures the agent has an initialized `ContextVariables` instance by creating one if it wasn't supplied during setup. This method runs after model initialization to guarantee context availability for subsequent operations.*


### __str__ (method, L1216-L1217, parent: SwarmResult)

> *Summary: Returns a string representation of the agent's current state by returning its internal `values` attribute. This method is used for human-readable output of the agent object.*


### _set_to_tool_execution (function, L1220-L1228)

> *Summary: Configures an agent to handle tool execution requests from other swarm agents by clearing its reply functions and registering a specific handler for incoming messages. This internal setup allows the agent to process external tool calls and update relevant context variables.*


### register_hand_off (function, L1232-L1304)

> *Summary: Registers a mechanism for an agent to transfer control to another based on specific conditions or after completing work. It accepts a list containing `OnCondition`, `OnContextCondition`, or `AfterWork` objects, which are then processed to set up internal state and callable functions within the agent.*


### _update_conditional_functions (function, L1307-L1334)

> *Summary: This routine dynamically manages an agent's available tools by checking predefined conditions for each function. It iterates through registered conditional functions, evaluates their availability based on the agent's state or context variables, and updates the agent's tool signature accordingly.*


### _generate_swarm_tool_reply (function, L1337-L1408)

> *Summary: This function processes and generates replies for agent tool calls by iterating over each requested tool. It enriches the tool call arguments with context variables, executes the tools via the agent, updates global state based on responses (like `context_variables` and `next_agent`), and returns a boolean success flag along with the finalized tool reply message.*


### SwarmAgent (class, L1411-L1427)

> *Summary: This class acts as a deprecated wrapper around `ConversableAgent`, issuing a warning upon instantiation to guide users toward the modern replacement. It inherits all functionality from its parent agent while signaling its impending removal in future versions.*


### __init__ (method, L1414-L1427, parent: SwarmAgent)

> *Summary: This constructor immediately issues a `DeprecationWarning`, advising users to switch to `ConversableAgent`. It then calls the parent class's initializer with all provided arguments.*

