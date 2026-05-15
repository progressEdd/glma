# cli/tests/test_create_artifact.py

8 class(es): TestCreateArtifactHelp, TestCreateArtifactValidation, TestCreateArtifactTemplate, TestCreateArtifactTool, TestCreateArtifactDataset, TestCreateArtifactAgent, TestCreateArtifactSkills, TestCreateArtifactBundle. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestCreateArtifactHelp | class |  |
| TestCreateArtifactValidation | class |  |
| TestCreateArtifactTemplate | class |  |
| TestCreateArtifactTool | class |  |
| TestCreateArtifactDataset | class |  |
| TestCreateArtifactAgent | class |  |
| TestCreateArtifactSkills | class |  |
| TestCreateArtifactBundle | class |  |

## Chunks

### TestCreateArtifactHelp (class, L14-L24)

> *Summary: These tests verify the CLI's help output for artifact creation commands. They assert that running `create --help` lists artifacts and that `create artifact --help` displays specific details like templates and file names.*


### test_help_lists_artifact (method, L15-L18, parent: TestCreateArtifactHelp)

> *Summary: Verifies that invoking the `create --help` command successfully returns an exit code of zero and includes the string "artifact" in its output. This tests the help documentation for the artifact creation functionality.*


### test_artifact_help (method, L20-L24, parent: TestCreateArtifactHelp)

> *Summary: Verifies that invoking the `create artifact --help` command successfully returns an exit code of zero and displays help text containing keywords like "template" and references to "artifact.json" or "artifact".*


### TestCreateArtifactValidation (class, L27-L38)

> *Summary: This test suite validates artifact creation by asserting that the CLI rejects requests for unknown types and prevents overwriting existing directories during the process. It uses a runner to invoke the application with specific arguments and checks the exit code and output messages for expected failures.*


### test_rejects_unknown_type (method, L28-L31, parent: TestCreateArtifactValidation)

> *Summary: This test verifies that the application correctly rejects an attempt to create an artifact using an unrecognized type. It asserts that invoking the `create artifact` command with a bogus type results in a non-zero exit code and includes an "Unknown artifact type" message in the output.*


### test_rejects_existing_directory (method, L33-L38, parent: TestCreateArtifactValidation)

> *Summary: This test verifies that the artifact creation command fails when a directory with the specified name already exists. It asserts an exit code of 1 and checks for an "already exists" message in the output upon invocation.*


### TestCreateArtifactTemplate (class, L41-L73)

> *Summary: This test verifies the CLI command for creating an artifact template by invoking it with a name and output directory, then asserts that the resulting structure contains expected files, configuration data (like `artifact.json`), and templated content within those files. A secondary test specifically checks that generated skill markdown files contain correct frontmatter metadata.*


### test_scaffolds_template (method, L42-L65, parent: TestCreateArtifactTemplate)

> *Summary: This test verifies the artifact creation process by invoking a CLI command to generate a template artifact in a temporary directory. It asserts that the operation succeeds, the resulting directory structure is correct, and key files contain expected metadata and templating placeholders.*


### test_skill_frontmatter (method, L67-L73, parent: TestCreateArtifactTemplate)

> *Summary: Invokes the artifact creation command to generate a template, then reads the resulting `SKILL.md` file to assert that it contains standard YAML frontmatter fields like separators, name, description, and license information.*


### TestCreateArtifactTool (class, L76-L90)

> *Summary: This test verifies that invoking the `create artifact tool` command successfully scaffolds a new project structure for a web scraper. It asserts that the resulting directory contains expected files, including an artifact manifest and source/test files, confirming correct generation.*


### test_scaffolds_tool (method, L77-L90, parent: TestCreateArtifactTool)

> *Summary: This test verifies that invoking the `create artifact tool` command successfully scaffolds a new project structure for a web scraper. It asserts that the generated directory contains expected files, including source code, tests, and skill definitions, and validates the contents of the resulting manifest file.*


### TestCreateArtifactDataset (class, L93-L107)

> *Summary: This test verifies the successful creation of an artifact dataset by invoking a CLI command with a specified output path. It asserts that the resulting directory contains a valid manifest, a sample data file in JSONL format, and necessary schema documentation.*


### test_scaffolds_dataset (method, L94-L107, parent: TestCreateArtifactDataset)

> *Summary: This test verifies the successful creation of a dataset artifact by invoking the `create artifact dataset` command with a specified output path. It then asserts that the resulting directory contains a valid manifest, a sample data file in JSONL format, and necessary schema documentation.*


### TestCreateArtifactAgent (class, L110-L124)

> *Summary: This test verifies the artifact creation process by invoking a command to scaffold an agent named "code-helper" into a temporary directory. It asserts that the resulting structure contains a valid `artifact.json` manifest, the expected `agent.md` file with specific content, and the necessary skill definition files.*


### test_scaffolds_agent (method, L111-L124, parent: TestCreateArtifactAgent)

> *Summary: This test verifies the `create artifact agent` command by invoking it with a target output directory. It asserts that the operation succeeds, generates an `artifact.json` manifest confirming the type and source, creates the primary agent markdown file, and scaffolds necessary skill files within the output structure.*


### TestCreateArtifactSkills (class, L127-L138)

> *Summary: This test verifies the artifact creation process for a "skills" type, expecting successful execution when invoking the `create artifact skills` command with a specified output directory. It then asserts that the generated artifact manifest is correct and that specific skill definition files are present in the expected subdirectory structure.*


### test_scaffolds_skills (method, L128-L138, parent: TestCreateArtifactSkills)

> *Summary: This test verifies the artifact creation process for a "skills" type, specifically using the "fastapi" template. It asserts that the command executes successfully and that the resulting directory contains expected manifest data and specific skill documentation files.*


### TestCreateArtifactBundle (class, L141-L153)

> *Summary: This test verifies the successful creation of an artifact bundle using the CLI. It asserts that the resulting output directory contains a valid `artifact.json` manifest identifying it as a bundle, and confirms the absence of a `skills` subdirectory.*


### test_scaffolds_bundle (method, L142-L153, parent: TestCreateArtifactBundle)

> *Summary: This test verifies the successful creation of an artifact bundle using the CLI runner, expecting an exit code of zero. It then asserts that the generated `artifact.json` correctly identifies the type as "bundle," contains no artifacts initially, and includes an installation order field, while also confirming the absence of a dedicated skills directory.*

