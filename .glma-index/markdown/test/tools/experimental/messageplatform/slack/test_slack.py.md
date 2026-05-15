# test/tools/experimental/messageplatform/slack/test_slack.py

3 class(es): TestSlackSendTool, TestSlackRetrieveTool, TestSlackRetrieveRepliesTool. 32 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestSlackSendTool | class |  |
| TestSlackRetrieveTool | class |  |
| TestSlackRetrieveRepliesTool | class |  |

## Chunks

### TestSlackSendTool (class, L18-L142)

> *Summary: This test suite verifies the functionality of a Slack message sending tool by mocking the underlying `slack_sdk.WebClient`. It tests various scenarios including successful single and multi-chunked message sends, as well as error handling for API failures, general exceptions, and chunking failures.*


### mock_webclient (method, L20-L33, parent: TestSlackSendTool)

> *Summary: This method sets up a mocked `WebClient` class for testing by patching both the original and cached import locations of `slack_sdk.WebClient`. The returned mock instance simulates successful API calls, specifically setting the return value for `chat_postMessage` to indicate success.*


### tool (method, L36-L37, parent: TestSlackSendTool)

> *Summary: Returns a configured instance of `SlackSendTool` using hardcoded test credentials for the bot token and channel ID. This method provides a ready-to-use tool object for testing purposes.*


### test_slack_send_tool_init (method, L39-L54, parent: TestSlackSendTool)

> *Summary: This test verifies that an initialized `SlackSendTool` correctly sets its name, description, and function signature based on predefined expectations. It asserts the tool's structure matches a specific JSON schema defining a required string parameter named "message".*


### test_successful_message_send (method, L57-L70, parent: TestSlackSendTool)

> *Summary: This test verifies that a message is correctly sent via the Slack tool by mocking the underlying web client. It asserts that `chat_postMessage` was called with the expected channel and text, and confirms the returned result contains success indicators.*


### test_long_message_chunking (method, L73-L91, parent: TestSlackSendTool)

> *Summary: This test verifies that a message exceeding the platform's maximum length is correctly split into multiple parts before sending. It asserts that the underlying API call is invoked twice for a 45,000-character input and confirms each resulting chunk respects the 40,000 character limit.*


### test_slack_api_error (method, L94-L103, parent: TestSlackSendTool)

> *Summary: This test verifies the error handling when the Slack API returns a specific failure. It mocks the underlying web client to raise a `SlackApiError` during message posting and asserts that the tool correctly reports the failure, including the `"channel_not_found"` error code.*


### test_general_exception (method, L106-L113, parent: TestSlackSendTool)

> *Summary: This test verifies that the Slack sending tool correctly handles unexpected exceptions during API calls. It mocks a web client to raise an `Exception` when `chat_postMessage` is called, asserting that the returned result contains both a failure message and the original exception text.*


### test_failed_message_response (method, L116-L123, parent: TestSlackSendTool)

> *Summary: This test verifies the error handling when Slack's `chat_postMessage` returns a failure response. It asserts that the tool correctly reports a "Message send failed" status along with the specific `"invalid_auth"` error received from the mock client.*


### test_chunked_message_failure (method, L126-L142, parent: TestSlackSendTool)

> *Summary: This test verifies the tool's behavior when sending a large message that requires chunking, simulating a failure during the second transmission attempt. It asserts that the underlying API call was made twice and that the returned result correctly indicates the failure reason ("rate\_limited").*


### TestSlackRetrieveTool (class, L146-L338)

> *Summary: This test suite verifies the functionality of a Slack message retrieval tool by mocking the `slack_sdk.WebClient`. It tests various scenarios, including successful retrieval with and without filters (date/ID), pagination handling, and robust error management for invalid inputs or API failures.*


### mock_webclient (method, L148-L166, parent: TestSlackRetrieveTool)

> *Summary: This method sets up a mocked `WebClient` class for testing by patching it in two locations using `pytest.MonkeyPatch`. The mock instance is configured to return predefined conversation history data when its methods are called.*


### tool (method, L169-L170, parent: TestSlackRetrieveTool)

> *Summary: Returns a configured instance of `SlackRetrieveTool` using hardcoded test credentials for the bot token and channel ID. This method provides a ready-to-use tool object for testing purposes.*


### test_slack_retrieve_tool_init (method, L172-L216, parent: TestSlackRetrieveTool)

> *Summary: This test verifies the initialization and structure of a Slack message retrieval tool by instantiating it with a bot token and channel ID. It asserts that the resulting object has the correct name, description, callable function, and matches a predefined JSON schema for its parameters (`messages_since` and `maximum_messages`).*


### test_successful_message_retrieval (method, L219-L230, parent: TestSlackRetrieveTool)

> *Summary: This test verifies that the tool successfully retrieves messages from Slack when no filters are applied. It asserts that the underlying API call was made correctly and that the returned data structure contains exactly one message with the expected text content.*


### test_message_retrieval_with_date (method, L233-L245, parent: TestSlackRetrieveTool)

> *Summary: This test verifies that the tool correctly retrieves messages using an ISO date filter as input. It asserts that the underlying API call is made with a valid, converted "oldest" timestamp parameter derived from the provided date string.*


### test_message_retrieval_with_message_id (method, L248-L257, parent: TestSlackRetrieveTool)

