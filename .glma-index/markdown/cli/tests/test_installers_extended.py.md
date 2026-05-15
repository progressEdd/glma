# cli/tests/test_installers_extended.py

6 function(s): _make_ag2_tool_artifact, _make_mcp_tool_artifact, _make_dataset_artifact, _make_bundle_artifact, _build_tool_installer, _build_dataset_installer. 3 class(es): TestToolInstaller, TestDatasetInstaller, TestBundleInstaller. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_ag2_tool_artifact | function |  |
| _make_mcp_tool_artifact | function |  |
| _make_dataset_artifact | function |  |
| _make_bundle_artifact | function |  |
| _build_tool_installer | function |  |
| _build_dataset_installer | function |  |
| TestToolInstaller | class |  |
| TestDatasetInstaller | class |  |
| TestBundleInstaller | class |  |

## Chunks

### _make_ag2_tool_artifact (function, L22-L46)

> *Summary: This function constructs a complete, local cache directory structure for an AG2-type tool artifact. It takes a base cache path and a tool name as input, generating necessary directories, creating a manifest file defining the tool's metadata, and populating source files within that structure before returning the final tool directory path.*


### _make_mcp_tool_artifact (function, L49-L75)

> *Summary: This function constructs a complete directory structure representing an MCP tool artifact within the specified cache directory. It generates and writes a manifest file (`artifact.json`) defining the tool's metadata, along with creating a placeholder source file (`server.py`).*


### _make_dataset_artifact (function, L78-L119)

> *Summary: This function constructs a local dataset artifact within a specified cache directory based on configuration flags. It generates an `artifact.json` manifest containing metadata (inline data paths, remote sources, or schema) and optionally creates sample inline data files in a dedicated subdirectory before returning the path to the created artifact directory.*


### _make_bundle_artifact (function, L122-L140)

> *Summary: This function constructs a directory structure within the cache to represent a software bundle artifact. It creates necessary directories, writes a manifest JSON file defining dependencies (like a specific skills pack), and returns the path to this newly created bundle location.*


### _build_tool_installer (function, L143-L154)

> *Summary: Creates and configures a complete set of installation components—including an `ArtifactClient`, `Lockfile`, `DependencyResolver`, and `SkillsInstaller`—all wired to local directories provided by the input path. It returns the fully assembled `ToolInstaller`, the associated `Lockfile`, and the project directory structure.*


### _build_dataset_installer (function, L157-L168)

> *Summary: Constructs a complete installation environment by initializing an `ArtifactClient` pointing to a temporary cache directory. It then assembles and returns a configured `DatasetInstaller`, its associated `Lockfile`, and the project directory structure.*


### TestToolInstaller (class, L176-L229)

> *Summary: These tests verify that tool installers correctly copy source files into a project's `tools` directory and update a lockfile upon installation. They specifically test both AG2 and MCP tool installation workflows, asserting file existence, content, and the recorded artifact metadata in the resulting install result.*


### test_install_ag2_tool_copies_source_and_records_lockfile (method, L179-L198, parent: TestToolInstaller)

> *Summary: This test verifies that installing an AG2 tool copies its source files into the project's tools directory and correctly logs this installation in a provided lockfile. It asserts the existence of specific copied files and confirms the artifact name within the installation result.*


### test_install_mcp_tool_copies_source_and_records_lockfile (method, L200-L229, parent: TestToolInstaller)

> *Summary: This test verifies that installing an MCP tool copies its source files to the project directory and correctly logs the installation in a lockfile. It simulates the installation process by patching configuration functions and asserts the existence of copied files and the recorded artifact metadata.*


### TestDatasetInstaller (class, L237-L297)

> *Summary: These tests verify dataset installation behavior by simulating various scenarios: copying inline data, handling remote file downloads with and without a `--full` flag to emit warnings, and writing a `schema.json` file when the artifact provides one. The installer takes an artifact definition (with options for inline/remote data and schema) and outputs installed files into a specified project directory along with installation results.*


### test_install_with_inline_data_copies_data_directory (method, L240-L255, parent: TestDatasetInstaller)

> *Summary: This test verifies that an installer correctly copies inline dataset data into a specific directory structure within the project upon installation. It asserts the existence and content of expected files in the destination path, confirming successful artifact creation and lockfile registration.*


### test_install_without_full_skips_remote_files_adds_warning (method, L257-L275, parent: TestDatasetInstaller)

> *Summary: When installing a dataset without the `--full` flag, this test verifies that a warning is issued indicating remote files were skipped and confirms that no actual remote files are downloaded to the destination directory. It uses a pre-built installer and project structure as input to assert the correct warning content and file absence in the output.*


### test_install_writes_schema_json_when_schema_present (method, L277-L297, parent: TestDatasetInstaller)

> *Summary: This test verifies that when a dataset artifact includes a schema, an accompanying `schema.json` file is correctly written to the installation directory during the install process. It asserts the existence and basic structure of this generated JSON file within the output.*


### TestBundleInstaller (class, L305-L381)

> *Summary: This test suite verifies the orchestration logic of a `BundleInstaller`, ensuring it correctly dispatches installation requests to specific sub-installers (like skills or tools) based on artifact types. It tests scenarios such as successful installation of referenced packs, selection of required artifacts when no optional ones exist, and error handling for unknown artifact types.*


### _build_bundle_installer (method, L308-L333, parent: TestBundleInstaller)

> *Summary: This method constructs a `BundleInstaller` instance by initializing its dependencies with mocked components for skills, templates, tools, datasets, and agents. It returns the configured installer along with the associated lockfile and temporary project directory structure.*


### test_install_bundle_installs_referenced_skills_pack (method, L335-L353, parent: TestBundleInstaller)

> *Summary: This test verifies that installing a bundle correctly triggers the skills installer for any referenced skill packs. It mocks the skills installation to confirm the correct pack name is passed to the mock installer and that the resulting dependency is recorded in the final installation result.*


### test_select_artifacts_returns_required_refs_when_no_optional (method, L355-L374, parent: TestBundleInstaller)

> *Summary: When provided with a list of bundle references containing only required artifacts, the method returns an array consisting solely of those mandatory reference names. This test verifies that no optional references are included in the output when none are present in the input set.*


### test_install_by_type_raises_fetch_error_for_unknown_type (method, L376-L381, parent: TestBundleInstaller)

> *Summary: When provided with an unrecognized artifact type key, the installation method is expected to raise a `FetchError`. This test verifies that passing `"widgets"` as the type results in the specified error being raised.*

