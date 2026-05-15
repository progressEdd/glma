# test/conftest.py

32 function(s): mock, async_mock, patch_pytest_terminal_writer, get_safe_api_types_from_test_context, get_credentials_from_file, get_credentials_from_env, get_credentials, credentials_azure, credentials_azure_gpt_4_1_mini, credentials_azure_gpt_4o_mini and 22 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mock | function |  |
| async_mock | function |  |
| patch_pytest_terminal_writer | function |  |
| get_safe_api_types_from_test_context | function |  |
| get_credentials_from_file | function |  |
| get_credentials_from_env | function |  |
| get_credentials | function |  |
| credentials_azure | function |  |
| credentials_azure_gpt_4_1_mini | function |  |
| credentials_azure_gpt_4o_mini | function |  |
| credentials | function |  |
| credentials_all | function |  |
| credentials_openai_mini | function |  |
| credentials_gpt_4o | function |  |
| credentials_o1_mini | function |  |
| credentials_o4_mini | function |  |
| credentials_o1 | function |  |
| credentials_gpt_4o_realtime | function |  |
| credentials_responses_gpt_4o_mini | function |  |
| credentials_responses_gpt_4o | function |  |
| credentials_gemini_realtime | function |  |
| credentials_gemini_flash | function |  |
| credentials_gemini_flash_exp | function |  |
| credentials_anthropic_claude_sonnet | function |  |
| credentials_deepseek_reasoner | function |  |
| credentials_deepseek_chat | function |  |
| get_mock_credentials | function |  |
| mock_credentials | function |  |
| mock_azure_credentials | function |  |
| pytest_sessionfinish | function |  |
| credentials_from_test_param | function |  |
| user_proxy | function |  |

## Chunks

### mock (function, L20-L21)

> *Summary: Provides a factory function that returns an instance of `MagicMock` for use in tests. This allows developers to easily substitute complex dependencies with controllable mock objects during testing.*


### async_mock (function, L25-L26)

> *Summary: Provides a factory function to instantiate and return an `AsyncMock` object for use in asynchronous testing scenarios. This mock can then be injected into tests to simulate asynchronous dependencies.*


### patch_pytest_terminal_writer (function, L29-L46)

> *Summary: This function intercepts and wraps the `write` and `line` methods of Pytest's `TerminalWriter`. It ensures that any message passed to these methods is sanitized for secrets before being written to the terminal.*


### get_safe_api_types_from_test_context (function, L68-L112)

> *Summary: Retrieves a set of allowed API type strings by inspecting the current test's pytest markers via the call stack. If relevant markers are found, it returns the corresponding types; otherwise, it defaults to allowing all known SDK types for backward compatibility.*


### get_credentials_from_file (function, L115-L159)

> *Summary: Loads LLM configuration from a JSON file while applying safety filters based on the current test context. It accepts an optional filter dictionary and temperature, returning a `Credentials` object containing the configured settings.*


### get_credentials_from_env (function, L162-L183)

> *Summary: Retrieves API credentials by reading a specified environment variable and constructing a `Credentials` object. It requires the environment variable to be set; otherwise, it skips the test execution.*


### get_credentials (function, L186-L230)

> *Summary: Retrieves configuration credentials by checking environment variables first, then a local configuration file, and finally falling back to a single specified environment variable. It filters the results based on the provided `api_type` and returns a `Credentials` object or `None`.*


### credentials_azure (function, L234-L238)

> *Summary: Retrieves Azure credentials by first attempting to read them from environment variables; if that fails, it falls back to reading them from a configuration file. The function returns an object conforming to the `Credentials` type upon successful retrieval.*


### credentials_azure_gpt_4_1_mini (function, L242-L249)

> *Summary: Retrieves Azure OpenAI credentials for the GPT-4.1-mini model by first attempting to read them from environment variables, falling back to reading them from a configuration file upon failure. The function returns an object conforming to the `Credentials` type.*


### credentials_azure_gpt_4o_mini (function, L253-L258)

> *Summary: Retrieves Azure OpenAI GPT-4o-mini credentials by first attempting to read them from environment variables, falling back to reading them from a configuration file if the environment variable lookup fails. The function returns an object conforming to the `Credentials` type upon successful retrieval.*


### credentials (function, L262-L266)

> *Summary: Retrieves credentials by first attempting to read them from environment variables, specifically filtering for "gpt-4o" tags. If that fails, it falls back to reading the credentials from a configuration file using the same tag filter.*


### credentials_all (function, L270-L274)

> *Summary: Retrieves application credentials by first attempting to read them from environment variables; if that fails, it falls back to loading them from a configuration file. The function returns a `Credentials` object containing the loaded secrets.*


### credentials_openai_mini (function, L278-L281)

> *Summary: Retrieves credentials for a specific OpenAI model configuration, using the `get_credentials` helper function with predefined API key and filtering parameters. It returns an object conforming to the `Credentials` type.*


