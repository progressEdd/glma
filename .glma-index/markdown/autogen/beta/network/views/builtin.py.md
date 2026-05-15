# autogen/beta/network/views/builtin.py

2 function(s): _to_event, _summarize_older. 2 class(es): FullTranscript, WindowedSummary. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FullTranscript | class |  |
| WindowedSummary | class |  |
| _to_event | function |  |
| _summarize_older | function |  |

## Chunks

### FullTranscript (class, L28-L63)

> *Summary: This class processes a log of envelopes, filtering for those visible to a specific participant. It transforms these visible envelopes into either `ModelMessage` (if sent by the participant) or `ModelRequest` (if sent by another party), using an envelope renderer to generate text content.*


### project (method, L44-L63, parent: FullTranscript)

> *Summary: Processes a list of `Envelope`s from a write-ahead log, filtering them based on visibility for a given participant. It transforms visible envelopes into a list of `BaseEvent`s, creating either a `ModelMessage` if the sender is the participant or a `ModelRequest` otherwise.*


### WindowedSummary (class, L66-L117)

> *Summary: This class manages the conversation history projection by retaining only the most recent $N$ visible messages. It processes a list of `Envelope`s from the Write-Ahead Log (`wal`), generating either all visible events or prepending a static `CompactionSummary` for older, aggregated content if the total count exceeds $N$.*


### __init__ (method, L83-L86, parent: WindowedSummary)

> *Summary: Initializes the object by storing a positive integer `recent_n` as an internal attribute. It validates that the provided input is at least one to prevent errors during operation.*


### recent_n (method, L89-L90, parent: WindowedSummary)

> *Summary: Returns the stored integer value representing the number of recent items tracked by the instance. This method provides direct access to an internal state variable.*


### project (method, L92-L117, parent: WindowedSummary)

> *Summary: Filters a list of `Envelope`s based on visibility for a given participant and renders them using an envelope renderer. If the resulting visible history exceeds a configured limit, it returns a compaction summary for older entries followed by the most recent events.*


### _to_event (function, L120-L123)

> *Summary: Transforms an incoming message based on the sender's identity; if the sender matches the specified ID, it returns a direct `ModelMessage`, otherwise, it generates a `ModelRequest` containing the text input.*


### _summarize_older (function, L126-L129)

> *Summary: Generates a summary string detailing the number of messages and the IDs of speakers present in a list of older `Envelope` objects. It sorts the unique sender IDs to ensure consistent output formatting.*

