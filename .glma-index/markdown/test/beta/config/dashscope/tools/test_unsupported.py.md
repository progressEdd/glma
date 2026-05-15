# test/beta/config/dashscope/tools/test_unsupported.py

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

> *Summary: This test verifies that attempting to use a `WebSearchTool` schema with the API raises an `UnsupportedToolError`. It initializes the tool, retrieves its schemas from the provided context, and then asserts the expected error when passing the retrieved schema to the API function.*


### test_web_fetch (function, L31-L37)

> *Summary: This test verifies that attempting to use a `WebFetchTool` schema with the API raises an `UnsupportedToolError`. It initializes the tool, retrieves its schemas from the provided context, and then asserts the expected error when passing the retrieved schema to the API function.*


### test_code_execution (function, L41-L47)

> *Summary: This test verifies that attempting to use a schema obtained from the `CodeExecutionTool` with the API function raises an `UnsupportedToolError`. It confirms the tool's schemas are correctly identified as unsupported by the API layer.*


### test_shell (function, L51-L57)

> *Summary: This test verifies that attempting to use a `ShellTool` schema with the API raises an `UnsupportedToolError`. It initializes the tool, retrieves its schemas from the provided context, and then asserts the expected exception when calling the API function.*


### test_memory (function, L61-L67)

> *Summary: This test verifies that an unsupported tool raises the expected `UnsupportedToolError` when its schema is passed to the API interface. It initializes a `MemoryTool`, retrieves its schemas using a provided context, and then asserts the error upon calling the API function with those schemas.*


### test_image_generation (function, L71-L77)

> *Summary: This test verifies that an unsupported tool raises the expected `UnsupportedToolError` when passed to the API layer. It initializes an `ImageGenerationTool`, retrieves its schemas, and then attempts to process those schemas through a function expecting support.*


### test_mcp_server (function, L81-L87)

> *Summary: This test verifies that an unsupported tool raises the expected error when passed to the API handler. It initializes an `MCPServerTool` and asserts that calling `tool_to_api` with its retrieved schema fails with an `UnsupportedToolError`.*


### test_skills (function, L91-L97)

> *Summary: This test verifies that an attempt to use a specific `SkillsTool` instance, initialized for "pptx", raises an `UnsupportedToolError` when passed to the API layer. It achieves this by first retrieving the tool's schema from the provided context and then calling the API function with that schema within a `pytest.raises` block.*

