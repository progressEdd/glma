# autogen/beta/network/envelope.py

1 function(s): visible_to. 1 class(es): Envelope. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Envelope | class |  |
| visible_to | function |  |

## Chunks

### Envelope (class, L81-L133)

> *Summary: Represents the standardized wire format for all Agent-to-Agent messages, containing metadata like sender/receiver IDs, event type, and data payload. It provides serialization methods to convert instances to JSON strings and reconstruct objects from dictionaries or JSON text.*


### to_dict (method, L119-L121, parent: Envelope)

> *Summary: Converts the object's state into a JSON-serializable dictionary representation. This method ensures that all fields can be reliably converted back to the original object structure.*


### to_json (method, L123-L125, parent: Envelope)

> *Summary: Converts the object's internal state into a standardized JSON string representation. It serializes the dictionary form of the object, ensuring keys are sorted for consistent hashing across different processes.*


### from_dict (method, L128-L129, parent: Envelope)

> *Summary: Constructs an instance of the class using a dictionary by unpacking its contents as keyword arguments. It takes a dictionary as input and returns a fully initialized object of the specified type.*


### from_json (method, L132-L133, parent: Envelope)

> *Summary: Parses a JSON string input into an instance of the class by first decoding the string to a dictionary and then calling the class's `from_dict` method. This allows object creation directly from serialized JSON data.*


### visible_to (function, L136-L147)

> *Summary: Determines if a specific recipient can view an envelope based on its addressing rules. It returns `True` if the sender matches the participant, if the envelope is a broadcast (`audience=None`), or if the participant is explicitly listed in the envelope's audience.*

