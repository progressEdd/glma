# autogen/a2a/client.py

2 function(s): _is_event_completed, _is_task_completed. 1 class(es): A2aRemoteAgent. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2aRemoteAgent | class |  |
| _is_event_completed | function |  |
| _is_task_completed | function |  |

## Chunks

### A2aRemoteAgent (class, L54-L405)

> *Summary: This class acts as an SDK client for interacting with a remote A2A server, inheriting compatibility from `ConversableAgent`. It manages connections by fetching agent metadata via its URL and handles asynchronous communication through streaming or polling mechanisms. The primary async method initiates conversations, processes incoming messages/tasks, and manages user input requests if the remote agent requires them.*


### __init__ (method, L71-L109, parent: A2aRemoteAgent)

> *Summary: Initializes an agent client by setting up HTTP communication via a provided or default factory and resolving card information based on the configured URL. It configures retry logic, sets up interceptors, and overrides reply generation methods to handle remote interactions.*


### from_card (method, L112-L154, parent: A2aRemoteAgent)

> *Summary: Constructs an `A2aRemoteAgent` instance using pre-existing agent metadata provided in an `AgentCard`. It initializes the agent with configuration details from the card while setting its registry URL to "UNKNOWN" and returns a configured instance of itself.*


### generate_remote_reply (method, L156-L162, parent: A2aRemoteAgent)

> *Summary: This method is intended to generate a response from a remote agent based on provided messages, sender context, and configuration. Currently, it explicitly raises an error because the implementing class does not support synchronous reply generation.*


### a_generate_remote_reply (method, L164-L245, parent: A2aRemoteAgent)

> *Summary: This method initiates and manages a remote conversation by sending an initial message to another agent via an A2A client. It handles streaming responses, processes incoming messages or task updates, prompts the user for required input if necessary, and returns success along with the final response content.*


### _get_requested_extensions (method, L247-L251, parent: A2aRemoteAgent)

> *Summary: Retrieves a list of extension URIs from the agent card's capabilities if they exist; otherwise, it returns `None`. This method inspects the internal state to determine which extensions need to be requested.*


### _ask_streaming (method, L253-L293, parent: A2aRemoteAgent)

> *Summary: This asynchronous method streams events by first sending a message and yielding all received events, including any initial task start event. If the stream doesn't complete, it attempts to reconnect and yield subsequent events for the started task up to a maximum number of retries upon connection failure.*


### _ask_polling (method, L295-L339, parent: A2aRemoteAgent)

> *Summary: This asynchronous generator streams events from a message exchange with an agent client, yielding initial events as they arrive. If the stream completes without confirmation, it enters a polling loop to check for task completion against a specified maximum number of retries before raising a connection error.*


### update_tool_signature (method, L341-L352, parent: A2aRemoteAgent)

> *Summary: Modifies the internal LLM configuration by updating or removing a specified tool signature. It accepts the signature (as a string or dictionary), a boolean indicating removal, and an optional flag to suppress overrides.*


### _get_agent_card (method, L354-L405, parent: A2aRemoteAgent)

> *Summary: Retrieves an agent's configuration card by first attempting a modern well-known path and falling back to a legacy path if the initial request returns a 404. It then optionally fetches and uses an authenticated extended card if the public card indicates support, returning a standardized `AgentCard` object.*


### _is_event_completed (function, L408-L411)

> *Summary: Determines if a stream event signifies completion by checking if it's a `Message` type or recursively calling another function on the first element of non-message events. It returns `True` upon successful identification of a completed state.*


### _is_task_completed (function, L414-L425)

> *Summary: Checks the state of a given `Task` object to determine if it's finished or requires further action. It raises an error if the task is in a failed or rejected state, otherwise returns `True` if the state is completed, canceled, or input required.*

