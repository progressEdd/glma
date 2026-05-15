# autogen/oai/gemini_types.py

1 function(s): _remove_extra_fields. 7 class(es): CommonBaseModel, CaseInSensitiveEnum, FunctionCallingConfigMode, LatLng, FunctionCallingConfig, RetrievalConfig, ToolConfig. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _remove_extra_fields | function |  |
| CommonBaseModel | class |  |
| CaseInSensitiveEnum | class |  |
| FunctionCallingConfigMode | class |  |
| LatLng | class |  |
| FunctionCallingConfig | class |  |
| RetrievalConfig | class |  |
| ToolConfig | class |  |

## Chunks

### _remove_extra_fields (function, L25-L57)

> *Summary: This function cleans up a dictionary response by removing any keys that are not defined in the provided Pydantic model. It recursively traverses nested dictionaries and lists within the response to ensure all data conforms strictly to the model's structure, handling field aliases during the process.*


### CommonBaseModel (class, L63-L87)

> *Summary: This base model inherits from `BaseModel` and configures serialization/deserialization rules for handling various data types, including arbitrary ones. It provides class methods to validate responses from external sources and instance methods to serialize the object into a dictionary format.*


### _from_response (method, L78-L84, parent: CommonBaseModel)

> *Summary: This method validates an incoming dictionary response against a specified model type, ensuring forward compatibility by first stripping any extraneous fields from the raw response data before instantiation. It returns an instance of the target class populated with the validated data.*


### to_json_dict (method, L86-L87, parent: CommonBaseModel)

> *Summary: Converts the instance's state into a standard Python dictionary suitable for JSON serialization by excluding any `None` values. This method relies on an internal `model_dump` operation to achieve the conversion.*


### CaseInSensitiveEnum (class, L90-L110)

> *Summary: This class implements a string-based enumeration that allows case-insensitive lookups. It attempts to resolve an input value by first checking its uppercase and then its lowercase form; if both fail, it creates and returns an instance representing the unknown value while issuing a warning.*


### _missing_ (method, L94-L110, parent: CaseInSensitiveEnum)

> *Summary: This method attempts to resolve an input `value` into a specific enum member by first checking for uppercase and then lowercase matches. If both fail, it warns the user and attempts to create a custom instance of the enum using the provided value as its name and value, returning `None` upon failure.*


### FunctionCallingConfigMode (class, L113-L120)

> *Summary: Defines an enumeration to specify different modes for function calling configurations. It provides predefined states such as `AUTO`, `ANY`, `NONE`, and `VALIDATED` for controlling how function calls are handled.*


### LatLng (class, L123-L139)

> *Summary: Represents a geographic coordinate pair using latitude and longitude as floating-point numbers. It enforces WGS84 standards, requiring latitude to be between -90.0 and 90.0, and longitude between -180.0 and 180.0.*


### FunctionCallingConfig (class, L142-L153)

> *Summary: Defines configuration for controlling how an AI model handles function calls. It accepts optional settings like a specific calling mode, a list of permitted function names when the mode is set to "ANY," and a flag to stream function call arguments.*


### RetrievalConfig (class, L156-L160)

> *Summary: Defines configuration parameters for retrieval operations, accepting optional geographical coordinates (`lat_lng`) and a user's preferred `language_code`. These inputs guide how information is retrieved based on location and language context.*


### ToolConfig (class, L163-L175)

> *Summary: Defines a configuration structure for tools shared across requests, allowing optional settings for function calling and retrieval. It also includes a boolean flag to control whether the server should report tool invocations.*

