# autogen/tools/experimental/web_search_preview/web_search_preview.py

1 class(es): WebSearchPreviewTool. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WebSearchPreviewTool | class |  |

## Chunks

### WebSearchPreviewTool (class, L27-L127)

> *Summary: This class wraps OpenAI's `web_search_preview` functionality, initializing with LLM configuration and optional context parameters like location and instructions. It exposes a function that takes a search query as input and returns either the raw text result or a structured object based on the provided format.*


### __init__ (method, L30-L127, parent: WebSearchPreviewTool)

> *Summary: Initializes a deprecated tool for performing web searches by configuring LLM settings, context size, and user location. It validates the `llm_config` to ensure an appropriate GPT-4 model is available before setting up the internal search function which takes a query string as input and returns either formatted text or a structured object based on configuration.*

