# autogen/agentchat/eligibility_policy.py

3 class(es): SelectionContext, AgentEligibilityPolicy, AgentDescriptionGuard. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SelectionContext | class |  |
| AgentEligibilityPolicy | class |  |
| AgentDescriptionGuard | class |  |

## Chunks

### SelectionContext (class, L19-L65)

> *Summary: Provides a minimal context object for eligibility policies during agent selection within a group chat. It holds the current message round, the name of the last speaker, and a tuple containing all registered participant names. The constructor ensures that the `participants` attribute is always normalized to an immutable tuple.*


### __post_init__ (method, L56-L65, parent: SelectionContext)

> *Summary: Ensures the `participants` attribute is always a tuple after initialization, raising an error if a raw string is provided to prevent unintended character iteration. It converts any iterable input into a fixed-size tuple for consistent internal state management.*


### AgentEligibilityPolicy (class, L70-L110)

> *Summary: Defines a contract for runtime filters used during speaker selection in group chats. Implementations must provide an `is_eligible` method that takes an agent and context, returning `True` if the agent should remain a candidate or `False` to exclude it. Multiple registered policies are combined using logical AND semantics.*


### is_eligible (method, L100-L110, parent: AgentEligibilityPolicy)

> *Summary: Determines if a given `Agent` should be considered for inclusion based on the provided `SelectionContext`. It returns a boolean indicating eligibility for the current selection round.*


### AgentDescriptionGuard (class, L117-L189)

> *Summary: This class wraps an agent to conditionally modify its description, prepending `[UNAVAILABLE]` when the agent is offline and removing it upon recovery. It ensures thread-safe state management by tracking the original description to restore the correct value after marking availability.*


### __init__ (method, L134-L137, parent: AgentDescriptionGuard)

> *Summary: Initializes the policy by storing a reference to an `Agent`, creating a thread lock for synchronization, and setting an initial state for the agent's description. This setup prepares the policy to manage interactions with the specified agent safely across threads.*


### mark_unavailable (method, L139-L152, parent: AgentDescriptionGuard)

> *Summary: This method prepends `[UNAVAILABLE]` to an agent's description, ensuring the operation is idempotent and thread-safe using a lock. It safely handles cases where the original description might be `None` by temporarily storing it for later restoration.*


### mark_available (method, L154-L189, parent: AgentDescriptionGuard)

> *Summary: This method restores an agent's description by removing the `[UNAVAILABLE]` prefix from its current value, provided it was previously marked as unavailable. It uses a lock to ensure thread safety and preserves any text appended after the prefix when restoring the description.*

