# test/beta/tools/search/test_tavily.py

1 function(s): _make_config. 3 class(es): TestSchema, TestSearchExecution, TestTavilySearchToolVariable. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_config | function |  |
| TestSchema | class |  |
| TestSearchExecution | class |  |
| TestTavilySearchToolVariable | class |  |

## Chunks

### _make_config (function, L47-L49)

> *Summary: Constructs a `TestConfig` object by creating a simulated tool call event containing the provided search query and specifying the default or custom tool name. This function returns the configuration needed to test model responses involving external tool usage.*


### TestSchema (class, L53-L75)

> *Summary: This test verifies the structure of schemas returned by a search tool, first checking the default configuration and then asserting custom parameters like name and description when initialized with specific values. It consumes a `Context` object to generate and validate these schema outputs against expected JSON structures.*


### test_default_schema (method, L54-L63, parent: TestSchema)

> *Summary: This test verifies that the `TavilySearchTool` returns a default search schema with the correct function name and parameter structure. It asserts that the returned schema requires a single string argument named "query".*


### test_custom_schema (method, L65-L75, parent: TestSchema)

> *Summary: This test verifies that a custom-configured `TavilySearchTool` correctly exposes its defined name, description, and parameter structure when requesting schemas from the context. It asserts these properties match the initial configuration provided to the tool instance.*


### TestSearchExecution (class, L79-L205)

> *Summary: This test suite verifies the functionality of a search execution mechanism by mocking external API calls to Tavily. It asserts that an agent correctly invokes the search tool with various inputs—including default, empty, and fully customized parameters—and validates the structure of the returned results event.*


### test_search_returns_structured_results (method, L81-L110, parent: TestSearchExecution)

> *Summary: This test verifies that the search tool returns structured data when called by an agent. It mocks a successful API response from Tavily and asserts that the resulting `ToolResultsEvent` contains correctly parsed search results, including titles, URLs, content, and scores.*


### test_search_empty_results (method, L113-L124, parent: TestSearchExecution)

> *Summary: This test verifies the agent's behavior when a search tool returns no results. It mocks an API call to return an empty list and asserts that the resulting event correctly contains this empty search response.*


### test_all_params_forwarded_to_client (method, L127-L168, parent: TestSearchExecution)

> *Summary: This test verifies that an agent correctly forwards all configured parameters from a `TavilySearchTool` instance to the external search API endpoint. It asserts that the request body sent to the mocked Tavily URL matches every specific configuration passed to the tool.*


### test_none_params_omitted (method, L171-L180, parent: TestSearchExecution)

> *Summary: This test verifies that when an agent is prompted to search, it correctly constructs and sends a request to the Tavily API using only the necessary parameters. It asserts that the outgoing POST request body contains exactly `{"query": "q"}`.*


### test_client_kwargs_forwarded_to_sdk (method, L183-L192, parent: TestSearchExecution)

> *Summary: This test verifies that custom API base URLs and client keyword arguments are correctly passed to the underlying SDK when initializing a search tool. It asserts that an HTTP POST request is made to the specified custom endpoint during agent execution.*


### test_custom_tool_name_in_agent (method, L195-L205, parent: TestSearchExecution)

> *Summary: This test verifies that an agent correctly invokes a custom-named search tool when prompted. It mocks the external API call and asserts that the configured `TavilySearchTool` with the specified name is actually called by the agent during execution.*


### TestTavilySearchToolVariable (class, L209-L242)

> *Summary: This test suite verifies the behavior of a search tool integration by mocking external API calls to Tavily. It asserts that when necessary variables are provided, the agent correctly constructs and sends the expected request payload; conversely, it confirms that missing required input variables raises an appropriate `KeyError`.*


### test_resolved (method, L211-L232, parent: TestTavilySearchToolVariable)

> *Summary: This test verifies that an agent correctly constructs and sends a search request to the Tavily API. It mocks the external API call, initializes the agent with specific variables, executes a query, and asserts that the sent request body matches the expected parameters.*


### test_missing_raises (method, L235-L242, parent: TestTavilySearchToolVariable)

> *Summary: This test verifies that an `Agent` raises a `KeyError` when attempting to use the search tool if the required topic variable is missing during execution. It mocks a successful API response from Tavily while asserting the expected error condition occurs when calling the agent's ask method.*

