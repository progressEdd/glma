# test/beta/test_assembly.py

6 class(es): TestConversationPolicy, TestSlidingWindowPolicy, TestTokenBudgetPolicy, TestAssemblerMiddleware, TestEpisodicMemoryPolicy, TestWorkingMemoryPolicy. 19 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestConversationPolicy | class |  |
| TestSlidingWindowPolicy | class |  |
| TestTokenBudgetPolicy | class |  |
| TestAssemblerMiddleware | class |  |
| TestEpisodicMemoryPolicy | class |  |
| TestWorkingMemoryPolicy | class |  |

## Chunks

### TestConversationPolicy (class, L33-L56)

> *Summary: This test suite verifies the `ConversationPolicy`'s filtering logic by ensuring it correctly processes a list of mixed conversation events, excluding non-conversational alerts like `ObserverAlert`. It also confirms that compaction summaries are retained when provided as input to the policy.*


### test_filters_to_conversation_events (method, L35-L47, parent: TestConversationPolicy)

> *Summary: This test verifies that a conversation policy correctly filters a list of input events. It takes a sequence of various model and tool events as input and asserts that the resulting filtered list excludes any `ObserverAlert` types while retaining four other event types.*


### test_includes_compaction_summary (method, L50-L56, parent: TestConversationPolicy)

> *Summary: This test verifies that a `ConversationPolicy` correctly filters and retains the initial `CompactionSummary` when processing a sequence of events including model requests. It asserts that the provided summary object is present in the resulting filtered list.*


### TestSlidingWindowPolicy (class, L65-L91)

> *Summary: This test suite verifies the behavior of a sliding window policy by simulating event processing against various scenarios. It asserts that the policy correctly filters inputs to respect a maximum event limit, handles cases where no trimming occurs, and transparently generates summary prompts when configured.*


### test_no_trim_below_max (method, L67-L73, parent: TestSlidingWindowPolicy)

> *Summary: When given a list of five input events and a `SlidingWindowPolicy` set to a maximum of ten, this test asserts that all five events are retained in the filtered output and no prompts are generated. This confirms the policy does not trim events when the event count is below the defined maximum.*


### test_trims_to_max (method, L76-L82, parent: TestSlidingWindowPolicy)

> *Summary: This test verifies that a `SlidingWindowPolicy` correctly filters an input stream of ten events down to the maximum allowed size of three. It asserts that the resulting filtered list contains the last three processed events, specifically checking for `"msg-7"` as the first element in the output.*


### test_transparent_adds_note (method, L85-L91, parent: TestSlidingWindowPolicy)

> *Summary: This test verifies that a sliding window policy configured for transparency correctly processes a sequence of ten input messages. It asserts that the resulting output contains a summary indicating the processing of three out of ten events.*


### TestTokenBudgetPolicy (class, L94-L111)

> *Summary: This test suite verifies the `TokenBudgetPolicy`'s behavior when processing a sequence of model requests. It asserts that the policy either keeps all events if they fit within the specified token budget or correctly trims them to adhere to the maximum allowed tokens, ensuring at least the last fitting event is retained.*


### test_no_trim_within_budget (method, L96-L101, parent: TestTokenBudgetPolicy)

> *Summary: This test verifies that when the token budget is not exceeded, no trimming occurs during policy application. It takes a list of model requests and returns a filtered list containing all original requests if they fit within the defined `TokenBudgetPolicy`.*


### test_trims_to_budget (method, L104-L111, parent: TestTokenBudgetPolicy)

> *Summary: This test verifies a token budget policy's trimming behavior by applying it to a list of model requests. It asserts that the resulting filtered list retains at least one event, specifically ensuring the last retained event matches the content of the second input request ("b" * 5).*


### TestAssemblerMiddleware (class, L114-L210)

> *Summary: This test suite verifies the behavior of an `AssemblerMiddleware` by simulating LLM calls with various policy configurations. It confirms that policies are applied sequentially, prompts are correctly restored upon completion or failure, and it validates the ordering constraints between defined policies.*


### test_applies_policies_in_order (method, L116-L141, parent: TestAssemblerMiddleware)

> *Summary: This test verifies that policies are processed sequentially by simulating an LLM call within a middleware setup. It feeds a sequence of events into the assembler and asserts that only specific, expected event types are passed through during the mocked LLM interaction.*


