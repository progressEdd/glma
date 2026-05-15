# test/beta/test_aggregate.py

8 class(es): TestAggregateTrigger, TestConversationSummaryAggregate, TestWorkingMemoryAggregate, TestConversationSummaryStreamId, _RecordingAggregate, TestAggregationWiredOnAgent, _RaisingAggregate, TestAggregationLifecycleEvents. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestAggregateTrigger | class |  |
| TestConversationSummaryAggregate | class |  |
| TestWorkingMemoryAggregate | class |  |
| TestConversationSummaryStreamId | class |  |
| _RecordingAggregate | class |  |
| TestAggregationWiredOnAgent | class |  |
| _RaisingAggregate | class |  |
| TestAggregationLifecycleEvents | class |  |

## Chunks

### TestAggregateTrigger (class, L33-L44)

> *Summary: Verifies the initialization and configuration of an `AggregateTrigger` object. It tests that default values are set correctly and confirms that custom input parameters like turn counts, event counts, and end-of-sequence flags are properly assigned to the instance.*


### test_defaults (method, L34-L38, parent: TestAggregateTrigger)

> *Summary: Verifies that a newly instantiated `AggregateTrigger` object defaults to zero for turn and event counts, and has its end-of-process flag set to false. This test confirms the initial state of the aggregation trigger configuration.*


### test_custom_values (method, L40-L44, parent: TestAggregateTrigger)

> *Summary: This test verifies the correct initialization of an `AggregateTrigger` instance by asserting that its internal parameters—turn frequency, event frequency, and end-of-process flag—are set to the expected values (5, 50, and True).*


### TestConversationSummaryAggregate (class, L47-L138)

> *Summary: This test suite verifies the `ConversationSummaryAggregate`'s behavior when processing conversation events. It ensures that summaries are written with timestamped filenames for chronological sorting, correctly handles empty input lists, tracks usage statistics from model responses, and maintains correct ordering across multiple aggregation runs.*


### test_writes_timestamped_summary (method, L49-L73, parent: TestConversationSummaryAggregate)

> *Summary: This test verifies that the aggregation process creates a single summary file in the knowledge store, ensuring its filename is correctly prefixed with an ISO-formatted timestamp for chronological sorting. It simulates model responses and checks the resulting stored entry's naming convention.*


### test_skips_empty_events (method, L76-L85, parent: TestConversationSummaryAggregate)

> *Summary: When provided with an empty list of events, the aggregation process should result in no entries being stored in the knowledge base. This test verifies that calling `aggregate` with zero input events leaves the memory store empty.*


### test_stores_usage (method, L88-L102, parent: TestConversationSummaryAggregate)

> *Summary: This test verifies that the aggregation strategy correctly captures usage metrics after processing a request. It mocks an API response containing token counts and asserts that the `strategy` object's `last_usage` attribute reflects these input tokens.*


### test_chronological_ordering_of_summaries (method, L105-L138, parent: TestConversationSummaryAggregate)

> *Summary: This test verifies that multiple conversation summaries are stored and retrieved in chronological order based on their timestamps. It simulates aggregating two distinct summaries at different times, then asserts that the resulting list from the knowledge store is correctly sorted by date.*


### TestWorkingMemoryAggregate (class, L141-L246)

> *Summary: This test suite verifies the `WorkingMemoryAggregate`'s behavior for updating and managing persistent memory. It tests scenarios including writing new content, merging updates with existing context by passing it to the LLM, skipping empty inputs, using custom prompt templates, and falling back to prior content if the LLM returns an empty response.*


### test_writes_working_memory (method, L143-L159, parent: TestWorkingMemoryAggregate)

> *Summary: This test verifies that an aggregation strategy correctly writes data to a knowledge store. It simulates an API response containing updated content and usage metrics, then asserts the store successfully retrieves this written content.*


### test_merges_with_existing (method, L162-L188, parent: TestWorkingMemoryAggregate)

> *Summary: This test verifies that the aggregation strategy correctly passes existing working memory to an LLM when merging new input. It asserts that the mock client was called with a prompt containing the pre-existing context, and subsequently confirms the store is updated with the merged result from the LLM response.*


### test_skips_empty_events (method, L191-L198, parent: TestWorkingMemoryAggregate)

> *Summary: When provided with an empty event stream, the aggregation process should not write any data to the knowledge store. This test verifies that calling `aggregate` with no input events results in a null read from the designated memory location.*


### test_custom_prompt_template_is_used (method, L201-L225, parent: TestWorkingMemoryAggregate)

> *Summary: This test verifies that a user-supplied prompt template overrides the system's default verbatim when aggregating information. It asserts that the resulting input sent to the mock client correctly incorporates both the custom template and pre-existing memory content.*


