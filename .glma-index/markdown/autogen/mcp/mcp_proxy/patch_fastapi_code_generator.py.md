# autogen/mcp/mcp_proxy/patch_fastapi_code_generator.py

4 function(s): patch_parse_schema, snakecase, patch_function_name_parsing, patch_generate_code.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| patch_parse_schema | function |  |
| snakecase | function |  |
| patch_function_name_parsing | function |  |
| patch_generate_code | function |  |

## Chunks

### patch_parse_schema (function, L25-L36)

> *Summary: This function modifies the `OpenAPIParser` by wrapping its `parse_schema` method to correct duplicate reference names within parsed schema objects. It intercepts the original parsing output and updates any references found with a specific duplicate name before returning the modified structure.*


### snakecase (function, L39-L43)

> *Summary: Converts a given string into snake_case by replacing non-alphanumeric separators with underscores and ensuring the entire result is lowercase, while prepending an underscore before any uppercase letters found after the first character.*


### patch_function_name_parsing (function, L46-L59)

> *Summary: This code modifies the `Operation` class to override how function names are derived. It calculates a standardized name from either an existing `operationId` or by combining the operation's type and its snake-cased path, ensuring the result is always in snake\_case.*


### patch_generate_code (function, L63-L98)

> *Summary: This function intercepts calls to `generate_code` by wrapping the original method. It parses a YAML input, finds schema names containing dots (e.g., `a.b`), replaces these dot-separated names with underscore-separated versions within the input text, and then executes the original generator with the modified input.*

