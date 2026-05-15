# autogen/beta/tools/search/duckduckgo.py

3 class(es): SearchResult, SearchResponse, DuckDuckSearchTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SearchResult | class |  |
| SearchResponse | class |  |
| DuckDuckSearchTool | class |  |

## Chunks

### SearchResult (class, L22-L25)

> *Summary: Represents a single search result containing the title, URL link (`href`), and snippet body of an item. This structure is used to hold data returned from a search operation.*


### SearchResponse (class, L29-L31)

> *Summary: Represents the output of a search operation, holding the original query string and a list of `SearchResult` objects. It serves as a structured container for the results returned by a search engine.*


### DuckDuckSearchTool (class, L34-L92)

> *Summary: This class wraps a DuckDuckGo search client to provide a structured tool for web searching. It accepts configuration parameters like maximum results and region, takes a query string as input, and outputs a list of search results containing titles, URLs, and snippets.*


### __init__ (method, L40-L80, parent: DuckDuckSearchTool)

> *Summary: Initializes a search tool that wraps the DuckDuckGo API client to perform web searches. It accepts optional configurations for maximum results, region, and safe search settings, returning structured titles, URLs, and snippets based on a provided query.*


### schemas (method, L82-L83, parent: DuckDuckSearchTool)

> *Summary: Retrieves the schema definitions for available tools by calling an underlying tool's method with the provided context. It returns a list of `FunctionToolSchema` objects describing those tools.*


### register (method, L85-L92, parent: DuckDuckSearchTool)

> *Summary: This method registers the underlying tool with a provided exit stack, execution context, and optional list of middleware components. It delegates the registration process directly to the internal `_tool` object.*

