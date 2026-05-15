# test/beta/config/gemini/tools/test_web_search.py

3 function(s): test_defaults, test_with_blocked_domains, test_mixed_with_function_tool.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_defaults | function |  |
| test_with_blocked_domains | function |  |
| test_mixed_with_function_tool | function |  |

## Chunks

### test_defaults (function, L15-L22)

> *Summary: This test verifies that the `WebSearchTool` correctly generates a list containing a single Google Search tool definition when provided with a context. It asserts that the resulting structure matches the expected output format for tool building.*


### test_with_blocked_domains (function, L26-L33)

> *Summary: This test verifies that a `WebSearchTool` configured with specific blocked domains correctly generates tool schemas where those same domains are excluded from the resulting Google Search configuration. It asserts that the generated tool structure matches the expected exclusion list.*


### test_mixed_with_function_tool (function, L37-L54)

> *Summary: This test verifies that combining a custom function tool with the `WebSearchTool` results in a specific list of structured tools. It asserts that the combined output contains both the declared function and a Google Search tool instance.*

