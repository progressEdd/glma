# cli/src/ag2_cli/commands/proxy.py

13 function(s): _parse_cli_help, _load_openapi_spec, _openapi_type_to_python, _parse_openapi_spec, _inspect_module_functions, _wrap_scripts, _python_type, _generate_tool_file, _display_tools, proxy_cli and 3 more. 2 class(es): ToolParam, ToolSpec.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ToolParam | class |  |
| ToolSpec | class |  |
| _parse_cli_help | function |  |
| _load_openapi_spec | function |  |
| _openapi_type_to_python | function |  |
| _parse_openapi_spec | function |  |
| _inspect_module_functions | function |  |
| _wrap_scripts | function |  |
| _python_type | function |  |
| _generate_tool_file | function |  |
| _display_tools | function |  |
| proxy_cli | function |  |
| proxy_openapi | function |  |
| proxy_module | function |  |
| proxy_scripts | function |  |

## Chunks

### ToolParam (class, L38-L45)

> *Summary: Defines a structure to hold metadata for a generated tool's parameters. It accepts a name, type (defaulting to string), description, required status, and an optional default value.*


### ToolSpec (class, L49-L56)

> *Summary: Defines the structure for a tool specification, holding metadata like name, description, and parameters. It also specifies where the tool originates from (e.g., CLI, OpenAPI) and contains its implementation code.*


### _parse_cli_help (function, L64-L172)

> *Summary: Executes the help command for a given CLI tool and subcommand to parse its usage information. It captures stdout/stderr from the `--help` output, extracts the description by scanning sections like "NAME," and identifies available flags/options using regex to build a `ToolSpec`. The resulting spec includes the parsed name, description, parameters (with types), and generated Python code for execution.*


### _load_openapi_spec (function, L180-L199)

> *Summary: Reads an OpenAPI specification from either a local file path or a remote URL. It automatically detects and parses the content as YAML (using `pyyaml`) if the source suggests it, otherwise it defaults to JSON parsing.*


### _openapi_type_to_python (function, L202-L213)

> *Summary: Converts an OpenAPI schema dictionary into a corresponding Python type hint string. It maps standard OpenAPI types like "string," "integer," and "object" to their Python equivalents such as `"str"` or `"dict"`.*


### _parse_openapi_spec (function, L216-L331)

> *Summary: Parses an OpenAPI specification dictionary to generate a list of `ToolSpec` objects. It extracts the base URL and iterates through paths and operations, converting path/query parameters and request body properties into structured tool parameters and generating corresponding Python implementation code using `httpx`.*


### _inspect_module_functions (function, L339-L392)

> *Summary: This function imports a specified Python module and introspects it to extract `ToolSpec` objects from its public functions. It analyzes each function's signature and docstring to build tool definitions, returning a list of these specifications.*


### _wrap_scripts (function, L400-L438)

> *Summary: This function scans a specified directory for executable shell or Python scripts and converts each one into an AG2 `ToolSpec`. It returns a list of these tool specifications, where each script is wrapped to execute with provided arguments.*


### _python_type (function, L446-L449)

> *Summary: Converts a string representation of a type into its corresponding Python annotation format using a predefined map. If the input type is not found in the map, it defaults to returning `"str"`.*


### _generate_tool_file (function, L452-L497)

> *Summary: Constructs a Python file containing functions for specified tools by analyzing their parameters and implementations. It takes a list of `ToolSpec` objects and an output path, returning the generated code string while optionally writing it to disk.*


### _display_tools (function, L500-L511)

> *Summary: This function renders a summary table of provided tool specifications to the console. It takes a list of `ToolSpec` objects and outputs a formatted display showing each tool's name, source type, parameter count, and truncated description.*


### proxy_cli (function, L520-L565)

> *Summary: This function generates Python tool functions by parsing the help documentation of a specified CLI command and its optional subcommands. It takes the base command name, comma-separated subcommands, an output path, and a preview flag as input, ultimately either displaying the generated code or writing it to the specified file.*


### proxy_openapi (function, L569-L617)

> *Summary: Loads an OpenAPI specification from a URL or file path to generate Python tool functions representing the API's endpoints. It optionally filters by operation IDs and can either preview the generated code or write it to a specified output file.*


### proxy_module (function, L621-L661)

> *Summary: Wraps specified functions from a given Python module into AG2 tool definitions. It takes the module name and optional function names as input, then outputs the generated code to a specified file path or previews it if requested.*


### proxy_scripts (function, L665-L696)

> *Summary: This function takes a directory of shell scripts and an optional output path to wrap them as Python tool functions. It processes the scripts, displays available tools, and either prints the generated code for preview or writes it to the specified file.*

