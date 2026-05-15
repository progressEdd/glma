# test/test_llm_config.py

1 function(s): openai_llm_config_entry. 2 class(es): TestLLMConfigEntry, TestLLMConfig. 40 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| openai_llm_config_entry | function |  |
| TestLLMConfigEntry | class |  |
| TestLLMConfig | class |  |

## Chunks

### openai_llm_config_entry (function, L65-L66)

> *Summary: Creates a configuration object for an OpenAI LLM, specifically setting the model to "gpt-4o-mini" and providing a mock API key. This function returns a fully initialized `OpenAILLMConfigEntry` instance ready for testing purposes.*


### TestLLMConfigEntry (class, L69-L117)

> *Summary: This test suite verifies the functionality of `OpenAILLMConfigEntry` by checking for extra field handling, successful serialization to a dictionary, correct deserialization from a dictionary, and robust access via `.get()`, item indexing (`[]`), and item assignment (`[]`). It ensures the configuration object behaves like a dictionary while maintaining its defined structure.*


### test_extra_fields (method, L70-L78, parent: TestLLMConfigEntry)

> *Summary: Verifies that an `OpenAILLMConfigEntry` instance correctly stores and exposes arbitrary extra configuration fields provided during initialization. It asserts the value of the `extra` attribute matches the input string `"extra"`.*


### test_serialization (method, L80-L89, parent: TestLLMConfigEntry)

> *Summary: This test verifies that an `OpenAILLMConfigEntry` object correctly serializes into a dictionary structure. It asserts that the dumped output matches a predefined configuration containing specific OpenAI parameters like model name and API key placeholder.*


### test_deserialization (method, L91-L93, parent: TestLLMConfigEntry)

> *Summary: This test verifies that an `OpenAILLMConfigEntry` object can be correctly reconstructed from its serialized dictionary representation. It asserts that the newly instantiated object matches the original input object after deserialization.*


### test_get (method, L95-L100, parent: TestLLMConfigEntry)

> *Summary: This test verifies that an `OpenAILLMConfigEntry` object correctly returns specific expected values for predefined keys like `"api_type"` and `"model"`. It also confirms the behavior of `.get()` when accessing non-existent keys, ensuring it returns `None` or a specified default value.*


### test_get_item_and_set_item (method, L102-L117, parent: TestLLMConfigEntry)

> *Summary: This test verifies that the configuration object supports dictionary-like access, ensuring it correctly retrieves predefined attributes and raises a `KeyError` for missing keys. It also confirms that arbitrary key/value pairs can be set and subsequently retrieved or reset to `None`.*


### TestLLMConfig (class, L120-L915)

> *Summary: This test suite validates the `LLMConfig` class by extensively testing its initialization from various inputs (dictionaries, configuration entries), attribute accessors (`get`, `getattr`, `setattr`), serialization/deserialization, and filtering capabilities. It ensures correct handling of different LLM provider configurations across multiple providers like OpenAI, Anthropic, and Groq.*


### openai_llm_config (method, L122-L128, parent: TestLLMConfig)

> *Summary: This method constructs a `LLMConfig` object by wrapping an input `OpenAILLMConfigEntry`. It standardizes the configuration with fixed values for temperature (0.5), checking interval (1000ms), and cache seed (42).*


### test_init_with_extras (method, L130-L154, parent: TestLLMConfig)

> *Summary: Verifies that an `LLMConfig` object can be initialized correctly when provided with both a dictionary of configuration extras and keyword arguments. It asserts the resulting instance matches the expected structure containing all passed parameters.*


### test_init_with_entities (method, L411-L412, parent: TestLLMConfig)

> *Summary: This test verifies that initializing an `LLMConfig` object using a dictionary input correctly matches a predefined expected configuration instance. It asserts equality between the newly created object and the target structure.*


### test_ensure_config (method, L484-L485, parent: TestLLMConfig)

> *Summary: This test verifies that the `LLMConfig.ensure_config` method correctly transforms an arbitrary configuration input into a standardized `LLMConfig` object matching the provided expectation. It asserts equality between the result of the transformation and the predefined target configuration.*


### test_serialization (method, L487-L504, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` object correctly serializes its state into a dictionary format. It asserts that the resulting dictionary matches a predefined structure containing configuration details like model name, API key, and temperature settings.*


