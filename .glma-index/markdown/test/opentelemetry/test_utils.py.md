# test/opentelemetry/test_utils.py

10 class(es): TestMessageToOtel, TestMessagesToOtel, TestReplyToOtelMessage, TestAggregateUsage, TestApiTypeToProvider, TestGetProviderName, TestGetModelName, TestGetProviderFromConfigList, TestGetModelFromConfigList, TestSetLlmRequestParams. 64 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestMessageToOtel | class |  |
| TestMessagesToOtel | class |  |
| TestReplyToOtelMessage | class |  |
| TestAggregateUsage | class |  |
| TestApiTypeToProvider | class |  |
| TestGetProviderName | class |  |
| TestGetModelName | class |  |
| TestGetProviderFromConfigList | class |  |
| TestGetModelFromConfigList | class |  |
| TestSetLlmRequestParams | class |  |

## Chunks

### TestMessageToOtel (class, L27-L206)

> *Summary: This test suite verifies the `message_to_otel` conversion function by providing various input message structures (e.g., text, system, tool calls, multimodal content). It asserts that the output correctly maps these inputs to the expected OpenTelemetry format, handling edge cases like missing data or invalid JSON arguments.*


### test_simple_text_message (method, L30-L36, parent: TestMessageToOtel)

> *Summary: This test verifies the `message_to_otel` conversion by taking a simple user message dictionary as input and asserting that it correctly transforms into an OpenTelemetry-like structure containing text parts. The expected output mirrors the input content within a structured list of parts.*


### test_assistant_text_message (method, L38-L43, parent: TestMessageToOtel)

> *Summary: This test verifies the `message_to_otel` conversion by taking a dictionary representing an assistant's text message as input. It asserts that the resulting OpenTelemetry structure correctly retains the role and formats the content into a single text part.*


### test_system_message (method, L45-L49, parent: TestMessageToOtel)

> *Summary: This test verifies the `message_to_otel` conversion by taking a system role message dictionary as input. It asserts that the resulting OpenTelemetry structure correctly retains the "system" role and formats the content into a text part within an array.*


### test_message_with_name (method, L51-L55, parent: TestMessageToOtel)

> *Summary: This test verifies the `message_to_otel` conversion by passing a dictionary containing role, content, and name. It asserts that the resulting OpenTelemetry structure correctly retains the user role and extracts the text content into a parts list.*


### test_tool_calls_message (method, L57-L77, parent: TestMessageToOtel)

> *Summary: This test verifies the serialization of a message containing tool calls into an OpenTelemetry format. It takes a dictionary representing an assistant's response with a specific function call and asserts that the resulting structure correctly maps the role, type, ID, name, and parsed arguments.*


### test_tool_calls_with_dict_arguments (method, L79-L95, parent: TestMessageToOtel)

> *Summary: This test verifies that when an input message contains tool calls with dictionary arguments, the `message_to_otel` conversion preserves the argument structure. It asserts that the resulting OpenTelemetry representation retains the original dictionary for the function's arguments.*


### test_tool_calls_with_invalid_json_arguments (method, L97-L113, parent: TestMessageToOtel)

> *Summary: When processing a message containing tool calls with non-JSON arguments, the function converts it to OpenTelemetry format. It asserts that if the argument string is invalid JSON, it remains unmodified in the resulting structure.*


### test_multiple_tool_calls (method, L115-L132, parent: TestMessageToOtel)

> *Summary: This test verifies that a message containing multiple tool calls is correctly transformed by `message_to_otel`. It asserts the resulting structure contains two parts, corresponding to the functions named "fn\_a" and "fn\_b".*


### test_tool_response_message (method, L134-L146, parent: TestMessageToOtel)

> *Summary: This test verifies the `message_to_otel` conversion by taking a dictionary representing a tool response message as input. It asserts that the resulting OpenTelemetry structure correctly contains the role, the specific tool call ID, and the content within its parts.*


### test_multimodal_content_list (method, L148-L160, parent: TestMessageToOtel)

> *Summary: This test verifies that a multimodal message structure, containing both text and an image URL, is correctly transformed by `message_to_otel`. It asserts the resulting structure maintains the user role and accurately separates the input into distinct parts for text and image content.*


### test_empty_content (method, L162-L166, parent: TestMessageToOtel)

> *Summary: This test verifies that an input message with empty content correctly transforms into an OpenTelemetry structure. It asserts the resulting object retains the correct role and has an empty parts list.*


