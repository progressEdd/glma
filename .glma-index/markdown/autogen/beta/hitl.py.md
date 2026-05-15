# autogen/beta/hitl.py

2 function(s): wrap_hitl, default_hitl_hook.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| wrap_hitl | function |  |
| default_hitl_hook | function |  |

## Chunks

### wrap_hitl (function, L26-L53)

> *Summary: This function returns a hook creator that wraps a given human interaction logic with an iterable of middleware. It constructs and chains middlewares to modify the input request before it is executed by the underlying model call, ultimately producing a callable execution handler.*


### default_hitl_hook (function, L56-L60)

> *Summary: This function returns an asynchronous handler that immediately raises a `HumanInputNotProvidedError` when called. It serves as a default hook for handling human-in-the-loop requests, effectively blocking execution until explicit input is provided.*

