# autogen/beta/policies/working_memory.py

1 class(es): WorkingMemoryPolicy. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WorkingMemoryPolicy | class |  |

## Chunks

### WorkingMemoryPolicy (class, L12-L36)

> *Summary: This policy retrieves the agent's persistent state from a knowledge store and injects it into the system prompt context. It takes existing prompts, events, and context as input, returning the augmented list of prompts if memory content is found.*


### apply (method, L22-L36, parent: WorkingMemoryPolicy)

> *Summary: Retrieves existing knowledge from a `KnowledgeStore` and prepends it to the input prompts if found. It returns the potentially augmented list of prompts along with the original events.*

