# autogen/tools/experimental/searxng/searxng_search.py

2 function(s): _execute_searxng_query, _searxng_search. 1 class(es): SearxngSearchTool. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _execute_searxng_query | function |  |
| _searxng_search | function |  |
| SearxngSearchTool | class |  |

## Chunks

### _execute_searxng_query (function, L20-L62)

> *Summary: Performs a web search by sending a GET request to a specified SearxNG instance URL, using the provided query and optional parameters like language or categories. It returns a list of dictionaries containing the structured search results from the API response, or an empty list upon failure.*


### _searxng_search (function, L65-L95)

> *Summary: Executes a search against a specified SearxNG instance using the provided query and optional filters like categories or language. It returns a list of dictionaries, each containing the title, URL, and snippet for the top results.*


### SearxngSearchTool (class, L99-L149)

> *Summary: This tool provides an interface to execute searches via a specified SearxNG instance URL. It accepts a search query and optional parameters like result limits or categories, returning a list of dictionaries containing the title, link, and snippet for each found result.*


### __init__ (method, L106-L123, parent: SearxngSearchTool)

> *Summary: This constructor initializes a tool for performing searches via a specified SearxNG instance URL. It issues a deprecation warning advising users to switch to DuckDuckGo or Tavily tools and sets up the necessary search function reference.*


### searxng_search (method, L125-L149, parent: SearxngSearchTool)

> *Summary: Executes a search against the SearxNG API using provided query parameters like text, result limit, categories, and language. It returns a list of dictionaries, where each dictionary contains the title, link, and snippet for a found search result.*

