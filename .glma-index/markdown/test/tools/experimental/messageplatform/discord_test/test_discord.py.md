# test/tools/experimental/messageplatform/discord_test/test_discord.py

2 class(es): TestDiscordSendTool, TestDiscordRetrieveTool. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestDiscordSendTool | class |  |
| TestDiscordRetrieveTool | class |  |

## Chunks

### TestDiscordSendTool (class, L15-L264)

> *Summary: This test suite verifies the `DiscordSendTool` by mocking the Discord client to isolate its logic. It tests successful message sending, automatic chunking for long messages, and error handling for missing guilds or channels, ensuring proper setup and teardown of the mocked client.*


### mock_discord_client (method, L17-L49, parent: TestDiscordSendTool)

> *Summary: This function generates a fully mocked Discord client instance, configured to immediately trigger the `on_ready` event upon calling its `start` method. It then patches both primary and internal import paths for the actual `discord.Client` class to return this controlled mock object.*


### tool (method, L52-L54, parent: TestDiscordSendTool)

> *Summary: This method instantiates and returns a `DiscordSendTool` object, pre-configured with specific test credentials like a mock bot token, guild name, and channel name. It serves to provide a ready-to-use tool instance for testing purposes.*


### test_discord_send_tool_init (method, L56-L75, parent: TestDiscordSendTool)

> *Summary: Verifies that an instance of `DiscordSendTool`, initialized with a token, guild name, and channel name, correctly sets its metadata (name, description) and possesses the expected JSON schema for its input parameter (`message`). This test confirms the tool is properly configured before execution.*


### test_successful_message_send (method, L78-L116, parent: TestDiscordSendTool)

> *Summary: This test verifies that a message is successfully sent via Discord. It mocks the necessary client, guild, and channel objects to ensure the tool's `func` method correctly calls the send function with the provided message and returns a success confirmation containing the message ID.*


### test_long_message_chunking (method, L119-L167, parent: TestDiscordSendTool)

> *Summary: This test verifies that a `DiscordSendTool` correctly splits an excessively long input message into multiple chunks before sending it via the mocked Discord client. It asserts that the total number of calls matches the expected chunk count, each individual chunk respects the maximum length limit, and all sent chunks reconstruct the original message perfectly.*


### test_guild_not_found (method, L170-L196, parent: TestDiscordSendTool)

> *Summary: This test verifies the tool's behavior when a specified guild does not exist by mocking an empty guilds list for the Discord client. It asserts that the function correctly returns an error indicating the missing guild and confirms no message sending attempts were made.*


### test_channel_not_found (method, L199-L233, parent: TestDiscordSendTool)

> *Summary: This test verifies that the tool correctly handles a scenario where the specified channel does not exist within the guild provided by mocking Discord client interactions. It asserts that an appropriate "could not find channel" error is returned, and crucially, confirms that no message sending attempt was made to any mock channels.*


### test_client_start_failure (method, L236-L264, parent: TestDiscordSendTool)

> *Summary: This test verifies that the tool correctly handles a failure during Discord client initialization by asserting that an expected exception is raised with a specific formatted message. It confirms that the client's `start` method was called, but its `close` method was never invoked when startup fails.*


### TestDiscordRetrieveTool (class, L268-L476)

> *Summary: This test suite verifies the `DiscordRetrieveTool` by mocking the Discord client to simulate various operational scenarios. It confirms correct initialization, successful message retrieval from a mocked channel history, and proper error handling when the specified guild or channel cannot be found.*


### mock_discord_client (method, L270-L302, parent: TestDiscordRetrieveTool)

> *Summary: This function generates a fully mocked Discord client instance, configured to immediately trigger the `on_ready` event upon calling its `start()` method. It then patches both primary and internal import paths for the actual Discord Client class to ensure tests use this controlled mock object.*


### tool (method, L305-L307, parent: TestDiscordRetrieveTool)

> *Summary: Instantiates and returns a `DiscordRetrieveTool` object, pre-configured with hardcoded test credentials for the bot token, guild name, and channel name. This method is used specifically to create an instance of the tool for testing purposes.*


### test_discord_retrieve_tool_init (method, L309-L341, parent: TestDiscordRetrieveTool)

> *Summary: This test verifies the initialization and structure of a Discord message retrieval tool. It asserts that the instantiated tool has the correct name, description, callable function, and matches a predefined JSON schema detailing its input parameters (`messages_since` and `maximum_messages`).*


### test_successful_message_retrieval (method, L344-L424, parent: TestDiscordRetrieveTool)

> *Summary: This test verifies that a tool correctly retrieves Discord messages by mocking the client's history response. It sets up mock message objects and asserts that the resulting list contains the expected IDs, content, author names, and timestamps from the mocked data.*


### test_guild_not_found (method, L427-L446, parent: TestDiscordRetrieveTool)

> *Summary: This test verifies the tool's behavior when a specified guild does not exist by mocking an empty list of guilds. It asserts that the function returns a list containing a specific error message indicating the missing guild name, while also confirming the Discord client lifecycle methods were called correctly.*


### test_channel_not_found (method, L449-L476, parent: TestDiscordRetrieveTool)

> *Summary: This test verifies the tool's behavior when a requested Discord channel does not exist within a specified guild. It mocks the Discord client and guild structure to ensure the function correctly returns an error message indicating the missing channel name.*

