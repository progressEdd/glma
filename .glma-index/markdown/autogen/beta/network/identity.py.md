# autogen/beta/network/identity.py

7 class(es): CostProfile, AuthBlock, Passport, ResumeExample, ObservedStat, Resume, AgentRuntime. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CostProfile | class |  |
| AuthBlock | class |  |
| Passport | class |  |
| ResumeExample | class |  |
| ObservedStat | class |  |
| Resume | class |  |
| AgentRuntime | class |  |

## Chunks

### CostProfile (class, L43-L48)

> *Summary: Defines optional hints for billing or routing, allowing specification of input/output token costs and a latency preference ("fast", "balanced", or "deep"). These fields are not validated by the current version.*


### AuthBlock (class, L52-L59)

> *Summary: Defines the structure for validating an identity during a connection handshake. It holds metadata such as the validation scheme, issuer, audience, key fingerprint, and arbitrary claims.*


### Passport (class, L63-L112)

> *Summary: Represents an immutable record containing identity and billing details for a registration, tracking attributes like name, provider, cost, and participant type (`kind`). It can be initialized from a dictionary via `from_dict` and provides a resolved `effective_kind` property that defaults to `"agent"` if the stored kind is `None`.*


### __post_init__ (method, L91-L95, parent: Passport)

> *Summary: After initialization, this method validates that the `kind` attribute, if present, belongs to a predefined set of acceptable passport types. It raises a `ValueError` immediately upon finding an invalid kind instead of allowing silent data corruption later in the process.*


### to_dict (method, L97-L98, parent: Passport)

> *Summary: Converts the object's state into a standard Python dictionary representation using `asdict`. This allows for easy serialization or data exchange of the object's attributes.*


### from_dict (method, L101-L107, parent: Passport)

> *Summary: Constructs an instance of the class from a dictionary by recursively converting nested "auth" and "cost" dictionaries into their respective object types before instantiation. It takes a dictionary as input and returns a fully initialized object matching the class structure.*


### effective_kind (method, L110-L112, parent: Passport)

> *Summary: Determines the final type of an identity, defaulting to `"agent"` if the stored `kind` attribute is null. This method returns a `PassportKind` enum value based on the instance's state.*


### ResumeExample (class, L116-L122)

> *Summary: This class structure holds metadata for a resume example, including its title, final outcome status, and associated identifiers like task and channel IDs. It also stores optional timestamps and any supplementary notes related to the example's execution.*


### ObservedStat (class, L126-L133)

> *Summary: Stores a per-capability track record derived from the hub, tracking counts for total observations, completions, failures, and expirations. It also holds an optional value for the 50th percentile latency in milliseconds.*


### Resume (class, L137-L166)

> *Summary: Represents a mutable profile containing claimed skills, domains, and examples, while tracking observed performance metrics. It allows serialization to and deserialization from dictionaries, handling nested `ResumeExample` and `ObservedStat` objects during conversion.*


### to_dict (method, L154-L155, parent: Resume)

> *Summary: Converts the object's state into a standard Python dictionary representation using `asdict`. This allows for serialization or easy data exchange of the instance's attributes.*


### from_dict (method, L158-L166, parent: Resume)

> *Summary: Converts a dictionary representation into an instance of the `Resume` class. It recursively transforms nested dictionaries within "examples" and "observed" fields into their respective object types before instantiation.*


### AgentRuntime (class, L170-L181)

> *Summary: This structure maintains per-connection state for a registered agent, tracking its ID, binding type, target endpoint, reachability status, and the time of its last heartbeat. It serves as bookkeeping data that is updated on every heartbeat but should not be relied upon immediately after a hub failover.*

