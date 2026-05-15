# autogen/agentchat/contrib/web_surfer.py

1 class(es): WebSurferAgent. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WebSurferAgent | class |  |

## Chunks

### WebSurferAgent (class, L30-L322)

> *Summary: This deprecated class implements an AI agent capable of browsing the web by integrating a `SimpleTextBrowser` and exposing several functions like searching (`informational_web_search`, `navigational_web_search`), visiting URLs, scrolling, and summarizing page content. It manages internal communication between an assistant and a user proxy to execute these browser-based tasks based on input messages.*


### __init__ (method, L45-L110, parent: WebSurferAgent)

> *Summary: Initializes a web-surfing agent by accepting configuration for its name, system prompts, LLM settings, and browser behavior. It sets up internal assistant and user proxy agents, configures function registration based on LLM settings, and registers specific reply handlers for web surfing, code execution, and termination checks.*


### _create_summarizer_client (method, L112-L141, parent: WebSurferAgent)

> *Summary: This method configures the summarizer's LLM settings by prioritizing a provided configuration, falling back to copying and potentially refining the main LLM configuration if none is given. It then initializes an `OpenAIWrapper` client using these finalized settings, or sets it to `None` if LLMs are disabled.*


### _register_functions (method, L143-L282, parent: WebSurferAgent)

> *Summary: This method registers several utility functions with the agent's proxies for web interaction and AI-driven content processing. It exposes capabilities like informational/navigational searching, direct page visiting, scrolling, and summarizing page content based on a query or URL.*


### generate_surfer_reply (method, L284-L322, parent: WebSurferAgent)

> *Summary: This method generates a response by simulating an interaction between a user proxy and an assistant agent, using provided messages or cached history as context. It initializes the agents, injects the current browser state into the conversation, sends the final message, and then returns the content of the generated reply from either the initial agent response or the subsequent proxy generation.*

