# autogen/beta/config/openai/files.py

1 class(es): OpenAIFilesClient. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OpenAIFilesClient | class |  |

## Chunks

### OpenAIFilesClient (class, L16-L71)

> *Summary: This class provides an asynchronous interface for interacting with the OpenAI Files API. It accepts configuration to initialize an underlying `AsyncOpenAI` client and offers methods to upload, read content from, list, and delete files using their respective IDs.*


### __init__ (method, L21-L32, parent: OpenAIFilesClient)

> *Summary: Initializes an asynchronous OpenAI client using configuration details provided in either `OpenAIConfig` or `OpenAIResponsesConfig`. It sets up the connection parameters like API key, base URL, and timeouts for subsequent API interactions.*


### upload (method, L34-L46, parent: OpenAIFilesClient)

> *Summary: This method uploads raw byte data to the OpenAI API using a specified filename and optional purpose. It returns an `UploadedFile` object containing metadata like the file ID, name, and size from the successful upload response.*


### read (method, L48-L54, parent: OpenAIFilesClient)

> *Summary: Retrieves the content and metadata for a specified file ID from the OpenAI API client. It returns a `FileContent` object containing the file's name and its binary data.*


### list (method, L56-L68, parent: OpenAIFilesClient)

> *Summary: Retrieves a list of files from the OpenAI API client and transforms each response object into an `UploadedFile` instance. It returns a synchronous list containing metadata for all uploaded files.*


### delete (method, L70-L71, parent: OpenAIFilesClient)

> *Summary: This method asynchronously deletes a specified file using its ID by calling the underlying client's files deletion endpoint. It takes a `file_id` string as input and returns nothing upon successful execution.*

