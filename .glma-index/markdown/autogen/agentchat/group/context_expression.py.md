# autogen/agentchat/group/context_expression.py

1 class(es): ContextExpression. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ContextExpression | class |  |

## Chunks

### ContextExpression (class, L15-L231)

> *Summary: This class parses and validates a string containing logical expressions that reference context variables (e.g., `${var}`). It converts the symbolic syntax into safe Python code, ensuring only allowed operations like comparisons and `len()` calls are present. The `evaluate` method then substitutes variable values from a provided context to compute a final boolean result.*


### __post_init__ (method, L41-L65, parent: ContextExpression)

> *Summary: Upon initialization, this method validates an input string expression by extracting variable names, converting symbolic operators to Python syntax, and parsing it using the `ast` module. It ensures the expression is syntactically correct and only contains allowed operations before storing both the AST and the runnable Python version for later use.*


### _extract_variable_names (method, L67-L71, parent: ContextExpression)

> *Summary: This method parses an input string to find and return a list of all variable names enclosed in `${...}` syntax. It uses a regular expression to extract the content within these specific delimiters.*


### _convert_to_python_syntax (method, L73-L98, parent: ContextExpression)

> *Summary: This method transforms a string containing symbolic logical operators into valid Python syntax by substituting symbols like `&`, `|`, and `!` with their keyword equivalents (`and`, `or`, `not`). It safely handles this conversion by temporarily replacing all existing string literals before performing the substitutions, then restoring them afterward.*


### _prepare_for_ast (method, L100-L107, parent: ContextExpression)

> *Summary: Transforms a string expression by substituting template variables (e.g., `${var}`) with their raw names, making the resulting string suitable for Abstract Syntax Tree (AST) parsing. It takes an input expression string and returns a modified string where placeholders are replaced by variable identifiers.*


### _validate_operations (method, L109-L155, parent: ContextExpression)

> *Summary: Recursively traverses an Abstract Syntax Tree (AST) to ensure it only contains a predefined set of allowed operations and structures. It validates specific constraints, such as restricting function calls to `len()` with one argument and limiting comparison operators within `ast.Compare` nodes, raising errors upon finding disallowed elements.*


### evaluate (method, L157-L228, parent: ContextExpression)

> *Summary: This method evaluates a stored Python expression string by substituting placeholders with values from the provided context variables. It first resolves `len()` calls against context values, then replaces remaining variable references with appropriately formatted strings before executing the final expression using `eval()`.*


### __str__ (method, L230-L231, parent: ContextExpression)

> *Summary: Provides a string representation of the context expression object, displaying its internal expression value within parentheses. This is used for debugging and logging purposes.*

