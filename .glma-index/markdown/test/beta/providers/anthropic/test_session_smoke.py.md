# test/beta/providers/anthropic/test_session_smoke.py

6 function(s): anthropic_config, _agent, _wait_text_count, test_consulting_two_agents_real_llm, test_conversation_bidirectional_real_llm, test_discussion_round_robin_three_real_agents.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| anthropic_config | function |  |
| _agent | function |  |
| _wait_text_count | function |  |
| test_consulting_two_agents_real_llm | function |  |
| test_conversation_bidirectional_real_llm | function |  |
| test_discussion_round_robin_three_real_agents | function |  |

## Chunks

### anthropic_config (function, L41-L45)

> *Summary: This function retrieves the `ANTHROPIC_API_KEY` environment variable; if missing, it skips testing. Otherwise, it constructs and returns an `AnthropicConfig` object configured for the "claude-haiku-4-5" model with a temperature of 0.*


### _agent (function, L48-L49)

> *Summary: Creates and returns a new `Agent` instance using the provided name, prompt string, and configuration object. This helper function abstracts the instantiation process for testing purposes.*


### _wait_text_count (function, L52-L60)

> *Summary: This asynchronous function polls a Write-Ahead Log (WAL) for a specific channel until the count of `EV_TEXT` events meets or exceeds an expected value, raising a timeout error if the condition is not met within the specified duration. It takes a Hub object, channel ID, and the target event count as input and returns the WAL contents upon success.*


### test_consulting_two_agents_real_llm (function, L65-L127)

> *Summary: This test verifies a two-agent consulting workflow using Anthropic LLMs, where one agent asks a math question and the other responds with only the numeric answer. It asserts that the interaction correctly triggers an auto-closing mechanism, posts the reply via `Channel.send`, and leaves corresponding creation and closure records in the audit log.*


### test_conversation_bidirectional_real_llm (function, L132-L179)

> *Summary: This test simulates a bidirectional conversation between two agents, Alice and Bob, using an Anthropic LLM configuration. It initiates a chat exchange, waits until at least three text messages are exchanged in alternating turns, asserts the sequence of senders is correct, and then cleanly closes the communication channel and associated resources.*


### test_discussion_round_robin_three_real_agents (function, L184-L227)

> *Summary: This test verifies a three-way discussion using round-robin scheduling among agents configured with Anthropic AI. It initializes a communication hub, registers three distinct agents (Alice, Bob, Carol), starts a discussion channel targeting all participants, and asserts that the resulting text messages follow the expected speaker rotation: Alice $\rightarrow$ Bob $\rightarrow$ Carol $\rightarrow$ Alice.*

