# test/tools/experimental/searxng/test_searxng.py

1 class(es): TestSearxngSearchTool. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestSearxngSearchTool | class |  |

## Chunks

### TestSearxngSearchTool (class, L16-L137)

> *Summary: This test suite verifies the functionality of a search tool by mocking external API calls to simulate successful and failed searches. It confirms correct initialization, schema validation for input parameters like `query` and `max_results`, and proper execution when called with various inputs.*


### mock_response (method, L22-L23, parent: TestSearxngSearchTool)

> *Summary: Provides a predefined dictionary structure simulating an API response containing a title, URL, and content string. This mock output is used to simulate successful data retrieval during testing.*


### test_initialization (method, L25-L28, parent: TestSearxngSearchTool)

> *Summary: Verifies that an instance of the `SearxngSearchTool` is correctly initialized by checking its assigned name and description string. This test confirms the tool's metadata matches expected values upon instantiation.*


### test_schema_validation (method, L30-L70, parent: TestSearxngSearchTool)

> *Summary: This test verifies that the `SearxngSearchTool` correctly generates a predefined JSON schema for its search function. It asserts that the tool's internal schema matches an expected structure defining parameters like `query`, `max_results`, and optional filters.*


### test_execute_query_success (method, L73-L88, parent: TestSearxngSearchTool)

> *Summary: This test verifies successful execution of a search query by mocking the underlying execution mechanism to return predefined results. It asserts that the tool returns a list containing one dictionary with specific title, link, and snippet values, while also confirming the mock was called with expected parameters.*


### test_search (method, L91-L106, parent: TestSearxngSearchTool)

> *Summary: This test verifies the functionality of a search tool by mocking its execution and response. It calls the tool with specific query parameters and asserts that the returned result is a list containing one dictionary matching predefined content, while also confirming the underlying execution function was called correctly with those inputs.*


### test_search_invalid_query (method, L108-L111, parent: TestSearxngSearchTool)

> *Summary: This test verifies that passing a `None` value for the query to the search tool raises a `ValidationError`. It confirms the tool correctly handles invalid input by failing as expected.*


### test_integration_live (method, L114-L118, parent: TestSearxngSearchTool)

> *Summary: This test verifies the integration of a `SearxngSearchTool` by executing a search for "open source search engine" with one result. It asserts that the returned results are a list and contain at least zero elements.*


### test_agent_integration (method, L121-L137, parent: TestSearxngSearchTool)

> *Summary: This test verifies the integration between an AI agent and a search tool by instructing the agent to find news on open-source search engines. It asserts that the agent correctly utilizes and exposes the `SearxngSearchTool` within its available tools during execution.*

