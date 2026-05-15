# autogen/tools/experimental/tinyfish/tinyfish_tool.py

2 function(s): _execute_tinyfish_scrape, _tinyfish_scrape. 1 class(es): TinyFishTool. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _execute_tinyfish_scrape | function |  |
| _tinyfish_scrape | function |  |
| TinyFishTool | class |  |

## Chunks

### _execute_tinyfish_scrape (function, L27-L52)

> *Summary: This function initiates a goal-directed web scrape by sending a URL, extraction goal, and API key to the TinyFish service. It returns the structured results from the API upon successful completion or an error/no-result status otherwise.*


### _tinyfish_scrape (function, L55-L88)

> *Summary: This function executes a TinyFish scraping operation using a provided URL, extraction goal, and API key. It returns a dictionary containing the original inputs along with either the successfully scraped data or an error object if the execution fails.*


### TinyFishTool (class, L92-L162)

> *Summary: This class provides a tool for performing goal-directed web scraping by interfacing with the TinyFish API. It accepts a target URL and a natural language description of desired data, returning structured results based on that goal.*


### __init__ (method, L105-L162, parent: TinyFishTool)

> *Summary: This constructor initializes the tool by requiring a `tinyfish_api_key`, which it fetches either from an argument or the `TINYFISH_API_KEY` environment variable. It then defines and registers an internal scraping function that takes a URL and a natural language goal to extract structured data using the provided API key.*

