# autogen/agentchat/contrib/multimodal_conversable_agent.py

1 class(es): MultimodalConversableAgent. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MultimodalConversableAgent | class |  |

## Chunks

### MultimodalConversableAgent (class, L22-L149)

> *Summary: This agent extends a base conversational agent to handle multimodal inputs by overriding message handling and reply generation. It processes string messages, specifically formatting them using `gpt4v_formatter` to support image content before sending requests to the underlying OpenAI client for responses.*


### __init__ (method, L27-L62, parent: MultimodalConversableAgent)

> *Summary: Initializes a multimodal agent by inheriting from `ConversableAgent` and setting up its core parameters like name and system message. It then overrides the OpenAI reply generation methods to enable multimodal capabilities for this specific agent instance.*


### update_system_message (method, L64-L71, parent: MultimodalConversableAgent)

> *Summary: This method updates the agent's system message configuration by taking a string or dictionary input and setting it in the internal OpenAI wrapper structure. It specifically overwrites the content and ensures the role is set to "system".*


### _append_oai_message (method, L73-L95, parent: MultimodalConversableAgent)

> *Summary: Processes incoming messages by converting them to a dictionary format and specifically handles `<img>` tags within string inputs using `gpt4v_formatter` before appending the result to an OpenAI-style conversation. It accepts a message (dict or str), a conversation agent, a role, and an optional name, returning a boolean indicating success.*


### _message_to_dict (method, L98-L123, parent: MultimodalConversableAgent)

> *Summary: Transforms various input types—string, list, or dictionary—into a standardized dictionary format suitable for GPT-4V prompting. It specifically formats string content using `gpt4v_formatter` and validates the structure of incoming dictionaries.*


### generate_oai_reply (method, L125-L149, parent: MultimodalConversableAgent)

> *Summary: This method constructs and sends a request to an OpenAI client using provided messages (or stored context) to generate a reply. It formats the input messages, including any images encoded in base64, then extracts the text or structured object from the API response before returning it along with a success flag.*

