# test/oai/test_utils.py

15 function(s): _compare_lists_of_dicts, mock_os_environ, test_filter_config, test_filter_config_comprehensive, test_config_list_from_json, test_config_list_openai_aoai, test_config_list_openai_aoai_env_vars, test_config_list_openai_aoai_env_vars_multi, test_config_list_openai_aoai_file_not_found, test_config_list_from_dotenv and 5 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _compare_lists_of_dicts | function |  |
| mock_os_environ | function |  |
| test_filter_config | function |  |
| test_filter_config_comprehensive | function |  |
| test_config_list_from_json | function |  |
| test_config_list_openai_aoai | function |  |
| test_config_list_openai_aoai_env_vars | function |  |
| test_config_list_openai_aoai_env_vars_multi | function |  |
| test_config_list_openai_aoai_file_not_found | function |  |
| test_config_list_from_dotenv | function |  |
| test_get_config_list | function |  |
| test_get_first_llm_config | function |  |
| test_get_first_llm_config_incorrect_config | function |  |
| test_tags | function |  |
| test_is_valid_api_key | function |  |

## Chunks

### _compare_lists_of_dicts (function, L199-L202)

> *Summary: Compares two lists of dictionaries by serializing each dictionary to a JSON string with sorted keys and then comparing the resulting sorted lists of strings. It returns `True` if both input lists contain the exact same data, regardless of original order.*


### mock_os_environ (function, L206-L208)

> *Summary: This context manager temporarily overrides the system's environment variables with a predefined set (`ENV_VARS`) for testing purposes and yields control back to the caller upon exiting the block.*


### test_filter_config (function, L212-L222)

> *Summary: This test verifies the `filter_config` function by passing a sample JSON dictionary, a filter configuration, and an exclusion list as inputs. It asserts that the resulting filtered list matches a predefined expected output structure.*


### test_filter_config_comprehensive (function, L226-L250)

> *Summary: This test function comprehensively validates the `filter_config` logic by running it against various configurations provided in a test case. It takes a filter dictionary and an exclusion list as input, asserting that the resulting list of configurations matches the expected output structure.*


### test_config_list_from_json (function, L253-L299)

> *Summary: This test verifies the `config_list_from_json` function by loading configuration lists from various inputs, including temporary files and environment variables. It asserts that the loaded list matches expected data structures, correctly applies filtering based on provided dictionaries, and handles file path variations.*


### test_config_list_openai_aoai (function, L302-L335)

> *Summary: This test verifies the configuration loading mechanism by providing a temporary directory containing sample API key and base URL files for both OpenAI and AOAI. It asserts that the resulting list of configurations correctly combines keys and URLs from these inputs, matching an expected structure including specific API type metadata for Azure.*


### test_config_list_openai_aoai_env_vars (function, L347-L357)

> *Summary: This test verifies that the `config_list_openai_aoai` utility correctly loads configurations from environment variables. It asserts that the returned list contains exactly two dictionaries: one for OpenAI and one specifically configured for Azure AI services.*


### test_config_list_openai_aoai_env_vars_multi (function, L369-L386)

> *Summary: This test verifies that the `config_list_openai_aoai` function correctly parses and returns a list of configuration dictionaries when multiple environment variables are provided. It asserts the presence of specific configurations for both OpenAI and Azure API endpoints with different keys and base URLs.*


### test_config_list_openai_aoai_file_not_found (function, L389-L392)

> *Summary: When provided with a non-existent file path for configuration, this test verifies that the function returns an empty list of configurations. It achieves this by temporarily clearing environment variables before calling the utility.*


### test_config_list_from_dotenv (function, L395-L481)

> *Summary: This test suite verifies the `config_list_from_dotenv` function's behavior by creating temporary `.env` files and testing various scenarios. It asserts correct configuration loading, filtering based on models, handling of missing files, and proper logging when API keys are invalid or absent.*


### test_get_config_list (function, L484-L528)

> *Summary: This test verifies the `get_config_list` function by ensuring it correctly processes lists of API keys and base URLs into structured configuration dictionaries. It validates correct data mapping, handles mismatched input lengths by raising an error, and tests edge cases like empty inputs or missing URL information.*


### test_get_first_llm_config (function, L553-L554)

> *Summary: This test verifies that the `get_first_llm_config` function correctly extracts and returns a specific configuration dictionary from an input LLM configuration. It asserts that the actual output matches a predefined expected structure.*


### test_get_first_llm_config_incorrect_config (function, L564-L566)

> *Summary: Asserts that calling `get_first_llm_config` with a provided configuration dictionary raises a `ValueError` containing the specified error message. This tests the function's behavior when given invalid input configurations.*


### test_tags (function, L569-L593)

> *Summary: This test verifies the `filter_config` function's behavior when filtering a configuration list based on various tag criteria. It asserts that matching configurations are correctly identified using exact, partial, and intersecting tag lists, while ensuring no matches occur for non-existent tags.*


### test_is_valid_api_key (function, L596-L617)

> *Summary: This test function verifies the `is_valid_api_key` utility by asserting expected boolean outcomes for various input strings. It checks edge cases, invalid formats, and confirms acceptance of specific valid structural patterns, including a mocked key.*

