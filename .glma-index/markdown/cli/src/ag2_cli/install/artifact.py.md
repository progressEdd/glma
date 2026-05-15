# cli/src/ag2_cli/install/artifact.py

12 function(s): _pluralize_type, parse_artifact_id, _parse_variable_spec, _parse_remote_file, _parse_template_config, _parse_tool_config, _parse_dataset_config, _parse_agent_config, _parse_bundle_config, load_artifact_json and 2 more. 11 class(es): VariableSpec, RemoteFile, SkillsConfig, TemplateConfig, ToolConfig, DatasetConfig, AgentConfig, BundleRef, BundleConfig, Artifact, InstallResult. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| VariableSpec | class |  |
| RemoteFile | class |  |
| SkillsConfig | class |  |
| TemplateConfig | class |  |
| ToolConfig | class |  |
| DatasetConfig | class |  |
| AgentConfig | class |  |
| BundleRef | class |  |
| BundleConfig | class |  |
| Artifact | class |  |
| _pluralize_type | function |  |
| parse_artifact_id | function |  |
| InstallResult | class |  |
| _parse_variable_spec | function |  |
| _parse_remote_file | function |  |
| _parse_template_config | function |  |
| _parse_tool_config | function |  |
| _parse_dataset_config | function |  |
| _parse_agent_config | function |  |
| _parse_bundle_config | function |  |
| load_artifact_json | function |  |
| load_legacy_manifest | function |  |
| load_artifact | function |  |

## Chunks

### VariableSpec (class, L11-L15)

> *Summary: Defines a structure to hold configuration for user input, including a prompt message, a default value, an optional transformation function, and a set of predefined choices. This class serves as a blueprint for defining interactive prompts within the CLI tool.*


### RemoteFile (class, L19-L23)

> *Summary: Represents a file accessible remotely, storing its name, URL, optional size, and SHA256 checksum. This structure holds metadata necessary for downloading or referencing an external artifact.*


### SkillsConfig (class, L27-L29)

> *Summary: Defines configuration settings for skills, specifying a default directory path and whether automatic installation should be enabled. It holds static attributes that control the behavior of skill installations.*


### TemplateConfig (class, L33-L37)

> *Summary: This configuration class holds settings for artifact installation, including a default scaffold path, customizable variables, file patterns to ignore during installation, and a list of post-installation scripts. It provides a structured way to define how templates should be deployed.*


### ToolConfig (class, L41-L51)

> *Summary: This class defines a configuration structure for an installed tool, holding metadata such as its kind, source path, runtime environment, and installation destination. It also manages lists of associated functions, provided tools, and external dependencies required by the tool.*


### DatasetConfig (class, L55-L61)

> *Summary: This class holds configuration parameters for a dataset, including inline data, remote file locations, expected format (defaulting to "jsonl"), schema definition, split mappings, and an evaluation compatibility flag. It serves as a structured container for defining how a dataset should be loaded and processed.*


### AgentConfig (class, L65-L72)

> *Summary: This class defines a configuration structure for an agent, holding settings like the source file, model name, maximum conversation turns, and lists of tools or skills to preload. It provides default values for these parameters, allowing easy setup of agent behavior.*


### BundleRef (class, L76-L78)

> *Summary: Represents a reference to an artifact bundle, storing the bundle's identifier as a string and indicating if its presence is mandatory. It serves as a simple data structure for tracking required dependencies.*


### BundleConfig (class, L82-L84)

> *Summary: This configuration object holds a list of artifact references and defines a fixed installation sequence for those artifacts. The default order prioritizes skills, tools, templates, datasets, and agents during deployment.*


### Artifact (class, L91-L121)

> *Summary: Represents a package artifact with metadata such as name, type, owner, and dependencies. It provides computed properties for generating fully qualified names (`owner/name`) and canonical references (`type_dir/owner/name`).*


### qualified_name (method, L113-L115, parent: Artifact)

> *Summary: Generates a fully qualified string identifier by concatenating the object's owner and name, separated by a slash. This method returns a single string representing the complete artifact path.*


### ref (method, L118-L121, parent: Artifact)

> *Summary: Generates a canonical string reference by combining the pluralized type, owner, and name of the artifact. This method outputs a structured path suitable for referencing the artifact within the system.*


### _pluralize_type (function, L124-L135)

> *Summary: This utility maps a singular artifact type string to its corresponding plural directory name using a predefined dictionary. It returns the mapped plural name if found, otherwise it returns the original input type unchanged.*


### parse_artifact_id (function, L138-L149)

> *Summary: This function takes an artifact ID string and parses it into a tuple containing the owner and the name. If a slash is present, it splits the input; otherwise, it defaults to using a predefined owner for the entire string as the name.*


### InstallResult (class, L153-L158)

> *Summary: This class aggregates the outcome of an installation process, storing references to the installed artifact and lists detailing created files, targets used, dependencies installed, and any encountered warnings. It serves as a comprehensive data structure for reporting installation success or failure.*


### _parse_variable_spec (function, L164-L170)

> *Summary: Constructs a `VariableSpec` object from a raw dictionary input by extracting and assigning values for prompt, default, transform, and choices. It safely handles missing keys in the input dictionary by providing empty defaults where necessary.*


### _parse_remote_file (function, L173-L179)

> *Summary: Constructs a `RemoteFile` object from a dictionary containing file metadata. It extracts the name, URL, size, and SHA256 hash from the input dictionary, providing empty strings as defaults if keys are missing.*


### _parse_template_config (function, L182-L191)

> *Summary: Parses a raw dictionary configuration to construct a `TemplateConfig` object. It extracts scaffold paths, ignore lists, post-install commands, and processes variable definitions from the input dictionary.*


### _parse_tool_config (function, L194-L206)

> *Summary: Constructs a `ToolConfig` object by extracting and providing default values for various configuration fields from an input dictionary. It maps keys like "kind," "source," and "runtime" to the corresponding attributes of the resulting configuration structure.*


### _parse_dataset_config (function, L209-L217)

> *Summary: Constructs a `DatasetConfig` object by extracting and processing configuration details from a raw dictionary input. It handles optional fields like inline data, remote file lists (which are recursively parsed), format, schema, splits, and evaluation compatibility flags.*


### _parse_agent_config (function, L220-L229)

> *Summary: Constructs an `AgentConfig` object by extracting configuration parameters from a raw dictionary input. It provides sensible default values for fields like source, model, and maximum turns if they are missing in the provided data.*


### _parse_bundle_config (function, L232-L242)

> *Summary: Parses a raw dictionary configuration to construct a `BundleConfig` object. It iterates over the "artifacts" list in the input, converting string references or dictionaries (which may specify requirements) into `BundleRef` objects, and sets a default installation order if none is provided.*


### load_artifact_json (function, L245-L290)

> *Summary: Reads a JSON file specified by a `Path` to construct an `Artifact` object. It parses various fields like name, owner, dependencies, and conditionally loads specific configurations (skills, template, tool, etc.) based on the artifact's type.*


### load_legacy_manifest (function, L293-L305)

> *Summary: Parses a `manifest.json` file located within a specified package directory to construct an `Artifact` object. It extracts metadata like name, description, and version from the JSON and configures it as a "skills" type artifact.*


### load_artifact (function, L308-L316)

> *Summary: Retrieves an artifact object from a specified directory by first checking for `artifact.json`; if that is absent, it attempts to load data using `manifest.json` as a fallback. Returns the loaded `Artifact` instance or `None` if neither file exists in the path.*

