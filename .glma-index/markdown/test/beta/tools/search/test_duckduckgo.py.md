# test/beta/tools/search/test_duckduckgo.py

1 function(s): _make_config. 3 class(es): TestSchema, TestSearchExecution, TestDuckDuckSearchToolVariable. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_config | function |  |
| TestSchema | class |  |
| TestSearchExecution | class |  |
| TestDuckDuckSearchToolVariable | class |  |

## Chunks

### _make_config (function, L24-L39)

> *Summary: Constructs a `TestConfig` object simulating a model's response that invokes a specified tool with the provided search query as an argument. It takes the query string and optional final reply/tool name to define this simulated interaction.*


### TestSchema (class, L43-L65)

> *Summary: This test verifies the structure of schemas returned by a search tool, ensuring both default and custom configurations produce expected function names, descriptions, and parameter definitions. It asserts that the resulting schema adheres to a specific JSON-like structure for its input parameters.*


### test_default_schema (method, L44-L53, parent: TestSchema)

> *Summary: This test verifies that the `DuckDuckSearchTool` correctly returns a default search schema when queried with a context. It asserts that the returned schema defines a function named "duckduckgo\_search" requiring a string parameter called "query".*


### test_custom_schema (method, L55-L65, parent: TestSchema)

> *Summary: This test verifies that a custom DuckDuckGo search tool correctly exposes its defined function signature to the system. It asserts that the returned schema matches the expected name, description, and parameter structure for a query string input.*


### TestSearchExecution (class, L69-L143)

> *Summary: These tests verify the behavior of an `Agent` when utilizing a `DuckDuckSearchTool`. They confirm that the agent correctly processes structured search results, handles empty result sets, passes custom configuration parameters to the underlying client, and respects specified tool names during execution.*


### test_search_returns_structured_results (method, L70-L92, parent: TestSearchExecution)

> *Summary: This test verifies that the search tool returns structured results when queried by an agent. It mocks the underlying client to provide predefined sample data and asserts that the agent processes this into a specific `SearchResponse` format.*


### test_search_empty_results (method, L94-L113, parent: TestSearchExecution)

> *Summary: This test verifies that the agent correctly handles zero results from a search tool when querying for nonexistent content. It mocks the search tool to return an empty list and asserts that the resulting event reflects this empty response.*


### test_custom_client_used (method, L115-L128, parent: TestSearchExecution)

> *Summary: This test verifies that an agent correctly utilizes a custom search client when prompted to "search." It asserts that the underlying mock text method is called exactly once with the expected query and configuration parameters.*


### test_custom_tool_name_in_agent (method, L130-L143, parent: TestSearchExecution)

> *Summary: This test verifies that an agent correctly utilizes a custom-named search tool when prompted. It sets up the DuckDuckGo tool with a specific name, initializes the agent with this tool and configuration, executes a search query, and asserts that the underlying text retrieval method was called exactly once.*


### TestDuckDuckSearchToolVariable (class, L147-L189)

> *Summary: This test verifies that the `DuckDuckSearchTool` correctly resolves input variables from an `Agent`'s configuration when executing a search query. It asserts that the underlying client method is called with the expected values for region and safesearch, and also tests that a `KeyError` is raised if required variables are missing.*


### test_resolved (method, L148-L177, parent: TestDuckDuckSearchToolVariable)

> *Summary: This test verifies that an agent correctly configures and calls the `DuckDuckSearchTool` when asked to search. It asserts that the underlying client's text method is invoked with the expected query, region ("us-en"), and safesearch setting ("off").*


### test_missing_raises (method, L179-L189, parent: TestDuckDuckSearchToolVariable)

> *Summary: This test verifies that an `Agent` raises a `KeyError` when attempting to use the search tool if the necessary configuration for safesearch is missing. It mocks the DuckDuckGo client and runs the agent with a specific query to trigger this expected failure.*

