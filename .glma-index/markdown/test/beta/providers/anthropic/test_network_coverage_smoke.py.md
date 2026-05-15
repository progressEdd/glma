# test/beta/providers/anthropic/test_network_coverage_smoke.py

7 function(s): anthropic_config, _wait_for_text_count, test_conversation_adapter_bidirectional_two_turns, test_peers_describe_returns_fallback_skill, test_channels_close_invoked_by_llm, test_context_search_finds_earlier_turn, test_workflow_graph_with_two_handoff_tools.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| anthropic_config | function |  |
| _wait_for_text_count | function |  |
| test_conversation_adapter_bidirectional_two_turns | function |  |
| test_peers_describe_returns_fallback_skill | function |  |
| test_channels_close_invoked_by_llm | function |  |
| test_context_search_finds_earlier_turn | function |  |
| test_workflow_graph_with_two_handoff_tools | function |  |

## Chunks

### anthropic_config (function, L70-L74)

> *Summary: This function retrieves the `ANTHROPIC_API_KEY` environment variable; if it's missing, it skips testing. Otherwise, it returns an `AnthropicConfig` object configured for the "claude-haiku-4-5" model with a temperature of 0.*


### _wait_for_text_count (function, L77-L91)

> *Summary: This asynchronous function polls a specified channel's write-ahead log until the count of `EV_TEXT` events meets or exceeds an expected value, respecting a defined timeout. It returns the final observed text event count after either meeting the expectation or exhausting the allotted time.*


### test_conversation_adapter_bidirectional_two_turns (function, L96-L147)

> *Summary: This test verifies a bidirectional, two-turn conversation flow between two agents using an Anthropic configuration. It sends an initial message from Alice to Bob, asserts that both messages are received by checking the text count, and confirms the channel remains active before explicitly closing it.*


### test_peers_describe_returns_fallback_skill (function, L152-L208)

> *Summary: Tests that the `peers(action="describe")` call returns a fallback skill description when no specific `SKILL.md` is registered for a peer. It verifies that an agent querying another peer successfully extracts a claimed capability, such as "arithmetic," from this fallback data structure.*


### test_channels_close_invoked_by_llm (function, L213-L271)

> *Summary: This test verifies that an LLM agent correctly invokes a `channels(action='close')` tool when instructed by the user. It sets up two agents, opens a conversation channel between them, prompts one agent to close it, and then asserts that the channel's state transitions to `CLOSED`.*


### test_context_search_finds_earlier_turn (function, L276-L335)

> *Summary: This test verifies that an LLM agent can successfully use a `context(action="search")` call to retrieve specific information from earlier messages within a conversation channel. It sets up two agents, seeds the chat with a secret fact, and then prompts one agent to search for that fact, asserting the correct value is returned in the response.*


### test_workflow_graph_with_two_handoff_tools (function, L340-L448)

> *Summary: This test verifies that a workflow graph correctly routes an initial user query to the appropriate specialized agent based on tool selection by a triage coordinator. It sends a billing-related message, asserts that the resulting event packet indicates routing to the `transfer_to_billing` tool, and cleans up all associated resources.*

