# autogen/llm_config/entry.py

3 class(es): LLMConfigEntryDict, ApplicationConfig, LLMConfigEntry. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LLMConfigEntryDict | class |  |
| ApplicationConfig | class |  |
| LLMConfigEntry | class |  |

## Chunks

### LLMConfigEntryDict (class, L17-L32)

> *Summary: Defines a structured dictionary for configuring LLM interactions. It accepts various parameters like API type, model name, token limits, and optional connection details such as base URLs and HTTP clients.*


### ApplicationConfig (class, L35-L64)

> *Summary: Defines configuration parameters for LLM interactions, accepting optional integer limits (`max_tokens`) and floating-point sampling controls (`top_p` or `temperature`). These settings govern generation length, randomness, and nucleus sampling behavior during model inference.*


### LLMConfigEntry (class, L67-L169)

> *Summary: This class defines a configuration structure for LLM connections, accepting parameters like API type, model name, and optional credentials/endpoints. It provides methods to apply global configurations, serialize secrets securely, and allows dictionary-like access to its fields while masking sensitive values in string representations.*


### apply_application_config (method, L86-L92, parent: LLMConfigEntry)

> *Summary: This method merges provided `ApplicationConfig` settings into a model configuration instance by overriding existing values only if the current instance's attributes are unset (i.e., `None`). It returns a new, updated copy of the configuration object.*


### create_client (method, L95-L95, parent: LLMConfigEntry)

> *Summary: Instantiates and returns a `ModelClient` object, likely setting up the necessary connections or configurations for interacting with an LLM model. This method is responsible for providing the operational client interface.*


### check_base_url (method, L99-L105, parent: LLMConfigEntry)

> *Summary: Validates an input URL, ensuring it starts with a recognized protocol (HTTP/HTTPS/WS/WSS). If the provided value is missing or lacks a scheme, it returns `None` or prepends `"http://"` respectively.*


### serialize_base_url (method, L108-L109, parent: LLMConfigEntry)

> *Summary: Converts an optional `HttpUrl` object into a string representation. It returns the string version of the URL if provided, or `None` otherwise.*


### serialize_api_key (method, L112-L113, parent: LLMConfigEntry)

> *Summary: Converts a `SecretStr` object into its plain string representation by retrieving the underlying secret value. This method is used to expose sensitive credentials as standard strings.*


### model_dump (method, L115-L116, parent: LLMConfigEntry)

> *Summary: This method serializes the object's state into a dictionary representation. It delegates the actual serialization to `BaseModel.model_dump`, allowing for optional exclusion of `None` values and accepting arbitrary arguments.*


### model_dump_json (method, L118-L119, parent: LLMConfigEntry)

> *Summary: This method serializes the object's state into a JSON string using `BaseModel`'s built-in functionality. It accepts optional arguments to control serialization behavior like excluding null values.*


### get (method, L121-L125, parent: LLMConfigEntry)

> *Summary: Retrieves an attribute value from the object using a provided key and optional default. If the retrieved value is a `SecretStr`, it returns its decrypted secret content instead of the wrapper object.*


### __getitem__ (method, L127-L134, parent: LLMConfigEntry)

> *Summary: Retrieves an attribute from the object using a string key; if the retrieved value is a `SecretStr`, it returns its decrypted secret value instead. Otherwise, it returns the attribute directly or raises a `KeyError` if the key does not exist.*


### __setitem__ (method, L136-L137, parent: LLMConfigEntry)

> *Summary: Allows dynamic attribute setting on the configuration object using dictionary-like syntax. It takes a string key and an arbitrary value to assign as an instance attribute.*


### __contains__ (method, L139-L140, parent: LLMConfigEntry)

> *Summary: Checks if an instance possesses a specific attribute by name. It returns `True` if the object has the given string as an attribute name, and `False` otherwise.*


### items (method, L142-L144, parent: LLMConfigEntry)

> *Summary: Returns an iterable of key-value pairs from the model's serialized dictionary representation. This method exposes all configuration settings stored within the object as tuples of strings and arbitrary types.*


### keys (method, L146-L148, parent: LLMConfigEntry)

> *Summary: Retrieves all configuration keys from the model's current state dictionary. It returns an iterable containing these string keys.*


### values (method, L150-L152, parent: LLMConfigEntry)

> *Summary: Returns an iterable view of all key-value pairs contained within the model's serialized data. This method provides access to the internal configuration parameters as a collection of values.*


### __repr__ (method, L154-L166, parent: LLMConfigEntry)

> *Summary: Generates a string representation of the configuration object by serializing its attributes and then sanitizing it for security. It masks values associated with keys ending in `_key` or `_token` within the resulting string to prevent accidental exposure of sensitive data.*


### __str__ (method, L168-L169, parent: LLMConfigEntry)

> *Summary: When converted to a string, this object returns its official representation using `repr()`. This allows for unambiguous debugging and logging of the configuration instance.*

