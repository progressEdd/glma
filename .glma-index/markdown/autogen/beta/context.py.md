# autogen/beta/context.py

2 class(es): Stream, ConversationContext. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Stream | class |  |
| ConversationContext | class |  |

## Chunks

### Stream (class, L24-L79)

> *Summary: Defines a protocol for managing event streams, allowing asynchronous sending of events and providing methods to filter, join, subscribe to, and retrieve specific events based on defined conditions or scopes. It supports both direct subscription callbacks and context-managed iteration over the stream's data.*


### send (method, L27-L27, parent: Stream)

> *Summary: This asynchronous method transmits a `BaseEvent` using the provided `ConversationContext`. It handles the core logic for dispatching events within the conversation flow.*


### where (method, L29-L29, parent: Stream)

> *Summary: Filters a collection based on the provided `condition` (which can be a class or a specific condition object). It returns a stream containing only the elements that satisfy the given criteria.*


### join (method, L31-L35, parent: Stream)

> *Summary: Combines multiple event streams into a single sequence. It accepts an optional `max_events` limit and yields events asynchronously until the combined stream is exhausted or the limit is reached.*


### subscribe (method, L38-L45, parent: Stream)

> *Summary: Registers a callback function to receive notifications from the context. It accepts the target function and optional parameters controlling interruption behavior, thread synchronization, and condition waiting. Returns a unique identifier for managing the subscription.*


### subscribe (method, L48-L55, parent: Stream)

> *Summary: Registers a callback function to receive notifications from the object. It accepts optional parameters like an interrupt flag and thread synchronization settings, returning a subscription ID for later management.*


### subscribe (method, L57-L64, parent: Stream)

> *Summary: Registers a callback function to receive notifications from the context object. It accepts optional parameters like an interrupt flag and thread synchronization settings, returning a subscription ID or the callable itself.*


### unsubscribe (method, L66-L66, parent: Stream)

> *Summary: Removes a specific subscription identified by `sub_id` from the current context object. It takes one `SubId` as input and returns nothing upon successful execution.*


### sub_scope (method, L68-L74, parent: Stream)

> *Summary: This method creates a nested execution context manager around a given callable. It accepts optional flags to control interruption behavior and thread synchronization during the scope's execution.*


### get (method, L76-L79, parent: Stream)

> *Summary: Retrieves an asynchronous context manager based on a provided `ClassInfo` or `Condition`. It returns an object that resolves to a `BaseEvent` future upon execution.*


### ConversationContext (class, L83-L102)

> *Summary: Manages the state of an ongoing conversation by holding stream connections, context variables, and message history. It provides asynchronous methods to both receive input from a user via the stream and send events into the conversation flow.*


### input (method, L94-L99, parent: ConversationContext)

> *Summary: Sends a user message to the underlying stream and waits for a response within a specified timeout. It takes a string message as input and returns the content of the resulting human message.*


### send (method, L101-L102, parent: ConversationContext)

> *Summary: This method asynchronously forwards an incoming `BaseEvent` to the underlying stream, passing itself as a reference during transmission. It acts as a simple relay mechanism for event propagation within the system.*

