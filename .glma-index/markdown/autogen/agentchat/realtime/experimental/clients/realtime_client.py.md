# autogen/agentchat/realtime/experimental/clients/realtime_client.py

2 function(s): register_realtime_client, get_client. 2 class(es): RealtimeClientProtocol, RealtimeClientBase. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RealtimeClientProtocol | class |  |
| RealtimeClientBase | class |  |
| register_realtime_client | function |  |
| get_client | function |  |

## Chunks

### RealtimeClientProtocol (class, L25-L105)

> *Summary: Defines a protocol specifying methods for interacting with a Realtime API, allowing clients to send function results, text, audio, and session updates. It also mandates methods for establishing connections, reading incoming events, and parsing received messages from the API.*


### send_function_result (method, L26-L33, parent: RealtimeClientProtocol)

> *Summary: This method transmits the outcome of an executed function back to a Realtime API endpoint. It accepts a unique call identifier and the corresponding string result as input.*


### send_text (method, L35-L42, parent: RealtimeClientProtocol)

> *Summary: Sends a specified text message, along with its designated role, to a Realtime API endpoint asynchronously. It takes a `Role` and a string for the message content as input and returns nothing upon successful transmission.*


### send_audio (method, L44-L50, parent: RealtimeClientProtocol)

> *Summary: This asynchronous method transmits an audio string to a Realtime API endpoint. It accepts one string argument representing the audio data and returns nothing upon successful transmission.*


### truncate_audio (method, L52-L60, parent: RealtimeClientProtocol)

> *Summary: This method modifies an existing audio segment within a Realtime API by cutting it off at a specified millisecond point. It requires the desired end time, the content's index, and a unique item identifier as input.*


### session_update (method, L62-L68, parent: RealtimeClientProtocol)

> *Summary: Sends specified session configuration changes to the Realtime API asynchronously. It accepts a dictionary containing the desired session options as input and performs no direct return value.*


### connect (method, L70-L70, parent: RealtimeClientProtocol)

> *Summary: Establishes a connection to the real-time service, returning an asynchronous context manager that handles setup and teardown. This method initiates the necessary communication link for subsequent interactions.*


### read_events (method, L72-L74, parent: RealtimeClientProtocol)

> *Summary: This method yields asynchronous `RealtimeEvent` objects by reading incoming data from the client connection. It acts as an event stream producer for consuming real-time updates.*


### _read_from_connection (method, L76-L78, parent: RealtimeClientProtocol)

> *Summary: This asynchronous method yields `RealtimeEvent` objects by continuously reading data from the established realtime connection. It acts as an event stream reader for incoming messages.*


### _parse_message (method, L80-L89, parent: RealtimeClientProtocol)

> *Summary: This method takes a dictionary representing an incoming Realtime API message and transforms it into a list of structured `RealtimeEvent` objects. It is responsible for interpreting the raw message format to extract meaningful event data.*


### get_factory (method, L92-L105, parent: RealtimeClientProtocol)

> *Summary: This method constructs and returns a factory function capable of producing a `RealtimeClientProtocol` instance. It takes an LLM configuration, a logger, and optional keyword arguments to initialize the client based on provided parameters.*


### RealtimeClientBase (class, L108-L143)

> *Summary: This base client manages asynchronous event flow by queuing incoming events from a connection and yielding them to consumers. It provides methods to enqueue audio data as specific delta events into the internal queue.*


### __init__ (method, L109-L110, parent: RealtimeClientBase)

> *Summary: Initializes the client by creating an asynchronous queue to manage incoming events. This queue will be used internally for real-time communication handling.*


### add_event (method, L112-L113, parent: RealtimeClientBase)

> *Summary: This method asynchronously queues a `RealtimeEvent` object into an internal event queue. It accepts either a valid event or `None` as input and places it onto the queue for later processing.*


### get_event (method, L115-L116, parent: RealtimeClientBase)

> *Summary: Retrieves the next available event from an internal queue asynchronously. It returns a `RealtimeEvent` object if one is present, or `None` otherwise.*


### _read_from_connection_task (method, L118-L121, parent: RealtimeClientBase)

> *Summary: This asynchronous method continuously consumes events from the underlying connection stream and forwards each received event to the client's event handler. Upon the stream closing, it sends a final `None` event to signal completion.*


### _read_events (method, L123-L135, parent: RealtimeClientBase)

> *Summary: This asynchronous method continuously yields `RealtimeEvent` objects by consuming items from an internal event queue, while concurrently running a background task to populate that queue from the underlying connection. It terminates when it receives a `None` event or encounters any exception during reading.*


### queue_input_audio_buffer_delta (method, L137-L143, parent: RealtimeClientBase)

> *Summary: Adds a delta update to the input audio buffer by queuing an `InputAudioBufferDelta` event containing the provided audio string. This method asynchronously notifies the system of incremental changes to the audio stream.*


### register_realtime_client (function, L151-L170)

> *Summary: This function returns a decorator that registers a provided client class into a global registry using its fully qualified name as the key. It allows developers to easily register custom Realtime API clients for later retrieval by the system.*


### get_client (function, L174-L191)

> *Summary: Retrieves an initialized `RealtimeClientProtocol` instance by iterating through registered client classes and attempting to create a factory using the provided LLM configuration and logger. If no suitable client can be instantiated, it raises a `ValueError`.*

