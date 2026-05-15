# autogen/oai/openai_utils.py

15 function(s): get_key, is_valid_api_key, get_config_list, get_first_llm_config, config_list_openai_aoai, config_list_from_models, config_list_gpt4_gpt35, get_config, config_list_from_dotenv, retrieve_assistants_by_name and 5 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_key | function |  |
| is_valid_api_key | function |  |
| get_config_list | function |  |
| get_first_llm_config | function |  |
| config_list_openai_aoai | function |  |
| config_list_from_models | function |  |
| config_list_gpt4_gpt35 | function |  |
| get_config | function |  |
| config_list_from_dotenv | function |  |
| retrieve_assistants_by_name | function |  |
| detect_gpt_assistant_api_version | function |  |
| create_gpt_vector_store | function |  |
| create_gpt_assistant | function |  |
| update_gpt_assistant | function |  |
| _satisfies | function |  |

## Chunks

### get_key (function, L154-L168)

> *Summary: Extracts a unique identifier from a configuration dictionary by removing specific keys defined in `NON_CACHE_KEY`. It returns this cleaned, serialized configuration as a string suitable for use as a dictionary key.*


### is_valid_api_key (function, L171-L183)

> *Summary: Checks if a provided string conforms to the expected format of an OpenAI API key by ensuring it starts with "sk-" and contains at least 48 alphanumeric characters (including underscores and dashes). Returns `True` if the input matches this pattern, otherwise `False`.*


### get_config_list (function, L187-L235)

> *Summary: Constructs a list of configuration dictionaries for OpenAI API clients based on provided keys and optional parameters like base URLs, API type, and version. It iterates through the input API keys, creating a unique configuration dictionary for each non-empty key while respecting length constraints if `base_urls` are supplied.*


### get_first_llm_config (function, L239-L263)

> *Summary: Extracts the initial LLM configuration from a provided structure. It checks for a `config_list` and returns the first element as a dictionary, or the entire input if no list is present but a model key exists.*


### config_list_openai_aoai (function, L267-L393)

> *Summary: Reads API keys and base URLs for OpenAI and Azure OpenAI services from environment variables or specified local files. It constructs and returns a list of configuration dictionaries, optionally filtering out one service type based on the `exclude` parameter.*


### config_list_from_models (function, L397-L460)

> *Summary: Generates a list of API configuration dictionaries by extending existing configurations with specified models. It takes paths and file names for keys/bases as input and returns a list where each entry includes the necessary credentials plus a `"model"` key populated from `model_list`.*


### config_list_gpt4_gpt35 (function, L464-L490)

> *Summary: Retrieves a list of configuration dictionaries specifically for GPT-4 and GPT-3.5-Turbo models by reading API keys and base URLs from specified files. It accepts optional paths, key file names, and an exclusion filter to customize the returned list.*


### get_config (function, L493-L528)

> *Summary: Creates a configuration dictionary for an API by accepting optional `api_key`, `base_url`, `api_type`, and `api_version` strings as input. It returns a dictionary containing these settings, optionally overriding them with environment variables if present.*


### config_list_from_dotenv (function, L532-L631)

> *Summary: Loads API configurations by reading from a specified `.env` file or environment variables, using a provided map to define model-specific keys and settings. It returns a filtered list of configuration dictionaries, each containing the model name and its associated credentials/parameters.*


### retrieve_assistants_by_name (function, L634-L641)

> *Summary: Fetches all available assistants from the OpenAI API and filters them to return a list containing only those whose names match the provided string input.*


### detect_gpt_assistant_api_version (function, L644-L647)

> *Summary: Determines the OpenAI Assistant API version by checking the installed `openai` library's version against a threshold. It returns `"v1"` for older versions and `"v2"` otherwise.*


### create_gpt_vector_store (function, L650-L668)

> *Summary: Initializes an OpenAI vector store using a provided name and then uploads specified file IDs to it. It polls the batch status, returning the created vector store object only upon successful completion of the file ingestion process.*


### create_gpt_assistant (function, L671-L718)

> *Summary: Constructs an OpenAI GPT Assistant by accepting a name, instructions, model, and configuration dictionary. It intelligently translates configurations for different API versions (V1 vs V2), handling tool definitions like retrieval or code interpretation based on the provided inputs to return the newly created `Assistant` object.*


### update_gpt_assistant (function, L721-L739)

> *Summary: This function modifies an existing OpenAI GPT Assistant using a provided configuration dictionary and the OpenAI client. It dynamically constructs update arguments based on whether the assistant uses v2 API features (like `tool_resources`) or older methods (like `file_ids`), returning the updated Assistant object.*


### _satisfies (function, L742-L746)

> *Summary: Checks if a given configuration value meets any of the specified acceptable values. It returns `True` if the value is present in the list of acceptable values, or if there is a non-empty intersection between two lists.*

