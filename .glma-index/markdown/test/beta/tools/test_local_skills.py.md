# test/beta/tools/test_local_skills.py

21 function(s): skill_tree, test_parse_frontmatter_basic, test_parse_frontmatter_no_header, test_parse_frontmatter_unclosed, test_parse_frontmatter_quoted_values, test_parse_frontmatter_multiline_description, test_loader_discover_names, test_loader_discover_metadata, test_loader_priority, test_loader_nonexistent_path and 11 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| skill_tree | function |  |
| test_parse_frontmatter_basic | function |  |
| test_parse_frontmatter_no_header | function |  |
| test_parse_frontmatter_unclosed | function |  |
| test_parse_frontmatter_quoted_values | function |  |
| test_parse_frontmatter_multiline_description | function |  |
| test_loader_discover_names | function |  |
| test_loader_discover_metadata | function |  |
| test_loader_priority | function |  |
| test_loader_nonexistent_path | function |  |
| test_loader_load | function |  |
| test_loader_load_missing | function |  |
| test_loader_get_path | function |  |
| test_loader_rejects_invalid_skill_name | function |  |
| test_loader_strict_requires_name_and_description | function |  |
| test_loader_strict_rejects_mismatched_name | function |  |
| test_loader_cache_avoids_rescan | function |  |
| test_loader_invalidate_forces_rescan | function |  |
| test_tool_exposes_three_functions | function |  |
| test_run_skill_script_schema | function |  |
| test_run_skill_script_executes | function |  |

## Chunks

### skill_tree (function, L21-L66)

> *Summary: Creates a minimal directory structure containing two skill definitions: one with versioning and scripts (`react-best-practices`) and another without (`markdown-guide`). It returns the root temporary path after setting up these files.*


### test_parse_frontmatter_basic (function, L69-L74)

> *Summary: This test verifies the basic functionality of parsing YAML frontmatter from a string input. It asserts that the `parse_frontmatter` function correctly extracts and types the "name," "description," and "version" fields from the provided text block.*


### test_parse_frontmatter_no_header (function, L77-L78)

> *Summary: Asserts that parsing content without a YAML frontmatter header correctly returns an empty dictionary. The function takes a string as input and expects an empty dict as output when no frontmatter is present.*


### test_parse_frontmatter_unclosed (function, L81-L82)

> *Summary: This test verifies that the frontmatter parsing function correctly handles input where the closing delimiter is missing. It asserts that providing an unclosed YAML block results in an empty dictionary output.*


### test_parse_frontmatter_quoted_values (function, L85-L89)

> *Summary: This test verifies that the `parse_frontmatter` function correctly extracts values from YAML frontmatter when those values are enclosed in quotes, even if they contain characters like colons. It takes a string containing quoted key-value pairs and asserts the resulting dictionary contains the exact quoted content.*


### test_parse_frontmatter_multiline_description (function, L92-L95)

> *Summary: This test verifies that the `parse_frontmatter` function correctly handles multi-line descriptions within YAML frontmatter. It takes a string containing frontmatter with a block scalar description and asserts that the parsed result includes the full, concatenated text of that description.*


### test_loader_discover_names (function, L98-L103)

> *Summary: Given a skill tree path, this test initializes a `SkillLoader` and discovers all available skills within that tree. It then asserts that the set of discovered skill names exactly matches `{"react-best-practices", "markdown-guide"}`.*


### test_loader_discover_metadata (function, L106-L117)

> *Summary: This test verifies that a `SkillLoader` correctly discovers and loads skill metadata from a given directory structure. It asserts specific attributes like description, version, and script presence for predefined skills within the loaded set.*


### test_loader_priority (function, L120-L133)

> *Summary: This test verifies that when multiple skill definitions exist, the one found in the first provided path takes precedence. It initializes a `SkillLoader` with two directories containing identical skills and asserts that the loaded metadata reflects the definition from the initial directory.*


### test_loader_nonexistent_path (function, L136-L139)

> *Summary: When initialized with a non-existent directory path, the skill loader's `discover()` method returns an empty list, indicating no skills were found.*


### test_loader_load (function, L142-L148)

> *Summary: This test verifies that a `SkillLoader` correctly loads skill content from a specified directory path. It asserts that the loaded content for "react-best-practices" contains expected strings like "React Best Practices" and "functional components".*


### test_loader_load_missing (function, L151-L155)

> *Summary: This test verifies that attempting to load a skill using a non-existent identifier raises a `SkillNotFoundError`. It initializes a `SkillLoader` with a given skill tree path and asserts the expected exception when calling `.load()` with an invalid name.*


### test_loader_get_path (function, L158-L163)

> *Summary: This test verifies that a `SkillLoader` correctly resolves the file system path for a given skill name within a provided skill tree structure. It asserts that the returned path matches the expected concatenation of the input skill tree and the target skill identifier.*


### test_loader_rejects_invalid_skill_name (function, L166-L169)

> *Summary: This test verifies that the `SkillLoader` correctly raises an `InvalidSkillNameError` when attempting to load a skill using an invalid name path. It initializes the loader with a given skill tree and asserts the expected exception during the loading attempt.*


### test_loader_strict_requires_name_and_description (function, L172-L179)

> *Summary: This test verifies that the skill loader fails when a skill file lacks mandatory metadata fields like `name` and `description`. It asserts that an `InvalidSkillError` is raised during discovery if only basic license information is present in the YAML frontmatter.*


### test_loader_strict_rejects_mismatched_name (function, L182-L197)

> *Summary: When initialized with `strict=True`, this test verifies that the skill loader rejects a skill if its internal name (`different-name`) does not match the containing directory's name (`skill-dir-name`). It asserts that an `InvalidSkillError` is raised upon discovery.*


### test_loader_cache_avoids_rescan (function, L200-L211)

> *Summary: This test verifies that the skill loading mechanism caches its results after an initial scan. It confirms that a subsequent call to discover skills, even after adding new files to the directory, returns the original set of discovered skills without rescanning.*


### test_loader_invalidate_forces_rescan (function, L214-L225)

> *Summary: This test verifies that invalidating the skill loader forces a rescan, ensuring newly added skills are detected. It initializes the loader with a skill tree, adds a new skill directory and file, calls `invalidate()`, and then asserts the new skill appears after rediscovery.*


### test_tool_exposes_three_functions (function, L229-L236)

> *Summary: This test verifies that a `SkillsToolkit` initialized with a skill tree exposes exactly three specific functions. It asserts that the retrieved schemas contain functions named "list\_skills", "load\_skill", and "run\_skill\_script".*


### test_run_skill_script_schema (function, L240-L257)

> *Summary: This test verifies that the `SkillsToolkit` correctly generates a JSON schema for its `run_skill_script` method. It asserts that the resulting schema defines a function type requiring both a string `name` and a string `script`.*


### test_run_skill_script_executes (function, L260-L267)

> *Summary: This test executes a Python script named `scaffold.py` within a specific directory structure derived from an input skill tree. It verifies that the execution successfully produces output containing the string "scaffold".*

