# autogen/agentchat/contrib/society_of_mind_agent.py

1 class(es): SocietyOfMindAgent. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SocietyOfMindAgent | class |  |

## Chunks

### SocietyOfMindAgent (class, L25-L213)

> *Summary: This deprecated agent orchestrates a group chat internally to simulate an "inner monologue." It takes a `GroupChatManager` and an optional `response_preparer` function/prompt as input. Upon conversation completion, it uses the `response_preparer` on the entire message history to extract or generate a final reply for external use.*


### __init__ (method, L46-L101, parent: SocietyOfMindAgent)

> *Summary: Initializes a deprecated agent by accepting configuration for its name, chat management, LLM settings, and response handling logic. It sets up internal reply mechanisms to handle various conversational actions like generating monologues or executing code based on the provided inputs.*


### _llm_response_preparer (method, L103-L149, parent: SocietyOfMindAgent)

> *Summary: Constructs a structured message list by prepending a system prompt and appending the user-modified conversation transcript to an initial system instruction. It then sends this complete context to an LLM client and returns the resulting text or dictionary representation of the model's output.*


### chat_manager (method, L152-L154, parent: SocietyOfMindAgent)

> *Summary: Retrieves and returns the internal `GroupChatManager` instance associated with the agent. This method provides access to the established group communication context.*


### update_chat_manager (method, L156-L171, parent: SocietyOfMindAgent)

> *Summary: Sets the agent's internal chat manager reference to the provided `GroupChatManager`. If a manager is supplied, it iterates through its reply functions to find and set the associated `GroupChat` object.*


### generate_inner_monologue_reply (method, L173-L213, parent: SocietyOfMindAgent)

> *Summary: This method simulates an agent's internal thought process by running a group chat simulation using provided messages and configuration. It resets the chat manager, populates agents with the external conversation history, initiates a new chat based on the latest message, and returns success along with a formatted response derived from the simulated group chat output.*

