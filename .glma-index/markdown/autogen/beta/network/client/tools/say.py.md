# autogen/beta/network/client/tools/say.py

1 function(s): make_say_tool.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| make_say_tool | function |  |

## Chunks

### make_say_tool (function, L31-L110)

> *Summary: Creates a stable, closure-bound tool that posts text messages to a specified or current channel. It accepts content and optional audience/channel identifiers, resolving agent names to IDs and constructing the message envelope via an adapter before sending it through the client's hub interface.*