### test_none_content (method, L168-L171, parent: TestMessageToOtel)

> *Summary: When provided a message dictionary where the content is `None`, this test asserts that the conversion function returns an empty list for its `"parts"` field. This verifies correct handling of null content during OpenTelemetry serialization.*


### test_missing_content_no_tool_calls (method, L173-L176, parent: TestMessageToOtel)

> *Summary: When provided a message structure containing only an assistant role, this test asserts that the conversion function returns an empty list for its `parts`. This verifies correct handling when no content is present in the input.*


### test_empty_tool_calls_list (method, L178-L182, parent: TestMessageToOtel)

> *Summary: When provided a message with an empty `tool_calls` list in the assistant's role, this test asserts that the resulting OpenTelemetry representation contains no parts. This confirms correct handling when no tool calls are present.*


### test_default_role_is_user (method, L184-L187, parent: TestMessageToOtel)

> *Summary: When provided a message dictionary lacking a specified role, this test asserts that the conversion function defaults the resulting object's role to `"user"`.*


### test_tool_call_missing_function (method, L189-L197, parent: TestMessageToOtel)

> *Summary: This test verifies the serialization of a tool call when no specific function is provided. It takes a message containing an assistant's tool call and asserts that the resulting OpenTelemetry representation has empty strings for the name and arguments.*


### test_tool_response_missing_content (method, L199-L206, parent: TestMessageToOtel)

> *Summary: This test verifies that when a tool response is provided without content, the resulting OpenTelemetry structure correctly reflects an empty response. It takes a minimal dictionary representing a tool message and asserts the corresponding `response` field in the output is an empty string.*


### TestMessagesToOtel (class, L212-L249)

> *Summary: This test suite verifies the `messages_to_otel` function's ability to correctly convert various lists of message dictionaries into OpenTelemetry format. It checks scenarios including empty, single, multiple, and mixed-type messages containing text, tool calls, and tool responses.*


### test_empty_list (method, L215-L216, parent: TestMessagesToOtel)

> *Summary: Verifies that when an empty list is provided as input, the function returns an empty list. This confirms correct handling of zero-length data inputs.*


### test_single_message (method, L218-L222, parent: TestMessagesToOtel)

> *Summary: This test verifies that the `messages_to_otel` function correctly transforms a list containing a single user message into an OpenTelemetry structure. It asserts that the output contains exactly one element matching the original user role.*


### test_multiple_messages (method, L224-L234, parent: TestMessagesToOtel)

> *Summary: This test verifies that the `messages_to_otel` function correctly transforms a list of conversational message dictionaries into an equivalent structure. It asserts that the output maintains the correct sequence and roles from the input messages.*


### test_mixed_message_types (method, L236-L249, parent: TestMessagesToOtel)

> *Summary: This test verifies that a list containing mixed message types (user text, assistant tool call, and tool response) is correctly transformed by `messages_to_otel`. It asserts the resulting structure contains three elements with the correct corresponding part types.*


### TestReplyToOtelMessage (class, L255-L294)

> *Summary: This suite of tests verifies the `reply_to_otel_message` function's ability to convert various input types (strings, dictionaries with content or tool calls, and `None`) into a standardized list of OpenTelemetry message structures. It asserts correct formatting for different scenarios, including text responses, tool call inclusions, and handling null inputs by returning an empty list.*


### test_string_reply (method, L258-L264, parent: TestReplyToOtelMessage)

> *Summary: This test verifies the expected structure of a string reply generated by an OpenTelemetry message handler. It asserts that the returned list contains one assistant response with specific content, role, and finish reason fields.*


### test_empty_string_reply (method, L266-L271, parent: TestReplyToOtelMessage)

> *Summary: This test verifies the response when an empty string is provided as input to `reply_to_otel_message`. It asserts that the returned list contains one message object with empty text content and a "stop" finish reason.*


### test_dict_reply_with_content (method, L273-L278, parent: TestReplyToOtelMessage)

> *Summary: This test verifies that sending a dictionary containing content results in a structured reply. It asserts the returned list contains one message object with the role set to "assistant" and the specified text content within its parts.*


### test_dict_reply_with_tool_calls (method, L280-L290, parent: TestReplyToOtelMessage)

> *Summary: This test verifies that a dictionary containing tool calls is correctly transformed into an OpenTelemetry message structure. It asserts the resulting list contains one assistant role message with a specific `tool_call` part type.*


