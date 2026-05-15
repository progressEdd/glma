# autogen/agentchat/group/targets/transition_target.py

9 class(es): TransitionTarget, AgentTarget, AgentNameTarget, NestedChatTarget, TerminateTarget, StayTarget, RevertToUserTarget, AskUserTarget, RandomAgentTarget. 66 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TransitionTarget | class |  |
| AgentTarget | class |  |
| AgentNameTarget | class |  |
| NestedChatTarget | class |  |
| TerminateTarget | class |  |
| StayTarget | class |  |
| RevertToUserTarget | class |  |
| AskUserTarget | class |  |
| RandomAgentTarget | class |  |

## Chunks

### TransitionTarget (class, L39-L80)

> *Summary: Provides a base interface for defining various transition targets within group chats, requiring subclasses to implement methods for resolution, naming, and agent wrapping. It allows the target to be activated in the `GroupChat` by setting itself as the next target for the `GroupToolExecutor`.*


### can_resolve_for_speaker_selection (method, L42-L44, parent: TransitionTarget)

> *Summary: This method checks if the current target is suitable for being selected as a speaker option. It always returns `False`, specifically to prevent resolution within nested chat contexts where encapsulation by an agent is expected.*


### resolve (method, L46-L53, parent: TransitionTarget)

> *Summary: This method is an abstract hook requiring subclasses to define how to determine the next speaker in a group chat. It accepts the `GroupChat`, the `current_agent`, and an optional `user_agent` as input, returning a `SpeakerSelectionResult`.*


### display_name (method, L55-L57, parent: TransitionTarget)

> *Summary: This method is an abstract interface requiring derived classes to provide a string representation of their specific target. It enforces that any subclass must override this function to return its unique display name.*


### normalized_name (method, L59-L61, parent: TransitionTarget)

> *Summary: This method is intended to return a space-free, standardized string representation of the target, which is necessary for function calling mechanisms. It currently raises an error, requiring concrete subclasses to provide their specific implementation.*


### needs_agent_wrapper (method, L63-L65, parent: TransitionTarget)

> *Summary: This method checks whether a specific target requires wrapping within an agent structure. It is abstract and mandates that any inheriting class must provide its own implementation for this check.*


### create_wrapper_agent (method, L67-L69, parent: TransitionTarget)

> *Summary: This method is intended to construct a specialized wrapper around a given `parent_agent` based on an provided index. It currently raises a `NotImplementedError`, requiring derived classes to define its specific implementation logic.*


### activate_target (method, L71-L80, parent: TransitionTarget)

> *Summary: This method sets itself as the next target for the `GroupToolExecutor` within a given group chat. It iterates through all agents to find and update the specific executor agent's target reference.*


### AgentTarget (class, L83-L123)

> *Summary: Represents a direct reference to another agent within a group chat. It takes an agent object during initialization and resolves to that agent's name when queried, providing methods for display and normalized naming.*


### __init__ (method, L88-L90, parent: AgentTarget)

> *Summary: Initializes a transition target by storing the name of an associated `ConversableAgent` and accepting arbitrary additional configuration data. This allows the target to be serialized while retaining context about the originating agent.*


### can_resolve_for_speaker_selection (method, L92-L94, parent: AgentTarget)

> *Summary: This method unconditionally returns `True`, indicating that the current target is always resolvable when determining which agent should speak. It takes no inputs and outputs a boolean value.*


### resolve (method, L96-L103, parent: AgentTarget)

> *Summary: This method determines the concrete agent instance within a `GroupChat` based on its configured name. It takes the chat, current, and user agents as input and returns a `SpeakerSelectionResult` containing the resolved agent's name.*


### display_name (method, L105-L107, parent: AgentTarget)

> *Summary: Returns a string representing the agent's name, which serves as its human-readable identifier within the group chat context.*


### normalized_name (method, L109-L111, parent: AgentTarget)

> *Summary: Returns a space-free version of the target's display name, intended for use in function calling contexts. This method relies on an existing `display_name()` method to generate its output string.*


### __str__ (method, L113-L115, parent: AgentTarget)

> *Summary: Provides a string representation of the target agent by formatting it as a transfer instruction, such as "Transfer to [agent\_name]". This is used when displaying the target within messages.*


### needs_agent_wrapper (method, L117-L119, parent: AgentTarget)

> *Summary: Determines whether a specific chat target requires wrapping within an agent structure. It currently always returns `False`, indicating no wrapper is needed by default.*


### create_wrapper_agent (method, L121-L123, parent: AgentTarget)

