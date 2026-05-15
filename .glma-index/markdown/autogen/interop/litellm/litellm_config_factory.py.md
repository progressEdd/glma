# autogen/interop/litellm/litellm_config_factory.py

2 function(s): get_crawl4ai_version, is_crawl4ai_v05_or_higher. 5 class(es): LiteLLmConfigAdapter, LiteLLmConfigFactory, DefaultLiteLLmConfigFactory, GoogleLiteLLmConfigFactory, OllamaLiteLLmConfigFactory. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LiteLLmConfigAdapter | class |  |
| get_crawl4ai_version | function |  |
| is_crawl4ai_v05_or_higher | function |  |
| LiteLLmConfigFactory | class |  |
| DefaultLiteLLmConfigFactory | class |  |
| GoogleLiteLLmConfigFactory | class |  |
| OllamaLiteLLmConfigFactory | class |  |

## Chunks

### LiteLLmConfigAdapter (class, L22-L34)

> *Summary: This adapter class holds three distinct configuration dictionaries: legacy, LLM-specific, and strategy-related. It provides methods to return copies of these internal configurations as standard Python dictionaries for external use.*


### as_legacy_kwargs (method, L27-L28, parent: LiteLLmConfigAdapter)

> *Summary: Converts the internal `legacy_config` attribute into a standard Python dictionary. This allows the configuration object to be used where legacy keyword arguments are expected.*


### as_llm_config_kwargs (method, L30-L31, parent: LiteLLmConfigAdapter)

> *Summary: Converts the internal configuration dictionary into a standard keyword argument dictionary suitable for LLM initialization. It returns a copy of the stored `llm_config_kwargs`.*


### as_strategy_kwargs (method, L33-L34, parent: LiteLLmConfigAdapter)

> *Summary: Returns a dictionary containing the strategy keyword arguments stored within the instance. This allows external code to access and use these configuration parameters.*


### get_crawl4ai_version (function, L37-L52)

> *Summary: Attempts to retrieve the installed version string for `crawl4ai` by first checking package metadata and then falling back to inspecting the imported module's `__version__` attribute. Returns the version as a string if found, or `None` otherwise.*


### is_crawl4ai_v05_or_higher (function, L55-L67)

> *Summary: Determines if the installed `crawl4ai` library meets or exceeds version 0.5.0 by retrieving its current version string and comparing its parsed integer components against a target version array. Returns `True` only if the version is successfully parsed and greater than or equal to `[0, 5, 0]`.*


### LiteLLmConfigFactory (class, L71-L145)

> *Summary: This factory class dynamically creates a `LiteLLmConfigAdapter` from an input configuration dictionary by iterating through registered factories until one accepts the config's API type. It standardizes parameters, separating them into legacy, LLM-specific, and strategy keyword arguments for compatibility across different library versions.*


### create_lite_llm_config (method, L75-L89, parent: LiteLLmConfigFactory)

> *Summary: This function generates a `LiteLLmConfigAdapter` by iterating through registered factories to process an input configuration (`LLMConfig` or `dict`). It returns an adapter that supports both legacy and modern keyword arguments depending on the detected configuration structure.*


### _create_adapter (method, L92-L121, parent: LiteLLmConfigFactory)

> *Summary: Constructs a configuration adapter by transforming a base dictionary into components suitable for `LiteLLmConfigAdapter`. It extracts provider-specific parameters like API keys and URLs from the input, prioritizing `base_url` over `api_base`, while preserving other settings in strategy arguments.*


### register_factory (method, L124-L129, parent: LiteLLmConfigFactory)

> *Summary: This decorator registers a provided class as a factory within the `_factories` set of an object. It wraps the input factory, ensuring that an instance of it is added to the registry upon decoration.*


### create (method, L132-L137, parent: LiteLLmConfigFactory)

> *Summary: This method transforms an initial LLM configuration dictionary by extracting the model name and API type. It then injects a combined `"provider"` string into the configuration before returning the modified dictionary.*


### get_api_type (method, L141-L141, parent: LiteLLmConfigFactory)

> *Summary: Determines the specific API type string based on an input class object. It returns a string identifier representing the underlying API structure.*


### accepts (method, L144-L145, parent: LiteLLmConfigFactory)

> *Summary: Determines if a class is compatible with an LLM configuration dictionary by checking if the `api_type` in the input matches the class's defined API type, defaulting to "openai" if not specified. Returns a boolean indicating compatibility.*


### DefaultLiteLLmConfigFactory (class, L149-L168)

> *Summary: This factory determines if a configuration dictionary is suitable for its scope, primarily checking that the `api_type` is not "google" or "ollama". It then transforms the input by renaming an optional `api_key` to `api_token`, falling back to environment variables if necessary, before calling the parent creation method.*


### get_api_type (method, L151-L152, parent: DefaultLiteLLmConfigFactory)

> *Summary: This method is intended to return a string identifying the specific LLM API type associated with a given class. Currently, it raises a `NotImplementedError` because the default factory lacks this information.*


### accepts (method, L155-L157, parent: DefaultLiteLLmConfigFactory)

> *Summary: Determines if a configuration object is compatible with the current implementation by checking if its specified `api_type` is neither "google" nor "ollama". It returns a boolean indicating compatibility based on this check.*


### create (method, L160-L168, parent: DefaultLiteLLmConfigFactory)

> *Summary: This method transforms an initial LLM configuration dictionary by ensuring the presence of an API key, either from the input or environment variables. It then standardizes the key name from `api_key` to `api_token` before calling the parent class's creation logic and returning the finalized configuration.*


### GoogleLiteLLmConfigFactory (class, L172-L190)

> *Summary: This factory configures LiteLLM settings for Google models by transforming an input configuration dictionary. It specifically maps the `api_key` to `api_token` and sets the internal API type to `"gemini"` before calling the parent class's creation method, while also defining which configurations it accepts.*


### get_api_type (method, L174-L175, parent: GoogleLiteLLmConfigFactory)

> *Summary: This method determines the API type for a given class, currently hardcoding and returning the string `"google"`. It takes a class object as input and outputs a fixed string identifier.*


### create (method, L178-L185, parent: GoogleLiteLLmConfigFactory)

> *Summary: This method transforms an initial LLM configuration dictionary by renaming the `api_key` to `api_token` and explicitly setting the `api_type` to `"gemini"`. It then passes this modified configuration to a parent class's creation method, returning the resulting complete configuration.*


### accepts (method, L188-L190, parent: GoogleLiteLLmConfigFactory)

> *Summary: Determines if a class is compatible with an LLM configuration dictionary by checking if the configuration's `api_type` matches the class's expected type or if it is specifically set to "gemini". Returns a boolean indicating compatibility.*


### OllamaLiteLLmConfigFactory (class, L194-L205)

> *Summary: This factory class configures LiteLLM for Ollama by transforming the input configuration dictionary. It specifically maps a `client_host` key from the input to the `api_base` field in the resulting configuration.*


### get_api_type (method, L196-L197, parent: OllamaLiteLLmConfigFactory)

> *Summary: This method determines the API type for a given class, currently hardcoding and returning `"ollama"` regardless of the input. It takes a class object as input and returns a string representing the configured API type.*


### create (method, L200-L205, parent: OllamaLiteLLmConfigFactory)

> *Summary: This method transforms an initial LLM configuration dictionary by ensuring any `client_host` key is renamed to `api_base`. It returns the modified configuration dictionary after inheriting and performing this specific key mapping.*

