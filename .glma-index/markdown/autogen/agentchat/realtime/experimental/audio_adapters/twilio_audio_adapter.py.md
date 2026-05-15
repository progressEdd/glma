# autogen/agentchat/realtime/experimental/audio_adapters/twilio_audio_adapter.py

1 function(s): twilio_audio_adapter. 1 class(es): TwilioAudioAdapter. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TwilioAudioAdapter | class |  |
| twilio_audio_adapter | function |  |

## Chunks

### TwilioAudioAdapter (class, L32-L142)

> *Summary: This class acts as an adapter, managing bidirectional audio streaming between a Twilio WebSocket and the OpenAI Realtime API. It processes incoming events from the Realtime API to send audio data back to Twilio, while simultaneously consuming media packets from Twilio to forward them to the AI client. Key behaviors include marking audio segments and truncating responses when user speech is detected.*


### __init__ (method, L35-L50, parent: TwilioAudioAdapter)

> *Summary: Initializes an adapter to manage real-time audio streaming between Twilio and the OpenAI Realtime API. It accepts a WebSocket connection object and sets up internal state variables for tracking stream IDs, timestamps, and queued messages.*


### on_event (method, L52-L77, parent: TwilioAudioAdapter)

> *Summary: When receiving a `RealtimeEvent`, this method processes audio data by encoding and sending it as a media payload over the WebSocket to Twilio, while also tracking response start times and updating the last assistant item ID. It additionally checks for a `SpeechStarted` event to trigger an interruption if a previous assistant response is active.*


### handle_speech_started_event (method, L79-L105, parent: TwilioAudioAdapter)

> *Summary: When the caller begins speaking, this method calculates the elapsed time since the assistant's response started and truncates the ongoing audio item if one exists. It then sends a "clear" event over the websocket and resets internal state tracking for responses.*


### send_mark (method, L107-L112, parent: TwilioAudioAdapter)

> *Summary: When called, this method sends a specific audio interruption mark event to the Twilio websocket if a stream SID is available. It constructs and transmits a JSON message indicating a "responsePart" mark while also queuing that part name internally.*


### run_loop (method, L114-L134, parent: TwilioAudioAdapter)

> *Summary: Continuously processes incoming text messages from a WebSocket connection, parsing JSON data to handle stream start events, extract media payloads for audio transmission via `realtime_client`, and manage marking queue items. It updates internal state based on received events like "media" or "start."*


### initialize_session (method, L136-L142, parent: TwilioAudioAdapter)

> *Summary: Sets up the initial configuration for a real-time audio session by instructing the underlying client to use G711 ulaw encoding for both input and output audio streams. This method ensures consistent audio format handling at the start of the connection.*


### twilio_audio_adapter (function, L147-L148)

> *Summary: This function takes a WebSocket connection and returns an instance of `TwilioAudioAdapter`, which implements the `RealtimeObserver` interface for handling real-time audio streams.*

