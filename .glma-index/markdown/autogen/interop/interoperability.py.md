# autogen/interop/interoperability.py

1 class(es): Interoperability. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Interoperability | class |  |

## Chunks

### Interoperability (class, L15-L71)

> *Summary: Manages cross-tool compatibility by providing methods to retrieve and convert arbitrary tool objects into specific interoperability types based on a provided string identifier. It relies on an internal registry to validate supported types and execute the necessary conversion logic.*


### convert_tool (method, L25-L40, parent: Interoperability)

> *Summary: This method transforms an arbitrary tool object into a specific interoperability format based on a provided string type. It retrieves the appropriate conversion class and delegates the actual transformation to that class's `convert_tool` method.*


### get_interoperability_class (method, L43-L62, parent: Interoperability)

> *Summary: This method retrieves a specific interoperability class type from a registry based on an input string identifier. It validates the provided `type` against the registry's supported types, raising a `ValueError` if the requested type is unsupported before returning the corresponding class object.*


### get_supported_types (method, L65-L71, parent: Interoperability)

> *Summary: Retrieves and returns a sorted list of string identifiers for all interoperability types registered within a given class's registry. The input is a class object, and the output is a sorted list of supported type strings.*

