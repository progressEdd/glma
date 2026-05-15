# test/opentelemetry/conftest.py

1 class(es): InMemorySpanExporter. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| InMemorySpanExporter | class |  |

## Chunks

### InMemorySpanExporter (class, L14-L38)

> *Summary: This class implements a test-specific span exporter that collects incoming `ReadableSpan` objects into an internal list, ensuring thread safety with a lock. It provides methods to retrieve all collected spans, clear the collection, and shut down gracefully.*


### __init__ (method, L20-L22, parent: InMemorySpanExporter)

> *Summary: Initializes an object to manage a collection of `ReadableSpan` objects and ensures thread-safe access using a lock. This setup prepares the instance for concurrent tracking and modification of spans.*


### export (method, L24-L27, parent: InMemorySpanExporter)

> *Summary: This method safely appends a sequence of `ReadableSpan` objects to an internal list while holding a lock, then returns a success status indicating the export operation completed.*


### get_finished_spans (method, L29-L31, parent: InMemorySpanExporter)

> *Summary: Retrieves a snapshot of all currently recorded spans from the internal collection, ensuring thread safety via a lock. It returns these spans as a list of `ReadableSpan` objects.*


### clear (method, L33-L35, parent: InMemorySpanExporter)

> *Summary: Resets the internal list of spans by acquiring a lock to ensure thread safety. This method clears all recorded span data within the object's state.*


### shutdown (method, L37-L38, parent: InMemorySpanExporter)

> *Summary: Clears all state within the fixture instance before teardown. This ensures a clean slate for subsequent tests.*

