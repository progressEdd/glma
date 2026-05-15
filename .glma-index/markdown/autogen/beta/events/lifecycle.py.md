# autogen/beta/events/lifecycle.py

10 class(es): ObserverStarted, ObserverCompleted, CompactionStarted, CompactionCompleted, CompactionFailed, AggregationStarted, AggregationCompleted, AggregationFailed, EventLogFailed, UnknownEvent.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ObserverStarted | class |  |
| ObserverCompleted | class |  |
| CompactionStarted | class |  |
| CompactionCompleted | class |  |
| CompactionFailed | class |  |
| AggregationStarted | class |  |
| AggregationCompleted | class |  |
| AggregationFailed | class |  |
| EventLogFailed | class |  |
| UnknownEvent | class |  |

## Chunks

### ObserverStarted (class, L17-L22)

> *Summary: Signals that an observer has successfully attached to the agent's data stream. This event carries a string identifying the observer.*


### ObserverCompleted (class, L25-L30)

> *Summary: Signals that an observer has finished its subscription to an agent's data stream. It carries a `name` attribute identifying the completed observer.*


### CompactionStarted (class, L33-L46)

> *Summary: Signals the start of an agent's data compaction process, providing details about the involved agent, strategy, and initial event count. This event should be monitored alongside completion or failure events to track the entire compaction lifecycle.*


### CompactionCompleted (class, L49-L59)

> *Summary: This event signals the completion of a compaction process on an agent. It carries details about the operation, including which agent and strategy were involved, the number of events before and after, LLM call count, and usage metrics.*


### CompactionFailed (class, L62-L75)

> *Summary: Signals an error during agent compaction by carrying details about the failing agent, strategy, and specific error information. This event is designed as a durable signal for observers to react to failures in the streaming process.*


### AggregationStarted (class, L78-L90)

> *Summary: This event signals the start of an agent's data aggregation process. It carries information about the originating agent, the strategy being used, and the initial count of events involved in the aggregation.*


### AggregationCompleted (class, L93-L102)

> *Summary: This event signals the completion of an agent's aggregation process. It carries details about the agent, strategy used, total events processed, and metrics like LLM calls and usage data.*


### AggregationFailed (class, L105-L118)

> *Summary: Signals that an aggregation strategy failed during an agent's stream processing. It carries details about the failing agent, strategy, and the specific error encountered.*


### EventLogFailed (class, L121-L133)

> *Summary: Signals that an error occurred while writing the event log after an agent's turn completes. It carries details about the failing agent, the type of error, and the error message itself.*


### UnknownEvent (class, L136-L143)

> *Summary: Serves as a fallback event structure when an incoming event's type cannot be determined during deserialization. It stores the original, unprocessed raw data within its `data` dictionary for later inspection.*

