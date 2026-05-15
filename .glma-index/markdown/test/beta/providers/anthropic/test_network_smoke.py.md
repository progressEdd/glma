# test/beta/providers/anthropic/test_network_smoke.py

4 function(s): anthropic_config, _wait_for_text_count, test_peers_then_delegate_consults_a_specialist, test_5way_discussion_round_robin_via_say_tool.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| anthropic_config | function |  |
| _wait_for_text_count | function |  |
| test_peers_then_delegate_consults_a_specialist | function |  |
| test_5way_discussion_round_robin_via_say_tool | function |  |

## Chunks

### anthropic_config (function, L49-L53)

> *Summary: This function retrieves the `ANTHROPIC_API_KEY` environment variable; if missing, it skips testing. Otherwise, it constructs and returns an `AnthropicConfig` object configured for the "claude-haiku-4-5" model with a temperature of 0.*


### _wait_for_text_count (function, L56-L71)

> *Summary: This asynchronous function polls a specified channel's write-ahead log until the number of `EV_TEXT` events meets or exceeds an expected count, returning that final count. It uses a timeout mechanism to prevent indefinite waiting and sleeps briefly between checks.*


### test_peers_then_delegate_consults_a_specialist (function, L76-L127)

> *Summary: This test verifies an end-to-end workflow where a coordinator agent discovers and consults a specialist agent on a network using Anthropic LLMs. It sets up two agents, registers them with specific roles (coordinator and math expert), and asserts that the coordinator successfully retrieves the correct answer from the specialist.*


### test_5way_discussion_round_robin_via_say_tool (function, L132-L194)

> *Summary: Tests a five-agent discussion simulation where agents take turns speaking via a `say` tool using Anthropic LLMs. It initializes the system, starts a round-robin channel with one agent seeding the conversation, and then asserts that exactly five text messages are exchanged in the correct sequential order, with each message containing substantive content.*

