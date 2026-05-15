# autogen/beta/network/rule.py

1 function(s): parse_duration. 6 class(es): ChannelTypeAccess, AccessBlock, RateBlock, InboxBlock, LimitsBlock, Rule. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| parse_duration | function |  |
| ChannelTypeAccess | class |  |
| AccessBlock | class |  |
| RateBlock | class |  |
| InboxBlock | class |  |
| LimitsBlock | class |  |
| Rule | class |  |

## Chunks

### parse_duration (function, L37-L52)

> *Summary: Converts a string or integer representing a time duration into total seconds. It handles suffixes like 's', 'm', 'h', and 'd' for various units, defaulting to the input value if it's an integer or empty string.*


### ChannelTypeAccess (class, L56-L58)

> *Summary: This class defines access control lists for channels, specifying which types are allowed to initiate (`initiate`) and accept (`accept`) connections. By default, both lists permit all channel types represented by `"*"`.*


### AccessBlock (class, L62-L65)

> *Summary: Defines a structure to control network access by specifying allowed inbound sources and outbound destinations using glob patterns. It also includes configuration for permitted channel types.*


### RateBlock (class, L69-L77)

> *Summary: This class holds configuration values for token-bucket rate limiting, specifically defining `per_minute` and `burst` capacities. These settings are stored on a rule but do not enforce the limit themselves; setting `per_minute` to zero disables the limiter.*


### InboxBlock (class, L81-L96)

> *Summary: Defines an inbox capacity policy controlling how incoming messages are handled when the queue is full. It accepts configuration for maximum pending items, overflow behavior (defaulting to rejection), and a soft threshold for backpressure signaling.*


### LimitsBlock (class, L100-L117)

> *Summary: This structure defines concurrency limits and default time-to-live (TTL) settings for channels and tasks. It holds configuration values like maximum concurrent counts, default TTL strings, rate limiting rules, and inbox configurations.*


### Rule (class, L121-L149)

> *Summary: This class serializes and deserializes rule configurations. It converts the object to a dictionary using `to_dict()` or reconstructs an instance from a dictionary input via `from_dict()`, handling nested structures for access and limits blocks.*


### to_dict (method, L126-L127, parent: Rule)

> *Summary: Converts the object's state into a standard Python dictionary using `asdict`. This allows for easy serialization or data exchange of the object's attributes.*


### from_dict (method, L130-L149, parent: Rule)

> *Summary: Constructs a `Rule` object from a dictionary by recursively parsing nested structures for access controls and rate limits. It transforms dictionaries representing specific blocks (like `ChannelTypeAccess`, `RateBlock`, `InboxBlock`) into their respective typed objects before instantiating the final rule.*

