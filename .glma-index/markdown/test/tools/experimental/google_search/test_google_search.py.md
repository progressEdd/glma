# test/tools/experimental/google_search/test_google_search.py

1 class(es): TestGoogleSearchTool. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestGoogleSearchTool | class |  |

## Chunks

### TestGoogleSearchTool (class, L17-L109)

> *Summary: This test suite verifies the functionality of a Google Search tool by initializing it under different configurations and simulating search queries. It uses mocking to inject predefined results into tests that validate both direct API calls and end-to-end agent interactions with various LLM providers (OpenAI and Gemini).*


### test_init (method, L19-L26, parent: TestGoogleSearchTool)

> *Summary: This test verifies that an instance of `GoogleSearchTool` is correctly initialized, either using an internal LLM if available or by providing specific API credentials. It asserts that the resulting tool object has the expected name and description for Google Search functionality.*


### expected_search_result (method, L29-L45, parent: TestGoogleSearchTool)

> *Summary: Returns a dictionary representing a mock Google search result structure. This data simulates two search results, each containing a title, link, and snippet for testing purposes.*


### test_google_search_f (method, L47-L58, parent: TestGoogleSearchTool)

> *Summary: This test verifies the output of a Google search function by mocking its underlying execution. It calls the search utility with specific parameters and asserts that the returned list contains exactly two results based on the mocked response.*


### _test_end_to_end (method, L60-L85, parent: TestGoogleSearchTool)

> *Summary: This test method verifies the end-to-end functionality of a Google Search tool integration with an assistant agent. It mocks the actual search execution to return predefined results and asserts that the underlying query function was called as expected during the assistant's run cycle.*


### test_end_to_end_openai (method, L88-L97, parent: TestGoogleSearchTool)

> *Summary: This test verifies the complete workflow by using a configured `GoogleSearchTool` with provided OpenAI credentials and an expected result. It calls a base testing method to ensure the search tool executes its query correctly against the specified expectations.*


### test_end_to_end_gemini (method, L100-L109, parent: TestGoogleSearchTool)

> *Summary: This test verifies the end-to-end functionality of a Google Search tool using Gemini credentials. It initializes the search tool and calls a base testing method with specific expected results, ensuring the query execution is initially disabled for this check.*

