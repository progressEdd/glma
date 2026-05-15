# autogen/agents/experimental/slack/slack.py

1 class(es): SlackAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SlackAgent | class |  |

## Chunks

### SlackAgent (class, L15-L73)

> *Summary: This agent facilitates interaction with Slack by wrapping communication tools for sending and retrieving messages. It requires a bot token and channel ID upon initialization, exposing methods to the LLM via registered tools.*


### __init__ (method, L24-L73, parent: SlackAgent)

> *Summary: Initializes an agent configured to interact with Slack using provided bot tokens and channel IDs. It sets up specialized tools for sending, retrieving messages, and fetching replies, optionally augmenting the system message with specific formatting guidelines before registering these tools with the LLM.*

