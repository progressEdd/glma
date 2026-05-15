# autogen/beta/network/adapters/base.py

6 function(s): default_extract_turn_input, default_build_round_envelope, default_render_envelope, default_tools_for, default_build_text_envelope, default_build_packet_envelope. 3 class(es): AdapterState, AdapterResult, ChannelAdapter. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AdapterState | class |  |
| AdapterResult | class |  |
| ChannelAdapter | class |  |
| default_extract_turn_input | function |  |
| default_build_round_envelope | function |  |
| default_render_envelope | function |  |
| default_tools_for | function |  |
| default_build_text_envelope | function |  |
| default_build_packet_envelope | function |  |

## Chunks

### AdapterState (class, L63-L68)

> *Summary: Defines a protocol that serves as a marker for concrete adapter states, indicating that specific implementations will define their own data structures. The hub treats this state opaquely, only passing it to certain lifecycle methods like `fold` or validation checks.*


### AdapterResult (class, L72-L81)

> *Summary: Represents the outcome an adapter signals to the hub after processing an envelope. It specifies the desired `next_state` for the channel and provides a reason (`auto_close_reason`) if the channel should automatically close.*


### ChannelAdapter (class, L84-L253)

> *Summary: Defines a protocol for channel adapters that dictates how different types of communication channels process events. It requires methods for state management (`initial_state`, `fold`), validation (`validate_create`, `validate_send`), and transforming data into LLM-consumable formats (`extract_turn_input`, `render_envelope`).*


### initial_state (method, L95-L97, parent: ChannelAdapter)

> *Summary: Generates an empty `AdapterState` based on provided `ChannelMetadata`. This method establishes the starting configuration for a new communication channel adapter.*


### fold (method, L99-L105, parent: ChannelAdapter)

> *Summary: This method deterministically updates the adapter's internal state by incorporating a new `Envelope`. It is designed to be pure, allowing for reliable state reconstruction from persistent logs.*


### validate_create (method, L107-L109, parent: ChannelAdapter)

> *Summary: Checks the provided `ChannelMetadata` to ensure it meets all necessary criteria for channel creation. It raises an exception if any validation rules are violated, such as incorrect participant counts or missing configuration parameters.*


### validate_send (method, L111-L121, parent: ChannelAdapter)

> *Summary: Checks if a given `Envelope` is permissible according to the protocol rules based on the current `AdapterState` and associated `ChannelMetadata`. It raises an error if the envelope violates the expected sequence or conditions before any folding operations occur.*


### on_accepted (method, L123-L133, parent: ChannelAdapter)

> *Summary: This method determines the next state transition after a channel acceptance has been processed by receiving metadata, an envelope, and the current adapter state as input. It returns an `AdapterResult` indicating the subsequent action.*


### default_view_policy (method, L135-L141, parent: ChannelAdapter)

> *Summary: Determines the standard view policy for a specific participant within a given channel. It takes channel metadata and a participant ID as input to return an appropriate `ViewPolicy`.*


### extract_turn_input (method, L143-L155, parent: ChannelAdapter)

> *Summary: Decodes an incoming `Envelope` to determine the specific input string, structured object, or list of objects that the next LLM should process during its turn. It returns `None` if the adapter is not designed to handle the envelope type.*


### build_round_envelope (method, L157-L177, parent: ChannelAdapter)

> *Summary: Constructs a standardized message envelope summarizing an agent interaction round. It takes metadata, sender/reply details, events, and state to produce either an `Envelope` containing the reply body or `None` if the round was silent.*


### render_envelope (method, L179-L192, parent: ChannelAdapter)

> *Summary: Converts an `Envelope` object into a string representation suitable for LLM visibility within view policies. It returns `None` if the envelope should be skipped during projection due to being non-substantive or malformed.*


### tools_for (method, L194-L213, parent: ChannelAdapter)

> *Summary: Determines which LLM tools an adapter makes available to a specific participant based on the current system state and client context. It returns a list of `Tool` objects, potentially filtering them based on turn-based logic or other state conditions.*


### build_text_envelope (method, L215-L233, parent: ChannelAdapter)

> *Summary: Creates a structured `Envelope` object specifically for transmitting text messages. It takes identifiers for the channel and sender, the message content, and optional targeting or causal context parameters.*


### build_packet_envelope (method, L235-L253, parent: ChannelAdapter)

> *Summary: Creates a structured packet envelope for network transmission using provided identifiers and payload. It supports optional routing metadata like handoffs, context sets, audience lists, and causation IDs to shape the final `Envelope` object.*


### default_extract_turn_input (function, L256-L265)

> *Summary: This function extracts the text content from an `Envelope` object, specifically checking for the `EV_TEXT` event type. It returns the extracted string if present and valid, otherwise it returns `None`.*


### default_build_round_envelope (function, L268-L291)

> *Summary: Constructs a standard `Envelope` containing text content if the reply has a non-empty body. It takes channel metadata, sender ID, the agent's reply, events, state, and a hub as input, returning an `Envelope` or `None`.*


### default_render_envelope (function, L294-L305)

> *Summary: This function extracts the text payload from an `Envelope` object if its event type is `EV_TEXT`. It returns the extracted string content or `None` for any other event type.*


### default_tools_for (function, L308-L320)

> *Summary: This function provides a default implementation for determining available tools, returning an empty list by default. It is intended to be overridden by specific adapters that need to provide channel-specific tool sets based on the client, metadata, state, and participant ID.*


### default_build_text_envelope (function, L323-L339)

> *Summary: Constructs a standard message envelope for sending text content. It takes channel and sender identifiers, the text payload, and optional audience or causation IDs to create an `Envelope` object with event type `EV_TEXT`.*


### default_build_packet_envelope (function, L342-L373)

> *Summary: Constructs a standard `Envelope` for emitting an `EV_PACKET`, incorporating the provided body and optional routing information derived from a `handoff`. It merges additional metadata like context or audience into the packet's event data structure.*

