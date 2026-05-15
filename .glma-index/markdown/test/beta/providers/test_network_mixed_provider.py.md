# test/beta/providers/test_network_mixed_provider.py

7 function(s): _require_all_keys, _wait_for_text_count, test_consulting_anthropic_initiator_openai_specialist, test_3way_discussion_one_per_provider, _wait_for_handoff, _wait_for_adapter_state, test_workflow_handoff_anthropic_to_openai.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _require_all_keys | function |  |
| _wait_for_text_count | function |  |
| test_consulting_anthropic_initiator_openai_specialist | function |  |
| test_3way_discussion_one_per_provider | function |  |
| _wait_for_handoff | function |  |
| _wait_for_adapter_state | function |  |
| test_workflow_handoff_anthropic_to_openai | function |  |

## Chunks

### _require_all_keys (function, L69-L75)

> *Summary: Checks for the presence of three specific environment variables (Anthropic, OpenAI, Gemini API keys). If all are set, it returns a tuple containing these three key values; otherwise, it skips the test execution.*


### _wait_for_text_count (function, L78-L92)

> *Summary: This asynchronous function polls a specified channel's write-ahead log until the count of `EV_TEXT` events meets or exceeds an expected value, respecting a defined timeout. It returns the final count of text events found in the log after waiting or timing out.*


### test_consulting_anthropic_initiator_openai_specialist (function, L98-L143)

> *Summary: This test verifies cross-provider delegation by setting up an Anthropic agent (Alice) to discover and delegate a query to an OpenAI agent (Bob). It confirms that the system correctly handles different tool-calling formats between providers, resulting in Alice receiving Bob's calculated answer ("266").*


### test_3way_discussion_one_per_provider (function, L150-L214)

> *Summary: This test verifies a round-robin discussion among three agents using different AI providers (Anthropic, OpenAI, Gemini). It initiates a debate and asserts that the resulting text events are recorded sequentially in the Write-Ahead Log according to the expected provider order.*


### _wait_for_handoff (function, L217-L229)

> *Summary: This asynchronous function polls a hub's write-ahead log for a specified channel until it finds any events marked as a "handoff." It returns a list of these handoff events if found within the given timeout, otherwise, it returns an empty list.*


### _wait_for_adapter_state (function, L232-L238)

> *Summary: This asynchronous function polls the adapter state for a given channel until a predicate returns true or a timeout is reached. It waits up to 60 seconds, checking the condition every 0.2 seconds before returning the final success status.*


### test_workflow_handoff_anthropic_to_openai (function, L244-L342)

> *Summary: This test verifies a cross-provider workflow handoff, simulating a human initiating a query that is routed from an Anthropic agent (triage) to an OpenAI agent (engineering). It asserts that the routing mechanism correctly transitions control and returns to the initial triage agent after the engineering response.*

