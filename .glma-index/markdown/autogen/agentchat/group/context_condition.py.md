# autogen/agentchat/group/context_condition.py

3 class(es): ContextCondition, StringContextCondition, ExpressionContextCondition. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ContextCondition | class |  |
| StringContextCondition | class |  |
| ExpressionContextCondition | class |  |

## Chunks

### ContextCondition (class, L16-L28)

> *Summary: Defines an abstract protocol for conditions that check state using provided context variables. It requires implementing a method to return a boolean based on those input variables.*


### evaluate (method, L19-L28, parent: ContextCondition)

> *Summary: This method is intended to check a specific condition using provided context variables, returning a boolean outcome. Currently, it raises an error, requiring derived classes to provide the actual implementation logic.*


### StringContextCondition (class, L31-L48)

> *Summary: This condition evaluates whether a specified named context variable within the provided context dictionary exists and holds a truthy value. It returns `True` if the variable is present and non-falsy, otherwise it returns `False`.*


### evaluate (method, L39-L48, parent: StringContextCondition)

> *Summary: Determines if a specified named context variable within the provided `ContextVariables` object evaluates to true. It returns `True` only if the variable exists and its value is truthy; otherwise, it returns `False`.*


### ExpressionContextCondition (class, L51-L77)

> *Summary: This class evaluates a provided `ContextExpression` using the supplied `ContextVariables`. It returns a boolean indicating whether the complex expression holds true within the given context.*


### __init__ (method, L59-L66, parent: ExpressionContextCondition)

> *Summary: Initializes the object by accepting a `ContextExpression` which dictates the condition to be evaluated. It passes this expression and any extra keyword arguments up to its parent class constructor.*


### evaluate (method, L68-L77, parent: ExpressionContextCondition)

> *Summary: This method executes a stored expression using provided `ContextVariables`. It returns a boolean indicating whether the condition defined by the expression is met within the given context.*

