# autogen/beta/network/adapters/workflow.py

8 function(s): _is_channel_protocol_event, _is_task_event, _is_substantive, _packet_turn_text, _packet_text, _resolve_routing, _extract_handoff, _extract_call_reason. 2 class(es): WorkflowState, WorkflowAdapter. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _is_channel_protocol_event | function |  |
| _is_task_event | function |  |
| _is_substantive | function |  |
| WorkflowState | class |  |
| WorkflowAdapter | class |  |
| _packet_turn_text | function |  |
| _packet_text | function |  |
| _resolve_routing | function |  |
| _extract_handoff | function |  |
| _extract_call_reason | function |  |

## Chunks

### _is_channel_protocol_event (function, L94-L95)

> *Summary: Checks if an incoming `Envelope`'s event type matches any predefined channel protocol events. Returns a boolean indicating whether the event is part of the established protocol.*


### _is_task_event (function, L98-L99)

> *Summary: Checks if an incoming `Envelope` represents a task event by inspecting its `event_type`. Returns `True` if the type string begins with `"ag2.task."`, otherwise returns `False`.*


### _is_substantive (function, L102-L106)

> *Summary: Determines if an `Envelope` represents a substantive turn-advancing event by checking if its type is either text (`EV_TEXT`) or a packet (`EV_PACKET`), excluding channel protocol or task events. Returns `True` only for these specific communication types.*


### WorkflowState (class, L110-L130)

> *Summary: This class encapsulates the essential state for a workflow channel, storing participant order, turn history, and context variables. It maintains a snapshot of the transition graph data to allow stateless operation across different channels.*


### WorkflowAdapter (class, L133-L454)

> *Summary: This class manages orchestrated multi-party communication based on a defined state transition graph provided in its configuration knobs. It processes incoming envelopes to update the workflow state—handling context changes and determining the next speaker via graph traversal or explicit handoffs—and generates outgoing packets representing the round's outcome.*


### __init__ (method, L141-L160, parent: WorkflowAdapter)

> *Summary: Initializes a workflow adapter by creating a `ChannelManifest` defining the structure and constraints for the workflow. This manifest specifies required participants, expected turn timings with different violation behaviors, and uses a transition graph as its core schema.*


### initial_state (method, L164-L187, parent: WorkflowAdapter)

> *Summary: Constructs the starting state for a workflow by parsing graph data from metadata and validating participant order against the specified initial speaker. It returns a `WorkflowState` object containing the ordered participants, the designated first speaker, creator ID, graph structure, and initial context variables.*


### fold (method, L189-L260, parent: WorkflowAdapter)

> *Summary: Processes an incoming `Envelope` against the current `WorkflowState`, updating context variables, advancing turn bookkeeping, and determining the next speaker. It either accepts a pre-resolved target from the envelope or uses internal graph rules to decide the subsequent state.*


### validate_create (method, L262-L278, parent: WorkflowAdapter)

> *Summary: Ensures a workflow configuration is valid by checking for at least two participants and verifying that the provided graph data is a correctly structured `TransitionGraph`. It raises errors if participant counts are too low, the graph data format is incorrect, or the specified initial speaker is not among the registered participants.*


### validate_send (method, L280-L302, parent: WorkflowAdapter)

> *Summary: Checks incoming messages against workflow rules based on the event type and current state. It ensures context setting events come from authorized participants and enforces turn-taking order for substantive messages.*


### on_accepted (method, L304-L327, parent: WorkflowAdapter)

> *Summary: Checks if a workflow should terminate based on incoming metadata and current state. It closes the channel if no next speaker is expected or if the turn count exceeds a predefined maximum limit from the transition graph.*


### default_view_policy (method, L329-L335, parent: WorkflowAdapter)

> *Summary: Calculates a default view policy based on channel metadata and participant ID. It returns a `WindowedSummary` object whose window size is determined by the maximum of four or twice the number of participants in the channel.*


### extract_turn_input (method, L337-L347, parent: WorkflowAdapter)

> *Summary: This method decodes an incoming `Envelope` to determine the next speaker's prompt string. It handles two event types, returning the text directly for `EV_TEXT` or concatenating routing and body data for `EV_PACKET`.*


### build_round_envelope (method, L349-L392, parent: WorkflowAdapter)

> *Summary: Constructs a network `Envelope` packet for a workflow round by packaging the reply content and determined routing intent derived from local events. It returns `None` if the round is silent (no body and no routing tool fired).*


### render_envelope (method, L394-L401, parent: WorkflowAdapter)

> *Summary: If the input event is an `EV_PACKET`, it processes and returns the corresponding text representation using a dedicated helper function; otherwise, it delegates rendering to a default envelope handler.*


### tools_for (method, L403-L412, parent: WorkflowAdapter)

> *Summary: This method returns a default set of tools because the workflow adapter itself provides no specific tooling. Handoff routing is managed externally via user-defined `@tool` functions that return `Handoff` objects.*


### build_text_envelope (method, L414-L418, parent: WorkflowAdapter)

> *Summary: This method constructs a standardized message envelope for plain text inputs. It takes channel and sender identifiers along with the text content, optionally including an audience or causation ID, before passing it to a default builder function.*


### build_packet_envelope (method, L420-L441, parent: WorkflowAdapter)

> *Summary: This method constructs a standardized packet envelope by wrapping the provided body with metadata like channel ID, sender ID, and optional routing information. It delegates the actual construction to `default_build_packet_envelope`, incorporating fields such as handoff, context set, audience, and causation ID.*


### _select (method, L446-L454, parent: WorkflowAdapter)

> *Summary: Determines the next transition by iterating through sorted transitions based on priority and checking if their conditions are met using the provided state and envelope. If a matching transition is found, it resolves to that target; otherwise, it defaults to the graph's designated default target.*


### _packet_turn_text (function, L460-L487)

> *Summary: Generates a conversational turn prompt string from an `Envelope` by combining a handoff signal line (if present in the routing data) and the message body, separated by a newline. It ensures the output reflects the state as seen by the next speaker after a handoff event.*


### _packet_text (function, L490-L518)

> *Summary: Generates a string representation of an `Envelope` for display by combining a handoff signal line (if present and the routing kind is "handoff") with the envelope's body. It returns `None` if both components are empty, otherwise it joins the parts with a newline character.*


### _resolve_routing (function, L521-L577)

> *Summary: Determines the packet's routing by iterating through agent events to find a matching tool call and result. It prioritizes dynamic handoffs from results; otherwise, it checks if the tool name matches a static rule defined in the provided transition graph. If no specific routing is found, it defaults to a text kind.*


### _extract_handoff (function, L580-L588)

> *Summary: This function inspects a `ToolResultEvent` to find if any of its parts contain a `Handoff` object within the data payload. It returns the found `Handoff` instance or `None` if no such structure exists in the result.*


### _extract_call_reason (function, L591-L609)

> *Summary: Parses the JSON arguments from a `ToolCallEvent` to extract a specific "reason" string. It safely handles cases where the input is invalid, not a dictionary, or lacks the expected key, returning an empty string upon failure.*

