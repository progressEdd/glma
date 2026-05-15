# test/beta/config/ollama/tools/test_tool_to_api.py

2 function(s): test_tool_to_api, test_tool_to_api_parameterless.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_tool_to_api | function |  |
| test_tool_to_api_parameterless | function |  |

## Chunks

### test_tool_to_api (function, L9-L26)

> *Summary: This test verifies that a provided tool schema is correctly transformed into an OpenAI-compatible API function definition. It asserts the resulting structure matches a predefined dictionary containing the function name, description, and parameter definitions for searching documentation.*


### test_tool_to_api_parameterless (function, L29-L35)

> *Summary: This test verifies that converting a parameterless tool schema into an API definition results in a function object with empty parameters. It asserts the structure of the resulting `parameters` field within the API tool definition.*

