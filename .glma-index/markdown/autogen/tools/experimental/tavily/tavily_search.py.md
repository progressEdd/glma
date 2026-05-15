# autogen/tools/experimental/tavily/tavily_search.py

2 function(s): _execute_tavily_query, _tavily_search. 1 class(es): TavilySearchTool. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _execute_tavily_query | function |  |
| _tavily_search | function |  |
| TavilySearchTool | class |  |

## Chunks

### _execute_tavily_query (function, L23-L57)

> *Summary: Performs a search using the Tavily API by accepting a query string and various configuration parameters like depth, topic, and result count. It returns the raw response object received from the Tavily client after executing the specified search request.*


### _tavily_search (function, L60-L103)

> *Summary: Executes a Tavily search using provided parameters like query, API key, and result limits to fetch web search results. It returns a list of dictionaries, each containing the title, URL (link), and snippet for the retrieved search items.*


### TavilySearchTool (class, L107-L176)

> *Summary: This class provides a tool wrapper for querying the Tavily Search API. It requires an API key (either provided or via environment variable) and accepts parameters like the search query, result count, and search depth to return a list of structured search results.*


### __init__ (method, L118-L176, parent: TavilySearchTool)

> *Summary: This constructor initializes a tool by requiring a Tavily API key, falling back to an environment variable if not provided. It then defines and registers a `tavily_search` function that accepts various search parameters like query, depth, and result count to execute searches via the Tavily API and return structured results.*

