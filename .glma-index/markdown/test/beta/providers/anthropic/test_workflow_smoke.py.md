# test/beta/providers/anthropic/test_workflow_smoke.py

3 function(s): anthropic_config, _wait_for_state, test_workflow_swarm_handoff_revert_close.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| anthropic_config | function |  |
| _wait_for_state | function |  |
| test_workflow_swarm_handoff_revert_close | function |  |

## Chunks

### anthropic_config (function, L60-L64)

> *Summary: Retrieves the API key from environment variables and returns a configured `AnthropicConfig` object if the key is present; otherwise, it skips testing. The configuration defaults to using the "claude-haiku-4-5" model with zero temperature.*


### _wait_for_state (function, L67-L79)

> *Summary: This asynchronous function polls a provided predicate against the adapter state of a specific channel until the condition is met or a timeout expires. It returns `True` if the predicate becomes true within the allotted time, otherwise it returns `False`.*


### test_workflow_swarm_handoff_revert_close (function, L84-L220)

> *Summary: This test verifies a multi-agent workflow where an initial user query is routed from a triage agent to an engineering agent via a tool call, and then successfully reverts back to the triage agent. It further asserts that the entire conversation state persists correctly across a simulated system restart by re-opening the hub against the same persistent store.*

