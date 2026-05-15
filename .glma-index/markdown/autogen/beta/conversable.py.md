# autogen/beta/conversable.py

1 class(es): ConversableAdapter. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ConversableAdapter | class |  |

## Chunks

### ConversableAdapter (class, L14-L88)

> *Summary: This adapter wraps an underlying agent to facilitate conversational interactions by overriding reply generation methods. It manages the conversation state, using the provided agent to ask questions based on message history and updates context variables upon receiving a response.*


### __init__ (method, L15-L30, parent: ConversableAdapter)

> *Summary: Initializes a conversational agent wrapper by storing a reference to the underlying `Agent` and setting up internal state for conversation history and tools. It then overrides the standard reply generation methods to route them through custom adapter functions.*


### generate_conversable_reply (method, L32-L38, parent: ConversableAdapter)

> *Summary: This method is intended to generate a conversational response based on provided messages and an agent context. Currently, it explicitly raises an error because the implementation does not support synchronous reply generation.*


### a_generate_conversable_reply (method, L40-L74, parent: ConversableAdapter)

> *Summary: This method generates a conversational reply by sending the last message content to an underlying agent, either starting a new conversation or continuing an existing one. It updates internal and sender context variables with any returned data and returns a success flag along with the formatted response.*


### update_tool_signature (method, L76-L88, parent: ConversableAdapter)

> *Summary: Modifies the internal LLM configuration by either adding or removing a tool signature based on the provided input and flag. Subsequently, it rebuilds the list of available client tools using the updated configuration.*

