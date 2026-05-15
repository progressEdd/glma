# autogen/beta/knowledge/disk.py

3 class(es): _DiskChangeHandler, _DiskChangeSubscription, DiskKnowledgeStore. 21 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _DiskChangeHandler | class |  |
| _DiskChangeSubscription | class |  |
| DiskKnowledgeStore | class |  |

## Chunks

### _DiskChangeHandler (class, L18-L98)

> *Summary: This class acts as a bridge, translating synchronous file system events from `watchdog` into asynchronous callbacks for the main event loop. It accepts a root path, virtual prefix, an asyncio loop, and a change callback; it filters out directory changes and maps physical paths to store-relative virtual paths before scheduling the provided coroutine.*


### __init__ (method, L32-L43, parent: _DiskChangeHandler)

> *Summary: Initializes a disk-backed knowledge store by setting the base directory, a virtual namespace prefix, an asyncio event loop, and a change notification callback. These parameters define where data is stored and how updates are reported.*


### _virtual_path_for (method, L45-L55, parent: _DiskChangeHandler)

> *Summary: Calculates a normalized, virtual path string from an absolute source path relative to the object's root directory. It returns `None` if the source path is outside the designated root or fails resolution checks based on configured prefixes.*


### _dispatch (method, L57-L65, parent: _DiskChangeHandler)

> *Summary: This method translates a source path to a virtual path and then schedules an asynchronous callback execution on the internal event loop if a valid virtual path is found. It handles potential `RuntimeError` exceptions during scheduling by closing the coroutine instead.*


### on_modified (method, L67-L70, parent: _DiskChangeHandler)

> *Summary: When a file system change event occurs, this method checks if the event pertains to a directory; if not, it dispatches the source path of the modification.*


### on_created (method, L72-L75, parent: _DiskChangeHandler)

> *Summary: When a file is created, this method checks if the event pertains to a directory; if not, it dispatches an event using the source path of the creation event.*


### on_deleted (method, L77-L80, parent: _DiskChangeHandler)

> *Summary: If the incoming event is not a directory, this method dispatches an event using the source path provided in the input event object. This handles notifications when files are removed from the monitored system.*


### on_moved (method, L82-L86, parent: _DiskChangeHandler)

> *Summary: When a file is moved, this method checks if the event involves a directory; if not, it dispatches an update using the destination path of the move event.*


### dispatch (method, L88-L98, parent: _DiskChangeHandler)

> *Summary: This method acts as the central entry point for filesystem events, inspecting an incoming `event` object to determine its type. It then delegates the handling of the event—such as 'modified', 'created', 'deleted', or 'moved'—to the corresponding internal handler method.*


### _DiskChangeSubscription (class, L101-L126)

> *Summary: This class wraps a watchdog observer returned by a knowledge store to manage its lifecycle. It provides an asynchronous `close` method that safely stops and joins the background thread of the underlying observer, preventing resource leaks.*


### __init__ (method, L109-L111, parent: _DiskChangeSubscription)

> *Summary: Initializes the disk handler by storing a provided observer object and setting an internal closed state to false. This sets up the necessary dependencies for managing file system interactions.*


### close (method, L113-L118, parent: _DiskChangeSubscription)

> *Summary: This method safely shuts down the disk resource by setting an internal closed flag and asynchronously executing a dedicated shutdown routine in the event loop's executor. It prevents redundant closing operations if the resource is already marked as closed.*


### _shutdown (method, L120-L126, parent: _DiskChangeSubscription)

> *Summary: This method safely terminates the background file system observer by unscheduling, stopping, and joining it, suppressing any exceptions that occur during these cleanup operations. It ensures a graceful shutdown of the monitoring process regardless of internal errors.*


### DiskKnowledgeStore (class, L129-L246)

> *Summary: This class provides persistent storage by mapping virtual paths to actual files within a specified root directory on the local filesystem. It supports asynchronous operations like reading, writing, listing contents, and deleting files/directories, while also offering event subscription for real-time file system change notifications using `watchdog`.*


### __init__ (method, L144-L145, parent: DiskKnowledgeStore)

> *Summary: Initializes the disk handler by storing a provided path as its internal root directory. This sets up the base location for all subsequent file system operations.*


### _resolve (method, L147-L153, parent: DiskKnowledgeStore)

> *Summary: This method translates a virtual path string into an absolute filesystem `Path` object. It resolves the path relative to a configured root, ensuring that the resulting path remains within the designated root directory to prevent traversal attacks.*


### read (method, L155-L159, parent: DiskKnowledgeStore)

> *Summary: Retrieves the content of a file given its path string after resolving it against the current knowledge base context. It returns the file's text content as a string if it exists, or `None` otherwise.*


### write (method, L161-L164, parent: DiskKnowledgeStore)

> *Summary: This method asynchronously saves string content to a specified file path after ensuring the necessary parent directories exist. It takes a `path` string and `content` string as input and performs no return value upon successful writing.*


### list (method, L166-L176, parent: DiskKnowledgeStore)

> *Summary: Retrieves a list of names for the contents within a specified directory path. It resolves the input path, checks if it's a directory, and returns sorted strings representing the names of its subdirectories (with a trailing slash) or files.*


### delete (method, L178-L183, parent: DiskKnowledgeStore)

> *Summary: Removes a file or directory at the specified path by first resolving it against the current knowledge base context. It uses `unlink()` for files and `shutil.rmtree()` for directories to ensure complete deletion.*


### exists (method, L185-L186, parent: DiskKnowledgeStore)

> *Summary: Checks if a given file path exists by first resolving the path internally and then querying its existence. Returns a boolean indicating presence or absence.*


### append (method, L188-L195, parent: DiskKnowledgeStore)

> *Summary: This method asynchronously appends string content to a specified file path after ensuring the necessary directory structure exists. It returns the byte offset where the appended data began.*


### read_range (method, L197-L208, parent: DiskKnowledgeStore)

> *Summary: Retrieves a specified byte range from a file located at the given path. It reads from the `start` offset up to either the end of the file or the calculated length defined by `end`, returning the content as a UTF-8 decoded string.*


### on_change (method, L210-L246, parent: DiskKnowledgeStore)

> *Summary: Registers a subscription to monitor filesystem changes within a specified path using the `watchdog` library for native event dispatching. It attempts platform-native watching, falling back to polling if necessary, and returns a subscription object that manages these notifications.*

