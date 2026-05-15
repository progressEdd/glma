# autogen/beta/observers/loop_detector.py

1 class(es): LoopDetector. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LoopDetector | class |  |

## Chunks

### LoopDetector (class, L16-L75)

> *Summary: Monitors `ToolCallEvent`s by maintaining a sliding window of recent calls to detect repetitive patterns. It outputs an `ObserverAlert` if the same tool and arguments appear consecutively for a specified threshold within the history.*


### __init__ (method, L33-L44, parent: LoopDetector)

> *Summary: Initializes a loop detector by setting parameters for window size and repetition threshold. It sets up an internal history buffer to track recent events and a set to flag detected loops based on incoming `ToolCallEvent`s.*


### process (method, L46-L70, parent: LoopDetector)

> *Summary: Analyzes incoming events to detect repetitive tool calls by tracking the sequence of `(tool_name, arguments)` pairs in internal history. If a specific tool call repeats consecutively for the configured threshold and hasn't been flagged, it returns an `ObserverAlert` warning about a potential infinite loop.*


### reset (method, L72-L75, parent: LoopDetector)

> *Summary: Clears the internal history and flagged items to prepare the observer for a new session. This method takes no inputs and returns nothing.*

