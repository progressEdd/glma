# test/fast_depends/async/test_depends.py

25 function(s): test_depends, test_empty_main_body, test_sync_depends, test_depends_response_cast, test_depends_error, test_depends_annotated, test_async_depends_annotated_str, test_async_depends_annotated_str_partial, test_cache, test_not_cache and 15 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_depends | function |  |
| test_empty_main_body | function |  |
| test_sync_depends | function |  |
| test_depends_response_cast | function |  |
| test_depends_error | function |  |
| test_depends_annotated | function |  |
| test_async_depends_annotated_str | function |  |
| test_async_depends_annotated_str_partial | function |  |
| test_cache | function |  |
| test_not_cache | function |  |
| test_yield | function |  |
| test_sync_yield | function |  |
| test_sync_yield_exception | function |  |
| test_sync_yield_exception_start | function |  |
| test_sync_yield_exception_main | function |  |
| test_class_depends | function |  |
| test_callable_class_depends | function |  |
| test_async_callable_class_depends | function |  |
| test_not_cast | function |  |
| test_not_cast_main | function |  |
| test_extra | function |  |
| test_generator | function |  |
| test_partial | function |  |
| test_default_key_value | function |  |
| test_asynccontextmanager | function |  |

## Chunks

### test_depends (function, L22-L31)

> *Summary: This test verifies dependency injection by calling an asynchronous function that relies on another injected async dependency. It asserts that the result of `some_func` is 7 when provided with the string "2" as input for its first argument.*


### test_empty_main_body (function, L35-L44)

> *Summary: This test verifies dependency injection when the main function body is minimal. It calls `some_func`, which depends on `dep_func` receiving an integer input and returning a float, asserting the injected value matches expectations.*


### test_sync_depends (function, L48-L57)

> *Summary: This test verifies dependency injection for synchronous functions within an asynchronous context. It calls `some_func` with string inputs, expecting the injected synchronous function to process them and return a float result that is then used in the final calculation.*


### test_depends_response_cast (function, L61-L70)

> *Summary: This test verifies that the dependency injection mechanism correctly casts an input string to an integer when used within an asynchronous function. It calls `some_func` with string inputs and asserts the resulting value, implicitly confirming type conversion occurred for the dependency.*


### test_depends_error (function, L74-L87)

> *Summary: This test verifies that dependency injection fails when the provided arguments do not match the expected types for dependent functions. It asserts that calling `some_func` with a string input raises a `ValidationError`.*


### test_depends_annotated (function, L91-L107)

> *Summary: This test verifies dependency injection with type annotations by defining functions that rely on an injected value derived from `dep_func`. It asserts correct execution and return values for both a function requiring two inputs plus the dependency, and one requiring only the dependency.*


### test_async_depends_annotated_str (function, L112-L133)

> *Summary: This test verifies dependency injection for asynchronous functions using `Annotated` types with `Depends`. It calls two injected async functions, passing string inputs which are implicitly converted to integers during execution.*


### test_async_depends_annotated_str_partial (function, L137-L158)

> *Summary: This test verifies dependency injection with `Annotated` and asynchronous functions. It calls two injected async functions, passing string inputs which are implicitly converted to integers for the first function call, and asserts the resulting float outputs.*


### test_cache (function, L162-L178)

> *Summary: This test verifies dependency injection behavior by ensuring that when `some_func` calls its dependencies, the nested function (`nested_dep_func`) is executed exactly once, and the injected values for both arguments are identical. It confirms that the dependency resolution correctly resolves to the same underlying execution context.*


### test_not_cache (function, L182-L201)

> *Summary: This test verifies that dependencies are re-evaluated when `use_cache=False` is explicitly set for all involved functions. It asserts that the mocked function is called twice, confirming that caching was bypassed during execution.*


### test_yield (function, L205-L221)

> *Summary: This test verifies dependency injection with an asynchronous generator function. It asserts that the injected dependency is called upon execution and that its exit method is correctly invoked after the main function completes.*


### test_sync_yield (function, L225-L241)

> *Summary: This test verifies that an asynchronous function correctly handles a synchronous dependency generator (`sync_dep_func`). It asserts that the mock is called upon entry and that `mock.exit()` is eventually called after the yielded value is consumed by the dependent function.*


### test_sync_yield_exception (function, L245-L263)

> *Summary: This test verifies that an asynchronous function correctly propagates an exception raised within a synchronous dependency generator. It asserts that the dependency is called, but its cleanup method (`mock.exit`) is never invoked when an error occurs during execution.*


### test_sync_yield_exception_start (function, L267-L281)

> *Summary: This test verifies that an exception raised by a synchronous dependency function is correctly propagated when awaited within an asynchronous context. It asserts that the main function body does not execute if the dependency fails, ensuring proper short-circuiting behavior.*


### test_sync_yield_exception_main (function, L285-L305)

> *Summary: This test verifies that an exception raised within an asynchronous function correctly triggers the `finally` block of a synchronous dependency generator. It asserts that the mock is called upon entry and exited upon the failure, even when an error occurs during execution.*


### test_class_depends (function, L309-L320)

> *Summary: This test verifies dependency injection by creating a mock class (`MyDep`) and asserting that an asynchronous function correctly receives an instance of this dependency with the expected value. It calls the injected function, passing `3` as input to trigger the dependency resolution.*


### test_callable_class_depends (function, L324-L337)

> *Summary: This test verifies dependency injection for callable classes by defining `MyDep` which implements `__call__`. It then injects an instance of this class into `some_func`, asserting that the injected value matches the initialized input.*


### test_async_callable_class_depends (function, L341-L354)

> *Summary: This test verifies dependency injection for an asynchronous callable class. It injects the result of calling an async method on an instance of `MyDep` into `some_func`, asserting that the returned value matches the initial input parameter.*


### test_not_cast (function, L358-L379)

> *Summary: This test verifies that dependency injection correctly resolves and passes objects when `cast=False` is specified for dependencies. It asserts that the injected values match expected types and content, even without explicit type casting during resolution.*


### test_not_cast_main (function, L384-L405)

> *Summary: This test verifies that dependency injection functions correctly when explicitly told not to cast dependencies. It calls an asynchronous function, providing string input and relying on injected objects (`A` instance and a `logging.Logger`) derived from other async providers.*


### test_extra (function, L409-L425)

> *Summary: This test verifies dependency injection when extra asynchronous and synchronous dependencies are provided to a function. It asserts that the injected mock object, along with its async and sync methods, were all called exactly once during execution.*


### test_generator (function, L429-L455)

> *Summary: This test verifies dependency injection behavior with asynchronous generators and functions. It asserts that the generator dependency is initialized before the main function runs, while the synchronous call dependency executes during iteration, ensuring proper lifecycle management for mocked dependencies.*


### test_partial (function, L459-L467)

> *Summary: This test verifies that dependency injection correctly handles partial application. It asserts that an asynchronous function receives the pre-configured value (10) from a partially applied dependency resolver.*


### test_default_key_value (function, L472-L480)

> *Summary: This test verifies that the default value provided by a dependency function is correctly injected into the main asynchronous function. It asserts that calling `func()` returns the default string `"a"` from its dependency.*


### test_asynccontextmanager (function, L484-L494)

> *Summary: This test verifies that an asynchronous context manager correctly integrates dependency injection. It calls an async function which uses a dependency to check if two input strings are equal, asserting the yielded boolean result is true.*