> *Summary: This method is intended to create a wrapper around a parent agent, taking the parent and an index as input. Currently, it raises a `NotImplementedError`, indicating that wrapping is not required for this specific target type.*


### AgentNameTarget (class, L126-L166)

> *Summary: Represents a specific conversational agent by its name, allowing it to be used as a selectable target within a group chat. It resolves to the provided agent's name string when called and provides methods for display and normalization.*


### __init__ (method, L131-L133, parent: AgentNameTarget)

> *Summary: Initializes an object by accepting the target agent's name as a required string argument and any additional configuration data. It passes these inputs up to the parent class constructor for setup.*


### can_resolve_for_speaker_selection (method, L135-L137, parent: AgentNameTarget)

> *Summary: This method unconditionally returns `True`, indicating that the current target is always resolvable when determining which agent should speak next in a group chat.*


### resolve (method, L139-L146, parent: AgentNameTarget)

> *Summary: This method determines which agent should speak by returning a `SpeakerSelectionResult` containing the target agent's name. It takes the group chat, current agent, and user agent as input to resolve this selection.*


### display_name (method, L148-L150, parent: AgentNameTarget)

> *Summary: Returns a string representing the agent's name, which serves as its human-readable identifier within the group chat context.*


### normalized_name (method, L152-L154, parent: AgentNameTarget)

> *Summary: Returns a space-free version of the target's display name, intended for use in function calling contexts. This method relies on an existing `display_name()` method to generate its output string.*


### __str__ (method, L156-L158, parent: AgentNameTarget)

> *Summary: Provides a string representation of the target agent by formatting it as a transfer instruction, such as "Transfer to [agent\_name]". This is used when displaying the target in messages.*


### needs_agent_wrapper (method, L160-L162, parent: AgentNameTarget)

> *Summary: Determines whether a specific chat target requires wrapping within an agent structure. It currently always returns `False`, indicating no wrapper is needed by default.*


### create_wrapper_agent (method, L164-L166, parent: AgentNameTarget)

> *Summary: This method is intended to create a wrapper around a parent agent, taking the parent and an index as input. Currently, it raises a `NotImplementedError`, indicating that this specific implementation does not require or support agent wrapping for its target.*


### NestedChatTarget (class, L169-L224)

> *Summary: Represents a configuration for a nested chat environment, requiring an agent wrapper to function. It provides methods to define its display name and dictates that it must be wrapped in an agent which then manages the nested chat lifecycle and hands off control back to the parent upon completion.*


### can_resolve_for_speaker_selection (method, L174-L176, parent: NestedChatTarget)

> *Summary: This method checks if the current target is suitable for use in selecting a speaker within a group conversation. It currently always returns `False`, indicating that resolution for speaker selection is not supported by default.*


### resolve (method, L178-L187, parent: NestedChatTarget)

> *Summary: This method is intended to determine a specific chat configuration within a group, but it currently raises `NotImplementedError`. It requires inputs including the group chat, the current agent, and an optional user agent.*


### display_name (method, L189-L191, parent: NestedChatTarget)

> *Summary: Returns a hardcoded string, `"a nested chat"`, representing the human-readable identifier for the target object. This method provides a simple textual representation of the entity.*


### normalized_name (method, L193-L195, parent: NestedChatTarget)

> *Summary: Returns a fixed string `"nested_chat"` to provide a space-free identifier suitable for function calling mechanisms. This method abstracts the internal representation of the target into a standardized format.*


### __str__ (method, L197-L199, parent: NestedChatTarget)

> *Summary: Provides a string representation for an `AgentTarget` object, specifically indicating a transfer to a nested chat context. This output is used when displaying the target within messages.*


### needs_agent_wrapper (method, L201-L203, parent: NestedChatTarget)

> *Summary: Determines whether the current target requires wrapping within an agent structure; it always returns `True` for this specific implementation, indicating that nested chat targets must be wrapped.*


### create_wrapper_agent (method, L205-L224, parent: NestedChatTarget)

> *Summary: This method constructs a new `ConversableAgent` designed to manage a nested chat session within a parent agent. It configures the wrapper agent with specific chat queue settings and ensures that upon completion of the nested interaction, control is handed back to the original parent agent.*


### TerminateTarget (class, L227-L261)

> *Summary: This class represents a conversation termination point within a group chat context. When resolved, it signals to the system that the current interaction should end by returning `terminate=True`.*


### can_resolve_for_speaker_selection (method, L230-L232, parent: TerminateTarget)

