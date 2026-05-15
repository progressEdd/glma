# test/beta/providers/openai/test_network_smoke.py

4 function(s): openai_config, _wait_for_text_count, test_peers_then_delegate_consults_a_specialist, test_3way_discussion_round_robin_via_say_tool.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| openai_config | function |  |
| _wait_for_text_count | function |  |
| test_peers_then_delegate_consults_a_specialist | function |  |
| test_3way_discussion_round_robin_via_say_tool | function |  |

## Chunks

### openai_config (function, L48-L52)

> *Summary: Retrieves the `OPENAI_API_KEY` environment variable; if missing, it skips testing. Otherwise, it constructs and returns an `OpenAIConfig` object using a specific model name and zero temperature.*


### _wait_for_text_count (function, L55-L69)

> *Summary: This asynchronous function polls a specified channel's write-ahead log until the count of `EV_TEXT` events meets or exceeds an expected value, respecting a defined timeout. It returns the final observed text event count after either meeting the expectation or timing out.*


### test_peers_then_delegate_consults_a_specialist (function, L74-L123)

> *Summary: This test simulates a multi-agent interaction where one agent (Alice) first discovers another specialized agent (Bob) on the network using a `peers` action, and then delegates a specific query to Bob for an answer. It asserts that Alice successfully receives and relays the expected numerical result from Bob.*


### test_3way_discussion_round_robin_via_say_tool (function, L128-L185)

> *Summary: This test verifies a round-robin discussion among three agents using the `say` tool via an OpenAI configuration. It initializes a multi-party channel, sends an initial prompt, and asserts that exactly three turns occur in the expected sequential order, with each contribution being non-trivial.*

