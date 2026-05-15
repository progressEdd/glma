# cli/tests/test_resolver.py

2 function(s): _write_artifact_json, _make_artifact. 6 class(es): TestResolveNoDependencies, TestResolveSingleDependency, TestResolveDiamondDependencies, TestResolveSkipsInstalled, TestTopologicalSort, TestFetchDependency. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _write_artifact_json | function |  |
| _make_artifact | function |  |
| TestResolveNoDependencies | class |  |
| TestResolveSingleDependency | class |  |
| TestResolveDiamondDependencies | class |  |
| TestResolveSkipsInstalled | class |  |
| TestTopologicalSort | class |  |
| TestFetchDependency | class |  |

## Chunks

### _write_artifact_json (function, L10-L15)

> *Summary: Creates a specified directory if it doesn't exist and then serializes a dictionary into an `artifact.json` file within that directory, returning the path to the newly created JSON file.*


### _make_artifact (function, L18-L36)

> *Summary: Constructs and returns an `Artifact` dataclass instance using provided parameters like name, type, owner, version, dependencies, and source directory. It serves as a utility to directly instantiate the artifact object for testing purposes.*


### TestResolveNoDependencies (class, L39-L54)

> *Summary: Verifies that when an artifact has no declared dependencies, the resolution process returns an empty list of required artifacts. It confirms this by instantiating a resolver with mock components and asserting no network fetching occurs.*


### test_returns_empty_when_no_depends (method, L42-L54, parent: TestResolveNoDependencies)

> *Summary: When provided with an artifact that has no dependencies, the resolver returns an empty list of resolved artifacts. This test verifies that no external fetching operations are performed when dependency requirements are absent.*


### TestResolveSingleDependency (class, L57-L116)

> *Summary: These tests verify the dependency resolution process when a root artifact has only one dependency. They confirm that the resolver correctly fetches and returns the expected single dependency, handling both fully qualified and two-part reference formats by mocking client interactions.*


### test_returns_single_dep (method, L60-L86, parent: TestResolveSingleDependency)

> *Summary: This test verifies that the dependency resolver correctly identifies and returns a single required dependency when provided with a root artifact depending on one specific skill. It mocks an artifact fetching client to simulate finding a pre-cached dependency and asserts the resolved list contains only that expected item.*


### test_returns_single_dep_two_part_ref (method, L88-L116, parent: TestResolveSingleDependency)

> *Summary: This test verifies that the resolver correctly identifies and returns a single dependency when provided with a two-part reference like `skills/helper`. It mocks artifact fetching to ensure the resolver calls the client with the correct package name, type, and default owner.*


### TestResolveDiamondDependencies (class, L119-L181)

> *Summary: Tests the dependency resolution logic for a diamond dependency structure ($A \to B, A \to C, B \to D, C \to D$). It verifies that when resolving from artifact 'a', the shared dependency 'd' is included exactly once and appears before its dependents ('b' and 'c') in the final resolved order.*


### test_diamond_deduplicates_shared_dep (method, L122-L181, parent: TestResolveDiamondDependencies)

> *Summary: This test verifies that the dependency resolver correctly handles a "diamond" dependency structure where two components (B and C) share a common dependency (D). It asserts that the shared dependency D is included exactly once in the resolved set, and that it appears before its dependents (B and C) in the final resolution order.*


### TestResolveSkipsInstalled (class, L184-L254)

> *Summary: These tests verify that the dependency resolver correctly skips dependencies already installed at the exact same version, but includes them if a newer version is available despite an older one being recorded in the lockfile. The resolver takes a root artifact definition and returns a list of artifacts needing installation based on existing installations.*


### test_skips_installed_at_same_version (method, L187-L218, parent: TestResolveSkipsInstalled)

> *Summary: This test verifies that the dependency resolver skips installing an artifact if it is already recorded as installed in the lockfile at the exact same version. It simulates fetching a cached artifact and then calls `resolver.resolve()` to confirm no installation action is taken for the specified dependency.*


### test_includes_installed_at_different_version (method, L220-L254, parent: TestResolveSkipsInstalled)

> *Summary: This test verifies that the dependency resolver correctly selects a newer installed artifact when an older version is recorded in the lockfile. It mocks fetching artifacts and then resolves dependencies for a root artifact, asserting the output uses the latest available version.*


