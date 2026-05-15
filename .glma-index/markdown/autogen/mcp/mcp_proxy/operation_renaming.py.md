# autogen/mcp/mcp_proxy/operation_renaming.py

3 function(s): validate_function_name, get_new_function_name, custom_visitor.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| validate_function_name | function |  |
| get_new_function_name | function |  |
| custom_visitor | function |  |

## Chunks

### validate_function_name (function, L30-L42)

> *Summary: Checks if a provided string adheres to length, lowercase snake\_case formatting, and uniqueness against a list of existing names. It returns `"exit"` upon successful validation or an informative error message otherwise.*


### get_new_function_name (function, L45-L85)

> *Summary: This function uses an AI agent to suggest a new, unique name for an OpenAPI operation based on its details and a list of already used names. It iteratively prompts the agent until a validated name is returned, which is then logged and outputted as a string.*


### custom_visitor (function, L88-L107)

> *Summary: Iterates through sorted API operations from a parser instance to check and potentially rename function names exceeding 64 characters using a helper function. It returns a dictionary containing the modified list of operations, ensuring unique names are tracked during the process.*

