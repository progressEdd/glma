# autogen/agentchat/realtime/experimental/realtime_events.py

7 class(es): RealtimeEvent, SessionCreated, SessionUpdated, AudioDelta, InputAudioBufferDelta, SpeechStarted, FunctionCall.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RealtimeEvent | class |  |
| SessionCreated | class |  |
| SessionUpdated | class |  |
| AudioDelta | class |  |
| InputAudioBufferDelta | class |  |
| SpeechStarted | class |  |
| FunctionCall | class |  |

## Chunks

### RealtimeEvent (class, L10-L11)

> *Summary: Represents a real-time event by encapsulating raw message data as a dictionary. It serves as the standardized structure for transmitting asynchronous updates within the system.*


### SessionCreated (class, L14-L15)

> *Summary: Represents a real-time event signaling the creation of a new session. It is a subclass of `RealtimeEvent` and carries a fixed type identifier `"session.created"`.*


### SessionUpdated (class, L18-L19)

> *Summary: Represents a session update event, inheriting from `RealtimeEvent`. It signals that the state of a session has changed and is identified by the type `"session.updated"`.*


### AudioDelta (class, L22-L25)

> *Summary: Represents a partial audio response update, carrying the `delta` string and an associated `item_id`. This class inherits from `RealtimeEvent` to signal real-time streaming data.*


### InputAudioBufferDelta (class, L28-L31)

> *Summary: Represents a change or update to an audio buffer stream, carrying the delta data as a string and an associated item identifier. This class inherits from `RealtimeEvent` to signal real-time system updates.*


### SpeechStarted (class, L34-L35)

> *Summary: Represents an event indicating that speech has begun, carrying a specific type identifier for real-time processing. This class inherits from `RealtimeEvent` to signal the start of audio input.*


### FunctionCall (class, L38-L42)

> *Summary: Represents a specific type of realtime event indicating the completion of function call arguments. It carries the name, argument dictionary, and unique ID associated with the completed function call.*

