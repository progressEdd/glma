# autogen/beta/types.py

2 class(es): Omit, StandardDataclass. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Omit | class |  |
| StandardDataclass | class |  |

## Chunks

### Omit (class, L78-L80)

> *Summary: Represents a placeholder that always evaluates to `False` when checked for truthiness. This class is used within the system's type definitions to signify exclusion or omission of data.*


### __bool__ (method, L79-L80, parent: Omit)

> *Summary: This method ensures that any instance of the class evaluates to `False` in a boolean context. It overrides Python's truthiness check to always return `False`.*


### StandardDataclass (class, L97-L100)

> *Summary: Defines a protocol requiring the presence of `__dataclass_fields__` on an object. This allows runtime type checking to determine if an instance adheres to the structure of a standard Python dataclass.*

