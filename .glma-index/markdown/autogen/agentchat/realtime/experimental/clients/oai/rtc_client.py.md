# autogen/agentchat/realtime/experimental/clients/oai/rtc_client.py

1 function(s): _rtc_client. 1 class(es): OpenAIRealtimeWebRTCClient. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OpenAIRealtimeWebRTCClient | class |  |
| _rtc_client | function |  |

## Chunks

### OpenAIRealtimeWebRTCClient (class, L34-L236)

> *Summary: This class implements an experimental client for the OpenAI Realtime API using a WebRTC protocol over a provided WebSocket. It manages sending various inputs like text and function results, while also reading relayed events from the WebSocket connection. Initialization requires LLM configuration and a WebSocket instance to establish communication with the service.*


### __init__ (method, L37-L61, parent: OpenAIRealtimeWebRTCClient)

> *Summary: Initializes an experimental client for the OpenAI Realtime API, accepting LLM configuration, a WebSocket connection, and an optional logger. It extracts necessary parameters like the model name, voice setting, temperature, and base URL from the provided configurations to establish its operational state.*


### logger (method, L64-L66, parent: OpenAIRealtimeWebRTCClient)

> *Summary: Retrieves an instance of a `Logger` object, defaulting to a globally defined logger if no specific logger has been initialized on the client. This provides consistent logging access for the OpenAI Realtime API client.*


### send_function_result (method, L68-L83, parent: OpenAIRealtimeWebRTCClient)

> *Summary: Transmits the outcome of a function execution to the OpenAI Realtime API via a WebSocket connection. It sends two JSON messages: one containing the `call_id` and the `result`, and a subsequent message signaling a general response creation.*


### send_text (method, L85-L101, parent: OpenAIRealtimeWebRTCClient)

> *Summary: This method transmits a user message to the OpenAI Realtime API via a WebSocket connection. It first cancels any existing response, then sends a new conversation item containing the specified role and text content, finally signaling the creation of a new response.*


### send_audio (method, L103-L110, parent: OpenAIRealtimeWebRTCClient)

> *Summary: Queues an incoming audio string for logging purposes when interacting with the OpenAI Realtime API. This method accepts one string argument representing the audio data and returns nothing.*


### truncate_audio (method, L112-L125, parent: OpenAIRealtimeWebRTCClient)

> *Summary: Sends a JSON message over the WebSocket to instruct the OpenAI Realtime API to truncate an audio segment. It uses provided values for the end time in milliseconds, content index, and item identifier.*


### session_update (method, L127-L141, parent: OpenAIRealtimeWebRTCClient)

> *Summary: This method transmits a dictionary of session options to the connected JavaScript client via WebSocket, as direct transmission to the OpenAI Realtime API is not possible in WebRTC contexts. It logs the action before sending the structured update message.*


### session_init_data (method, L143-L151, parent: OpenAIRealtimeWebRTCClient)

> *Summary: Prepares the initial configuration payload for an OpenAI session by bundling settings like voice preference, temperature, and audio/text modalities. This method returns a list containing a single update message to control the start of the interaction.*


### _initialize_session (method, L153-L153, parent: OpenAIRealtimeWebRTCClient)

> *Summary: This asynchronous method sets up the necessary state for a real-time client session. It performs internal initialization tasks required before communication can begin.*


### connect (method, L156-L185, parent: OpenAIRealtimeWebRTCClient)

> *Summary: Establishes a connection to the OpenAI Realtime API by making an HTTP POST request with configuration details like the model and voice. Upon successful response, it sends initialization data over an associated WebSocket before yielding control.*


### read_events (method, L187-L190, parent: OpenAIRealtimeWebRTCClient)

> *Summary: This method asynchronously yields `RealtimeEvent` objects by iterating over an internal stream of events fetched from the OpenAI Realtime API. It acts as a generator to expose incoming real-time data to the caller.*


### _read_from_connection (method, L192-L206, parent: OpenAIRealtimeWebRTCClient)

> *Summary: This asynchronous method continuously reads text messages from an underlying WebSocket connection. It parses these incoming JSON messages and yields individual `RealtimeEvent` objects for processing, breaking the loop upon any read error.*


### _parse_message (method, L208-L217, parent: OpenAIRealtimeWebRTCClient)

> *Summary: Converts a raw dictionary received from the OpenAI Realtime API into a list containing one or more `RealtimeEvent` objects by calling an internal parsing helper. It takes a single message dictionary as input and returns a list of parsed events.*


### get_factory (method, L220-L236, parent: OpenAIRealtimeWebRTCClient)

> *Summary: This method constructs a factory function that produces an `OpenAIRealtimeWebRTCClient` if the provided LLM configuration specifies "openai" and the keyword arguments include only `"websocket"`. Otherwise, it returns `None`, indicating no suitable client can be created.*


### _rtc_client (function, L242-L243)

> *Summary: This function initializes and returns an `OpenAIRealtimeWebRTCClient` instance, taking a WebSocket connection as input to establish real-time communication capabilities.*

