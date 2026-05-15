# test/test_browser_utils.py

3 function(s): downloads_folder, test_simple_text_browser, test_bing_search.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| downloads_folder | function |  |
| test_simple_text_browser | function |  |
| test_bing_search | function |  |

## Chunks

### downloads_folder (function, L58-L60)

> *Summary: This generator yields a path to a temporary directory created for use as a download location. It ensures the directory is automatically cleaned up after yielding its value.*


### test_simple_text_browser (function, L64-L148)

> *Summary: This test function verifies the functionality of a text-based web browser by visiting various URLs, asserting page content matches expectations, and testing scrolling mechanics. It also validates file handling by checking downloaded images via MD5 checksums and confirming content retrieval for plain text and PDFs.*


### test_bing_search (function, L156-L173)

> *Summary: This test verifies the functionality of a Bing search by initializing a text browser with specific headers and an API key. It asserts that the resulting page content contains the expected string, matches the correct title, and captures the viewport dimensions accurately.*

