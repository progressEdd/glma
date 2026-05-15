# cli/tests/test_publish.py

2 function(s): _make_artifact, _valid_template_manifest. 3 class(es): TestPublishHelp, TestPublishDryRun, TestValidateArtifact. 18 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_artifact | function |  |
| _valid_template_manifest | function |  |
| TestPublishHelp | class |  |
| TestPublishDryRun | class |  |
| TestValidateArtifact | class |  |

## Chunks

### _make_artifact (function, L20-L29)

> *Summary: This helper function constructs a temporary directory structure representing an artifact. It takes a base path, a name, a manifest dictionary, and optional extra files to write into the resulting directory, returning the path to the created artifact folder.*


### _valid_template_manifest (function, L32-L44)

> *Summary: Creates a standardized dictionary structure representing a valid template manifest, allowing optional overrides to customize its contents. It returns the fully constructed and merged manifest dictionary.*


### TestPublishHelp (class, L52-L62)

> *Summary: These tests verify the CLI's help functionality for the `publish` command and its subcommands. They assert that invoking `--help` on `publish` shows artifact information, while invoking it on `publish artifact` displays specific options like `dry-run` and `repo`.*


### test_help_lists_publish (method, L53-L56, parent: TestPublishHelp)

> *Summary: Invokes the application with the `publish --help` command to verify that the help output is generated successfully and contains the keyword "artifact".*


### test_artifact_help (method, L58-L62, parent: TestPublishHelp)

> *Summary: Verifies that invoking the `publish artifact --help` command successfully returns an exit code of zero and includes expected help text like "dry-run" and "repo" in its output.*


### TestPublishDryRun (class, L65-L117)

> *Summary: This test suite verifies the behavior of a dry-run publishing command by invoking it with various artifact inputs. It asserts correct exit codes and output messages for scenarios including valid artifacts, missing JSON files, incomplete metadata, non-directory paths, and successful path reporting.*


### test_valid_artifact_passes (method, L66-L79, parent: TestPublishDryRun)

> *Summary: This test verifies that publishing a correctly constructed artifact succeeds when running a dry run. It constructs an artifact using predefined templates and then invokes the publish command, asserting a successful exit code and specific output messages confirming the dry run passed all checks.*


### test_missing_artifact_json_fails (method, L81-L86, parent: TestPublishDryRun)

> *Summary: This test verifies that the publishing command fails when an artifact directory is provided but lacks a required `artifact.json` file. It asserts that the invocation returns a non-zero exit code and includes a specific error message in its output.*


### test_missing_required_fields_fails (method, L88-L92, parent: TestPublishDryRun)

> *Summary: This test verifies that the publishing command fails when required fields are missing from an artifact. It asserts that invoking the `publish` command with a dry run results in a non-zero exit code and includes an error message about the missing "description".*


### test_not_a_directory_fails (method, L94-L99, parent: TestPublishDryRun)

> *Summary: Verifies that attempting to publish a file path when the provided input is not a directory results in a failure exit code and an appropriate error message. It uses a temporary file created within the test environment as the invalid input for the publishing command.*


### test_shows_target_path (method, L101-L117, parent: TestPublishDryRun)

> *Summary: This test verifies that the publishing command correctly indicates the target path when run in dry-run mode. It asserts that the output from invoking `publish artifact` contains the expected directory structure for a given artifact.*


### TestValidateArtifact (class, L125-L286)

> *Summary: This test suite verifies the artifact validation logic by calling `_validate_artifact` with various inputs representing artifacts. It asserts expected outcomes, such as successful validation (no errors), failure due to invalid JSON or unknown types, and specific warnings for missing configurations like authors or tags.*


### test_valid_template (method, L126-L139, parent: TestValidateArtifact)

> *Summary: This test verifies that a correctly constructed artifact passes validation without any errors. It takes an artifact created from a valid template and asserts that the resulting manifest is present and contains zero error-level issues.*


### test_invalid_json (method, L141-L147, parent: TestValidateArtifact)

> *Summary: When provided with a directory containing an artifact file with malformed JSON content, the function returns `None` for the manifest and populates the issues list with a message indicating "Invalid JSON."*


### test_unknown_type (method, L149-L162, parent: TestValidateArtifact)

> *Summary: This test verifies that the validation process correctly flags an artifact as having an unknown type when provided with a specific structure. It asserts that the returned list of issues contains a message indicating "Unknown artifact type."*


### test_missing_type_config (method, L164-L178, parent: TestValidateArtifact)

> *Summary: This test verifies that an artifact lacking a specific type configuration will trigger validation errors. It asserts the presence of a "Missing 'tool' config" error when validating an artifact created with only basic metadata.*


### test_bad_version_warns (method, L180-L192, parent: TestValidateArtifact)

> *Summary: This test verifies that an artifact containing a non-semantic version string triggers a warning during validation. It constructs an artifact with a bad version and asserts that the resulting issues list contains at least one warning mentioning "semver".*


### test_no_authors_warns (method, L194-L206, parent: TestValidateArtifact)

> *Summary: When validating an artifact created with no specified authors, the function asserts that the validation process returns at least one issue message containing "authors," indicating both a required-field error and a warning are triggered. This test confirms the expected behavior when author metadata is omitted during artifact creation.*


### test_no_tags_warns (method, L208-L220, parent: TestValidateArtifact)

> *Summary: This test verifies that an artifact lacking tags triggers a warning during validation. It constructs an artifact with no specified tags and asserts that the resulting issues list contains at least one warning mentioning "tags".*


### test_missing_scaffold_dir_warns (method, L222-L233, parent: TestValidateArtifact)

> *Summary: This test verifies that the artifact validation process emits a warning when a required scaffold directory is missing during artifact creation. It asserts that at least one warning message contains the string "scaffold".*


### test_empty_skills_dir_warns (method, L235-L248, parent: TestValidateArtifact)

> *Summary: This test verifies that the artifact validation process emits a warning when the designated skills directory exists but is empty. It achieves this by creating an artifact with an empty `skills` subdirectory and asserting the presence of a specific warning message.*


### test_skills_type_checks_root_dirs (method, L250-L266, parent: TestValidateArtifact)

> *Summary: This test verifies that an artifact configured with a `skills` section correctly triggers specific validation warnings during the artifact validation process. It constructs an artifact, validates it, and asserts that at least one warning message contains either "rules/" or "skills/".*


### test_bundle_skips_skills_check (method, L268-L286, parent: TestValidateArtifact)

> *Summary: This test verifies that when validating a bundle artifact, no errors are reported, and specifically ensures that the validation process does not generate any warnings related to "skills." It takes an artifact created as a bundle as input and asserts the resulting list of issues contains zero errors and no skill-related messages.*

