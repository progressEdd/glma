# test/agentchat/contrib/test_swarm.py

39 function(s): invalid_agent, test_swarm_result, test_swarm_result_serialization, test_after_work_initialization, test_on_condition, test_receiving_agent, test_resume_speaker, test_after_work_options, test_on_condition_handoff, test_temporary_user_proxy and 29 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| invalid_agent | function |  |
| test_swarm_result | function |  |
| test_swarm_result_serialization | function |  |
| test_after_work_initialization | function |  |
| test_on_condition | function |  |
| test_receiving_agent | function |  |
| test_resume_speaker | function |  |
| test_after_work_options | function |  |
| test_on_condition_handoff | function |  |
| test_temporary_user_proxy | function |  |
| test_context_variables_updating_multi_tools | function |  |
| test_context_variables_updating_multi_tools_including_pydantic_object | function |  |
| test_function_transfer | function |  |
| test_invalid_parameters | function |  |
| test_non_swarm_in_hand_off | function |  |
| test_initialization | function |  |
| test_update_system_message | function |  |
| test_string_agent_params_for_transfer | function |  |
| test_after_work_callable | function |  |
| test_on_condition_unique_function_names | function |  |
| test_prepare_swarm_agents | function |  |
| test_create_nested_chats | function |  |
| test_process_initial_messages | function |  |
| test_setup_context_variables | function |  |
| test_cleanup_temp_user_messages | function |  |
| test_a_initiate_swarm_chat | function |  |
| test_swarmresult_afterworkoption | function |  |
| test_update_on_condition_str | function |  |
| test_agent_tool_registration_for_execution | function |  |
| test_compress_message_func | function |  |
| test_swarmresult_afterworkoption_tool_swarmresult | function |  |
| test_on_condition_available | function |  |
| test_on_context_condition | function |  |
| test_register_hand_off_on_context_condition | function |  |
| test_on_context_condition_run | function |  |
| test_on_context_condition_available | function |  |
| test_change_tool_context_variables_to_depends | function |  |
| test_change_tool_context_variables_dependency_injection | function |  |
| test_change_tool_context_variables_function_signature | function |  |

## Chunks

### invalid_agent (function, L50-L56)

> *Summary: Creates and returns a simple `Agent` instance using a custom dataclass. It accepts an optional string name to initialize the agent with.*


### test_swarm_result (function, L59-L80)

> *Summary: Verifies the `SwarmResult` class by testing its initialization with various inputs: a simple string value, context variables, an agent object, or a termination option. It confirms that the resulting object correctly stores these inputs and produces the expected string representation when converted to a string.*


### test_swarm_result_serialization (function, L83-L105)

> *Summary: This test verifies that a `SwarmResult` object can be correctly serialized to JSON, ensuring that agent names and context variables are preserved. It checks serialization behavior both when the agent is an instantiated object and when it's provided as a string identifier.*


### test_after_work_initialization (function, L108-L132)

> *Summary: Verifies the `AfterWork` constructor handles various input types—an enum, a string, an agent instance, or a callable—by correctly setting the internal `agent` attribute. It also confirms that providing an invalid option raises a `ValueError`.*


### test_on_condition (function, L135-L141)

> *Summary: Verifies that initializing `OnCondition` with an invalid agent object raises a `ValueError`. This test confirms the constructor enforces that the provided target must be a valid `ConversableAgent` or dictionary.*


### test_receiving_agent (function, L144-L190)

> *Summary: This test verifies the behavior of a receiving agent within a swarm chat simulation by testing three scenarios: starting with no named initial message, starting with a named initial message from another agent, and starting with a user-provided agent. It asserts that the correct agents take turns speaking based on the input messages and configuration.*


### test_resume_speaker (function, L193-L229)

> *Summary: This test verifies that when resuming a multi-message conversation, the last speaker in the history initiates the chat process. It mocks agent initiation to confirm that only the designated final agent starts the `initiate_swarm_chat` flow.*


### test_after_work_options (function, L232-L301)

> *Summary: This test verifies the behavior of different post-work options within a multi-agent swarm simulation. It initializes agents and mocks LLM responses, then tests how `TERMINATE`, `REVERT_TO_USER`, `STAY`, and custom callable functions dictate which agent speaks next after an initial agent completes its task during chat initiation.*


### test_on_condition_handoff (function, L305-L350)

> *Summary: This test verifies the `OnCondition` handoff mechanism between two agents in a swarm simulation. It sets up mock LLM responses to force Agent 1 to trigger a transfer to Agent 2, asserting that the chat history correctly reflects this transition after execution.*


