# autogen/tools/experimental/browser_use/browser_use.py

3 class(es): ExtractedContent, BrowserUseResult, BrowserUseTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ExtractedContent | class |  |
| BrowserUseResult | class |  |
| BrowserUseTool | class |  |

## Chunks

### ExtractedContent (class, L25-L46)

> *Summary: This data model structures content retrieved from a browser, holding the extracted text and an optional URL. It enforces that if the provided URL is `"about:blank"`, it will be normalized to `None`.*


### check_url (method, L38-L46, parent: ExtractedContent)

> *Summary: This method inspects an input string, which is expected to be a URL. It returns `None` if the URL exactly matches `"about:blank"`; otherwise, it returns the original URL string unchanged.*


### BrowserUseResult (class, L50-L59)

> *Summary: This data structure encapsulates the outcome of a browser interaction, holding a list of `ExtractedContent` items and an optional string representing the overall final result. It serves as a standardized container for reporting browsing task completion.*


### BrowserUseTool (class, L74-L153)

> *Summary: This class implements a tool that executes tasks by controlling a web browser via an agent framework. It accepts configuration for the LLM, optional pre-configured browser sessions, and task parameters to return extracted content and the final result of the browsing operation.*


### __init__ (method, L77-L144, parent: BrowserUseTool)

> *Summary: Initializes a tool that executes tasks using a web browser via an agent. It accepts configurations for LLM settings, an existing browser session, and optional arguments/configurations to customize the execution environment before running the task. The method returns a result containing extracted content and the final outcome of the browsing operation.*


### _get_controller (method, L147-L153, parent: BrowserUseTool)

> *Summary: This method extracts the response format from an LLM configuration, checking both a top-level key and within the first element of a `config_list`. It then instantiates and returns a `Controller` object using this extracted format.*