### test_none_reply (method, L292-L294, parent: TestReplyToOtelMessage)

> *Summary: This test verifies that when `None` is passed to the message replying function, it correctly returns an empty list. It asserts this expected behavior for handling null input.*


### TestAggregateUsage (class, L300-L350)

> *Summary: These tests verify the `aggregate_usage` function's behavior when processing token usage data from various inputs. It checks aggregation across single and multiple models, handles empty or malformed input dictionaries by returning appropriate results (e.g., `None` for empty input, zeroed tokens for missing keys).*


### test_single_model (method, L303-L312, parent: TestAggregateUsage)

> *Summary: This test verifies the `aggregate_usage` function by providing a dictionary containing token usage for a single model ("gpt-4"). It asserts that the returned result correctly identifies the model and its corresponding input (100) and output (50) token counts.*


### test_multiple_models (method, L314-L325, parent: TestAggregateUsage)

> *Summary: This test verifies the `aggregate_usage` function by providing a dictionary of token usage for multiple models (GPT-4 and GPT-3.5-Turbo). It asserts that the returned aggregated result correctly combines the input tokens (300) and output tokens (150) from all specified models.*


### test_empty_dict (method, L327-L329, parent: TestAggregateUsage)

> *Summary: When provided with an empty dictionary, the function returns `None`. This tests the expected behavior for zero input data.*


### test_missing_token_keys (method, L331-L340, parent: TestAggregateUsage)

> *Summary: When provided with usage data missing token counts for a specific model, the function returns the model identifier along with zero values for both input and output tokens. This test verifies that `aggregate_usage` handles incomplete usage records gracefully by defaulting token counts to zero.*


### test_partial_token_data (method, L342-L350, parent: TestAggregateUsage)

> *Summary: This test verifies the `aggregate_usage` function by providing a usage dictionary containing only prompt tokens for one model. It asserts that the returned aggregated data correctly reflects an input token count of 50 and zero output tokens.*


### TestApiTypeToProvider (class, L356-L373)

> *Summary: Verifies the predefined mapping between abstract API types and their concrete provider implementations. It asserts that specific known providers map to expected strings and confirms that an unknown provider is absent from the mapping dictionary.*


### test_known_providers (method, L359-L370, parent: TestApiTypeToProvider)

> *Summary: Verifies that a mapping dictionary correctly associates common AI provider names (like "openai" or "anthropic") with their corresponding internal provider identifiers. This test ensures the configuration lookup for known services is accurate across various providers.*


### test_unknown_provider_not_in_dict (method, L372-L373, parent: TestApiTypeToProvider)

> *Summary: Asserts that a specific key, `"unknown_provider"`, is absent from the `API_TYPE_TO_PROVIDER` dictionary. This test verifies the expected structure of the provider mapping configuration.*


### TestGetProviderName (class, L379-L439)

> *Summary: These tests verify the `get_provider_name` function's behavior when extracting a provider name from an agent object based on its LLM configuration. It checks various edge cases, including missing or invalid configurations, and confirms correct extraction for specific API types like "openai" and "azure".*


### test_agent_without_llm_config (method, L382-L384, parent: TestGetProviderName)

> *Summary: When provided with a mock agent lacking an `llm_config` attribute, the function asserts that the provider name returned by `get_provider_name` is `None`. This tests the system's behavior when no language model configuration is present.*


### test_agent_with_false_llm_config (method, L386-L389, parent: TestGetProviderName)

> *Summary: When an agent's `llm_config` is set to `False`, the function asserts that no provider name can be retrieved for it. This tests the behavior of identifying LLM providers when configuration is explicitly disabled.*


### test_agent_with_none_llm_config (method, L391-L394, parent: TestGetProviderName)

> *Summary: This test verifies that when an agent's `llm_config` is explicitly set to `None`, the provider name retrieval function correctly returns `None`. It mocks an agent object and asserts the expected behavior based on this configuration.*


### test_agent_with_empty_config_list (method, L396-L399, parent: TestGetProviderName)

> *Summary: When the agent's `llm_config` has an empty or null configuration list, this test asserts that no provider name can be determined. It verifies that the function returns `None` under these specific input conditions.*


### test_agent_with_openai_api_type (method, L401-L406, parent: TestGetProviderName)

