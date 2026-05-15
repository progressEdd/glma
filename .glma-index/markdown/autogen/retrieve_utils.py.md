# autogen/retrieve_utils.py

10 function(s): split_text_to_chunks, extract_text_from_pdf, split_files_to_chunks, get_files_from_dir, parse_html_to_markdown, _generate_file_name_from_url, get_file_from_url, is_url, create_vector_db_from_dir, query_vector_db.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| split_text_to_chunks | function |  |
| extract_text_from_pdf | function |  |
| split_files_to_chunks | function |  |
| get_files_from_dir | function |  |
| parse_html_to_markdown | function |  |
| _generate_file_name_from_url | function |  |
| get_file_from_url | function |  |
| is_url | function |  |
| create_vector_db_from_dir | function |  |
| query_vector_db | function |  |

## Chunks

### split_text_to_chunks (function, L80-L135)

> *Summary: This function segments a large string into smaller text blocks based on a maximum token limit, configurable chunking modes, and optional line-based breaking rules. It iteratively finds optimal split points to ensure no resulting chunk exceeds `max_tokens`, while also enforcing a minimum length for each output segment.*


### extract_text_from_pdf (function, L139-L158)

> *Summary: Reads a specified PDF file, handling potential encryption by attempting decryption before iterating through all pages to concatenate their extracted text content. Returns the aggregated string of text found in the PDF, or an empty string if extraction fails due to encryption issues.*


### split_files_to_chunks (function, L161-L201)

> *Summary: Reads content from a list of files (which can be paths or `(path, url)` tuples), handling various formats like PDF and unstructured data. It then splits the aggregated text into smaller chunks based on token limits and returns both the list of text chunks and corresponding source metadata for each chunk.*


### get_files_from_dir (function, L204-L251)

> *Summary: Retrieves a list of file paths based on a provided directory, URL, or list of items, filtering by specified extensions. It supports recursive traversal and handles inputs that are individual files, URLs (by downloading them), or directories.*


### parse_html_to_markdown (function, L255-L283)

> *Summary: Converts an HTML string into a Markdown formatted string. It strips script and style tags, and if the URL is from Wikipedia, it specifically targets content within `mw-content-text` for cleaner conversion before applying final formatting with the page title.*


### _generate_file_name_from_url (function, L286-L294)

> *Summary: Creates a unique filename from a URL by combining the network location, the original basename, and a truncated hash of the full URL. It ensures the resulting string does not exceed a specified maximum length.*


### get_file_from_url (function, L297-L331)

> *Summary: Downloads a file from a given URL to a specified or default path. It handles both binary downloads and HTML content by parsing the latter into Markdown before saving it. Returns a tuple containing the local save path and the original URL.*


### is_url (function, L334-L340)

> *Summary: Checks if an input string conforms to a valid URL structure by attempting to parse it using `urlparse`. It returns `True` only if both a scheme and network location are present in the parsed result, otherwise returning `False`.*


### create_vector_db_from_dir (function, L344-L433)

> *Summary: Ingests files from a specified directory (or list/URL) and processes them into chunks using configurable text splitting and embedding models. It then populates or retrieves a ChromaDB collection with these document embeddings, returning the initialized database client.*


### query_vector_db (function, L437-L490)

> *Summary: Retrieves relevant documents from a vector database based on input text queries. It takes query texts and optional parameters like the number of results, database path, and embedding configuration to return structured results containing IDs, documents, and metadata.*

