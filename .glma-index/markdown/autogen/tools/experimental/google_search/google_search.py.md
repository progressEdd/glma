# autogen/tools/experimental/google_search/google_search.py

2 function(s): _execute_query, _google_search. 1 class(es): GoogleSearchTool. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _execute_query | function |  |
| _google_search | function |  |
| GoogleSearchTool | class |  |

## Chunks

### _execute_query (function, L24-L26)

> *Summary: This function executes a Google Custom Search API query using provided credentials and parameters. It takes the search term, API key, engine ID, and desired result count as input, returning the raw JSON response from the search service.*


### _google_search (function, L29-L42)

> *Summary: This function executes a Google search using provided credentials and parameters, returning a list of dictionaries containing the title, link, and snippet for each search result. It processes the raw API response to extract only these key pieces of information.*


### GoogleSearchTool (class, L46-L93)

> *Summary: This class provides an interface to execute searches via the Google Search API. It accepts optional API credentials and determines whether to use internal LLM tooling or external API keys based on configuration flags. The primary method takes a search query and returns a list of structured search results.*


### __init__ (method, L49-L93, parent: GoogleSearchTool)

> *Summary: Initializes a tool capable of performing Google searches, accepting optional API keys and engine IDs. It configures whether to use an internal LLM-based search or rely on external credentials, raising errors if required parameters are missing based on the configuration.*

