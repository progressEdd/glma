# test/agents/experimental/websurfer/test_websurfer.py

4 class(es): WebSurferTestHelper, TestCrawl4AIWebSurfer, TestBrowserUseWebSurfer, TestFirecrawlWebSurfer. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WebSurferTestHelper | class |  |
| TestCrawl4AIWebSurfer | class |  |
| TestBrowserUseWebSurfer | class |  |
| TestFirecrawlWebSurfer | class |  |

## Chunks

### WebSurferTestHelper (class, L17-L51)

> *Summary: Provides utility methods for testing `WebSurferAgent` instances; it includes a helper to verify if a specific tool was called within the chat history of a result. The primary test function initiates a conversation with the agent using a provided URL and asserts that the expected web-scraping tool was invoked.*


### _check_tool_called (method, L19-L24, parent: WebSurferTestHelper)

> *Summary: Determines if a specific tool was invoked within the provided chat history by iterating through messages and checking for a matching `tool_calls` entry. It returns `True` if the specified `tool_name` is found in any message's tool calls, otherwise it returns `False`.*


### test_init (method, L26-L35, parent: WebSurferTestHelper)

> *Summary: This test verifies the initialization of a `WebSurferAgent` by ensuring its internal configuration (`llm_config`) is correctly set based on provided credentials and matches an expected structure containing specific tools. It asserts that the configuration object is neither `False` nor of an incorrect type.*


### test_end2end (method, L37-L51, parent: WebSurferTestHelper)

> *Summary: This test verifies the end-to-end functionality of a `WebSurferAgent` by initiating a chat with it. It uses a provided URL as input and asserts that the agent successfully calls the specified web tool (`browser_use`, `crawl4ai`, or `firecrawl`) during the interaction.*


### TestCrawl4AIWebSurfer (class, L55-L91)

> *Summary: This test suite verifies the initialization and end-to-end functionality of a web surfing agent specifically using the `crawl4ai` tool. It asserts that the agent correctly exposes a function capable of crawling a URL based on a provided instruction.*


### test_init (method, L58-L84, parent: TestCrawl4AIWebSurfer)

> *Summary: This test verifies the initialization process by asserting that a specific function definition for `crawl4ai` is correctly generated. It uses provided mock credentials and an expected structure to confirm the agent's setup includes the necessary web crawling tool schema.*


### test_end2end (method, L88-L91, parent: TestCrawl4AIWebSurfer)

> *Summary: This test method executes an end-to-end workflow, inheriting a base test and optionally running it with different web scraping tools like `browser_use`, `crawl4ai`, or `firecrawl`. It accepts OpenAI credentials and the specific tool to use as inputs.*


### TestBrowserUseWebSurfer (class, L95-L125)

> *Summary: This test suite verifies the initialization and end-to-end functionality of a web surfer agent specifically using the `browser_use` tool. It asserts that the agent correctly exposes the browser usage function with its expected parameters when initialized.*


### test_init (method, L98-L118, parent: TestBrowserUseWebSurfer)

> *Summary: This test method verifies the initialization process by asserting that a specific function definition for `browser_use` is correctly registered. It uses provided mock credentials and an expected structure to confirm the agent's setup includes the browser tool capability.*


### test_end2end (method, L122-L125, parent: TestBrowserUseWebSurfer)

> *Summary: This test method executes an end-to-end workflow, inheriting a base test while optionally allowing the use of different web scraping tools like `crawl4ai` or `firecrawl`. It primarily serves to validate system functionality across various browser interaction methods.*


### TestFirecrawlWebSurfer (class, L129-L217)

> *Summary: This test suite verifies the initialization and end-to-end functionality of a `WebSurferAgent` configured to use the Firecrawl tool. It asserts that the agent correctly exposes the expected function schema for scraping URLs via its tools and successfully executes a chat interaction using the Firecrawl API.*


### test_init (method, L132-L190, parent: TestFirecrawlWebSurfer)

> *Summary: This test verifies the initialization of a `WebSurferAgent` by asserting that its internal tool configuration matches an expected structure, specifically when configured to use the "firecrawl" web tool with a provided API key. It confirms the agent correctly incorporates the specified LLM configuration and tools upon instantiation.*


### test_end2end (method, L195-L217, parent: TestFirecrawlWebSurfer)

> *Summary: This test verifies the end-to-end functionality of a `WebSurferAgent` by initiating a chat with it. It uses the agent to scrape information from a specified URL via the configured web tool and asserts that the scraping function was called during the interaction.*