### credentials_gpt_4o (function, L285-L286)

> *Summary: Retrieves specific API credentials for the GPT-4o model by querying a credential store using an environment variable key. It returns a `Credentials` object containing the necessary authentication details.*


### credentials_o1_mini (function, L290-L291)

> *Summary: Retrieves a `Credentials` object by fetching credentials for the "o1-mini" OpenAI model using the provided API key. This function acts as a fixture to supply necessary authentication details during testing.*


### credentials_o4_mini (function, L295-L296)

> *Summary: Retrieves a specific set of credentials by fetching the "OPENAI\_API\_KEY" for the "o4-mini" model using an OpenAI API type. It returns a `Credentials` object containing the necessary authentication details.*


### credentials_o1 (function, L300-L301)

> *Summary: Retrieves a `Credentials` object by fetching specific API key details for the "o1" model from an OpenAI source. It uses predefined configuration parameters to narrow down the credential search.*


### credentials_gpt_4o_realtime (function, L305-L312)

> *Summary: Retrieves and returns a `Credentials` object configured for the OpenAI API using the "gpt-4o-realtime-preview" model. It fetches credentials based on the environment variable "OPENAI\_API\_KEY" with specific filtering and temperature settings.*


### credentials_responses_gpt_4o_mini (function, L316-L321)

> *Summary: This function retrieves and returns a `Credentials` object by fetching API credentials for the "gpt-4.1-mini" model using the OpenAI API type set to "responses." It relies on an external `get_credentials` helper function for its operation.*


### credentials_responses_gpt_4o (function, L325-L330)

> *Summary: Retrieves and returns a `Credentials` object by fetching API credentials for the GPT-4o model using the provided OpenAI API key. This function specifically targets response-based credential retrieval.*


### credentials_gemini_realtime (function, L334-L337)

> *Summary: Retrieves and returns a `Credentials` object by fetching credentials specifically tagged for "gemini-realtime" using the Gemini API key configuration. This function acts as a factory to provide necessary authentication details for real-time Gemini operations.*


### credentials_gemini_flash (function, L341-L344)

> *Summary: Retrieves and returns a `Credentials` object specifically configured for the Gemini 2.5 Flash model using an API key sourced from the environment variable "GEMINI\_API\_KEY". This function acts as a factory to provide necessary credentials for testing purposes.*


### credentials_gemini_flash_exp (function, L348-L351)

> *Summary: Retrieves a `Credentials` object by fetching credentials specifically tagged for the "gemini-flash-exp" configuration, using the Gemini 3 Flash preview model. This function acts as a setup utility to provide necessary authentication details for testing purposes.*


### credentials_anthropic_claude_sonnet (function, L355-L361)

> *Summary: Retrieves and returns a `Credentials` object configured for the Anthropic Claude Sonnet model. It fetches necessary credentials using the "ANTHROPIC\_API\_KEY" environment variable, specifically tagging it for this model variant.*


### credentials_deepseek_reasoner (function, L365-L371)

> *Summary: Retrieves and returns a `Credentials` object configured specifically for the DeepSeek Reasoner model. It fetches necessary API key credentials using predefined configuration parameters pointing to the DeepSeek API endpoint.*


### credentials_deepseek_chat (function, L375-L381)

> *Summary: Retrieves and returns a `Credentials` object configured specifically for interacting with the DeepSeek chat API. It fetches necessary credentials using an environment variable key while setting specific model, API type, and base URL parameters.*


### get_mock_credentials (function, L384-L393)

> *Summary: Creates and returns a `Credentials` object configured with mock API keys for a specified language model and optional temperature setting. This helper function abstracts the setup of LLM configuration using predefined mock credentials.*


### mock_credentials (function, L397-L398)

> *Summary: This function generates and returns a `Credentials` object by calling an external helper with the "gpt-4o" model specified. It serves to provide mocked credentials for testing purposes.*


### mock_azure_credentials (function, L402-L413)

> *Summary: Creates and returns a `Credentials` object configured to use Azure credentials with specific mock API details and a fixed temperature setting. This function simulates the setup of an LLM connection for testing purposes.*


### pytest_sessionfinish (function, L416-L421)

> *Summary: When a pytest session concludes, this function checks if the initial exit status was 5 (indicating no tests were collected) and overrides it to 0 if true. This ensures that test runs with no collected tests report success instead of failure.*


### credentials_from_test_param (function, L425-L431)

> *Summary: Retrieves and validates credential objects by looking up the fixture specified in the test parameter. It accepts a `pytest.FixtureRequest` and returns a `Credentials` instance, raising an error if the retrieved value is not of that type.*


### user_proxy (function, L435-L440)

> *Summary: Creates and returns a configured `UserProxyAgent` instance named "User" that is set to never prompt for human input and disables code execution. This proxy object can then be used within testing or agent workflows.*

