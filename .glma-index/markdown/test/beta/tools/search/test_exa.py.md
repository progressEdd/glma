# test/beta/tools/search/test_exa.py

2 function(s): _tool_call_config, _exa_result. 8 class(es): TestSchema, TestSearchExecution, TestFindSimilar, TestGetContents, TestAnswer, TestExaToolkitVariable, TestIntegrationHeader, TestIndividualTools. 23 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _tool_call_config | function |  |
| _exa_result | function |  |
| TestSchema | class |  |
| TestSearchExecution | class |  |
| TestFindSimilar | class |  |
| TestGetContents | class |  |
| TestAnswer | class |  |
| TestExaToolkitVariable | class |  |
| TestIntegrationHeader | class |  |
| TestIndividualTools | class |  |

## Chunks

### _tool_call_config (function, L30-L43)

> *Summary: Constructs a `TestConfig` object simulating a model response that includes a specific tool call. It takes input arguments and a tool name to generate the structured output for testing purposes.*


### _exa_result (function, L46-L62)

> *Summary: Constructs a dictionary representing search result metadata using provided parameters like title, URL, and relevance score. It returns this structured data containing all input fields for easy consumption by other parts of the system.*


### TestSchema (class, L66-L93)

> *Summary: This test suite verifies the functionality of an `ExaToolkit` by asserting that it correctly returns a predefined set of schemas, validates the parameter structure for the search function, and confirms custom tool names and descriptions are applied when creating specialized tools. It takes a `Context` object as input and asserts against expected schema structures derived from the toolkit's API calls.*


### test_default_schemas (method, L67-L73, parent: TestSchema)

> *Summary: This test verifies that an initialized `ExaToolkit` returns a predefined set of four function schemas when queried with a given context. It asserts that the extracted function names match the expected list: `"exa_search"`, `"exa_find_similar"`, `"exa_get_contents"`, and `"exa_answer"`.*


### test_search_schema_has_query_param (method, L75-L84, parent: TestSchema)

> *Summary: This test verifies that the `exa_search` function schema within the toolkit includes a required string parameter named "query". It achieves this by fetching all schemas from the toolkit and asserting the structure of the specific search schema's parameters.*


### test_custom_tool_name_and_description (method, L86-L93, parent: TestSchema)

> *Summary: This test verifies that a custom tool name and description are correctly reflected in the generated schemas when using an `ExaToolkit`. It calls the toolkit's search method with specific metadata and asserts that the resulting schema matches those inputs.*


### TestSearchExecution (class, L97-L247)

> *Summary: This test suite verifies the behavior of an AI agent interacting with an Exa search tool by mocking HTTP responses. It confirms that the agent correctly structures and forwards various parameters—including query, advanced filters, and content limits—to the external API based on how they are configured in the toolkit or passed during the call.*


### test_returns_structured_results (method, L99-L141, parent: TestSearchExecution)

> *Summary: This test verifies that an agent correctly processes structured search results from the Exa API. It mocks a successful HTTP response containing two search results and asserts that the resulting `ToolResultsEvent` contains these data points in the expected format.*


### test_empty_results (method, L144-L154, parent: TestSearchExecution)

> *Summary: This test verifies the agent's behavior when an external search API returns no results. It mocks a successful HTTP response with an empty results list and asserts that the resulting tool event correctly reflects this empty outcome for the given query.*


### test_none_params_omitted (method, L157-L165, parent: TestSearchExecution)

> *Summary: This test verifies that when an agent is prompted to search, it correctly constructs and sends a request payload containing the expected query parameter to the Exa API endpoint. It asserts that the outgoing HTTP request body matches a specific partial dictionary structure.*


### test_all_params_forwarded (method, L168-L202, parent: TestSearchExecution)

> *Summary: This test verifies that an agent correctly forwards all provided parameters when calling the Exa search tool. It asserts that the request body sent to the external API matches the input configuration, including specific values for various search criteria like date ranges and domain lists.*


### test_search_and_contents_when_max_characters_set_on_method (method, L205-L222, parent: TestSearchExecution)

> *Summary: This test verifies that when a maximum character limit is configured on the search tool, the agent correctly passes this constraint in its API request. It asserts that the outgoing POST request to the Exa search endpoint includes both the query and the specified `maxCharacters` value within the contents payload.*


### test_toolkit_level_max_characters_applied_to_default_search (method, L225-L236, parent: TestSearchExecution)

> *Summary: This test verifies that the `ExaToolkit` correctly applies a specified maximum character limit to the default search query when an agent invokes it. It asserts that the outgoing request body sent to the Exa API includes the configured `maxCharacters` value of 800.*


### test_toolkit_level_num_results_applied_to_default_search (method, L239-L247, parent: TestSearchExecution)

> *Summary: This test verifies that the `ExaToolkit` correctly applies a specified number of results when used with an agent's search query. It mocks the external API call and asserts that the request sent to the search endpoint includes both the query and the configured `numResults`.*


### TestFindSimilar (class, L251-L301)

> *Summary: These tests verify that an `Agent` correctly passes configuration parameters to the underlying Exa toolkit when invoking a similarity search tool. Specifically, it confirms that arguments like `num_results`, `num_results` from the toolkit constructor, and `exclude_source_domain` are accurately reflected in the outgoing API request body.*


### test_num_results_forwarded_from_method (method, L253-L267, parent: TestFindSimilar)

