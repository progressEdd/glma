# autogen/tools/experimental/messageplatform/discord/discord.py

2 class(es): DiscordSendTool, DiscordRetrieveTool. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DiscordSendTool | class |  |
| DiscordRetrieveTool | class |  |

## Chunks

### DiscordSendTool (class, L25-L116)

> *Summary: This tool sends a specified string message to a designated Discord channel within a particular guild. It requires the bot token, channel name, and guild name as inputs, and returns a success or failure status indicating if the message was sent (potentially chunked for length limits).*


### __init__ (method, L28-L116, parent: DiscordSendTool)

> *Summary: Initializes a tool capable of sending messages to a specific Discord channel within a guild. It accepts the bot token, channel name, and guild name as inputs, asynchronously connecting to Discord to send the provided message content and returning a success or failure status string.*


### DiscordRetrieveTool (class, L121-L285)

> *Summary: This tool retrieves messages from a specified Discord channel within a guild using a provided bot token. It accepts optional inputs for a starting date (ISO format or snowflake ID) and a maximum message count to control the retrieval scope, returning a list of message dictionaries upon successful execution.*


### __init__ (method, L124-L259, parent: DiscordRetrieveTool)

> *Summary: Initializes a tool capable of fetching message history from a specified Discord channel. It accepts the bot token, guild name, and channel name as inputs, optionally filtering results by a starting date/ID or maximum count, and returns a list of structured message dictionaries upon successful retrieval.*


### _is_snowflake (method, L262-L269, parent: DiscordRetrieveTool)

> *Summary: Validates if an input string conforms to the structure of a Discord snowflake ID by checking if it consists only of digits and has a length between 17 and 20 characters. Returns `True` if the format is correct, otherwise `False`.*


### _snowflake_to_iso (method, L272-L285, parent: DiscordRetrieveTool)

> *Summary: Converts a Discord snowflake ID string into an ISO 8601 formatted timestamp string. It validates the input as a snowflake and uses a specific epoch offset to calculate the corresponding UTC datetime object before formatting it.*

