# test/agentchat/realtime_agent/realtime_test_utils.py

2 function(s): text_to_speech, trace.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| text_to_speech | function |  |
| trace | function |  |

## Chunks

### text_to_speech (function, L25-L47)

> *Summary: Generates audio from a given string by calling the OpenAI Text-to-Speech API, accepting text, an API key, and optional parameters for model, voice, and output format. It returns the resulting audio content encoded as a Base64 string.*


### trace (function, L53-L84)

> *Summary: This utility provides a decorator that wraps a function to execute a provided mock before the call and optionally sets `precall` and `postcall` events around the execution. It returns a decorated version of the input function, allowing for synchronous tracing behavior.*

