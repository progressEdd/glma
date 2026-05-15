# test/beta/tools/test_skill_search.py

29 function(s): _make_tarball, _monorepo_tarball, _standalone_tarball, _make_meta, test_extract_skill_monorepo, test_extract_skill_standalone, test_extract_skill_no_skill_md_raises, test_extract_skill_excludes_git_dir, test_extract_skill_overwrites_existing, test_extract_skill_validates_metadata and 19 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_tarball | function |  |
| _monorepo_tarball | function |  |
| _standalone_tarball | function |  |
| _make_meta | function |  |
| test_extract_skill_monorepo | function |  |
| test_extract_skill_standalone | function |  |
| test_extract_skill_no_skill_md_raises | function |  |
| test_extract_skill_excludes_git_dir | function |  |
| test_extract_skill_overwrites_existing | function |  |
| test_extract_skill_validates_metadata | function |  |
| test_search_skills_formats_output | function |  |
| test_search_skills_no_results | function |  |
| test_search_skills_network_error | function |  |
| test_install_skill_monorepo | function |  |
| test_install_skill_standalone | function |  |
| test_install_skill_records_hash | function |  |
| test_install_skill_rate_limit | function |  |
| test_install_skill_not_found | function |  |
| test_install_skill_invalid_id | function |  |
| test_remove_skill_success | function |  |
| test_remove_skill_cleans_lock_file | function |  |
| test_remove_skill_not_found | function |  |
| test_remove_skill_path_traversal_blocked | function |  |
| test_lock_record_and_read | function |  |
| test_lock_remove | function |  |
| test_lock_get_hash | function |  |
| test_lock_read_nonexistent | function |  |
| test_toolkit_exposes_six_tools | function |  |
| test_toolkit_individual_tools_accessible | function |  |

## Chunks

### _make_tarball (function, L42-L51)

> *Summary: Creates a compressed `.tar.gz` archive in memory from a dictionary mapping filenames to their content (bytes or string). It iterates through the provided entries, encodes strings if necessary, and writes each file into the resulting byte stream.*


### _monorepo_tarball (function, L54-L58)

> *Summary: Generates a compressed tarball containing skill documentation and associated rules for a specified `skill_id`. It takes the desired skill ID as input and returns the resulting binary data.*


### _standalone_tarball (function, L61-L65)

> *Summary: Generates a byte string representing a tarball containing specific files and content. It packages a markdown file (`SKILL.md`) and a simple Python script into the archive structure.*


### _make_meta (function, L68-L78)

> *Summary: Creates a `SkillMetadata` object for mocking installation tests by setting up a specific directory structure within a temporary path. It configures the metadata with predefined values like name, description, and version.*


### test_extract_skill_monorepo (function, L81-L94)

> *Summary: This test verifies the `extract_skill` function by providing a gzipped tarball containing skill data and an output directory. It asserts that the extracted metadata matches expected values and that specific files, like `SKILL.md` and rule files, are present in the destination structure.*


### test_extract_skill_standalone (function, L97-L108)

> *Summary: This test verifies the `extract_skill` function by providing it a standalone compressed archive containing skill data. It asserts that the extraction process correctly places the expected metadata and files, such as documentation and Python scripts, into the specified destination directory.*


### test_extract_skill_no_skill_md_raises (function, L111-L118)

> *Summary: This test verifies that attempting to extract skills from a tarball containing no `SKILL.md` file raises a specific `SkillInstallError`. It achieves this by creating a minimal tar archive and calling the extraction function with an empty skill directory path.*


### test_extract_skill_excludes_git_dir (function, L121-L134)

> *Summary: This test verifies that the skill extraction process correctly ignores files within a `.git` directory when unpacking a tarball. It creates a compressed archive containing both a skill file and a Git configuration file, then asserts that no part of the Git structure remains in the extracted destination.*


### test_extract_skill_overwrites_existing (function, L137-L148)

> *Summary: This test verifies that the skill extraction process overwrites existing files within a destination directory structure. It takes a compressed tarball as input and asserts that any pre-existing file is replaced by the newly extracted content, specifically checking for the removal of an old "stale.txt" in favor of a new "SKILL.md".*


### test_extract_skill_validates_metadata (function, L151-L160)

> *Summary: This test verifies that attempting to extract a skill with an improperly formatted name raises an `InvalidSkillError`. It achieves this by creating a tarball containing a Markdown file with an invalid skill name and calling the extraction function within a `pytest.raises` context.*


### test_search_skills_formats_output (function, L164-L181)

> *Summary: This test verifies the output format of a skill search operation by mocking the underlying client to return predefined skill data. It asserts that the resulting string contains expected counts, specific skill names, install statistics, and the correct function call for installation.*


### test_search_skills_no_results (function, L185-L190)

