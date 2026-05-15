# test/fast_depends/sync/test_config.py

4 function(s): dep, limited_str, regular, test_config.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| dep | function |  |
| limited_str | function |  |
| regular | function |  |
| test_config | function |  |

## Chunks

### dep (function, L15-L16)

> *Summary: This function takes a string input and returns that exact string unchanged, acting as an identity mapping for dependency testing.*


### limited_str (function, L20-L20)

> *Summary: This function wraps a dependency, accepting an optional argument `a` that is resolved via the provided `dep`. It likely limits or processes the input value based on the dependency's resolution.*


### regular (function, L24-L25)

> *Summary: This function acts as a simple dependency resolver, accepting an input `a` derived from a specified dependency (`dep`) and returning that same value. It essentially passes through the resolved dependency into its return value.*


### test_config (function, L28-L32)

> *Summary: This test verifies that a standard string input passes validation, while an input to the `limited_str` function correctly raises a `ValidationError`. It confirms the expected behavior for both regular and constrained string inputs.*

