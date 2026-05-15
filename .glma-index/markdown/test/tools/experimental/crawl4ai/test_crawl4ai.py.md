# test/tools/experimental/crawl4ai/test_crawl4ai.py

1 class(es): TestCrawl4AITool. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestCrawl4AITool | class |  |

## Chunks

### TestCrawl4AITool (class, L20-L146)

> *Summary: This test suite verifies the functionality of a web crawling tool by testing its initialization, schema generation, and execution paths. It validates behavior both without an LLM and with LLM integration, including scenarios for structured data extraction using provided schemas.*


### test_without_llm (method, L22-L45, parent: TestCrawl4AITool)

> *Summary: This test verifies the initialization and functionality of a `Crawl4AITool` instance without relying on an LLM. It asserts that the tool has the correct metadata schema and successfully executes with a provided URL to return a string result.*


### test_get_crawl_config (method, L54-L77, parent: TestCrawl4AITool)

> *Summary: This test verifies the configuration returned by a function when setting up a crawl job, accepting credentials and an optional extraction model schema as input. It asserts that the resulting `CrawlerRunConfig` correctly reflects whether an extraction model was provided, validating provider details and schema presence accordingly.*


### test_with_llm (method, L81-L88, parent: TestCrawl4AITool)

> *Summary: Instantiates a crawling tool configured with OpenAI credentials and executes it against a specified URL using an instruction prompt. It asserts that the returned result is a string containing the extracted information.*


### test_with_llm_and_extraction_schema (method, L92-L107, parent: TestCrawl4AITool)

> *Summary: This test verifies that a tool configured with an LLM and a specific extraction schema can process a given URL. It asserts that calling the tool with a target URL and instruction returns a string result containing the extracted data.*


### test_validate_llm_strategy_kwargs (method, L131-L146, parent: TestCrawl4AITool)

> *Summary: This test verifies the argument validation logic for LLM strategy configurations. It calls a private method with provided keyword arguments and configuration status, asserting either that no error is raised or that a specific `ValueError` matching an expected message occurs.*

