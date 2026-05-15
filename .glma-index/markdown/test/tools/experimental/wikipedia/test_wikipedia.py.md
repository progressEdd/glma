# test/tools/experimental/wikipedia/test_wikipedia.py

4 class(es): FakePage, TestWikipediaClient, TestWikipediaQueryRunTool, TestWikipediaPageLoadTool. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FakePage | class |  |
| TestWikipediaClient | class |  |
| TestWikipediaQueryRunTool | class |  |
| TestWikipediaPageLoadTool | class |  |

## Chunks

### FakePage (class, L22-L29)

> *Summary: Represents a mock Wikipedia page object initialized with an existence status, optional summary, and full text content. It provides a method to check if the simulated page is present.*


### __init__ (method, L23-L26, parent: FakePage)

> *Summary: Initializes an object to hold metadata about a Wikipedia entry, accepting boolean existence status and optional string fields for the summary and full text content. These attributes are stored internally for later access.*


### exists (method, L28-L29, parent: FakePage)

> *Summary: Checks the internal state flag to determine if a Wikipedia entity is present, returning a boolean value.*


### TestWikipediaClient (class, L33-L90)

> *Summary: This test suite verifies the functionality of a `WikipediaClient` by mocking external API calls to simulate various scenarios. It checks successful search results, HTTP error handling during searches, and the retrieval of both existing and non-existent Wikipedia pages.*


### test_search_success (method, L39-L62, parent: TestWikipediaClient)

> *Summary: This test verifies successful API interaction by mocking a valid JSON response from the Wikipedia search endpoint. It asserts that calling the search method with an input query returns a list containing exactly one result matching the expected title.*


### test_search_http_error (method, L65-L73, parent: TestWikipediaClient)

> *Summary: This test verifies that the client correctly raises a `requests.HTTPError` when an HTTP request to Wikipedia fails with an error status code. It achieves this by mocking the GET request to return a response object configured to raise an exception upon calling `raise_for_status()`.*


### test_get_page_exists (method, L75-L82, parent: TestWikipediaClient)

> *Summary: This test verifies the `get_page` method by mocking a successful response from the Wikipedia client. It asserts that the returned page object is not null and contains the expected simulated summary text.*


### test_get_page_nonexistent (method, L84-L90, parent: TestWikipediaClient)

> *Summary: This test verifies that requesting a non-existent Wikipedia page returns `None`. It mocks the underlying API call to simulate a missing page and asserts the resulting object is null.*


### TestWikipediaQueryRunTool (class, L94-L162)

> *Summary: This test suite verifies the functionality of a tool designed to query Wikipedia by mocking its underlying CLI interactions. It tests successful retrieval, handling of no results, and exception scenarios during the search process, while also confirming its correct registration with an agent.*


### tool (method, L100-L107, parent: TestWikipediaQueryRunTool)

> *Summary: Provides a pre-configured instance of `WikipediaQueryRunTool` specifically for testing purposes, ensuring the tool runs without verbose output.*


### test_query_run_success (method, L109-L136, parent: TestWikipediaQueryRunTool)

> *Summary: This test verifies successful execution of a Wikipedia query by mocking the underlying CLI search and page retrieval methods. It asserts that calling `query_run` with an input string returns a list containing a formatted string summarizing the retrieved page data.*


### test_query_run_no_results (method, L138-L142, parent: TestWikipediaQueryRunTool)

> *Summary: When the underlying Wikipedia search returns an empty list, this test verifies that the tool correctly outputs a specific "no results found" message when queried with any string.*


### test_query_run_exception (method, L144-L149, parent: TestWikipediaQueryRunTool)

> *Summary: This test verifies that when the underlying Wikipedia search fails with an exception, the method correctly catches it and returns a specific error string prefixed with "wikipedia search failed: ". It simulates failure by patching the `wiki_cli`'s `search` method.*


### test_agent_integration (method, L152-L162, parent: TestWikipediaQueryRunTool)

> *Summary: This test verifies that a `WikipediaPageLoadTool` correctly registers its associated query tool with an `AssistantAgent`. It confirms the agent's tools list contains the expected `WikipediaQueryRunTool` instance with the correct name.*


### TestWikipediaPageLoadTool (class, L166-L236)

> *Summary: This test suite verifies the functionality of a tool designed to fetch content from Wikipedia. It tests successful retrieval, handling of no results, and exception management when querying the underlying Wikipedia API client, and also confirms its integration with an agent system.*


### tool (method, L172-L179, parent: TestWikipediaPageLoadTool)

> *Summary: Provides a pre-configured instance of `WikipediaPageLoadTool` specifically for use in tests, ensuring it operates without verbose output.*


### test_content_search_success (method, L181-L210, parent: TestWikipediaPageLoadTool)

> *Summary: This test verifies successful content retrieval by mocking the Wikipedia tool's search and page fetching methods to return predefined data. It asserts that calling `content_search` with a query returns a non-empty list of `Document` objects containing the expected title and content snippet.*


### test_content_search_no_results (method, L212-L216, parent: TestWikipediaPageLoadTool)

> *Summary: When the underlying Wikipedia search returns an empty list, this test verifies that the content search method correctly outputs a specific "no results found" message. It mocks the `wiki_cli`'s `search` function to simulate zero matches for any given query.*


### test_content_search_exception (method, L218-L223, parent: TestWikipediaPageLoadTool)

> *Summary: This test verifies that when the underlying Wikipedia search fails with an exception, the method catches it and returns a specific error string prefixed with "wikipedia search failed: ". It simulates failure by patching the `wiki_cli`'s `search` method to raise an `Exception`.*


### test_agent_integration (method, L226-L236, parent: TestWikipediaPageLoadTool)

> *Summary: This test verifies that the `WikipediaPageLoadTool` is correctly registered with an `AssistantAgent`. It confirms the tool's presence and correct name within the agent's list of available tools after registration.*

