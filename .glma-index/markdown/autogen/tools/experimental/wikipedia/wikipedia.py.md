# autogen/tools/experimental/wikipedia/wikipedia.py

4 class(es): Document, WikipediaClient, WikipediaQueryRunTool, WikipediaPageLoadTool. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Document | class |  |
| WikipediaClient | class |  |
| WikipediaQueryRunTool | class |  |
| WikipediaPageLoadTool | class |  |

## Chunks

### Document (class, L24-L40)

> *Summary: Represents a Wikipedia document using Pydantic, holding the textual content of the page and a dictionary containing associated metadata like URL, title, and word count. It structures the data retrieved from a Wikipedia source for consistent handling.*


### WikipediaClient (class, L43-L121)

> *Summary: Provides methods to interact with the Wikipedia API for a specified language edition. It accepts a search query or a page title as input, returning a list of search results or a full `WikipediaPage` object, respectively.*


### __init__ (method, L58-L71, parent: WikipediaClient)

> *Summary: Sets up a Wikipedia client by configuring the base API URL and HTTP headers using provided language and tool identifiers. It initializes the underlying `wikipediaapi` object with these settings to enable interaction with the specified Wikipedia edition.*


### search (method, L73-L103, parent: WikipediaClient)

> *Summary: Fetches a list of Wikipedia articles matching a given query string, returning up to a specified limit. It constructs and executes an HTTP GET request to the Wikipedia API, parsing the JSON response to return dictionaries containing titles, sizes, word counts, and timestamps for each result.*


### get_page (method, L105-L121, parent: WikipediaClient)

> *Summary: Retrieves a `WikipediaPage` object from the underlying Wikipedia API using a provided page title string. It returns the page object if it exists, or `None` otherwise, raising an exception for lower-level API failures.*


### WikipediaQueryRunTool (class, L125-L192)

> *Summary: This tool queries a specified language edition of Wikipedia using the `wikipediaapi` package. Given a search string, it returns a list of formatted strings, each containing a page title and its summary, or an error message if the query fails.*


### __init__ (method, L142-L159, parent: WikipediaQueryRunTool)

> *Summary: Sets up the tool by configuring it with a specified language, limiting the number of returned summaries to `top_k`, and enabling verbose logging if requested. It initializes an underlying Wikipedia client and registers itself as a callable tool for running queries.*


### query_run (method, L161-L192, parent: WikipediaQueryRunTool)

> *Summary: This method searches Wikipedia using a provided query string, truncating it if necessary. It returns a list of formatted strings, each containing the page title and summary for found results, or an error message if the search fails or yields no results.*


### WikipediaPageLoadTool (class, L196-L284)

> *Summary: This tool searches Wikipedia for articles matching a given query, returning a list of `Document` objects containing truncated page content and rich metadata like URL and word count. It accepts a string query and returns either the structured list of documents or an error message if the search fails.*


### __init__ (method, L213-L239, parent: WikipediaPageLoadTool)

> *Summary: Sets up a tool to search Wikipedia by configuring the target language, maximum number of results ($\text{top\_k}$), and content truncation length. It initializes an underlying client and registers itself with a specific name and description for use in agent workflows.*


### content_search (method, L241-L284, parent: WikipediaPageLoadTool)

> *Summary: Performs a Wikipedia content search using a provided query string, returning a list of `Document` objects containing truncated page text and metadata if results are found. If the search fails or yields no content, it returns an error message or a specific "No good Wikipedia Search Result was found" string.*

