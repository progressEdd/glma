# autogen/beta/network/adapters/conversation.py

2 function(s): _is_channel_protocol_event, _is_task_event. 2 class(es): ConversationState, ConversationAdapter. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _is_channel_protocol_event | function |  |
| _is_task_event | function |  |
| ConversationState | class |  |
| ConversationAdapter | class |  |

## Chunks

### _is_channel_protocol_event (function, L70-L71)

> *Summary: Checks if an incoming `Envelope`'s event type matches any predefined channel protocol events. Returns a boolean indicating whether the event is part of the established communication protocol.*


### _is_task_event (function, L74-L75)

> *Summary: Checks if an incoming `Envelope` represents a task event by examining its `event_type`. Returns `True` if the type string begins with `"ag2.task."`, otherwise returns `False`.*


### ConversationState (class, L79-L89)

> *Summary: This class maintains the essential bookkeeping for a conversation channel, tracking metrics like the total number of turns and identifiers for the last speaker and envelope. It serves as a folded state representation, meaning it doesn't enforce turn-by-turn ordering constraints during processing.*


### ConversationAdapter (class, L92-L228)

> *Summary: Manages a bidirectional, two-participant conversation flow by tracking turns and validating message integrity. It processes text events to update the state, provides tools for participants (like `say`), and defaults to a windowed summary view policy.*


### __init__ (method, L100-L119, parent: ConversationAdapter)

> *Summary: Initializes a conversation adapter by setting up an internal cache and defining a `ChannelManifest`. This manifest specifies the conversation type, requires exactly two participants (initiator and respondent), and sets expectations like a maximum silence duration.*


### initial_state (method, L123-L124, parent: ConversationAdapter)

> *Summary: Creates a default `ConversationState` object using the provided channel metadata. This method initializes the state for a new conversation context.*


### fold (method, L126-L135, parent: ConversationAdapter)

> *Summary: This method updates the conversation state only when an incoming envelope is a text event and not a channel or task protocol message. It increments the turn count and records the sender and envelope IDs from the received text envelope.*


### validate_create (method, L137-L144, parent: ConversationAdapter)

> *Summary: Ensures a conversation setup is valid by checking that the provided metadata contains exactly two participants, specifically one designated as an initiator and one as a respondent. It raises a `ProtocolError` if these participant roles or counts are incorrect.*


### validate_send (method, L146-L163, parent: ConversationAdapter)

> *Summary: Ensures that an incoming message is a text event and originates from one of the authorized participants within the conversation's channel metadata. If these conditions are not met, it raises a `ProtocolError` to enforce communication rules.*


### on_accepted (method, L165-L173, parent: ConversationAdapter)

> *Summary: This method handles the acceptance of content within a conversation flow. It immediately returns an empty result, indicating that accepting content does not trigger any state transition initiated by the adapter itself.*


### default_view_policy (method, L175-L180, parent: ConversationAdapter)

> *Summary: This method generates a `ViewPolicy` by returning a `WindowedSummary`, which is configured to summarize the last $\text{N}$ messages based on a predefined default. It takes channel metadata and a participant ID as input to determine this policy.*


### extract_turn_input (method, L182-L183, parent: ConversationAdapter)

> *Summary: This method delegates the extraction of input for a specific turn to a default implementation. It takes an `envelope` object as input and returns the extracted turn data.*


### build_round_envelope (method, L185-L186, parent: ConversationAdapter)

> *Summary: This method constructs a standardized envelope for a conversation round by passing along various contextual data like metadata, sender ID, and event lists. It delegates the actual construction to a predefined helper function.*


### render_envelope (method, L188-L189, parent: ConversationAdapter)

> *Summary: This method delegates the rendering of an `envelope` object to a predefined default implementation. It serves as a simple pass-through wrapper for serialization or formatting purposes.*


### tools_for (method, L191-L195, parent: ConversationAdapter)

> *Summary: Returns a list containing the cached "say" tool for the given client, as conversation turns are not ordered and both participants have access to this function. The method relies on internal memoization per client for efficient tool resolution.*


### _cached_say_tool (method, L197-L204, parent: ConversationAdapter)

> *Summary: Retrieves a memoized "say" tool for a given client agent ID, returning a previously generated instance if available or creating and caching a new one otherwise. This ensures the tool is only instantiated once per unique agent across multiple calls.*


### build_text_envelope (method, L206-L207, parent: ConversationAdapter)

> *Summary: Constructs a standardized message envelope for communication by packaging the channel ID, sender ID, and text content. It accepts optional parameters like an audience or causation ID to enrich the message structure before returning the final envelope object.*


### build_packet_envelope (method, L209-L228, parent: ConversationAdapter)

> *Summary: This method constructs a standardized packet envelope by forwarding provided communication details—including channel ID, sender ID, and message body—to a default builder function. It accepts optional metadata like handoff instructions, context sets, audience lists, and causation IDs to enrich the resulting packet structure.*

