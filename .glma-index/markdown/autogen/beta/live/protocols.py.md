# autogen/beta/live/protocols.py

2 class(es): AudioPlayer, TTSConfig. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AudioPlayer | class |  |
| TTSConfig | class |  |

## Chunks

### AudioPlayer (class, L11-L12)

> *Summary: Defines an asynchronous protocol requiring a `play` method that accepts content of type `T1` and returns nothing. This establishes a contract for any object intended to handle audio playback.*


### play (method, L12-L12, parent: AudioPlayer)

> *Summary: This asynchronous method accepts a piece of content and initiates playback or processing based on that input. It returns nothing upon completion.*


### TTSConfig (class, L15-L16)

> *Summary: Defines a protocol for Text-to-Speech configurations that must implement an asynchronous `synthesize` method accepting a string and returning a specific type. This ensures any conforming object can generate audio from input text.*


### synthesize (method, L16-L16, parent: TTSConfig)

> *Summary: This asynchronous method takes a string input and returns an object of type `T2`, likely performing some form of synthesis or generation based on the provided text.*

