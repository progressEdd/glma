# autogen/beta/config/gemini/config.py

6 class(es): GeminiBaseConfigOverrides, GeminiConfigOverrides, VertexAIConfigOverrides, GeminiBaseConfig, GeminiConfig, VertexAIConfig. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GeminiBaseConfigOverrides | class |  |
| GeminiConfigOverrides | class |  |
| VertexAIConfigOverrides | class |  |
| GeminiBaseConfig | class |  |
| GeminiConfig | class |  |
| VertexAIConfig | class |  |

## Chunks

### GeminiBaseConfigOverrides (class, L18-L32)

> *Summary: Defines a structure for overriding base Gemini configuration settings, allowing developers to specify parameters like model name, sampling controls (temperature, top\_p), and generation limits. It accepts optional overrides for various generation behaviors and includes fields for advanced thinking configurations.*


### GeminiConfigOverrides (class, L35-L36)

> *Summary: This class defines optional overrides for a base configuration, specifically allowing the setting of an `api_key` as a string or `None`. It inherits from a general configuration override structure.*


### VertexAIConfigOverrides (class, L39-L42)

> *Summary: This class defines optional overrides for Gemini configurations when using Vertex AI. It accepts credentials (as an object or string), a Google Cloud project ID, and a location string to customize the connection settings.*


### GeminiBaseConfig (class, L46-L98)

> *Summary: This configuration class holds various parameters for interacting with a Gemini model, such as temperature, token limits, and penalties. It provides methods to construct the final API request configuration by selectively including provided settings or resolving complex thinking configurations based on `thinking_level` and `thinking_budget`.*


### _build_create_config (method, L62-L86, parent: GeminiBaseConfig)

> *Summary: Constructs a `CreateConfig` object by selectively copying various generation parameters (like temperature, top\_p, max\_output\_tokens) from the instance's attributes. It also incorporates any resolved "thinking" configuration into the final output structure.*


### _resolve_thinking_config (method, L88-L98, parent: GeminiBaseConfig)

> *Summary: If a pre-existing configuration exists, it is returned directly; otherwise, this method constructs and returns a `ThinkingConfig` object using the provided `thinking_level` and/or `thinking_budget`, or returns `None` if neither is set.*


### GeminiConfig (class, L102-L119)

> *Summary: This configuration class holds settings for interacting with the Gemini API, including an optional `api_key`. It provides methods to instantiate both a general `GeminiClient` and a specialized `GeminiFilesClient` based on its current state.*


### copy (method, L105-L106, parent: GeminiConfig)

> *Summary: Creates a new configuration instance by merging the current object's settings with provided overrides. It returns a complete `GeminiConfig` object reflecting the merged state.*


### create (method, L108-L116, parent: GeminiConfig)

> *Summary: Instantiates and returns a `GeminiClient` object using configuration parameters like the model name, API key, streaming preference, and cached content settings. It internally builds specific creation configurations before passing them to the client constructor.*


### create_files_client (method, L118-L119, parent: GeminiConfig)

> *Summary: Instantiates and returns a `GeminiFilesClient` object, passing the current instance as an argument for dependency injection. This method provides access to file management capabilities within the Gemini context.*


### VertexAIConfig (class, L123-L141)

> *Summary: This configuration class holds parameters like credentials, project ID, and location for interacting with Vertex AI models. It provides a `create` method to instantiate and return a configured `GeminiClient` object based on the stored settings.*


### copy (method, L128-L129, parent: VertexAIConfig)

> *Summary: Creates a new configuration instance by merging the current object's settings with provided overrides. It returns a complete `VertexAIConfig` object reflecting the merged state.*


### create (method, L131-L141, parent: VertexAIConfig)

> *Summary: Instantiates and returns a `GeminiClient` object using configuration parameters stored within the instance. It passes model details, authentication credentials, project/location settings, streaming preference, and derived creation configurations to the client constructor.*

