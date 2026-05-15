# autogen/tools/experimental/duckduckgo/duckduckgo_search.py

2 function(s): _execute_duckduckgo_query, _duckduckgo_search. 1 class(es): DuckDuckGoSearchTool. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _execute_duckduckgo_query | function |  |
| _duckduckgo_search | function |  |
| DuckDuckGoSearchTool | class |  |

## Chunks

### _execute_duckduckgo_query (function, L20-L40)

> *Summary: Performs a search using the DuckDuckGo API, accepting a query string and an optional maximum result count. It returns a list of dictionaries containing the retrieved search results or an empty list if an error occurs during execution.*


### _duckduckgo_search (function, L43-L67)

> *Summary: Executes a DuckDuckGo search using a provided query and result limit, then transforms the raw results into a list of dictionaries containing the title, link, and snippet for each entry. It returns this structured list or an empty list if no results are found.*


### DuckDuckGoSearchTool (class, L71-L103)

> *Summary: This tool provides an interface to execute searches via the DuckDuckGo engine without requiring an API key. It accepts a search query string and an optional number of results, returning a list of dictionaries containing titles, links, and snippets for each result.*


### __init__ (method, L78-L103, parent: DuckDuckGoSearchTool)

> *Summary: This method sets up a tool wrapper that exposes a function capable of querying the DuckDuckGo Search API. It accepts a `query` string and an optional `num_results` integer, returning a list of dictionaries containing titles, links, and snippets for the search results.*