### TestTopologicalSort (class, L257-L347)

> *Summary: This test suite verifies the `_topological_sort` method by providing various dependency graphs as input. It asserts that the output sequence correctly orders dependencies (e.g., prerequisites before dependents), handles independent nodes, and raises a `CyclicDependencyError` when cycles are present in the graph.*


### test_simple_chain (method, L260-L277, parent: TestTopologicalSort)

> *Summary: This test verifies the topological sorting functionality of a dependency resolver. It takes a simple directed graph representing dependencies (e.g., A depends on B) and asserts that the output order correctly lists dependencies before the items that rely on them (C, B, A).*


### test_simple_chain_longer (method, L279-L295, parent: TestTopologicalSort)

> *Summary: This test verifies the topological sorting functionality of a dependency resolver using a predefined, linear dependency graph. It asserts that the resulting order correctly reflects the dependencies, yielding `["D", "C", "B", "A"]` for the input structure.*


### test_independent_nodes (method, L297-L314, parent: TestTopologicalSort)

> *Summary: This test verifies that the dependency resolver correctly performs a topological sort on a graph where all nodes are independent. Given an empty dependency graph structure, it asserts the resulting sorted order is deterministically alphabetical when reversed.*


### test_cycle_detection_raises_error (method, L316-L332, parent: TestTopologicalSort)

> *Summary: This test verifies that the resolver correctly identifies and raises a `CyclicDependencyError` when provided with a graph containing a circular dependency (A -> B -> C -> A). It achieves this by calling the internal topological sort method on an initialized resolver instance.*


### test_self_cycle_raises_error (method, L334-L347, parent: TestTopologicalSort)

> *Summary: This test verifies that attempting to resolve a dependency graph containing a self-reference (e.g., "A" depends on "A") correctly raises a `CyclicDependencyError`. It initializes a resolver with mock dependencies and passes the cyclic graph structure to its topological sort method for validation.*


### TestFetchDependency (class, L350-L467)

> *Summary: This test suite verifies the dependency resolution logic by testing how a resolver handles various reference formats. It ensures correct artifact fetching for two-part and three-part references, while also confirming that invalid or missing references return `None` under different failure conditions (e.g., wrong format, fetch errors).*


### test_two_part_ref (method, L353-L379, parent: TestFetchDependency)

> *Summary: This test verifies that the dependency resolver correctly interprets a two-part reference string like `"skills/my-skill"`. It asserts that when resolving this, the underlying client is called with the correct type (`"skills"`), name (`"my-skill"`), and defaults the owner to `"ag2ai"`.*


### test_three_part_ref (method, L381-L408, parent: TestFetchDependency)

> *Summary: This test verifies dependency resolution for a three-part reference by mocking artifact fetching and initializing a resolver with a lockfile. It asserts that the resolver correctly retrieves the specified tool's metadata, including name, owner, and version, after calling the client fetch method with the correct parameters.*


### test_invalid_ref_single_part_returns_none (method, L410-L421, parent: TestFetchDependency)

> *Summary: When provided with a single-part invalid reference string, the dependency resolver returns `None` without attempting to fetch any artifacts from the client. This test verifies that an unresolvable input correctly results in no action being taken by the underlying client mock.*


### test_invalid_ref_four_parts_returns_none (method, L423-L434, parent: TestFetchDependency)

> *Summary: When provided with a dependency reference containing four path segments, the resolver returns `None` without attempting to fetch any artifacts from the client. This test verifies that malformed references are handled gracefully by returning no result.*


### test_fetch_error_returns_none (method, L436-L449, parent: TestFetchDependency)

> *Summary: When the artifact fetching process encounters a `FetchError`, this test verifies that the dependency resolution mechanism correctly returns `None` for the requested item. It mocks the client to simulate a fetch failure and asserts the resolver's output matches this expected null return.*


### test_missing_artifact_json_returns_none (method, L451-L467, parent: TestFetchDependency)

> *Summary: When provided with a dependency request and an artifact directory lacking `artifact.json`, the resolver returns `None`. This test verifies that the resolution process gracefully handles missing metadata for a specified skill.*

