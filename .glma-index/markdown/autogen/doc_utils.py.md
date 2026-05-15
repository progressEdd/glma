# autogen/doc_utils.py

2 function(s): export_module, get_target_module.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| export_module | function |  |
| get_target_module | function |  |

## Chunks

### export_module (function, L18-L26)

> *Summary: This function returns a decorator that registers a class within a specified module mapping. It inspects the decorated class's original module and maps its fully qualified name to the provided module string in an internal registry.*


### get_target_module (function, L29-L35)

> *Summary: Determines the intended documentation module for an object by checking its `__module__` and `__name__`. It returns a specific module string from a predefined mapping if the fully qualified name exists, otherwise it returns `None`.*

