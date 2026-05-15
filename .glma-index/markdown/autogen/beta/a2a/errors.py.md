# autogen/beta/a2a/errors.py

9 class(es): A2AError, A2AClientToolsNotSupportedError, A2AInvalidCardError, A2AReconnectError, A2ATaskTerminalError, A2ATaskFailedError, A2ATaskRejectedError, A2ATaskAuthRequiredError, RehydratedToolError. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2AError | class |  |
| A2AClientToolsNotSupportedError | class |  |
| A2AInvalidCardError | class |  |
| A2AReconnectError | class |  |
| A2ATaskTerminalError | class |  |
| A2ATaskFailedError | class |  |
| A2ATaskRejectedError | class |  |
| A2ATaskAuthRequiredError | class |  |
| RehydratedToolError | class |  |

## Chunks

### A2AError (class, L8-L9)

> *Summary: Serves as the base exception class for all errors encountered during A2A integrations. It inherits from Python's standard `Exception` to allow custom error handling within the system.*


### A2AClientToolsNotSupportedError (class, L12-L16)

> *Summary: This exception signals that an agent, connected via an A2A server, lacks advertised support for the `urn:ag2:client-tools:v1` extension when tools are provided as input. It inherits from a base `A2AError`.*


### A2AInvalidCardError (class, L19-L20)

> *Summary: This exception signals that the provided `AgentCard` lacks necessary information for establishing a connection. It inherits from a base `A2AError`.*


### A2AReconnectError (class, L23-L28)

> *Summary: Signals that all configured reconnection attempts for a streaming task have failed. It stores the total number of attempts made in an instance attribute.*


### __init__ (method, L26-L28, parent: A2AReconnectError)

> *Summary: Initializes an error object indicating that a streaming task failed after exhausting a specified number of reconnection attempts. It stores the count of those attempts as an instance attribute for later inspection.*


### A2ATaskTerminalError (class, L31-L37)

> *Summary: Represents a base error for when an automated agent-to-agent task reaches a terminal failure or rejection state. It initializes with the failing `Task` object and constructs an error message detailing the task ID and its final status.*


### __init__ (method, L34-L37, parent: A2ATaskTerminalError)

> *Summary: Initializes an error object by storing a reference to the associated `Task`. It constructs a descriptive message indicating the task ID and its final state, which is then passed to the parent constructor.*


### A2ATaskFailedError (class, L40-L41)

> *Summary: Represents a specific error indicating that an automated agent-to-agent task terminated with a failure state. It inherits from `A2ATaskTerminalError` to signal the completion of a failed process.*


### A2ATaskRejectedError (class, L44-L45)

> *Summary: Represents a terminal error indicating that an autonomous agent task was explicitly rejected. It inherits from `A2ATaskTerminalError` to signify the final state of the task.*


### A2ATaskAuthRequiredError (class, L48-L56)

> *Summary: Indicates that a task terminated because authentication credentials are missing, as per the A2A specification. This error signals the client application must obtain and apply necessary credentials before retrying the operation.*


### RehydratedToolError (class, L59-L67)

> *Summary: This exception serves as a placeholder for tool errors that are reconstructed from serialized data, as the original exception type is lost during transmission. It inherits from `Exception` to maintain compatibility with how error strings are processed in JSON decoding contexts.*

