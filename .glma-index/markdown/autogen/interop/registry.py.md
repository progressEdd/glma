# autogen/interop/registry.py

1 function(s): register_interoperable_class. 1 class(es): InteroperableRegistry. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| InteroperableRegistry | class |  |
| register_interoperable_class | function |  |

## Chunks

### InteroperableRegistry (class, L16-L41)

> *Summary: This class manages a central registry mapping short names to interoperable classes. It allows registering new types, retrieving registered classes by name, and listing both all available short names and those that are fully supported.*


### __init__ (method, L17-L18, parent: InteroperableRegistry)

> *Summary: Initializes an internal dictionary to store mappings between string identifiers and `Interoperable` class types. This structure serves as a central registry for interoperability components.*


### register (method, L20-L26, parent: InteroperableRegistry)

> *Summary: This method adds a new class to the internal registry using a unique string identifier. It accepts a short name and an `InteroperableClass`, storing the class if the name is not already present, and returns the registered class.*


### get_short_names (method, L28-L29, parent: InteroperableRegistry)

> *Summary: Retrieves a sorted list of all registered keys from the internal registry. This method takes no input and returns a `list[str]` containing the short names.*


### get_supported_types (method, L31-L34, parent: InteroperableRegistry)

> *Summary: Retrieves a list of type names from the registry that are currently supported. It filters the available short names by checking if their corresponding entry has no recorded reason for being unsupported.*


### get_class (method, L36-L37, parent: InteroperableRegistry)

> *Summary: Retrieves a class object from an internal registry using a provided string identifier. It returns the corresponding `Interoperable` type if the key exists in the registry map.*


### get_instance (method, L40-L41, parent: InteroperableRegistry)

> *Summary: Retrieves a singleton instance of the `InteroperableRegistry` by accessing a pre-registered global variable. This method requires no input other than the class type itself to return the existing registry object.*


### register_interoperable_class (function, L50-L70)

> *Summary: This function returns a decorator that registers an `Interoperable` class using a provided short name into a global registry. When applied to a class, it modifies the class by adding it to the system's known interoperability types.*

