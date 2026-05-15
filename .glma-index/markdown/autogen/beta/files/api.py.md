# autogen/beta/files/api.py

1 class(es): FilesAPI. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FilesAPI | class |  |

## Chunks

### FilesAPI (class, L14-L49)

> *Summary: Provides an interface for managing files with an external provider, allowing developers to upload content from local paths or raw bytes, read specific files by ID, list all stored files, and delete files. It wraps the underlying client's operations to handle path resolution and input validation.*


### __init__ (method, L17-L18, parent: FilesAPI)

> *Summary: Initializes the object by creating and storing a file client instance based on the provided `ModelConfig`. This sets up the necessary interface for interacting with files.*


### upload (method, L20-L37, parent: FilesAPI)

> *Summary: This method uploads a file to the provider, accepting either a local file path (which it reads into bytes) or raw byte data as input. It validates that at least one source is provided and returns an `UploadedFile` object upon successful upload via the underlying client.*


### read (method, L39-L41, parent: FilesAPI)

> *Summary: Retrieves the full content of a specified file using its unique identifier. It asynchronously calls an underlying client method to fetch and return the `FileContent` object.*


### list (method, L43-L45, parent: FilesAPI)

> *Summary: Retrieves a list of all uploaded files from the configured provider by calling an underlying client method asynchronously. It returns a list containing `UploadedFile` objects representing the available files.*


### delete (method, L47-L49, parent: FilesAPI)

> *Summary: Removes a specified file using its unique identifier by calling the underlying client's deletion method asynchronously. It takes one string argument, `file_id`, and returns nothing upon successful execution.*