> *Summary: This test verifies the behavior when a skill search yields no results by mocking the `SkillsClient` to return an empty list. It asserts that the resulting output from the toolkit contains the message "No skills found".*


### test_search_skills_network_error (function, L194-L200)

> *Summary: This test verifies error handling when the underlying skill search client fails due to a network issue. It mocks the `SkillsClient.search` method to raise an exception and asserts that the toolkit's output correctly reflects this connection refusal error.*


### test_install_skill_monorepo (function, L204-L212)

> *Summary: This test verifies the installation process of a skill within a monorepo structure. It mocks the skill download to simulate fetching metadata and then asserts that the resulting output string contains expected installation confirmation, description, and loading commands for the specified skill ID.*


### test_install_skill_standalone (function, L216-L222)

> *Summary: This test verifies the standalone installation of a skill by mocking the download process for a specific skill ID. It asserts that the resulting object confirms the successful installation of the "last30days" skill.*


### test_install_skill_records_hash (function, L226-L238)

> *Summary: This test verifies that installing a skill correctly writes its computed hash and source information to `skills-lock.json`. It mocks the skill download process to ensure the resulting lock file contains the expected metadata for the specified skill ID.*


### test_install_skill_rate_limit (function, L242-L248)

> *Summary: This test verifies the rate limiting behavior of skill installation by mocking `SkillsClient.download_skill` to raise a specific runtime error. It asserts that the resulting output from calling `toolkit.install_skill()` contains the phrase "rate limit".*


### test_install_skill_not_found (function, L252-L258)

> *Summary: This test verifies the system's handling when a requested skill cannot be downloaded. It mocks `SkillsClient.download_skill` to raise a `RuntimeError` and asserts that the resulting installation attempt correctly reports the "not found" status.*


### test_install_skill_invalid_id (function, L262-L266)

> *Summary: This test verifies that attempting to install a skill with an invalid ID triggers the expected error response. It initializes a `SkillSearchToolkit` and calls its installation method using `"invalid"` as the input skill identifier.*


### test_remove_skill_success (function, L270-L280)

> *Summary: This test verifies the successful removal of a registered skill from the search toolkit. It initializes a skill directory, registers a dummy skill file, calls the `remove_skill` method with the skill's name, and asserts that the expected success message is returned and the skill directory no longer exists.*


### test_remove_skill_cleans_lock_file (function, L284-L300)

> *Summary: This test verifies that removing a skill correctly updates the lock file by calling `toolkit.remove_skill()`. It initializes a mock environment with a pre-populated skills lock and asserts that the specified skill is absent from the resulting JSON data.*


### test_remove_skill_not_found (function, L304-L311)

> *Summary: This test verifies that attempting to remove a skill that does not exist returns an appropriate error message. It initializes the `SkillSearchToolkit` and calls the `remove_skill()` method with a non-existent skill name, asserting the resulting output contains "Cannot remove".*


### test_remove_skill_path_traversal_blocked (function, L315-L325)

> *Summary: This test verifies that the skill removal mechanism prevents path traversal attacks by attempting to delete a skill located outside the designated installation directory. It asserts that the operation fails and the external directory remains untouched when an invalid path is provided as input.*


### test_lock_record_and_read (function, L328-L336)

> *Summary: This test verifies the functionality of a skills lock mechanism by first recording skill metadata (name, source, hash) and then reading it back. It asserts that the retrieved data correctly reflects the recorded version and specific skill details.*


### test_lock_remove (function, L339-L348)

> *Summary: This test verifies that a specific skill can be successfully removed from the stored skills data managed by a `SkillsLock` object. It records two skills, removes one, and then asserts that only the remaining skill is present when reading the lock's contents.*


### test_lock_get_hash (function, L351-L356)

> *Summary: This test verifies the functionality of retrieving a stored hash from a skills lock object. It initializes the lock, records a skill's data, and then asserts that `get_hash` returns the correct value for an existing key while returning `None` for a missing one.*


### test_lock_read_nonexistent (function, L359-L363)

> *Summary: This test verifies that reading from a non-existent skills lock file returns a default structure. It initializes the `SkillsLock` with a path to a missing JSON file and asserts the returned data matches an empty versioned dictionary.*


### test_toolkit_exposes_six_tools (function, L367-L374)

> *Summary: This test verifies that a `SkillSearchToolkit` instance exposes exactly six predefined tools. It achieves this by retrieving all schemas from the toolkit and asserting that the set of function names matches an expected list of six specific skill management operations.*


### test_toolkit_individual_tools_accessible (function, L378-L383)

> *Summary: This test verifies that specific methods within a `SkillSearchToolkit` instance expose the correct function names in their associated schemas. It iterates over predefined tool actions, retrieves the schema for each method using the toolkit and context, and asserts the schema's function name matches the expected attribute name.*

