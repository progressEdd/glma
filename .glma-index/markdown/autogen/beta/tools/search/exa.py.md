# autogen/beta/tools/search/exa.py

6 class(es): ExaSearchResult, ExaSearchResponse, ExaContentResult, ExaAnswerCitation, ExaAnswerResult, ExaToolkit. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ExaSearchResult | class |  |
| ExaSearchResponse | class |  |
| ExaContentResult | class |  |
| ExaAnswerCitation | class |  |
| ExaAnswerResult | class |  |
| ExaToolkit | class |  |

## Chunks

### ExaSearchResult (class, L33-L39)

> *Summary: Represents a single result from an Exa search query, holding metadata such as the title, URL, relevance score, publication date, author, and snippet text. It structures the output data returned by the external search tool.*


### ExaSearchResponse (class, L43-L45)

> *Summary: Represents the structured output from an Exa search, containing the original query string and a list of detailed search results. It acts as a container for the data returned by the external search tool.*


### ExaContentResult (class, L49-L54)

> *Summary: This class structures the data returned from an Exa search, holding a URL, title, and main text content. It optionally stores author and publication date information for each result.*


### ExaAnswerCitation (class, L58-L61)

> *Summary: Represents a citation from an Exa search result, storing the source URL, title, and relevant text snippet. This class acts as a data structure to hold structured information retrieved during a search operation.*


### ExaAnswerResult (class, L65-L67)

> *Summary: This class structures the output from an Exa search, holding a primary string answer and an optional list of citation objects. It serves as a container for the retrieved information.*


### ExaToolkit (class, L70-L326)

> *Summary: Provides an interface to the Exa search engine by exposing four distinct tools: web searching, finding similar pages, fetching URL contents, and generating AI-powered answers with citations. It initializes with an optional API key and returns callable functions for each specific Exa endpoint.*


### __init__ (method, L105-L122, parent: ExaToolkit)

> *Summary: Initializes the toolset by configuring API keys and optional search parameters like result count and character limits. It then registers several core search functionalities—including general search, similarity finding, content retrieval, and answering—under a unified "exa\_toolkit" name.*


### search (method, L124-L202, parent: ExaToolkit)

> *Summary: This method generates a tool that queries the Exa search engine using a provided query string and various optional filters like date ranges, domains, and result limits. It returns a structured `ToolResult` containing ranked search results with titles, URLs, scores, and text content.*


### find_similar (method, L204-L255, parent: ExaToolkit)

> *Summary: This method generates a tool that queries the Exa API to discover web pages similar to a provided URL. It accepts optional parameters like result count, domain inclusions/exclusions, and category filters before returning a list of structured search results.*


### get_contents (method, L257-L293, parent: ExaToolkit)

> *Summary: This method generates a tool that fetches the complete text content from a provided list of URLs using an Exa API client. It takes a list of strings (URLs) and returns a `ToolResult` containing structured content objects for each successfully fetched page.*


### answer (method, L295-L326, parent: ExaToolkit)

> *Summary: This method generates a callable tool that uses the Exa API to generate an AI-powered answer to a given query, including associated web citations. It takes a question string and returns a `ToolResult` containing the generated answer text and a list of citation objects.*

