# test/agentchat/group/test_available_condition.py

4 class(es): TestAvailableCondition, TestStringAvailableCondition, TestContextExpressionAvailableCondition, TestAvailableConditionIntegration. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestAvailableCondition | class |  |
| TestStringAvailableCondition | class |  |
| TestContextExpressionAvailableCondition | class |  |
| TestAvailableConditionIntegration | class |  |

## Chunks

### TestAvailableCondition (class, L18-L30)

> *Summary: Verifies that any class implementing the `AvailableCondition` protocol but failing to override the `is_available` method correctly raises a `NotImplementedError` when called with an agent and context. This ensures required methods are explicitly implemented by subclasses.*


### test_protocol_raise_not_implemented (method, L19-L30, parent: TestAvailableCondition)

> *Summary: Verifies that an implementation of the `AvailableCondition` protocol raises a `NotImplementedError` when its required `is_available` method is not overridden by the subclass. It achieves this by instantiating a minimal class conforming to the protocol and calling the unimplemented method against a mocked agent.*


### TestStringAvailableCondition (class, L33-L164)

> *Summary: This test suite verifies the `StringAvailableCondition` class, which checks if a specified context variable exists and evaluates to a truthy value within an agent's context. It confirms correct initialization, handling of missing or falsy values (like `None`, empty strings, or empty collections), and ensures the condition ignores any provided message history during evaluation.*


### test_init (method, L34-L38, parent: TestStringAvailableCondition)

> *Summary: Verifies that an instance of `StringAvailableCondition` correctly stores the provided context variable name upon initialization. It confirms the internal state matches the input string argument.*


### test_init_with_extra_data (method, L40-L48, parent: TestStringAvailableCondition)

> *Summary: This test verifies that an instance of `StringAvailableCondition` correctly initializes with a specified context variable name and accepts arbitrary keyword arguments. It asserts that the provided context variable is stored as expected, noting limitations regarding how Pydantic v2 handles extra data.*


### test_is_available_with_true_value (method, L50-L59, parent: TestStringAvailableCondition)

> *Summary: Verifies that a `StringAvailableCondition` evaluates to true when the specified context variable holds a truthy value. It mocks an agent with a context containing `"test_variable": True` and asserts the condition returns `True`.*


### test_is_available_with_false_value (method, L61-L70, parent: TestStringAvailableCondition)

> *Summary: Verifies that a `StringAvailableCondition` evaluates to `False` when the specified context variable holds a falsy value (like `False`). It achieves this by mocking an agent whose context variables contain the test variable set to `False`.*


### test_is_available_with_missing_value (method, L72-L81, parent: TestStringAvailableCondition)

> *Summary: Verifies that a `StringAvailableCondition` evaluates to `False` when the specified context variable is absent from the agent's context variables. It passes an agent mock with empty context data and asserts the condition returns `False`.*


### test_is_available_with_none_value (method, L83-L92, parent: TestStringAvailableCondition)

> *Summary: Verifies that a `StringAvailableCondition` evaluates to false when the specified context variable holds a `None` value within the agent's context. It passes a mocked agent with `None` data for the test variable and asserts the condition returns `False`.*


### test_is_available_with_non_bool_value (method, L94-L119, parent: TestStringAvailableCondition)

> *Summary: This test verifies that a `StringAvailableCondition` correctly determines availability based on the truthiness of a specified context variable's value. It asserts that the method returns `True` for truthy inputs (like non-empty strings or 1) and `False` for falsy inputs (like empty strings or 0).*


### test_is_available_with_collection_values (method, L121-L146, parent: TestStringAvailableCondition)

> *Summary: This test verifies the `StringAvailableCondition` logic when checking for variable presence using collection types as values in the agent's context. It asserts that the condition returns true for non-empty lists/dictionaries and false for empty ones.*


### test_messages_parameter_ignored (method, L148-L164, parent: TestStringAvailableCondition)

> *Summary: Verifies that the `messages` argument passed to an availability check does not influence the outcome when checking a string variable's existence in the agent's context. It confirms that two different sets of input messages yield the same boolean result as expected.*


### TestContextExpressionAvailableCondition (class, L167-L333)

> *Summary: This test suite verifies the functionality of an expression availability condition, which checks if a specified context expression evaluates to true based on an agent's variables. It confirms correct initialization, successful evaluation against mock contexts (including complex logic and comparisons), and proper error handling for missing variables or unsupported expressions.*


