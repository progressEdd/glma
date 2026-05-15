# test/agentchat/contrib/test_agent_builder.py

8 function(s): _config_check, builder, test_build, test_build_from_library, test_build_with_agent_configs, test_save, test_load, test_clear_agent.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _config_check | function |  |
| builder | function |  |
| test_build | function |  |
| test_build_from_library | function |  |
| test_build_with_agent_configs | function |  |
| test_save | function |  |
| test_load | function |  |
| test_clear_agent | function |  |

## Chunks

### _config_check (function, L28-L38)

> *Summary: Validates a configuration dictionary to ensure essential sections like coding, default LLM settings, and code execution configurations are present. It further iterates through `agent_configs` to confirm each agent definition includes a name, model, description, and system message.*


### builder (function, L42-L47)

> *Summary: Creates an `AgentBuilder` instance by extracting LLM configuration and setting specific model tags from a provided `Credentials` object. This function configures the builder to use "gpt-4o" for both its internal and agent models.*


### test_build (function, L52-L73)

> *Summary: This test verifies the agent construction process by using a predefined task and credentials to build an agent configuration. It asserts that the resulting configuration adheres to the maximum allowed number of agents defined in the builder.*


### test_build_from_library (function, L80-L122)

> *Summary: This test verifies the `build_from_library` method by constructing an agent configuration using a predefined library and a specific task prompt. It asserts that the resulting configuration adheres to constraints, such as the maximum allowed number of agents, under both default and specified embedding model configurations.*


### test_build_with_agent_configs (function, L126-L151)

> *Summary: This test verifies that an `AgentBuilder` correctly constructs and returns a list of agents when provided with specific configuration parameters. It asserts the presence of a `TextAnalyzerAgent` instance within the resulting agent collection based on the input configurations.*


### test_save (function, L155-L181)

> *Summary: This test verifies the `save` functionality by first building an agent using a complex task and then saving its configuration to a JSON file within a temporary directory. It asserts that the resulting file exists and passes the loaded configuration through a validation helper function.*


### test_load (function, L185-L201)

> *Summary: This test verifies the agent builder's loading capability by reading a configuration file and processing it with specified code execution settings. It returns the loaded agent configurations, which are then validated against expected structures.*


### test_clear_agent (function, L205-L220)

> *Summary: This test verifies that an agent builder correctly removes all instantiated agents after loading a configuration. It loads a specific configuration and then calls `clear_all_agents()` to assert that the internal list of assigned processes becomes empty.*

