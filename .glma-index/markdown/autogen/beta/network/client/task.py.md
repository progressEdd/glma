# autogen/beta/network/client/task.py

1 class(es): ClientTask. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ClientTask | class |  |

## Chunks

### ClientTask (class, L26-L59)

> *Summary: Represents a tracked remote task for an observer, holding references to its metadata and the client agent. It allows accessing key properties like ID and state, and provides an asynchronous method to refresh the task's metadata from the hub.*


### __init__ (method, L29-L37, parent: ClientTask)

> *Summary: Initializes a task object by storing provided `TaskMetadata` and an `AgentClient` instance as internal attributes. This constructor performs no operations other than parameter assignment.*


### task_id (method, L40-L41, parent: ClientTask)

> *Summary: Retrieves the unique identifier for the current task from the object's metadata. This method returns a string representing the task ID.*


### metadata (method, L44-L45, parent: ClientTask)

> *Summary: Returns the stored `TaskMetadata` object associated with the task instance. This method provides read access to the task's descriptive information.*


### state (method, L48-L49, parent: ClientTask)

> *Summary: Retrieves the current operational status of the task by accessing and returning the `state` attribute from the internal metadata object. This method provides a direct read of the task's lifecycle stage.*


### owner_id (method, L52-L53, parent: ClientTask)

> *Summary: Retrieves the unique identifier of the task's owner from the internal metadata structure. This method returns a string representing the owner ID.*


### info (method, L55-L59, parent: ClientTask)

> *Summary: Retrieves and updates the task's metadata by calling the remote hub client with the stored task ID, returning the newly fetched `TaskMetadata`.*