> *Summary: This test verifies that a provider name is correctly identified as "openai" when an agent's LLM configuration specifies the API type as "openai". It mocks the necessary agent and configuration objects to assert this behavior.*


### test_agent_with_azure_api_type (method, L408-L413, parent: TestGetProviderName)

> *Summary: Given a mocked agent configured with an API type of "azure," this test asserts that the provider name returned by `get_provider_name` is correctly identified as `"azure.ai.openai"`.*


### test_agent_with_unknown_api_type (method, L415-L420, parent: TestGetProviderName)

> *Summary: This test verifies that the `get_provider_name` function correctly identifies a provider when its configuration specifies an unknown API type, such as `"custom_provider"`. It mocks an agent's configuration to simulate this scenario and asserts the returned name matches the configured value.*


### test_agent_with_no_api_type_on_object (method, L422-L429, parent: TestGetProviderName)

> *Summary: When an object's configuration lacks an `api_type`, the function returns `None` for the provider name. This test verifies that `get_provider_name` correctly handles a mock configuration entry where `api_type` is explicitly set to `None`.*


### test_agent_with_dict_config_entry (method, L431-L439, parent: TestGetProviderName)

> *Summary: This test verifies that a provider name can be correctly retrieved when the configuration entry lacks an `api_type` attribute, relying instead on a `.get()` method call. It passes a mock agent configured with such an entry and asserts the returned provider name is "anthropic".*


### TestGetModelName (class, L442-L464)

> *Summary: This suite verifies the `get_model_name` utility by testing various agent configurations. It asserts that the function returns `None` when LLM configuration is missing, false, or the config list is empty, but correctly extracts the model name string when a valid configuration entry exists.*


### test_agent_without_llm_config (method, L445-L447, parent: TestGetModelName)

> *Summary: This test verifies that when an agent object lacks LLM configuration, the `get_model_name` function correctly returns `None`. It achieves this by mocking an agent and asserting the expected null return value.*


### test_agent_with_false_llm_config (method, L449-L452, parent: TestGetModelName)

> *Summary: When an agent's `llm_config` is set to `False`, the function asserts that retrieving a model name from it returns `None`. This tests the behavior of the system when LLM configuration is explicitly disabled.*


### test_agent_with_model (method, L454-L459, parent: TestGetModelName)

> *Summary: This test verifies that a function correctly extracts the model name from an agent's configuration. It mocks an agent with a specific LLM configuration entry and asserts the returned value matches the expected model identifier ("gpt-4").*


### test_agent_with_empty_config_list (method, L461-L464, parent: TestGetModelName)

> *Summary: When the agent's `llm_config` has an empty or null configuration list, this test asserts that the model name retrieval function returns `None`. It mocks the agent to simulate this specific configuration state.*


### TestGetProviderFromConfigList (class, L470-L502)

> *Summary: This test suite verifies the `get_provider_from_config_list` function's behavior when processing a list of configuration objects or dictionaries. It asserts that the function correctly extracts the provider name based on the presence and value of an `api_type`, defaulting to "openai" if no specific type is found, and always using the first valid entry in the list.*


### test_empty_config_list (method, L473-L474, parent: TestGetProviderFromConfigList)

> *Summary: When provided with an empty list of configurations, this test asserts that the function defaults to returning `"openai"` as the provider.*


### test_dict_config_with_api_type (method, L476-L478, parent: TestGetProviderFromConfigList)

> *Summary: This test verifies that a provider name can be correctly extracted from a list of configuration dictionaries. It passes a list containing one dictionary specifying the `"api_type"` and asserts the returned value matches the expected provider string.*


### test_dict_config_without_api_type (method, L480-L482, parent: TestGetProviderFromConfigList)

> *Summary: Given a list of configuration dictionaries, this test asserts that the provider is correctly identified as "openai" when the input dictionary lacks an explicit `api_type`.*


### test_dict_config_unknown_api_type (method, L484-L486, parent: TestGetProviderFromConfigList)

> *Summary: This test verifies that a provider can be correctly retrieved from a configuration list when the API type is an unknown custom value. It passes a list containing one dictionary with `"api_type": "my_custom"` and asserts the function returns `"my_custom"`.*


### test_object_config_with_api_type (method, L488-L491, parent: TestGetProviderFromConfigList)

> *Summary: When provided a mock configuration object with `api_type` set to `"bedrock"`, this test asserts that the function correctly returns the string `"aws.bedrock"` when processing a list containing only that configuration.*


