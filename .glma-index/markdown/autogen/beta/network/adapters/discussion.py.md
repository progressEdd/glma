# autogen/beta/network/adapters/discussion.py

2 function(s): _is_channel_protocol_event, _is_task_event. 2 class(es): DiscussionState, DiscussionAdapter. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _is_channel_protocol_event | function |  |
| _is_task_event | function |  |
| DiscussionState | class |  |
| DiscussionAdapter | class |  |

## Chunks

### _is_channel_protocol_event (function, L73-L74)

> *Summary: Checks if an incoming `Envelope`'s event type matches any predefined channel protocol events. Returns a boolean indicating whether the event is part of the established channel protocol.*


### _is_task_event (function, L77-L78)

> *Summary: Checks if an incoming `Envelope` represents a task event by inspecting its `event_type`. Returns `True` if the type string begins with `"ag2.task."`, otherwise returns `False`.*


### DiscussionState (class, L82-L97)

> *Summary: Represents the persistent state for a discussion channel, capturing key information like participant order and turn tracking. It stores snapshots of speaker sequence and recent activity to allow deterministic rehydration from a Write-Ahead Log without full metadata access during folding.*


### DiscussionAdapter (class, L100-L257)

> *Summary: Manages a multi-participant discussion channel enforcing turn-taking via round-robin ordering. It processes incoming text messages by updating the state to determine the next expected speaker and validates that only the designated participant sends a message at any given time.*


### __init__ (method, L114-L134, parent: DiscussionAdapter)

> *Summary: Initializes a discussion adapter by setting up an internal cache and creating a `ChannelManifest`. This manifest defines the channel type, versioning, minimum participant count, expected behavior (like turn timing), and default viewing policy for discussions.*


### initial_state (method, L138-L143, parent: DiscussionAdapter)

> *Summary: Generates the starting state for a discussion based on channel metadata. It determines the speaking order from participants and sets the initial expected speaker to the creator of the channel.*


### fold (method, L145-L163, parent: DiscussionAdapter)

> *Summary: This method advances the discussion state based on a received text envelope, provided it's not a channel or task event. It determines the next speaker by cycling through the participants in their defined order and updates the state with the current sender as the last speaker and increments the turn count.*


### validate_create (method, L165-L172, parent: DiscussionAdapter)

> *Summary: Ensures a new discussion channel has at least two participants and validates that the specified ordering knob is one of the supported options, raising a `ProtocolError` if either condition fails.*


### validate_send (method, L174-L188, parent: DiscussionAdapter)

> *Summary: Ensures that an incoming message is a text event from the expected speaker in a discussion channel. It validates the envelope type and sender ID against the current state before allowing processing.*


### on_accepted (method, L190-L198, parent: DiscussionAdapter)

> *Summary: When a discussion is accepted, this method returns an empty result, indicating that the acceptance itself does not trigger any immediate state changes within the adapter logic. It assumes channel closure and speaker rotation are handled elsewhere by `Hub` or `fold`.*


### default_view_policy (method, L200-L206, parent: DiscussionAdapter)

> *Summary: Calculates a default view policy based on channel metadata and participant ID. It returns a `WindowedSummary` object whose window size is determined by the maximum of four or twice the number of participants in the channel.*


### extract_turn_input (method, L208-L209, parent: DiscussionAdapter)

> *Summary: This method delegates the extraction of turn input from an `envelope` object to a default implementation. It serves as a simple pass-through mechanism for retrieving structured conversational data.*


### build_round_envelope (method, L211-L212, parent: DiscussionAdapter)

> *Summary: This method acts as a simple wrapper that delegates the construction of a round envelope to a default implementation. It accepts metadata, sender ID, reply status, events, current state, and a hub object as inputs to produce the final envelope structure.*


### render_envelope (method, L214-L215, parent: DiscussionAdapter)

> *Summary: This method delegates the rendering of an `envelope` object to a default implementation. It accepts one `envelope` input and returns the rendered output from that default function.*


### tools_for (method, L217-L224, parent: DiscussionAdapter)

> *Summary: This method determines which tools are available for a given participant based on the current discussion state. It returns a list containing only the "say" tool if the participant is the next expected speaker in the round-robin sequence; otherwise, it returns an empty list.*


### _cached_say_tool (method, L226-L233, parent: DiscussionAdapter)

> *Summary: Retrieves a memoized "say" tool for a given client agent ID, returning a previously generated instance if available or creating and caching a new one otherwise. This ensures the tool is only instantiated once per unique agent across multiple calls.*


### build_text_envelope (method, L235-L236, parent: DiscussionAdapter)

> *Summary: This method constructs a standardized message envelope by calling a default implementation. It accepts channel ID, sender ID, and the message text as primary inputs, optionally including an audience and causation ID for context.*


### build_packet_envelope (method, L238-L257, parent: DiscussionAdapter)

> *Summary: This method constructs a standardized packet envelope by forwarding provided communication details—including channel ID, sender ID, and message body—to a default implementation. It accepts optional metadata like handoff instructions, context sets, audience lists, and causation IDs to enrich the resulting packet structure.*

