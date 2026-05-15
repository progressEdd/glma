# test/tools/experimental/perplexity/test_perplexity.py

1 class(es): TestPerplexitySearchTool. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestPerplexitySearchTool | class |  |

## Chunks

### TestPerplexitySearchTool (class, L23-L210)

> *Summary: This test suite validates the `PerplexitySearchTool` by checking initialization constraints, schema correctness, parameter validation, and successful/error handling during API execution. It verifies that the tool correctly interfaces with mock HTTP requests for both successful query responses and JSON decoding failures, while also testing its integration with an agent framework.*


### mock_response (method, L29-L47, parent: TestPerplexitySearchTool)

> *Summary: Returns a predefined dictionary structure simulating an API response for testing purposes. This mock object contains details like model ID, usage statistics, citations, and the assistant's generated message content.*


### test_initialization (method, L50-L63, parent: TestPerplexitySearchTool)

> *Summary: Verifies the `PerplexitySearchTool` initialization logic based on an authentication flag. If internal auth is enabled, it expects a `ValueError` when no API key is provided; otherwise, it confirms the tool's name, description, model, and token limits are correctly set with a valid key.*


### test_tool_schema (method, L65-L82, parent: TestPerplexitySearchTool)

> *Summary: Verifies that the `PerplexitySearchTool` correctly generates a JSON schema defining its function signature, including the required `query` string parameter. It asserts that the generated schema matches a predefined structure based on the tool's description.*


### test_parameter_validation (method, L93-L99, parent: TestPerplexitySearchTool)

> *Summary: This test verifies that the `PerplexitySearchTool` constructor raises a `ValueError` when provided with invalid parameters from the input dictionary. It asserts that the raised exception message contains the specified error string, confirming proper parameter validation.*


### test_execute_query_success (method, L102-L134, parent: TestPerplexitySearchTool)

> *Summary: This test verifies successful API interaction by mocking HTTP requests and responses. It executes a query using the `PerplexitySearchTool` with predefined inputs and asserts that the returned object is correctly structured and matches expected content from the mock response.*


### test_execute_query_error (method, L137-L151, parent: TestPerplexitySearchTool)

> *Summary: This test verifies that the tool correctly handles a `JSONDecodeError` when attempting to parse an invalid JSON response from an API call. It asserts that executing the query raises a `RuntimeError` containing a specific error message upon receiving non-JSON data.*


### test_search (method, L154-L174, parent: TestPerplexitySearchTool)

> *Summary: This test verifies the core search functionality by mocking API execution and response. It calls the `search` method with a query, asserting that the returned object is a `SearchResponse` containing expected content, citations, and no errors, while also verifying the exact arguments passed to the underlying execution mock.*


### test_search_invalid_query (method, L176-L183, parent: TestPerplexitySearchTool)

> *Summary: This test verifies that attempting to search with an empty string input causes the `PerplexitySearchTool` to raise a `ValueError`. It asserts that the raised exception contains a specific message indicating that a valid, non-empty query is required.*


### test_search_exception_case (method, L185-L195, parent: TestPerplexitySearchTool)

> *Summary: This test verifies that the search method correctly handles exceptions thrown during query execution by mocking the underlying API call to raise an error. It asserts that when an exception occurs, the returned `SearchResponse` object contains no content or citations but includes a descriptive error message.*


### test_agent_integration (method, L198-L210, parent: TestPerplexitySearchTool)

> *Summary: This test verifies the setup of an `AssistantAgent` by injecting a `PerplexitySearchTool`. It confirms that the agent correctly registers and exposes the search tool with the expected name to its available tools list.*

