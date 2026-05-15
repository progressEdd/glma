# autogen/agentchat/group/handoffs.py

1 class(es): Handoffs. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Handoffs | class |  |

## Chunks

### Handoffs (class, L16-L303)

> *Summary: This class manages transition logic for an agent by storing three types of conditions: context-based (evaluated without LLM), LLM-based (evaluated with LLM), and post-work targets. It provides fluent methods to add, clear, and retrieve these conditions based on specific criteria or target types.*


### add_context_condition (method, L34-L48, parent: Handoffs)

> *Summary: Appends a specified `OnContextCondition` to the object's list of context conditions after validating its type. It returns the current instance to allow for method chaining.*


### add_context_conditions (method, L50-L64, parent: Handoffs)

> *Summary: Extends the internal list of context conditions by appending a provided list of `OnContextCondition` objects after validating their types. Returns the instance itself to allow for method chaining.*


### add_llm_condition (method, L66-L80, parent: Handoffs)

> *Summary: Appends a specified `OnCondition` object to the internal list of LLM conditions for this handoff mechanism. It validates the input type and returns the instance itself to allow for method chaining.*


### add_llm_conditions (method, L82-L96, parent: Handoffs)

> *Summary: Extends the internal list of LLM conditions by appending a provided list of `OnCondition` objects after validating their types. Returns the instance itself to allow for method chaining.*


### set_after_work (method, L98-L115, parent: Handoffs)

> *Summary: This method replaces all existing after-work targets with a single new target specified by the input `TransitionTarget`. It ensures backward compatibility by wrapping the provided target in an always-true context condition and returns the instance for chaining.*


### add_after_work (method, L117-L151, parent: Handoffs)

> *Summary: This method appends a specified context condition to an agent's list of after-work triggers, ensuring that any conditions without a specific trigger (`condition=None`) are always placed at the end of the sequence. It handles replacement and reordering logic based on whether the incoming condition is `None` or not.*


### add_after_works (method, L153-L185, parent: Handoffs)

> *Summary: This method appends a list of context-based conditions to an existing set, ensuring only one fallback condition (`condition=None`) is present and placed at the end. It validates inputs, filters out any pre-existing `None` fallbacks, adds all non-`None` conditions, and then appends the final provided `None` condition if any exist.*


### add (method, L188-L188, parent: Handoffs)

> *Summary: This method accepts an `OnContextCondition` object and adds it to the current handoff configuration. It returns the updated `Handoffs` instance.*


### add (method, L191-L191, parent: Handoffs)

> *Summary: This method appends a new `OnCondition` trigger to the agent's list of handoff conditions. It takes one `OnCondition` object as input and returns the updated `Handoffs` instance.*


### add (method, L193-L212, parent: Handoffs)

> *Summary: This method accepts either an `OnContextCondition` or an `OnCondition` object to register a handoff trigger. It delegates the addition based on the input type, returning the instance for fluent chaining or raising a `TypeError` if the condition is unsupported.*


### add_many (method, L214-L244, parent: Handoffs)

> *Summary: Accepts a list of `OnContextCondition` and `OnCondition` objects, segregating them into context-specific and LLM-specific lists before adding them to the instance's respective handlers. It returns the instance itself to allow for method chaining.*


### clear (method, L246-L255, parent: Handoffs)

> *Summary: Resets the internal state of the handoff object by emptying lists tracking context, LLM, and post-work conditions. It returns `self` to allow for method chaining in subsequent operations.*


### get_llm_conditions_by_target_type (method, L257-L266, parent: Handoffs)

> *Summary: Retrieves a list of `OnCondition` objects from stored conditions that match the provided target type. It filters the internal collection based on whether each condition possesses the specified type.*


### get_context_conditions_by_target_type (method, L268-L281, parent: Handoffs)

> *Summary: Retrieves a list of `OnContextCondition` objects from the instance's collection that match a given target type. It filters the internal conditions based on whether each one possesses the specified target type.*


### get_llm_conditions_requiring_wrapping (method, L283-L289, parent: Handoffs)

> *Summary: Retrieves a list of `OnCondition` objects from the agent's stored LLM conditions where the associated target necessitates wrapping logic. This filtering operation returns only those specific conditions that meet the wrapping requirement.*


### get_context_conditions_requiring_wrapping (method, L291-L297, parent: Handoffs)

> *Summary: Retrieves a list of `OnContextCondition` objects from the instance's stored conditions where the associated target necessitates wrapping. This filters the existing context conditions based on a specific requirement check within each condition's target.*


### set_llm_function_names (method, L299-L303, parent: Handoffs)

> *Summary: Iterates through all defined LLM conditions to assign a unique function name to each one. This ensures that multiple conditions targeting the same agent can have distinct, identifiable names for the language model.*

