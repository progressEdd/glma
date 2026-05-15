# autogen/agentchat/group/on_condition.py

1 class(es): OnCondition. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OnCondition | class |  |

## Chunks

### OnCondition (class, L19-L55)

> *Summary: Represents a transition rule that dictates when to hand off control to another agent or nested chat based on LLM evaluation. It holds references to the destination agent, the specific condition for triggering the switch, and optional context availability checks.*


### has_target_type (method, L38-L47, parent: OnCondition)

> *Summary: Determines if the agent's current `target` object is an instance of the provided `target_type`. It returns a boolean indicating a match between the runtime type and the expected class.*


### target_requires_wrapping (method, L49-L55, parent: OnCondition)

> *Summary: Determines whether a specified target needs to be wrapped by an agent by delegating the check to the target's internal method. It returns a boolean indicating the necessity for such wrapping.*

