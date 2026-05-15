# test/tools/experimental/duckduckgo/test_duckduckgo.py

1 class(es): TestDuckDuckGoSearchTool. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestDuckDuckGoSearchTool | class |  |

## Chunks

### TestDuckDuckGoSearchTool (class, L17-L150)

> *Summary: This test suite verifies the functionality and schema of a search tool that interfaces with DuckDuckGo. It tests initialization, JSON schema validation, successful query execution with default and custom parameters, input validation for empty queries, and integration within an AI agent environment.*


### mock_response (method, L23-L33, parent: TestDuckDuckGoSearchTool)

> *Summary: Returns a predefined list containing a single dictionary structure simulating search results. This mock fixture provides sample data with `title`, `href`, and `body` keys for testing purposes.*


### test_initialization (method, L35-L41, parent: TestDuckDuckGoSearchTool)

> *Summary: Verifies that an instance of `DuckDuckGoSearchTool` is correctly initialized by checking its assigned name and ensuring its description contains the expected usage instruction.*


### test_schema_validation (method, L43-L67, parent: TestDuckDuckGoSearchTool)

> *Summary: Verifies that the `DuckDuckGoSearchTool` instance possesses a correctly structured JSON schema. It compares the tool's actual schema against a predefined dictionary containing the function name, description, and parameter definitions for the search operation.*


### test_execute_query_success (method, L70-L88, parent: TestDuckDuckGoSearchTool)

> *Summary: Verifies that the search tool correctly processes and returns structured results when an API call succeeds. It inputs a test query, expects the mocked execution to return predefined data, and asserts the output matches expected structure and content while confirming the correct arguments were passed to the underlying executor.*


### test_search (method, L91-L106, parent: TestDuckDuckGoSearchTool)

> *Summary: Verifies the core search functionality by mocking external execution and response data. It calls the tool with specific inputs ("Test query", 3 results) and asserts that the returned structure matches expected content and that the underlying execution function was called correctly with those parameters.*


### test_search_invalid_query (method, L108-L115, parent: TestDuckDuckGoSearchTool)

> *Summary: This test verifies that passing `None` as the query to the search tool correctly triggers a Pydantic validation error. It asserts that the resulting exception message specifically indicates an invalid string input.*


### test_agent_integration (method, L118-L150, parent: TestDuckDuckGoSearchTool)

> *Summary: This test verifies that an `AssistantAgent` correctly integrates and utilizes a `DuckDuckGoSearchTool`. It mocks the search execution to confirm the agent calls the tool when prompted with a query, asserting both the call occurred and the tool is properly registered.*

