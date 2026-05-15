# autogen/opentelemetry/instrumentators/pattern.py

2 function(s): instrument_pattern, instrument_groupchat.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_pattern | function |  |
| instrument_groupchat | function |  |

## Chunks

### instrument_pattern (function, L25-L127)

> *Summary: This function modifies a given pattern instance to automatically trace its group chat creation process using OpenTelemetry. It wraps the `prepare_group_chat` method, instrumenting all created agents and group chats within the returned pattern object.*


### instrument_groupchat (function, L130-L214)

> *Summary: This function modifies a `GroupChat` object by wrapping its internal methods (`_create_internal_agents`, `a_auto_select_speaker`, and `_auto_select_speaker`) with OpenTelemetry tracing logic. It takes the `GroupChat` instance and a `TracerProvider` as input, returning the instrumented `GroupChat` with spans added to track agent selection processes.*

