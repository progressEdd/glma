# cli/src/ag2_cli/install/resolver.py

2 class(es): CyclicDependencyError, DependencyResolver. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CyclicDependencyError | class |  |
| DependencyResolver | class |  |

## Chunks

### CyclicDependencyError (class, L10-L11)

> *Summary: This custom exception signals that a circular dependency has been found during resolution. It inherits from the base `Exception` class for error handling.*


### DependencyResolver (class, L14-L118)

> *Summary: This class resolves the complete set of required artifacts for a given input artifact by recursively fetching and mapping all its dependencies from a remote client. It then uses topological sorting to produce an ordered list of necessary artifacts that are not already installed according to the provided lockfile, ensuring they are listed in installation order (dependencies first).*


### __init__ (method, L17-L19, parent: DependencyResolver)

> *Summary: Initializes the resolver with an `ArtifactClient` for artifact interaction and a `Lockfile` object to manage dependency constraints. These inputs are stored as instance attributes for subsequent resolution operations.*


### resolve (method, L21-L44, parent: DependencyResolver)

> *Summary: This method determines all necessary dependencies for a given artifact by building a dependency graph and performing a topological sort. It returns an ordered list of artifacts that are not already installed at the required version, excluding the root artifact itself.*


### _collect (method, L46-L64, parent: DependencyResolver)

> *Summary: Recursively traverses an artifact's dependencies to populate a manifest dictionary and build a dependency graph. It takes an initial `Artifact`, existing `manifests`, and the `graph` structure as input, returning nothing while populating these structures with all reachable artifacts and their connections.*


### _fetch_dependency (method, L66-L86, parent: DependencyResolver)

> *Summary: Retrieves a dependency's manifest from the remote registry based on a reference string, which can be two or three parts separated by slashes. It first attempts to find and load the artifact JSON from a local cache directory; otherwise, it returns `None`.*


### _topological_sort (method, L88-L118, parent: DependencyResolver)

> *Summary: Calculates a valid installation order from a dependency graph using Kahn's algorithm. It takes a dictionary representing nodes and their dependencies as input and returns a list of nodes ordered such that all prerequisites are installed before the items that depend on them, raising an error if a cycle exists.*

