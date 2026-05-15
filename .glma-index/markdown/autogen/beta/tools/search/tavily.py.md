# autogen/beta/tools/search/tavily.py

3 class(es): SearchResult, SearchResponse, TavilySearchTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SearchResult | class |  |
| SearchResponse | class |  |
| TavilySearchTool | class |  |

## Chunks

### SearchResult (class, L29-L33)

> *Summary: Represents a single search result containing the title, URL, and content of a retrieved item. It optionally includes a relevance score for ranking purposes.*


### SearchResponse (class, L37-L41)

> *Summary: This data structure holds the output from a search operation, containing the original query, a list of detailed search results, an optional synthesized answer, and any associated image URLs. It serves as a container for all relevant information returned by a search tool.*


### TavilySearchTool (class, L44-L141)

> *Summary: This class wraps the Tavily search API to provide web search functionality within an agent framework. It accepts numerous optional parameters like query, result limits, and date ranges to configure the search before executing the asynchronous request via `httpx`. The output is a structured `ToolResult` containing search results, potentially an LLM-generated answer, and images.*


### __init__ (method, L47-L129, parent: TavilySearchTool)

> *Summary: Initializes a search tool wrapper for Tavily, accepting numerous optional parameters like API keys, result limits, and date ranges. It exposes an asynchronous method that takes a query string and context to perform web searches, returning structured results including titles, URLs, snippets, and optionally an LLM-generated answer.*


### schemas (method, L131-L132, parent: TavilySearchTool)

> *Summary: Retrieves the schema definitions for available tools by calling the underlying tool's method with a given context. It returns a list of `FunctionToolSchema` objects describing those tools.*


### register (method, L134-L141, parent: TavilySearchTool)

> *Summary: This method delegates the registration process to an underlying tool object, accepting an exit stack, a context, and optional middleware for configuration. It ensures the tool is properly set up within the provided execution environment.*

