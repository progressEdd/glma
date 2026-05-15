# autogen/agents/experimental/document_agent/document_utils.py

9 function(s): is_url, _download_rendered_html, _download_binary_file, _get_extension_from_file_type, _is_valid_extension_for_file_type, download_url, list_files, handle_input, preprocess_path. 3 class(es): QueryType, Ingest, Query.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| QueryType | class |  |
| Ingest | class |  |
| Query | class |  |
| is_url | function |  |
| _download_rendered_html | function |  |
| _download_binary_file | function |  |
| _get_extension_from_file_type | function |  |
| _is_valid_extension_for_file_type | function |  |
| download_url | function |  |
| list_files | function |  |
| handle_input | function |  |
| preprocess_path | function |  |

## Chunks

### QueryType (class, L28-L30)

> *Summary: Defines an enumeration for different types of queries, currently including `RAG_QUERY` to specify retrieval-augmented generation requests. This enum serves as a constant set of query identifiers used throughout the system.*


### Ingest (class, L33-L34)

> *Summary: Defines a data structure requiring either a file path or a URL string as input for document ingestion. This model serves as the standardized input container for processing external documents.*


### Query (class, L37-L39)

> *Summary: Defines a data structure holding the parameters for document agent operations. It accepts a `QueryType` enum and a string representing the actual search or retrieval query.*


### is_url (function, L42-L54)

> *Summary: Determines if a given string is a valid URL by parsing it to ensure both a scheme (like http or https) and a network location are present. It returns `True` only if these components exist after stripping whitespace, otherwise returning `False`.*


### _download_rendered_html (function, L58-L96)

> *Summary: Fetches the fully rendered HTML content from a specified URL by launching a headless Chrome instance managed via ChromeDriver. It first validates the input URL against security restrictions before returning the page's source code upon successful execution.*


### _download_binary_file (function, L100-L216)

> *Summary: Downloads a file from a given URL to a specified directory, intelligently determining if the download should be treated as binary or text based on content analysis and file extension. It performs security checks against unsafe URLs before saving the content to the resulting `Path`.*


### _get_extension_from_file_type (function, L219-L246)

> *Summary: Determines a file extension by mapping an `InputFormat` to a default extension, with special logic to derive the exact image format from a provided content type string. It returns the appropriate file extension (e.g., `.png`, `.jpeg`) or defaults to `.bin` if no match is found.*


### _is_valid_extension_for_file_type (function, L249-L257)

> *Summary: Determines if a provided file extension corresponds to a specific input format by checking its mapping within a predefined dictionary. It strips any leading dot from the extension before performing the validation against the `InputFormat`.*


### download_url (function, L261-L310)

> *Summary: Downloads content from a given URL, either by fetching the raw file or rendering web pages using Selenium. It accepts a URL and an optional output directory, returning the `Path` to the saved file.*


### list_files (function, L313-L323)

> *Summary: Recursively scans a given directory path to return a list of all file `Path` objects found within it. It raises an error if the provided input is not an existing directory.*


### handle_input (function, L327-L348)

> *Summary: This utility function processes an input, which can be a local file path, a directory path, or a URL string. It either downloads the content from a URL into a specified output directory, lists all files within a given directory, or returns the path of a single existing file.*


### preprocess_path (function, L352-L390)

> *Summary: Takes a string or `Path` object along with flags indicating if it should be treated as a file or directory, and whether to create missing paths. It resolves the input path to an absolute form, creating necessary parent directories if requested, and validates that the resulting path matches the specified type (file or directory).*

