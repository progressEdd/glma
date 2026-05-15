# autogen/interop/pydantic_ai/pydantic_ai.py

1 class(es): PydanticAIInteroperability. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| PydanticAIInteroperability | class |  |

## Chunks

### PydanticAIInteroperability (class, L27-L172)

> *Summary: This class provides interoperability between Pydantic AI tools and a generic `Tool` format. It offers methods to convert a `PydanticAITool` into a standard `Tool`, handling context injection and dependency checks, and also includes a utility to wrap the tool's function to manage retries based on a provided execution context.*


### inject_params (method, L39-L94, parent: PydanticAIInteroperability)

> *Summary: This method wraps a provided tool function to automatically inject a run context and manage execution retries based on the tool's configuration. It accepts a context object and the tool instance, returning a new callable that handles parameter injection and raises an error if maximum retries are exceeded.*


### convert_tool (method, L98-L162, parent: PydanticAIInteroperability)

> *Summary: Converts a `PydanticAITool` instance into a standardized `Tool` object by validating the input and handling context dependencies. It ensures required context (`deps`) is present if the tool needs it, then wraps the tool's function using parameter injection before returning the final `Tool`.*


### get_unsupported_reason (method, L165-L172, parent: PydanticAIInteroperability)

> *Summary: Checks if the necessary `pydantic_ai.tools` module is available after attempting an optional import. If the import fails, it returns a string instructing the user to install the required extra dependency; otherwise, it returns `None`.*

