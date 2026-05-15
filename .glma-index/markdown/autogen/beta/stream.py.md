# autogen/beta/stream.py

4 class(es): ABCStream, _FilteredStorage, MemoryStream, SubStream. 18 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ABCStream | class |  |
| _FilteredStorage | class |  |
| MemoryStream | class |  |
| SubStream | class |  |

## Chunks

### ABCStream (class, L25-L86)

> *Summary: Provides methods to manage event streams, allowing developers to subscribe to specific events using `sub_scope` or filter them with `where`. It supports yielding sequences of events via `join` (with optional limits) and asynchronously waiting for a single matching event using `get`.*


### sub_scope (method, L27-L43, parent: ABCStream)

> *Summary: This method registers a callable function for streaming and yields control until the scope exits. Upon exiting, it automatically unsubscribes the registered function to prevent resource leaks.*


### join (method, L46-L65, parent: ABCStream)

> *Summary: This method creates an asynchronous event stream by accepting events via a background writer task and yielding them to the caller. It allows limiting the output to a specified maximum number of events or streaming indefinitely.*


### where (method, L67-L73, parent: ABCStream)

> *Summary: Filters the current stream based on a provided `condition`, which can be a specific `Condition` object or any class information. It returns a new `SubStream` instance that only includes elements satisfying the specified criteria.*


### get (method, L76-L86, parent: ABCStream)

> *Summary: This method yields an `AsyncIterator` that resolves to a future event matching the provided condition. It sets up a scope where any matching event will be used to fulfill the yielded future.*


### _FilteredStorage (class, L89-L99)

> *Summary: This class wraps an existing storage backend to selectively persist events. It intercepts `save_event` calls and only passes the event down to the inner storage if the event's type does not possess a `__transient__` attribute.*


### __init__ (method, L94-L95, parent: _FilteredStorage)

> *Summary: Initializes the object by storing a reference to an `Storage` instance provided as input. This sets up the internal dependency for subsequent operations within the class.*


### save_event (method, L97-L99, parent: _FilteredStorage)

> *Summary: If the provided event is not marked as transient, this method asynchronously persists the event and its associated context using an inner service. It acts as a conditional wrapper around the core saving mechanism.*


### MemoryStream (class, L102-L221)

> *Summary: This class manages the lifecycle and event propagation for a stream, holding subscribers and interrupters to process incoming events. It accepts an optional storage mechanism and allows developers to register callbacks that react to streamed events, which are then processed sequentially by both interruptors and standard subscribers upon calling `send`.*


### __init__ (method, L115-L141, parent: MemoryStream)

> *Summary: Initializes a stream object, setting a unique ID and managing internal subscription/interruption dictionaries. It configures history using provided or default storage, optionally filtering transient events based on the `persist_all` flag.*


### subscribe (method, L144-L151, parent: MemoryStream)

> *Summary: Registers a callback function to receive streamed data from the object. It accepts a callable and optional configuration flags like interruption behavior or synchronization settings, returning a unique subscription ID.*


### subscribe (method, L154-L161, parent: MemoryStream)

> *Summary: Registers a callback function to receive streamed data from the object. It accepts optional parameters like an interrupt flag and thread synchronization settings before returning a subscription ID for later management.*


### subscribe (method, L163-L182, parent: MemoryStream)

> *Summary: Registers a callback function to receive streamed data by creating and returning a subscription ID. It manages the subscription internally, either storing it for interruption or standard notification based on input flags.*


### unsubscribe (method, L184-L186, parent: MemoryStream)

> *Summary: Removes a subscription identifier from both the active subscribers and interrupter tracking dictionaries. This method ensures that the specified subscription is completely unregistered from the system's state.*


### send (method, L188-L221, parent: MemoryStream)

> *Summary: This method processes an incoming event by first iterating through registered interrupters; if any interrupter modifies the event, that modified version is passed to subsequent subscribers. Finally, it asynchronously notifies all registered subscribers about the potentially altered event.*


### SubStream (class, L224-L289)

> *Summary: This class manages a filtered subset of events from a parent stream based on an initial condition. It allows subscribers to register callbacks that will only receive events matching the combined filter criteria, forwarding all subscription and sending operations up to its parent stream.*


### __init__ (method, L231-L239, parent: SubStream)

> *Summary: Initializes a stream instance by assigning it a unique ID and storing references to its parent stream and the filtering condition it must satisfy. This sets up the basic structure for managing data flow within the streaming system.*


### subscribe (method, L242-L249, parent: SubStream)

> *Summary: Registers a callback function to receive streamed data from the object. It accepts the target function and optional configuration flags like interruption behavior or synchronization settings, returning a unique subscription ID.*


### subscribe (method, L252-L259, parent: SubStream)

> *Summary: Registers a callback function to receive streamed data from the object. It accepts optional parameters like an interrupt flag and thread synchronization settings to control how notifications are handled. Returns a subscription ID for later management or cancellation.*


### subscribe (method, L261-L283, parent: SubStream)

> *Summary: This method returns either a subscription ID or a wrapper function depending on whether a callback is provided. It delegates the actual subscription logic to its parent object, applying an optional filter condition if one was passed in.*


### unsubscribe (method, L285-L286, parent: SubStream)

> *Summary: This method removes a subscription identified by `sub_id` from the parent object. It delegates the unsubscription action directly to the containing class instance.*


### send (method, L288-L289, parent: SubStream)

> *Summary: This method forwards an incoming `BaseEvent` and its associated `ConversationContext` up to the parent object for processing. It acts as a simple pass-through mechanism within the event handling hierarchy.*

