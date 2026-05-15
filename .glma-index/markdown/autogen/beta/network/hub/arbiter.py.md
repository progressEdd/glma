# autogen/beta/network/hub/arbiter.py

1 function(s): _match_any. 5 class(es): Allow, Deny, HubArbiter, BaseHubArbiter, RuleBasedArbiter. 18 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Allow | class |  |
| Deny | class |  |
| HubArbiter | class |  |
| _match_any | function |  |
| BaseHubArbiter | class |  |
| RuleBasedArbiter | class |  |

## Chunks

### Allow (class, L50-L51)

> *Summary: Represents a decision indicating that an action is permitted within the system's arbitration logic. It serves as a simple status object signaling approval.*


### Deny (class, L55-L64)

> *Summary: Represents a decision indicating that an action is not permitted within the network hub. It stores a human-readable `reason` and specifies which subclass of `NetworkError` to raise upon denial, defaulting to `AccessDeniedError`.*


### HubArbiter (class, L71-L162)

> *Summary: Defines an interface for decision-making logic that a hub uses before committing actions like sending or registering. It requires implementations to provide asynchronous methods to authorize outbound sends, check inbox capacity per recipient, gate individual dispatches, and manage channel creation based on various inputs.*


### authorize_send (method, L82-L95, parent: HubArbiter)

> *Summary: This method determines if an envelope can be sent by checking outbound access rules against a sender and validating the delegation depth limit. It takes an `Envelope`, `Passport` sender, a `Rule`, and a list of recipient `Passports` as input, returning a `Decision`.*


### authorize_inbox (method, L97-L110, parent: HubArbiter)

> *Summary: Checks if a recipient's inbox has capacity before allowing an envelope to be posted. It takes the envelope, recipient details, and current pending count as input, returning a `Decision` that either permits or denies sending based on the defined rules.*


### authorize_dispatch (method, L112-L124, parent: HubArbiter)

> *Summary: Determines whether a notification should be sent to a specific recipient based on provided context. It accepts an envelope, sender, recipient, and a recipient rule, returning a `Decision` that dictates if dispatch proceeds or is silently skipped for that single recipient.*


### authorize_channel_open (method, L126-L140, parent: HubArbiter)

> *Summary: This method determines if a new channel creation request should proceed by validating permissions and resource limits. It checks each invited user's inbound access against the creator's identity and ensures the creator has not exceeded their maximum concurrent channels.*


### authorize_register (method, L142-L148, parent: HubArbiter)

> *Summary: This method determines if a registration should be allowed by checking provided passport, resume, and rule objects. It currently defaults to allowing the registration without specific validation logic.*


### resolve_unknown_audience (method, L150-L162, parent: HubArbiter)

> *Summary: This asynchronous method acts as a federation hook to handle audience members unknown to the hub. It accepts an `Envelope` and a list of `unknown_ids`, returning either `None` (to drop them) or a list of agent IDs for re-delivery by a federated arbiter.*


### _match_any (function, L165-L167)

> *Summary: Checks if a given string name matches any pattern within a list using case-sensitive glob matching. Returns `True` immediately upon finding the first match or if the list contains a wildcard pattern that matches everything.*


### BaseHubArbiter (class, L170-L234)

> *Summary: This base class provides a no-operation implementation for network arbitration logic, returning `Allow()` by default for all authorization checks. Subclasses should override specific methods to implement custom rules based on inputs like envelopes, passports, and associated rules.*


### authorize_send (method, L183-L190, parent: BaseHubArbiter)

> *Summary: This method unconditionally permits sending an `Envelope` from a specified `Sender` to a list of `Recipients`, provided the sender adheres to the given `Rule`. It always returns an `Allow()` decision without performing any actual authorization checks.*


### authorize_inbox (method, L192-L199, parent: BaseHubArbiter)

> *Summary: This method unconditionally permits an incoming message envelope destined for a specific recipient based on provided rules and current pending counts. It always returns an `Allow` decision without performing any complex authorization checks.*


### authorize_dispatch (method, L201-L208, parent: BaseHubArbiter)

> *Summary: This method unconditionally returns an `Allow` decision, effectively permitting the dispatch of a message envelope from a sender to a recipient based on a provided rule. It accepts the envelope, sender, recipient, and recipient rule as inputs.*


### authorize_channel_open (method, L210-L219, parent: BaseHubArbiter)

> *Summary: This method determines if a channel opening request should be permitted based on provided manifest details, creator identity and rules, invited participants, their associated rules, and the count of active channels for the creator. It currently unconditionally returns an `Allow()` decision.*


### authorize_register (method, L221-L227, parent: BaseHubArbiter)

> *Summary: This method unconditionally grants permission by returning an `Allow` decision, regardless of the provided `Passport`, `Resume`, or `Rule` inputs. It serves as a simple authorization gatekeeper within the system.*


### resolve_unknown_audience (method, L229-L234, parent: BaseHubArbiter)

> *Summary: This asynchronous method takes an `Envelope` and a list of unknown IDs as input. It currently returns `None`, indicating it does not perform any audience resolution logic in its present state.*


### RuleBasedArbiter (class, L237-L340)

> *Summary: This class enforces communication rules by checking various authorization requests based on sender/recipient identities, associated access rules, and envelope metadata. It determines if sending, receiving, opening channels, or registering is permitted by applying inbound/outbound restrictions and capacity limits.*


### authorize_send (method, L245-L268, parent: RuleBasedArbiter)

> *Summary: Checks if a sender is permitted to send an envelope to a list of recipients based on predefined access rules and message depth limits. It returns `Allow()` if all checks pass, or a specific `Deny()` decision otherwise.*


### authorize_inbox (method, L270-L284, parent: RuleBasedArbiter)

> *Summary: Checks if a recipient's inbox has reached its configured maximum pending limit based on the provided rule and current count. Returns `Deny` with an `InboxFull` error if capacity is exceeded, otherwise returns `Allow`.*


### authorize_dispatch (method, L286-L295, parent: RuleBasedArbiter)

> *Summary: Checks if the sender's name is listed in the recipient's allowed inbound sources defined by a rule. Returns an `Allow` decision if the sender matches the rule, otherwise returns a `Deny` decision with a specific reason.*


### authorize_channel_open (method, L297-L324, parent: RuleBasedArbiter)

> *Summary: This method validates permissions for opening a new channel by first checking if each invited participant accepts inbound connections from the creator. It then enforces a concurrency limit on the creator based on their associated rules before returning an `Allow` or `Deny` decision.*


### authorize_register (method, L326-L332, parent: RuleBasedArbiter)

> *Summary: This method unconditionally grants permission by returning an `Allow` decision. It accepts a `Passport`, `Resume`, and `Rule` object as input to determine authorization.*


### resolve_unknown_audience (method, L334-L340, parent: RuleBasedArbiter)

> *Summary: When provided with an envelope and a list of unknown IDs, this method returns `None`, effectively dropping the unknown IDs in single-hub operation mode.*

