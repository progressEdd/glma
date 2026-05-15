# cli/src/ag2_cli/install/installers/agents.py

1 class(es): AgentInstaller. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AgentInstaller | class |  |

## Chunks

### AgentInstaller (class, L17-L109)

> *Summary: This class handles the installation of custom agent artifacts by fetching them from a client and placing necessary components into a project directory. It processes the artifact to install the main agent definition, bundled MCP servers, and any required skills or dependencies before recording the successful installation in a lockfile.*


### __init__ (method, L20-L30, parent: AgentInstaller)

> *Summary: Initializes the agent installer by accepting and storing instances of an `ArtifactClient`, `Lockfile`, `DependencyResolver`, and `SkillsInstaller`. These dependencies are used to manage artifact retrieval, dependency resolution, and skill installation during the setup process.*


### install (method, L32-L109, parent: AgentInstaller)

> *Summary: This method installs an agent artifact by fetching its configuration and associated files from a remote cache. It copies the agent definition into the project's `.claude` directory, installs bundled MCP servers and skills based on provided targets, resolves dependencies, and finally records the installation details in a lockfile before returning a comprehensive result object.*

