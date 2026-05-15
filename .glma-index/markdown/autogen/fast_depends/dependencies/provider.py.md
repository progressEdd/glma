# autogen/fast_depends/dependencies/provider.py

1 class(es): Provider. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Provider | class |  |

## Chunks

### Provider (class, L13-L37)

> *Summary: Manages dependency substitution by storing mappings from original callable functions to replacement callables. It allows setting overrides directly or temporarily within a context manager that automatically restores the original mapping upon exiting.*


### __init__ (method, L16-L17, parent: Provider)

> *Summary: Initializes an object to manage dependency overrides by setting up an empty dictionary for storing these overrides. This structure allows the instance to track and modify how dependencies are resolved later in the process.*


### clear (method, L19-L20, parent: Provider)

> *Summary: Resets the internal state by emptying the `dependency_overrides` dictionary. This method ensures a clean slate for dependency management operations.*


### override (method, L22-L27, parent: Provider)

> *Summary: Registers a replacement function for an existing dependency callable within the instance's overrides dictionary. It takes the original and the new callable as inputs to establish this substitution.*


### scope (method, L30-L37, parent: Provider)

> *Summary: This method temporarily swaps a function's implementation with an provided replacement within the current scope. It registers the override before yielding and ensures the original function is restored afterward.*