> *Summary: This method unconditionally returns `True`, indicating that the current target is always resolvable when determining which agent should speak. It takes no inputs and produces a boolean output.*


### resolve (method, L234-L241, parent: TerminateTarget)

> *Summary: This method immediately signals the end of a group chat interaction. It accepts the current group, agent, and user agent as input and returns a result indicating termination.*


### display_name (method, L243-L245, parent: TerminateTarget)

> *Summary: Returns a fixed string, "Terminate," representing the human-readable identifier for this transition target. This method takes no inputs and always outputs the same string.*


### normalized_name (method, L247-L249, parent: TerminateTarget)

> *Summary: Returns a fixed string `"terminate"` to provide a standardized, space-free identifier suitable for function calling mechanisms. This method ensures consistent naming regardless of the target's actual state or configuration.*


### __str__ (method, L251-L253, parent: TerminateTarget)

> *Summary: Provides a string representation for an `AgentTarget` object, which is fixed to return the literal string "Terminate". This output is intended for display within messages.*


### needs_agent_wrapper (method, L255-L257, parent: TerminateTarget)

> *Summary: Determines whether a specific chat target requires wrapping within an agent structure. It currently always returns `False`, indicating no wrapper is needed by default.*


### create_wrapper_agent (method, L259-L261, parent: TerminateTarget)

> *Summary: This method is intended to create a wrapper around a parent agent, taking the parent and an index as input. Currently, it raises a `NotImplementedError`, indicating that this specific implementation does not require or support agent wrapping for its target.*


### StayTarget (class, L264-L298)

> *Summary: This class defines a target that instructs the system to remain with the currently active agent. When resolved, it returns the name of the `current_agent`, effectively selecting that agent for continued interaction within the group chat context.*


### can_resolve_for_speaker_selection (method, L267-L269, parent: StayTarget)

> *Summary: This method unconditionally returns `True`, indicating that the current target is always resolvable when determining which agent should speak. It takes no inputs and outputs a boolean value.*


### resolve (method, L271-L278, parent: StayTarget)

> *Summary: When called, this method determines that the conversation should remain with the currently active agent. It accepts a `GroupChat`, the `current_agent`, and an optional `user_agent` as input, returning a result specifying the current agent's name.*


### display_name (method, L280-L282, parent: StayTarget)

> *Summary: Returns a static string, `"Stay"`, representing the human-readable identifier for the agent's current transition target. This method takes no inputs and always outputs the same string.*


### normalized_name (method, L284-L286, parent: StayTarget)

> *Summary: Returns a fixed string `"stay"` to provide a space-free, standardized identifier suitable for function calling mechanisms. This method ensures consistent naming regardless of the underlying target's actual identity.*


### __str__ (method, L288-L290, parent: StayTarget)

> *Summary: Provides a string representation for an `AgentTarget` object, which is used to display the target's intent as a function call message. It consistently returns the fixed string "Stay with agent".*


### needs_agent_wrapper (method, L292-L294, parent: StayTarget)

> *Summary: Determines whether a specific chat target requires wrapping within an agent structure. It currently always returns `False`, indicating no wrapper is needed by default.*


### create_wrapper_agent (method, L296-L298, parent: StayTarget)

> *Summary: This method is intended to create a wrapper around a parent agent, taking the parent and an index as input. Currently, it raises a `NotImplementedError` because the specific target implementation does not require agent wrapping.*


### RevertToUserTarget (class, L301-L337)

> *Summary: This class defines a transition target that forces the conversation to switch back to the user agent. It resolves by returning the name of the provided `user_agent` when called within a group chat context.*


### can_resolve_for_speaker_selection (method, L304-L306, parent: RevertToUserTarget)

> *Summary: This method unconditionally returns `True`, indicating that the current target is always resolvable when determining which agent should speak next in a group chat.*


### resolve (method, L308-L317, parent: RevertToUserTarget)

> *Summary: When called, this method forces a return to the specified `user_agent` within the group chat context. It requires a non-null user agent and returns a result indicating that the user agent should be selected as the next speaker.*


### display_name (method, L319-L321, parent: RevertToUserTarget)

> *Summary: Returns a fixed string, "Revert to User," which serves as the human-readable identifier for the target. This method takes no inputs and outputs a `str`.*


### normalized_name (method, L323-L325, parent: RevertToUserTarget)

> *Summary: Returns a fixed string `"revert_to_user"` to provide a space-free identifier suitable for function calling mechanisms. This method ensures consistent naming regardless of other internal state.*


### __str__ (method, L327-L329, parent: RevertToUserTarget)

