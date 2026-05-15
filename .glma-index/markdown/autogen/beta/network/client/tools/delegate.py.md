# autogen/beta/network/client/tools/delegate.py

2 function(s): make_delegate_tool, _reply_or_terminal_predicate.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| make_delegate_tool | function |  |
| _reply_or_terminal_predicate | function |  |

## Chunks

### make_delegate_tool (function, L43-L138)

> *Summary: Creates a callable tool that initiates a one-shot consulting channel with a specified peer agent. It takes the target name and prompt as input, handles connection setup, sends the request, waits for a reply or terminal event within a timeout, and returns the received text content or an error string upon failure.*


### _reply_or_terminal_predicate (function, L141-L149)

> *Summary: Returns a predicate function that checks if an incoming `Envelope` is either a text reply from the specified `target_id` or any predefined terminal channel event. This allows filtering messages based on whether they constitute a substantive response or signal the end of a communication sequence.*

