# test/tools/experimental/tavily/test_tavily.py

1 class(es): TestTavilySearchTool. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTavilySearchTool | class |  |

## Chunks

### TestTavilySearchTool (class, L17-L205)

> *Summary: This test suite verifies the functionality and schema of a search tool wrapper for Tavily. It tests initialization, parameter validation, successful API query execution against mocked responses, and integration with an `AssistantAgent`.*


### mock_response (method, L23-L35, parent: TestTavilySearchTool)

> *Summary: Returns a predefined dictionary structure simulating a successful search API response, containing a list of results with title, URL, and content fields for testing purposes.*


### test_initialization (method, L38-L50, parent: TestTavilySearchTool)

> *Summary: Verifies that `TavilySearchTool` requires an API key when internal authentication is enabled, raising a `ValueError` if none is provided. When initialized with a valid key, it confirms the tool's name, description, and stored API key match expected values.*


### test_tool_schema (method, L52-L108, parent: TestTavilySearchTool)

> *Summary: Verifies that the `TavilySearchTool` instance generates a JSON schema matching a predefined structure. It compares the generated schema, which defines parameters like `query`, `search_depth`, and result limits, against an expected dictionary.*


### test_parameter_validation (method, L116-L122, parent: TestTavilySearchTool)

> *Summary: This test verifies that the `TavilySearchTool` constructor raises a `ValueError` when provided with invalid parameters. It asserts that the raised exception message contains the expected error string based on the input dictionary.*


### test_execute_query_success (method, L125-L148, parent: TestTavilySearchTool)

> *Summary: This test verifies successful API query execution by mocking the underlying execution function to return a predefined response. It asserts that the tool returns a list containing one dictionary with specific title, link, and snippet values, while also confirming the mock was called with expected parameters.*


### test_search (method, L151-L172, parent: TestTavilySearchTool)

> *Summary: This test verifies the core search functionality by mocking API execution and response. It calls the `TavilySearchTool` with a specific query and asserts that the returned result is a list containing one item with expected title, link, and snippet values, while also confirming the underlying execution function was called with predefined parameters.*


### test_search_invalid_query (method, L174-L181, parent: TestTavilySearchTool)

> *Summary: Verifies that passing `None` as the query to the search tool correctly triggers a Pydantic validation error, specifically checking for an "Input should be a valid string" message. This confirms input validation enforces a non-null string for the search operation.*


### test_agent_integration (method, L184-L205, parent: TestTavilySearchTool)

> *Summary: This test verifies the integration of a `TavilySearchTool` with an `AssistantAgent`. It runs a query, asserting that the agent correctly invokes the mocked search tool and that the tool is properly registered on the assistant.*

