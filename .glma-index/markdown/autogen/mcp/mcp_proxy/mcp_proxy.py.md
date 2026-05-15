# autogen/mcp/mcp_proxy/mcp_proxy.py

2 function(s): optional_temp_path, add_to_builtins. 1 class(es): MCPProxy. 33 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| optional_temp_path | function |  |
| add_to_builtins | function |  |
| MCPProxy | class |  |

## Chunks

### optional_temp_path (function, L49-L54)

> *Summary: If no path is provided, it yields an iterator over a newly created temporary directory; otherwise, it yields the specified path converted to a `Path` object. This function provides either a temporary or user-defined directory path as an iterable of `Path` objects.*


### add_to_builtins (function, L58-L70)

> *Summary: This function temporarily injects new global variables into the `builtins` module using a provided dictionary. It ensures that all injected variables are restored to their original state or removed upon completion via a `finally` block.*


### MCPProxy (class, L73-L582)

> *Summary: This class acts as a proxy to generate and manage client interfaces from OpenAPI schemas. It accepts server configurations and an OpenAPI definition (via URL or string) to create callable methods that execute HTTP requests, handling parameter mapping, security application, and configuration dumping for various use cases like LLM integration.*


### __init__ (method, L74-L86, parent: MCPProxy)

> *Summary: Initializes a proxy object designed to generate clients from an OpenAPI schema. It stores configuration details like server endpoints and title, while setting up internal structures for security definitions, tags, and function grouping.*


### _convert_camel_case_within_braces_to_snake (method, L89-L97, parent: MCPProxy)

> *Summary: This utility transforms specific substrings enclosed in curly braces from CamelCase to snake\_case. It uses regular expressions to locate these patterns and applies a nested conversion function to insert underscores before capital letters and lowercase the entire content within the braces.*


### _get_params (method, L100-L115, parent: MCPProxy)

> *Summary: This method analyzes a function's signature and an incoming URL path to categorize expected parameters. It returns sets of query, path, and optional body/security parameters, along with the presence of a request body.*


### get_mcp (method, L117-L126, parent: MCPProxy)

> *Summary: Instantiates a `FastMCP` object using the instance's title and provided settings. It then iterates through registered functions, attempting to register each one with the new MCP instance while logging warnings for any Pydantic validation failures during registration.*


### _process_params (method, L128-L155, parent: MCPProxy)

> *Summary: This method constructs the final request URL, query parameters, and JSON body by parsing a provided process path template against function arguments. It handles parameter expansion, serializes input data into a JSON body, and integrates security configurations before returning the complete request components.*


### set_security_params (method, L157-L169, parent: MCPProxy)

> *Summary: Updates the internal security configuration with provided parameters, optionally applying them to a specific named security context. It validates that the new parameters are compatible with the existing security definition if a name is supplied.*


### _get_matching_security (method, L171-L178, parent: MCPProxy)

> *Summary: Iterates through a list of available securities, returning the first one whose `accept` method validates against provided security parameters. If no matching security is found after checking all options, it raises a `ValueError`.*


### _get_security_params (method, L180-L197, parent: MCPProxy)

> *Summary: Retrieves the configured security parameters and a matching security object based on a provided method name. It first checks for specific security settings; if none are found, it falls back to default parameters or raises an error.*


### _request (method, L199-L241, parent: MCPProxy)

> *Summary: This method returns a decorator that wraps functions to proxy HTTP requests. It takes the desired HTTP `method`, target `path`, and optional security/description metadata, then intercepts calls to apply security checks before executing the underlying request using the `requests` library. The decorated function ultimately returns the JSON response from the external service.*


### put (method, L243-L244, parent: MCPProxy)

> *Summary: This method constructs and returns a callable function that executes an HTTP PUT request to the specified `path`, forwarding all provided keyword arguments. It acts as a wrapper around the internal request mechanism for performing updates or replacements at a given endpoint.*


### get (method, L246-L247, parent: MCPProxy)

> *Summary: This method acts as a wrapper to initiate an HTTP GET request. It takes a `path` string and optional keyword arguments, returning a callable function that executes the underlying request.*


### post (method, L249-L250, parent: MCPProxy)

> *Summary: This method acts as a wrapper to execute an HTTP POST request. It takes a target `path` and arbitrary keyword arguments, returning a callable function that performs the actual request via an internal helper.*


### delete (method, L252-L253, parent: MCPProxy)

> *Summary: This method constructs and returns a callable function that executes an HTTP DELETE request against a specified resource path. It delegates the actual network operation to an internal `_request` helper method.*


### head (method, L255-L256, parent: MCPProxy)

> *Summary: This method initiates an HTTP HEAD request to a specified `path` using the internal request mechanism. It returns a callable function that executes this head request and yields a dictionary containing the response data.*


