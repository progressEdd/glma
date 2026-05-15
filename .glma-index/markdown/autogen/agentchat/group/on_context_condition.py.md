# autogen/agentchat/group/on_context_condition.py

1 class(es): OnContextCondition. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OnContextCondition | class |  |

## Chunks

### OnContextCondition (class, L17-L51)

> *Summary: This model defines a rule for transitioning between agents based on context variables, evaluating conditions without involving the LLM. It specifies a `target` agent and an optional `condition` to trigger the handoff, while also supporting an optional `available` check.*


### has_target_type (method, L34-L43, parent: OnContextCondition)

> *Summary: Determines if the agent's current `target` object is an instance of the provided `target_type`. It returns a boolean indicating a match between the stored target and the input type.*


### target_requires_wrapping (method, L45-L51, parent: OnContextCondition)

> *Summary: Determines whether a specific target entity needs to be wrapped by an agent. It achieves this by delegating the check to the target's own `needs_agent_wrapper()` method and returns the resulting boolean value.*

