# autogen/beta/aggregate.py

4 class(es): AggregateStrategy, AggregateTrigger, ConversationSummaryAggregate, WorkingMemoryAggregate. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AggregateStrategy | class |  |
| AggregateTrigger | class |  |
| ConversationSummaryAggregate | class |  |
| WorkingMemoryAggregate | class |  |

## Chunks

### AggregateStrategy (class, L30-L50)

> *Summary: Defines a contract for strategies that process raw event streams, execution context, and a knowledge store. Its primary purpose is to extract structured knowledge from the input events and persist it within the provided knowledge store asynchronously.*


### aggregate (method, L37-L50, parent: AggregateStrategy)

> *Summary: This method processes a list of historical events, along with the execution context and a knowledge store, to extract and persist relevant knowledge. It updates the provided `KnowledgeStore` based on the input event stream.*


### AggregateTrigger (class, L54-L62)

> *Summary: Defines deterministic criteria for initiating data aggregation, allowing configuration via turn count (`every_n_turns`), event count (`every_n_events`), or upon conversation completion (`on_end`). These conditions operate independently to trigger the aggregation process.*


### ConversationSummaryAggregate (class, L65-L107)

> *Summary: This component generates a summary for a sequence of conversation events by calling an LLM with the event data as input. It then persists this generated summary to a file within the knowledge store, keyed by timestamp and stream ID.*


### __init__ (method, L72-L78, parent: ConversationSummaryAggregate)

> *Summary: Initializes the object by storing a provided `ModelConfig` and setting up a Pydantic serializer instance for data handling. It also initializes an empty dictionary to track the last usage of components.*


### aggregate (method, L80-L91, parent: ConversationSummaryAggregate)

> *Summary: This method processes a list of events by first generating a summary from them. It then saves this summary to the knowledge store, using a timestamp and stream ID in the filename.*


### _summarize (method, L93-L107, parent: ConversationSummaryAggregate)

> *Summary: This method generates a summary string by sending a list of conversation events to an external model client. It constructs a prompt from the event strings, awaits the model's response, updates usage statistics, and returns the generated content.*


### WorkingMemoryAggregate (class, L126-L202)

> *Summary: This class updates a designated working memory file by merging new events with the existing content using an LLM call. It takes model configuration and an optional prompt template as input, returning the updated string content written back to storage.*


### __init__ (method, L162-L174, parent: WorkingMemoryAggregate)

> *Summary: Initializes an aggregator by storing a model configuration and a prompt template. It also sets up a Pydantic serializer for data handling and initializes a dictionary to track usage statistics.*


### aggregate (method, L176-L186, parent: WorkingMemoryAggregate)

> *Summary: This method merges a list of incoming `BaseEvent` objects into the existing state stored in the knowledge base. It reads the current working memory, applies the updates from the events using an internal merge function, and then writes the resulting aggregated data back to storage.*


### _merge (method, L188-L202, parent: WorkingMemoryAggregate)

> *Summary: This method synthesizes a new string by sending the current state and a list of events to an LLM client via a formatted prompt. It returns the model's generated content, falling back to the original input if no content is returned.*

