# autogen/beta/policies/episodic_memory.py

1 class(es): EpisodicMemoryPolicy. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| EpisodicMemoryPolicy | class |  |

## Chunks

### EpisodicMemoryPolicy (class, L12-L53)

> *Summary: This policy retrieves the most recent conversation summaries from a knowledge store and injects them into the system prompt to provide the agent with context from past episodes. It accepts existing prompts, events, and a context object containing dependencies like the `KnowledgeStore`, returning modified prompts and unchanged events.*


### __init__ (method, L21-L23, parent: EpisodicMemoryPolicy)

> *Summary: Initializes the episodic memory with a maximum episode limit and a flag determining its transparency. These parameters control how many episodes are tracked and whether the memory state is exposed.*


### apply (method, L25-L53, parent: EpisodicMemoryPolicy)

> *Summary: Retrieves and prepends summaries of recent conversations from a knowledge store to the input prompts if available. It returns the augmented list of prompts along with the original events.*