> *Summary: Provides a string representation for an `AgentTarget` object, specifically returning the fixed string "Revert to User" to represent a return-to-user action in chat messages.*


### needs_agent_wrapper (method, L331-L333, parent: RevertToUserTarget)

> *Summary: Determines whether a specific chat target requires wrapping within an agent structure. It currently always returns `False`, indicating no wrapper is needed by default.*


### create_wrapper_agent (method, L335-L337, parent: RevertToUserTarget)

> *Summary: This method is intended to create a wrapper around a parent agent, taking the parent and an index as input. Currently, it raises a `NotImplementedError` because the specific target implementation does not require this wrapping mechanism.*


### AskUserTarget (class, L340-L374)

> *Summary: This class defines a transition target that forces interaction by requesting input from the user. When resolved, it signals a manual speaker selection method to the group chat system.*


### can_resolve_for_speaker_selection (method, L343-L345, parent: AskUserTarget)

> *Summary: This method unconditionally returns `True`, indicating that the current target is always resolvable when determining which agent should speak. It takes no inputs and outputs a boolean value.*


### resolve (method, L347-L354, parent: AskUserTarget)

> *Summary: When called with a `GroupChat`, an agent, and an optional user agent, this method immediately returns a result indicating that manual speaker selection is required. It serves as a fallback or default mechanism to prompt the user for input in group conversations.*


### display_name (method, L356-L358, parent: AskUserTarget)

> *Summary: Returns a fixed string, `"Ask User"`, representing the human-readable identifier for this chat target. This method takes no inputs and always outputs the same string.*


### normalized_name (method, L360-L362, parent: AskUserTarget)

> *Summary: Returns a fixed string `"ask_user"` to provide a space-free identifier suitable for function calling mechanisms. This method ensures consistent naming regardless of the object's internal state.*


### __str__ (method, L364-L366, parent: AskUserTarget)

> *Summary: Provides a string representation for an `AgentTarget` object, specifically returning the fixed string `"Ask User"` to represent it in conversational messages.*


### needs_agent_wrapper (method, L368-L370, parent: AskUserTarget)

> *Summary: Determines whether the current target requires wrapping within an agent structure. It currently always returns `False`, indicating no wrapper is needed by default.*


### create_wrapper_agent (method, L372-L374, parent: AskUserTarget)

> *Summary: This method is intended to create a wrapper around a parent agent, but it currently raises `NotImplementedError` because the specific target implementation does not necessitate such wrapping. It accepts a parent agent and an index as input and returns a new `ConversableAgent`.*


### RandomAgentTarget (class, L377-L421)

> *Summary: This class selects a random agent from a provided list of agents to act as the next speaker. Given a group chat context, it resolves by choosing any agent other than the current one and returns that agent's name for selection.*


### __init__ (method, L383-L385, parent: RandomAgentTarget)

> *Summary: Initializes a transition target by accepting a list of `ConversableAgent` instances and storing their names for serialization. It passes these collected agent names, along with any other provided data, to the parent constructor.*


### can_resolve_for_speaker_selection (method, L387-L389, parent: RandomAgentTarget)

> *Summary: This method unconditionally returns `True`, indicating that the current target is always resolvable when determining which agent should speak. It takes no inputs and outputs a boolean value.*


### resolve (method, L391-L401, parent: RandomAgentTarget)

> *Summary: This method selects a random agent from the group chat, excluding the currently active agent. It returns a `SpeakerSelectionResult` containing the chosen agent's name.*


### display_name (method, L403-L405, parent: RandomAgentTarget)

> *Summary: Retrieves and returns the designated string identifier for the agent's target. This method uses the `nominated_name` attribute to generate the output string.*


### normalized_name (method, L407-L409, parent: RandomAgentTarget)

> *Summary: Returns a space-free version of the target's display name, intended for use in function calling contexts. This method relies on an existing `display_name()` method to generate its output string.*


### __str__ (method, L411-L413, parent: RandomAgentTarget)

> *Summary: Provides a string representation of the target agent, formatted as a function call message indicating a transfer to a specific nominated agent.*


### needs_agent_wrapper (method, L415-L417, parent: RandomAgentTarget)

> *Summary: Determines whether the current target requires wrapping within an agent structure. It currently always returns `False`, indicating no wrapper is needed by default.*


### create_wrapper_agent (method, L419-L421, parent: RandomAgentTarget)

> *Summary: This method is intended to create a wrapper around a parent agent, taking the parent and an index as input. Currently, it raises a `NotImplementedError`, indicating that this specific implementation doesn't require or support agent wrapping for its target.*

