# test/fast_depends/sync/test_cast.py

21 function(s): test_not_annotated, test_annotated_partial, test_arbitrary_args, test_arbitrary_response, test_validation_error, test_types_casting, test_types_casting_from_str, test_pydantic_types_casting, test_pydantic_field_types_casting, test_wrong_incoming_types and 11 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_not_annotated | function |  |
| test_annotated_partial | function |  |
| test_arbitrary_args | function |  |
| test_arbitrary_response | function |  |
| test_validation_error | function |  |
| test_types_casting | function |  |
| test_types_casting_from_str | function |  |
| test_pydantic_types_casting | function |  |
| test_pydantic_field_types_casting | function |  |
| test_wrong_incoming_types | function |  |
| test_wrong_return_types | function |  |
| test_annotated | function |  |
| test_args_kwargs_1 | function |  |
| test_args_kwargs_2 | function |  |
| test_args_kwargs_3 | function |  |
| test_generator | function |  |
| test_generator_iterator_type | function |  |
| test_multi_annotated | function |  |
| test_var_keyword_with_named_positional_or_keyword_args | function |  |
| test_var_keyword_only_extras | function |  |
| test_var_keyword_with_positional_call | function |  |

## Chunks

### test_not_annotated (function, L19-L24)

> *Summary: This test verifies that an injected function, when called with string inputs, returns a string even without explicit type annotations. It asserts the return type of `some_func("1", "2")` is `str`.*


### test_annotated_partial (function, L27-L33)

> *Summary: This test verifies that an injected function correctly handles type coercion when provided with incorrect input types. It asserts that calling the decorated function with a string where an integer is expected still results in an integer output after implicit conversion.*


### test_arbitrary_args (function, L36-L45)

> *Summary: This test verifies that a function annotated with `@inject` correctly accepts and returns an instance of a custom class type. It passes an `ArbitraryType` object to the decorated function and asserts the return value is of the same type.*


### test_arbitrary_response (function, L48-L57)

> *Summary: This test verifies that a function accepting an arbitrary custom type correctly returns an instance of that same type. It demonstrates the system's ability to handle and propagate non-standard object types through dependency injection.*


### test_validation_error (function, L60-L69)

> *Summary: This test verifies that a function expecting a string input with a maximum length of one raises a `ValidationError` when provided an invalid value (e.g., a non-string or a string exceeding the limit). It confirms proper validation enforcement for field constraints.*


### test_types_casting (function, L72-L81)

> *Summary: This test verifies that the function correctly handles type casting when provided string inputs for integer parameters. It asserts that calling the decorated function with strings `"1"` and `"2"` results in a `float` return value.*


### test_types_casting_from_str (function, L84-L89)

> *Summary: This test verifies that a function annotated to accept an integer can correctly process and return a `float` when provided with a string input like `"1"`. It confirms the system's ability to cast string representations of numbers into the expected numeric types.*


### test_pydantic_types_casting (function, L92-L100)

> *Summary: This test verifies that Pydantic correctly casts string inputs to the expected integer type when initializing a model instance passed to a function. It asserts that the return value from the injected function is an `int`.*


### test_pydantic_field_types_casting (function, L103-L115)

> *Summary: This test verifies that Pydantic correctly casts input values when using field aliases. It asserts that functions accepting aliased inputs, one expecting an integer and the other a string, successfully process a string input ("2") and return a `float`.*


### test_wrong_incoming_types (function, L118-L124)

> *Summary: This test verifies that the system correctly raises a `ValidationError` when an input argument, expected to be an integer, is provided as a set. It confirms type checking enforcement for function arguments.*


### test_wrong_return_types (function, L127-L133)

> *Summary: Asserts that calling a function expecting an integer input with a string will raise a `ValidationError`. This tests the type checking mechanism when incorrect data types are provided to the decorated function.*


### test_annotated (function, L136-L144)

> *Summary: This test verifies that an annotated type hint, specifically one using `Annotated` with a field alias, is correctly handled by the injection mechanism. It asserts that calling a decorated function with input matching the aliased parameter results in the expected return type.*


### test_args_kwargs_1 (function, L147-L157)

> *Summary: This test verifies argument and keyword handling for a function expecting positional arguments (`a`, `b`) and variable arguments/keywords (`*args`, `**kwargs`). It asserts that the function correctly parses mixed inputs (like floats passed as integers) into the expected tuple structure.*


### test_args_kwargs_2 (function, L160-L174)

> *Summary: This test verifies argument and keyword handling for a function expecting positional arguments (`a`, `*args`) and a keyword-only argument (`b`). It asserts that the function correctly processes mixed inputs, returning the expected tuple containing the integer value of `a`, the tuple of floats from `*args`, and the integer value of `b`.*


### test_args_kwargs_3 (function, L177-L185)

> *Summary: This test verifies that a function accepting positional and keyword-only arguments correctly handles type coercion when inputs are provided as floats but expected as integers. It asserts the return tuple matches the coerced integer values from the input float arguments.*


### test_generator (function, L188-L195)

> *Summary: This test verifies that a generator function, which yields the input string converted to an integer twice, produces the expected sequence of integer outputs. It calls `simple_func` with `"1"` and asserts that the yielded values are both equal to `1`.*


### test_generator_iterator_type (function, L198-L205)

> *Summary: Verifies that a function returning an iterator yields the expected sequence of values. It calls `simple_func` with a string input and asserts that the resulting iteration produces integers, specifically checking for the value `1`.*


### test_multi_annotated (function, L209-L219)

> *Summary: This test verifies that Pydantic correctly applies multiple validation constraints, including range checks and custom post-processing via `AfterValidator`. It asserts that input values failing the initial constraint raise a `ValidationError`, while valid inputs are transformed according to all specified validators.*


### test_var_keyword_with_named_positional_or_keyword_args (function, L222-L237)

> *Summary: Verifies that a function accepting positional/keyword arguments and `**kwargs` correctly routes explicitly named keyword arguments to their designated slots rather than bundling them all into the catch-all dictionary. It confirms that specific inputs like `"A"` and `"B"` are assigned to `arg1` and `arg2`, while extra keywords populate `kwargs`.*


### test_var_keyword_only_extras (function, L240-L247)

> *Summary: This test verifies that when a function accepts only `**kwargs`, all provided keyword arguments are correctly captured and returned as a dictionary. It asserts that calling the decorated function with named arguments results in those arguments being present in the output dictionary.*


### test_var_keyword_with_positional_call (function, L250-L260)

> *Summary: This test verifies that positional arguments passed to a function are correctly received alongside keyword arguments collected in `**kwargs`. It calls the decorated function with both positional and keyword inputs and asserts the returned values match the provided inputs.*