### test_get (method, L506-L511, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` object correctly retrieves specific configuration values like temperature, check interval, and cache seed using the `.get()` method. It also confirms proper handling for missing keys, returning `None` or a specified default value.*


### test_getattr (method, L513-L520, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` instance correctly exposes its predefined attributes (like `temperature`, `check_every_ms`, and `cache_seed`) while also ensuring that attempting to access a non-existent attribute raises the expected `AttributeError`.*


### test_setattr (method, L522-L525, parent: TestLLMConfig)

> *Summary: This test verifies that the `temperature` attribute of an `LLMConfig` object can be successfully modified and updated to a new value. It asserts the initial state, changes the value, and then confirms the change took effect.*


### test_get_item_and_set_item (method, L527-L542, parent: TestLLMConfig)

> *Summary: This test verifies that the configuration object supports dictionary-like access, allowing retrieval of predefined settings like "temperature" and raising a `KeyError` for unknown keys. It also confirms that arbitrary attributes can be set and subsequently retrieved or reset to `None`.*


### test_items (method, L544-L562, parent: TestLLMConfig)

> *Summary: Verifies that the `items()` method of an `LLMConfig` object returns a dictionary-like view containing specific configuration details. It asserts that this returned structure matches a predefined set of expected values for API type, model, temperature, and other settings.*


### test_keys (method, L564-L568, parent: TestLLMConfig)

> *Summary: Verifies that the `LLMConfig` object exposes a dictionary-like view of its configuration keys. It asserts that the returned keys match a predefined set: `"temperature"`, `"check_every_ms"`, `"cache_seed"`, and `"config_list"`.*


### test_values (method, L570-L589, parent: TestLLMConfig)

> *Summary: Verifies that the `values()` method of an `LLMConfig` object returns a dictionary view containing specific configuration data for OpenAI models. It asserts that the returned values match a predefined structure including model details and parameters like temperature.*


### test_unpack (method, L591-L621, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` object correctly serializes its contents into a dictionary structure. It takes an `OpenAILLMConfigEntry` and populates the configuration, then asserts that the resulting dictionary matches a predefined expected structure.*


### test_contains (method, L623-L630, parent: TestLLMConfig)

> *Summary: This test verifies that a provided `LLMConfig` object contains specific expected keys like `"temperature"` and `"cache_seed"`, while also asserting the absence of an unexpected key. It confirms the presence and correct handling of the `"config_list"` attribute within the configuration structure.*


### test_where (method, L662-L667, parent: TestLLMConfig)

> *Summary: This test verifies the filtering logic of an `LLMConfig` instance by applying a provided dictionary of filters and an exclusion flag to generate a resulting configuration object. It asserts that the output matches a predefined expected configuration structure.*


### test_where_invalid_filter (method, L669-L674, parent: TestLLMConfig)

> *Summary: This test verifies that attempting to apply a filtering condition with an invalid API type raises a `ValueError`. It asserts that the error message correctly reflects the attempted filter criteria.*


### test_repr (method, L676-L701, parent: TestLLMConfig)

> *Summary: Verifies the string representation (`__repr__`) of an `LLMConfig` object constructed from an `OpenAILLMConfigEntry`. It tests two scenarios: one where routing is default (omitting `routing_method`) and another where a custom routing method and temperature are explicitly set, ensuring all key configuration fields appear correctly in the output string.*


### test_str (method, L703-L727, parent: TestLLMConfig)

> *Summary: This test verifies the string representation (`__str__`) of an `LLMConfig` object, which is initialized with an `OpenAILLMConfigEntry`. It asserts that the output correctly includes configuration details like API type, model name, and tags, while also validating how routing method and temperature are reflected in the string when explicitly set.*


### test_routing_method_default (method, L729-L731, parent: TestLLMConfig)

> *Summary: Verifies that when initialized with an `OpenAILLMConfigEntry`, the resulting configuration object's routing method defaults to `None`. This test ensures the default state of the routing mechanism for OpenAI configurations.*


### test_routing_method_custom (method, L733-L735, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` object correctly sets its `routing_method` to `"round_robin"` when initialized with a specific configuration entry and the specified routing method. It asserts the resulting internal state matches the input parameter.*


### test_routing_method_invalid (method, L737-L739, parent: TestLLMConfig)

> *Summary: Asserts that instantiating an `LLMConfig` with a provided configuration entry and an invalid routing method raises a `ValidationError`. This tests the validation logic for acceptable routing methods.*


