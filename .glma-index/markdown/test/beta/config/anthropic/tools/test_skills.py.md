# test/beta/config/anthropic/tools/test_skills.py

4 function(s): test_extract_skills_strings, test_extract_skills_with_version, test_extract_skills_no_skills_schema, test_tool_to_api_raises_for_skills_schema.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_extract_skills_strings | function |  |
| test_extract_skills_with_version | function |  |
| test_extract_skills_no_skills_schema | function |  |
| test_tool_to_api_raises_for_skills_schema | function |  |

## Chunks

### test_extract_skills_strings (function, L14-L23)

> *Summary: This test verifies that a tool correctly extracts skill definitions for specified file types ("pptx" and "xlsx") from a given context. It asserts the output matches an expected list containing structured skill objects for both input formats.*


### test_extract_skills_with_version (function, L27-L36)

> *Summary: Given a `Context`, this test verifies that the tool correctly extracts skill definitions, including specific versions like `"20251013"` and `"latest"`, from an initialized `SkillsTool`. It asserts the resulting list matches the expected structure containing the skill ID and its associated version for each defined skill.*


### test_extract_skills_no_skills_schema (function, L40-L51)

> *Summary: When provided with a schema from a non-Skills tool, the function asserts that the skill extraction process returns an empty list. This test ensures the filtering mechanism correctly ignores unrelated tools like `WebSearchTool`.*


### test_tool_to_api_raises_for_skills_schema (function, L55-L67)

> *Summary: This test verifies that the `tool_to_api` function correctly rejects a schema originating from a `SkillsTool`. It asserts that passing this specific skill schema to the API conversion layer raises an `UnsupportedToolError`, ensuring proper filtering logic is maintained.*

