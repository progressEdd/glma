# autogen/beta/config/anthropic/files.py

1 class(es): AnthropicFilesClient. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AnthropicFilesClient | class |  |

## Chunks

### AnthropicFilesClient (class, L17-L70)

> *Summary: This class provides an interface to manage files with the Anthropic API by wrapping an asynchronous client. It supports uploading data (bytes), reading content by ID, listing existing files, and deleting files via methods that take configuration objects as input and return file metadata or status updates.*


### __init__ (method, L22-L30, parent: AnthropicFilesClient)

> *Summary: Initializes an asynchronous Anthropic client using configuration details like API key, base URL, and timeouts provided in the input config object. It sets up the necessary HTTP client instance for making API calls to Anthropic services.*


### upload (method, L32-L44, parent: AnthropicFilesClient)

> *Summary: This method uploads raw byte data to the Anthropic API using a specified filename and optional purpose. It returns an `UploadedFile` object containing metadata like the file ID, name, and creation timestamp from the successful upload response.*


### read (method, L46-L53, parent: AnthropicFilesClient)

> *Summary: Retrieves the content and metadata for a specified file ID from the Anthropic API. It downloads the file content and separately fetches its associated metadata to construct and return a `FileContent` object.*


### list (method, L55-L67, parent: AnthropicFilesClient)

> *Summary: Retrieves a list of files from the Anthropic API client and transforms each response object into an `UploadedFile` instance. It maps essential file attributes like ID, filename, size, and creation time to the standardized output structure.*


### delete (method, L69-L70, parent: AnthropicFilesClient)

> *Summary: Removes a specified file from the service using its unique ID by calling the underlying client's deletion endpoint. It takes a `file_id` string as input and returns nothing upon successful execution.*