### test_object_config_without_api_type (method, L493-L495, parent: TestGetProviderFromConfigList)

> *Summary: When provided a mock configuration object lacking an `api_type`, this test asserts that the provider detection function correctly defaults to returning `"openai"`.*


### test_uses_first_config_entry (method, L497-L502, parent: TestGetProviderFromConfigList)

> *Summary: This test verifies that a function correctly selects the provider type from a list of configurations by prioritizing the first entry. Given a list containing dictionaries specifying API types, it asserts that the returned value matches the `api_type` of the initial dictionary in the list.*


### TestGetModelFromConfigList (class, L505-L526)

> *Summary: This suite of tests verifies the `get_model_from_config_list` function's ability to extract a model name from a list of configuration dictionaries or mock objects. It asserts correct behavior for empty lists, configurations containing models, and configurations lacking model information.*


### test_empty_config_list (method, L508-L509, parent: TestGetModelFromConfigList)

> *Summary: Asserts that when an empty list of configurations is provided, the function returns `None`. This verifies correct handling for zero input configurations.*


### test_dict_config_with_model (method, L511-L513, parent: TestGetModelFromConfigList)

> *Summary: This test verifies that a function correctly extracts the model name from a list of configuration dictionaries. It passes a list containing one dictionary specifying `"gpt-4o"` and asserts the returned value is `"gpt-4o"`.*


### test_dict_config_without_model (method, L515-L517, parent: TestGetModelFromConfigList)

> *Summary: Asserts that when provided a configuration list containing only API keys, the function correctly returns `None` because no model definition is present. This tests the behavior of extracting a model from a config structure lacking model information.*


### test_object_config_with_model (method, L519-L522, parent: TestGetModelFromConfigList)

> *Summary: This test verifies that a function correctly extracts the model name from a list of configuration objects, specifically when one object has its `model` attribute set to `"claude-3-opus"`. It asserts the returned value matches the expected string.*


### test_object_config_without_model (method, L524-L526, parent: TestGetModelFromConfigList)

> *Summary: Asserts that when provided a list containing a mock configuration object, the function correctly returns `None` because no model can be derived from it. This tests the behavior of extracting a model from a configuration list lacking specific model information.*


### TestSetLlmRequestParams (class, L532-L581)

> *Summary: This class contains unit tests verifying the `set_llm_request_params` function's behavior when updating OpenTelemetry spans. It asserts that specific LLM request parameters are correctly added as span attributes based on the input configuration dictionary, handling cases with all, partial, or no provided parameters.*


### test_all_params_present (method, L535-L550, parent: TestSetLlmRequestParams)

> *Summary: This test verifies that a function correctly sets all expected generation parameters onto an OpenTelemetry span. It passes a mock span and a dictionary containing various LLM configuration values, asserting that `span.set_attribute` was called exactly five times with the correct parameter names and corresponding values.*


### test_no_params_present (method, L552-L556, parent: TestSetLlmRequestParams)

> *Summary: This test verifies that no attributes are set on an OpenTelemetry span when the input configuration dictionary contains no message parameters. It mocks a span and calls `set_llm_request_params` with a minimal config, asserting that `span.set_attribute` is never invoked.*


### test_partial_params (method, L558-L562, parent: TestSetLlmRequestParams)

> *Summary: This test verifies that when partial configuration parameters are provided to the LLM request setter, the `set_attribute` method on the span is called correctly with the specific parameter and its value. It ensures the attribute name matches the expected format for temperature settings.*


### test_none_value_skipped (method, L564-L568, parent: TestSetLlmRequestParams)

> *Summary: When provided a configuration dictionary containing `None` for the "temperature" key and a valid value for "max\_tokens," this test verifies that only non-null parameters are passed to the span's attribute setting method. Specifically, it asserts that the maximum tokens were correctly recorded while ignoring the null temperature value.*


### test_zero_value_included (method, L570-L576, parent: TestSetLlmRequestParams)

> *Summary: This test verifies that zero-value parameters are correctly recorded on an OpenTelemetry span. It asserts that `set_attribute` is called exactly twice with the correct keys and their corresponding zero values from the input configuration dictionary.*


### test_empty_config (method, L578-L581, parent: TestSetLlmRequestParams)

> *Summary: When called with an empty dictionary as input parameters for a span mock, this test verifies that no attributes are set on the span object. It confirms the function correctly handles zero configuration data without invoking `set_attribute`.*

