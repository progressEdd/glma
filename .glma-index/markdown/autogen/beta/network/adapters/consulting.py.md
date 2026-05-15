# autogen/beta/network/adapters/consulting.py

2 function(s): _is_channel_protocol_event, _is_task_event. 2 class(es): ConsultingState, ConsultingAdapter. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _is_channel_protocol_event | function |  |
| _is_task_event | function |  |
| ConsultingState | class |  |
| ConsultingAdapter | class |  |

## Chunks

### _is_channel_protocol_event (function, L71-L72)

> *Summary: Checks if an incoming `Envelope` object represents a predefined channel protocol event by checking its `event_type` against a constant set of known events. Returns a boolean indicating the match.*


### _is_task_event (function, L75-L76)

> *Summary: Checks if an incoming `Envelope` represents a task event by examining its `event_type`. Returns `True` if the type string begins with `"ag2.task."`, otherwise returns `False`.*


### ConsultingState (class, L80-L92)

> *Summary: This class holds a simplified state for tracking interactions within a consulting channel. It uses boolean flags to record if the initiator has sent a message and if the respondent has replied, allowing the system to determine when the conversation is complete.*


### ConsultingAdapter (class, L95-L307)

> *Summary: This adapter enforces a strict two-participant conversation flow: one initiator sends a message, and exactly one respondent replies. It validates the roles during channel creation and manages state transitions to automatically close upon receiving the reply, while caching the `say` tool for performance optimization.*


### __init__ (method, L103-L135, parent: ConsultingAdapter)

> *Summary: Initializes the adapter by setting up a per-client cache for `say_tool` to optimize repeated schema builds. It also configures a fixed manifest defining communication expectations, requiring exactly two participants with specific roles.*


### _initiator_id (method, L140-L141, parent: ConsultingAdapter)

> *Summary: Retrieves the unique identifier of the entity that initiated a channel by accessing the `creator_id` from the provided `ChannelMetadata`. This method returns the initiator's ID as a string.*


### _respondent_id (method, L144-L148, parent: ConsultingAdapter)

> *Summary: Extracts the `agent_id` of the first participant identified as a `RESPONDENT` within the provided channel metadata. If no respondent is found, it raises a `ProtocolError`.*


### initial_state (method, L152-L153, parent: ConsultingAdapter)

> *Summary: When provided with channel metadata, this method initializes and returns a new `ConsultingState` object. It serves as the starting point for the consulting process within the system.*


### fold (method, L155-L172, parent: ConsultingAdapter)

> *Summary: This method processes text-based envelopes to manage the conversational state between an initiator and a respondent. It updates the state by setting `initiator_sent` or `respondent_replied` flags based on whether the current envelope is received, provided it's not a protocol or task event.*


### validate_create (method, L174-L181, parent: ConsultingAdapter)

> *Summary: Ensures the provided channel metadata adheres to consulting protocol rules by verifying that there is precisely one initiator and one respondent among exactly two total participants. Raises a `ProtocolError` if these specific participant role and count requirements are not met.*


### validate_send (method, L183-L211, parent: ConsultingAdapter)

> *Summary: Checks if a message envelope adheres to the expected turn-taking sequence in a consulting channel, allowing protocol events and task envelopes to bypass validation. It raises a `ProtocolError` if the channel is already complete or if the sender ID does not match the expected initiator or respondent based on the current state.*


### on_accepted (method, L213-L230, parent: ConsultingAdapter)

> *Summary: When an event of type `EV_TEXT` is received, this method checks the current consulting state; if both initiator and respondent have sent messages, it transitions the channel to a closed state. Otherwise, it returns no change in state.*


### default_view_policy (method, L232-L237, parent: ConsultingAdapter)

> *Summary: This method returns a `FullTranscript` view policy when provided with channel metadata and a participant ID. It serves as the default behavior for determining what content a user can see within a channel.*


### extract_turn_input (method, L239-L240, parent: ConsultingAdapter)

> *Summary: This method delegates the extraction of turn input from an `envelope` object to a default implementation. It serves as a simple pass-through mechanism for retrieving structured data from the provided input container.*


### build_round_envelope (method, L242-L243, parent: ConsultingAdapter)

> *Summary: This method acts as a simple wrapper that delegates the construction of a round envelope to a default implementation. It accepts metadata, sender ID, reply information, events, current state, and a hub object as inputs to produce the resulting envelope structure.*


### render_envelope (method, L245-L246, parent: ConsultingAdapter)

> *Summary: This method delegates the rendering of an `envelope` object to a default implementation. It serves as a simple pass-through wrapper for serialization or formatting purposes.*


### tools_for (method, L248-L268, parent: ConsultingAdapter)

> *Summary: Determines which tools are available for a given participant based on the conversation's state and roles. It returns a list containing the "say" tool if the current participant is either the initiator before they send their prompt, or the respondent after the prompt has been sent but before they have replied. Otherwise, it returns an empty list.*


### _cached_say_tool (method, L270-L283, parent: ConsultingAdapter)

> *Summary: This method retrieves or creates a memoized "say" tool specific to a given client agent ID. It checks an internal cache using the `client.agent_id` and returns the cached tool if present, otherwise it generates and caches a new one before returning it.*


### build_text_envelope (method, L285-L286, parent: ConsultingAdapter)

> *Summary: This method constructs a standardized message envelope for text communication. It accepts channel and sender identifiers along with the message content and optional targeting or causal context parameters to return the fully formed envelope object.*


### build_packet_envelope (method, L288-L307, parent: ConsultingAdapter)

> *Summary: This method constructs a standardized packet envelope by forwarding provided communication details—including channel ID, sender ID, and message body—to a default implementation. It accepts optional metadata such as handoff instructions, context sets, audience lists, and causation IDs to enrich the resulting packet structure.*

