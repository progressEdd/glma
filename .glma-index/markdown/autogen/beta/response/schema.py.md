# autogen/beta/response/schema.py

2 function(s): make_adapter, _is_safe_subclass. 2 class(es): ResponseSchema, RawSchema. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ResponseSchema | class |  |
| RawSchema | class |  |
| make_adapter | function |  |
| _is_safe_subclass | function |  |

## Chunks

### ResponseSchema (class, L22-L124)

> *Summary: This class constructs a schema object from a Python type or `ClassInfo`, automatically deriving the name and description from metadata or JSON schema. It provides methods to ensure an existing object conforms to the schema and asynchronously validates a raw string response against the defined structure, returning the parsed data if embedded types are present.*


### __init__ (method, L24-L31, parent: ResponseSchema)

> *Summary: Initializes a response schema object by accepting the expected data type, an optional name and description, and a boolean flag to control embedding. This sets up the structure for representing structured responses from agents.*


### __init__ (method, L34-L41, parent: ResponseSchema)

> *Summary: Initializes a response schema object using provided class information and optional metadata like name, description, and embedding status. It sets up the structure for representing structured responses based on the input `ClassInfo`.*


### __init__ (method, L43-L69, parent: ResponseSchema)

> *Summary: Initializes a response schema object by generating an adapter and its corresponding JSON schema from provided type information. It then sets the name, defaulting to derived values or "ResponseSchema," and populates the description using schema metadata, docstrings, or defaults.*


### ensure_schema (method, L73-L76, parent: ResponseSchema)

> *Summary: This method validates and ensures that a given object conforms to the expected schema defined by the class. It takes a class type and an instance of that type as input, returning nothing upon successful validation.*


### ensure_schema (method, L80-L83, parent: ResponseSchema)

> *Summary: Validates and ensures a given object conforms to the expected response schema. It takes a class type and an instance of a proto message as input, returning a structured schema representation.*


### ensure_schema (method, L87-L90, parent: ResponseSchema)

> *Summary: This method validates and ensures that a given object conforms to the expected schema type. It takes a class definition and an instance of that type as input, returning a fully validated `ResponseSchema` object.*


### ensure_schema (method, L93-L101, parent: ResponseSchema)

> *Summary: This method validates and standardizes an input object against a defined schema. It returns the original `ResponseProto` if it's already of that type, otherwise, it constructs and returns a new instance using the provided schema information.*


### from_schema (method, L104-L111, parent: ResponseSchema)

> *Summary: Constructs a `RawSchema` instance from a provided dictionary schema. It accepts the class type, the schema dictionary, and optional name/description strings to initialize the object.*


### validate (method, L113-L124, parent: ResponseSchema)

> *Summary: Checks if a string response conforms to a schema using an internal adapter; it returns the parsed data if an embedded type is defined, otherwise it returns the full validation result.*


### RawSchema (class, L127-L153)

> *Summary: This class wraps a JSON schema definition along with metadata like name and description. Its primary behavior is to accept a raw string response from a model and return it unmodified after issuing a warning that automatic validation is not performed.*


### __init__ (method, L128-L138, parent: RawSchema)

> *Summary: Initializes an object by storing a JSON schema dictionary, a unique name, and an optional description. It sets up the core structure for defining structured responses based on the provided schema.*


### validate (method, L140-L153, parent: RawSchema)

> *Summary: This method accepts a raw string response and context object to perform validation. It issues a warning that it cannot actually validate the model's output and returns the input string unmodified.*


### make_adapter (function, L156-L195)

> *Summary: This function constructs and returns a `TypeAdapter` instance along with a boolean indicating if the resulting schema is embedded. It analyzes input type information to determine the appropriate final structure, handling cases like strings, tuples/lists, unions, dataclasses, and dictionaries differently before wrapping it in an optional one-field response model.*


### _is_safe_subclass (function, L198-L202)

> *Summary: Checks if a class inherits from a specified base or tuple of bases. It handles potential `TypeError` during the subclass check by testing the class's type instead.*

