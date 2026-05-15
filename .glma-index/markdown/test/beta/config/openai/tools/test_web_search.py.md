# test/beta/config/openai/tools/test_web_search.py

7 function(s): test_responses_api_defaults, test_responses_api_with_context_size, test_responses_api_with_max_uses, test_responses_api_all_options, test_responses_api_with_user_location, test_responses_api_with_user_location_partial, test_responses_api_with_allowed_domains. 1 class(es): TestResponsesApiIncludes. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_responses_api_defaults | function |  |
| test_responses_api_with_context_size | function |  |
| test_responses_api_with_max_uses | function |  |
| test_responses_api_all_options | function |  |
| test_responses_api_with_user_location | function |  |
| test_responses_api_with_user_location_partial | function |  |
| test_responses_api_with_allowed_domains | function |  |
| TestResponsesApiIncludes | class |  |

## Chunks

### test_responses_api_defaults (function, L14-L19)

> *Summary: This test verifies that the `WebSearchTool` schema, when processed by a conversion function, correctly maps to the `"web_search"` type in the responses API format. It takes a testing context as input and asserts the resulting dictionary structure.*


### test_responses_api_with_context_size (function, L23-L28)

> *Summary: This test verifies that a `WebSearchTool` configured with `"high"` context size correctly generates the expected API response schema when provided with a `Context` object. It asserts the resulting dictionary matches the specific tool type and context setting.*


### test_responses_api_with_max_uses (function, L32-L37)

> *Summary: This test verifies that a `WebSearchTool` configured with a maximum usage limit of five correctly translates its schema into the expected API response format. It asserts that the resulting structure includes `"type": "web_search"` and `"max_uses": 5`.*


### test_responses_api_all_options (function, L41-L50)

> *Summary: This test verifies that a `WebSearchTool` instance with specific configurations correctly translates its schema into the expected API response format. It asserts that the resulting dictionary accurately reflects the input parameters like `"search_context_size"` and `"max_uses"`.*


### test_responses_api_with_user_location (function, L54-L69)

> *Summary: This test verifies that the `WebSearchTool` correctly generates a schema when provided with specific user location data. It asserts that the resulting API representation accurately reflects the input city, region, and country as an approximate type.*


### test_responses_api_with_user_location_partial (function, L73-L87)

> *Summary: This test verifies that the `WebSearchTool` correctly generates a specific API response structure when provided with user location details. It asserts that the resulting schema maps to an expected dictionary format containing `"web_search"` type and approximate location data for Germany and Berlin.*


### test_responses_api_with_allowed_domains (function, L91-L99)

> *Summary: This test verifies that the `WebSearchTool` correctly translates its configuration, specifically allowed domains, into the expected structure for the responses API. It asserts that the generated schema includes a `"filters"` object containing the specified list of allowed domains.*


### TestResponsesApiIncludes (class, L103-L118)

> *Summary: This class verifies that the `responses_api_includes` function correctly maps tool schemas to required API inclusion fields. It asserts that web search tools require a specific source field, while other built-in or no-tool scenarios result in an empty list of inclusions.*


### test_web_search_requests_action_sources (method, L107-L110, parent: TestResponsesApiIncludes)

> *Summary: This test verifies that the `WebSearchTool` correctly exposes its schema, asserting that the resulting API response includes `"web_search_call.action.sources"` when provided with a context object.*


### test_no_tools_returns_empty (method, L112-L113, parent: TestResponsesApiIncludes)

> *Summary: Asserts that when no tools are provided, the API response for tool results is an empty list. This verifies the expected behavior of the system under a null tool configuration.*


### test_unrelated_builtin_returns_empty (method, L115-L118, parent: TestResponsesApiIncludes)

> *Summary: This test verifies that when a built-in function is used without relation to the current context, it yields no results. It calls `CodeExecutionTool().schemas()` with a provided context and asserts that the resulting list of schemas is empty.*