### test_from_json_env (method, L741-L746, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` object can be correctly instantiated from a JSON string provided in the environment variables. It sets a sample configuration, calls the static factory method using the environment key, and asserts the resulting object matches the expected instance.*


### test_from_json_env_not_found (method, L749-L752, parent: TestLLMConfig)

> *Summary: This test verifies that attempting to load configuration from a non-existent environment variable raises a `ValueError`. It asserts the error message specifically indicates the missing environment name.*


### test_from_json_env_with_kwargs (method, L754-L759, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` object can be correctly instantiated from a JSON environment variable while also accepting keyword arguments. It asserts that the resulting instance matches an expected configuration built with both the parsed JSON data and provided overrides.*


### test_from_json_path (method, L761-L774, parent: TestLLMConfig)

> *Summary: This test verifies the `from_json` static method by first creating a temporary JSON configuration file and asserting that it correctly instantiates an `LLMConfig` object matching expected values. It also confirms that attempting to load from a non-existent path raises a `FileNotFoundError`.*


### test_copy (method, L776-L791, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` object can be correctly duplicated using its built-in `.copy()` and `.deepcopy()` methods, as well as Python's standard `copy` and `deepcopy` functions. It asserts that the resulting copies are structurally equal to the original but are distinct objects in memory.*


### test_llm_config_doesnt_patch_entry (method, L793-L801, parent: TestLLMConfig)

> *Summary: Verifies that an `OpenAILLMConfigEntry` object retains its original state when passed into an `LLMConfig`, specifically ensuring the `max_tokens` attribute remains unset (`None`) on the entry itself, even if it's present in the resulting configuration list.*


### test_llm_config_doesnt_patch_entry_dict (method, L803-L811, parent: TestLLMConfig)

> *Summary: Verifies that an input dictionary passed to `LLMConfig` is not mutated when creating the configuration list. It confirms that the original `entry` dictionary remains unchanged after initialization.*


### test_openai_llm_config_entry_with_workspace_dir (method, L813-L823, parent: TestLLMConfig)

> *Summary: This test verifies that an `OpenAIResponsesLLMConfigEntry` correctly stores and exposes a specified `workspace_dir`. It initializes the configuration with a directory path and asserts its presence in both the object attribute and its dictionary representation.*


### test_openai_llm_config_entry_with_allowed_paths (method, L825-L835, parent: TestLLMConfig)

> *Summary: Verifies that an `OpenAIResponsesLLMConfigEntry` correctly stores and serializes a list of allowed file paths, using `"gpt-4o-mini"` as the model identifier. It confirms both direct attribute access and dictionary serialization yield the expected path list.*


### test_openai_llm_config_entry_workspace_dir_and_allowed_paths (method, L837-L851, parent: TestLLMConfig)

> *Summary: Verifies that an `OpenAIResponsesLLMConfigEntry` correctly stores and serializes its `workspace_dir` and `allowed_paths` attributes when initialized with specific values. It confirms these properties are present in the dictionary returned by `model_dump()`.*


### test_openai_llm_config_entry_defaults_workspace_dir_and_allowed_paths (method, L853-L865, parent: TestLLMConfig)

> *Summary: Verifies that an `OpenAIResponsesLLMConfigEntry` instance defaults its `workspace_dir` and `allowed_paths` to `None`. It further asserts that these `None` attributes are correctly omitted when serializing the entry using `model_dump(exclude_none=True)`.*


### test_llm_config_with_entry_workspace_dir_and_allowed_paths (method, L867-L883, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` correctly stores workspace directory and allowed paths within its contained configuration entry. It asserts that these specific path attributes reside only on the entry object, not directly on the main configuration instance.*


### test_llm_config_copy_preserves_entry_workspace_dir (method, L885-L897, parent: TestLLMConfig)

> *Summary: This test verifies that the `copy()` method of an LLM configuration preserves the `workspace_dir` attribute within its entries. It initializes a configuration with a specific workspace directory and asserts that this value remains unchanged after copying.*


### test_llm_config_dict_with_workspace_dir_and_allowed_paths (method, L899-L915, parent: TestLLMConfig)

> *Summary: This test verifies that an `LLMConfig` object correctly ingests and stores `workspace_dir` and `allowed_paths` when initialized from a dictionary. It asserts these values are present in the internal configuration list while confirming they are not exposed directly on the main config object.*

