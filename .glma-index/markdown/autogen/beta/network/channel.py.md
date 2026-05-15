# autogen/beta/network/channel.py

1 function(s): is_terminal_channel_state. 7 class(es): ChannelState, ParticipantRole, ParticipantSchema, Expectation, ChannelManifest, Participant, ChannelMetadata. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ChannelState | class |  |
| is_terminal_channel_state | function |  |
| ParticipantRole | class |  |
| ParticipantSchema | class |  |
| Expectation | class |  |
| ChannelManifest | class |  |
| Participant | class |  |
| ChannelMetadata | class |  |

## Chunks

### ChannelState (class, L37-L48)

> *Summary: Defines the possible lifecycle states for a communication channel using an enumeration. These states—such as `PENDING`, `ACTIVE`, and `CLOSED`—govern how the channel progresses through its operational phases within the system's state machine.*


### is_terminal_channel_state (function, L57-L59)

> *Summary: Checks if a given `ChannelState` belongs to a predefined set of terminal states. Returns `True` if the channel is in a final state where it cannot receive further envelopes, and `False` otherwise.*


### ParticipantRole (class, L62-L71)

> *Summary: Defines enumerated string constants representing the roles a participant can hold within a channel. These roles, such as `INITIATOR`, `RESPONDENT`, and `PARTICIPANT`, dictate interaction patterns for different types of discussions.*


### ParticipantSchema (class, L75-L80)

> *Summary: Defines a schema structure to enforce constraints on participants, specifying minimum and maximum counts along with an allowed list of roles. It holds configuration for participant limits and role validation within a system context.*


### Expectation (class, L84-L96)

> *Summary: Defines a contract structure used by the hub to evaluate communication expectations based on Write-Ahead Logs and clock time. It specifies which built-in evaluation logic applies, how violations should be handled (e.g., audit, auto\_close), and optionally targets specific roles or agents.*


### ChannelManifest (class, L100-L126)

> *Summary: This data structure defines the configuration and metadata for a communication channel, specifying its adapter type, version, participant requirements, and operational policies. It provides methods to serialize itself into a dictionary or reconstruct an instance from one.*


### to_dict (method, L116-L117, parent: ChannelManifest)

> *Summary: Converts the object's state into a standard Python dictionary representation using `asdict`. This allows for serialization or easy data exchange of the channel's attributes.*


### from_dict (method, L120-L126, parent: ChannelManifest)

> *Summary: Converts a dictionary representation into an instance of the `ChannelManifest` class. It deserializes nested participant dictionaries and transforms expectation lists from dictionaries into structured objects before instantiation.*


### Participant (class, L130-L150)

> *Summary: Represents a participant in a network channel, storing its ID, role, sequence order, and join time. It provides methods to serialize the object into a dictionary and reconstruct an instance from one.*


### to_dict (method, L136-L142, parent: Participant)

> *Summary: Converts the channel object into a dictionary representation containing its agent ID, role value, order, and join timestamp. This serialization is useful for transmitting channel state data.*


### from_dict (method, L145-L150, parent: Participant)

> *Summary: Constructs a `Participant` object from a dictionary input by extracting and converting the "role" string into a `ParticipantRole` enum. It then instantiates the class using the modified payload data.*


### ChannelMetadata (class, L154-L226)

> *Summary: This class serves as a mutable record tracking the lifecycle and configuration of a communication channel. It stores core metadata like participants, state, creation details, and adapter-specific settings, providing methods to serialize/deserialize itself from dictionaries and check for terminal states.*


### to_dict (method, L188-L205, parent: ChannelMetadata)

> *Summary: Converts the channel object into a serializable dictionary representation. It aggregates all internal attributes, including nested objects like `manifest` and lists of participants, into a standard Python dictionary structure.*


### from_dict (method, L208-L220, parent: ChannelMetadata)

> *Summary: Constructs a `ChannelMetadata` object from a dictionary input by recursively converting nested dictionaries into structured objects like `ChannelManifest`, `Participant`, and `ChannelState`. It handles the deserialization of complex data structures contained within the provided dictionary.*


### participant_ids (method, L222-L223, parent: ChannelMetadata)

> *Summary: Retrieves a list of string identifiers corresponding to all agents currently participating in the channel. It iterates over the internal `participants` collection and extracts each agent's unique ID.*


### is_terminal (method, L225-L226, parent: ChannelMetadata)

> *Summary: Checks the current state of the channel against a predefined terminal condition to determine if the process should stop. It returns a boolean indicating whether the channel has reached its final state.*

