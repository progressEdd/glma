# test/agents/experimental/messageplatform/telegram/test_telegram.py

1 class(es): TestTelegramAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTelegramAgent | class |  |

## Chunks

### TestTelegramAgent (class, L12-L85)

> *Summary: This test verifies the initialization of a Telegram agent, ensuring it correctly configures its available tools (`telegram_send` and `telegram_retrieve`) and sets a specific system prompt detailing formatting guidelines for Telegram communication. It asserts that the agent's LLM configuration includes these defined functions.*


### test_init (method, L13-L85, parent: TestTelegramAgent)

> *Summary: This test verifies the initialization of a `TelegramAgent` by asserting its internal state. It confirms that the agent possesses specific tools (`telegram_send`, `telegram_retrieve`), correctly incorporates LLM configuration, and is initialized with a predefined system message detailing Telegram formatting rules.*

