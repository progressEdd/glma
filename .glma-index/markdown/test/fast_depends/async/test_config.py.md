# test/fast_depends/async/test_config.py

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

> *Summary: This asynchronous function takes a string input and returns that exact string immediately. It serves as a simple dependency mock for testing purposes.*


### limited_str (function, L20-L20)

> *Summary: This asynchronous function accepts a dependency (`dep`) and likely returns a string or value constrained by that dependency's logic. It serves as a configurable input mechanism within an async context.*


### regular (function, L24-L25)

> *Summary: This asynchronous function accepts an input `a` resolved by a dependency and immediately returns that value. It serves as a simple wrapper to pass through the result of a dependency injection mechanism.*


### test_config (function, L29-L33)

> *Summary: This asynchronous test verifies that a standard string input passes validation while simultaneously asserting that an input to a restricted string validator raises a `ValidationError`. It uses the `regular` and `limited_str` functions for testing different validation behaviors.*

