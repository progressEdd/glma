# autogen/agents/experimental/discord/discord.py

1 class(es): DiscordAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DiscordAgent | class |  |

## Chunks

### DiscordAgent (class, L15-L66)

> *Summary: This agent acts as a conversational interface for Discord by wrapping two specialized tools: one for sending messages and another for retrieving them. It requires a bot token, channel name, and guild name upon initialization to operate within the specified Discord environment.*


### __init__ (method, L24-L66, parent: DiscordAgent)

> *Summary: This constructor sets up a Discord agent by initializing communication tools for sending and retrieving messages via Discord using provided bot credentials, channel, and guild names. It configures the agent's system message with optional formatting guidelines before registering these I/O tools with the parent conversational framework.*

