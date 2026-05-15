# autogen/beta/compact.py

5 class(es): CompactionSummary, CompactStrategy, CompactTrigger, TailWindowCompact, SummarizeCompact. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CompactionSummary | class |  |
| CompactStrategy | class |  |
| CompactTrigger | class |  |
| TailWindowCompact | class |  |
| SummarizeCompact | class |  |

## Chunks

### CompactionSummary (class, L29-L38)

> *Summary: Represents a synthetic event summarizing multiple compacted historical events. It stores the resulting summary string and the total count of events that were condensed into this single entry.*


### CompactStrategy (class, L42-L63)

> *Summary: Defines a contract for strategies that reduce event streams to meet system constraints. It accepts the current list of events, execution context, and an optional knowledge store, returning a causally ordered, compacted list of events.*


### compact (method, L49-L63, parent: CompactStrategy)

> *Summary: This method processes a list of historical events, potentially using an external knowledge store to manage and persist any discarded information. It returns the resulting, condensed list of `BaseEvent` objects after compaction.*


### CompactTrigger (class, L67-L75)

> *Summary: Defines deterministic thresholds for initiating data compaction, which triggers if any configured limit is surpassed. It uses configurable maximum event counts and token estimates to determine when compaction should occur.*


### TailWindowCompact (class, L78-L104)

> *Summary: This class implements a simple context management strategy that retains only the most recent $N$ events from an input list. It discards older events and optionally persists the dropped events to a knowledge store before returning the truncated list.*


### __init__ (method, L85-L86, parent: TailWindowCompact)

> *Summary: Initializes an object by storing a specific integer value as its internal target. This sets the primary goal or reference point for subsequent operations within the instance.*


### compact (method, L88-L104, parent: TailWindowCompact)

> *Summary: This method truncates a list of incoming events to keep only the most recent $\text{self.\_target}$ items. If a knowledge store is provided, it asynchronously persists the discarded (older) events before returning the condensed list.*


### SummarizeCompact (class, L107-L164)

> *Summary: This class summarizes a list of older events into a single `CompactionSummary` event using an LLM call, keeping only the most recent events up to a specified target size. It accepts a list of `BaseEvent`s and returns a new history list containing the summary followed by the retained recent events.*


### __init__ (method, L116-L123, parent: SummarizeCompact)

> *Summary: Initializes the object by storing a target integer and a model configuration. It also sets up a Pydantic serializer instance for data handling and initializes an empty dictionary to track usage history.*


### compact (method, L125-L148, parent: SummarizeCompact)

> *Summary: If the provided list of events exceeds a configured target size, this method summarizes the oldest events using an LLM and persists them to storage if available. It then returns a new list containing the summary event followed by the most recent events.*


### _summarize (method, L150-L164, parent: SummarizeCompact)

> *Summary: This method generates a concise summary of a list of conversation events by sending the concatenated event history to an external model client via a structured prompt request. It returns the resulting text content from the model's response, while also updating internal usage tracking metrics.*

