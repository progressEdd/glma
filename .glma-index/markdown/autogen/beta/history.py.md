# autogen/beta/history.py

3 class(es): Storage, MemoryStorage, History. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Storage | class |  |
| MemoryStorage | class |  |
| History | class |  |

## Chunks

### Storage (class, L14-L21)

> *Summary: Defines a protocol for persistent storage operations related to conversational history. It requires methods to asynchronously save, retrieve, set, and clear event histories associated with a specific stream ID.*


### save_event (method, L15-L15, parent: Storage)

> *Summary: Persists a given `BaseEvent` object into the system's state using an associated `Context`. This asynchronous method handles the recording of events.*


### get_history (method, L17-L17, parent: Storage)

> *Summary: Retrieves a sequence of past events associated with a given `StreamId`. It returns an iterable collection of `BaseEvent` objects.*


### set_history (method, L19-L19, parent: Storage)

> *Summary: Updates the internal event history for a specific stream ID by accepting an iterable of base events. This method asynchronously persists the provided sequence of events to the object's state.*


### drop_history (method, L21-L21, parent: Storage)

> *Summary: Removes the conversation history associated with a specific `StreamId`. It is an asynchronous method that takes one identifier as input and returns nothing.*


### MemoryStorage (class, L24-L38)

> *Summary: This class provides an in-memory implementation of event storage, using a dictionary to map `StreamId`s to lists of `BaseEvent` objects. It supports asynchronous operations to save, retrieve, set, and delete event histories for specific streams.*


### __init__ (method, L25-L26, parent: MemoryStorage)

> *Summary: Initializes an object to store event history using a `defaultdict` mapping stream IDs to lists of base events. This structure allows for the accumulation and retrieval of sequential event data per stream.*


### save_event (method, L28-L29, parent: MemoryStorage)

> *Summary: Appends a given `BaseEvent` to the list of events associated with a specific stream ID within the current context's data structure. This method updates the internal state by recording the event for later retrieval.*


### get_history (method, L31-L32, parent: MemoryStorage)

> *Summary: Retrieves all historical events associated with a given `StreamId` from the internal data store. It returns an iterable sequence of `BaseEvent` objects for that specific stream.*


### set_history (method, L34-L35, parent: MemoryStorage)

> *Summary: This method updates the internal data structure by storing a sequence of `BaseEvent` objects associated with a given `StreamId`. It overwrites any existing history for that stream.*


### drop_history (method, L37-L38, parent: MemoryStorage)

> *Summary: Removes a specific conversation history entry from the internal data store using a provided `StreamId`. This operation modifies the instance's state by deleting the corresponding record.*


### History (class, L41-L50)

> *Summary: Manages the event history for a specific stream by encapsulating storage interactions. It allows retrieving all past events from the configured storage or replacing the entire history with a new iterable of events.*


### __init__ (method, L42-L44, parent: History)

> *Summary: Initializes a history object by storing a unique `stream_id` and a reference to a `Storage` mechanism for data persistence. This sets up the necessary context for tracking historical events within a specific stream.*


### get_events (method, L46-L47, parent: History)

> *Summary: Retrieves a sequence of historical events by querying the underlying storage using the instance's stream ID. It returns an iterable collection of `BaseEvent` objects.*


### replace (method, L49-L50, parent: History)

> *Summary: This method asynchronously updates the stored event history for a stream by persisting a provided iterable of `BaseEvent` objects to storage. It takes an iterable of events as input and performs no return value.*

