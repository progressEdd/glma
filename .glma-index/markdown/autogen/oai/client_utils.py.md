# autogen/oai/client_utils.py

3 function(s): validate_parameter, merge_config_with_tools, should_hide_tools. 1 class(es): FormatterProtocol. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FormatterProtocol | class |  |
| validate_parameter | function |  |
| merge_config_with_tools | function |  |
| should_hide_tools | function |  |

## Chunks

### FormatterProtocol (class, L15-L18)

> *Summary: Defines a protocol requiring any implementing class to provide a `format` method that returns a string. This enforces a standardized way for structured output objects to serialize themselves into a readable string representation.*


### format (method, L18-L18, parent: FormatterProtocol)

> *Summary: This method serializes the object's internal state into a string representation. It is called on an instance to produce a formatted output string.*


### validate_parameter (function, L21-L110)

> *Summary: This function validates a configuration parameter from an input dictionary against specified constraints like allowed types, value lists, and numerical bounds. It returns the validated value or falls back to a provided default if any validation rule is violated, issuing a warning upon failure.*


### merge_config_with_tools (function, L113-L137)

> *Summary: Combines two configuration dictionaries, prioritizing client-specific settings while intelligently merging tool definitions. It ensures that the final configuration includes merged tools only if they exist and the deprecated `functions` parameter is absent.*


### should_hide_tools (function, L140-L190)

> *Summary: Determines whether to suppress tool options based on the conversation history and a specified parameter. It checks if any tools have been invoked (`if_any_run`) or if every available tool has been called at least once (`if_all_run`), returning `True` if hiding is required.*

