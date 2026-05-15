# test/beta/config/openai/tools/test_tool_to_api.py

3 function(s): test_tool_to_api, test_tool_to_api_parameterless, test_tool_to_responses_api_parameterless.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_tool_to_api | function |  |
| test_tool_to_api_parameterless | function |  |
| test_tool_to_responses_api_parameterless | function |  |

## Chunks

### test_tool_to_api (function, L9-L27)

> *Summary: This test verifies that a provided tool schema is correctly transformed into the expected OpenAI API function definition structure. It asserts that the resulting dictionary matches a predefined structure containing the function name, description, and parameter definitions for searching documentation.*


### test_tool_to_api_parameterless (function, L30-L37)

> *Summary: This test verifies that converting a parameterless tool schema into an API structure results in a function definition with empty parameters. It asserts the resulting `parameters` object is an empty object structure.*


### test_tool_to_responses_api_parameterless (function, L40-L47)

> *Summary: This test verifies that when a parameterless tool schema is passed to the conversion function, the resulting API structure correctly defines an empty object for its parameters. It asserts that the `parameters` field in the output matches a specific structure indicating no required inputs.*

