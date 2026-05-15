# autogen/agentchat/contrib/capabilities/transform_messages.py

1 class(es): TransformMessages. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TransformMessages | class |  |

## Chunks

### TransformMessages (class, L17-L93)

> *Summary: This capability applies a sequence of user-defined message transformations to an agent's incoming messages before response generation. It accepts a list of transformation objects and hooks into the agent's processing pipeline to execute them in order, returning the modified message history.*


### __init__ (method, L52-L58, parent: TransformMessages)

> *Summary: Initializes the transformer with a list of `MessageTransform` objects and a boolean flag controlling logging verbosity. It stores these configurations internally for later use in message processing.*


### add_to_agent (method, L60-L68, parent: TransformMessages)

> *Summary: Registers a message transformation capability onto a given agent by hooking into the `process_all_messages_before_reply` lifecycle event. This ensures that all incoming messages are automatically transformed before the agent generates a response.*


### _transform_messages (method, L70-L93, parent: TransformMessages)

> *Summary: This method processes a list of chat messages by applying a sequence of registered transformations to them. It preserves the initial system message if present and returns the fully transformed list of messages.*

