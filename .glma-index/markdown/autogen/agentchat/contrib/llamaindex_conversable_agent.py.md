# autogen/agentchat/contrib/llamaindex_conversable_agent.py

1 class(es): LLamaIndexConversableAgent. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LLamaIndexConversableAgent | class |  |

## Chunks

### LLamaIndexConversableAgent (class, L30-L117)

> *Summary: This class wraps an external LlamaIndex agent to function as an Autogen conversational agent. It intercepts the standard reply generation methods, routing incoming messages and chat history through the provided `llama_index_agent` for responses, both synchronously and asynchronously.*


### __init__ (method, L31-L64, parent: LLamaIndexConversableAgent)

> *Summary: Initializes an agent wrapper that integrates a provided LlamaIndex `AgentRunner`. It enforces the presence of both a name and a description, then overrides the standard OpenAI reply generation methods to utilize LlamaIndex functionality.*


### _generate_oai_reply (method, L66-L79, parent: LLamaIndexConversableAgent)

> *Summary: This method generates a response by passing the user's message and conversation history to an underlying LlamaIndex agent. It returns a boolean indicating success along with the resulting reply content from the AI model.*


### _a_generate_oai_reply (method, L81-L96, parent: LLamaIndexConversableAgent)

> *Summary: This asynchronous method generates an OpenAI-style reply by first extracting the current user message and conversation history from provided inputs. It then passes these to an underlying LlamaIndex agent for processing and returns a boolean success flag along with the resulting response content.*


### _extract_message_and_history (method, L98-L117, parent: LLamaIndexConversableAgent)

> *Summary: This method retrieves the latest user message content and a structured list of preceding conversation turns from an input message list or stored agent messages. It filters the history to include only "user" and "assistant" roles before returning the current message text and the formatted chat history.*