> *Summary: This test verifies that the `Agent` correctly forwards the specified number of results when calling an external search tool. It mocks a successful API response and asserts that the request sent to the mock endpoint contains the expected URL and the configured `numResults`.*


### test_num_results_forwarded_from_toolkit (method, L270-L282, parent: TestFindSimilar)

> *Summary: This test verifies that the agent correctly forwards the specified number of results when calling an external tool via ExaToolkit. It mocks a successful API response and asserts that the request sent to the endpoint contains the expected `numResults` parameter derived from the toolkit configuration.*


### test_exclude_source_domain_forwarded (method, L285-L301, parent: TestFindSimilar)

> *Summary: This test verifies that when an agent calls the `find_similar` tool with `exclude_source_domain=True`, the resulting API request correctly includes this flag in its payload. It mocks the external search endpoint and asserts the structure of the outgoing POST request body.*


### TestGetContents (class, L305-L342)

> *Summary: This test verifies that an agent correctly retrieves content from the Exa API when prompted. It mocks a successful POST request to `/contents` and asserts that the agent calls the endpoint with the correct URL and that the returned data is processed into the expected `ExaContentResult`.*


### test_returns_content (method, L307-L342, parent: TestGetContents)

> *Summary: This test verifies that an agent correctly processes and returns content retrieved from the Exa API. It mocks a successful HTTP response containing search results, then asserts that the agent's tool call matches expected input parameters and that the final output contains the mocked content data.*


### TestAnswer (class, L346-L379)

> *Summary: This test verifies that an agent correctly processes and returns a structured answer, including citations, after calling the Exa API via a mocked HTTP response. It asserts that the tool call was made with the correct query and that the resulting data matches the expected structure from the mock service.*


### test_returns_answer_with_citations (method, L348-L379, parent: TestAnswer)

> *Summary: This test verifies that an agent correctly processes a response from the Exa tool, asserting that the returned answer and associated citations are accurately captured in the `ToolResultsEvent`. It mocks an HTTP POST request to simulate receiving structured data containing both a textual answer and citation metadata.*


### TestExaToolkitVariable (class, L383-L417)

> *Summary: This test suite verifies the behavior of an Exa search tool integration within an Agent framework. It asserts that when input variables are provided, the resulting API call correctly incorporates those values, and it also confirms that a `KeyError` is raised if required input variables are missing during execution.*


### test_resolved (method, L385-L402, parent: TestExaToolkitVariable)

> *Summary: This test verifies that an agent correctly invokes the Exa search tool with specific parameters when prompted. It mocks the external API call and asserts that the request sent to the service contains the expected query, result limit (10), and search type ("neural").*


### test_missing_raises (method, L405-L417, parent: TestExaToolkitVariable)

> *Summary: This test verifies that the system raises a `KeyError` when an agent attempts to use the search tool without specifying a required `search_type`. It mocks a successful API response but asserts failure due to missing input parameters during execution.*


### TestIntegrationHeader (class, L421-L474)

> *Summary: These tests verify that various Exa toolkit operations, such as searching or finding similar items, correctly inject a specific `x-exa-integration` header into outgoing HTTP requests made by an Agent. They use mocking to simulate API responses and assert the presence of this required header on the mocked routes.*


### test_search_sets_header (method, L423-L430, parent: TestIntegrationHeader)

> *Summary: This test verifies that an `Agent` correctly includes the required `x-exa-integration: ag2` header when calling the Exa search endpoint via a provided toolkit. It mocks the API response to ensure the agent's request structure is correct.*


### test_find_similar_sets_header (method, L433-L444, parent: TestIntegrationHeader)

> *Summary: This test verifies that an agent correctly calls the Exa API endpoint when prompted to find similar items. It asserts that the outgoing request includes a specific `x-exa-integration` header, confirming proper tool invocation setup.*


### test_get_contents_sets_header (method, L447-L458, parent: TestIntegrationHeader)

> *Summary: This test verifies that when an agent requests content using the ExaToolkit, it correctly sets the `x-exa-integration` header to "ag2" in the outgoing HTTP request. It mocks a successful API response and asserts the presence of this specific header on the last recorded call.*


### test_answer_sets_header (method, L461-L474, parent: TestIntegrationHeader)

> *Summary: This test verifies that an agent correctly includes the `x-exa-integration` header in its API call to Exa when querying for a specific topic. It mocks a successful response from the `/answer` endpoint and asserts the correct integration identifier is present in the outgoing request headers.*


### TestIndividualTools (class, L478-L510)

> *Summary: These tests verify the functionality of an `Agent` when interacting with tools provided by an `ExaToolkit`. They assert that the agent correctly invokes specific API endpoints (like `/search`) either when only one tool is available or when multiple tools are present in the toolkit.*


### test_search_tool_passed_alone (method, L480-L493, parent: TestIndividualTools)

> *Summary: This test verifies that an agent correctly invokes the search tool when prompted with a specific query. It mocks the external API call to return a successful result and asserts that the mock endpoint was indeed called by the agent.*


### test_pick_two_tools_from_toolkit (method, L496-L510, parent: TestIndividualTools)

> *Summary: This test verifies that an agent correctly invokes the search tool when prompted with a specific query. It sets up mock HTTP responses for Exa API endpoints and asserts that the `exa_search` route was called during the agent's execution.*