### test_restores_prompts_after_call (method, L144-L162, parent: TestAssemblerMiddleware)

> *Summary: This test verifies that an assembler middleware correctly restores the original prompt context after an LLM call. It injects a temporary prompt during execution but asserts that the context reverts to its initial state afterward.*


### test_validate_order_warns_on_bad_ordering (method, L164-L175, parent: TestAssemblerMiddleware)

> *Summary: This test verifies that the `AssemblerMiddleware` correctly identifies and warns about an invalid policy ordering when provided with a list of policies. It asserts that exactly one warning is generated, specifically mentioning the misplaced "sliding\_window" policy.*


### test_validate_order_no_warnings_for_correct_order (method, L177-L187, parent: TestAssemblerMiddleware)

> *Summary: This test verifies that when provided with a list of policies, the `AssemblerMiddleware` correctly validates the order and returns no warnings if the input is correct. It uses mock policy objects to simulate the middleware's validation process.*


### test_restores_prompts_on_exception (method, L190-L210, parent: TestAssemblerMiddleware)

> *Summary: This test verifies that an assembler middleware correctly restores the original prompt state when an underlying LLM call fails with a `RuntimeError`. It achieves this by injecting a failing callback and asserting that the context's prompt reverts to its initial value after the exception is caught.*


### TestEpisodicMemoryPolicy (class, L213-L261)

> *Summary: This test suite verifies the `EpisodicMemoryPolicy`'s behavior when interacting with a knowledge store. It confirms that the policy correctly injects stored conversation summaries into prompts, respects a maximum episode limit by prioritizing recent memories, and behaves as a no-op if no memory store is available or if no summaries exist.*


### test_injects_summaries_from_store (method, L215-L227, parent: TestEpisodicMemoryPolicy)

> *Summary: This test verifies that an episodic memory policy correctly injects stored summaries into generated prompts. It initializes a `MemoryKnowledgeStore` with sample data, configures the policy and context to use this store, and asserts that the resulting prompts contain references to the injected session summaries.*


### test_limits_to_max_episodes (method, L230-L245, parent: TestEpisodicMemoryPolicy)

> *Summary: This test verifies that an episodic memory policy correctly limits the retrieved memories to a maximum number of episodes. It populates a knowledge store with ten items and asserts that when applying the policy with `max_episodes=3`, only the three most recent summaries are included in the resulting prompts.*


### test_no_op_without_store (method, L248-L252, parent: TestEpisodicMemoryPolicy)

> *Summary: This test verifies that when a no-operation instruction is applied to the memory policy within a given context, it returns the original input prompt unchanged and no events. It uses an `EpisodicMemoryPolicy` initialized with existing data and processes a single text input request.*


### test_no_op_when_no_summaries (method, L255-L261, parent: TestEpisodicMemoryPolicy)

> *Summary: When provided with no input memories, this test verifies that the memory policy returns an empty list of prompts. It sets up a mock knowledge store and context to simulate the scenario where no episodic data is available for processing.*


### TestWorkingMemoryPolicy (class, L264-L292)

> *Summary: These tests verify the `WorkingMemoryPolicy`'s behavior by checking if it correctly injects content from a provided knowledge store into generated prompts when memory is available. It also confirms that the policy produces no output when either the knowledge store or the specific working memory file does not exist.*


### test_injects_working_memory (method, L266-L276, parent: TestWorkingMemoryPolicy)

> *Summary: This test verifies that a policy correctly retrieves and incorporates data from a memory store. It writes content to the store, then applies the policy using a context linked to that store, asserting that the resulting prompts contain the stored information.*


### test_no_op_without_store (method, L279-L283, parent: TestWorkingMemoryPolicy)

> *Summary: This test verifies that applying a `WorkingMemoryPolicy` with no input and an empty memory stream results in no generated prompts. It confirms the policy correctly handles scenarios where no data is available for processing.*


### test_no_op_without_working_memory_file (method, L286-L292, parent: TestWorkingMemoryPolicy)

> *Summary: When applying a policy with no input and without a working memory file, the function asserts that no prompts are generated. It initializes necessary components like a knowledge store and context to test this specific scenario.*

