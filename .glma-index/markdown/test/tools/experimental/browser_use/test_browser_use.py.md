# test/tools/experimental/browser_use/test_browser_use.py

1 function(s): test_browser_use_llm_config_without_context. 2 class(es): TestExtractedContent, TestBrowserUseToolOpenai. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestExtractedContent | class |  |
| TestBrowserUseToolOpenai | class |  |
| test_browser_use_llm_config_without_context | function |  |

## Chunks

### TestExtractedContent (class, L21-L31)

> *Summary: This test verifies that the `ExtractedContent` object correctly sets its URL based on provided inputs. It asserts that a given input URL matches the stored URL, or is set to `None` for specific edge cases like "about:blank".*


### test_url_is_properly_set (method, L29-L31, parent: TestExtractedContent)

> *Summary: This test verifies that the `ExtractedContent` object correctly stores and exposes a provided URL. It takes an input URL and an expected URL, asserting that the object's internal URL matches the expectation.*


### TestBrowserUseToolOpenai (class, L45-L134)

> *Summary: This test suite verifies the functionality and configuration of a `BrowserUseTool`. It tests tool initialization against expected schemas, executes the tool asynchronously with various credentials to extract content from a specified URL, and validates end-to-end execution within an agent chat simulation.*


### test_browser_use_tool_init (method, L46-L61, parent: TestBrowserUseToolOpenai)

> *Summary: This test verifies the initialization of a `BrowserUseTool` instance, ensuring it correctly sets its name and description. It further asserts that the tool's associated function schema matches an expected structure defining a required string parameter named "task".*


### test_browser_use_tool (method, L69-L85, parent: TestBrowserUseToolOpenai)

> *Summary: This test verifies the functionality of a `BrowserUseTool` by executing it against a specific URL task. It initializes the tool with provided credentials and asserts that the returned result is a `BrowserUseResult` containing extracted content.*


### browser_use_tool (method, L88-L89, parent: TestBrowserUseToolOpenai)

> *Summary: Creates and returns a `BrowserUseTool` instance, configuring it using the LLM settings provided within the input `Credentials`.*


### test_get_controller (method, L91-L93, parent: TestBrowserUseToolOpenai)

> *Summary: This test verifies that the `BrowserUseTool` correctly instantiates and returns an object conforming to the `Controller` type when provided with mock credentials containing LLM configuration. It asserts the returned object's type matches the expected controller interface.*


### test_end2end (method, L96-L118, parent: TestBrowserUseToolOpenai)

> *Summary: This test simulates an end-to-end interaction where a user proxy initiates a chat with an assistant to fetch information from a specific URL using a browser tool. It asserts that the resulting chat history contains at least one message where the tool output is successfully parsed as a `BrowserUseResult` object.*


### test_llm_config_current_property (method, L120-L134, parent: TestBrowserUseToolOpenai)

> *Summary: This test verifies that `BrowserUseTool` initializes correctly when an explicit `LLMConfig` object is passed during instantiation. It asserts the tool's name, description, and that its associated function is callable.*


### test_browser_use_llm_config_without_context (function, L137-L144)

> *Summary: Asserts that instantiating `BrowserUseTool` with a `None` value for `llm_config` correctly raises a `ValueError`. This test verifies the required configuration check when no LLM settings are supplied to the tool.*

