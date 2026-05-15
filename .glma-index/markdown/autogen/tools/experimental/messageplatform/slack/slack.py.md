# autogen/tools/experimental/messageplatform/slack/slack.py

3 class(es): SlackSendTool, SlackRetrieveTool, SlackRetrieveRepliesTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SlackSendTool | class |  |
| SlackRetrieveTool | class |  |
| SlackRetrieveRepliesTool | class |  |

## Chunks

### SlackSendTool (class, L25-L86)

> *Summary: This tool sends messages to a specified Slack channel using a provided bot token. It accepts a string message as input and returns a success or failure status indicating if the message was sent, handling potential API errors and chunking long messages automatically.*


### __init__ (method, L28-L86, parent: SlackSendTool)

> *Summary: Initializes the tool by setting up an asynchronous function that sends messages to Slack. This function accepts a message string and uses provided bot tokens and channel IDs to post the content, handling message chunking for long inputs.*


### SlackRetrieveTool (class, L91-L190)

> *Summary: This tool retrieves message history from a specified Slack channel using a bot token. It accepts optional inputs for a starting date (ISO format or message ID) and a maximum message count to limit the returned data. The output is a dictionary containing the total message count, the list of messages, and the start time reference.*


### __init__ (method, L94-L190, parent: SlackRetrieveTool)

> *Summary: Initializes a tool capable of fetching messages from a specified Slack channel using a bot token. It accepts optional inputs for a starting date (ISO format or message ID) and a maximum count to retrieve the relevant chat history. The function returns a dictionary containing the retrieved messages, their count, and the start time reference.*


### SlackRetrieveRepliesTool (class, L195-L387)

> *Summary: This tool retrieves all responses to a given Slack message by querying both its direct thread replies and subsequent messages in the main channel. It can optionally poll for a specified minimum number of total replies within a set timeout period before returning the collected data.*


### __init__ (method, L198-L387, parent: SlackRetrieveRepliesTool)

> *Summary: Initializes a tool that asynchronously retrieves all replies for a given Slack message timestamp from both its direct thread and subsequent channel messages. It can optionally wait up to a specified timeout for a minimum number of combined replies before returning the collected data or indicating a timeout.*

