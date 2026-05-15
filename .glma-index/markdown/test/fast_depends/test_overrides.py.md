# test/fast_depends/test_overrides.py

7 function(s): provider, test_not_override, test_sync_override, test_override_context, test_sync_by_async_override, test_async_override, test_async_by_sync_override.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| provider | function |  |
| test_not_override | function |  |
| test_sync_override | function |  |
| test_override_context | function |  |
| test_sync_by_async_override | function |  |
| test_async_override | function |  |
| test_async_by_sync_override | function |  |

## Chunks

### provider (function, L16-L18)

> *Summary: This function yields a pre-existing dependency provider and then clears it afterward. It serves to manage the lifecycle of the `dependency_provider` within its execution context.*


### test_not_override (function, L21-L34)

> *Summary: This test verifies that dependency injection correctly uses the original implementation when no overrides are provided. It calls a function dependent on `base_dep`, asserting the returned value is 1 and confirming the mock's original method was called exactly once.*


### test_sync_override (function, L37-L57)

> *Summary: This test verifies that a dependency override correctly substitutes the original implementation with a custom one during function execution. It asserts that the injected function receives the value from the overridden dependency and confirms the override mechanism was invoked exactly once.*


### test_override_context (function, L60-L74)

> *Summary: This test verifies dependency overriding by first executing a function that uses an overridden dependency to return `2`, and then asserts the same function returns its original value of `1` after the scope exits. It demonstrates how context-based providers can temporarily substitute dependencies during execution.*


### test_sync_by_async_override (function, L77-L91)

> *Summary: This test verifies that when an asynchronous override is set for a dependency, attempting to inject it into a synchronous function raises an `AssertionError`. It sets up a provider with a base synchronous dependency and an async override before calling the decorated function.*


### test_async_override (function, L95-L115)

> *Summary: This test verifies that an asynchronous dependency override correctly substitutes the original implementation with a mocked version during function execution. It asserts that the injected function receives the value from the overridden dependency and confirms the mocking methods were called as expected.*


### test_async_by_sync_override (function, L119-L139)

> *Summary: This test verifies that an asynchronous dependency can be overridden by a synchronous one. It sets up a provider to swap out an async function returning 1 for a sync function returning 2, then asserts the injected function receives the overridden value of 2.*

