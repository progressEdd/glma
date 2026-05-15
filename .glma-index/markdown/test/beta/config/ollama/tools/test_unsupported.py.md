# test/beta/config/ollama/tools/test_unsupported.py

8 function(s): test_web_search, test_web_fetch, test_code_execution, test_shell, test_memory, test_image_generation, test_mcp_server, test_skills.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_web_search | function |  |
| test_web_fetch | function |  |
| test_code_execution | function |  |
| test_shell | function |  |
| test_memory | function |  |
| test_image_generation | function |  |
| test_mcp_server | function |  |
| test_skills | function |  |

## Chunks

### test_web_search (function, L21-L27)

> *Summary: This test verifies that attempting to use a `WebSearchTool` schema with the API raises an `UnsupportedToolError`. It initializes the tool, retrieves its schemas using a provided context, and then asserts the expected error when passing the retrieved schema to the API function.*


### test_web_fetch (function, L31-L37)

> *Summary: This test verifies that attempting to use a schema obtained from `WebFetchTool` with the API raises an `UnsupportedToolError`. It initializes the tool, retrieves its schemas using the provided context, and then asserts the expected error when passing one of those schemas to `tool_to_api`.*


### test_code_execution (function, L41-L47)

> *Summary: This test verifies that attempting to use a schema obtained from the `CodeExecutionTool` with an API function raises an `UnsupportedToolError`. It achieves this by first fetching schemas using the tool within a given context and then calling the API wrapper.*


### test_shell (function, L51-L57)

> *Summary: This test verifies that attempting to use a `ShellTool` schema with the API function raises an `UnsupportedToolError`. It initializes the tool, retrieves its schemas from the context, and then asserts the expected exception when passing one of those schemas.*


### test_memory (function, L61-L67)

> *Summary: This test verifies that an unsupported tool raises the expected error when passed to the API layer. It initializes a `MemoryTool`, retrieves its schemas using a provided context, and then asserts that calling `tool_to_api` with one of those schemas fails with an `UnsupportedToolError`.*


### test_image_generation (function, L71-L77)

> *Summary: This test verifies that an `ImageGenerationTool` schema correctly raises an `UnsupportedToolError` when passed to the API handler. It achieves this by first retrieving the tool's schemas from a given context and then asserting the expected exception during the API call.*


### test_mcp_server (function, L81-L87)

> *Summary: This test verifies that an attempt to use a schema obtained from the `MCPServerTool` will raise an `UnsupportedToolError`. It initializes the tool with a specific server URL and then asserts the expected failure when passing its retrieved schemas to the API function.*


### test_skills (function, L91-L97)

> *Summary: This test verifies that an attempt to use a specific `SkillsTool` instance, initialized for "pptx", will raise an `UnsupportedToolError` when passed to the API function. It achieves this by first retrieving the tool's schemas from the provided context and then asserting the expected exception during the API call.*

