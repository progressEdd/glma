# cli/tests/test_artifact.py

3 class(es): TestLoadArtifactJson, TestLoadLegacyManifest, TestLoadArtifact. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestLoadArtifactJson | class |  |
| TestLoadLegacyManifest | class |  |
| TestLoadArtifact | class |  |

## Chunks

### TestLoadArtifactJson (class, L7-L204)

> *Summary: This test suite verifies the functionality of parsing various types of artifact JSON manifests by calling `load_artifact_json` with predefined data structures. It ensures that the resulting artifact object correctly populates fields specific to skills, templates, tools (AG2 and MCP), datasets, agents, bundles, and minimal configurations.*


### test_parse_skills_artifact (method, L10-L33, parent: TestLoadArtifactJson)

> *Summary: This test verifies the functionality of loading an artifact from a JSON file by creating a sample skills manifest, passing it to `load_artifact_json`, and asserting that the resulting object correctly parses all expected metadata fields like name, type, version, and skill configuration.*


### test_parse_template_artifact (method, L35-L66, parent: TestLoadArtifactJson)

> *Summary: This test verifies the correct parsing of a JSON file representing an artifact, specifically one of type "template." It loads a predefined manifest containing details like scaffold paths, variable definitions with transformations, and post-installation scripts to ensure data integrity.*


### test_parse_tool_ag2 (method, L68-L88, parent: TestLoadArtifactJson)

> *Summary: This test verifies the correct parsing of a JSON manifest file representing an AG2 tool artifact. It loads the data from a temporary file and asserts that the resulting object correctly contains the expected tool kind, function list size, and dependency requirements.*


### test_parse_tool_mcp (method, L90-L118, parent: TestLoadArtifactJson)

> *Summary: This test verifies the correct parsing of a JSON manifest file representing an MCP tool artifact. It loads the data from a temporary file and asserts that key fields like `kind`, `runtime`, and specific configuration values are correctly extracted into the resulting artifact object.*


### test_parse_dataset (method, L120-L144, parent: TestLoadArtifactJson)

> *Summary: This test verifies the functionality of loading an artifact from a JSON file by creating a mock manifest containing dataset information. It asserts that the loaded object correctly parses and exposes the dataset's format, compatibility status, and remote file details.*


### test_parse_agent (method, L146-L169, parent: TestLoadArtifactJson)

> *Summary: This test verifies the functionality of loading an agent-specific artifact from a JSON file. It creates a sample manifest, saves it to a temporary path, and then asserts that the loaded object correctly contains expected values for the agent's model, tools, and turn limit.*


### test_parse_bundle (method, L171-L192, parent: TestLoadArtifactJson)

> *Summary: This test verifies the functionality of loading an artifact from a JSON file, ensuring that the parsed object correctly contains and validates the bundle structure, including the list of required and optional artifacts. It takes a temporary path containing a specific manifest as input and asserts the resulting `artifact` object's properties.*


### test_parse_minimal_manifest (method, L194-L204, parent: TestLoadArtifactJson)

> *Summary: This test verifies the parsing of a minimal JSON manifest file by loading it using `load_artifact_json`. It asserts that the resulting artifact object correctly extracts the provided name while defaulting version, authors, and dependencies to empty values.*


### TestLoadLegacyManifest (class, L207-L226)

> *Summary: This test verifies backward compatibility by loading a legacy `manifest.json` file from a temporary directory. It asserts that the loaded artifact correctly reflects the name, display name, version, and source directory defined in the input manifest.*


### test_loads_existing_skills_manifest (method, L210-L226, parent: TestLoadLegacyManifest)

> *Summary: This test verifies that the `load_legacy_manifest` function correctly reads and parses a pre-existing JSON manifest file from a temporary directory. It asserts that the resulting artifact object contains the expected metadata (name, display name, version) matching the input data.*


### TestLoadArtifact (class, L229-L259)

> *Summary: These tests verify the `load_artifact` function's behavior when reading artifact metadata from a directory. It asserts that the function prioritizes loading data from `artifact.json`, falls back to `manifest.json` if the former is absent, and returns `None` if no manifest file exists in the provided path.*


### test_prefers_artifact_json (method, L232-L243, parent: TestLoadArtifact)

> *Summary: This test verifies that the artifact loading mechanism prioritizes JSON files when both a JSON and manifest file are present in the input directory. It loads artifacts from a temporary path containing both `artifact.json` (with name "test-new") and `manifest.json` (with name "test-old"), asserting that the loaded artifact reflects the data from the JSON file.*


### test_falls_back_to_manifest_json (method, L245-L254, parent: TestLoadArtifact)

> *Summary: This test verifies that the artifact loading mechanism successfully falls back to reading a `manifest.json` file when processing an artifact directory. It asserts that the loaded artifact object correctly reflects the data from this JSON manifest.*


### test_returns_none_when_no_manifest (method, L256-L259, parent: TestLoadArtifact)

> *Summary: When provided with a directory containing no manifest file, the artifact loading function returns `None`. This test verifies that the expected behavior for an empty or unmanifested input path is to yield no result.*

