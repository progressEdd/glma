# autogen/agentchat/realtime/experimental/clients/oai/base_client.py

1 class(es): OpenAIRealtimeClient. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OpenAIRealtimeClient | class |  |

## Chunks

### OpenAIRealtimeClient (class, L33-L215)

> *Summary: This class implements a client for interacting with the OpenAI Realtime API, configured via an `LLMConfig`. It manages connections and provides asynchronous methods to send text, function results, or audio data to the service, while also offering a generator to read incoming real-time events.*


### __init__ (method, L36-L60, parent: OpenAIRealtimeClient)

> *Summary: Initializes an experimental client for the OpenAI Realtime API, storing configuration details like model name, voice selection, and temperature from the provided `llm_config`. It sets up internal state variables to manage the connection and core client instance.*


### logger (method, L63-L65, parent: OpenAIRealtimeClient)

> *Summary: Retrieves a configured logging instance, defaulting to a globally available logger if no specific one has been set on the client object. This ensures consistent logging across the OpenAI Realtime API interactions.*


### connection (method, L68-L72, parent: OpenAIRealtimeClient)

> *Summary: Retrieves the established asynchronous WebSocket connection object if it has been previously initialized. It raises a `RuntimeError` if the underlying connection hasn't been set up.*


### send_function_result (method, L74-L89, parent: OpenAIRealtimeClient)

> *Summary: This method transmits the outcome of a function execution back to the OpenAI Realtime API. It takes a `call_id` and the resulting `result` string as input, creating a "function\_call\_output" item in the conversation and then triggering a response update.*


### send_text (method, L91-L102, parent: OpenAIRealtimeClient)

> *Summary: This method sends a text message to the OpenAI Realtime API by first canceling any existing response and then creating a new conversation item with the specified role and content. It concludes by initiating a new response stream for the incoming message.*


### send_audio (method, L104-L111, parent: OpenAIRealtimeClient)

> *Summary: This method queues and sends an audio string to the OpenAI Realtime API. It first buffers the incoming audio delta internally before appending it to the connection's input audio buffer.*


### truncate_audio (method, L113-L123, parent: OpenAIRealtimeClient)

> *Summary: This method sends a request via the underlying connection to truncate an audio segment within the OpenAI Realtime API. It takes the desired end time in milliseconds, the content index, and a unique item ID as input.*


### _initialize_session (method, L125-L133, parent: OpenAIRealtimeClient)

> *Summary: Sets up the initial communication session with OpenAI by configuring parameters like voice settings, audio/text modalities, and temperature. This method uses stored instance attributes to define the session's operational characteristics before interaction begins.*


### session_update (method, L135-L144, parent: OpenAIRealtimeClient)

> *Summary: This method transmits configuration changes to the OpenAI Realtime API using an existing connection object. It accepts a dictionary of session options and asynchronously updates the active session state.*


### connect (method, L147-L168, parent: OpenAIRealtimeClient)

> *Summary: Establishes a connection to the OpenAI Realtime API using configuration parameters like API keys and base URLs. It yields control while maintaining an active WebSocket connection, ensuring cleanup upon exiting the context manager.*


### read_events (method, L170-L180, parent: OpenAIRealtimeClient)

> *Summary: This asynchronous method streams events from the OpenAI Realtime API, yielding each `RealtimeEvent` as it arrives. It ensures the underlying connection is closed upon completion or error.*


### _read_from_connection (method, L182-L186, parent: OpenAIRealtimeClient)

> *Summary: This asynchronous method streams events by iterating over an underlying connection object and yielding parsed `RealtimeEvent` objects from each received message. It acts as a generator to expose real-time data from the OpenAI Realtime API.*


### _parse_message (method, L188-L197, parent: OpenAIRealtimeClient)

> *Summary: Converts a raw dictionary received from the OpenAI Realtime API into a list containing one or more `RealtimeEvent` objects by calling an internal parsing helper. It takes a single message dictionary as input and returns a list of parsed events.*


### get_factory (method, L200-L215, parent: OpenAIRealtimeClient)

> *Summary: This method conditionally returns a factory function that instantiates an `OpenAIRealtimeClient` if the provided LLM configuration specifies "openai" as the API type and no extra keyword arguments are present. Otherwise, it returns `None`.*

