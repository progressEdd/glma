# test/interop/litellm/test_litellm_config_factory.py

2 class(es): TestLiteLLmConfigFactory, TestCrawl4aiCompatibility. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestLiteLLmConfigFactory | class |  |
| TestCrawl4aiCompatibility | class |  |

## Chunks

### TestLiteLLmConfigFactory (class, L16-L91)

> *Summary: This test suite verifies the `LiteLLmConfigFactory`'s ability to transform various input configuration lists into standardized legacy, LLM, and strategy keyword argument dictionaries. It uses parameterized tests to assert correct output structures for different provider types like OpenAI, Deepseek, Azure, Google, Anthropic, Ollama, etc.*


### test_number_of_factories (method, L17-L18, parent: TestLiteLLmConfigFactory)

> *Summary: Verifies that the `LiteLLmConfigFactory` class maintains exactly three registered factory instances. This assertion checks the internal state of the configuration factory registry.*


### test_get_provider_and_api_key (method, L81-L91, parent: TestLiteLLmConfigFactory)

> *Summary: This test verifies that a configuration factory correctly generates and exposes three distinct sets of parameters—legacy, LLM-specific, and strategy—from an input list of configurations. It asserts that the generated adapter's methods return the pre-defined expected dictionaries for each parameter set.*


### TestCrawl4aiCompatibility (class, L94-L209)

> *Summary: This test suite verifies compatibility fixes related to `crawl4ai` version detection and configuration adaptation within the LiteLLM factory. It tests scenarios for detecting installed versions, validating version thresholds (v0.5 or higher), and ensuring correct transformation of input configurations into legacy, LLM-specific, and strategy keyword arguments across various API types.*


### test_get_crawl4ai_version_when_installed (method, L97-L101, parent: TestCrawl4aiCompatibility)

> *Summary: This test verifies that the `get_crawl4ai_version` function correctly retrieves a specific version string when the `crawl4ai` package is present and its metadata is mocked to return `"0.5.0"`. It asserts that the returned value matches the mocked version.*


### test_get_crawl4ai_version_when_not_installed (method, L103-L113, parent: TestCrawl4aiCompatibility)

> *Summary: This test verifies that the `get_crawl4ai_version` function correctly returns `None` when the `crawl4ai` package is not installed. It achieves this by mocking a `PackageNotFoundError` and ensuring `sys.modules` reflects the absence of the package.*


### test_is_crawl4ai_v05_or_higher (method, L129-L133, parent: TestCrawl4aiCompatibility)

> *Summary: This test verifies the version comparison logic by mocking a function that returns a specific `version` string. It asserts that the returned boolean result from checking if the mocked version is v05 or higher matches the provided `expected` value.*


### test_is_crawl4ai_v05_or_higher_invalid_version (method, L135-L139, parent: TestCrawl4aiCompatibility)

> *Summary: When the version retrieval function returns an invalid string, this test asserts that the version checking logic correctly evaluates to `False`. It verifies the behavior of the comparison function when encountering non-standard input.*


### test_config_adaptation_with_multiple_parameters (method, L141-L169, parent: TestCrawl4aiCompatibility)

> *Summary: This test verifies that a configuration factory correctly adapts input parameters for different output formats. It takes a list of Azure API configurations and asserts the resulting structures match expected legacy, LLM, and strategy keyword arguments.*


### test_config_adaptation_preserves_other_parameters (method, L171-L185, parent: TestCrawl4aiCompatibility)

> *Summary: This test verifies that when adapting a configuration list, parameters not intended for the LLM config are correctly preserved in the strategy arguments. It confirms that tags remain accessible while provider and API key details are correctly mapped to the LLM configuration kwargs.*


### test_provider_format_in_adapted_config (method, L197-L202, parent: TestCrawl4aiCompatibility)

> *Summary: This test verifies that the `LiteLLmConfigFactory` correctly sets the provider format within an adapted configuration object based on provided API type and model inputs. It asserts that the resulting configuration's "provider" key matches the expected value for various scenarios.*


### test_backward_compatibility_no_crawl4ai (method, L204-L209, parent: TestCrawl4aiCompatibility)

> *Summary: Verifies that the configuration factory correctly generates legacy keyword arguments for an OpenAI model even when a specific dependency (`crawl4ai`) is absent. It takes a list of configurations and asserts the resulting adapter matches expected legacy parameters like `api_token` and `provider`.*