### test_temporary_user_proxy (function, L353-L366)

> *Summary: This test verifies that a temporary user proxy agent name is correctly cleared during swarm chat execution. It initiates a multi-agent conversation and asserts that none of the resulting messages contain the special `"_User"` name in their metadata.*


### test_context_variables_updating_multi_tools (function, L370-L430)

> *Summary: This test verifies that shared `ContextVariables` are correctly updated across multiple tool executions within a multi-agent swarm simulation. It initializes a counter, executes two functions that modify this counter by different amounts (1 and 100), and asserts the final state reflects the cumulative change (101).*


### test_context_variables_updating_multi_tools_including_pydantic_object (function, L434-L497)

> *Summary: This test verifies that context variables, specifically a Pydantic object, are correctly updated across multiple tool calls within a multi-agent swarm simulation. It initializes a context variable with an initial value and then executes two functions that modify this variable; the assertion confirms the final state reflects the cumulative changes from both function executions.*


### test_function_transfer (function, L501-L553)

> *Summary: This test verifies that a function call initiated by one agent correctly transfers execution to another agent within the swarm environment. It sets up two agents, mocks their LLM responses to trigger a function call from `agent2` to `agent1`, and asserts that the context variables are updated and the conversation history reflects the transfer.*


### test_invalid_parameters (function, L556-L571)

> *Summary: This test verifies that `initiate_swarm_chat` correctly raises a `ValueError` when provided with incorrect inputs. It specifically checks for failures related to non-`ConversableAgent` types for the initial agent, invalid contents in the agents list, and an unrecognized value for the `after_work` parameter.*


### test_non_swarm_in_hand_off (function, L574-L588)

> *Summary: Verifies that the `register_hand_off` function strictly enforces valid agent types for hand-off targets. It asserts that passing non-callable or incorrect data types (like integers instead of condition objects) raises specific `ValueError` exceptions.*


### test_initialization (function, L591-L629)

> *Summary: This test verifies the input validation of `initiate_swarm_chat` by asserting that it raises `ValueError` when provided with invalid agents in the agent list or as the initial agent. It also confirms a specific error is raised if an agent specified in a hand-off mechanism is not present in the main agent list.*


### test_update_system_message (function, L632-L715)

> *Summary: This test verifies the `update_agent_state_before_reply` mechanism by simulating chat interactions with agents configured to generate system messages using either a custom callable or a string template. It confirms that when multiple update functions are provided, only the last one executed dictates the final captured system message content.*


### test_string_agent_params_for_transfer (function, L719-L818)

> *Summary: This test verifies that string-based agent parameters are handled correctly during a simulated swarm chat execution without invoking actual LLMs. It sets up two agents with mocked responses to test successful interaction and then asserts failure when an agent references a non-existent name in its output.*


### test_after_work_callable (function, L822-L898)

> *Summary: This test verifies the functionality of agent handoffs within a swarm chat simulation by registering specific callback functions for each agent. It initiates a multi-agent conversation, asserting that agents transition sequentially based on their registered `AfterWork` handlers and ultimately terminates correctly.*


### test_on_condition_unique_function_names (function, L902-L957)

> *Summary: This test verifies that when multiple `OnCondition` handoffs are registered from one agent to another, the generated function names used for transitions remain unique across all conditions. It simulates a multi-agent chat session and asserts that three distinct transition functions were created with sequentially numbered names.*


### test_prepare_swarm_agents (function, L961-L1012)

> *Summary: This test function verifies the setup of swarm agents by initializing multiple `ConversableAgent` instances with a specific LLM configuration and attaching custom functions. It then calls an internal preparation utility to ensure the resulting tool executor correctly aggregates all registered functions and validates various error conditions for invalid agent inputs or missing handoff targets.*


### test_create_nested_chats (function, L1016-L1060)

> *Summary: This test verifies the functionality for creating and registering nested chat agents by setting up two conversational agents and defining a handoff queue. It asserts that the resulting nested agent is correctly created, named, and configured to hand control back to the originating agent upon completion of its task.*


### test_process_initial_messages (function, L1063-L1104)

> *Summary: This test verifies the `_process_initial_messages` utility by simulating various initial message inputs to a group of agents. It asserts correct message parsing, identification of the last acting agent, and whether temporary users are created based on the provided message structure and existing user context.*


### test_setup_context_variables (function, L1107-L1125)

> *Summary: This test verifies that a shared `ContextVariables` object is correctly propagated to all participating agents and the group chat manager when setting up an agent swarm environment. It asserts that every component—including the tool executor, individual agents, and the manager—references the exact same context instance.*


