# autogen/agents/experimental/websurfer/websurfer.py

1 class(es): WebSurferAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WebSurferAgent | class |  |

## Chunks

### WebSurferAgent (class, L25-L69)

> *Summary: This agent inherits from `ConversableAgent` and is designed to interact with the web by selecting a specific search or browsing tool based on configuration. It initializes itself by setting up the chosen tool (e.g., `BrowserUseTool`, `TavilySearchTool`) using provided LLM configurations and keyword arguments, then registers this tool for use by its underlying LLM.*


### __init__ (method, L28-L69, parent: WebSurferAgent)

> *Summary: This constructor initializes a web-browsing agent by selecting and instantiating a specific search or browsing tool based on the `web_tool` argument. It configures this chosen tool using provided LLM settings and keyword arguments, then registers it with the parent agent for use.*

