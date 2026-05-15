# test/tools/experimental/messageplatform/telegram/test_telegram.py

2 class(es): TestTelegramSendTool, TestTelegramRetrieveTool. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTelegramSendTool | class |  |
| TestTelegramRetrieveTool | class |  |

## Chunks

### TestTelegramSendTool (class, L20-L215)

> *Summary: This test suite verifies the `TelegramSendTool` by mocking the underlying Telegram API client. It tests various scenarios including successful single and multi-chunked message sending, as well as error handling for missing entities, general exceptions during sending, and initial client connection failures.*


### mock_telegram_client (method, L22-L50, parent: TestTelegramSendTool)

> *Summary: This function sets up a comprehensive mock for `TelegramClient` by patching the actual class within the module under test. It configures the mock instance to simulate successful context management and provides predefined return values for methods like `get_entity` and `send_message`, allowing tests to control Telegram interactions.*


### tool (method, L53-L55, parent: TestTelegramSendTool)

> *Summary: Instantiates and returns a `TelegramSendTool` object, pre-configured with hardcoded test credentials for API ID, hash, and a specific chat ID. This method is designed solely to provide a mock or testing instance of the sending tool.*


### test_telegram_send_tool_init (method, L57-L75, parent: TestTelegramSendTool)

> *Summary: This test verifies that an initialized `TelegramSendTool` correctly sets its name, description, and function schema based on provided API credentials and chat ID. It asserts the tool's structure matches a predefined JSON schema for sending messages.*


### test_successful_message_send (method, L78-L101, parent: TestTelegramSendTool)

> *Summary: This test verifies that sending a message via the `TelegramSendTool` executes correctly. It asserts that the underlying mock client is used for entity retrieval and successfully calls `send_message` with the expected content, confirming the returned result contains success indicators and the sent message ID.*


### test_long_message_chunking (method, L104-L150, parent: TestTelegramSendTool)

> *Summary: This test verifies that a tool correctly splits an excessively long input message into multiple chunks before sending it via the Telegram client. It asserts that the client's `send_message` method is called exactly three times, each with a payload under the 4096-character limit, and that subsequent calls correctly reference the previous chunk's ID as a reply.*


### test_entity_not_found (method, L153-L175, parent: TestTelegramSendTool)

> *Summary: This test verifies the tool's behavior when Telegram fails to retrieve a specified chat or channel entity by mocking `get_entity` to raise an error. It asserts that no message is sent and confirms the returned result contains specific failure messages indicating initialization issues.*


### test_general_exception (method, L178-L195, parent: TestTelegramSendTool)

> *Summary: This test verifies that the tool correctly handles unexpected exceptions during message sending by mocking the Telegram client to raise an `Exception`. It asserts that the tool catches this error, reports a specific failure message containing the original exception text, and still attempts necessary setup/teardown operations.*


### test_client_start_failure (method, L198-L215, parent: TestTelegramSendTool)

> *Summary: This test verifies that the tool correctly handles an exception during Telegram client initialization by mocking `__aenter__` to raise an error. It asserts that the resulting output contains specific failure messages and confirms that no message sending operation was attempted.*


### TestTelegramRetrieveTool (class, L219-L347)

> *Summary: This test suite verifies the functionality of a Telegram message retrieval tool by mocking the underlying `TelegramClient`. It ensures correct initialization, validates the function schema against expected parameters (like search and limits), and confirms that the tool correctly passes input arguments to the mocked client methods during asynchronous calls.*


### mock_telegram_client (method, L221-L245, parent: TestTelegramRetrieveTool)

> *Summary: This function sets up a comprehensive mock for `TelegramClient` by replacing the actual class in the module's namespace using `monkeypatch`. It returns an asynchronous mock instance configured with mocked methods like `get_entity`, `iter_dialogs`, and `iter_messages` to simulate Telegram API interactions.*


### tool (method, L248-L250, parent: TestTelegramRetrieveTool)

> *Summary: Instantiates and returns a `TelegramRetrieveTool` object, pre-configured with hardcoded test credentials (`api_id`, `api_hash`) and a specific `chat_id`. This method is designed solely for setting up testing environments.*


### test_telegram_retrieve_tool_init (method, L252-L287, parent: TestTelegramRetrieveTool)

> *Summary: This test verifies that an initialized `TelegramRetrieveTool` correctly sets its name, description, and function schema based on provided API credentials. It asserts the tool's structure matches a predefined JSON schema defining parameters for message retrieval by date/ID, maximum count, or search term.*


### test_message_retrieval_with_search (method, L290-L318, parent: TestTelegramRetrieveTool)

> *Summary: This test verifies that a retrieval tool correctly queries messages using a search term against a mocked Telegram client. It asserts that the provided `search` parameter is passed to the underlying message iteration method and confirms an attempt was made to fetch entity information.*


### test_message_retrieval_with_limit (method, L321-L347, parent: TestTelegramRetrieveTool)

> *Summary: This test verifies that a message retrieval tool correctly passes the `maximum_messages` limit when fetching messages from a mocked Telegram client. It asserts that the underlying iteration method is called with the specified limit parameter.*

