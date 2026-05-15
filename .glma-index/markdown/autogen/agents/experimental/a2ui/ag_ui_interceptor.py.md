# autogen/agents/experimental/a2ui/ag_ui_interceptor.py

1 function(s): create_a2ui_event_interceptor.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| create_a2ui_event_interceptor | function |  |

## Chunks

### create_a2ui_event_interceptor (function, L25-L90)

> *Summary: Generates an asynchronous event interceptor that processes agent responses to extract A2UI JSON content. It parses the response text using provided delimiters and versions, yielding `ActivitySnapshotEvent`s for detected operations while simultaneously stripping the extracted A2UI data from the original response message.*

