# autogen/agentchat/realtime/experimental/audio_adapters/websocket_audio_adapter.py

1 function(s): websocket_audio_adapter. 1 class(es): WebSocketAudioAdapter. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WebSocketAudioAdapter | class |  |
| websocket_audio_adapter | function |  |

## Chunks

### WebSocketAudioAdapter (class, L31-L133)

> *Summary: This adapter observes a WebSocket connection, processing incoming `RealtimeEvent`s from the OpenAI Realtime API. It forwards audio data received via `AudioDelta` events over the websocket and handles speech start events by potentially truncating an ongoing response using timing information derived from media timestamps.*


### __init__ (method, L32-L47, parent: WebSocketAudioAdapter)

> *Summary: Initializes an observer to manage real-time audio data from a WebSocket connection. It stores the provided `WebSocket` instance and sets up internal state variables like stream IDs, timestamps, and message queues for tracking ongoing interactions.*


### on_event (method, L49-L74, parent: WebSocketAudioAdapter)

> *Summary: When receiving a `RealtimeEvent`, this method processes audio deltas by decoding and sending the base64-encoded audio payload over the websocket, while also tracking response start times and updating the last assistant item. It additionally handles `SpeechStarted` events to trigger an interruption of any ongoing response.*


### handle_speech_started_event (method, L76-L101, parent: WebSocketAudioAdapter)

> *Summary: When the caller begins speaking, this method calculates the elapsed time since the response started and truncates the last assistant audio item if one exists. It then sends a "clear" event over the WebSocket and resets internal state tracking variables.*


### send_mark (method, L103-L107, parent: WebSocketAudioAdapter)

> *Summary: When called, this method sends a specific "mark" event over the established WebSocket connection using the stream ID. It also queues the `"responsePart"` marker internally for tracking purposes.*


### initialize_session (method, L109-L112, parent: WebSocketAudioAdapter)

> *Summary: Sets up the real-time connection by sending a session update to the client, specifying that both input and output audio streams will use the PCM16 format. This configures the initial communication parameters for audio exchange.*


### run_loop (method, L114-L133, parent: WebSocketAudioAdapter)

> *Summary: This asynchronous method continuously reads text messages from a websocket connection, parsing them to handle different events. It forwards audio payloads marked as "media" to the `RealtimeClient` and initializes stream tracking when a "start" event is received.*


### websocket_audio_adapter (function, L138-L139)

> *Summary: This function wraps a provided `WebSocket` connection to instantiate and return an adapter that implements the `RealtimeObserver` interface. It serves as a factory for creating audio handling logic based on a live websocket stream.*

