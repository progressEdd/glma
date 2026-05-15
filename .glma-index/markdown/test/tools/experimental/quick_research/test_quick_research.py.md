# test/tools/experimental/quick_research/test_quick_research.py

1 class(es): TestQuickResearchTool. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestQuickResearchTool | class |  |

## Chunks

### TestQuickResearchTool (class, L25-L402)

> *Summary: This test suite validates the `QuickResearchTool` by verifying its initialization, JSON schema structure, and various internal helper functions like HTML cleaning, domain extraction, and token splitting. It extensively tests the end-to-end research pipeline using mocks to simulate Tavily search results and web crawling/summarization, ensuring correct handling of success cases, timeouts, failures, and query limits.*


### llm_config (method, L31-L32, parent: TestQuickResearchTool)

> *Summary: Returns a configured `LLMConfig` object, hardcoding the model to `"gpt-4o-mini"` and providing a test API key. This method establishes the default configuration for an LLM instance during testing.*


### mock_tavily_response (method, L35-L49, parent: TestQuickResearchTool)

> *Summary: Provides a hardcoded dictionary simulating the response structure from a Tavily search API call. This mock returns a list of two results, each containing a title, URL, and content snippet.*


### mock_crawl_html (method, L52-L65, parent: TestQuickResearchTool)

> *Summary: Returns a hardcoded HTML string simulating the content fetched from a web crawl. This mock output includes various elements like scripts, links, and images for testing purposes.*


### test_initialization_missing_tavily_key (method, L69-L73, parent: TestQuickResearchTool)

> *Summary: This test verifies that attempting to initialize the research tool without a Tavily API key correctly raises a `ValueError`. It achieves this by temporarily removing the environment variable and passing `None` for the API key during instantiation.*


### test_initialization_success (method, L75-L81, parent: TestQuickResearchTool)

> *Summary: Verifies that the `QuickResearchTool` initializes correctly when provided with an LLM configuration and a Tavily API key. It asserts the tool's name, description content, stored API key, and that its main function is callable.*


### test_initialization_custom_params (method, L83-L90, parent: TestQuickResearchTool)

> *Summary: Verifies that the `QuickResearchTool` correctly initializes and stores custom parameters provided during instantiation. It confirms that setting `num_results_per_query` to 5 results in the tool object reflecting this value.*


### test_tool_schema (method, L94-L108, parent: TestQuickResearchTool)

> *Summary: Verifies that a `QuickResearchTool`'s generated JSON schema correctly defines a function named "quick\_research" and requires a "queries" parameter. It also asserts that internal dependencies are excluded from the final schema definition.*


### test_clean_html (method, L112-L118, parent: TestQuickResearchTool)

> *Summary: This test verifies that the `_clean_html` function successfully sanitizes input HTML by removing embedded scripts and CSS styles while preserving core textual content. It asserts that specific malicious or styling elements are absent from the output when provided with mock HTML and a base URL.*


### test_clean_html_preserves_same_site_links (method, L120-L124, parent: TestQuickResearchTool)

> *Summary: This test verifies that the HTML cleaning utility correctly preserves links pointing to the same site. It takes an HTML string and a base URL as input, asserting that the resulting cleaned output still contains the original link text.*


### test_clean_html_removes_media_tags (method, L126-L139, parent: TestQuickResearchTool)

> *Summary: This test verifies that the HTML cleaning utility successfully strips out media elements like `<img>`, `<video>`, and `<audio>` tags from an input string. It asserts that only plain text remains after processing the provided HTML content.*


### test_reg_dom (method, L143-L147, parent: TestQuickResearchTool)

> *Summary: This test verifies the functionality of a domain extraction utility by asserting correct outputs for various inputs, such as full URLs and subdomains. It confirms that the function successfully isolates the registered domain from different hostname formats.*


### test_split_tokens_short_text (method, L151-L158, parent: TestQuickResearchTool)

> *Summary: This test verifies that a brief input string results in exactly one token chunk. It uses the `cl100k_base` encoding to process the short text and asserts the resulting list contains a single element including the expected substring.*


### test_split_tokens_long_text (method, L160-L171, parent: TestQuickResearchTool)

> *Summary: This test verifies that a long input string is correctly segmented into multiple smaller text chunks using the `cl100k_base` encoding. It asserts that the resulting list of chunks contains more than one element and that each chunk is a non-empty string.*


### test_tavily_search (method, L176-L188, parent: TestQuickResearchTool)

> *Summary: This test verifies that the `_tavily_search` function correctly processes and returns a list of formatted search results when provided with mock Tavily API responses. It asserts the structure, length, and specific content of the returned data while confirming the underlying search client was called exactly once.*


### test_tavily_search_empty_results (method, L191-L198, parent: TestQuickResearchTool)

> *Summary: When the underlying search client returns an empty list of results, this test verifies that the function correctly processes and outputs an empty list. It mocks the client to simulate a zero-result scenario for a given query.*


### test_crawl_and_summarise_timeout (method, L203-L230, parent: TestQuickResearchTool)

> *Summary: This test verifies that the `_crawl_and_summarise` function returns a page content of `None` when the underlying web crawler times out during execution. It achieves this by mocking the asynchronous crawler to intentionally delay its operation for an extended period.*


### test_crawl_and_summarise_no_summarise (method, L233-L259, parent: TestQuickResearchTool)

> *Summary: This test verifies that when summarization is disabled, the function returns the raw HTML content scraped from a given URL. It mocks the web crawler to inject predefined HTML and asserts that the resulting output contains this exact raw text.*


### test_research_single_query (method, L264-L304, parent: TestQuickResearchTool)

> *Summary: This test verifies the single-query research pipeline by mocking external search and crawling functions. It inputs a query, configuration, and encoding, expecting an output containing the original query and a list of sources with titles and summaries derived from the mocked results.*


### test_quick_research_empty_queries (method, L309-L313, parent: TestQuickResearchTool)

> *Summary: When provided with an empty list of queries, the research tool returns a string representation of an empty list. This test verifies that no output is generated when the input query set is null.*


### test_quick_research_caps_queries (method, L316-L333, parent: TestQuickResearchTool)

> *Summary: This test verifies that the tool limits the number of executed research queries to a predefined maximum, even when provided with more inputs. It mocks the underlying single-query execution and asserts that the resulting data structure contains no more than five entries, corresponding to the call count on the mocked function.*


### test_quick_research_full_pipeline (method, L336-L365, parent: TestQuickResearchTool)

> *Summary: This test verifies the complete research workflow by mocking external search and crawling services. It executes the tool with a specific query, asserting that the returned JSON structure contains one result matching the mocked search title and summary content.*


### test_quick_research_handles_crawl_failures (method, L368-L402, parent: TestQuickResearchTool)

> *Summary: When provided with mock search results and a crawl function that intentionally raises an error for certain URLs, this test verifies that the research tool gracefully skips failed crawls. It asserts that only successfully crawled pages are included in the final output sources.*

