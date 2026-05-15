# cli/tests/test_installers.py

4 class(es): TestSkillsInstaller, TestLoadSkillsFromArtifact, TestTemplateInstaller, TestAgentInstaller. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestSkillsInstaller | class |  |
| TestLoadSkillsFromArtifact | class |  |
| TestTemplateInstaller | class |  |
| TestAgentInstaller | class |  |

## Chunks

### TestSkillsInstaller (class, L7-L63)

> *Summary: This test suite verifies the functionality of a skills installer by simulating installations using mocked dependencies and artifact clients. It asserts that installing specified artifacts results in the creation of expected files within a temporary directory structure and correctly updates the installation lockfile, with one test also validating filtering capabilities during installation.*


### test_install_bundled_ag2_skills (method, L10-L40, parent: TestSkillsInstaller)

> *Summary: This test verifies the installation process for bundled AG2 skills by using a `SkillsInstaller` with mock clients and resolvers. It inputs a target configuration, executes the install command, and asserts that the expected artifacts are created in the temporary directory and correctly recorded in the lockfile.*


### test_install_with_name_filter (method, L42-L63, parent: TestSkillsInstaller)

> *Summary: This test verifies that an installer correctly processes a request to install specific targets while applying a name filter. It asserts that only the item matching the "imports" filter is installed, resulting in at least one created file within the expected directory structure.*


### TestLoadSkillsFromArtifact (class, L66-L118)

> *Summary: This test suite verifies the `load_skills_from_artifact` function by simulating various artifact structures. It confirms that the function correctly parses skills from both flat Markdown files and structured directory layouts, handling mixed skill types like rules, skills, agents, and commands.*


### test_loads_flat_format (method, L69-L84, parent: TestLoadSkillsFromArtifact)

> *Summary: This test verifies that the `load_skills_from_artifact` function correctly parses a flat format skill file. It takes an `Artifact` object pointing to a directory containing a Markdown rule file and asserts that it returns a list containing one properly parsed skill object with the correct name, category, and body content.*


### test_loads_directory_format (method, L86-L102, parent: TestLoadSkillsFromArtifact)

> *Summary: This test verifies that the `load_skills_from_artifact` function correctly parses a directory structure containing agent skills. It creates a mock skill directory, initializes an artifact pointing to it, and asserts that exactly one skill object is returned with the correct name and category.*


### test_loads_mixed_categories (method, L104-L118, parent: TestLoadSkillsFromArtifact)

> *Summary: This test verifies that a loading function correctly parses artifacts containing multiple, mixed-type definitions. It creates mock directories with files representing different categories (rule, skill, agent, command) and asserts the loader returns all four types.*


### TestTemplateInstaller (class, L121-L211)

> *Summary: This test suite verifies the functionality of template installation by first creating a mock template artifact and then executing installation logic using various components like `ArtifactClient` and `DependencyResolver`. It asserts that templates are correctly scaffolded, variables are substituted into files, and preview mode prevents file creation while still reporting intended changes.*


### _make_template (method, L124-L156, parent: TestTemplateInstaller)

> *Summary: This method constructs a minimal, self-contained application template artifact within a specified temporary directory structure. It generates an `artifact.json` manifest and populates the necessary scaffold files (like `README.md.tmpl` and `main.py`) to define the template's structure and variables.*


### test_scaffolds_project (method, L158-L187, parent: TestTemplateInstaller)

> *Summary: This test verifies the functionality of a template installer by simulating a project scaffolding process. It uses an `ArtifactClient`, `Lockfile`, and `DependencyResolver` to execute installation, asserting that expected files are created, variables are correctly substituted in templates, and temporary extensions are removed from output files.*


### test_preview_mode (method, L189-L211, parent: TestTemplateInstaller)

> *Summary: This test verifies the behavior of an installer when run in preview mode, using mock clients and resolvers to simulate installation against a temporary project directory. It asserts that files are listed as intended but confirms no actual files are created on disk during this dry-run execution.*


### TestAgentInstaller (class, L214-L262)

> *Summary: This test verifies the `AgentInstaller`'s functionality by simulating an installation process for a predefined agent artifact. It takes mock artifacts and project paths as input, asserting that the agent file is correctly placed in the project directory and recorded in the lockfile upon successful execution.*


### test_installs_agent_file (method, L217-L262, parent: TestAgentInstaller)

> *Summary: This test verifies that the `AgentInstaller` correctly installs an agent artifact into a project directory. It sets up mock artifacts, initializes necessary components like clients and resolvers, calls the install method with a specific agent name, and then asserts the resulting agent file exists in the correct location with expected content, while also checking the lockfile state.*

