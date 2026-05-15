# autogen/beta/tools/search/perplexity.py

4 class(es): PerplexitySearchResult, PerplexityImageMeta, PerplexitySearchResponse, PerplexitySearchToolkit. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| PerplexitySearchResult | class |  |
| PerplexityImageMeta | class |  |
| PerplexitySearchResponse | class |  |
| PerplexitySearchToolkit | class |  |

## Chunks

### PerplexitySearchResult (class, L35-L39)

> *Summary: Represents a single search result from the Perplexity API, holding the title, URL, and optional snippet or date information. It structures the data returned for each item found during a search query.*


### PerplexityImageMeta (class, L43-L48)

> *Summary: This class serves as a data structure to hold metadata for an image, accepting the primary `image_url` and optional fields like `origin_url`, `title`, `width`, and `height`. It encapsulates all relevant descriptive information associated with a specific image resource.*


### PerplexitySearchResponse (class, L52-L57)

> *Summary: This data structure holds the complete output from a Perplexity search, containing the original query, a list of detailed results, summary content, citation references, and any associated images. It serves as a container for all retrieved information returned by the search tool.*


### PerplexitySearchToolkit (class, L60-L284)

> *Summary: This class provides two distinct tools wrapping the Perplexity search APIs: one for raw web searches and another for LLM-generated answers with citations. It initializes by accepting API credentials and configuration options, then exposes methods to generate specialized `FunctionTool` instances for agent use.*


### __init__ (method, L90-L111, parent: PerplexitySearchToolkit)

> *Summary: Initializes the search tool by storing configuration parameters like API keys, proxy settings, and timeouts. It then calls its parent constructor, registering itself as a "perplexity\_toolkit" with specified middleware.*


### search (method, L113-L175, parent: PerplexitySearchToolkit)

> *Summary: Generates a callable tool that executes web searches using the Perplexity Search API. It accepts a search query and optional filtering parameters (like domain or date ranges) to return structured search results containing titles, URLs, snippets, and dates.*


### answer (method, L177-L284, parent: PerplexitySearchToolkit)

> *Summary: Generates a comprehensive answer to a given query by querying Perplexity AI, incorporating web citations and search results. It accepts various optional parameters like model selection, context size, and filtering options, returning the generated content along with structured data for related searches and images.*

