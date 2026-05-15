# autogen/agentchat/group/group_tool_executor.py

1 class(es): GroupToolExecutor. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GroupToolExecutor | class |  |

## Chunks

### GroupToolExecutor (class, L28-L449)

> *Summary: This class manages the execution of tools within a group chat context. It receives messages containing tool calls, executes them (synchronously or asynchronously), processes the results to update context variables and determine the next agent transition, and returns the structured reply message. Key behaviors include normalizing tool content and handling handoffs based on the tool's return type.*


### __init__ (method, L31-L51, parent: GroupToolExecutor)

> *Summary: Initializes an agent designed to execute tools within a group context by setting up specific system instructions and internal state tracking for tool call origins and next targets. It registers both synchronous and asynchronous reply handlers to process incoming tool results and determine the subsequent conversational flow.*


### set_next_target (method, L53-L55, parent: GroupToolExecutor)

> *Summary: Updates an internal state variable to specify the subsequent agent or entity for group interaction. This method accepts a `TransitionTarget` object as input and modifies the instance's target pointer.*


### get_next_target (method, L57-L64, parent: GroupToolExecutor)

> *Summary: Retrieves the predetermined `TransitionTarget` from an internal state variable, raising a `ValueError` if no target has been explicitly set beforehand.*


### has_next_target (method, L66-L68, parent: GroupToolExecutor)

> *Summary: Determines if the group execution flow has another designated target by checking the internal `_group_next_target` attribute. Returns `True` if a subsequent target exists, otherwise returns `False`.*


### clear_next_target (method, L70-L72, parent: GroupToolExecutor)

> *Summary: Resets the internal state by setting the `_group_next_target` attribute to `None`, effectively clearing any planned subsequent action or destination for the group.*


### set_tool_call_originator (method, L74-L76, parent: GroupToolExecutor)

> *Summary: This method stores the name of an initiating agent within the object's state. It accepts a string representing the agent's name and updates the internal `_tool_call_originator` attribute for transparency purposes.*


### get_tool_call_originator (method, L78-L80, parent: GroupToolExecutor)

> *Summary: Retrieves the identifier of the agent responsible for initiating a specific tool call. It returns this originator's ID as a string or `None` if no initiator is recorded.*


### clear_tool_call_originator (method, L82-L84, parent: GroupToolExecutor)

> *Summary: Resets an internal attribute to `None`, effectively removing any record of which agent initiated a tool call. This method performs no external operations and simply modifies the object's state.*


### _modify_context_variables_param (method, L86-L128, parent: GroupToolExecutor)

> *Summary: This method wraps a given callable to inject dependency injection into its `context_variables` parameter. It inspects the function's signature and replaces the original annotation with one that uses `Annotated` and `Depends(on(...))` pointing to the provided group context variables, returning the modified wrapper function.*


### make_tool_copy_with_context_variables (method, L130-L147, parent: GroupToolExecutor)

> *Summary: This method checks if a given tool accepts `context_variables` and, if so, regenerates the tool by removing that parameter and injecting dependencies into its underlying function. It returns the newly created tool instance or `None` if no modification was necessary.*


### _change_tool_context_variables_to_depends (method, L149-L155, parent: GroupToolExecutor)

> *Summary: This method modifies a tool's context variables by replacing them with dependency injection references if the tool supports it. It achieves this by creating a copy of the tool, registering the new version with the agent, and removing the original one.*


### register_agents_functions (method, L157-L169, parent: GroupToolExecutor)

> *Summary: This method integrates functions and tools from a list of agents into the group tool executor. It merges agent function maps and updates any agent tools requiring context variables to use dependency injection before registering all agent tools for execution.*


### function_is_agent_llm_handoff (method, L171-L187, parent: GroupToolExecutor)

> *Summary: Checks if a specified function name matches any of the LLM handoff conditions configured for a given agent within the group chat. It returns `True` if the agent exists, is a `ConversableAgent`, and has an associated condition matching the input function name.*


### get_sender_agent_for_message (method, L189-L201, parent: GroupToolExecutor)

> *Summary: Retrieves the originating agent from a message dictionary by looking up the sender's name within the group manager. It returns the corresponding `Agent` object if the message contains a "name" and the group manager is available, otherwise it returns `None`.*


### is_handoff_function (method, L203-L218, parent: GroupToolExecutor)

> *Summary: Determines if a message contains a tool call that represents an agent handoff by checking the message structure and invoking a helper method against the specified agent and function name. It returns `True` if any tool call matches a predefined LLM handoff pattern, otherwise it returns `False`.*


### _send_llm_handoff_event (method, L220-L236, parent: GroupToolExecutor)

> *Summary: When a message indicates an LLM handoff condition, this method extracts the sending agent and publishes an `OnConditionLLMTransitionEvent` to the default I/O stream. This event signals a transition from the source agent to a specified target state.*


### _send_reply_result_handoff_event (method, L238-L253, parent: GroupToolExecutor)

> *Summary: This method broadcasts a `ReplyResultTransitionEvent` to the default I/O stream after identifying the message's sender agent. It uses the provided message and target transition to signal the completion of a tool execution result handoff.*


### _normalize_tool_content (method, L255-L287, parent: GroupToolExecutor)

> *Summary: Converts various input types into a standardized string representation suitable for tool output. It specifically handles OpenAI message formats by serializing them differently than general Python objects, which are otherwise serialized using JSON or converted via `str()`.*


### _generate_group_tool_reply (method, L289-L375, parent: GroupToolExecutor)

> *Summary: This method processes and generates replies for group tool calls by iterating over each requested function call. It enriches the tool arguments with context variables, invokes the agent to generate a reply based on the tool execution, and then updates internal state (context variables and next target) using the received tool responses before returning the final structured reply message.*


### _a_generate_group_tool_reply (method, L377-L449, parent: GroupToolExecutor)

> *Summary: This asynchronous method processes messages containing tool calls by executing each requested function using the agent's event loop. It aggregates the results from these executions, updates context variables if present, and determines the next conversational target before returning a success status and the modified message containing all tool responses.*

