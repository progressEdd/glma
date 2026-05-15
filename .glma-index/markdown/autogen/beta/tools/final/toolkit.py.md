# autogen/beta/tools/final/toolkit.py

1 class(es): Toolkit. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Toolkit | class |  |

## Chunks

### Toolkit (class, L20-L130)

> *Summary: This class aggregates multiple tools, allowing them to be combined using the `|` operator or added via a fluent `tool()` method. It manages tool registration and provides methods to retrieve schemas for execution within a given context.*


### __init__ (method, L27-L38, parent: Toolkit)

> *Summary: Initializes a toolkit by accepting an arbitrary collection of `Tool` objects and optional middleware. It stores these provided tools internally, assigning a name if one is not explicitly given.*


### tools (method, L41-L42, parent: Toolkit)

> *Summary: Returns a tuple containing all the available `Tool` instances stored in the object's internal dictionary. This provides an iterable collection of the tool definitions for external use.*


### set_provider (method, L44-L46, parent: Toolkit)

> *Summary: This method iterates over all internal tools and configures each one to use the specified `Provider` object. It updates the tool's dependency on a particular service provider.*


### _add_tool (method, L48-L54, parent: Toolkit)

> *Summary: This method registers a provided tool, ensuring it's wrapped by existing middleware if necessary. It raises an error if the tool name already exists unless explicitly marked as unsafe.*


### __or__ (method, L56-L63, parent: Toolkit)

> *Summary: This method merges the current toolkit's tools with another input, which can be either another `Toolkit` instance or a single function wrapped as a `FunctionTool`. It returns a new `Toolkit` containing the combined set of tools while preserving the original name and middleware.*


### tool (method, L66-L75, parent: Toolkit)

> *Summary: Creates a structured tool object from a given callable function. It accepts the function along with optional metadata like name, description, and schema, and configures execution behavior such as threading and middleware.*


### tool (method, L78-L87, parent: Toolkit)

> *Summary: This method wraps a given function to create a `FunctionTool` object. It accepts optional parameters like name, description, and schema for the tool's definition, along with configuration for execution threading and middleware.*


### tool (method, L89-L114, parent: Toolkit)

> *Summary: This method acts as a factory for creating tool wrappers. If provided with a callable function, it immediately wraps and registers that function into the instance; otherwise, it returns a higher-order function that accepts a callable to perform the wrapping and registration upon invocation.*


### schemas (method, L116-L120, parent: Toolkit)

> *Summary: Aggregates the schema definitions from all registered tools within a given context. It iterates over `self.tools`, calls each tool's asynchronous `schemas` method, and returns a combined iterable list of `ToolSchema` objects.*


### register (method, L122-L130, parent: Toolkit)

> *Summary: Iterates over the instance's tools and calls a `register` method on each one, passing along an exit stack, context, and optional middleware for setup. This action effectively registers all contained tools within the provided execution environment.*

