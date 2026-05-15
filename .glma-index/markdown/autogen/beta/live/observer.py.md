# autogen/beta/live/observer.py

1 function(s): TTSObserver. 1 class(es): _ChunkToSpeech. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TTSObserver | function |  |
| _ChunkToSpeech | class |  |

## Chunks

### TTSObserver (function, L14-L25)

> *Summary: Creates an observer that wraps a text-to-speech engine using configuration data. It listens for model message chunks to stream audio and also triggers the TTS completion handler upon receiving a full model message.*


### _ChunkToSpeech (class, L28-L75)

> *Summary: This class buffers incoming text chunks from a model, accumulating them until the accumulated text meets a minimum character count and ends at a sentence boundary. Upon meeting these criteria or when the stream completes, it synthesizes the buffered text into audio PCM and sends it as an event.*


### __init__ (method, L29-L37, parent: _ChunkToSpeech)

> *Summary: Initializes the observer with a `TTSConfig` object and an optional minimum character count. It stores these configuration parameters internally to manage text processing state.*


### on_chunk (method, L39-L47, parent: _ChunkToSpeech)

> *Summary: This method processes incoming message chunks by appending the content to a pending buffer. If the accumulated text meets the criteria defined by `_should_emit`, it asynchronously emits that text using the provided context.*


### on_complete (method, L49-L51, parent: _ChunkToSpeech)

> *Summary: When an operation finishes, this method emits any buffered text content to the provided context and then clears the internal buffer. It ensures that pending output is delivered upon completion of a task.*


### _should_emit (method, L53-L66, parent: _ChunkToSpeech)

> *Summary: Checks if the input text meets a minimum length and, if so, attempts to segment it at sentence boundaries. It returns the processed text up to the last detected boundary or `None` if no suitable segmentation point is found.*


### _emit (method, L68-L75, parent: _ChunkToSpeech)

> *Summary: This method takes text and a context object, synthesizes the text into PCM audio using configuration settings, and then sends a `SynthesizedAudioEvent` containing the resulting audio if synthesis was successful.*

