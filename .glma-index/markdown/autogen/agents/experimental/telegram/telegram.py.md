# autogen/agents/experimental/telegram/telegram.py

1 class(es): TelegramAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TelegramAgent | class |  |

## Chunks

### TelegramAgent (class, L15-L76)

> *Summary: This agent facilitates communication via Telegram by wrapping a `ConversableAgent` with specific tooling. It requires API credentials and a target chat ID to initialize, providing methods to both send messages to and retrieve messages from the specified Telegram contact.*


### __init__ (method, L24-L76, parent: TelegramAgent)

> *Summary: Initializes an agent configured to interact with Telegram using provided API credentials and a target chat ID. It sets up specialized send and retrieve tools, optionally augmenting the system message with specific HTML formatting guidelines for Telegram messages before registering these tools with the LLM.*

