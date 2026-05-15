# cli/tests/test_registry.py

3 class(es): TestParseFrontmatter, TestLoadPack, TestListPacks. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestParseFrontmatter | class |  |
| TestLoadPack | class |  |
| TestListPacks | class |  |

## Chunks

### TestParseFrontmatter (class, L7-L56)

> *Summary: This test suite verifies the `parse_frontmatter` function by providing various string inputs. It asserts that the function correctly separates YAML frontmatter (parsed into a dictionary) from the main body content, handling cases like valid data, missing delimiters, boolean type conversion, and stripping quotes from string values.*


### test_valid_frontmatter (method, L10-L18, parent: TestParseFrontmatter)

> *Summary: This test verifies that the `parse_frontmatter` function correctly separates YAML metadata from main content. It takes a string containing frontmatter and body, asserting that the parsed dictionary matches expected values and the remaining text is returned as the body.*


### test_no_frontmatter_returns_empty_dict_and_full_text (method, L20-L27, parent: TestParseFrontmatter)

> *Summary: When provided with text lacking YAML frontmatter, the function returns an empty dictionary for metadata and the entire input string as the body content. This test verifies that no parsing occurs when the expected structure is absent.*


### test_missing_closing_delimiter_returns_empty_dict_and_full_text (method, L29-L36, parent: TestParseFrontmatter)

> *Summary: When provided with frontmatter lacking a closing delimiter, the function returns an empty dictionary for the metadata and the entire input string as the body content. This test verifies that incomplete YAML blocks are handled gracefully by returning no parsed data.*


### test_boolean_values_converted_to_python_bools (method, L38-L47, parent: TestParseFrontmatter)

> *Summary: This test verifies that boolean values within YAML frontmatter are correctly parsed into native Python booleans. It inputs a string containing various true/false representations and asserts the resulting dictionary contains accurate `True` or `False` types for those keys.*


### test_quoted_strings_have_quotes_stripped (method, L49-L56, parent: TestParseFrontmatter)

> *Summary: This test verifies that the `parse_frontmatter` function correctly strips surrounding quotes from string values within YAML frontmatter. It takes a string containing frontmatter and body, asserting that parsed fields retain their intended content without extraneous quotation marks.*


### TestLoadPack (class, L59-L80)

> *Summary: Tests verify that the `load_pack` function returns `None` when provided with a pack name that does not exist or when the specified directory lacks a manifest file, using temporary filesystem fixtures for isolation. These tests ensure robust handling of missing or incomplete installation packages.*


### test_returns_none_for_nonexistent_pack (method, L62-L68, parent: TestLoadPack)

> *Summary: When attempting to load a pack with an invalid name, the function returns `None`. This test verifies that calling `registry.load_pack()` with a non-existent identifier yields no result.*


### test_returns_none_when_no_manifest (method, L70-L80, parent: TestLoadPack)

> *Summary: When provided with a directory lacking a `manifest.json`, the function returns `None` after setting the content directory path. This test verifies that loading a pack without manifest data results in no return value.*


### TestListPacks (class, L83-L107)

> *Summary: This test verifies that the pack listing function correctly discovers and returns names of valid content packs from a specified directory structure. It ensures only directories containing a `manifest.json` file are included in the resulting list, while others are ignored.*


### test_returns_pack_names (method, L86-L107, parent: TestListPacks)

> *Summary: This test verifies that the pack listing function correctly identifies valid installation packages by scanning a temporary directory structure. It ensures only directories containing a `manifest.json` file are returned, excluding those without one.*

