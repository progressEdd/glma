# autogen/agentchat/group/available_condition.py

3 class(es): AvailableCondition, StringAvailableCondition, ExpressionAvailableCondition. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AvailableCondition | class |  |
| StringAvailableCondition | class |  |
| ExpressionAvailableCondition | class |  |

## Chunks

### AvailableCondition (class, L18-L31)

> *Summary: Defines a protocol requiring implementations to check if a specific condition is ready for evaluation. It accepts an agent and message history as input and returns a boolean indicating whether the condition should proceed with evaluation.*


### is_available (method, L21-L31, parent: AvailableCondition)

> *Summary: This method checks whether a specific conversational condition is relevant for evaluation given an agent and the message history. It currently requires subclasses to provide their own implementation logic.*


### StringAvailableCondition (class, L34-L61)

> *Summary: Checks for the existence and truthiness of a specified context variable within an agent's state. It takes a variable name during initialization and returns `True` if the variable is present and evaluates to true in the agent's context.*


### __init__ (method, L42-L49, parent: StringAvailableCondition)

> *Summary: Initializes an object by accepting a string representing a context variable name and optional keyword arguments. It passes these inputs directly up to its parent class constructor.*


### is_available (method, L51-L61, parent: StringAvailableCondition)

> *Summary: Determines if a named context variable within an agent is present and evaluates to a truthy value. It takes an agent object and conversation history as input, returning a boolean indicating availability.*


### ExpressionAvailableCondition (class, L64-L91)

> *Summary: This class evaluates a provided `ContextExpression` against an agent's current context variables to determine availability. It takes a `ContextExpression` upon initialization and returns a boolean indicating whether the condition is met when its `is_available` method is called with an agent object.*


### __init__ (method, L72-L79, parent: ExpressionAvailableCondition)

> *Summary: Initializes an object by accepting a `ContextExpression` instance and optional keyword arguments. It passes these inputs directly up to its parent class constructor.*


### is_available (method, L81-L91, parent: ExpressionAvailableCondition)

> *Summary: Determines if a condition is met by evaluating an internal expression against the provided agent's context variables. It returns a boolean indicating the truthiness of that expression based on the agent's state.*

