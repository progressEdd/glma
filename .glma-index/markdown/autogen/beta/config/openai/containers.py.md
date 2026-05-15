# autogen/beta/config/openai/containers.py

3 class(es): ExpiresAfter, ContainerInfo, ContainerManager. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ExpiresAfter | class |  |
| ContainerInfo | class |  |
| ContainerManager | class |  |

## Chunks

### ExpiresAfter (class, L13-L22)

> *Summary: Defines a container expiry policy specifying how long an inactive session should persist. It takes the inactivity duration in minutes and uses a fixed reference point, currently only supporting `"last_active_at"`.*


### ContainerInfo (class, L26-L31)

> *Summary: This class holds metadata describing a created container. It stores the container's unique ID, an optional name, and its current status.*


### ContainerManager (class, L34-L123)

> *Summary: This class manages OpenAI-hosted shell containers, allowing users to create and delete reusable environments via an initialized `AsyncOpenAI` client. It accepts configuration parameters like API keys and can be called with optional names, memory limits, or expiration policies to return container metadata including a unique ID.*


### __init__ (method, L56-L78, parent: ContainerManager)

> *Summary: Initializes an asynchronous OpenAI client by accepting optional configuration parameters like API keys, base URLs, and retry limits. It constructs and stores an `AsyncOpenAI` instance using these provided settings for making external API calls.*


### create (method, L80-L115, parent: ContainerManager)

> *Summary: This method provisions a new hosted container by sending configuration details like name, memory limit, and expiry policy to the underlying client. It returns a `ContainerInfo` object containing the newly created container's ID and metadata.*


### delete (method, L117-L123, parent: ContainerManager)

> *Summary: Removes a specified Docker container using its unique identifier. It asynchronously calls the underlying client's delete method with the provided `container_id` string.*

