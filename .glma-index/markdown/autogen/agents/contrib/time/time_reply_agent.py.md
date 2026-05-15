# autogen/agents/contrib/time/time_reply_agent.py

1 class(es): TimeReplyAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TimeReplyAgent | class |  |

## Chunks

### TimeReplyAgent (class, L14-L74)

> *Summary: This class creates an agent designed solely to return the current date and time upon request. It accepts a custom format string and output prefix during initialization, then registers a reply function that uses Python's `datetime` module to generate and return the formatted timestamp.*


### __init__ (method, L24-L74, parent: TimeReplyAgent)

> *Summary: Initializes an agent configured to respond with the current date and time. It accepts a custom format string and output prefix, then registers a reply function that uses `datetime.now()` formatted according to the provided settings.*

