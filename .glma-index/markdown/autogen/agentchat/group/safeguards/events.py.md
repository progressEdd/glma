# autogen/agentchat/group/safeguards/events.py

1 class(es): SafeguardEvent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SafeguardEvent | class |  |

## Chunks

### SafeguardEvent (class, L38-L140)

> *Summary: This class encapsulates safeguard-related occurrences by storing details like event type, messages, and involved agents. It provides a `print` method that formats and outputs these events to the console with distinct colors and emojis based on the event's nature (e.g., check, violation, action).*


### __init__ (method, L49-L70, parent: SafeguardEvent)

> *Summary: Initializes an event object by accepting various optional and required parameters such as a unique identifier, event type, message content, and details about the involved agents or guardrails. It stores these inputs to represent a specific interaction or safety event within the system.*


### print (method, L72-L140, parent: SafeguardEvent)

> *Summary: This method formats and prints an event message to a provided callable, dynamically choosing colors and emojis based on the `event_type`. It constructs detailed output including agent information, guardrail details, and content previews before printing a matching footer for non-load events.*

