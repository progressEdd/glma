# test/agentchat/group/test_context_condition.py

4 class(es): TestContextCondition, TestStringContextCondition, TestExpressionContextCondition, TestContextConditionIntegration. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestContextCondition | class |  |
| TestStringContextCondition | class |  |
| TestExpressionContextCondition | class |  |
| TestContextConditionIntegration | class |  |

## Chunks

### TestContextCondition (class, L18-L30)

> *Summary: This test verifies that any class inheriting from `ContextCondition` but failing to override the `evaluate` method will raise a `NotImplementedError` when called with mock context variables. It ensures the protocol enforces implementation of the evaluation logic in subclasses.*


### test_protocol_raise_not_implemented (method, L19-L30, parent: TestContextCondition)

> *Summary: Verifies that any class implementing the `ContextCondition` protocol but failing to override the `evaluate` method correctly raises a `NotImplementedError`. This test confirms the expected runtime behavior when an abstract method is called on an incomplete implementation.*


### TestStringContextCondition (class, L33-L134)

> *Summary: This test suite verifies the behavior of a context condition that checks for the truthiness of a specific variable within a provided context. It confirms correct initialization, and tests evaluation against various inputs—including `True`, `False`, missing values, `None`, and different types like strings or collections—to ensure accurate boolean output.*


### test_init (method, L34-L38, parent: TestStringContextCondition)

> *Summary: Verifies that an instance of `StringContextCondition` correctly stores the provided string variable name upon initialization. It confirms the internal state matches the input argument.*


### test_init_with_extra_data (method, L40-L48, parent: TestStringContextCondition)

> *Summary: This test verifies that an instance of `StringContextCondition` correctly initializes with specified variable names and arbitrary additional keyword arguments. It asserts that the primary `variable_name` attribute is set as expected, while noting limitations regarding how Pydantic handles extra data storage.*


### test_evaluate_with_true_value (method, L50-L57, parent: TestStringContextCondition)

> *Summary: This test verifies that a `StringContextCondition` correctly evaluates to `True` when the specified variable in the input context holds a truthy value (`True`). It asserts that calling `.evaluate()` on the condition with the provided context yields `True`.*


### test_evaluate_with_false_value (method, L59-L66, parent: TestStringContextCondition)

> *Summary: This test verifies that a `StringContextCondition` evaluates to `False` when the specified variable in the context holds a falsy value. It passes a context containing `{ "test_variable": False }` and asserts the condition's evaluation returns `False`.*


### test_evaluate_with_missing_value (method, L68-L75, parent: TestStringContextCondition)

> *Summary: When provided with an empty context, this test verifies that a `StringContextCondition` correctly evaluates to `False` because the specified variable is missing from the input data. It confirms the condition's behavior when no relevant variables are present in the execution environment.*


### test_evaluate_with_none_value (method, L77-L84, parent: TestStringContextCondition)

> *Summary: When provided with a context where the specified variable holds a `None` value, this test confirms that the condition evaluates to `False`. It uses a `StringContextCondition` against a mock context containing `None` for the target variable.*


### test_evaluate_with_non_bool_value (method, L86-L109, parent: TestStringContextCondition)

> *Summary: This test verifies that a `StringContextCondition` correctly evaluates to `True` or `False` based on the truthiness of a provided variable's value within a context. It specifically checks behavior using non-boolean inputs like empty/non-empty strings and integers (0 vs 1).*


### test_evaluate_with_collection_values (method, L111-L134, parent: TestStringContextCondition)

> *Summary: This test verifies that a `StringContextCondition` correctly evaluates based on the truthiness of collection types provided in the context variables. It asserts that non-empty lists and dictionaries evaluate to `True`, while empty lists and dictionaries evaluate to `False`.*


### TestExpressionContextCondition (class, L137-L326)

> *Summary: This test suite verifies the functionality of an expression context condition, which evaluates a string-based logical expression against provided context variables. It confirms correct initialization, successful evaluation for various boolean and numeric comparisons, proper error handling for missing variables, and limitations regarding nested variable access.*


### test_init (method, L138-L142, parent: TestExpressionContextCondition)

> *Summary: Verifies that an `ExpressionContextCondition` correctly stores the provided `ContextExpression`. It initializes the condition using a string-based expression like "${var1} and ${var2}" and asserts the stored expression matches the input.*


