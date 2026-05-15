# autogen/beta/knowledge/base.py

1 function(s): _normalize. 3 class(es): ChangeSubscription, NoopChangeSubscription, KnowledgeStore. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ChangeSubscription | class |  |
| NoopChangeSubscription | class |  |
| KnowledgeStore | class |  |
| _normalize | function |  |

## Chunks

### ChangeSubscription (class, L11-L22)

> *Summary: Defines a protocol for objects returned by `KnowledgeStore.on_change` to manage filesystem-level reactivity. It requires an asynchronous `close()` method to stop receiving change notifications from the backing store.*


### close (method, L20-L22, parent: ChangeSubscription)

> *Summary: This asynchronous method stops the object from receiving further change notifications. It is called on an instance of the class to terminate its listening state.*


### NoopChangeSubscription (class, L25-L33)

> *Summary: This class acts as a placeholder sentinel indicating that the underlying backend cannot efficiently observe changes. When encountered, the system defaults to a polling mechanism for change detection.*


### close (method, L32-L33, parent: NoopChangeSubscription)

> *Summary: This asynchronous method provides a placeholder for cleanup operations, returning nothing upon execution. It is intended to be called when the object's resources need to be released.*


### KnowledgeStore (class, L37-L103)

> *Summary: Defines an abstract interface for storing agent knowledge using Unix-like filesystem semantics over any backend. It requires methods for basic CRUD operations, plus `append` and `read_range` for WAL sessions, and optionally supports change notifications via `on_change`.*


### read (method, L52-L54, parent: KnowledgeStore)

> *Summary: Asynchronously reads the string content from a specified file path; returns `None` if the file does not exist.*


### write (method, L56-L58, parent: KnowledgeStore)

> *Summary: Asynchronously saves the provided string content to a specified file path, automatically creating any necessary parent directories along the way.*


### list (method, L60-L66, parent: KnowledgeStore)

> *Summary: Retrieves the names of all immediate subdirectories and files within a specified directory path. It returns these names as a list of strings, ensuring directories are marked with a trailing slash.*


### delete (method, L68-L70, parent: KnowledgeStore)

> *Summary: Removes a specific entry identified by the provided `path` string; it silently succeeds if the target does not exist.*


### exists (method, L72-L74, parent: KnowledgeStore)

> *Summary: Asynchronously checks for the existence of a given file or directory path. It accepts a string representing the path and returns a boolean indicating its presence.*


### append (method, L76-L83, parent: KnowledgeStore)

> *Summary: Atomically adds specified content to a file located at a given path, creating necessary parent directories if absent. It returns the byte offset where the appended content began, enabling subsequent range reads.*


### read_range (method, L85-L93, parent: KnowledgeStore)

> *Summary: Retrieves a specific byte slice from a file given its path and start/end indices. If the end index is omitted, it reads until the end of the file, returning the content as UTF-8 text or an empty string if the file is missing.*


### on_change (method, L95-L103, parent: KnowledgeStore)

> *Summary: Registers a listener to receive notifications when files within a specified path are modified. It accepts a file path and a callback function, returning a subscription object that manages the ongoing change monitoring.*


### _normalize (function, L106-L114)

> *Summary: This utility function standardizes a given file path string by ensuring it starts with a forward slash, collapsing any double slashes into single ones, and removing any trailing slash unless the path is just "/". It takes a raw path string as input and returns a consistently formatted absolute path string.*

