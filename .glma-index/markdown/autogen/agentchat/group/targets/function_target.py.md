# autogen/agentchat/group/targets/function_target.py

3 function(s): construct_broadcast_messages_list, broadcast, validate_fn_sig. 3 class(es): FunctionTargetMessage, FunctionTargetResult, FunctionTarget. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FunctionTargetMessage | class |  |
| FunctionTargetResult | class |  |
| construct_broadcast_messages_list | function |  |
| broadcast | function |  |
| validate_fn_sig | function |  |
| FunctionTarget | class |  |

## Chunks

### FunctionTargetMessage (class, L26-L37)

> *Summary: Represents a message intended for a specific agent within a function target result. It encapsulates both the string content of the message and a reference to the destination `Agent`.*


### FunctionTargetResult (class, L40-L51)

> *Summary: Represents the outcome of a function handoff, encapsulating messages for broadcasting, optional updates to group context variables, and the designated next transition target. It serves as the structured return value after an agent executes a function call within the group chat system.*


### construct_broadcast_messages_list (function, L54-L80)

> *Summary: This function transforms an input message (either a string or a list of `FunctionTargetMessage` objects) into a standardized list of `FunctionTargetMessage`s. It determines the recipient agent based on the provided `TransitionTarget`, routing the content to the specified agent, user, or keeping it with the current agent if no specific target is defined.*


### broadcast (function, L83-L109)

> *Summary: Sends provided message(s), which can be individual messages or strings, across a specified target within a group chat. It wraps the content with a system-level function handoff notification before dispatching it via the current agent's group manager.*


### validate_fn_sig (function, L112-L159)

> *Summary: This utility validates the signature of a user-defined callback function, ensuring it accepts at least two positional arguments. It then verifies that all non-core parameters beyond the first two are either present in provided extra arguments or have default values defined on the function itself.*


### FunctionTarget (class, L162-L245)

> *Summary: This class acts as a transition target that executes a specified tool function using the last message content and agent context as inputs. It processes the returned `FunctionTargetResult` to update context variables, broadcast messages if present, and finally resolves and returns the next designated target for the group chat.*


### __init__ (method, L172-L188, parent: FunctionTarget)

> *Summary: Initializes a target by validating and storing an incoming callable function. It ensures the provided function is callable, validates its signature against any extra arguments, and then passes this information to the parent class constructor.*


### can_resolve_for_speaker_selection (method, L190-L191, parent: FunctionTarget)

> *Summary: This method always returns `False`, indicating that the current target cannot be resolved for speaker selection purposes. It serves as a simple gatekeeping mechanism within the agent chat group logic.*


### resolve (method, L193-L230, parent: FunctionTarget)

> *Summary: Executes a provided function using the last message and agent context to produce a result. It updates group context variables if necessary, broadcasts any generated messages to the specified target, and finally returns the next designated target for the group chat.*


### display_name (method, L232-L233, parent: FunctionTarget)

> *Summary: Returns the name of the associated function as a string identifier for display purposes.*


### normalized_name (method, L235-L236, parent: FunctionTarget)

> *Summary: Transforms the internal function name by replacing all spaces with underscores to create a standardized, usable string identifier. This method takes no input and returns the modified name as a string.*


### __str__ (method, L238-L239, parent: FunctionTarget)

> *Summary: Provides a string representation indicating the target function name for transfer. This is used when representing the object as a string, outputting "Transfer to tool [function\_name]".*


### needs_agent_wrapper (method, L241-L242, parent: FunctionTarget)

> *Summary: This method always returns `False`, indicating that the current target does not require an agent wrapper for its execution. It serves as a simple boolean check within the group targeting logic.*


### create_wrapper_agent (method, L244-L245, parent: FunctionTarget)

> *Summary: This method intentionally raises an error because the `FunctionTarget` agent executes its logic directly within a larger process rather than requiring a separate wrapping agent. It expects to be called without creating any intermediary agent structure.*