### test_falls_back_to_existing_on_empty_response (method, L228-L246, parent: TestWorkingMemoryAggregate)

> *Summary: When the language model returns an empty response, this test verifies that the aggregation strategy correctly falls back and retains the previously stored content from the knowledge store. It simulates an LLM returning no data while ensuring the existing memory remains unchanged after processing.*


### TestConversationSummaryStreamId (class, L249-L270)

> *Summary: This test verifies that the generated summary filename includes the complete stream UUID when aggregating conversation data. It mocks necessary services and asserts that the resulting stored entry contains the full ID of the stream used during aggregation.*


### test_filename_uses_full_stream_id (method, L251-L270, parent: TestConversationSummaryStreamId)

> *Summary: This test verifies that the generated summary filename incorporates the complete stream UUID instead of just a partial identifier. It initializes an aggregate, runs it with mock dependencies, and asserts that the resulting stored entry contains the full ID string.*


### _RecordingAggregate (class, L273-L282)

> *Summary: This in-process strategy tracks invocation counts and records a summary file to the provided store upon each call. It increments an internal counter and writes a fixed string to a uniquely named markdown file within the memory path.*


### __init__ (method, L276-L278, parent: _RecordingAggregate)

> *Summary: Initializes an object by setting a call counter to zero and creating an empty dictionary to track the last usage of various items. This structure is used to maintain state across multiple operations within the instance.*


### aggregate (method, L280-L282, parent: _RecordingAggregate)

> *Summary: Increments a call counter and asynchronously writes the current count to a specific file path within the provided storage. This method updates internal state based on an input event stream.*


### TestAggregationWiredOnAgent (class, L285-L351)

> *Summary: These tests verify the end-to-end behavior of an aggregation middleware attached to an Agent, ensuring that `on_end=True` triggers aggregation exactly once per request, even when other triggers are active or when the underlying LLM call fails. The code uses mock components like `MemoryKnowledgeStore` and `MemoryStream` to simulate agent interactions and assert on the number of calls made by the recording aggregate strategy.*


### test_on_end_fires_once_per_ask (method, L289-L309, parent: TestAggregationWiredOnAgent)

> *Summary: This test verifies that the `on_end` trigger fires exactly once per ask when an agent completes its task. It sets up an agent with a recording aggregate and asserts that both the aggregate's call count and the collected completion events are equal to one after the agent is asked a question.*


### test_on_end_does_not_double_fire_with_other_triggers (method, L312-L327, parent: TestAggregationWiredOnAgent)

> *Summary: This test verifies that when both `on_end` and `every_n_turns=1` are active, the aggregation mechanism fires only once per request cycle. It initializes an agent with a specific configuration and asserts that the internal aggregate counter is exactly one after executing a single "go" command.*


### test_on_end_runs_even_when_turn_raises (method, L330-L351, parent: TestAggregationWiredOnAgent)

> *Summary: This test verifies that the `on_end` aggregation hook executes even if an underlying LLM call fails during an agent's turn. It simulates a failed turn by using a configuration without canned responses and asserts that the aggregate strategy recorded exactly one call.*


### _RaisingAggregate (class, L354-L360)

> *Summary: This class implements an aggregation strategy designed specifically to fail during testing. It accepts events, a context, and a store but immediately raises a `RuntimeError` upon execution.*


### aggregate (method, L359-L360, parent: _RaisingAggregate)

> *Summary: This method is intended to process a collection of `events` using provided `context` and `store`. Currently, it raises a runtime error, indicating unimplemented aggregation logic.*


### TestAggregationLifecycleEvents (class, L364-L415)

> *Summary: This test suite verifies that lifecycle events, specifically `AggregationStarted` and `AggregationFailed`, are correctly emitted to a stream when an agent interacts with an aggregation strategy. It asserts the timing of these events relative to execution and confirms failure reporting when the underlying aggregate raises an exception.*


### test_started_event_fires_before_strategy_runs (method, L368-L387, parent: TestAggregationLifecycleEvents)

> *Summary: This test verifies that an `AggregationStarted` event is emitted immediately when an agent begins processing, even before the associated aggregation strategy has executed. It achieves this by subscribing to events during an agent's execution and asserting one such event was captured.*


### test_failed_event_fires_when_strategy_raises (method, L389-L415, parent: TestAggregationLifecycleEvents)

> *Summary: This test verifies that an `AggregationFailed` event is emitted when the configured aggregation strategy raises an exception during processing. It sets up an agent using a mock store and stream, then asserts that exactly one failure event containing specific error details is captured while no completion events occur.*

