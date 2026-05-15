# autogen/beta/config/gemini/files.py

1 class(es): GeminiFilesClient. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GeminiFilesClient | class |  |

## Chunks

### GeminiFilesClient (class, L17-L68)

> *Summary: This class provides an asynchronous interface for interacting with the Google Gemini Files API using a provided configuration. It supports uploading binary data to create files, retrieving content from existing file IDs, listing all managed files, and deleting specified files.*


### __init__ (method, L22-L23, parent: GeminiFilesClient)

> *Summary: Initializes the object by creating a Gemini client instance using an API key provided in the configuration object. This sets up the necessary connection to interact with the Gemini service.*


### upload (method, L25-L37, parent: GeminiFilesClient)

> *Summary: This method uploads raw byte data to the Gemini service, determining the MIME type from the provided filename. It returns an `UploadedFile` object containing metadata like the file ID and creation time after a successful upload via the underlying client.*


### read (method, L39-L51, parent: GeminiFilesClient)

> *Summary: Retrieves the content of a specified file ID by first fetching its metadata and then downloading the binary data via an asynchronous client call. It returns a `FileContent` object containing the file's name, raw data, and MIME type, raising an error if no download URI is available.*


### list (method, L53-L65, parent: GeminiFilesClient)

> *Summary: Retrieves a list of uploaded files from the Gemini API client's file service. It transforms the raw paginated response into a list of `UploadedFile` objects containing metadata like ID, name, and size.*


### delete (method, L67-L68, parent: GeminiFilesClient)

> *Summary: Removes a specified file from the service using its unique ID as input and returns nothing upon successful deletion. This asynchronous method delegates the actual deletion call to an underlying client object.*

