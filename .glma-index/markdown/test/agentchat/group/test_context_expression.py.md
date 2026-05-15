# test/agentchat/group/test_context_expression.py

1 class(es): TestContextExpressionNewSyntax. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestContextExpressionNewSyntax | class |  |

## Chunks

### TestContextExpressionNewSyntax (class, L11-L455)

> *Summary: This test suite verifies the functionality of `ContextExpression` by executing various logical and comparison operations against a provided context. It validates support for basic boolean logic, symbolic operators (`!`, `&`, `|`), numeric/string comparisons, length checks on collections, and complex nested expressions, ensuring correct evaluation even when variables are missing.*


### test_basic_boolean_operations (method, L14-L41, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies the functionality of boolean logic within a context expression evaluator. It uses an input `ContextVariables` object containing predefined true/false values to assert correct evaluation for simple lookups, NOT, AND, and OR operations.*


### test_symbolic_operators (method, L43-L70, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies the correct evaluation of symbolic boolean operators (`!`, `&`, `|`) within a context expression. It takes a `ContextVariables` object containing boolean variables as input and asserts that expressions like `!${var_true}` or `${var_true} & ${var_false}` yield the expected boolean output.*


### test_mixed_syntax (method, L72-L84, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies that the expression evaluator correctly handles a mix of symbolic and keyword operators within context expressions. It asserts expected boolean outcomes when evaluating strings containing variables like `${var_true}` against provided context data.*


### test_numeric_comparisons (method, L86-L125, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies the correct evaluation of various numeric comparisons (equality, inequality, greater than, less than, and boundary checks) using predefined numerical variables within a context. It asserts that expressions like `${var} == value` resolve to the expected boolean outcome based on the input data.*


### test_comparisons_with_symbolic_operators (method, L127-L138, parent: TestContextExpressionNewSyntax)

> *Summary: Verifies that boolean logic and numeric comparisons can be correctly evaluated when combined using symbolic operators (`&`, `|`, `!`) against a provided context of variables. It tests various combinations, including mixed types and nested expressions, to ensure accurate logical evaluation.*


### test_string_comparisons (method, L140-L165, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies the functionality of string comparisons within a context expression evaluator. It uses a `ContextVariables` object containing predefined strings to assert correct boolean outcomes for equality (`==`) and inequality (`!=`) checks against literals and other variables.*


### test_string_comparisons_with_symbolic_operators (method, L167-L174, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies that string comparisons combined with logical operators evaluate correctly within a given context. It uses `ContextVariables` to provide input data and asserts the boolean results of complex expressions like `${str_hello} == 'hello' & ${is_premium}`.*


### test_complex_expressions (method, L176-L214, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies the evaluation of complex, nested logical expressions using a provided set of context variables. It asserts that various combinations of boolean logic, comparisons (e.g., `>=`), and string matching yield the expected true or false results based on the input data.*


### test_complex_expressions_with_symbolic_operators (method, L216-L253, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies the correct evaluation of complex boolean and relational expressions using symbolic operators against a provided set of context variables. It asserts that various combinations, including nested logic and mixed operators, yield expected boolean results based on the input data.*


### test_missing_variables (method, L255-L284, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies that evaluating expressions containing undefined variables within a `ContextVariables` object raises a `KeyError`. It confirms the expected failure behavior for various logical and symbolic operations when inputs are missing.*


### test_real_world_examples (method, L286-L324, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies the functionality of `ContextExpression` by evaluating several real-world business logic scenarios. It takes a predefined set of context variables (like user status, order details, and customer attributes) as input to assert correct boolean outcomes from complex string expressions.*


### test_real_world_examples_with_symbolic_operators (method, L326-L370, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies the correct evaluation of complex business logic expressions using symbolic operators against a predefined set of context variables. It asserts that various combinations of boolean and comparison operations yield expected true results based on the input data.*


### test_precedence_with_symbolic_operators (method, L372-L393, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies that the expression evaluator correctly handles operator precedence ($\text{NOT} > \text{AND} > \text{OR}$) and respects explicit parentheses when evaluating boolean logic expressions against a provided context. It asserts expected outcomes for various combinations of symbolic operators like `&`, `|`, and `!`.*


### test_length_operations (method, L395-L455, parent: TestContextExpressionNewSyntax)

> *Summary: This test verifies that `ContextExpression` correctly evaluates length operations (`len()`) across various Python collections like lists, strings, and dictionaries. It uses a predefined context containing different data structures to assert expected boolean outcomes for comparisons and logical combinations involving lengths.*

