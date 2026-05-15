# autogen/beta/files/types.py

2 function(s): _datetime_to_timestamp, _created_at_to_float. 3 class(es): FileContent, FileProvider, UploadedFile. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FileContent | class |  |
| FileProvider | class |  |
| UploadedFile | class |  |
| _datetime_to_timestamp | function |  |
| _created_at_to_float | function |  |

## Chunks

### FileContent (class, L18-L21)

> *Summary: Represents the content of a file, holding its name (optional), raw binary data, and an optional MIME type. This structure is used to encapsulate file information for processing or transfer.*


### FileProvider (class, L24-L27)

> *Summary: Defines an enumeration of supported file providers for AI models. It allows specifying which provider—OpenAI, Anthropic, or Gemini—should be used when handling files.*


### UploadedFile (class, L30-L37)

> *Summary: Represents a file uploaded to the system, holding metadata like provider and size. It provides an asynchronous `read` method that uses a provided API client to download and return the actual file content.*


### read (method, L35-L37, parent: UploadedFile)

> *Summary: Retrieves the full content of a file by calling the `read` method on an injected `FilesAPI` client, returning the content as a `FileContent` object.*


### _datetime_to_timestamp (function, L40-L43)

> *Summary: Converts a timezone-naive `datetime` object into a Unix timestamp (float), defaulting to UTC if no timezone information is present. It ensures the input datetime has timezone awareness before calculating the timestamp.*


### _created_at_to_float (function, L46-L70)

> *Summary: Converts various input types (like `None`, numbers, `datetime` objects, or strings) into a Unix timestamp as a `float`. It handles string parsing by attempting direct conversion or ISO format interpretation, defaulting to the current time if no valid value is provided.*

