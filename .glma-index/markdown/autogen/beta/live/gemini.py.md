# autogen/beta/live/gemini.py

6 function(s): _tool_schema_to_function_declaration, _ensure_object_schema, _send_tool_result, _pump_events, _handle_server_content, _encode_args. 4 class(es): AudioOutput, TextOutput, InputConfig, RealTimeConfig. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AudioOutput | class |  |
| TextOutput | class |  |
| InputConfig | class |  |
| RealTimeConfig | class |  |
| _tool_schema_to_function_declaration | function |  |
| _ensure_object_schema | function |  |
| _send_tool_result | function |  |
| _pump_events | function |  |
| _handle_server_content | function |  |
| _encode_args | function |  |

## Chunks

### AudioOutput (class, L64-L74)

> *Summary: Configures audio output settings for a Gemini live session, enabling the `AUDIO` response modality and surfacing spoken responses as transcription events. It accepts optional parameters like a specific voice name and language code.*


### TextOutput (class, L78-L83)

> *Summary: This class configures a Gemini live session to only receive and process text data. It ensures that the model's output is delivered as raw text chunks without any associated audio playback.*


### InputConfig (class, L87-L98)

> *Summary: This configuration object controls audio input settings for a live Gemini session. It accepts boolean flags and optional dictionaries to enable transcription, specify languages, and configure activity detection and turn coverage handling.*


### RealTimeConfig (class, L101-L217)

> *Summary: Configures a bidirectional connection to Gemini's Live API based on provided model and I/O settings. It establishes an asynchronous session that pumps captured audio into the API while emitting transcription, audio, and tool-call events onto a supplied context stream.*


### __init__ (method, L110-L167, parent: RealTimeConfig)

> *Summary: Initializes a connection configuration for a live model interaction, accepting parameters like the target model name, desired output type (audio or text), input settings, and generation constraints. It constructs a comprehensive configuration dictionary based on these inputs to manage modalities, transcription, and real-time audio processing features.*


### _build_session (method, L169-L182, parent: RealTimeConfig)

> *Summary: Constructs a configuration dictionary by merging base settings with optional system instructions and tool definitions. It takes iterable lists of strings for instructions and `ToolSchema` objects to build the final connection configuration object.*


### session (method, L185-L217, parent: RealTimeConfig)

> *Summary: Establishes a real-time streaming session with the Gemini model by connecting to the client using provided instructions and tools. It concurrently pumps incoming audio events and forwards tool results while yielding control until the stream is terminated.*


### _tool_schema_to_function_declaration (function, L220-L227)

> *Summary: Converts a `ToolSchema` object into a Gemini-compatible function declaration dictionary. It specifically handles `FunctionToolSchema`, extracting the name, description, and ensuring the parameters are correctly formatted as an object schema.*


### _ensure_object_schema (function, L230-L234)

> *Summary: If provided parameters are null or lack a specified type, it returns an empty object schema. Otherwise, it validates and returns the input dictionary as the object schema.*


### _send_tool_result (function, L237-L257)

> *Summary: This asynchronous function processes a `ToolResultEvent` by extracting content from its parts—either as text or serialized data—and aggregates these into a single string. It then sends this aggregated result back to the session using a `FunctionResponse`.*


### _pump_events (function, L260-L296)

> *Summary: Continuously processes incoming messages from an asynchronous session until the connection closes or a turn completes. It aggregates server content into a response and emits tool call events when function calls are received, resetting the accumulated text upon turn completion.*


### _handle_server_content (function, L299-L327)

> *Summary: Processes incoming live server content to emit transcription updates and model responses into the conversation context. It streams text chunks from both input and output transcriptions, while also sending synthesized audio data when present in the model's turn parts.*


### _encode_args (function, L330-L333)

> *Summary: Converts a dictionary of arguments into a JSON string representation. If the input argument dictionary is null or empty, it returns an empty JSON object string.*

