# autogen/tools/experimental/quick_research/quick_research.py

9 function(s): _reg_dom, _clean_html, _split_tokens, _ask_llm, _ask_llm_async, _summarise_text_async, _crawl_and_summarise, _tavily_search, _research_single_query. 1 class(es): QuickResearchTool. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _reg_dom | function |  |
| _clean_html | function |  |
| _split_tokens | function |  |
| _ask_llm | function |  |
| _ask_llm_async | function |  |
| _summarise_text_async | function |  |
| _crawl_and_summarise | function |  |
| _tavily_search | function |  |
| _research_single_query | function |  |
| QuickResearchTool | class |  |

## Chunks

### _reg_dom (function, L52-L55)

> *Summary: This helper function parses a network location string to extract the primary registered domain and its suffix. It returns the full domain name, or just the domain part if no suffix is found.*


### _clean_html (function, L58-L77)

> *Summary: This function strips HTML content by removing media and script tags, then filters out anchor links pointing to external domains or specific asset types. It returns a cleaned string containing only the extracted text, formatted with appropriate line breaks and spacing.*


### _split_tokens (function, L83-L92)

> *Summary: This function segments a string into overlapping chunks based on token limits defined by an encoder object. It takes text and an encoder, returning a list of strings where each chunk is approximately `MAX_CHUNK_TOKENS` long with an overlap of `OVERLAP_TOKENS`.*


### _ask_llm (function, L98-L121)

> *Summary: This function synchronously queries an LLM using provided configuration and prompts to generate a response. It takes a list of configurations, a user prompt, and a system message, returning the stripped text content from the LLM's output or an empty string upon failure.*


### _ask_llm_async (function, L124-L126)

> *Summary: This asynchronous helper executes the synchronous `_ask_llm` function within a separate thread to prevent blocking the event loop. It accepts configuration lists, prompts, and system messages, returning the resulting string from the LLM call.*


### _summarise_text_async (function, L129-L163)

> *Summary: This asynchronous function summarizes a potentially long text by first checking if it fits within the model's input limit, truncating if necessary. If too large, it splits the text into chunks, asynchronously queries an LLM for each chunk's partial summary, and then uses a final LLM call to merge these partial summaries into one cohesive output.*


### _crawl_and_summarise (function, L169-L237)

> *Summary: Fetches content from a given URL using an asynchronous web crawler and optionally generates an LLM summary of the cleaned text. It returns a dictionary containing the URL, fetch timestamp, the processed page content (either raw or summarized), and detailed timing metrics for each stage.*


### _tavily_search (function, L243-L260)

> *Summary: This function queries the Tavily Search API using a provided search string and API key to fetch relevant web results. It returns a list of dictionaries, where each dictionary contains the title and URL for a specified number of top search results.*


### _research_single_query (function, L266-L310)

> *Summary: This asynchronous function performs a complete research cycle for one query by first searching using Tavily. It then crawls and summarizes the top search results concurrently before compiling a final dictionary containing the original query and a list of summarized sources.*


### QuickResearchTool (class, L318-L430)

> *Summary: This tool executes parallel web research across a list of input queries. For each query, it uses Tavily to find top results, crawls those URLs with `crawl4ai`, and then summarizes the content using an LLM configured via provided settings. It returns a JSON string containing structured summaries for all processed queries.*


### __init__ (method, L334-L430, parent: QuickResearchTool)

> *Summary: Initializes a research tool by configuring an LLM setup and validating the presence of a Tavily API key. It internally defines an asynchronous function that takes a list of search queries to perform parallel web searches, crawl results, and summarize content using the provided configurations.*

