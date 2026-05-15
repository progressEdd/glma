# autogen/agentchat/group/targets/group_manager_target.py

1 function(s): prepare_groupchat_auto_speaker. 4 class(es): GroupManagerSelectionMessage, GroupManagerSelectionMessageString, GroupManagerSelectionMessageContextStr, GroupManagerTarget. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| prepare_groupchat_auto_speaker | function |  |
| GroupManagerSelectionMessage | class |  |
| GroupManagerSelectionMessageString | class |  |
| GroupManagerSelectionMessageContextStr | class |  |
| GroupManagerTarget | class |  |

## Chunks

### prepare_groupchat_auto_speaker (function, L24-L58)

> *Summary: This function configures a `GroupChat` instance for automatic speaker selection by updating its prompt template. It filters the available agents to exclude tool executors and wrapped agents before setting the final speaker selection prompt based on an optional manager selection message.*


### GroupManagerSelectionMessage (class, L63-L68)

> *Summary: This abstract base model defines a contract for messages used to select group managers. Subclasses must implement `get_message` to return a formatted string based on an input agent.*


### get_message (method, L66-L68, parent: GroupManagerSelectionMessage)

> *Summary: This method requires subclasses to provide a concrete implementation for retrieving and formatting a message from a given `ConversableAgent`. It currently raises an error if not overridden.*


### GroupManagerSelectionMessageString (class, L72-L79)

> *Summary: This class wraps a simple string to represent a selection message for group management. It takes a `str` input and returns that exact string when queried by an agent.*


### get_message (method, L77-L79, parent: GroupManagerSelectionMessageString)

> *Summary: Retrieves the stored message content from the instance's state. It takes one `ConversableAgent` as input and returns the message as a string.*


### GroupManagerSelectionMessageContextStr (class, L83-L109)

> *Summary: This class wraps a message template string, initially replacing `{agentlist}` with `<<agent_list>>` upon initialization. It then formats this template using an agent's context variables and restores the original `{agentlist}` placeholder before returning the final formatted string.*


### _replace_agentlist_placeholder (method, L91-L98, parent: GroupManagerSelectionMessageContextStr)

> *Summary: This method substitutes the string placeholder `{agentlist}` with `<<agent_list>>` if it exists within an input string. It returns the modified string or the original value if no substitution is necessary.*


### get_message (method, L100-L109, parent: GroupManagerSelectionMessageContextStr)

> *Summary: Retrieves a formatted message string by substituting context variables from an input `ConversableAgent` into a predefined template. It returns the resulting string, replacing a specific placeholder (`<<agent_list>>`) for later processing.*


### GroupManagerTarget (class, L112-L151)

> *Summary: This class acts as a target representing the group manager, allowing it to resolve speaker selection automatically within a group chat. It uses a predefined `selection_message` to prepare the group chat for automatic speaking and returns a result indicating "auto" selection.*


### can_resolve_for_speaker_selection (method, L117-L119, parent: GroupManagerTarget)

> *Summary: This method always returns `True`, indicating that the current target is capable of being resolved when selecting a speaker in a group chat context.*


### resolve (method, L121-L131, parent: GroupManagerTarget)

> *Summary: If a predefined selection message exists, it configures the group chat to use that speaker automatically. Otherwise, it defaults to an automatic speaker selection method for the group conversation.*


### display_name (method, L133-L135, parent: GroupManagerTarget)

> *Summary: Returns a fixed string, `"the group manager"`, representing the human-readable identifier for this agent's role. This method takes no inputs and outputs a `str`.*


### normalized_name (method, L137-L139, parent: GroupManagerTarget)

> *Summary: Returns a space-free version of the target's display name, intended for use in function calling contexts. This method relies on an existing `display_name()` method to generate its output string.*


### __str__ (method, L141-L143, parent: GroupManagerTarget)

> *Summary: Provides a standardized string representation for an agent target, which is used when displaying it as a function call message. This method always returns the fixed string "Transfer to the group manager".*


### needs_agent_wrapper (method, L145-L147, parent: GroupManagerTarget)

> *Summary: Determines whether a specific target requires wrapping within an agent structure. It currently always returns `False`, indicating no wrapper is needed by default.*


### create_wrapper_agent (method, L149-L151, parent: GroupManagerTarget)

> *Summary: This method is intended to create a wrapper around a parent agent, but it explicitly raises `NotImplementedError` because the group manager target does not necessitate such wrapping. It accepts a `ConversableAgent` and an integer index as input.*