### test_init_with_extra_data (method, L144-L149, parent: TestExpressionContextCondition)

> *Summary: Verifies that an `ExpressionContextCondition` correctly initializes when provided with additional keyword arguments alongside its primary expression. It confirms the internal expression attribute matches the input instance.*


### test_evaluate_calls_expression_evaluate (method, L152-L163, parent: TestExpressionContextCondition)

> *Summary: This test verifies that an `ExpressionContextCondition` correctly invokes the underlying expression's evaluation method when provided with context variables. It asserts that the condition evaluates to the mocked return value of the expression and that the evaluation method was called exactly once with the input context.*


### test_evaluate_with_true_expression (method, L165-L172, parent: TestExpressionContextCondition)

> *Summary: When provided with a context containing `var1=True` and `var2=True`, this test confirms that an expression combining them with an AND operator correctly evaluates to `True`. The function takes variable data as input and returns the boolean evaluation of the defined condition.*


### test_evaluate_with_false_expression (method, L174-L181, parent: TestExpressionContextCondition)

> *Summary: When provided with a context containing `var1=True` and `var2=False`, this test verifies that the condition evaluates to `False` because the expression `${var1} and ${var2}` resolves to false. The function takes context variables as input and returns a boolean result based on the evaluated expression.*


### test_evaluate_with_complex_expression (method, L183-L201, parent: TestExpressionContextCondition)

> *Summary: This test verifies the correct evaluation of a complex boolean expression involving logical operators (`or`, `and`, `not`). It passes various sets of input variables to an `ExpressionContextCondition` and asserts that the resulting truth value matches expected outcomes.*


### test_evaluate_with_missing_variables_raises_keyerror (method, L203-L229, parent: TestExpressionContextCondition)

> *Summary: This test verifies that evaluating a condition expression against an empty or partially populated context correctly raises a `KeyError`. It confirms the error message explicitly indicates which required context variables are missing during evaluation.*


### test_nested_variable_not_supported (method, L231-L250, parent: TestExpressionContextCondition)

> *Summary: This test verifies that the `ContextExpression` class rejects dot notation for nested attributes by expecting a `ValueError`. It confirms functionality by successfully evaluating an expression using flattened variable names against provided context data.*


### test_evaluate_with_comparison_operators (method, L252-L300, parent: TestExpressionContextCondition)

> *Summary: This test verifies that an `ExpressionContextCondition` correctly evaluates boolean logic based on comparison operators (`>`, `<`, `==`, `!=`). It takes a set of context variables (like counts or statuses) as input and returns `True` or `False` depending on whether the defined expression holds true for those inputs.*


### test_evaluate_with_numeric_comparisons (method, L302-L326, parent: TestExpressionContextCondition)

> *Summary: This test verifies that a context condition correctly evaluates boolean outcomes based on numeric comparisons within provided variables. It checks scenarios for greater than or equal to, and less than or equal to, using input data like `{"count": 10}` and `{"count": 9}` to assert the resulting `True` or `False`.*


### TestContextConditionIntegration (class, L329-L413)

> *Summary: This test suite verifies the dynamic evaluation of context-based conditions, specifically `StringContextCondition` and `ExpressionContextCondition`, against a mutable set of context variables. It confirms that conditions correctly evaluate based on variable presence, value changes (updates/removals), and demonstrates combining multiple conditions using logical AND/OR operations.*


### test_string_condition_with_updates (method, L330-L351, parent: TestContextConditionIntegration)

> *Summary: This test verifies the `StringContextCondition`'s behavior when its target variable in the context is dynamically modified. It confirms that evaluation returns `False` if the variable is missing, and correctly reflects changes (from `False` to `True`) or removal of the specified string value within the provided context variables.*


### test_expression_condition_with_updates (method, L353-L379, parent: TestContextConditionIntegration)

> *Summary: This test verifies that an `ExpressionContextCondition` correctly evaluates dynamic expressions based on a mutable context. It demonstrates the condition's ability to change its boolean output when input variables are updated, and confirms it raises a `KeyError` if required variables are removed from the context.*


### test_combine_conditions (method, L381-L413, parent: TestContextConditionIntegration)

> *Summary: This test verifies the logical combination of different context conditions, such as `StringContextCondition` and `ExpressionContextCondition`. It evaluates how these conditions behave when combined using both AND and OR operators across various input contexts.*

