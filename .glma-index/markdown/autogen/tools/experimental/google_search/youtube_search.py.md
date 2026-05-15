# autogen/tools/experimental/google_search/youtube_search.py

3 function(s): _execute_search_query, _get_video_details, _youtube_search. 1 class(es): YoutubeSearchTool. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _execute_search_query | function |  |
| _get_video_details | function |  |
| _youtube_search | function |  |
| YoutubeSearchTool | class |  |

## Chunks

### _execute_search_query (function, L23-L44)

> *Summary: This function performs a YouTube video search by calling the YouTube Data API, accepting a query string, an API key, and a maximum result count as input. It returns the complete search response object from the API or re-raises any encountered HTTP errors.*


### _get_video_details (function, L51-L74)

> *Summary: Fetches detailed metadata for a list of YouTube video IDs using the provided API key and the YouTube Data API. It constructs and executes a `videos().list` request, returning the full response object or re-raising any encountered HTTP errors.*


### _youtube_search (function, L77-L133)

> *Summary: Performs a YouTube search using an API key and query, returning a list of video dictionaries. It first fetches basic search results and optionally calls another function to enrich these results with detailed statistics like view count and duration if requested.*


### YoutubeSearchTool (class, L137-L181)

> *Summary: This tool interfaces with the YouTube Data API to find relevant videos. It accepts a search query and optional parameters like maximum results or detail inclusion, returning a list of video information dictionaries.*


### __init__ (method, L140-L181, parent: YoutubeSearchTool)

> *Summary: This constructor initializes a search tool that requires a YouTube API key to function. It exposes a callable method accepting a search query and optional parameters like result count or detail level, returning a list of video information dictionaries.*

