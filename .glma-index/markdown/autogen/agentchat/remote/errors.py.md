# autogen/agentchat/remote/errors.py

2 class(es): RemoteAgentError, RemoteAgentNotFoundError. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RemoteAgentError | class |  |
| RemoteAgentNotFoundError | class |  |

## Chunks

### RemoteAgentError (class, L6-L9)

> *Summary: Serves as the base exception for any errors encountered when interacting with a remote agent. It inherits from `Exception` to allow specific error handling in calling code.*


### RemoteAgentNotFoundError (class, L12-L17)

> *Summary: This exception signals that a requested remote agent could not be located. It accepts an `agent_name` string and raises an error indicating the specific missing agent.*


### __init__ (method, L15-L17, parent: RemoteAgentNotFoundError)

> *Summary: Initializes an error object by storing the provided `agent_name` and setting a descriptive message indicating that the remote agent was not found. This constructor is used to create specific exceptions related to missing agents in a remote context.*

