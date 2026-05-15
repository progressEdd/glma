# autogen/agentchat/contrib/captainagent/agent_builder.py

2 function(s): _config_check, _retrieve_json. 1 class(es): AgentBuilder. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _config_check | function |  |
| _retrieve_json | function |  |
| AgentBuilder | class |  |

## Chunks

### _config_check (function, L28-L39)

> *Summary: Validates a configuration dictionary to ensure all necessary top-level keys like `coding`, `default_llm_config`, and `code_execution_config` are present. It also iterates through `agent_configs` to confirm each agent has a defined name, system message, and description.*


### _retrieve_json (function, L42-L49)

> *Summary: Extracts the content from the first markdown code block found within a given string input using regex matching. If no code blocks are present, it returns the original text unchanged.*


### AgentBuilder (class, L53-L793)

> *Summary: This class orchestrates the creation of a multi-agent system by using an LLM to interpret a task and generate configurations for specialized agents. It supports building agents from scratch based on prompts or selecting them from a predefined library via vector search, ultimately returning a list of configured `ConversableAgent` instances ready for execution.*


### __init__ (method, L185-L250, parent: AgentBuilder)

> *Summary: Initializes an agent builder by loading LLM configurations from a specified file or environment variable, filtering models based on provided lists and tags for the builder and agents. It validates that at least one suitable builder model exists before setting up internal state for managing agent creation tasks.*


### set_builder_model (method, L252-L253, parent: AgentBuilder)

> *Summary: Sets the internal `builder_model` attribute of the agent builder using a provided string identifier for the model. This configures which underlying model will be used by the builder component.*


### set_agent_model (method, L255-L256, parent: AgentBuilder)

> *Summary: Assigns a specified string representing the language model to the agent's internal configuration. This method updates the `agent_model` attribute based on the provided input string.*


### _create_agent (method, L258-L359, parent: AgentBuilder)

> *Summary: Constructs a group chat participant agent based on provided configuration details like model name, system message, and LLM settings. It initializes either a standard `AssistantAgent` or a specialized `GPTAssistantAgent`, automatically setting up endpoints for open-source models if necessary before returning the configured agent instance.*


### clear_agent (method, L361-L380, parent: AgentBuilder)

> *Summary: Removes a specified agent by name from the system's tracking dictionary. If recycling is enabled, it terminates the associated endpoint server if no other agents depend on that specific server ID.*


### clear_all_agents (method, L382-L386, parent: AgentBuilder)

> *Summary: Iterates through all registered agents and calls a clear method on each one, optionally recycling the endpoint during the process. This action effectively removes every cached agent managed by the instance.*


### build (method, L388-L515, parent: AgentBuilder)

> *Summary: This method constructs a set of specialized agents by querying an LLM based on a provided `building_task`. It iteratively generates agent names, system messages, and descriptions using the builder model before assembling configurations. Finally, it returns the list of instantiated agents along with cached configuration details.*


### build_from_library (method, L517-L671, parent: AgentBuilder)

> *Summary: This method constructs a set of specialized agents by first querying an agent library using semantic search based on the `building_task`. It then uses a language model to select the most relevant agents from the retrieved pool, potentially generating new ones if no match is found. Finally, it caches the configuration and returns the fully instantiated list of agents.*


### _build_agents (method, L673-L715, parent: AgentBuilder)

> *Summary: Constructs a list of conversational agents based on cached configurations and optional parameters like an OpenAI assistant flag or a custom user proxy. It returns the resulting list of agents along with a copy of the cached configuration dictionary.*


### save (method, L717-L733, parent: AgentBuilder)

> *Summary: Writes the agent's cached configuration data to a JSON file. If no specific path is provided, it generates a unique filename based on an MD5 hash of the building task and saves the content locally.*


### load (method, L735-L793, parent: AgentBuilder)

> *Summary: Reads agent configuration from a provided file path or JSON string to load settings. It then uses these configurations to construct and return a list of agents along with the cached configuration data, optionally overriding code execution settings during construction.*

