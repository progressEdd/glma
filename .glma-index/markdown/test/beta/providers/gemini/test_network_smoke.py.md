# test/beta/providers/gemini/test_network_smoke.py

4 function(s): gemini_config, _wait_for_text_count, test_peers_then_delegate_consults_a_specialist, test_3way_discussion_round_robin_via_say_tool.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| gemini_config | function |  |
| _wait_for_text_count | function |  |
| test_peers_then_delegate_consults_a_specialist | function |  |
| test_3way_discussion_round_robin_via_say_tool | function |  |

## Chunks

### gemini_config (function, L48-L52)

> *Summary: Retrieves the necessary configuration for Gemini API interaction by checking for an environment variable. It returns a `GeminiConfig` object containing the model name, the provided API key, and a fixed temperature of zero if the key is present.*


### _wait_for_text_count (function, L55-L69)

> *Summary: This asynchronous function polls a channel's write-ahead log until the number of `EV_TEXT` events meets or exceeds an expected count, respecting a specified timeout. It returns the final count of text events found in the log after waiting or timing out.*


### test_peers_then_delegate_consults_a_specialist (function, L74-L123)

> *Summary: This test verifies a multi-agent workflow where an agent ("alice") first discovers a specialist peer ("bob") using a `peers` action, and then delegates the actual query to that discovered specialist via a `delegate` call. It asserts that the final response from alice contains the expected numerical result (204).*


### test_3way_discussion_round_robin_via_say_tool (function, L128-L181)

> *Summary: This test sets up three distinct AI agents to engage in a structured discussion using a round-robin mechanism via the `say` tool. It verifies that all participants contribute exactly once, and critically, asserts that the sequence of speakers strictly follows the predefined rotation order.*

