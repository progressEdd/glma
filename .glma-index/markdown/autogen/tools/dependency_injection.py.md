# autogen/tools/dependency_injection.py

11 function(s): on, Depends, get_context_params, _is_context_param, _is_depends_param, remove_params, _remove_injected_params_from_signature, _string_metadata_to_description_field, _fix_staticmethod, _set_return_annotation_to_any and 1 more. 3 class(es): BaseContext, ChatContext, Field. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BaseContext | class |  |
| ChatContext | class |  |
| on | function |  |
| Depends | function |  |
| get_context_params | function |  |
| _is_context_param | function |  |
| _is_depends_param | function |  |
| remove_params | function |  |
| _remove_injected_params_from_signature | function |  |
| Field | class |  |
| _string_metadata_to_description_field | function |  |
| _fix_staticmethod | function |  |
| _set_return_annotation_to_any | function |  |
| inject_params | function |  |

## Chunks

### BaseContext (class, L36-L43)

> *Summary: Provides an abstract foundation for specialized context objects within the application. It acts as a parent interface, requiring subclasses to define their specific context behaviors.*


### ChatContext (class, L47-L78)

> *Summary: Represents a conversational state by wrapping an agent instance to manage chat history. It provides read-only access to all stored messages and retrieves the most recent message from the underlying agent.*


### __init__ (method, L54-L60, parent: ChatContext)

> *Summary: This constructor accepts a `ConversableAgent` instance and stores it internally as the primary agent reference. It sets up the context by associating this specific agent with the object's state.*


### chat_messages (method, L63-L69, parent: ChatContext)

> *Summary: Retrieves all conversation history from an agent object. It returns a dictionary mapping each participating agent to a list of their respective message dictionaries.*


### last_message (method, L72-L78, parent: ChatContext)

> *Summary: Retrieves and returns the most recent message from the underlying agent's state. It acts as a simple accessor to expose the latest communication within the system.*


### on (function, L84-L88)

> *Summary: This function creates and returns a zero-argument callable that captures the provided value. When invoked, this returned function simply returns the captured input value.*


### Depends (function, L92-L104)

> *Summary: This utility wraps a given context or dependency into a `FastDepends` object. It returns a callable wrapper that resolves the specified dependency when needed for injection.*


### get_context_params (function, L107-L118)

> *Summary: Inspects a function's signature to identify and return the names of parameters that match a specified context type. It takes a callable function and a context class as input, yielding a list of matching parameter names.*


### _is_context_param (function, L121-L127)

> *Summary: Checks if a given parameter's annotation represents a subtype of a specified context class. It handles complex annotations like `Annotated` to determine if the parameter depends on a relevant context object.*


### _is_depends_param (function, L130-L135)

> *Summary: Checks if a given parameter is marked as a dependency by inspecting its default value or metadata annotation. Returns `True` if the parameter explicitly depends on another service via `model.Depends`.*


### remove_params (function, L138-L140)

> *Summary: Modifies a callable's signature by removing specified parameters from its existing `inspect.Signature`. It updates the function object directly to reflect the reduced parameter list for introspection purposes.*


### _remove_injected_params_from_signature (function, L143-L148)

> *Summary: This utility modifies a function's signature by removing parameters identified as context or dependency injection targets. It takes a callable and returns a new version of that callable with the specified parameters stripped out.*


### Field (class, L151-L168)

> *Summary: Stores a descriptive string associated with an annotated field, allowing metadata to be attached to types. It is initialized with a `description` string and exposes it via a read-only property.*


### __init__ (method, L158-L164, parent: Field)

> *Summary: This constructor initializes an object by storing a provided string as its internal description attribute. It accepts one argument, `description`, which sets the metadata for the instance.*


### description (method, L167-L168, parent: Field)

> *Summary: Returns a string containing the object's descriptive text, which is stored internally as `self._description`. This method provides a human-readable summary of the dependency injection configuration.*


### _string_metadata_to_description_field (function, L171-L188)

> *Summary: This function modifies a callable by inspecting its type hints to convert string-based metadata into structured `Field` objects. It iterates through annotations and their arguments, replacing simple string descriptions with richer field definitions if the necessary metadata is present.*


### _fix_staticmethod (function, L191-L202)

> *Summary: This utility function modifies a `staticmethod` object in Python 3.9+ to ensure its underlying callable is correctly invoked, specifically when accessing `staticmethod.__func__`. It returns the original or wrapped callable based on this version-specific check.*


### _set_return_annotation_to_any (function, L205-L227)

> *Summary: This utility wraps a given callable, preserving its original structure while explicitly overriding its return type annotation to `Any`. It handles both synchronous and asynchronous functions by creating the appropriate wrapper before modifying the signature's return type.*


### inject_params (function, L230-L249)

> *Summary: This utility wraps a given function to automatically inject dependencies and then cleans up the resulting signature by removing those injected parameters. It returns a new, decorated callable that behaves like the original but now has its required dependencies supplied externally.*

