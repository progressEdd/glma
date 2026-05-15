# test/beta/config/anthropic/tools/test_web_fetch.py

3 function(s): test_defaults, test_full, test_dynamic_version.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_defaults | function |  |
| test_full | function |  |
| test_dynamic_version | function |  |

## Chunks

### test_defaults (function, L13-L21)

> *Summary: This test verifies that the `WebFetchTool` correctly generates a specific API schema when provided with a context. It asserts that the resulting structure matches the expected format for a web fetch tool.*


### test_full (function, L25-L44)

> *Summary: This test verifies that a configured `WebFetchTool` correctly translates its parameters into the expected API schema format. It takes a `Context` object as input and asserts the resulting structure matches predefined constraints like domain lists and token limits.*


### test_dynamic_version (function, L48-L56)

> *Summary: This test verifies that a specific `WebFetchTool` instance, initialized with a fixed version string, correctly generates an API schema matching the expected structure and version. It asserts that the resulting schema maps to the correct tool name and its specified dynamic version identifier.*

