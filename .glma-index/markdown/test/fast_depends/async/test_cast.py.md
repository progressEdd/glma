# test/fast_depends/async/test_cast.py

17 function(s): test_not_annotated, test_annotated_partial, test_arbitrary_args, test_arbitrary_response, test_types_casting, test_types_casting_from_str, test_pydantic_types_casting, test_pydantic_field_types_casting, test_wrong_incoming_types, test_wrong_return_types and 7 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_not_annotated | function |  |
| test_annotated_partial | function |  |
| test_arbitrary_args | function |  |
| test_arbitrary_response | function |  |
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

## Chunks

### test_not_annotated (function, L20-L25)

> *Summary: This test verifies that an injected asynchronous function, lacking type annotations, performs string concatenation when given string inputs. It asserts the return value is of type `str`.*


### test_annotated_partial (function, L29-L35)

> *Summary: This test verifies that an asynchronous function decorated with `@inject` correctly handles type hints. It asserts that calling the injected function with mixed types (an integer and a string representing an integer) results in an integer output after implicit type coercion.*


### test_arbitrary_args (function, L39-L48)

> *Summary: This test verifies that an asynchronous function correctly accepts and returns an instance of a custom class type. It injects an object of `ArbitraryType` into the decorated async function and asserts the return value is of the same type.*


### test_arbitrary_response (function, L52-L61)

> *Summary: This test verifies that an asynchronous function correctly handles and returns an instance of a custom, arbitrary type. It injects an object of `ArbitraryType` into the function and asserts the return value is also of that same type.*


### test_types_casting (function, L65-L74)

> *Summary: This test verifies that string inputs ("1" and "2") passed to an asynchronous function expecting integers are correctly cast to floats upon return. It confirms the function successfully processes the input types despite the initial type hints.*


### test_types_casting_from_str (function, L78-L83)

> *Summary: This asynchronous test verifies that string inputs, like `"1"`, are correctly cast to the expected `float` return type when passed to an injected function. It asserts the resulting value's type after execution.*


### test_pydantic_types_casting (function, L87-L95)

> *Summary: This test verifies that Pydantic correctly casts string inputs to the expected integer type when initializing a model instance passed into an asynchronous function. It asserts that the returned value from the injected function is indeed an `int`.*


### test_pydantic_field_types_casting (function, L99-L111)

> *Summary: This test verifies that Pydantic correctly casts input values when using field aliases. It asserts that functions accepting aliased inputs can successfully process string representations of numbers and strings, returning a `float`.*


### test_wrong_incoming_types (function, L115-L121)

> *Summary: This test verifies that the system correctly raises a `ValidationError` when an asynchronous function expecting an integer receives a set as input. It asserts proper type checking enforcement during execution.*


### test_wrong_return_types (function, L125-L131)

> *Summary: This test verifies that an asynchronous function expecting an integer input will raise a `ValidationError` when provided with a string, ensuring type checking is enforced during execution. It asserts the expected exception occurs when calling the decorated async function with incorrect input types.*


### test_annotated (function, L135-L143)

> *Summary: This test verifies that an annotated type hint, specifically one using `Field` with an alias, correctly receives and processes input data. It asserts that the injected function successfully converts the aliased string input into the expected native Python type (`int`) before returning a `float`.*


### test_args_kwargs_1 (function, L147-L157)

> *Summary: This test verifies argument and keyword handling for an asynchronous function. It calls the decorated function with mixed positional and keyword arguments and asserts that the returned tuple correctly reflects the parsed inputs according to type expectations.*


### test_args_kwargs_2 (function, L161-L175)

> *Summary: This test verifies argument and keyword handling for an asynchronous function that accepts positional arguments (`*args`) and named parameters. It asserts the return value matches the expected tuple structure after calling the function with mixed positional and keyword inputs.*


### test_args_kwargs_3 (function, L179-L187)

> *Summary: This test verifies that type coercion occurs when calling an asynchronous function with mixed positional and keyword arguments. It asserts the return values are correctly cast to integers despite float inputs being provided.*


### test_generator (function, L191-L198)

> *Summary: This asynchronous test verifies that an injected generator function yields the input string converted to an integer twice. It consumes the yielded values and asserts they match the expected integer value.*


### test_generator_iterator_type (function, L202-L209)

> *Summary: This test verifies that an asynchronous generator function correctly yields values when iterated over. It calls `simple_func` with the string "1" and asserts that the resulting iterator produces the integer value 1 twice.*


### test_multi_annotated (function, L214-L224)

> *Summary: This test verifies the behavior of multiple annotations on an input parameter within an asynchronous function. It asserts that providing an invalid value (like `1`) raises a validation error, while a valid input (`10`) correctly passes through both constraints and transformations to return `20`.*

