# autogen/beta/tools/final/function_tool.py

4 function(s): tool, tool, tool, _wrap_middleware. 3 class(es): FunctionDefinition, FunctionToolSchema, FunctionTool. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FunctionDefinition | class |  |
| FunctionToolSchema | class |  |
| FunctionTool | class |  |
| tool | function |  |
| tool | function |  |
| tool | function |  |
| _wrap_middleware | function |  |

## Chunks

### FunctionDefinition (class, L26-L32)

> *Summary: Represents a structured definition for a callable function, holding its name, description, and associated parameters. It ensures that the "title" key is removed from the parameter dictionary upon initialization.*


### __post_init__ (method, L31-L32, parent: FunctionDefinition)

> *Summary: After initialization, this method removes the "title" key from the instance's parameters dictionary. This ensures that the title attribute is not present in the final configuration passed to the tool.*


### FunctionToolSchema (class, L36-L43)

> *Summary: This schema defines a tool specifically for function calling, encapsulating a `FunctionDefinition`. It provides a class method to instantiate itself from a dictionary containing the necessary function details.*


### from_dict (method, L41-L43, parent: FunctionToolSchema)

> *Summary: Constructs a `FunctionToolSchema` instance by extracting function details from an input dictionary. It uses the provided dictionary to initialize a nested `FunctionDefinition`.*


### FunctionTool (class, L46-L135)

> *Summary: This class encapsulates a callable function as an executable tool, taking a model, name, schema, and optional middleware upon initialization. It allows configuration via `with_middleware` and executes the underlying logic by calling its associated model asynchronously when invoked with a `ToolCallEvent`.*


### __init__ (method, L55-L76, parent: FunctionTool)

> *Summary: Initializes a tool by setting the underlying model and applying middleware to it. It constructs a structured schema using provided function details (name, description, parameters) for external use.*


### with_middleware (method, L78-L85, parent: FunctionTool)

> *Summary: Creates and returns a copy of the current tool, augmenting its middleware stack by prepending any provided middleware layers to the existing ones. This ensures the original tool instance remains unmodified.*


### schemas (method, L87-L88, parent: FunctionTool)

> *Summary: Returns a list containing the tool's schema based on the provided execution context. This allows external systems to understand the structure and capabilities of the function tool.*


### set_provider (method, L90-L91, parent: FunctionTool)

> *Summary: Assigns a specific `Provider` object to the instance's internal state. This method updates which service or data source the class will utilize for subsequent operations.*


### ensure_tool (method, L94-L101, parent: FunctionTool)

> *Summary: This method wraps a given function or existing `Tool` instance to ensure it conforms to the `Tool` interface. It creates a copy if the input is already a `Tool`, converts a callable into one, and then sets an optional provider on the resulting tool object before returning it.*


### register (method, L103-L120, parent: FunctionTool)

> *Summary: This method wraps the tool's core execution logic with a chain of provided and internal middleware hooks. It then registers an asynchronous handler within the context's streaming scope to intercept specific `ToolCallEvent`s, execute the wrapped logic, and send the result back through the context.*


### __call__ (method, L122-L135, parent: FunctionTool)

> *Summary: This method executes the underlying model using arguments from a `ToolCallEvent` and the provided `Context`. It returns a `ToolResultEvent` upon success or a `ToolErrorEvent` if any exception occurs during execution.*


### tool (function, L139-L147)

> *Summary: Creates a `FunctionTool` wrapper around an arbitrary callable function. It accepts the function itself along with optional metadata like name, description, and schema, and configures execution behavior such as threading and middleware.*


### tool (function, L151-L159)

> *Summary: This function creates a `FunctionTool` wrapper around an existing callable. It accepts optional metadata like name, description, and schema, and allows configuration for synchronous execution and middleware chaining. The output is a configured tool object ready for use in agent workflows.*


### tool (function, L162-L192)

> *Summary: This utility creates a wrapper for functions to expose them as callable tools. It accepts an optional function and configuration parameters like name, description, and schema, returning either the configured `FunctionTool` instance or a factory function that produces it when given a target function.*


### _wrap_middleware (function, L195-L199)

> *Summary: This function wraps an execution handler to inject middleware functionality. It returns a new asynchronous callable that executes the inner tool logic after passing through the provided `hook`.*

