# autogen/beta/events/_serialization.py

11 function(s): _is_event_instance, _is_event_class, qualified_name, qualified_name_from_class, event_to_dict, serialize_value, deserialize_payload, deserialize_value, _resolve_class, _resolve_event_type and 1 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _is_event_instance | function |  |
| _is_event_class | function |  |
| qualified_name | function |  |
| qualified_name_from_class | function |  |
| event_to_dict | function |  |
| serialize_value | function |  |
| deserialize_payload | function |  |
| deserialize_value | function |  |
| _resolve_class | function |  |
| _resolve_event_type | function |  |
| import_event_class | function |  |

## Chunks

### _is_event_instance (function, L20-L21)

> *Summary: Checks if a given value is an instance of an event by inspecting its type for the presence of `_event_fields_`. Returns `True` if the attribute exists, indicating it's an event object.*


### _is_event_class (function, L24-L25)

> *Summary: Checks if a given object is a class that has been registered as an event by checking if it's a type and possesses the `_event_fields_` attribute. Returns a boolean indicating whether the input conforms to the expected event class structure.*


### qualified_name (function, L28-L30)

> *Summary: Retrieves the complete, unambiguous name of a given event object's class. It takes an `event` instance as input and returns its string representation.*


### qualified_name_from_class (function, L33-L35)

> *Summary: Constructs a string representing the full path to a given class by combining its module and qualified name. It takes a Python type object as input and returns a fully qualified name string.*


### event_to_dict (function, L38-L49)

> *Summary: Converts a `BaseEvent` instance into a serializable dictionary by iterating over its attributes. It skips any internal attributes (those starting with an underscore) and recursively serializes each value using `serialize_value`.*


### serialize_value (function, L52-L79)

> *Summary: This function recursively converts various Python objects into JSON-compatible structures. It handles custom types like events, enums, exceptions, dataclasses, and Pydantic models by wrapping them in specific dictionary formats before serializing nested collections or primitive values directly.*


### deserialize_payload (function, L82-L90)

> *Summary: This function recursively processes an input dictionary to reconstruct nested events and special data types within a payload. It iterates over the provided dictionary, applying a recursive deserialization process to each value using an optional event registry.*


### deserialize_value (function, L93-L122)

> *Summary: Recursively converts serialized data structures back into native Python objects by inspecting special keys like `__event__`, `__bytes__`, or `__pydantic__`. It handles nested events, byte decoding, UUID reconstruction, and deserializing dataclasses or Pydantic models based on the provided registry.*


### _resolve_class (function, L125-L139)

> *Summary: This function dynamically imports and resolves a Python class given its fully qualified string path. It iteratively attempts to load the module and traverse attributes until it finds an object that is a `type`, raising an error if resolution fails.*


### _resolve_event_type (function, L142-L151)

> *Summary: This function attempts to map a string type name to its corresponding class, prioritizing an provided `event_registry`. If the registry fails to resolve it, it falls back to dynamically importing the event class based on the type name.*


### import_event_class (function, L154-L174)

> *Summary: Retrieves an event class object given its fully qualified name string. It iteratively attempts to resolve nested module paths by importing modules and traversing attribute chains until a valid `BaseEvent` subclass is found or all possibilities are exhausted.*

