# autogen/llm_config/config.py

2 class(es): LLMConfig, _LLMConfig. 26 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LLMConfig | class |  |
| _LLMConfig | class |  |

## Chunks

### LLMConfig (class, L25-L293)

> *Summary: Manages and aggregates multiple LLM configurations, accepting various inputs like lists of entries or dictionaries for initialization. It provides methods to serialize the configuration to JSON, filter settings using `where()`, and allows access to underlying model parameters via standard attribute/item accessors.*


### __init__ (method, L28-L117, parent: LLMConfig)

> *Summary: Initializes an LLM configuration object by merging provided model configurations (`*configs`) with global generation parameters like `temperature`, `max_tokens`, and response format. It processes the input configs to build a list of specific model settings, which are then stored internally along with other operational controls such as timeouts and routing methods.*


### ensure_config (method, L120-L154, parent: LLMConfig)

> *Summary: This method standardizes various input types—including dictionaries, lists of items, or existing configuration objects—into a consistent `LLMConfig` instance. It handles direct object conversion, dictionary unpacking, and list iteration to ensure the resulting configuration is always an `LLMConfig`.*


### from_json (method, L157-L178, parent: LLMConfig)

> *Summary: This method constructs an instance of a configuration class by reading settings from either an environment variable or a specified JSON file. It validates that exactly one source (environment or path) is provided and then instantiates the target class using the parsed data.*


### where (method, L180-L192, parent: LLMConfig)

> *Summary: Filters a list of existing configurations based on provided keyword arguments and an optional exclusion flag. It returns a new `LLMConfig` instance containing only the matching configurations or raises a `ValueError` if no matches are found.*


### model_dump (method, L194-L196, parent: LLMConfig)

> *Summary: Converts the internal model state into a dictionary representation. It calls the underlying model's dump method and then filters out any keys whose values are empty lists.*


### model_dump_json (method, L198-L201, parent: LLMConfig)

> *Summary: Converts the object's state into a JSON string by first serializing it to a dictionary and then using `json.dumps`. It accepts optional arguments for controlling the serialization process, such as excluding null values.*


### model_validate (method, L203-L204, parent: LLMConfig)

> *Summary: This method acts as a proxy, forwarding any arguments received to the underlying `_model`'s validation function. It returns the result of that internal model validation process.*


### model_validate_json (method, L207-L208, parent: LLMConfig)

> *Summary: Delegates JSON validation to the underlying model instance using its `model_validate_json` method. It accepts arbitrary positional and keyword arguments and returns the validated object.*


### model_validate_strings (method, L211-L212, parent: LLMConfig)

> *Summary: This method acts as a simple pass-through wrapper, forwarding any arguments received to the underlying `_model`'s `model_validate_strings` function and returning its result. It ensures string validation logic from the core model is executed when called on this instance.*


### __eq__ (method, L214-L217, parent: LLMConfig)

> *Summary: Compares two configuration objects by checking if their internal model identifiers match. It returns `False` or raises an error if the provided value is not another `LLMConfig` instance.*


### _getattr (method, L219-L221, parent: LLMConfig)

> *Summary: Retrieves an attribute value from a given object using its string name. It acts as a simple wrapper around Python's built-in `getattr` function.*


### get (method, L223-L225, parent: LLMConfig)

> *Summary: Retrieves a configuration value from the underlying model object using a specified key. It returns the stored value if found, or an optional default if the key does not exist.*


### __getitem__ (method, L227-L231, parent: LLMConfig)

> *Summary: Retrieves a configuration value by string key from the underlying model object. If the specified key does not exist on the model, it raises a `KeyError`.*


### __setitem__ (method, L233-L237, parent: LLMConfig)

> *Summary: Allows dynamic setting of attributes on an underlying model object using a string key and a provided value. It attempts to set the attribute directly but raises a `ValueError` if the specified key does not exist on the model.*


### __getattr__ (method, L239-L243, parent: LLMConfig)

> *Summary: This method dynamically retrieves attributes from an underlying model object. It acts as a proxy, forwarding requests for missing attributes to the internal `_model` instance while raising a descriptive error if the attribute is not found there.*


### __setattr__ (method, L245-L249, parent: LLMConfig)

> *Summary: This method intercepts attribute assignments to route them either directly onto the instance if the attribute is `_model`, or delegate the assignment to the internal model object. It ensures that configuration properties are set correctly on the underlying LLM model instance.*


### __contains__ (method, L251-L252, parent: LLMConfig)

> *Summary: Checks if a given string key exists as an attribute on the internal model object. Returns `True` if the attribute is present and `False` otherwise.*


### __repr__ (method, L254-L263, parent: LLMConfig)

> *Summary: Generates a developer-friendly string representation of the configuration object by dumping its contents into key-value pairs. It then sanitizes this output to mask sensitive values associated with keys ending in "key" or "token".*


### __copy__ (method, L265-L267, parent: LLMConfig)

> *Summary: Creates a shallow copy of the configuration object by extracting model parameters and then reconstructing a new `LLMConfig` instance using the existing list of options and the copied model settings. This ensures that modifications to the returned copy do not affect the original object's state.*


### __deepcopy__ (method, L269-L270, parent: LLMConfig)

> *Summary: This method ensures a deep copy of the configuration object by first performing a shallow copy and then recursively copying any mutable attributes. It allows for creating independent instances of the LLM configuration while preserving internal state integrity.*


### copy (method, L272-L273, parent: LLMConfig)

> *Summary: Creates a shallow copy of the current configuration object. This allows for creating independent instances based on an existing configuration state.*


### deepcopy (method, L275-L276, parent: LLMConfig)

> *Summary: Creates a completely independent copy of the current configuration object. It accepts an optional memoization dictionary to handle recursive copying during the process.*


### __str__ (method, L278-L279, parent: LLMConfig)

> *Summary: When called, this method returns the string representation of the object using `repr()`. This provides a developer-friendly, unambiguous string output for debugging or logging.*


### items (method, L281-L283, parent: LLMConfig)

> *Summary: Returns an iterable of key-value pairs from the configuration object's serialized data. This method exposes all stored settings as tuples of strings and arbitrary types.*


### keys (method, L285-L287, parent: LLMConfig)

> *Summary: Retrieves all configuration keys from the current model instance by dumping its state and returning the set of keys. This method provides an iterable view of the stored parameters.*


### values (method, L289-L291, parent: LLMConfig)

> *Summary: Retrieves all the configuration values from the current model instance as an iterable collection. It first serializes the object's state and then returns only the dictionary values.*


### _LLMConfig (class, L296-L317)

> *Summary: This class defines the structure for LLM configurations, holding parameters like timeouts, seeds, and tool/function lists. It enforces strict validation by forbidding any extra fields in the configuration data it receives.*

