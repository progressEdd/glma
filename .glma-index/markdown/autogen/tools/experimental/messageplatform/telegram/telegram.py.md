# autogen/tools/experimental/messageplatform/telegram/telegram.py

3 class(es): BaseTelegramTool, TelegramSendTool, TelegramRetrieveTool. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BaseTelegramTool | class |  |
| TelegramSendTool | class |  |
| TelegramRetrieveTool | class |  |

## Chunks

### BaseTelegramTool (class, L24-L86)

> *Summary: Provides a base structure for Telegram interaction, managing API credentials and client instantiation. It offers utility methods to convert string IDs into specific peer types and asynchronously resolves an entity from a given chat ID by attempting direct retrieval or searching through existing dialogs.*


### __init__ (method, L27-L30, parent: BaseTelegramTool)

> *Summary: Initializes the Telegram client by storing the required API ID, API hash, and a unique session name. These parameters are used to configure the connection for subsequent operations.*


### _get_client (method, L32-L34, parent: BaseTelegramTool)

> *Summary: Instantiates and returns a new `TelegramClient` object using the stored session name, API ID, and API hash. This method ensures that a fresh client connection is available for subsequent operations.*


### _get_peer_from_id (method, L37-L58, parent: BaseTelegramTool)

> *Summary: This method parses a string `chat_id` to determine the correct Telegram peer type. It converts the input string into an integer and returns either a `PeerChannel`, `PeerChat`, or `PeerUser` object based on whether the ID is positive, negative, or starts with "-100".*


### _initialize_entity (method, L60-L86, parent: BaseTelegramTool)

> *Summary: Attempts to resolve a Telegram entity using a provided `chat_id` by first trying direct retrieval via the client. If that fails, it iterates through all existing dialogs to find and return the corresponding entity object, raising an error if unsuccessful.*


### TelegramSendTool (class, L91-L156)

> *Summary: This tool sends messages to specified Telegram chats using provided API credentials and a target chat ID. It handles both single-message sending and automatically chunks long messages into sequential replies, returning a success message including the sent content or an error description upon failure.*


### __init__ (method, L94-L156, parent: TelegramSendTool)

> *Summary: Initializes the tool with Telegram credentials and a target chat ID. It exposes an asynchronous function that sends a message to Telegram, automatically chunking long messages into sequential replies if necessary, and returns a success or failure status string.*


### TelegramRetrieveTool (class, L161-L272)

> *Summary: This tool retrieves messages from a specified Telegram chat using provided API credentials. It accepts optional parameters to filter results by a starting date (ISO format or message ID), maximum count, or search term, returning a dictionary containing the retrieved messages and metadata.*


### __init__ (method, L164-L272, parent: TelegramRetrieveTool)

> *Summary: Initializes a tool capable of fetching messages from a specified Telegram chat using provided API credentials. It exposes an asynchronous function that accepts optional parameters for filtering by date (ISO format or message ID), maximum count, and search query, returning a structured list of retrieved messages or an error string.*

