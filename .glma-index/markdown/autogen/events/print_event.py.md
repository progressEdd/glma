# autogen/events/print_event.py

1 class(es): PrintEvent. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| PrintEvent | class |  |

## Chunks

### PrintEvent (class, L15-L44)

> *Summary: This event class serializes input objects into strings (handling JSON serialization for complex types) and stores them along with a separator and ending character. Its primary behavior is to execute a provided callable function using these serialized objects as arguments when the `print` method is called.*


### __init__ (method, L25-L28, parent: PrintEvent)

> *Summary: Initializes an event by converting a variable number of input objects into JSON strings. It then passes these serialized objects, along with specified formatting parameters like separator and line ending, to the parent class constructor.*


### _to_json (method, L30-L40, parent: PrintEvent)

> *Summary: Converts a given object into a JSON string representation. It prioritizes using the object's `model_dump_json` method if available, otherwise it attempts standard JSON serialization before falling back to a string conversion.*


### print (method, L42-L44, parent: PrintEvent)

> *Summary: This method executes a provided callable function with the event's stored objects as arguments. It uses resolved print settings to output the data, ensuring immediate flushing of the stream.*