> *Summary: This test verifies that a Slack retrieval tool correctly queries message history using a specific timestamp filter. It asserts that the underlying web client method is called with the correct channel ID and the provided `messages_since` value as the oldest marker.*


### test_message_retrieval_with_pagination (method, L260-L285, parent: TestSlackRetrieveTool)

> *Summary: This test verifies that a tool correctly retrieves all messages from a Slack channel when the API response requires pagination. It mocks the underlying web client to return two pages of data, asserting that the tool calls the history endpoint twice and aggregates both message sets into the final output.*


### test_message_retrieval_with_maximum (method, L288-L295, parent: TestSlackRetrieveTool)

> *Summary: This test verifies that the `SlackRetrieveTool` correctly passes a specified maximum message count to the underlying Slack API call. It asserts that the mock web client's conversation history method is called exactly once with the correct channel ID and the provided limit of 500.*


### test_invalid_date_format (method, L298-L303, parent: TestSlackRetrieveTool)

> *Summary: When provided with an invalid date string for the `messages_since` parameter, this test asserts that the tool returns a specific error message and does not make any external API calls to the web client.*


### test_slack_api_error (method, L306-L316, parent: TestSlackRetrieveTool)

> *Summary: This test verifies error handling when the Slack API returns a specific failure. It mocks the underlying web client to raise a `SlackApiError` during conversation history retrieval and asserts that the tool correctly reports the "channel\_not\_found" error message.*


### test_general_exception (method, L319-L327, parent: TestSlackRetrieveTool)

> *Summary: This test verifies that the Slack retrieval tool correctly handles unexpected exceptions during API calls. It mocks a web client to raise an `Exception` and asserts that the resulting output string contains both a failure message and the specific exception text.*


### test_failed_message_response (method, L330-L338, parent: TestSlackRetrieveTool)

> *Summary: This test verifies the error handling when Slack returns a failure response, specifically simulating an `invalid_auth` error. It asserts that the tool's execution returns a message containing both the general failure notice and the specific authentication error code.*


### TestSlackRetrieveRepliesTool (class, L342-L593)

> *Summary: This test suite verifies the functionality of a Slack tool designed to retrieve replies for a specific message timestamp from Slack. It uses extensive mocking of the `WebClient` to simulate various API responses, testing successful retrieval, pagination handling, minimum reply waiting logic, and robust error management for both Slack-specific and general exceptions.*


### mock_webclient (method, L344-L371, parent: TestSlackRetrieveRepliesTool)

> *Summary: This method generates a mocked `WebClient` class and instance to simulate Slack API responses for testing purposes. It configures the mock to return predefined message history and replies when methods like `conversations_history` or `conversations_replies` are called, ensuring predictable test behavior across different import paths.*


### tool (method, L374-L375, parent: TestSlackRetrieveRepliesTool)

> *Summary: Returns a configured instance of `SlackRetrieveRepliesTool` using hardcoded test credentials for the bot token and channel ID. This method provides a ready-to-use tool object for testing purposes.*


### test_slack_retrieve_replies_tool_init (method, L377-L428, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies that an initialized `SlackRetrieveRepliesTool` correctly sets its name, description, and function schema based on predefined parameters. It asserts the tool's structure matches an expected JSON schema defining inputs like message timestamp, minimum replies, and polling intervals.*


### test_successful_message_reply_retrieval (method, L431-L447, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies that a tool successfully retrieves messages replying to a specific timestamp when no filters are applied. It asserts that the underlying Slack API call was made correctly and that the returned data structure contains one expected message with the correct text.*


### test_message_reply_retrieval_with_ts (method, L450-L462, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies that a tool correctly retrieves message replies by filtering based on a provided timestamp. It asserts that the underlying Slack API call uses the specified `oldest` parameter and confirms the returned result contains the expected parent message timestamp.*


### test_message_reply_retrieval_with_pagination (method, L465-L491, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies that the tool correctly retrieves all messages when paginated by mocking a sequence of API responses from `conversations_history`. It asserts that the final returned result contains the correct total count after iterating through multiple pages.*


### test_message_reply_retrieval_with_minimum (method, L494-L527, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies that the reply retrieval tool correctly gathers messages when a minimum reply threshold is set. It mocks Slack API responses to simulate paginated history and asserts that the returned results meet or exceed the specified `min_replies` count across different message types.*


### test_message_reply_retrieval_with_timeout (method, L530-L558, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies that a tool correctly retrieves multiple message replies from Slack, simulating pagination. It passes mock responses for two pages of history and asserts the final count reflects both retrieved messages.*


### test_slack_api_error (method, L561-L571, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies error handling when the Slack API returns a specific failure, such as `channel_not_found`. It mocks the underlying web client to raise a `SlackApiError` during history retrieval and asserts that the tool correctly captures and reports this exception.*


### test_general_exception (method, L574-L582, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies that the tool correctly handles unexpected exceptions during Slack API calls by mocking a failure in `conversations_history`. It asserts that the returned result string contains specific error messages indicating both the general failure and the underlying exception.*


### test_failed_message_response (method, L585-L593, parent: TestSlackRetrieveRepliesTool)

> *Summary: This test verifies the tool's behavior when Slack returns a failure response, specifically simulating an `invalid_auth` error. It asserts that the returned result string correctly indicates both the general failure and the specific authentication error received from the mock client.*

