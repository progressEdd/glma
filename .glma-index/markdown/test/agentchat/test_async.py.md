# test/agentchat/test_async.py

5 function(s): get_market_news, _test_async_groupchat, test_async_groupchat, _test_stream, test_stream.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_market_news | function |  |
| _test_async_groupchat | function |  |
| test_async_groupchat | function |  |
| _test_stream | function |  |
| test_stream | function |  |

## Chunks

### get_market_news (function, L19-L55)

> *Summary: Retrieves a slice of market news articles based on start and end indices. It processes the input range to format each article's title, summary, and sentiment score into a single newline-separated string output.*


### _test_async_groupchat (function, L58-L87)

> *Summary: This test sets up an asynchronous group chat involving a `UserProxyAgent` and an `AssistantAgent`. It initiates a conversation with the user proxy, allowing the agents to interact within a defined round limit until the assistant replies "TERMINATE".*


### test_async_groupchat (function, L93-L96)

> *Summary: This asynchronous test function executes a core group chat simulation by calling an internal helper method with provided credentials. It verifies the functionality of asynchronous group communication within the system.*


### _test_stream (function, L99-L162)

> *Summary: Simulates a streaming data feed by running an asynchronous task that periodically generates market news. It then initiates a chat session between an AssistantAgent and UserProxyAgent, registering a custom reply handler to ingest the streamed news data into the conversation flow for summarization. The function ultimately prints the final summary and cost of the completed chat exchange.*


### test_stream (function, L168-L171)

> *Summary: This asynchronous test function executes a stream test using provided credentials. It calls an internal helper function to perform the streaming operation and asserts its behavior.*

