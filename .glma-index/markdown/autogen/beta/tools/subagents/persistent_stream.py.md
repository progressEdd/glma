# autogen/beta/tools/subagents/persistent_stream.py

1 function(s): persistent_stream.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| persistent_stream | function |  |

## Chunks

### persistent_stream (function, L17-L28)

> *Summary: This factory function produces a stream creator that generates a `MemoryStream` instance for a given agent and context. It ensures a unique stream ID is used by checking the context's dependencies before creating the stream tied to the provided storage.*

