# autogen/beta/network/client/plugin.py

2 class(es): NetworkContextPolicy, NetworkPlugin. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| NetworkContextPolicy | class |  |
| NetworkPlugin | class |  |

## Chunks

### NetworkContextPolicy (class, L48-L69)

> *Summary: This policy prepends a network-aware prefix to all prompts sent to an LLM call. It takes the current list of prompts and events as input, returning the modified prompt list with the agent's identity included at the start.*


### __init__ (method, L58-L60, parent: NetworkContextPolicy)

> *Summary: Initializes the object by storing a reference to an `AgentClient` instance provided during construction. This method has no observable side effects other than setting this internal attribute.*


### apply (method, L62-L69, parent: NetworkContextPolicy)

> *Summary: Prepends a personalized greeting containing the client's name and agent ID to a list of input prompts. It returns the modified prompt list along with the original list of events.*


### NetworkPlugin (class, L72-L108)

> *Summary: This plugin injects core network-level tools like `peers`, `channels`, and `tasks` into an agent's toolset upon registration with a client. It also attaches a specific context policy to the agent, enabling interaction within the network environment.*


### __init__ (method, L88-L98, parent: NetworkPlugin)

> *Summary: Initializes the object by setting up a set of specialized tools—including delegates, peers, channels, tasks, and context accessors—all derived from an injected `AgentClient` instance. This allows the object to interact with various components of the agent system via these provided tool interfaces.*


### register (method, L100-L108, parent: NetworkPlugin)

> *Summary: Attaches the client's network context policy to a specified agent. This method ensures the necessary tooling and assembly policies are wired onto the target agent for network interaction.*

