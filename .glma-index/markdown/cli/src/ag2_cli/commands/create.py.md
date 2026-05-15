# cli/src/ag2_cli/commands/create.py

22 function(s): _to_var_name, _write_file, _detect_generation_model, _llm_generate, _parse_json_response, create_project, _create_project_from_description, create_agent, _create_agent_from_description, create_tool and 12 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _to_var_name | function |  |
| _write_file | function |  |
| _detect_generation_model | function |  |
| _llm_generate | function |  |
| _parse_json_response | function |  |
| create_project | function |  |
| _create_project_from_description | function |  |
| create_agent | function |  |
| _create_agent_from_description | function |  |
| create_tool | function |  |
| _create_tool_from_openapi | function |  |
| _create_tool_from_module | function |  |
| create_team | function |  |
| _artifact_json | function |  |
| _skill_md | function |  |
| _scaffold_template | function |  |
| _scaffold_tool | function |  |
| _scaffold_dataset | function |  |
| _scaffold_agent | function |  |
| _scaffold_skills | function |  |
| _scaffold_bundle | function |  |
| create_artifact | function |  |

## Chunks

### _to_var_name (function, L213-L215)

> *Summary: Converts a string input, which might contain hyphens or spaces, into a syntactically valid lowercase Python variable name by replacing those characters with underscores.*


### _write_file (function, L218-L221)

> *Summary: This utility function ensures the necessary directory structure exists for a given path before writing content to it. It takes a `Path` object and a string of `content`, saving the text to the specified file location.*


### _detect_generation_model (function, L255-L263)

> *Summary: Checks environment variables for specific API keys (OpenAI, Anthropic, Google) to automatically determine and return a corresponding LLM model identifier string, or `None` if no keys are found.*


### _llm_generate (function, L266-L304)

> *Summary: This function executes a single Large Language Model call using the `autogen` library, requiring an installed `ag2` package and an environment API key. It takes a user prompt and a system message as input, returning the generated text response from the LLM agent's chat history or summary.*


### _parse_json_response (function, L307-L331)

> *Summary: This utility attempts to extract and deserialize a Python dictionary from an input string, prioritizing direct JSON parsing, then searching within markdown code blocks, and finally attempting to parse any bracketed object found in the text. If all extraction methods fail, it logs an error with a snippet of the raw response before exiting.*


### create_project (function, L361-L442)

> *Summary: Scaffolds a new AG2 project structure based on provided inputs: an optional name, a template selection, or a natural language description for AI generation. It creates the necessary directory and populates it with boilerplate files like configuration, agents, tools, and tests, finally reporting the creation success and next steps.*


### _create_project_from_description (function, L445-L609)

> *Summary: Generates a complete AG2 project structure by prompting an LLM with a natural language description to produce a JSON specification of agents and tools. It then uses this spec to create necessary files, including agent modules, tool implementations, configuration, and the main execution script based on whether one or multiple agents are defined.*


### create_agent (function, L613-L667)

> *Summary: Scaffolds a new agent file by either prompting for a name and optionally including specified tools, or generating the agent entirely from a natural language description provided via `--from-description`. It outputs a Python file containing boilerplate code based on the input parameters.*


### _create_agent_from_description (function, L670-L751)

> *Summary: Generates an agent and its associated tools by sending a natural language description to an LLM for specification extraction. It outputs a Python file containing the agent definition, optionally including tool registrations, and creates stub files for each specified tool in a `tools` directory.*


### create_tool (function, L755-L809)

> *Summary: This function scaffolds a new AG2 tool by either generating it from an OpenAPI specification or a Python module, or by creating a basic template if only a name and description are provided. It handles input validation for required parameters and writes the resulting code to a file in the current working directory's `tools` subdirectory.*


### _create_tool_from_openapi (function, L812-L833)

> *Summary: Parses an OpenAPI specification string to extract available endpoints and then generates corresponding Python tool files. It takes the spec source and an optional name, outputting a file containing the generated tools into the current directory or a `tools` subdirectory.*


### _create_tool_from_module (function, L836-L851)

> *Summary: Inspects a specified Python module to find public functions and then generates corresponding tool files into the current directory or a `tools` subdirectory. It takes a module name, optional function names, and an optional output name as input, producing file system side effects upon success.*


### create_team (function, L855-L903)

> *Summary: This function scaffolds a multi-agent team file based on provided inputs: a required team name, an optional orchestration pattern, and an optional comma-separated list of agent names. It validates the pattern, constructs Python code using templates with defined agents, and writes the resulting team definition to a new `.py` file in the current directory's `teams` folder.*


### _artifact_json (function, L913-L926)

> *Summary: Constructs a standardized JSON string representing a new artifact configuration. It takes the artifact's name and type as primary inputs, merges any additional keyword arguments, and returns a formatted JSON string ready for file output.*


### _skill_md (function, L929-L941)

> *Summary: Generates a standardized Markdown template for a `SKILL.md` file, taking a skill name and description as string inputs to produce the formatted output. This function structures the content with frontmatter metadata and a placeholder heading.*


### _scaffold_template (function, L944-L970)

> *Summary: This function generates a project scaffolding structure by creating several files within the specified output directory. It writes an `artifact.json`, a template README, and two skill documentation files based on the provided name.*


### _scaffold_tool (function, L973-L1002)

> *Summary: This function scaffolds a new tool structure given a name and output path. It generates necessary files like `artifact.json`, Python source, test stubs, and skill documentation within the specified directory.*


### _scaffold_dataset (function, L1005-L1026)

> *Summary: This function generates a basic dataset structure in the specified output path. It creates an `artifact.json` defining the dataset metadata, populates a sample data file (`sample.jsonl`), and scaffolds a schema markdown file within a dedicated skills directory.*


### _scaffold_agent (function, L1029-L1051)

> *Summary: This function generates a basic project structure for a new agent by creating several files within the specified output directory. It writes an `artifact.json` configuration, a descriptive `agent.md`, and a specific skill markdown file (`SKILL.md`) tailored to the provided agent name.*


### _scaffold_skills (function, L1054-L1070)

> *Summary: This function generates the necessary file structure and content for a new skill artifact. It writes an `artifact.json` defining the skill, and two Markdown files (`SKILL.md`) detailing conventions and providing a step-by-step guide within the specified output directory.*


### _scaffold_bundle (function, L1073-L1084)

> *Summary: Generates a basic bundle structure by writing an `artifact.json` file to the specified output path. This JSON defines the bundle as type "bundle" and sets a predefined installation order for its components.*


### create_artifact (function, L1098-L1137)

> *Summary: Scaffolds a new artifact structure based on the specified type and name, optionally placing it in a custom output directory. It validates the input type, ensures the target directory doesn't exist, generates the necessary files (including `artifact.json`), and prints instructions for subsequent authoring and publishing steps.*