### test_init (method, L168-L172, parent: TestContextExpressionAvailableCondition)

> *Summary: Verifies that an `ExpressionAvailableCondition` correctly stores the provided `ContextExpression` upon initialization. It confirms the internal state matches the input expression object.*


### test_init_with_extra_data (method, L174-L182, parent: TestContextExpressionAvailableCondition)

> *Summary: This test verifies that an `ExpressionAvailableCondition` object correctly stores its provided `ContextExpression`. It demonstrates initialization by passing in additional keyword arguments, though it notes Pydantic v2's behavior regarding storing these extras.*


### test_is_available_calls_expression_evaluate (method, L185-L199, parent: TestContextExpressionAvailableCondition)

> *Summary: This test verifies that an `ExpressionAvailableCondition` correctly invokes the associated expression's evaluation method when checking availability. It passes a mocked agent containing context variables to the evaluator and asserts both the call was made with the correct context and the resulting boolean value matches the mock return.*


### test_is_available_with_true_expression (method, L201-L210, parent: TestContextExpressionAvailableCondition)

> *Summary: When provided with a context expression like `"var1 and var2"` and mock agent variables where both `var1` and `var2` are true, the availability check returns `True`. This verifies that the condition correctly evaluates to true based on its input expression and context.*


### test_is_available_with_false_expression (method, L212-L221, parent: TestContextExpressionAvailableCondition)

> *Summary: When provided with a context expression like `${var1} and ${var2}` and mock variables where `var2` is false, the method evaluates to `False`. This confirms that the availability check correctly returns `False` when the underlying logical expression fails.*


### test_is_available_with_complex_expression (method, L223-L243, parent: TestContextExpressionAvailableCondition)

> *Summary: This test verifies the `is_available` method's logic when evaluating a complex boolean expression involving multiple context variables. It passes mock agents with different variable states to confirm the function correctly returns `True` or `False` based on the expression's evaluation.*


### test_is_available_with_missing_variables (method, L245-L255, parent: TestContextExpressionAvailableCondition)

> *Summary: This test verifies that an `ExpressionAvailableCondition` correctly raises a `KeyError` when the underlying context is missing variables required by its expression (e.g., `${var2}`). It simulates this by providing mock agent data containing only one of two necessary variables.*


### test_is_available_with_nested_variables (method, L257-L263, parent: TestContextExpressionAvailableCondition)

> *Summary: This test verifies that attempting to create a `ContextExpression` with nested variable lookups, such as `${user.is_premium} and ${user.status} == 'active'`, correctly raises a `ValueError`. It confirms the current implementation does not support complex, chained attribute operations within the expression string.*


### test_messages_parameter_ignored (method, L265-L281, parent: TestContextExpressionAvailableCondition)

> *Summary: Verifies that the `messages` argument passed to an availability check does not influence the outcome when the condition relies solely on context variables. It confirms that two different sets of input messages yield the same boolean result as expected from the defined expression.*


### test_is_available_with_comparison_operators (method, L283-L333, parent: TestContextExpressionAvailableCondition)

> *Summary: Verifies that an `ExpressionAvailableCondition` correctly evaluates to true or false based on comparison operators (`>`, `<`, `==`, `!=`) against mock agent context variables. It tests various scenarios by setting different values for context data and checking the resulting boolean output of the condition's availability check.*


### TestAvailableConditionIntegration (class, L336-L381)

> *Summary: These tests verify the functionality of availability conditions by simulating agent contexts. They confirm that `StringAvailableCondition` correctly evaluates based on a specific context variable's boolean state, and that `ExpressionAvailableCondition` accurately assesses complex logical expressions against dynamic context variables.*


### test_string_condition_with_real_agent (method, L337-L357, parent: TestAvailableConditionIntegration)

> *Summary: This test verifies that a `StringAvailableCondition` correctly evaluates based on the presence and value of a specified context variable within an agent's state. It confirms the condition returns false when the variable is absent or set to `False`, and true only when it is explicitly set to `True`.*


### test_context_expression_condition_with_real_agent (method, L359-L381, parent: TestAvailableConditionIntegration)

> *Summary: This test verifies that an `ExpressionAvailableCondition` correctly evaluates its logic based on a provided agent's context variables. It demonstrates toggling the condition's availability by changing values like `login_count` and `is_premium` within the mock agent's state.*

