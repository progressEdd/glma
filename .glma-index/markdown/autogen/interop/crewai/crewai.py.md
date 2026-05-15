# autogen/interop/crewai/crewai.py

1 function(s): _sanitize_name. 1 class(es): CrewAIInteroperability. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _sanitize_name | function |  |
| CrewAIInteroperability | class |  |

## Chunks

### _sanitize_name (function, L18-L19)

> *Summary: This function cleans a string by replacing any non-word characters or leading digits with an underscore. It ensures the input string is suitable for use as a valid identifier.*


### CrewAIInteroperability (class, L28-L94)

> *Summary: This class provides a static method to convert an instance of a `CrewAITool` into a standardized `Tool` object. It sanitizes the tool's name and description, wraps the original execution logic in a callable function, and returns the resulting interoperable `Tool`.*


### convert_tool (method, L37-L81, parent: CrewAIInteroperability)

> *Summary: Transforms a `CrewAITool` instance into a standardized `Tool` object by sanitizing the name and augmenting the description. It wraps the tool's execution logic within a callable function that accepts arguments matching the tool's schema.*


### get_unsupported_reason (method, L84-L94, parent: CrewAIInteroperability)

> *Summary: Checks the current Python version against supported ranges and attempts to import a specific submodule. It returns an error string if the Python version is unsupported or if the required optional dependency fails to load, otherwise it returns `None`.*

