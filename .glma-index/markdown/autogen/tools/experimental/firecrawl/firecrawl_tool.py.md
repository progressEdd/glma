# autogen/tools/experimental/firecrawl/firecrawl_tool.py

10 function(s): _execute_firecrawl_scrape, _execute_firecrawl_crawl, _execute_firecrawl_map, _execute_firecrawl_search, _execute_firecrawl_deep_research, _firecrawl_scrape, _firecrawl_crawl, _firecrawl_map, _firecrawl_search, _firecrawl_deep_research. 1 class(es): FirecrawlTool. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _execute_firecrawl_scrape | function |  |
| _execute_firecrawl_crawl | function |  |
| _execute_firecrawl_map | function |  |
| _execute_firecrawl_search | function |  |
| _execute_firecrawl_deep_research | function |  |
| _firecrawl_scrape | function |  |
| _firecrawl_crawl | function |  |
| _firecrawl_map | function |  |
| _firecrawl_search | function |  |
| _firecrawl_deep_research | function |  |
| FirecrawlTool | class |  |

## Chunks

### _execute_firecrawl_scrape (function, L28-L69)

> *Summary: Performs a web scraping operation by calling the Firecrawl API using a provided URL and API key. It accepts various optional parameters to control output formats, included/excluded HTML tags, headers, waiting time, and request timeout, returning the resulting scrape data as a dictionary.*


### _execute_firecrawl_crawl (function, L78-L127)

> *Summary: Performs a web crawl using the Firecrawl API, taking a starting URL and various configuration parameters like output formats, depth limits, and inclusion/exclusion patterns. It returns the complete crawl result as a dictionary.*


### _execute_firecrawl_map (function, L136-L168)

> *Summary: This function performs a website mapping operation by calling the Firecrawl API. It takes a target URL and various configuration parameters like search terms, subdomain inclusion, and result limits to return a dictionary containing the scraped map results.*


### _execute_firecrawl_search (function, L177-L218)

> *Summary: Performs a search operation against the Firecrawl API using provided parameters like query, API key, and various filters. It accepts numerous optional arguments to customize the search scope (e.g., language, country, time range) and returns the resulting data as a dictionary.*


### _execute_firecrawl_deep_research (function, L227-L262)

> *Summary: Performs an in-depth research operation by calling the Firecrawl API using a provided query and API key. It accepts various constraints like maximum depth, time limit, and custom prompts to return the resulting data structure from the service.*


### _firecrawl_scrape (function, L265-L316)

> *Summary: Executes a web scraping operation against a specified URL using the Firecrawl API, accepting various configuration options like output formats and tag filtering. It returns a list containing a dictionary structured with the scraped title, URL, content (markdown or HTML), and metadata upon success, or an empty list on failure.*


### _firecrawl_crawl (function, L319-L378)

> *Summary: Executes a web crawl using the Firecrawl API, taking a starting URL and an API key as primary inputs along with various configuration options like depth limits and path filters. It returns a list of dictionaries, where each dictionary contains the title, URL, content (markdown or HTML), and metadata for a successfully crawled page.*


### _firecrawl_map (function, L381-L430)

> *Summary: Executes a Firecrawl mapping operation on a given URL using an API key and optional parameters like search terms or subdomain inclusion. It processes the raw results, extracting only the URLs into a list of dictionaries, returning this list upon success or an empty list if an error occurs.*


### _firecrawl_search (function, L433-L493)

> *Summary: Executes a Firecrawl search using provided parameters like query, API key, and various filters to fetch web results. It processes the raw response into a standardized list of dictionaries containing title, URL, content (markdown or HTML), description, and metadata for each result.*


### _firecrawl_deep_research (function, L496-L557)

> *Summary: Executes a comprehensive web research operation using the Firecrawl API based on a provided query and API key. It accepts configuration parameters like search depth and time limits, returning a structured dictionary containing the final analysis, sources, and summaries of the findings.*


### FirecrawlTool (class, L561-L842)

> *Summary: This class provides an interface to the Firecrawl API, enabling web content extraction and research via five distinct methods: scraping a single URL, recursively crawling a site, mapping URLs, performing targeted searches, and executing deep topic research. It requires a valid `firecrawl_api_key` for all operations and exposes these functionalities as callable attributes.*


### __init__ (method, L580-L842, parent: FirecrawlTool)

> *Summary: This class initializes a deprecated tool for interacting with the Firecrawl API, requiring an API key or environment variable to function. It exposes several methods—`scrape`, `crawl`, `map`, `search`, and `deep_research`—to perform URL scraping, website crawling, URL mapping, web searching, and in-depth research using the provided credentials.*

