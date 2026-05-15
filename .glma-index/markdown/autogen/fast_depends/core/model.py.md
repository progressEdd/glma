# autogen/fast_depends/core/model.py

1 function(s): _sort_dep. 2 class(es): ResponseModel, CallModel. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ResponseModel | class |  |
| CallModel | class |  |
| _sort_dep | function |  |

## Chunks

### ResponseModel (class, L42-L43)

> *Summary: This class serves as a generic container for API responses, holding a single payload of type `T`. It inherits from `BaseModel` to provide structured data validation.*


### CallModel (class, L46-L500)

> *Summary: This class defines a model for representing and resolving function calls, managing dependencies, argument binding (positional/keyword), caching, and optional data casting. It provides synchronous (`solve`) and asynchronous (`asolve`) methods to execute the wrapped call after recursively solving all its required inputs.*


### call_name (method, L90-L92, parent: CallModel)

> *Summary: Retrieves the name of the method associated with the object's `call` attribute by unwrapping it and returning its `__name__` or class name if not available. This provides a string representation of the function being called.*


### flat_params (method, L95-L99, parent: CallModel)

> *Summary: Aggregates parameters from the current object and all its direct and extra dependencies. It returns a dictionary mapping parameter names to their corresponding values across the dependency chain.*


### flat_dependencies (method, L102-L129, parent: CallModel)

> *Summary: Aggregates all direct and transitive dependencies from the model's dependency list and extra dependencies into a single dictionary. The output maps each callable function to a tuple containing its corresponding `CallModel` instance and a tuple of its immediate dependent callables.*


### __init__ (method, L131-L180, parent: CallModel)

> *Summary: Initializes a model instance by storing the callable function and optional configuration parameters like response models, caching settings, and argument definitions. It processes dependencies to establish a sorted execution order and cleans up input parameters based on defined fields.*


### _solve (method, L182-L288, parent: CallModel)

> *Summary: This method resolves the arguments for a dependency call by merging positional and keyword arguments from inputs, applying overrides if present, and optionally casting results through a model. It yields intermediate states of resolved arguments before finally executing the underlying callable with the determined parameters and returning its result.*


### _cast_response (method, L290-L294, parent: CallModel)

> *Summary: If a response model is defined, it transforms the input `value` into an instance of that model and returns its internal `response`. Otherwise, it passes the input `value` through unchanged.*


### solve (method, L296-L385, parent: CallModel)

> *Summary: This method resolves a dependency by first checking the cache; if not found, it recursively solves all required and extra dependencies. It then executes the core logic using the resolved arguments and returns the final computed value or an iterable of values based on its configuration.*


### asolve (method, L387-L500, parent: CallModel)

> *Summary: This method recursively resolves a dependency by first checking the cache and then concurrently solving its required dependencies and extra fields. It ultimately executes the core logic using the resolved arguments and returns the final computed value or result from the generator if applicable.*


### _sort_dep (function, L503-L533)

> *Summary: This function recursively sorts a dependency model by inserting it into a collector list based on the positions of its dependencies. It traverses the provided call models and uses the existing order in `collector` to determine the correct insertion point for the current model.*

