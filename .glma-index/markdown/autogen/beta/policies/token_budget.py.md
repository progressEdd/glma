# autogen/beta/policies/token_budget.py

1 class(es): TokenBudgetPolicy. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TokenBudgetPolicy | class |  |

## Chunks

### TokenBudgetPolicy (class, L13-L49)

> *Summary: This policy enforces a token limit by estimating character counts from provided events and prompts. If the total size exceeds the configured maximum, it truncates the event list, prioritizing retention of the most recent events while ensuring tool pairings are maintained.*


### __init__ (method, L21-L23, parent: TokenBudgetPolicy)

> *Summary: Initializes a token budget tracker by calculating the maximum allowed characters based on a provided token limit and character-to-token ratio. It also sets a flag to determine if the budget tracking should be visible externally.*


### apply (method, L25-L49, parent: TokenBudgetPolicy)

> *Summary: If the total character count of provided events exceeds a predefined limit, this method truncates the event list by retaining only the most recent events until the token budget is met. It returns the original prompts along with the newly filtered and potentially adjusted list of events.*

