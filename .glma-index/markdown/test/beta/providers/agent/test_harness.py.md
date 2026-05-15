# test/beta/providers/agent/test_harness.py

11 function(s): test_conversation_policy_basic, test_sliding_window_trims_long_history, test_token_budget_policy_clamps_history, test_multiple_policies_compose, test_knowledge_tool_via_actor, test_bootstrap_runs_once, test_tail_window_compact_triggers, test_summarize_compact_uses_llm, test_on_end_aggregation, test_every_n_turns_aggregation and 1 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_conversation_policy_basic | function |  |
| test_sliding_window_trims_long_history | function |  |
| test_token_budget_policy_clamps_history | function |  |
| test_multiple_policies_compose | function |  |
| test_knowledge_tool_via_actor | function |  |
| test_bootstrap_runs_once | function |  |
| test_tail_window_compact_triggers | function |  |
| test_summarize_compact_uses_llm | function |  |
| test_on_end_aggregation | function |  |
| test_every_n_turns_aggregation | function |  |
| test_every_n_events_aggregation | function |  |

## Chunks

### test_conversation_policy_basic (function, L43-L56)

> *Summary: This test verifies that an agent configured with a `ConversationPolicy` still produces a sensible response when asked a simple question. It initializes the agent with the policy and asserts that the resulting reply body contains the expected text.*


### test_sliding_window_trims_long_history (function, L59-L105)

> *Summary: This test verifies that the `SlidingWindowPolicy` correctly limits the history sent to an LLM agent. It captures all outgoing message payloads and asserts that the final payload adheres to the maximum event limit while ensuring older, specified inputs are successfully trimmed from the context.*


### test_token_budget_policy_clamps_history (function, L108-L134)

> *Summary: This test verifies that a tight `TokenBudgetPolicy` correctly evicts older conversation turns when interacting with an agent. It builds a multi-turn history and asserts that the final response does not contain any of the initial inputs because they were trimmed from the LLM's context due to the small token budget.*


### test_multiple_policies_compose (function, L137-L151)

> *Summary: This test verifies the composition of multiple policies—Conversation, SlidingWindow, and TokenBudget—within an Agent. It sends a simple query to the agent and asserts that the resulting response body contains the expected answer ("2").*


### test_knowledge_tool_via_actor (function, L154-L182)

> *Summary: This test verifies an agent's ability to use a knowledge tool by first instructing it to write information to a memory store, then confirming the data was saved directly. Finally, it prompts the agent again to recall that stored information via the tool and asserts the correct retrieval.*


### test_bootstrap_runs_once (function, L185-L200)

> *Summary: This test verifies that the `DefaultBootstrap` mechanism writes a specific initialization marker to the knowledge store only upon the first execution of an agent's query. It confirms this by asserting the presence of the `/.initialized` sentinel after the initial call.*


### test_tail_window_compact_triggers (function, L203-L232)

> *Summary: This test verifies that a `TailWindowCompact` knowledge store triggers compaction after a specified number of events are processed by an agent. It simulates four turns of interaction and asserts that at least one compaction event occurs, confirming the correct strategy and event count difference.*


### test_summarize_compact_uses_llm (function, L235-L262)

> *Summary: This test verifies that the `SummarizeCompact` mechanism triggers an LLM call when processing a sequence of interactions. It initializes an agent with memory and compaction settings, then executes multiple prompts to confirm at least one compacting event containing an LLM call is recorded.*


### test_on_end_aggregation (function, L265-L293)

> *Summary: This test verifies that an agent configured with `on_end=True` correctly triggers and executes a conversation summary aggregation upon task completion. It asserts that at least one aggregation event is captured, the correct strategy was used, and the resulting summary has been persisted to the knowledge store.*


### test_every_n_turns_aggregation (function, L296-L331)

> *Summary: This test verifies that an aggregation trigger configured for every two turns correctly fires and updates a knowledge store. It simulates sequential user interactions, asserting that exactly two aggregation events are captured and that the underlying knowledge store contains data after the process completes.*


### test_every_n_events_aggregation (function, L334-L365)

> *Summary: This test verifies that an `AggregateTrigger` configured for every $N$ events fires precisely when the total event count crosses a multiple of $N$. It simulates sequential agent interactions, asserting that two aggregation events are captured after specific query sequences.*

