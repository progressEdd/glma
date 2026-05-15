# autogen/beta/tools/skills/local_skills/toolkit.py

1 class(es): SkillsToolkit. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SkillsToolkit | class |  |

## Chunks

### SkillsToolkit (class, L20-L165)

> *Summary: Provides a unified interface for local skills by packaging three distinct functionalities into one toolkit: listing available skills, loading detailed skill instructions, and executing scripts within a skill's directory. It discovers skills in default or specified runtime paths and exposes these capabilities as callable tools.*


### __init__ (method, L55-L72, parent: SkillsToolkit)

> *Summary: Initializes the toolkit by establishing a runtime environment, either from a provided configuration or by creating a default local instance. It then sets up the base class with a list of available skills, loads the primary skill, and prepares to execute its script using specified middleware.*


### runtime (method, L75-L77, parent: SkillsToolkit)

> *Summary: Returns the internal `SkillRuntime` object, which is responsible for discovering and loading available skills. This method provides access to the core skill execution environment managed by the instance.*


### list_skills (method, L79-L92, parent: SkillsToolkit)

> *Summary: Generates a callable tool that lists all available local skills discovered by the runtime. It accepts optional name, description, and middleware arguments to configure the resulting function tool.*


### load_skill (method, L94-L109, parent: SkillsToolkit)

> *Summary: This method generates a callable tool that retrieves the complete content of a specified skill file from the runtime environment. It accepts a skill name as input and returns the corresponding string content, wrapped as a `FunctionTool`.*


### run_skill_script (method, L111-L165, parent: SkillsToolkit)

> *Summary: Generates a callable tool that executes scripts located within a specified skill's `scripts` directory. It accepts the skill name, script filename, and optional arguments, determining execution method (e.g., Python interpreter, shell) based on file extension or shebang line. The output is the standard output of the executed script command.*