### test_cleanup_temp_user_messages (function, L1128-L1142)

> *Summary: This test verifies that a helper function correctly removes the `name` attribute from user messages within a provided chat history structure. It asserts that after processing, all entries with the `"role"` of `"user"` no longer contain a `"name"` key.*


### test_a_initiate_swarm_chat (function, L1146-L1185)

> *Summary: This asynchronous test verifies the functionality of initiating a swarm chat by testing three scenarios: starting with a string message, starting with a list of messages, and providing initial context variables. It asserts that the resulting chat history is populated correctly and that context variables are successfully passed through the execution flow.*


### test_swarmresult_afterworkoption (function, L1188-L1235)

> *Summary: This test verifies how agent sequencing is determined within a swarm context based on provided `AfterWorkOption` states. It calls a helper function with various combinations of input options to assert specific outcomes, such as termination, returning to the last speaker, reverting to the user, or defaulting to automatic selection.*


### test_update_on_condition_str (function, L1239-L1330)

> *Summary: This test verifies that handoff conditions defined using string templates correctly substitute variables from the chat context. It simulates multi-agent conversations, asserting that the captured condition description matches the expected template with substituted values for both string and callable function scenarios.*


### test_agent_tool_registration_for_execution (function, L1334-L1354)

> *Summary: Verifies that tools registered on an agent are correctly exposed to the internal tool executor during swarm setup. It takes a mock credentials object as input and asserts that the specified tool name exists within the execution agent's function map after preparation.*


### test_compress_message_func (function, L1357-L1403)

> *Summary: Tests the `make_remove_function` utility by applying it to a list of chat messages. It removes specific function calls from the input messages and asserts that the resulting list has the expected length and retains certain data integrity after modification.*


### test_swarmresult_afterworkoption_tool_swarmresult (function, L1406-L1479)

> *Summary: This test suite verifies how agent selection is determined after a tool execution result within a swarm context. It calls a helper function that simulates group chat interaction with various `AfterWorkOption` inputs to assert the correct next agent or selection mode is returned.*


### test_on_condition_available (function, L1483-L1582)

> *Summary: This test verifies the functionality of `OnCondition` hand-offs by simulating various scenarios for its `available` parameter. It checks how the system behaves when the condition is evaluated with no availability, a true context variable, a false context variable, a negated context variable using `ContextExpression`, and a custom callable function.*


### test_on_context_condition (function, L1585-L1617)

> *Summary: Verifies the initialization and validation logic for `OnContextCondition` by testing valid setups with string or `ContextExpression` inputs. It asserts correct behavior against invalid inputs such as non-agent targets, incorrect condition types, empty strings, or improper parameter values.*


### test_register_hand_off_on_context_condition (function, L1620-L1634)

> *Summary: This test verifies that registering an `OnContextCondition` correctly adds the specified handoff to an agent's internal list. It takes two agents and a context expression as input, asserting that the condition is successfully registered on the source agent.*


### test_on_context_condition_run (function, L1637-L1694)

> *Summary: This test verifies the `_run_oncontextconditions` logic by simulating agent interactions within a group chat setup. It confirms that when an agent's context variables meet a defined condition, the function correctly triggers a handoff to a specified target agent or nested chat configuration.*


### test_on_context_condition_available (function, L1698-L1777)

> *Summary: This test verifies the functionality of `OnContextCondition` by simulating various ways to define its availability. It inputs different configurations—including simple boolean checks, string-based context lookups, complex expressions, and custom callable functions—to determine if a condition should be met when running agent interactions. The output asserts that the expected boolean result is returned based on the provided context data or function execution.*


### test_change_tool_context_variables_to_depends (function, L1781-L1858)

> *Summary: This test verifies that a utility function correctly refactors tools from using explicit `context_variables` parameters to utilizing dependency injection. It tests this transformation on both a tool possessing and one lacking the context variable parameter, ensuring the agent's registered tools remain consistent after modification.*


### test_change_tool_context_variables_dependency_injection (function, L1862-L1922)

> *Summary: This test verifies that a tool correctly utilizes dependency injection for its `context_variables` parameter after modification. It sets up an agent with specific context variables, creates a function-based tool, modifies the tool to depend on the context, and then asserts that calling the modified tool without explicitly passing context yields the same result as calling it with them.*


### test_change_tool_context_variables_function_signature (function, L1926-L2007)

> *Summary: This test verifies that a specific utility function correctly updates the signature of a registered tool when dependency injection is applied to its context variables. It inputs an agent and a tool with a `ContextVariables` parameter, then asserts that the resulting tool's function signature has been modified as expected by the transformation logic.*

