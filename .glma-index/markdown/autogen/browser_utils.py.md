# autogen/browser_utils.py

1 class(es): SimpleTextBrowser. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SimpleTextBrowser | class |  |

## Chunks

### SimpleTextBrowser (class, L35-L310)

> *Summary: This class functions as a text-based web browser, capable of fetching content from URLs or performing Bing searches based on input URIs. It processes HTML by stripping scripts and converting to Markdown (with special handling for Wikipedia), supports plain text and PDF extraction, and can download files if configured. The primary output is the current viewport's text content, which can be navigated using page up/down controls.*


### __init__ (method, L38-L69, parent: SimpleTextBrowser)

> *Summary: Sets up a browser instance by configuring initial settings such as the starting URL, viewport size, download directory, and Bing API credentials. It initializes internal state variables for tracking page history, titles, and content based on these provided parameters.*


### address (method, L72-L74, parent: SimpleTextBrowser)

> *Summary: Retrieves and returns the URL of the most recently visited page from the browser's history stack. This method provides the current page's address as a string output.*


### set_address (method, L76-L95, parent: SimpleTextBrowser)

> *Summary: This method updates the browser's current page by appending the provided URI or path to its history. It handles special cases like "about:blank" and Bing searches, otherwise resolving relative paths before fetching the content.*


### viewport (method, L98-L101, parent: SimpleTextBrowser)

> *Summary: Retrieves and returns a string slice representing the visible area from the stored page content based on the current viewport's defined boundaries. It uses the `viewport_pages` structure to locate the correct start and end indices for slicing the main `page_content`.*


### page_content (method, L104-L106, parent: SimpleTextBrowser)

> *Summary: Retrieves and returns the complete HTML content of the currently loaded web page as a string. This method accesses an internal attribute holding the page's data.*


### _set_page_content (method, L108-L113, parent: SimpleTextBrowser)

> *Summary: Updates the internal page content with a provided string and then triggers a page splitting operation. It ensures the current viewport page index remains within the bounds of available pages after updating the content.*


### page_down (method, L115-L117, parent: SimpleTextBrowser)

> *Summary: Increments the current page index within a set of pages, ensuring it does not exceed the last available page in the viewport. This method updates the internal state to simulate scrolling down one page.*


### page_up (method, L119-L121, parent: SimpleTextBrowser)

> *Summary: Decrements the current viewport page number, ensuring it never drops below zero. This method updates an internal state variable to simulate scrolling the view upwards by one page.*


### visit_page (method, L123-L130, parent: SimpleTextBrowser)

> *Summary: Sets the browser's address to the provided URI or path, then returns the current content visible in the viewport.*


### _split_pages (method, L132-L152, parent: SimpleTextBrowser)

> *Summary: This method divides the page content into chunks based on a predefined viewport size, specifically for web pages starting with `http:` or `https:`. It iterates through the content, creating tuples representing start and end indices, ensuring each chunk ends at whitespace if possible.*


### _bing_api_call (method, L154-L180, parent: SimpleTextBrowser)

> *Summary: This method executes a GET request to the Bing API using a provided search query and an internal API key for authentication. It constructs necessary headers and parameters, sends the HTTP request, checks for errors, and returns the resulting JSON data structure.*


### _bing_search (method, L182-L211, parent: SimpleTextBrowser)

> *Summary: Fetches search results from Bing using a provided query and formats them into structured text. It aggregates web snippets and news items, setting the page title and content accordingly before storing it internally.*


### _fetch_page (method, L213-L310, parent: SimpleTextBrowser)

> *Summary: Fetches content from a given URL, handling HTTP requests and error conditions. It parses the response based on content type—converting HTML to Markdown (with special Wikipedia logic), extracting plain text, or saving PDFs/files for download—and updates internal page title and content attributes accordingly.*

