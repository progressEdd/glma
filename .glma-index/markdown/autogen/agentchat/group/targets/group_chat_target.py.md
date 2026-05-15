# autogen/agentchat/group/targets/group_chat_target.py

2 class(es): GroupChatConfig, GroupChatTarget. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GroupChatConfig | class |  |
| GroupChatTarget | class |  |

## Chunks

### GroupChatConfig (class, L25-L33)

> *Summary: Defines the configuration structure for a group chat transition target. It requires a `pattern` and either a list of message dictionaries or a single string for messages, while optionally setting a maximum number of rounds to 20.*


### GroupChatTarget (class, L37-L133)

> *Summary: This class defines a target representing a group chat that requires wrapping within an agent. It provides methods to identify and configure the target, crucially implementing `create_wrapper_agent` which instantiates a specialized agent capable of running the nested group chat via a registered reply function. This wrapper agent then automatically hands off control back to its parent upon completion.*


### can_resolve_for_speaker_selection (method, L42-L44, parent: GroupChatTarget)

> *Summary: This method checks if the current group chat target is suitable for speaker selection; it always returns `False` because, for this specific target type, the chat must first be wrapped within an agent.*


### resolve (method, L46-L55, parent: GroupChatTarget)

> *Summary: This method is intentionally unimplemented, raising an error because it expects a nested chat configuration that requires encapsulating the group chat within another agent for proper targeting. It accepts a `GroupChat`, a `current_agent`, and an optional `user_agent` as input but returns nothing due to the exception.*


### display_name (method, L57-L59, parent: GroupChatTarget)

> *Summary: Returns a static string, `"a group chat"`, representing the human-readable identifier for this group chat target.*


### normalized_name (method, L61-L63, parent: GroupChatTarget)

> *Summary: Returns a standardized string identifier, `"group_chat"`, which is used internally by the system for function calling purposes. This method takes no input and always produces the same output.*


### __str__ (method, L65-L67, parent: GroupChatTarget)

> *Summary: Provides a string representation that describes the target's action. When called, it consistently returns the fixed string "Transfer to group chat".*


### needs_agent_wrapper (method, L69-L71, parent: GroupChatTarget)

> *Summary: This method always returns `True`, indicating that any instance of this target requires wrapping within an agent for proper operation. It serves as a mandatory check to enforce agent encapsulation for group chat targets.*


### create_wrapper_agent (method, L73-L133, parent: GroupChatTarget)

> *Summary: This method constructs a specialized `ConversableAgent` that acts as a wrapper for initiating and managing an internal group chat session. It configures the agent to execute the group chat logic via a registered reply function, which takes input from the parent conversation and returns the resulting summary back into the main flow.*

