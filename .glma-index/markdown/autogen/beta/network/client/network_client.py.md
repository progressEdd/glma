# autogen/beta/network/client/network_client.py

1 class(es): NetworkClient. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| NetworkClient | class |  |

## Chunks

### NetworkClient (class, L21-L51)

> *Summary: Defines the interface for a network participant, requiring methods to expose an agent ID and passport, handle incoming messages via `receive`, and gracefully shut down using `disconnect`. Implementations must translate received envelopes into their specific local execution context.*


### agent_id (method, L32-L32, parent: NetworkClient)

> *Summary: Retrieves the unique identifier string associated with the current agent instance. This method takes no input and returns a `str`.*


### passport (method, L35-L35, parent: NetworkClient)

> *Summary: Retrieves a `Passport` object from the client instance. This method is responsible for fetching and returning the necessary credential information.*


### resume (method, L38-L38, parent: NetworkClient)

> *Summary: This method initiates a resumption process, likely using the client's internal state to continue an interrupted operation and returning a `Resume` object detailing the status.*


### receive (method, L40-L47, parent: NetworkClient)

> *Summary: This asynchronous method processes an incoming `Envelope` delivered by a hub. It translates the received envelope into actions appropriate for the specific client implementation, such as invoking `Agent.ask` or pushing to a queue.*


### disconnect (method, L49-L51, parent: NetworkClient)

> *Summary: This asynchronous method cleanly shuts down the client's resources, ensuring that calling it multiple times has no adverse effect. It performs resource teardown without requiring specific inputs.*

