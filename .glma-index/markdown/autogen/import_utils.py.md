# autogen/import_utils.py

7 function(s): optional_import_block, get_missing_imports, patch_object, require_optional_import, _mark_object, run_for_optional_imports, skip_on_missing_imports. 8 class(es): ModuleInfo, Result, PatchObject, PatchCallable, PatchStatic, PatchInit, PatchProperty, PatchClass. 26 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ModuleInfo | class |  |
| Result | class |  |
| optional_import_block | function |  |
| get_missing_imports | function |  |
| PatchObject | class |  |
| PatchCallable | class |  |
| PatchStatic | class |  |
| PatchInit | class |  |
| PatchProperty | class |  |
| PatchClass | class |  |
| patch_object | function |  |
| require_optional_import | function |  |
| _mark_object | function |  |
| run_for_optional_imports | function |  |
| skip_on_missing_imports | function |  |

## Chunks

### ModuleInfo (class, L33-L151)

> *Summary: This class encapsulates module metadata, including name and optional version constraints. It provides methods to check if a specified module is installed in the system and satisfies its defined version requirements, returning an error message or `None` upon success. A static method allows parsing a string representation of module requirements into this object.*


### is_in_sys_modules (method, L40-L89, parent: ModuleInfo)

> *Summary: Checks if a specified module is available in `sys.modules` and verifies its version against defined minimum and maximum constraints. It returns `None` upon success, or a descriptive string detailing installation issues, path conflicts, or version mismatches.*


### __repr__ (method, L91-L97, parent: ModuleInfo)

> *Summary: Generates a string representation of the object, incorporating its name and optional version constraints (minimum and maximum) based on inclusivity flags. The output is a formatted string detailing the package or module's identity and required version range.*


### from_str (method, L100-L151, parent: ModuleInfo)

> *Summary: Parses a string containing module name and optional version constraints into a structured `ModuleInfo` object. It uses regex to extract the package name and then analyzes constraint operators (like `>=`, `<`, etc.) within the string to populate minimum and maximum version bounds.*


### Result (class, L154-L162)

> *Summary: Represents the outcome of an operation, tracking whether it has failed. It exposes a read-only property that raises an error if the result state hasn't been determined yet.*


### __init__ (method, L155-L156, parent: Result)

> *Summary: Initializes an instance by setting a private attribute, `_failed`, to `None` to track the success or failure state of subsequent operations.*


### is_successful (method, L159-L162, parent: Result)

> *Summary: Checks the internal state to determine if a process completed successfully. It returns `True` if no failure flag has been set, otherwise it raises an error if the result hasn't been determined yet.*


### optional_import_block (function, L166-L186)

> *Summary: Provides a generator-based context manager that temporarily suppresses `ImportError` exceptions within its scope. It yields a result object, marking it as failed if an import error occurs during the block's execution.*


### get_missing_imports (function, L189-L203)

> *Summary: Accepts a single or iterable of module names and returns a dictionary mapping the name of each module to `True` if it is present in the system modules. It filters out any modules that are not found within the current environment's installed packages.*


### PatchObject (class, L211-L278)

> *Summary: This abstract class defines a mechanism for patching an existing object by handling missing dependencies. It accepts an object and metadata (missing modules and dependency target), and requires subclasses to implement logic for accepting the object type and performing the actual patch operation. The class provides utility methods to generate informative error messages and register concrete implementations via a factory method.*


### __init__ (method, L212-L218, parent: PatchObject)

> *Summary: Initializes an object by first validating that the provided target object can be patched. It then stores references to the object, a dictionary of modules needing replacement, and a dependency target string for later use.*


### accept (method, L222-L222, parent: PatchObject)

> *Summary: Checks if a given object conforms to the structure of a specified class type. It returns `True` if the object matches the expected structure and `False` otherwise.*


### patch (method, L225-L225, parent: PatchObject)

> *Summary: Applies a patch to the object instance, excluding any specified types listed in `except_for`. It returns the patched object of type `T`.*


### get_object_with_metadata (method, L227-L228, parent: PatchObject)

> *Summary: Retrieves the stored object, including any associated metadata, from the instance's internal attribute. This method returns the complete object representation held by the class.*


### msg (method, L231-L240, parent: PatchObject)

> *Summary: Generates a detailed error message string indicating which modules are missing for a specific object. It constructs the message based on whether one or multiple dependencies are absent, listing each missing module and providing a suggested `pip install` command.*


### copy_metadata (method, L242-L255, parent: PatchObject)

> *Summary: This method copies essential metadata attributes like `__doc__`, `__name__`, and `__module__` from an original object to a provided patched object. It ensures the resulting object inherits key descriptive information from its source counterpart.*


### register (method, L260-L265, parent: PatchObject)

> *Summary: This function acts as a decorator that registers a provided class into an internal registry list. It accepts any subclass of `PatchObject` and returns the decorated class after adding it to the system's collection.*


### create (method, L268-L278, parent: PatchObject)

> *Summary: It attempts to find a suitable handler within the class's registry that can accept an input object; if found, it instantiates and returns that handler with provided configuration details. Otherwise, it returns `None`.*


### PatchCallable (class, L282-L300)

