# autogen/messages/print_message.py

1 class(es): PrintMessage. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| PrintMessage | class |  |

## Chunks

### PrintMessage (class, L18-L48)

> *Summary: This class formats and prints a collection of objects to a specified output stream. It accepts variable arguments, serializes them into strings (handling JSON serialization for complex types), and then uses Python's built-in `print` function with custom separators and endings.*


### __init__ (method, L28-L31, parent: PrintMessage)

> *Summary: Initializes the message by converting all provided input objects into JSON strings. It then passes these serialized objects, along with specified formatting parameters like separator and line ending, to the parent class constructor.*


### _to_json (method, L33-L43, parent: PrintMessage)

> *Summary: Converts a given object into a JSON string representation. It prioritizes using the object's built-in `model_dump_json` method if available, otherwise it attempts standard `json.dumps`, falling back to `str()` conversion upon failure.*


### print (method, L45-L48, parent: PrintMessage)

> *Summary: This method outputs the stored objects using a provided callable function as the destination. It calls the specified function with all internal object values, respecting configured separators and flushing settings.*

