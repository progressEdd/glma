# test/fast_depends/sync/test_depends.py

21 function(s): test_depends, test_empty_main_body, test_depends_error, test_depends_response_cast, test_depends_annotated, test_depends_annotated_str, test_depends_annotated_str_partial, test_cache, test_not_cache, test_yield and 11 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_depends | function |  |
| test_empty_main_body | function |  |
| test_depends_error | function |  |
| test_depends_response_cast | function |  |
| test_depends_annotated | function |  |
| test_depends_annotated_str | function |  |
| test_depends_annotated_str_partial | function |  |
| test_cache | function |  |
| test_not_cache | function |  |
| test_yield | function |  |
| test_class_depends | function |  |
| test_callable_class_depends | function |  |
| test_not_cast | function |  |
| test_not_cast_main | function |  |
| test_extra | function |  |
| test_async_extra | function |  |
| test_async_depends | function |  |
| test_generator | function |  |
| test_partial | function |  |
| test_default_key_value | function |  |
| test_contextmanager | function |  |

## Chunks

### test_depends (function, L21-L30)

> *Summary: This test verifies dependency injection by calling `some_func`, which requires an input derived from `dep_func`. The function expects a string for its first argument and asserts that the result of `some_func` equals 7.*


### test_empty_main_body (function, L33-L42)

> *Summary: This test verifies dependency injection when the main function body is empty or minimal. It calls `some_func` with a string input, expecting the injected dependency (`dep_func`) to process it and return a float value of $1.0$.*


### test_depends_error (function, L45-L58)

> *Summary: This test verifies that dependency injection fails when the provided arguments do not match the expected types of the dependent functions. It asserts a `ValidationError` occurs when calling `some_func` with an incorrect input type for its dependencies.*


### test_depends_response_cast (function, L61-L70)

> *Summary: This test verifies that dependency injection correctly casts input types when using `Depends`. It calls a function expecting integer inputs but provides string arguments, asserting the injected dependency resolves and returns an integer.*


### test_depends_annotated (function, L73-L89)

> *Summary: This test verifies dependency injection functionality by defining functions that rely on an annotated dependency derived from `dep_func`. It asserts correct execution and type handling when calling injected functions with various inputs.*


### test_depends_annotated_str (function, L93-L114)

> *Summary: This test verifies dependency injection with annotated types by calling functions that expect arguments derived from other dependencies. It asserts correct execution and type handling when injecting values via `Depends(dep_func)`.*


### test_depends_annotated_str_partial (function, L117-L138)

> *Summary: This test verifies dependency injection with `Annotated` types, ensuring that a function parameter annotated with `Depends(dep_func)` correctly receives the return value of the dependency function. It asserts that both injected functions execute successfully using string inputs which are implicitly cast to integers for calculation.*


### test_cache (function, L141-L160)

> *Summary: This test verifies dependency injection behavior by setting up nested dependencies where the inner function's call is expected to be triggered exactly once when the outer function executes. It asserts that two different dependency resolutions ultimately point to the same underlying mocked function instance.*


### test_not_cache (function, L163-L182)

> *Summary: This test verifies that dependencies are re-evaluated when `use_cache=False` is explicitly set for all involved functions. It asserts that the mocked function is called twice, once for each dependency injection point.*


### test_yield (function, L185-L201)

> *Summary: This test verifies dependency injection behavior when the dependency function uses `yield`. It asserts that the mocked dependency is called before execution and that its exit method is called after the dependent function completes.*


### test_class_depends (function, L204-L215)

> *Summary: This test verifies dependency injection by creating a mock class (`MyDep`) and asserting that a decorated function correctly receives an instance of this dependency with the expected internal state. It calls the injected function, passing `3` as an argument to trigger the dependency resolution.*


### test_callable_class_depends (function, L218-L231)

> *Summary: This test verifies dependency injection when the dependency is an instance of a callable class. It injects an instance of `MyDep` (initialized with 3) into `some_func`, asserting that the injected value matches the expected initialization parameter.*


### test_not_cast (function, L234-L255)

> *Summary: This test verifies that dependency injection correctly resolves and passes objects when `cast=False` is specified for dependencies. It asserts that the injected values match expected states without attempting type casting during resolution.*


### test_not_cast_main (function, L259-L280)

> *Summary: This test verifies that dependency injection functions correctly when explicitly disabling type casting for dependencies. It calls `some_func` with an input and asserts the behavior of injected values, ensuring the provided objects are used as-is.*


### test_extra (function, L283-L295)

> *Summary: This test verifies dependency injection when extra dependencies are provided. It injects a mock object into `some_func` via an injected function (`dep`) and asserts that the mocked methods were called exactly once during execution.*


### test_async_extra (function, L298-L308)

> *Summary: This test verifies that when an asynchronous dependency is provided via `extra_dependencies`, the system correctly raises an `AssertionError` if the dependent function attempts to call a synchronous method on the mocked object. It uses `pytest.raises` to assert this failure condition during execution.*


### test_async_depends (function, L311-L319)

> *Summary: This test verifies that dependency injection fails when an asynchronous function is used as a dependency within a synchronous endpoint. It asserts that calling the decorated function raises an `AssertionError` due to this type mismatch.*


### test_generator (function, L322-L340)

> *Summary: This test verifies dependency injection behavior when the dependency function is a generator. It asserts that the mocked start method is called before yielding values, and the end method is only called after all yielded values have been consumed.*


### test_partial (function, L343-L351)

> *Summary: This test verifies that dependency injection correctly handles partial application. It asserts that a function receiving an argument derived from a partially applied dependency returns the expected fixed value (10).*


### test_default_key_value (function, L355-L363)

> *Summary: This test verifies that the default value provided by a dependency function is correctly injected into the consuming function. It asserts that calling the decorated function returns the expected default string value, `"a"`.*


### test_contextmanager (function, L366-L376)

> *Summary: This test verifies dependency injection within a context manager. It defines a simple dependency function and uses it to provide an argument to a generator-based function, asserting the yielded boolean result.*