> *Summary: This class wraps a callable object to intercept calls, allowing for selective patching based on the function's name. If the wrapped function's name is not in an exclusion list, it replaces the original with a new function that always raises an `ImportError` containing a specified message.*


### accept (method, L284-L285, parent: PatchCallable)

> *Summary: Checks if a given object is either a function or a method using Python's `inspect` module. Returns `True` if it matches either type, otherwise returns `False`.*


### patch (method, L287-L300, parent: PatchCallable)

> *Summary: This method replaces an existing callable object with a new wrapper function that always raises an `ImportError` containing a specific message, unless the original object's name is in the provided exclusion list. It returns this newly created replacement function.*


### PatchStatic (class, L304-L331)

> *Summary: This class intercepts and replaces `staticmethod` objects by wrapping the original function with a new callable that always raises an `ImportError`. It accepts any object, checks if it's a `staticmethod`, and returns the modified static method wrapper.*


### accept (method, L306-L308, parent: PatchStatic)

> *Summary: Checks if an object is a `staticmethod` instance. It takes a class and an object as input and returns a boolean indicating the type match.*


### patch (method, L310-L328, parent: PatchStatic)

> *Summary: This method replaces an existing object's functionality with a wrapper that always raises an `ImportError` containing a specific message. It checks if the target object's name is in the provided exclusion list before applying this replacement.*


### get_object_with_metadata (method, L330-L331, parent: PatchStatic)

> *Summary: Retrieves the underlying function object from the instance's attribute, effectively returning the callable associated with the object.*


### PatchInit (class, L335-L355)

> *Summary: This class intercepts and replaces the `__init__` method of an object if its name is not in a specified exclusion list. It substitutes the original initializer with a static method that always raises an `ImportError`, effectively preventing instantiation while retaining metadata about the original function.*


### accept (method, L337-L338, parent: PatchInit)

> *Summary: Checks if a given object is an instance method descriptor specifically named `__init__`. Returns `True` only if both conditions are met.*


### patch (method, L340-L352, parent: PatchInit)

> *Summary: This method replaces an existing callable object with a new one that always raises an `ImportError` containing a specific message, unless the original function's name is in the provided exclusion list. It returns this newly wrapped static method for use as a replacement.*


### get_object_with_metadata (method, L354-L355, parent: PatchInit)

> *Summary: Retrieves the stored object, including any associated metadata, from the instance's internal attribute. This method returns the complete object structure held by the class.*


### PatchProperty (class, L359-L381)

> *Summary: This class wraps a data descriptor to intercept and replace its getter method with one that raises an `ImportError`. It accepts any object that is a data descriptor possessing an `fget` attribute, returning the modified `property` object upon successful patching.*


### accept (method, L361-L362, parent: PatchProperty)

> *Summary: Checks if an object is a data descriptor by verifying it's a datadescriptor and possesses an `fget` attribute. Returns `True` if both conditions are met, indicating the object can be treated as such.*


### patch (method, L364-L378, parent: PatchProperty)

> *Summary: This method replaces an existing getter function of a property with one that always raises an `ImportError` containing a specified message, unless the original getter's name is in the provided exclusion list. It returns a new `property` object wrapping this modified behavior.*


### get_object_with_metadata (method, L380-L381, parent: PatchProperty)

> *Summary: Retrieves the underlying object's file handle, which contains associated metadata. This method returns the raw file stream object from the instance.*


### PatchClass (class, L385-L408)

> *Summary: This class modifies a target class by iterating over its members and applying patches to each one using `patch_object`. It accepts any object that is a class and returns the modified class instance after patching all non-excluded members.*


### accept (method, L387-L388, parent: PatchClass)

> *Summary: Checks if a given object is a class type by using `inspect.isclass()`. It returns `True` if the input object is a class and `False` otherwise.*


### patch (method, L390-L408, parent: PatchClass)

> *Summary: Modifies an object's members by iterating through its attributes and applying patches to non-internal methods, unless the object's original name is in a specified exclusion list. It returns the modified object instance after attempting to replace eligible members with their patched versions.*


### patch_object (function, L411-L426)

> *Summary: Creates and applies a patching mechanism to an object based on specified missing modules and dependency targets. It returns the patched object or the original object if patching is not possible or necessary, handling exceptions as configured.*


### require_optional_import (function, L429-L454)

> *Summary: This function returns a decorator that conditionally patches an object based on whether specified optional modules are available. If dependencies are present, it returns an identity decorator; otherwise, it applies patching using the provided module list and dependency target.*


### _mark_object (function, L457-L466)

> *Summary: This utility wraps an object with a specific `pytest` marker derived from the input string, then further applies an auxiliary negative flag to that marked object. It takes any object and a dependency target name as input, returning the modified, decorated object.*


### run_for_optional_imports (function, L469-L510)

> *Summary: This function returns a decorator that wraps test functions or classes to conditionally execute them based on the presence of optional dependencies. It checks for missing modules and raises an `ImportError` if any required optional packages are not installed, guiding the user on how to install them via pip.*


### skip_on_missing_imports (function, L513-L539)

> *Summary: This function generates a decorator that conditionally skips tests based on the presence of optional modules. It takes module names and a dependency target, returning a decorator that either applies a test marker or uses `pytest.mark.skip` if any specified modules are missing, providing installation instructions in the skip message.*

