# test/tools/experimental/web_search_preview/test_web_search_preview.py

1 class(es): TestWebSearchPreviewTool. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestWebSearchPreviewTool | class |  |

## Chunks

### TestWebSearchPreviewTool (class, L12-L26)

> *Summary: This test suite verifies the initialization and basic functionality of a web search tool. It confirms the tool's name and description upon instantiation and asserts that calling the tool with a query returns a string response.*


### test_init (method, L13-L17, parent: TestWebSearchPreviewTool)

> *Summary: This test verifies the initialization of a `WebSearchPreviewTool` instance using provided LLM credentials. It asserts that the resulting tool has the correct name and description prefix.*


### test_web_search_preview_f (method, L19-L26, parent: TestWebSearchPreviewTool)

> *Summary: Initializes a web search tool using provided LLM credentials and executes it with a specific query. It asserts that the returned result from the search operation is a string.*

