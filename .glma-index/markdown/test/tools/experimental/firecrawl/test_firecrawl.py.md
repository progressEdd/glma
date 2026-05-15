# test/tools/experimental/firecrawl/test_firecrawl.py

1 class(es): TestFirecrawlTool. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestFirecrawlTool | class |  |

## Chunks

### TestFirecrawlTool (class, L16-L347)

> *Summary: This test suite validates the `FirecrawlTool` by mocking API responses for scraping, crawling, and mapping operations. It verifies correct initialization with required keys, schema generation, and proper execution of methods using both default and custom API endpoints.*


### mock_scrape_response (method, L22-L30, parent: TestFirecrawlTool)

> *Summary: Provides a predefined dictionary simulating the output of a web scraping operation. This mock returns structured data containing markdown, HTML content, and associated metadata like title and source URL.*


### mock_crawl_response (method, L33-L53, parent: TestFirecrawlTool)

> *Summary: Provides a fixed dictionary structure simulating the output of a web crawling operation. This mock returns a list containing two sample page objects, each with markdown content, HTML markup, and associated metadata like title and source URL.*


### mock_map_response (method, L56-L63, parent: TestFirecrawlTool)

> *Summary: Provides a predefined dictionary simulating a map response containing a list of example URLs. This mock data is used to test components that expect structured link information from a mapping service.*


### test_initialization (method, L65-L68, parent: TestFirecrawlTool)

> *Summary: Verifies that an instance of `FirecrawlTool`, initialized with a test API key, correctly sets its name and includes the expected description detailing its scraping functionality.*


### test_initialization_with_api_url (method, L70-L73, parent: TestFirecrawlTool)

> *Summary: Verifies that an instance of the tool correctly stores the provided API key and custom URL when initialized with specific string inputs. It asserts that the internal attributes match the input values.*


### test_initialization_no_api_key (method, L75-L77, parent: TestFirecrawlTool)

> *Summary: Asserts that instantiating the tool without providing an API key raises a `ValueError` containing a specific message. This verifies the mandatory requirement for the API key during object creation.*


### test_schema_validation (method, L79-L155, parent: TestFirecrawlTool)

> *Summary: This test verifies that the `FirecrawlTool` correctly generates a predefined JSON schema for its `firecrawl_scrape` function. It asserts that the tool's generated schema matches an expected structure, which defines parameters like URL, output formats, and various request options.*


### test_scrape_success (method, L158-L169, parent: TestFirecrawlTool)

> *Summary: When provided with a mock response, this test verifies that the `FirecrawlTool` successfully scrapes a given URL. It asserts that the output is a list containing one item with expected title, URL, and content matching the mocked data.*


### test_scrape_with_options (method, L172-L188, parent: TestFirecrawlTool)

> *Summary: This test verifies the `FirecrawlTool`'s scraping functionality when provided with various configuration options like desired formats, included/excluded tags, and custom headers. It asserts that the tool successfully executes the scrape using mocked dependencies and returns a list containing one result.*


### test_crawl_success (method, L191-L199, parent: TestFirecrawlTool)

> *Summary: This test verifies successful crawling by mocking the execution and response. It calls the `crawl` method with a URL and limit, asserting that the returned list contains exactly two items with predefined titles.*


### test_map_success (method, L202-L211, parent: TestFirecrawlTool)

> *Summary: This test verifies the successful execution of a mapping operation by mocking the underlying API response. It asserts that the `map` method returns a list containing three specific URLs derived from the input URL.*


### test_scrape_with_custom_api_url (method, L214-L243, parent: TestFirecrawlTool)

> *Summary: Tests the `FirecrawlTool`'s ability to scrape a given URL using a specified custom API endpoint and key. It asserts that the underlying execution function is called with these custom parameters and verifies the returned scraped content matches the expected structure.*


### test_crawl_with_custom_api_url (method, L246-L291, parent: TestFirecrawlTool)

> *Summary: This test verifies that the `FirecrawlTool` correctly uses a specified custom API URL when crawling a given URL, asserting that the underlying execution function is called with all provided parameters. It then confirms the returned crawl results match an expected structure containing page data.*


### test_map_with_custom_api_url (method, L294-L318, parent: TestFirecrawlTool)

> *Summary: This test verifies that the `FirecrawlTool` correctly uses a specified custom API URL when performing a mapping operation on a given URL. It asserts that the underlying execution function is called with the correct custom parameters and validates the returned structured data against an expected list of mapped URLs.*


### test_search_invalid_query (method, L320-L323, parent: TestFirecrawlTool)

> *Summary: This test verifies that providing a `None` value for the URL input to the tool raises a `ValidationError`. It instantiates the tool with a test API key and asserts the expected exception during execution.*


### test_integration_live_scrape (method, L326-L330, parent: TestFirecrawlTool)

> *Summary: This test verifies the integration of a live scraping tool by passing a URL to it and asserting that the returned result is a non-empty list. It uses a placeholder API key for execution.*


### test_agent_integration (method, L333-L347, parent: TestFirecrawlTool)

> *Summary: This test verifies agent functionality by initializing an assistant with a `FirecrawlTool` and executing it against a prompt requesting web scraping from a specific URL. It asserts that the assistant successfully returns a non-null response after running for a maximum of two turns.*

