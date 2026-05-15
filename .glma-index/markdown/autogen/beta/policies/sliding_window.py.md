# autogen/beta/policies/sliding_window.py

1 class(es): SlidingWindowPolicy. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SlidingWindowPolicy | class |  |

## Chunks

### SlidingWindowPolicy (class, L13-L37)

> *Summary: This policy maintains a fixed-size history by retaining only the most recent $N$ events from an input list. If the event count exceeds the maximum size, it truncates older entries and optionally appends a notification to the prompts indicating how many events were dropped.*


### __init__ (method, L21-L23, parent: SlidingWindowPolicy)

> *Summary: Initializes a sliding window policy by setting the maximum number of events it can track and an optional flag to control transparency. This configuration dictates how many past events are considered in subsequent operations.*


### apply (method, L25-L37, parent: SlidingWindowPolicy)

> *Summary: When the event history exceeds a defined maximum size, this method truncates the `events` list to retain only the most recent entries. It optionally appends a notification prompt if transparency is enabled before returning the potentially modified prompts and the trimmed events.*

