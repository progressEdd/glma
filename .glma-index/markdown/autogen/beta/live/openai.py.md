# autogen/beta/live/openai.py

4 function(s): _tool_schema_to_session_tool, _send_tool_result, _pump_events, _voice_to_wav_buffer. 7 class(es): AudioOutput, TextOutput, InputConfig, STTConfig, STTTranslationConfig, TTSConfig, RealTimeConfig. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AudioOutput | class |  |
| TextOutput | class |  |
| InputConfig | class |  |
| STTConfig | class |  |
| STTTranslationConfig | class |  |
| TTSConfig | class |  |
| RealTimeConfig | class |  |
| _tool_schema_to_session_tool | function |  |
| _send_tool_result | function |  |
| _pump_events | function |  |
| _voice_to_wav_buffer | function |  |

## Chunks

### AudioOutput (class, L91-L101)

> *Summary: Defines configuration parameters for real-time audio output, mirroring an OpenAI type structure. It specifies the voice to use, the audio format (defaulting to PCM at 24kHz), and playback speed.*


### TextOutput (class, L105-L109)

> *Summary: This class represents a configuration for real-time sessions that only accept text output from the model. It explicitly disables any audio generation, ensuring the model's response is delivered as raw text chunks.*


### InputConfig (class, L113-L130)

> *Summary: This class holds configuration parameters for real-time audio input to an OpenAI service. It accepts settings for audio format, optional transcription and noise reduction, and default turn detection behavior.*


### STTConfig (class, L133-L158)

> *Summary: This configuration class manages speech-to-text operations using an OpenAI client. It takes a model identifier and optionally a pre-configured client, then asynchronously transcribes audio input while streaming partial results to the provided context.*


### __init__ (method, L134-L141, parent: STTConfig)

> *Summary: Initializes the object by setting a specified audio model identifier and optionally accepting an existing `AsyncOpenAI` client; otherwise, it instantiates a new one.*


### transcribe (method, L143-L158, parent: STTConfig)

> *Summary: This method streams audio transcription from a `VoiceInput` using the OpenAI client, yielding partial text updates to the provided `Context` as they arrive. It returns the complete transcribed string upon stream completion.*


### STTTranslationConfig (class, L161-L179)

> *Summary: This configuration object manages speech-to-text translation using an OpenAI client. It takes a model identifier and optionally a pre-configured client, then asynchronously transcribes audio input into text while notifying the provided context upon completion.*


### __init__ (method, L162-L169, parent: STTTranslationConfig)

> *Summary: Initializes the object by setting a specified audio model identifier and optionally accepting an existing `AsyncOpenAI` client; otherwise, it defaults to creating a new one.*


### transcribe (method, L171-L179, parent: STTTranslationConfig)

> *Summary: This method takes a voice input and context to asynchronously transcribe the audio using an OpenAI client. It sends a `TranscriptionCompletedEvent` via the context upon successful transcription and returns the resulting text string.*


### TTSConfig (class, L182-L205)

> *Summary: This configuration object manages text-to-speech generation using OpenAI's API. It accepts a model identifier and optional voice/speed settings to synthesize input text into raw PCM audio bytes via an asynchronous client call.*


### __init__ (method, L183-L195, parent: TTSConfig)

> *Summary: Initializes an object to manage speech generation by setting the target model, preferred voice, and playback speed. It automatically creates an `AsyncOpenAI` client if none is provided during instantiation.*


### synthesize (method, L197-L205, parent: TTSConfig)

> *Summary: Generates audio bytes from input text by calling the OpenAI speech API with specified model and voice settings. It returns the raw PCM audio data as a byte string.*


### RealTimeConfig (class, L208-L318)

> *Summary: Configures a real-time transcription session using OpenAI's bidirectional API by accepting model names and various input/output parameters. Calling the `session` context manager establishes a connection, pumps captured audio events into the stream, and yields control while processing incoming transcription or tool result events on the provided context.*


### __init__ (method, L216-L271, parent: RealTimeConfig)

> *Summary: Initializes a real-time communication handler by configuring parameters for an OpenAI model, accepting inputs like desired output type (audio/text), input configuration, and optional tracing settings. It constructs a session request dictionary based on these inputs to manage the connection lifecycle with an `AsyncOpenAI` client.*


### _build_session (method, L273-L284, parent: RealTimeConfig)

> *Summary: Constructs a session request payload by merging base session parameters with optional instructions and tool definitions. It serializes provided instruction strings and transforms `ToolSchema` objects into the required session tool format before returning the final configuration object.*


### session (method, L287-L318, parent: RealTimeConfig)

> *Summary: Establishes a real-time connection to an OpenAI model, managing the session state with provided instructions and tools. It concurrently streams incoming audio events for buffering and tool results for forwarding until the stream is closed or cancelled.*


### _tool_schema_to_session_tool (function, L321-L329)

> *Summary: Converts a `ToolSchema` instance into a `RealtimeFunctionToolParam`, specifically handling the `FunctionToolSchema` by extracting function name, description, and parameters. It raises an error if the input schema is not of the supported function type.*


### _send_tool_result (function, L332-L353)

> *Summary: This asynchronous function processes a `ToolResultEvent` by aggregating content from its parts—either text or serialized data—into a single string. It then sends this aggregated output as a "function\_call\_output" item to the conversation and triggers a response update on the connection.*


### _pump_events (function, L356-L400)

> *Summary: This asynchronous function processes incoming events from a real-time connection and relays them to a conversation context. It handles various event types—such as audio transcription deltas/completions, synthesized audio chunks, text/audio output deltas, tool calls, and final response completion—by sending corresponding structured events into the context.*


### _voice_to_wav_buffer (function, L403-L412)

> *Summary: Converts a `VoiceInput` object, containing audio data and metadata like channels and frame rate, into an in-memory WAV file buffer. It writes the raw audio content to the buffer and returns it ready for use as a streamable `.wav` file.*

