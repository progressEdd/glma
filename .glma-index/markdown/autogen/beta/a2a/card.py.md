# autogen/beta/a2a/card.py

4 function(s): build_card, _build_interfaces, _agent_description, _resolve_skills.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| build_card | function |  |
| _build_interfaces | function |  |
| _agent_description | function |  |
| _resolve_skills | function |  |

## Chunks

### build_card (function, L30-L121)

> *Summary: Constructs an `AgentCard` object to describe an agent for A2A discovery, taking the agent instance and various configuration parameters like URLs, transports, skills, and security requirements as input. It synthesizes interfaces based on enabled transports, resolves agent capabilities including skills, and returns a fully populated `AgentCard`.*


### _build_interfaces (function, L124-L152)

> *Summary: Constructs a list of `AgentInterface` objects based on specified transport types and configuration URLs. It determines the correct interface URL and protocol binding for each requested transport (JSONRPC, REST, or gRPC) using provided inputs like base URLs and tenant mappings.*


### _agent_description (function, L155-L159)

> *Summary: Retrieves the primary system prompt from an `Agent` object, returning the first element of the prompt list if one exists, otherwise returns an empty string.*


### _resolve_skills (function, L162-L193)

> *Summary: Determines the final list of skills for an agent by prioritizing explicitly provided skills, then automatically discovering skills from attached toolkits, and finally falling back to a default skill based on the agent's name if no other skills are found. It takes an `Agent` object, optional explicit skills, and a description string as input, returning a prioritized list of `AgentSkill` objects.*

