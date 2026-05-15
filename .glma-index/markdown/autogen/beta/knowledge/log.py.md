# autogen/beta/knowledge/log.py

1 class(es): EventLogWriter. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| EventLogWriter | class |  |

## Chunks

### EventLogWriter (class, L16-L102)

> *Summary: This class manages the persistence of stream events to a knowledge store as Write-Ahead Log (WAL) entries. It accepts streams and events to write final logs or compaction-dropped segments, and can load all associated events by reading numbered dropped segments followed by the main log file.*


### __init__ (method, L25-L26, parent: EventLogWriter)

> *Summary: Initializes the object by storing a reference to a `KnowledgeStore` instance. This allows the class to interact with and manage knowledge data provided during instantiation.*


### persist (method, L28-L32, parent: EventLogWriter)

> *Summary: Writes a sequence of events to a specific JSON Lines file identified by the stream ID. It serializes the input iterable of base events and asynchronously writes the resulting lines to disk under the configured log prefix.*


### persist_dropped (method, L34-L45, parent: EventLogWriter)

> *Summary: This method saves events that were dropped during compaction to a uniquely named log file within the store. It first checks for existing dropped segments for the given stream ID and then writes the serialized input events to the next available numbered file.*


### load (method, L47-L67, parent: EventLogWriter)

> *Summary: Retrieves a complete, ordered list of events for a given stream ID by first loading all sequentially numbered "dropped" segments from the WAL files, followed by the final event log file. It returns these as typed `BaseEvent` instances, substituting unknown types with `UnknownEvent`.*


### _serialize_events (method, L69-L77, parent: EventLogWriter)

> *Summary: Converts an iterable of `BaseEvent` objects into a list of JSON strings. Each string represents an event, containing its qualified type and serialized data dictionary.*


### _load_file (method, L79-L102, parent: EventLogWriter)

> *Summary: Reads a file specified by `path` and parses its JSON lines into a list of structured event objects. It attempts to instantiate specific event types based on the record's "type" field, falling back to an `UnknownEvent` if the type is unrecognized or parsing fails.*

