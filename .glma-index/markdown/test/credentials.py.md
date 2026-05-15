# test/credentials.py

2 function(s): build_config_from_env, get_credentials_from_env_vars. 2 class(es): Secrets, Credentials. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Secrets | class |  |
| Credentials | class |  |
| build_config_from_env | function |  |
| get_credentials_from_env_vars | function |  |

## Chunks

### Secrets (class, L17-L62)

> *Summary: This utility manages a set of stored secrets and provides methods to generate regex patterns or sanitize input strings based on those secrets. It builds a pattern matching all substrings of a minimum length derived from the registered secrets, which can then be used to censor sensitive content in a given string.*


### add_secret (method, L21-L23, parent: Secrets)

> *Summary: This method adds a new secret string to the internal secrets collection and then clears the cache for the pattern retrieval mechanism. It takes one string input representing the secret and returns nothing.*


### get_secrets_pattern (method, L27-L43, parent: Secrets)

> *Summary: Generates a compiled regular expression pattern designed to find any substring of a specified minimum length (`x`) present within the application's secrets. It iterates through all stored secrets and generates all possible substrings meeting the length criteria, combining them into an OR-separated regex.*


### sanitize_secrets (method, L46-L62, parent: Secrets)

> *Summary: This method censors substrings within an input string based on a predefined list of secrets and a minimum length threshold. It uses a dynamically generated regex pattern derived from the secrets to replace matching segments with asterisks.*


### Credentials (class, L65-L99)

> *Summary: Manages OpenAI API credentials by storing and registering the necessary configuration upon initialization. It provides properties to access key details like the API key, model name, and API type, while offering methods to return sanitized versions of the configuration for safe logging or display.*


### __init__ (method, L68-L70, parent: Credentials)

> *Summary: Initializes the object by storing an `LLMConfig` instance and registering its API key with a global secrets manager.*


### sanitize (method, L72-L77, parent: Credentials)

> *Summary: This method takes an object's configuration, copies it, and then iterates through the `config_list` to replace any existing API keys with a masked string. It returns the modified configuration dictionary.*


### __repr__ (method, L79-L80, parent: Credentials)

> *Summary: Returns a string representation of the object after sanitizing its internal state. This method ensures that sensitive data is masked when debugging or logging the instance.*


### __str___ (method, L82-L83, parent: Credentials)

> *Summary: Converts the object's sanitized state into a string representation. It takes no explicit inputs other than `self` and returns a descriptive string output.*


### config_list (method, L86-L87, parent: Credentials)

> *Summary: Retrieves a list of configuration dictionaries by iterating over the `llm_config.config_list` attribute and serializing each item using `model_dump()`. This method returns a list where each element is a dictionary representation of a stored configuration object.*


### api_key (method, L90-L91, parent: Credentials)

> *Summary: Retrieves the API key string from the first element of the internal configuration list. This method provides access to a stored credential value.*


### api_type (method, L94-L95, parent: Credentials)

> *Summary: Retrieves the API type string from the first element of the internal configuration list. This method assumes the configuration structure is present and accessible via `self.config_list`.*


### model (method, L98-L99, parent: Credentials)

> *Summary: Retrieves the "model" string from the first dictionary within the instance's `config_list`. This method returns a single string representing the model identifier.*


### build_config_from_env (function, L102-L136)

> *Summary: Constructs a configuration dictionary by retrieving an API key from the specified environment variable. It accepts parameters like API type, model name, and optional URLs/versions to build and return the complete configuration object, or `None` if the key is missing.*


### get_credentials_from_env_vars (function, L139-L279)

> *Summary: Constructs a list of `Credentials` objects by reading various API keys and configuration details from environment variables for multiple LLM providers (OpenAI, Azure, Gemini, Anthropic, etc.). It returns the final credentials object after optionally filtering the collected configurations based on provided criteria.*

