# autogen/beta/policies/alert.py

1 class(es): AlertPolicy. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AlertPolicy | class |  |

## Chunks

### AlertPolicy (class, L21-L95)

> *Summary: This policy injects observer alerts into the LLM prompt by filtering events for unique `ObserverAlert` instances based on content, not object identity. It appends non-fatal alerts as text to the prompts and emits a `HaltEvent` if any fatal alerts are found, ensuring critical issues stop execution.*


### __init__ (method, L45-L46, parent: AlertPolicy)

> *Summary: Initializes an instance by creating an empty set to track unique tuples representing delivered alerts. This set stores the keys for tracking which notifications have already been sent.*


### apply (method, L48-L87, parent: AlertPolicy)

> *Summary: Processes incoming events to identify and manage alerts. It filters for undelivered `ObserverAlert`s, injects non-fatal ones into the prompt list, and emits a `HaltEvent` via the context if any fatal alerts are found.*


### _format_alerts (method, L90-L95, parent: AlertPolicy)

> *Summary: This method takes a list of `ObserverAlert` objects and formats them into a single, multi-line string report. It prepends a header and iterates through the alerts, formatting each one with its severity level, source, and message.*

