# autogen/beta/policies/_pairing.py

1 function(s): ensure_tool_pairing.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ensure_tool_pairing | function |  |

## Chunks

### ensure_tool_pairing (function, L10-L26)

> *Summary: Filters a list of events to remove `ToolResultsEvents` that lack a corresponding preceding `ToolCallsEvent`. It achieves this by collecting all tool call IDs from model responses and only retaining results whose parent ID matches one of those collected IDs.*

