# autogen/graph_utils.py

4 function(s): has_self_loops, check_graph_validity, invert_disallowed_to_allowed, visualize_speaker_transitions_dict.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| has_self_loops | function |  |
| check_graph_validity | function |  |
| invert_disallowed_to_allowed | function |  |
| visualize_speaker_transitions_dict | function |  |

## Chunks

### has_self_loops (function, L18-L27)

> *Summary: Determines if an agent is listed as a possible transition target for itself within a provided dictionary mapping agents to their allowed next agents. It returns `True` if any agent's name appears in its own list of allowed transitions.*


### check_graph_validity (function, L30-L112)

> *Summary: Validates a transition dictionary against a list of agents, ensuring correct structure and membership by raising `ValueError` on structural errors. It also issues warnings if agents are isolated, if the defined transitions don't cover all provided agents, or if any agent appears multiple times in a transition list.*


### invert_disallowed_to_allowed (function, L115-L138)

> *Summary: This function constructs a graph of permissible speaker transitions by starting with all possible connections between agents. It then filters out any transitions specified as disallowed in the input dictionary, returning a map showing which agents each agent can transition to.*


### visualize_speaker_transitions_dict (function, L142-L173)

> *Summary: Constructs a directed graph from a dictionary mapping agent names to lists of successor agents, then visualizes this transition structure using `networkx` and displays or saves the resulting plot based on the provided export path.*