### patch (method, L258-L259, parent: MCPProxy)

> *Summary: This method initiates a PATCH request to a specified endpoint using provided arguments. It returns a callable function that executes the HTTP patch operation against the target resource.*


### _get_template_dir (method, L262-L266, parent: MCPProxy)

> *Summary: Determines the location of template files by constructing a path relative to the current module's location and verifies its existence, raising an error if it is missing. Returns the `Path` object pointing to the templates directory upon success.*


### generate_code (method, L270-L305, parent: MCPProxy)

> *Summary: This method generates Python code from an OpenAPI YAML string, saving the resulting client implementation to a specified directory. It configures template directories and custom visitors before reading the generated `main.py` file, performing minor path adjustments, and overwriting it with the modified content.*


### set_globals (method, L307-L311, parent: MCPProxy)

> *Summary: This method extracts public attributes from a given module, filtering them to retain only those objects whose module belongs to either `models_<suffix>` or `typing`. The resulting dictionary of selected globals is then stored internally.*


### create (method, L315-L376, parent: MCPProxy)

> *Summary: Constructs an `MCPProxy` instance by generating code from an OpenAPI specification (provided as a string or URL). It processes the spec based on configuration flags like function renaming and grouping, then returns the initialized proxy object.*


### _get_authentications (method, L378-L393, parent: MCPProxy)

> *Summary: Retrieves a list of unique authentication configurations from the instance's security settings. It iterates through all defined securities, filters out unsupported types, and ensures each configuration is added only once based on its serialized parameters before returning the collected dictionaries.*


### dump_configurations (method, L395-L407, parent: MCPProxy)

> *Summary: Iterates over defined function groups to serialize configurations for each group into separate JSON files within the specified output directory. It also writes a master configuration file containing all registered functions to the root of the provided directory.*


### dump_configuration (method, L409-L439, parent: MCPProxy)

> *Summary: Generates a configuration file by rendering a Jinja2 template using provided server details and function metadata. It takes an output path and an optional list of functions to include in the generated configuration structure.*


### load_configuration (method, L441-L445, parent: MCPProxy)

> *Summary: Reads the content of a specified configuration file path and then passes that raw string data to an internal method for parsing and loading. This function takes a file path as input and modifies the object's state based on the file's contents.*


### load_configuration_from_string (method, L447-L459, parent: MCPProxy)

> *Summary: Parses a JSON string containing configuration data to initialize the proxy's state. It extracts server URLs, sets security parameters based on authentication definitions, and filters registered functions to only include those matching specified operations.*


### _get_functions_to_register (method, L461-L499, parent: MCPProxy)

> *Summary: Determines which registered methods should be exposed by accepting either a list of function names or a dictionary mapping names to metadata. It returns a dictionary pairing the actual callable objects with their corresponding name and description metadata, raising an error if requested functions are missing from the registry.*


### _remove_pydantic_undefined_from_tools (method, L502-L528, parent: MCPProxy)

> *Summary: This method iterates through a list of tool definitions and modifies them by removing Pydantic's `Undefined` defaults from parameters that are otherwise optional. When such a default is removed, the corresponding parameter name is added to the required parameters list for that function.*


### _register_for_llm (method, L530-L543, parent: MCPProxy)

> *Summary: This method registers a set of provided functions with an agent for LLM interaction, using metadata to define the function's name and description. It then cleans up the agent's tool configuration by removing any undefined Pydantic entries.*


### _register_for_execution (method, L545-L553, parent: MCPProxy)

> *Summary: This method registers a set of functions with a specified agent for execution. It processes the input function mappings to call `agent.register_for_execution` for each function, linking it to its designated name.*


### get_functions (method, L555-L556, parent: MCPProxy)

> *Summary: This method is deprecated and raises a warning, directing users to utilize the `function_names` property for retrieving available functions. It currently returns no meaningful data due to its obsolete status.*


### function_names (method, L559-L560, parent: MCPProxy)

> *Summary: Retrieves a list of string names corresponding to all registered functions held by the instance. It iterates over internal registered functions and extracts their names as output.*


### get_function (method, L562-L566, parent: MCPProxy)

> *Summary: Retrieves a registered callable function by its string name from an internal dictionary. It iterates through stored functions and returns the matching one, raising a `ValueError` if no function with that name exists.*


### set_function (method, L568-L574, parent: MCPProxy)

> *Summary: Updates an existing registered function by replacing it with a new callable, provided the function's name matches one in the internal registry. If no matching named function is found, it raises a `ValueError`.*


### inject_parameters (method, L576-L582, parent: MCPProxy)

> *Summary: This method is intended to inject parameters into registered functions based on a provided name and keyword arguments. Currently, it raises a `NotImplementedError`, indicating the functionality is incomplete.*

