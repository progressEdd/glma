# autogen/agentchat/realtime/experimental/clients/gemini/client.py

1 class(es): GeminiRealtimeClient. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GeminiRealtimeClient | class |  |

## Chunks

### GeminiRealtimeClient (class, L38-L269)

> *Summary: This class manages a real-time connection to the Gemini API, configured via an `LLMConfig` input. It allows sending text, audio chunks, and function results over a WebSocket connection while asynchronously receiving events like model turns or tool calls. The primary output is a stream of parsed `RealtimeEvent` objects when its `read_events` method is called within a managed context.*


### __init__ (method, L41-L74, parent: GeminiRealtimeClient)

> *Summary: Initializes a client for the Gemini Realtime API by accepting an LLM configuration and an optional logger. It parses the provided configuration to set up model details, base URL, temperature, and initializes internal state variables for connection management.*


### logger (method, L77-L79, parent: GeminiRealtimeClient)

> *Summary: Retrieves a logging instance, defaulting to a globally configured logger if no specific one has been set on the object. This provides consistent logging access for the Gemini Realtime API client.*


### connection (method, L82-L86, parent: GeminiRealtimeClient)

> *Summary: Retrieves the established Gemini WebSocket connection object if it has been previously initialized. It raises a `RuntimeError` if the internal connection state is uninitialized.*


### send_function_result (method, L88-L99, parent: GeminiRealtimeClient)

> *Summary: Sends the outcome of a previously requested function to the Gemini Realtime API using a specific call ID and the resulting string value. This asynchronous method transmits the structured response payload over an established connection if event reading is active.*


### send_text (method, L101-L116, parent: GeminiRealtimeClient)

> *Summary: Sends a structured JSON message containing the specified `role` and `text` to the Gemini Realtime API connection if event reading is active. The function constructs a payload including a `turn_complete` flag before transmitting it asynchronously.*


### send_audio (method, L118-L136, parent: GeminiRealtimeClient)

> *Summary: This method transmits audio data to the Gemini Realtime API by constructing a specific JSON message containing PCM audio chunks. It queues the incoming audio buffer and sends the formatted message over the established connection if event reading is active.*


### truncate_audio (method, L138-L140, parent: GeminiRealtimeClient)

> *Summary: This method currently does nothing as the Gemini Realtime API does not natively support audio truncation. It accepts an end time in milliseconds, a content index, and an item ID but returns no value.*


### _initialize_session (method, L142-L172, parent: GeminiRealtimeClient)

> *Summary: Configures and sends the initial session parameters to the Gemini Realtime API connection. It uses internal state like system instructions, model name, available tools, response modalities, and generation settings to establish the chat context.*


### session_update (method, L174-L183, parent: GeminiRealtimeClient)

> *Summary: This method records configuration updates intended for a session by merging the provided `session_options` dictionary into an internal pending updates store. It ignores any incoming updates if the client is currently processing real-time events.*


### connect (method, L186-L194, parent: GeminiRealtimeClient)

> *Summary: Establishes an asynchronous connection to the Gemini Realtime API using a provided base URL and JSON content type. It yields control while the connection is active, ensuring cleanup by setting the internal connection reference to `None` upon exiting the block.*


### read_events (method, L196-L205, parent: GeminiRealtimeClient)

> *Summary: This asynchronous method streams real-time events from the Gemini client connection. It requires an active connection and yields each received `RealtimeEvent` until the stream is closed or interrupted.*


### _read_from_connection (method, L207-L213, parent: GeminiRealtimeClient)

> *Summary: This asynchronous method continuously reads raw messages from an established connection stream. It decodes the incoming data, parses it as JSON to extract multiple events, and yields each resulting event sequentially.*


### _parse_message (method, L215-L251, parent: GeminiRealtimeClient)

> *Summary: This method processes a raw dictionary response from the Gemini Realtime API to extract structured events. It checks for specific keys like `serverContent`, `toolCall`, or `setupComplete` to return specialized event objects such as `AudioDelta`, `FunctionCall`, or `SessionCreated`. If none of these structures are present, it defaults to returning a generic `RealtimeEvent`.*


### get_factory (method, L254-L269, parent: GeminiRealtimeClient)

> *Summary: This method conditionally returns a factory function that instantiates a `GeminiRealtimeClient` if the provided LLM configuration specifies "google" as the API type and no extra keyword arguments are present. Otherwise, it returns `None`.*

