# test/beta/config/anthropic/tools/test_unsupported.py

2 function(s): test_image_generation, test_shell.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_image_generation | function |  |
| test_shell | function |  |

## Chunks

### test_image_generation (function, L15-L21)

> *Summary: This test verifies that an `ImageGenerationTool` schema correctly raises an `UnsupportedToolError` when passed to the API handler. It achieves this by first retrieving the tool's schemas from a given context and then asserting the expected exception during the API call.*


### test_shell (function, L25-L32)

> *Summary: This test verifies that the `ShellTool` is unsupported when interacting with Anthropic via the API. It asserts that calling `tool_to_api` with the tool's schema raises an `UnsupportedToolError`.*

