# autogen/fast_depends/_compat.py

6 function(s): model_schema, get_config_base, get_aliases, get_config_base, model_schema, get_aliases. 3 class(es): CreateBaseModel, CreateBaseModel, Config.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| model_schema | function |  |
| get_config_base | function |  |
| get_aliases | function |  |
| CreateBaseModel | class |  |
| get_config_base | function |  |
| model_schema | function |  |
| get_aliases | function |  |
| CreateBaseModel | class |  |

## Chunks

### model_schema (function, L37-L38)

> *Summary: Generates a JSON schema dictionary from a Pydantic `BaseModel` instance by calling its built-in `model_json_schema()` method. This allows for introspection of the model's structure and data types.*


### get_config_base (function, L40-L41)

> *Summary: If provided with configuration data, it returns that data; otherwise, it initializes and returns a new `ConfigDict` using predefined default settings.*


### get_aliases (function, L43-L44)

> *Summary: Retrieves a tuple of string aliases for all fields within a given Pydantic-like model. It uses the field's defined alias if present, otherwise defaults to the field's original name.*


### CreateBaseModel (class, L46-L49)

> *Summary: This class inherits from `BaseModel` and configures it to allow arbitrary types, specifically for backward compatibility with older versions of FastStream. It serves as a wrapper model definition.*


### get_config_base (function, L55-L56)

> *Summary: Retrieves a base configuration class by either using the provided `config_data` or defaulting to a predefined set of values. It delegates the actual retrieval logic to another function, `get_config`.*


### model_schema (function, L58-L59)

> *Summary: Retrieves the JSON schema dictionary for a given Pydantic `BaseModel` instance by calling its built-in `.schema()` method. This function takes a model class and returns its structured schema representation.*


### get_aliases (function, L61-L62)

> *Summary: Retrieves a tuple of string aliases from a given Pydantic `BaseModel` by iterating over its fields and returning the alias if present, otherwise using the field's name.*


### CreateBaseModel (class, L64-L68)

> *Summary: This class inherits from `BaseModel` specifically to maintain compatibility with older versions of FastStream prior to 0.3.7. It configures the model to allow arbitrary types within its structure.*


### Config (class, L67-L68, parent: CreateBaseModel)

> *Summary: This class configuration enables serialization of arbitrary Python types within the system. It allows complex, non-standard data structures to be handled during configuration processing.*

