# autogen/coding/func_with_reqs.py

5 function(s): _to_code, _import_to_str, with_requirements, _build_python_functions_file, to_stub. 5 class(es): Alias, ImportFromModule, _StringLoader, FunctionWithRequirementsStr, FunctionWithRequirements. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _to_code | function |  |
| Alias | class |  |
| ImportFromModule | class |  |
| _import_to_str | function |  |
| _StringLoader | class |  |
| FunctionWithRequirementsStr | class |  |
| FunctionWithRequirements | class |  |
| with_requirements | function |  |
| _build_python_functions_file | function |  |
| to_stub | function |  |

## Chunks

### _to_code (function, L23-L31)

> *Summary: Converts a callable or string representation of a function into its source code as a string. It retrieves the source using `inspect.getsource` and strips any leading decorator syntax if present.*


### Alias (class, L35-L37)

> *Summary: Represents a mapping between two names, storing the original `name` and its corresponding `alias`. This structure is used to define alternative identifiers for existing entities.*


### ImportFromModule (class, L41-L43)

> *Summary: Represents a dependency structure where the class holds the name of a module and a list of imported items, which can be strings or aliases. This structure defines what external components are needed for a given context.*


### _import_to_str (function, L49-L63)

> *Summary: Converts an `Import` object into its corresponding Python import string representation. It handles direct imports (`import module`), aliased imports (`import module as alias`), and `from ... import ...` statements based on the structure of the input object.*


### _StringLoader (class, L66-L77)

> *Summary: This class wraps a string input to act as a source loader for code generation tasks. It provides methods to retrieve the raw string content or its UTF-8 encoded byte representation based on provided names or paths.*


### __init__ (method, L67-L68, parent: _StringLoader)

> *Summary: Initializes an object by storing a string input as its internal `data` attribute. This sets up the instance with the provided textual information for later use.*


### get_source (method, L70-L71, parent: _StringLoader)

> *Summary: Retrieves the stored source code string associated with a given fully qualified name. It directly returns the `self.data` attribute as the output.*


### get_data (method, L73-L74, parent: _StringLoader)

> *Summary: Encodes the internal data attribute into a UTF-8 byte string using the provided file path as input. It returns the resulting `bytes` object.*


### get_filename (method, L76-L77, parent: _StringLoader)

> *Summary: Prepends a fixed string to the provided full name and appends `.py` to construct a simulated filename. This method takes a string input and returns a modified string representing a file path.*


### FunctionWithRequirementsStr (class, L81-L114)

> *Summary: This class compiles a Python function provided as a string input, along with specified packages and imports. It parses the string to create an executable module containing exactly one function, storing that compiled function for later use.*


### __init__ (method, L88-L111, parent: FunctionWithRequirementsStr)

> *Summary: Initializes an object by dynamically compiling a Python function provided as a string input. It loads and executes the code to ensure it contains exactly one callable function, storing this compiled function internally for later use.*


### __call__ (method, L113-L114, parent: FunctionWithRequirementsStr)

> *Summary: This method explicitly prevents direct invocation of the object by raising a `NotImplementedError`. It serves as a placeholder indicating that string-based functions requiring specific objects cannot be called this way.*


### FunctionWithRequirements (class, L118-L137)

> *Summary: This class wraps a callable function along with its required Python packages and global imports. It allows instantiation from either an existing callable or a string representation, and can be invoked directly to execute the wrapped function.*


### from_callable (method, L124-L127, parent: FunctionWithRequirements)

> *Summary: Creates an instance of a `FunctionWithRequirements` object by wrapping a provided callable function. It accepts optional lists of Python packages and global imports to associate with the wrapped function.*


### from_str (method, L130-L133, parent: FunctionWithRequirements)

> *Summary: Constructs a `FunctionWithRequirementsStr` object from provided string representations of the function name, required Python packages, and global imports. It serves as a simple factory method to initialize this data structure.*


### __call__ (method, L136-L137, parent: FunctionWithRequirements)

> *Summary: This method acts as a callable wrapper that executes the stored function with any provided positional and keyword arguments. It returns the result produced by calling the underlying function.*


### with_requirements (function, L140-L161)

> *Summary: This decorator accepts lists of Python packages and imports to wrap another function. It returns a new object that encapsulates the original function along with its specified dependencies for execution context management.*


### _build_python_functions_file (function, L164-L178)

> *Summary: This function generates a string containing Python code by first aggregating all necessary global imports from a list of provided functions. It then concatenates these imports with the generated source code for each input function to produce a complete, runnable file content string.*


### to_stub (function, L181-L203)

> *Summary: Generates a string representation of a function stub based on its signature and documentation. It accepts either a callable or a specialized structure containing a function, returning the formatted stub code as a string.*

