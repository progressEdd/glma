# autogen/tools/function_utils.py

13 function(s): get_typed_annotation, get_typed_signature, get_typed_return_annotation, get_param_annotations, get_parameter_json_schema, get_required_params, get_default_values, get_parameters, get_missing_annotations, get_function_schema and 3 more. 4 class(es): Parameters, Function, ToolFunction, _SerializableResult.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_typed_annotation | function |  |
| get_typed_signature | function |  |
| get_typed_return_annotation | function |  |
| get_param_annotations | function |  |
| Parameters | class |  |
| Function | class |  |
| ToolFunction | class |  |
| get_parameter_json_schema | function |  |
| get_required_params | function |  |
| get_default_values | function |  |
| get_parameters | function |  |
| get_missing_annotations | function |  |
| get_function_schema | function |  |
| get_load_param_if_needed_function | function |  |
| load_basemodels_if_needed | function |  |
| _SerializableResult | class |  |
| serialize_to_str | function |  |

## Chunks

### get_typed_annotation (function, L36-L51)

> *Summary: This utility resolves a parameter's type annotation by first unwrapping `AG2Field` instances and then attempting to evaluate string-based annotations using the provided global namespace. It returns the fully resolved or wrapped type object.*


### get_typed_signature (function, L54-L75)

> *Summary: This utility extracts the full type-annotated signature of a given callable. It introspects the function's parameters and uses an auxiliary function to resolve any complex annotations found within its global scope, returning a complete `inspect.Signature` object.*


### get_typed_return_annotation (function, L78-L94)

> *Summary: Retrieves the fully typed return annotation from a given callable by inspecting its signature. If no explicit annotation exists, it returns `None`, otherwise it resolves the type using the function's global namespace.*


### get_param_annotations (function, L97-L108)

> *Summary: Extracts a mapping from parameter names to their type annotations from a given function signature object. It filters out any parameters that do not have an explicit annotation defined.*


### Parameters (class, L111-L116)

> *Summary: Represents the structure for defining function parameters according to the OpenAI API specification. It requires a dictionary of properties and a list specifying which properties are mandatory.*


### Function (class, L119-L124)

> *Summary: Represents a structure mirroring an OpenAI API function definition. It accepts and stores the function's description, name, and its associated parameters object as inputs.*


### ToolFunction (class, L127-L131)

> *Summary: Represents a structure conforming to the OpenAI API's definition for a callable tool. It requires a `function` object detailing the function's signature and description.*


### get_parameter_json_schema (function, L134-L164)

> *Summary: Generates a JSON schema object for a given function parameter by inspecting its type and associated metadata. It incorporates the parameter's default value from a provided dictionary and sets a description derived from the parameter's annotations.*


### get_required_params (function, L167-L176)

> *Summary: Extracts a list of parameter names from a given function signature that do not have a default value assigned. This allows developers to quickly identify arguments that must be provided when calling the associated function.*


### get_default_values (function, L179-L188)

> *Summary: Extracts a dictionary containing the default values for all parameters within a provided function signature object. It filters out any parameters that do not have an explicitly defined default value.*


### get_parameters (function, L191-L213)

> *Summary: Constructs a `Parameters` Pydantic model representing function arguments for the OpenAI API. It takes lists of required parameters, type annotations, and default values to build the schema properties and required fields.*


### get_missing_annotations (function, L216-L231)

> *Summary: Determines which parameters in a function signature lack type annotations based on a list of required arguments. It returns two sets: one containing the truly missing required annotations and another listing optional parameters that are currently unannotated.*


### get_function_schema (function, L235-L307)

> *Summary: Generates a JSON schema structure suitable for OpenAI API tool definitions from a Python callable. It inspects the function's signature to derive parameter types, required status, and default values, raising errors if mandatory parameters lack annotations.*


### get_load_param_if_needed_function (function, L310-L342)

> *Summary: This utility determines if a given type annotation represents a Pydantic model; if so, it returns a function capable of instantiating that model from a dictionary. Otherwise, it returns `None`, handling complex types like `Annotated` recursively.*


### load_basemodels_if_needed (function, L346-L388)

> *Summary: This decorator wraps a function to automatically instantiate Pydantic models for its arguments if they are provided as raw data. It returns either a synchronous or asynchronous wrapper that pre-processes the input keyword arguments before executing the original function.*


### _SerializableResult (class, L391-L392)

> *Summary: This class models a serializable result containing a single arbitrary value. It acts as a standardized container for output data from functions or tools.*


### serialize_to_str (function, L396-L412)

> *Summary: Converts various Python objects into a string representation for serialization. It prioritizes returning the object as-is if it's already a string, uses JSON dumping for `BaseModel` instances, and falls back to generic string conversion or JSON encoding otherwise.*

