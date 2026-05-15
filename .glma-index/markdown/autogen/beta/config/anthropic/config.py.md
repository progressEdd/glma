# autogen/beta/config/anthropic/config.py

2 class(es): AnthropicConfigOverrides, AnthropicConfig. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AnthropicConfigOverrides | class |  |
| AnthropicConfig | class |  |

## Chunks

### AnthropicConfigOverrides (class, L18-L35)

> *Summary: Defines a structure for overriding Anthropic API configuration parameters. It accepts various optional and required settings like model name, API key, token limits, and HTTP client details to customize API calls.*


### AnthropicConfig (class, L39-L94)

> *Summary: This configuration class holds parameters for interacting with the Anthropic API, including model selection, request limits, and various optional settings like temperature and caching. It provides methods to instantiate both a general `AnthropicClient` using these settings or a specialized `AnthropicFilesClient`.*


### copy (method, L58-L59, parent: AnthropicConfig)

> *Summary: Creates a new configuration instance by merging the current object's settings with provided overrides. It returns a complete `AnthropicConfig` object reflecting the merged state.*


### create (method, L61-L91, parent: AnthropicConfig)

> *Summary: This method constructs and returns an `AnthropicClient` instance by assembling configuration options from the object's attributes. It merges model-specific parameters like temperature, top\_p, and stop sequences into the client's creation arguments.*


### create_files_client (method, L93-L94, parent: AnthropicConfig)

> *Summary: Instantiates and returns a client object for interacting with Anthropic's file management system, using the current instance as a dependency.*

