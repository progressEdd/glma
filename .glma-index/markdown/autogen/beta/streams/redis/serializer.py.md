# autogen/beta/streams/redis/serializer.py

2 function(s): serialize, deserialize. 1 class(es): Serializer.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Serializer | class |  |
| serialize | function |  |
| deserialize | function |  |

## Chunks

### Serializer (class, L13-L17)

> *Summary: Defines an enumeration to specify the serialization format used for storing data in Redis or transmitting it via pub/sub. It provides constants for JSON (the default) and Pickle formats.*


### serialize (function, L20-L24)

> *Summary: Converts a Python object into a byte string based on the provided serialization format. If `pickle` is requested, it uses `pickle.dumps`; otherwise, it JSON-encodes and encodes the result to bytes.*


### deserialize (function, L27-L31)

> *Summary: Converts raw byte data into a usable Python object based on the provided serialization format. If the format is Pickle, it uses `pickle.loads`; otherwise, it parses the bytes as JSON and then processes the resulting structure.*

