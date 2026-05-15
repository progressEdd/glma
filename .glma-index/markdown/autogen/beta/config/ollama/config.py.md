# autogen/beta/config/ollama/config.py

2 class(es): OllamaConfigOverrides, OllamaConfig. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OllamaConfigOverrides | class |  |
| OllamaConfig | class |  |

## Chunks

### OllamaConfigOverrides (class, L15-L25)

> *Summary: Defines a dictionary structure for overriding default Ollama configuration parameters. It accepts optional settings like model name, host address, and various generation controls such as temperature, max tokens, and stopping sequences.*


### OllamaConfig (class, L29-L63)

> *Summary: This configuration class holds parameters for interacting with an Ollama model, including the model name, host address, and generation settings like temperature and max tokens. It provides methods to instantiate an `OllamaClient` using these settings or to raise an error if a file-specific client is requested.*


### copy (method, L41-L42, parent: OllamaConfig)

> *Summary: Creates a new configuration instance by merging the current object's settings with provided overrides. It returns a complete `OllamaConfig` object reflecting the merged state.*


### create (method, L44-L60, parent: OllamaConfig)

> *Summary: Constructs and returns an `OllamaClient` instance by packaging configuration parameters like temperature, max tokens, and model name into the client object. It uses provided settings to initialize the connection details for interacting with Ollama.*


### create_files_client (method, L62-L63, parent: OllamaConfig)

> *Summary: This method raises a `NotImplementedError` if the current object type does not support interacting with the Files API. It serves as a placeholder to enforce implementation in subclasses that handle file operations.*

