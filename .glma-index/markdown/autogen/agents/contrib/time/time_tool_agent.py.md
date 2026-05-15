# autogen/agents/contrib/time/time_tool_agent.py

1 class(es): TimeToolAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TimeToolAgent | class |  |

## Chunks

### TimeToolAgent (class, L15-L52)

> *Summary: This agent acts as a calendar assistant that utilizes a `TimeTool` to fetch and return the current date and time. It accepts a custom date/time format during initialization and automatically registers the tool for LLM invocation, adhering to a specific output message structure.*


### __init__ (method, L28-L52, parent: TimeToolAgent)

> *Summary: This constructor initializes an agent designed to interact with a time utility. It accepts a specific date/time format string and uses it to configure an internal `TimeTool`, then registers this tool for use by the underlying LLM.*

