# test/beta/config/gemini/tools/test_tool_to_api.py

4 function(s): test_tool_to_api, test_parameterless_tool_empty_dict_gets_object_schema, test_parameterless_tool_null_type_gets_object_schema, test_additional_properties_stripped_from_anyof_branches.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_tool_to_api | function |  |
| test_parameterless_tool_empty_dict_gets_object_schema | function |  |
| test_parameterless_tool_null_type_gets_object_schema | function |  |
| test_additional_properties_stripped_from_anyof_branches | function |  |

## Chunks

### test_tool_to_api (function, L12-L26)

> *Summary: This test verifies that a provided tool schema is correctly transformed into the expected API tool structure. It asserts that the output list contains a single `Tool` object whose function declaration accurately reflects the input schema's name, description, and parameters JSON schema.*


### test_parameterless_tool_empty_dict_gets_object_schema (function, L29-L50)

> *Summary: This test verifies that when a function definition provides an empty parameter dictionary, the resulting API tool correctly normalizes it to use a JSON schema of type `object` with no properties. It asserts that the generated tool structure matches this expected normalized format.*


### test_parameterless_tool_null_type_gets_object_schema (function, L53-L74)

> *Summary: This test verifies that when a function is defined with no parameters, the underlying API tool schema correctly defaults to an empty object structure instead of using a `null` type. It asserts that the generated tool declaration for "list\_skills" has an empty properties dictionary within its JSON schema.*


### test_additional_properties_stripped_from_anyof_branches (function, L77-L125)

> *Summary: This test verifies that the schema mapper correctly strips `additionalProperties` from within `anyOf` branches when converting a Pydantic-like structure to the API tool format. It asserts that the resulting function declaration's parameters JSON schema omits these properties, preventing Gemini from rejecting the definition.*

