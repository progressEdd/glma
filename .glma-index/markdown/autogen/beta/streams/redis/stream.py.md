# autogen/beta/streams/redis/stream.py

1 class(es): RedisStream. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RedisStream | class |  |

## Chunks

### RedisStream (class, L24-L143)

> *Summary: This class manages a persistent, distributed event stream backed by Redis, ensuring all events are broadcast via Pub/Sub across multiple processes. It handles local immediate dispatch upon sending while simultaneously persisting the event and publishing it to Redis for remote listeners to receive and process.*


### __init__ (method, L45-L74, parent: RedisStream)

> *Summary: Initializes a Redis-backed stream handler by setting up connections, storage, and necessary internal state for publishing and subscribing. It configures the stream using provided Redis credentials, prefix, and serializer, while also managing event subscription lifecycle to prevent duplicate writes.*


### _ensure_listener (method, L76-L80, parent: RedisStream)

> *Summary: Checks if an asynchronous Redis Pub/Sub listener task is active; if it's missing or finished, a new listening task is created and started to begin monitoring streams.*


### _listen (method, L82-L104, parent: RedisStream)

> *Summary: This method subscribes to a Redis Pub/Sub channel and continuously listens for incoming messages. It filters out self-published events, deserializes valid payload data into an event object, and then dispatches that event through the class's `send` mechanism.*


### _split_origin (method, L107-L116, parent: RedisStream)

> *Summary: Parses a byte string formatted as `<instance_id> <RS> <payload>` to separate the origin ID from the message body. It returns a tuple containing the decoded origin ID (or `None`) and the remaining payload bytes.*


### send (method, L118-L134, parent: RedisStream)

> *Summary: This method persists an incoming event to Redis storage and immediately dispatches it to local subscribers. It then publishes a serialized, origin-tagged version of the event to a Redis channel for remote listeners to consume.*


### close (method, L136-L143, parent: RedisStream)

> *Summary: This method gracefully shuts down the stream by canceling any active listener task and closing all associated Redis connections (publisher, subscriber) and storage resources. It ensures a clean termination of background operations.*

