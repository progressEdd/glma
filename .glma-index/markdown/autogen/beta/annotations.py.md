# autogen/beta/annotations.py

3 class(es): Inject, Variable, ContextField. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Inject | class |  |
| Variable | class |  |
| ContextField | class |  |

## Chunks

### Inject (class, L15-L45)

> *Summary: This class acts as a custom field wrapper to inject values into function arguments based on context dependencies. It accepts configuration for naming, default values, and factory functions, returning the modified keyword arguments dictionary after resolving any necessary injections.*


### __init__ (method, L18-L32, parent: Inject)

> *Summary: Initializes an annotation object by storing a name and optional default values or factory functions. It then passes these settings to the parent class, determining if the field is required based on whether a default was provided.*


### use (method, L34-L45, parent: Inject)

> *Summary: This method modifies keyword arguments based on a provided context, injecting default or dependency-resolved values for the parameter if they are available in the context's dependencies. It returns the updated dictionary of keyword arguments.*


### Variable (class, L48-L78)

> *Summary: Represents a configurable parameter that can be injected into function calls based on context variables or provided defaults/factories. It accepts optional `real_name`, `default`, and `default_factory` to determine the value assigned to its internal `param_name`.*


### __init__ (method, L51-L65, parent: Variable)

> *Summary: Initializes an annotation object by storing a name and optional default values (either a static value or a factory function). It then calls the parent constructor, setting whether the field is required based on the presence of a provided default.*


### use (method, L67-L78, parent: Variable)

> *Summary: This method modifies keyword arguments by injecting values for the annotated parameter if a context is provided. It prioritizes using existing variables from the context, then sets defaults or calls default factories within the context's variables dictionary before returning the updated arguments.*


### ContextField (class, L81-L87)

> *Summary: This class modifies input arguments by injecting a context value if provided via `CONTEXT_OPTION_NAME`. It ensures the field has a defined parameter name before overwriting that parameter with the retrieved context.*


### use (method, L82-L87, parent: ContextField)

> *Summary: This method conditionally injects a context value from `kwargs` into the instance's parameter name if the context option is provided. It returns the modified keyword arguments dictionary, ensuring the context is correctly associated with the relevant parameter.*

