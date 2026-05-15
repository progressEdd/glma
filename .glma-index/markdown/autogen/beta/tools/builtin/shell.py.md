# autogen/beta/tools/builtin/shell.py

5 class(es): NetworkPolicy, ContainerAutoEnvironment, ContainerReferenceEnvironment, ShellToolSchema, ShellTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| NetworkPolicy | class |  |
| ContainerAutoEnvironment | class |  |
| ContainerReferenceEnvironment | class |  |
| ShellToolSchema | class |  |
| ShellTool | class |  |

## Chunks

### NetworkPolicy (class, L20-L23)

> *Summary: Defines a structure to specify allowed outbound network domains for shell containers. It holds a list of strings representing the permitted hostnames for external connections.*


### ContainerAutoEnvironment (class, L27-L30)

> *Summary: This class is responsible for automatically provisioning and managing a container environment. It holds an optional `NetworkPolicy` object to configure network access for the managed container.*


### ContainerReferenceEnvironment (class, L34-L41)

> *Summary: Represents a reference to an already existing container using its ID. It holds only the `container_id` and does not allow configuration of network policies, as those are set during initial container creation.*


### ShellToolSchema (class, L51-L62)

> *Summary: Defines the schema for a shell execution tool, specifying its type and version. It acts as a capability flag to indicate that shell execution is supported by a provider, though currently only OpenAI supports server-side execution via this mechanism.*


### ShellTool (class, L65-L117)

> *Summary: This class provides a server-side tool for executing shell commands, primarily supporting the OpenAI Responses API via configuration of an execution environment. It defines schemas for command invocation and registers itself to intercept specific tool call events within the agent's context stream.*


### __init__ (method, L90-L99, parent: ShellTool)

> *Summary: Initializes the shell tool by setting its configuration parameters, which include an optional execution environment and a specific shell version. It stores these settings internally for later use in executing shell commands.*


### schemas (method, L101-L103, parent: ShellTool)

> *Summary: Generates a list of `ShellToolSchema` objects by resolving any variable references within the tool's parameters using the provided execution context. This allows dynamic configuration of shell tool definitions based on runtime data.*


### register (method, L105-L117, parent: ShellTool)

> *Summary: This method registers a handler for shell tool calls within an execution stack and context. It sets up a scope that intercepts events matching the predefined shell tool name, allowing custom logic to be executed upon invocation.*

