# test/oai/test_responses_client.py

106 function(s): mocked_openai_client, test_messages_are_transformed_into_input, test_structured_output_path_uses_parse, test_usage_dict_parses_pydantic_like_object, test_message_retrieval_handles_various_item_types, test_message_retrieval_strips_extra_fields, test_get_delta_messages_filters_completed_blocks, test_create_converts_multimodal_blocks, test_calculate_openai_image_cost_gpt_image_1, test_calculate_openai_image_cost_dalle_3 and 96 more. 3 class(es): ImageGenerationCall, _FakeUsage, _FakeResponse. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ImageGenerationCall | class |  |
| _FakeUsage | class |  |
| _FakeResponse | class |  |
| mocked_openai_client | function |  |
| test_messages_are_transformed_into_input | function |  |
| test_structured_output_path_uses_parse | function |  |
| test_usage_dict_parses_pydantic_like_object | function |  |
| test_message_retrieval_handles_various_item_types | function |  |
| test_message_retrieval_strips_extra_fields | function |  |
| test_get_delta_messages_filters_completed_blocks | function |  |
| test_create_converts_multimodal_blocks | function |  |
| test_calculate_openai_image_cost_gpt_image_1 | function |  |
| test_calculate_openai_image_cost_dalle_3 | function |  |
| test_calculate_openai_image_cost_dalle_2 | function |  |
| test_calculate_openai_image_cost_case_insensitive | function |  |
| test_calculate_openai_image_cost_invalid_model | function |  |
| test_calculate_openai_image_cost_invalid_size | function |  |
| test_calculate_openai_image_cost_invalid_quality | function |  |
| test_add_image_cost_single_image | function |  |
| test_add_image_cost_multiple_images | function |  |
| test_add_image_cost_no_images | function |  |
| test_add_image_cost_missing_model_extra | function |  |
| test_add_image_cost_defaults | function |  |
| test_total_cost_includes_image_costs | function |  |
| test_image_costs_persist_across_calls | function |  |
| test_add_image_cost_bug_demonstration | function |  |
| test_add_image_cost_partial_defaults | function |  |
| test_add_image_cost_with_non_image_first | function |  |
| test_parse_params_with_verbosity_high | function |  |
| test_parse_params_with_verbosity_low | function |  |
| test_parse_params_with_verbosity_medium | function |  |
| test_parse_params_with_reasoning_effort_low | function |  |
| test_parse_params_with_reasoning_effort_medium | function |  |
| test_parse_params_with_reasoning_effort_high | function |  |
| test_parse_params_with_reasoning_effort_xhigh | function |  |
| test_parse_params_with_both_verbosity_and_reasoning_effort | function |  |
| test_create_passes_reasoning_effort_to_api | function |  |
| test_message_retrieval_with_real_response_structure | function |  |
| _create_apply_patch_call_mock | function |  |
| _create_message_mock | function |  |
| _create_reasoning_mock | function |  |
| test_apply_patch_tool_added_to_built_in_tools | function |  |
| test_apply_patch_with_other_built_in_tools | function |  |
| test_message_retrieval_handles_apply_patch_call | function |  |
| test_message_retrieval_handles_multiple_apply_patch_calls | function |  |
| test_message_retrieval_mixed_content_with_apply_patch | function |  |
| test_apply_patch_call_preserves_status | function |  |
| test_apply_patch_no_diff_for_delete | function |  |
| test_create_with_no_built_in_tools_excludes_apply_patch | function |  |
| test_message_retrieval_with_realistic_apply_patch_response | function |  |
| test_apply_patch_with_reasoning_is_filtered | function |  |
| test_apply_patch_operation_with_agent_tool | function |  |
| test_apply_patch_operation_without_agent_creates_default_editor | function |  |
| test_apply_patch_operation_with_async_patches | function |  |
| test_apply_patch_operation_unknown_operation_type | function |  |
| test_apply_patch_operation_handles_exceptions | function |  |
| test_apply_patch_operation_all_operation_types | function |  |
| test_apply_patch_operation_with_allowed_paths | function |  |
| test_extract_apply_patch_calls_from_content | function |  |
| test_extract_apply_patch_calls_from_tool_calls | function |  |
| test_extract_apply_patch_calls_from_both_content_and_tool_calls | function |  |
| test_extract_apply_patch_calls_ignores_non_assistant_messages | function |  |
| test_extract_apply_patch_calls_skips_items_without_call_id | function |  |
| test_execute_apply_patch_calls_with_apply_patch_tool | function |  |
| test_execute_apply_patch_calls_with_apply_patch_async_tool | function |  |
| test_execute_apply_patch_calls_returns_empty_when_not_in_built_in_tools | function |  |
| test_execute_apply_patch_calls_returns_empty_for_empty_dict | function |  |
| test_execute_apply_patch_calls_handles_multiple_calls | function |  |
| test_execute_apply_patch_calls_skips_calls_without_operation | function |  |
| test_convert_messages_to_input_basic_text | function |  |
| test_convert_messages_to_input_filters_apply_patch_calls | function |  |
| test_convert_messages_to_input_handles_image_params | function |  |
| test_convert_messages_to_input_handles_multimodal_content | function |  |
| test_convert_messages_to_input_handles_tool_role_messages | function |  |
| test_convert_messages_to_input_filters_tool_responses_for_processed_apply_patch | function |  |
| test_convert_messages_to_input_raises_error_for_invalid_content_type | function |  |
| test_convert_messages_to_input_handles_empty_content_blocks | function |  |
| test_convert_messages_to_input_null_content_assistant_message | function |  |
| test_convert_messages_to_input_empty_string_content_assistant_message | function |  |
| test_message_retrieval_tool_call_only_produces_none_content | function |  |
| test_convert_messages_to_input_preserves_order_in_reverse | function |  |
| test_shell_tool_shell_call_outcome_model_dump | function |  |
| test_shell_tool_shell_command_output_model_dump | function |  |
| test_shell_tool_shell_call_output_model_dump | function |  |
| test_shell_tool_shell_call_output_post_init | function |  |
| test_shell_tool_extract_shell_calls_from_content | function |  |
| test_shell_tool_extract_shell_calls_from_tool_calls | function |  |
| test_shell_tool_extract_shell_calls_from_both_content_and_tool_calls | function |  |
| test_shell_tool_extract_shell_calls_ignores_non_assistant_messages | function |  |
| test_shell_tool_extract_shell_calls_skips_items_without_call_id | function |  |
| test_shell_tool_execute_shell_calls_returns_empty_when_not_in_built_in_tools | function |  |
| test_shell_tool_execute_shell_calls_returns_empty_for_empty_dict | function |  |
| test_shell_tool_execute_shell_calls_with_shell_tool | function |  |
| test_shell_tool_execute_shell_calls_handles_multiple_calls | function |  |
| test_shell_tool_execute_shell_calls_skips_calls_without_action | function |  |
| test_shell_tool_execute_shell_operation_with_no_commands | function |  |
| test_shell_tool_execute_shell_operation_success | function |  |
| test_shell_tool_execute_shell_operation_handles_exceptions | function |  |
| test_shell_tool_execute_shell_operation_initializes_executor | function |  |
| test_shell_tool_execute_shell_operation_updates_existing_executor | function |  |
| test_shell_tool_normalize_messages_for_responses_api_with_shell_calls | function |  |
| test_shell_tool_normalize_messages_for_responses_api_filters_shell_calls | function |  |
| test_shell_tool_normalize_messages_for_responses_api_with_previous_shell_calls | function |  |
| test_shell_tool_create_with_shell_tool_added_to_built_in_tools | function |  |
| test_shell_tool_create_with_shell_calls_executes_commands | function |  |
| test_shell_tool_create_with_shell_and_other_built_in_tools | function |  |
| test_shell_tool_create_with_no_built_in_tools_excludes_shell | function |  |
| test_shell_tool_convert_messages_to_input_filters_shell_calls | function |  |
| test_shell_tool_convert_messages_to_input_filters_tool_responses_for_processed_shell | function |  |

## Chunks

### ImageGenerationCall (class, L33-L34)

> *Summary: Represents a call to an image generation service, serving as a placeholder structure for handling such requests. It currently has no defined behavior or methods.*


### _FakeUsage (class, L41-L48)

> *Summary: This class simulates the usage statistics found within an OpenAI response object. It accepts arbitrary keyword arguments during initialization and returns them as a dictionary via its `model_dump` method.*


### __init__ (method, L44-L45, parent: _FakeUsage)

> *Summary: Initializes an object by storing any provided keyword arguments in the `_fields` attribute for later use.*


### model_dump (method, L47-L48, parent: _FakeUsage)

> *Summary: Returns a dictionary containing all the internal fields of the object instance. This method provides a snapshot of the current state held by the client object.*


### _FakeResponse (class, L51-L59)

> *Summary: This class simulates a minimal API response object, initialized with optional `output` (a list) and `usage` (a dictionary). It predefines fixed values for cost, model name, and ID to mimic a successful service return.*


### __init__ (method, L54-L59, parent: _FakeResponse)

> *Summary: Initializes a response client object, setting default values for output (as an empty list) and usage (as an empty dictionary). It also preconfigures fixed attributes like cost, model name, and ID.*


### mocked_openai_client (function, L68-L79)

> *Summary: Creates and returns a mocked client object configured to simulate the OpenAI API's response interface. By default, its `create` and `parse` methods return a generic fake response object for testing purposes.*


### test_messages_are_transformed_into_input (function, L87-L108)

> *Summary: This test verifies that a list of message dictionaries is correctly transformed into the expected `input` format when calling the client's creation method. It asserts that the original `messages` parameter is absent from the final call arguments and that the converted `input` structure accurately reflects the initial user content.*


### test_structured_output_path_uses_parse (function, L111-L130)

> *Summary: This test verifies that when a structured output schema is provided, the client correctly calls the `.responses.parse` method on the underlying mock instead of `.responses.create`. It further asserts that the necessary `text_format` argument is passed to this parsing call.*


### test_usage_dict_parses_pydantic_like_object (function, L133-L144)

> *Summary: This test verifies that the client correctly parses a mock response object containing structured usage data into a dictionary format. It asserts that specific token counts, cost, and model information are accurately extracted from the input structure.*


### test_message_retrieval_handles_various_item_types (function, L147-L194)

> *Summary: This test verifies that the message retrieval mechanism correctly aggregates diverse response types—including text, function calls, and web search requests—into a unified assistant message structure. It asserts that the resulting message contains both plain text content and structured tool call information.*


### test_message_retrieval_strips_extra_fields (function, L197-L229)

> *Summary: This test verifies that the message retrieval process filters out extraneous metadata from API responses. It ensures that the returned message content only contains expected fields like `type`, `role`, and `text`, while explicitly excluding internal fields such as `phase`, `status`, and `id`.*


### test_get_delta_messages_filters_completed_blocks (function, L237-L257)

> *Summary: This test verifies that a method filtering delta messages correctly discards any messages already marked as "completed." Given a list of mixed-status messages, it asserts that only the final, non-completed message is returned.*


### test_create_converts_multimodal_blocks (function, L260-L294)

> *Summary: This test verifies that the client correctly transforms a multimodal input containing text and an image URL into the expected structured format when calling the OpenAI API. It asserts that the resulting request payload contains the original content blocks and includes the specified built-in tools.*


### test_calculate_openai_image_cost_gpt_image_1 (function, L302-L321)

> *Summary: This test verifies the image generation cost calculation for the `gpt-image-1` model across various combinations of input sizes and quality settings. It iterates through predefined test cases, asserting that the calculated cost matches the expected value and no errors occur.*


### test_calculate_openai_image_cost_dalle_3 (function, L324-L338)

> *Summary: Verifies the correct pricing for DALL-E 3 image generation by iterating through predefined test cases. It calls a cost calculation function with various input dimensions and quality settings to assert the returned cost matches the expected value.*


### test_calculate_openai_image_cost_dalle_2 (function, L341-L352)

> *Summary: This test verifies the correct cost calculation for DALL-E 2 images across various input sizes and qualities. It iterates through predefined test cases, calling a cost calculation function and asserting that the returned cost matches the expected value without errors.*


### test_calculate_openai_image_cost_case_insensitive (function, L355-L365)

> *Summary: Verifies that the image cost calculation function correctly handles variations in casing for model and quality parameters. It asserts expected costs are returned when inputs like `"GPT-IMAGE-1"` or `"Dall-E-3"` are provided with different cases.*


### test_calculate_openai_image_cost_invalid_model (function, L368-L373)

> *Summary: This test verifies that when an unknown model name is provided to the cost calculation function, it correctly returns zero cost and an error message detailing the invalid model along with a list of supported models.*


### test_calculate_openai_image_cost_invalid_size (function, L376-L386)

> *Summary: This test verifies that the image cost calculation function correctly returns zero cost and an appropriate error message when provided with invalid input dimensions for specific OpenAI models like `gpt-image-1` and `dall-e-3`. It asserts the expected error string is present in the returned error object.*


### test_calculate_openai_image_cost_invalid_quality (function, L389-L399)

> *Summary: This test verifies that the image cost calculation function correctly returns zero cost and an appropriate error message when provided with unsupported or invalid quality settings for specific OpenAI models. It asserts this behavior using two distinct examples: one for `gpt-image-1` and another for `dall-e-3`.*


### test_add_image_cost_single_image (function, L402-L418)

> *Summary: This test verifies that a single image generation call correctly updates the total image cost within an `OpenAIResponsesClient`. It simulates receiving a response containing one mocked image generation object and asserts the resulting accumulated cost is $0.063$.*


### test_add_image_cost_multiple_images (function, L421-L439)

> *Summary: This test verifies that the `_add_image_cost` method correctly calculates the total cost when processing a response containing multiple image generation calls with varying sizes and qualities. It inputs a mock response object populated with several mocked image call objects and asserts the resulting accumulated cost matches the expected sum of individual costs.*


### test_add_image_cost_no_images (function, L442-L454)

> *Summary: When processing a response containing no image generations, this test verifies that the internal `image_costs` counter remains zero after calling the cost calculation method. It uses a mocked OpenAI client and a fake response object to simulate the input scenario.*


### test_add_image_cost_missing_model_extra (function, L457-L472)

> *Summary: When provided a response object lacking the `model_extra` attribute, this test verifies that the internal method correctly handles the missing data without raising an exception and ensures no image generation costs are recorded. It asserts that the accumulated cost remains zero after processing the incomplete response.*


### test_add_image_cost_defaults (function, L475-L491)

> *Summary: This test verifies that when an image generation call lacks any extra model data (`model_extra` is empty), the internal method correctly adds zero cost to the client's running total. It simulates a response with an empty `model_extra` dictionary and asserts that the resulting `image_costs` remains at zero.*


### test_total_cost_includes_image_costs (function, L494-L508)

> *Summary: This test verifies that the `cost()` method correctly aggregates the base API usage cost with any separately assigned image costs. It achieves this by setting a predefined image cost on the client and asserting the returned total equals the sum of the response's cost and the image cost.*


### test_image_costs_persist_across_calls (function, L511-L530)

> *Summary: This test verifies that the `OpenAIResponsesClient` correctly accumulates costs from multiple calls to its creation method when generating images. It simulates two sequential image generation requests, asserting that the final internal cost matches the sum of the individual mock response costs.*


### test_add_image_cost_bug_demonstration (function, L533-L552)

> *Summary: This test verifies a bug in cost calculation by simulating an OpenAI response containing two image generation calls with different quality settings. It asserts that the internal method incorrectly processes both items, summing their respective costs instead of only processing the current item as intended.*


### test_add_image_cost_partial_defaults (function, L555-L571)

> *Summary: This test verifies that the cost calculation correctly applies default values when an image generation response only provides partial model extras, specifically using "high" for quality if it's missing. It asserts that the resulting calculated cost matches the expected value based on these defaults.*


### test_add_image_cost_with_non_image_first (function, L574-L593)

> *Summary: This test verifies that the `_add_image_cost` method correctly handles responses where the first content item is not an image generation call. It asserts that zero image costs are recorded when processing a mixed list containing both a message and an image generation call.*


### test_parse_params_with_verbosity_high (function, L601-L629)

> *Summary: This test verifies that the `_parse_params` method correctly transforms a dictionary input by migrating the `"verbosity"` key into a nested `"text"` structure while preserving all other parameters. It asserts that the original verbosity key is removed and the transformed parameter set matches the expected output.*


### test_parse_params_with_verbosity_low (function, L632-L660)

> *Summary: This test verifies that the `_parse_params` method correctly transforms a dictionary of configuration parameters, specifically converting a `"verbosity": "low"` entry into a nested `"text": {"verbosity": "low"}` structure while preserving other input values. It asserts that the original verbosity key is removed and the resulting parameter set matches the expected transformed state.*


### test_parse_params_with_verbosity_medium (function, L663-L691)

> *Summary: This test verifies that the internal parameter parsing method correctly transforms a `verbosity` string input into a nested `"text"` structure while preserving all other provided configuration parameters. It asserts that the original verbosity key is removed and the transformed value is present in the resulting dictionary.*


### test_parse_params_with_reasoning_effort_low (function, L694-L709)

> *Summary: This test verifies that the `_parse_params` method correctly transforms a dictionary input by converting the `"reasoning_effort"` key into a nested `"reasoning"` structure while preserving other parameters. It asserts that the original key is removed and the new structured data is present in the returned dictionary.*


### test_parse_params_with_reasoning_effort_medium (function, L712-L727)

> *Summary: This test verifies that the `_parse_params` method correctly transforms a dictionary input by converting the `"reasoning_effort"` key into a nested `"reasoning"` structure while preserving other parameters. It asserts that the original key is removed and the new structured data matches expectations.*


### test_parse_params_with_reasoning_effort_high (function, L730-L745)

> *Summary: This test verifies that the `_parse_params` method correctly transforms a specific input parameter, `"reasoning_effort": "high"`, into a nested `"reasoning"` structure while preserving other parameters. It asserts that the original key is removed and the new structured data is present in the returned dictionary.*


### test_parse_params_with_reasoning_effort_xhigh (function, L748-L763)

> *Summary: This test verifies that the `_parse_params` method correctly transforms a specific input parameter, `"reasoning_effort": "xhigh"`, into a structured `"reasoning"` object within the parameters dictionary. It asserts that the original key is removed and the new structure accurately reflects the input value while preserving other parameters.*


### test_parse_params_with_both_verbosity_and_reasoning_effort (function, L766-L785)

> *Summary: This test verifies that the `_parse_params` method correctly transforms input parameters, specifically mapping `"verbosity"` and `"reasoning_effort"` into nested structures within a resulting dictionary while preserving other arbitrary inputs. It asserts that the original keys are removed from the input structure after transformation.*


### test_create_passes_reasoning_effort_to_api (function, L788-L802)

> *Summary: This test verifies that the `OpenAIResponsesClient` correctly transforms a user-provided `"reasoning_effort"` field into a nested `"reasoning": {"effort": ...}` structure when calling the underlying API client. It asserts that the original key is removed and the new, transformed structure is present in the API call arguments.*


### test_message_retrieval_with_real_response_structure (function, L805-L873)

> *Summary: This test verifies the `message_retrieval` method by feeding it a mock response containing both reasoning and message objects with multiple content blocks. It asserts that only the relevant message is extracted, its content blocks are correctly concatenated into a single string, and specific structural properties match expectations.*


### _create_apply_patch_call_mock (function, L876-L896)

> *Summary: Generates a mock object simulating an `apply_patch_call` response. It constructs the mock based on provided identifiers, operation type, path, optional difference data, and final status.*


### _create_message_mock (function, L899-L912)

> *Summary: This factory generates a mock message object structured to resemble an assistant's response. It accepts the message content as input and returns an instance of a class that simulates the necessary serialization methods for testing purposes.*


### _create_reasoning_mock (function, L915-L929)

> *Summary: This factory produces a mock object simulating reasoning output. It returns an instance of `MockReasoning` whose `model_dump` method provides a predefined dictionary structure for testing purposes.*


### test_apply_patch_tool_added_to_built_in_tools (function, L937-L950)

> *Summary: This test verifies that when an `OpenAIResponsesClient` is initialized and called with `"apply_patch"` in the `built_in_tools`, the underlying mocked OpenAI client receives a request containing the `apply_patch` tool definition. It asserts that the list of tool types passed to the API call includes "apply\_patch".*


### test_apply_patch_with_other_built_in_tools (function, L953-L966)

> *Summary: This test verifies that the `create` method correctly includes multiple specified built-in tools—specifically `web_search`, `apply_patch`, and `image_generation`—when called with a list of them. It asserts that all requested tool types are present in the arguments passed to the underlying mocked OpenAI client.*


### test_message_retrieval_handles_apply_patch_call (function, L969-L1002)

> *Summary: This test verifies that the message retrieval logic correctly processes a response containing an `apply_patch_call`. It simulates receiving a specific patch call and asserts that the resulting message contains this call, confirming its status, operation type, path, and diff content.*


### test_message_retrieval_handles_multiple_apply_patch_calls (function, L1005-L1038)

> *Summary: When provided with a response containing multiple `apply_patch` calls, this test verifies that the message retrieval process correctly parses and structures each operation—including updates, creations, and deletions—into a list of structured messages. It asserts that all expected operations are present and accurately represented in the output content.*


### test_message_retrieval_mixed_content_with_apply_patch (function, L1041-L1064)

> *Summary: This test verifies that the message retrieval function correctly processes a response containing both plain text and an `apply_patch_call`. It asserts that the returned list of messages contains exactly one entry with two distinct content parts: one for the text and one detailing the file patch operation.*


### test_apply_patch_call_preserves_status (function, L1067-L1082)

> *Summary: This test verifies that the `apply_patch_call`'s status is correctly maintained across different states ("in\_progress", "completed", "failed"). It simulates receiving a response containing a patched call and asserts that the retrieved patch object retains its original status.*


### test_apply_patch_no_diff_for_delete (function, L1085-L1100)

> *Summary: Verifies that when applying a delete operation, the resulting patch structure correctly omits the `diff` field. It simulates receiving a response for a file deletion and asserts the patch content reflects this absence of diff information.*


### test_create_with_no_built_in_tools_excludes_apply_patch (function, L1103-L1116)

> *Summary: This test verifies that the `OpenAIResponsesClient` does not include the `apply_patch` tool when creating a response if no built-in tools are provided. It asserts that the arguments passed to the underlying OpenAI client's create method do not list "apply\_patch" among the available tools.*


### test_message_retrieval_with_realistic_apply_patch_response (function, L1119-L1190)

> *Summary: This test verifies that the client correctly retrieves and consolidates a complex response containing both explanatory text and multiple file patch operations from an input mock response. It asserts that the output message contains exactly one text element and two distinct `apply_patch_call` elements, while also validating token usage extraction.*


### test_apply_patch_with_reasoning_is_filtered (function, L1193-L1213)

> *Summary: This test verifies that a client correctly filters out reasoning blocks when processing responses. It simulates receiving both reasoning and patch call data, asserting that the resulting message content only contains the `apply_patch_call` type and excludes any "reasoning" types.*


### test_apply_patch_operation_with_agent_tool (function, L1216-L1229)

> *Summary: This test verifies the `_apply_patch_operation` method by simulating a file creation operation within a temporary directory context. It asserts that the returned result correctly identifies the call ID and confirms the successful creation of the specified file.*


### test_apply_patch_operation_without_agent_creates_default_editor (function, L1232-L1252)

> *Summary: This test verifies that applying a patch operation, when provided with a `workspace_dir`, results in the creation of a default editor instance within the client's execution context. It uses temporary directories to safely simulate file system operations during the call.*


### test_apply_patch_operation_with_async_patches (function, L1255-L1298)

> *Summary: This test verifies the `_apply_patch_operation` method's behavior when processing file operations asynchronously. It uses a mocked client and temporary directory to confirm that create, update, and delete operations execute correctly with `async_patches=True`, returning completed results for each action.*


### test_apply_patch_operation_unknown_operation_type (function, L1301-L1313)

> *Summary: This test verifies that the patch operation handler correctly fails when provided with an unrecognized operation type. It inputs a dictionary containing an unknown operation and asserts the resulting status is "failed" with an appropriate error message.*


### test_apply_patch_operation_handles_exceptions (function, L1316-L1339)

> *Summary: This test verifies that the `_apply_patch_operation` method correctly handles exceptions when provided with an invalid workspace directory path. It asserts that the resulting operation status is "failed" and contains an appropriate error message, regardless of whether the system is Windows or Unix-like.*


### test_apply_patch_operation_all_operation_types (function, L1342-L1372)

> *Summary: This test verifies that the `_apply_patch_operation` method correctly handles all three file modification types—create, update, and delete—by executing these operations within a temporary directory context. It asserts that each operation completes successfully and returns an output reflecting the intended change.*


### test_apply_patch_operation_with_allowed_paths (function, L1375-L1415)

> *Summary: This test verifies that the `_apply_patch_operation` method correctly enforces path restrictions when applying file updates. It attempts to patch a file within an explicitly allowed directory structure and asserts success, while simultaneously asserting failure for an attempt targeting a disallowed path.*


### test_extract_apply_patch_calls_from_content (function, L1423-L1446)

> *Summary: This test verifies that the `_extract_apply_patch_calls` method correctly parses a list of messages to find and return any embedded `apply_patch_call` objects. It takes a message structure containing text and patch call data as input and asserts the resulting dictionary contains exactly one matching call ID with the correct type.*


### test_extract_apply_patch_calls_from_tool_calls (function, L1449-L1471)

> *Summary: This test verifies that the `_extract_apply_patch_calls` method correctly parses a list of messages containing tool calls. It takes a message structure with an embedded `apply_patch_call` and asserts that the returned result accurately captures this specific call ID and type.*


### test_extract_apply_patch_calls_from_both_content_and_tool_calls (function, L1474-L1502)

> *Summary: This test verifies that the `_extract_apply_patch_calls` method correctly gathers patch calls from both the message content and the tool calls within a single assistant message. It asserts that two distinct patch call IDs are successfully extracted from the provided input structure.*


### test_extract_apply_patch_calls_ignores_non_assistant_messages (function, L1505-L1527)

> *Summary: This test verifies that the message processing logic correctly filters for and extracts only `apply_patch_call` objects found within assistant role messages. It takes a list of mixed-role messages as input and asserts that the output contains exactly one extracted call ID corresponding to the assistant's patch request.*


### test_extract_apply_patch_calls_skips_items_without_call_id (function, L1530-L1551)

> *Summary: This test verifies that the `_extract_apply_patch_calls` method correctly filters out items lacking a `call_id` when processing a list of messages. It asserts that only the patch call containing a valid ID is returned from the input message structure.*


### test_execute_apply_patch_calls_with_apply_patch_tool (function, L1554-L1578)

> *Summary: This test verifies that the `_execute_apply_patch_calls` method correctly processes and executes patch application calls when the necessary tool is available. It takes a dictionary of patch call requests, a list of enabled tools, and a temporary directory to simulate file operations, returning a list containing the processed output for each successful call.*


### test_execute_apply_patch_calls_with_apply_patch_async_tool (function, L1581-L1604)

> *Summary: This test verifies that the `_execute_apply_patch_calls` method correctly utilizes asynchronous tool execution when `"apply_patch_async"` is present in the available tools. It takes a dictionary of patch calls, a list of enabled async tools, and a temporary directory to process and return the results of the executed operations.*


### test_execute_apply_patch_calls_returns_empty_when_not_in_built_in_tools (function, L1607-L1624)

> *Summary: When provided with a dictionary of patch calls and no enabled tools, the function returns an empty list. It simulates executing apply patch calls against a temporary directory using a mocked OpenAI client.*


### test_execute_apply_patch_calls_returns_empty_for_empty_dict (function, L1627-L1636)

> *Summary: When provided with an empty dictionary for patch calls, this test verifies that the `_execute_apply_patch_calls` method returns an empty list. It uses a mocked OpenAI client and a temporary directory to execute and assert this behavior.*


### test_execute_apply_patch_calls_handles_multiple_calls (function, L1639-L1671)

> *Summary: This test verifies that the client correctly processes and executes multiple `apply_patch` calls provided in a dictionary input. It asserts that the function returns results corresponding to all submitted patch operations, successfully handling concurrent or sequential execution of these calls within a temporary directory context.*


### test_execute_apply_patch_calls_skips_calls_without_operation (function, L1674-L1701)

> *Summary: This test verifies that a client method filters incoming patch calls, executing only those containing an `operation` field. It takes a dictionary of potential patch calls and returns a list containing only the valid calls that should be processed.*


### test_convert_messages_to_input_basic_text (function, L1704-L1724)

> *Summary: This test verifies that the internal conversion method correctly transforms a list of standard text messages into structured input items. It asserts that the resulting list contains two entries, ordered in reverse chronological sequence (assistant then user), with appropriate content types assigned to each role.*


### test_convert_messages_to_input_filters_apply_patch_calls (function, L1727-L1755)

> *Summary: This test verifies that a message conversion utility correctly filters out `apply_patch_call` objects when transforming assistant messages into input structures. It asserts that only the plain text content remains in the resulting list of input items, excluding any patch call instructions.*


### test_convert_messages_to_input_handles_image_params (function, L1758-L1790)

> *Summary: This test verifies that the `_convert_messages_to_input` method correctly parses image parameters from a list of messages. It takes a message structure containing an `image_params` block and asserts that these parameters are extracted into a separate dictionary while the resulting input items only contain the corresponding text content.*


### test_convert_messages_to_input_handles_multimodal_content (function, L1793-L1816)

> *Summary: This test verifies that the message conversion utility correctly processes a list containing mixed text and image content. It takes a structured message format as input and asserts that the resulting `input_items` accurately preserves the sequence and types of all multimodal components.*


### test_convert_messages_to_input_handles_tool_role_messages (function, L1819-L1838)

> *Summary: This test verifies that the message conversion utility correctly transforms a list containing a `"tool"` role message into a structured `function_call_output` item. It confirms the resulting item accurately captures the tool call ID and its associated output content.*


### test_convert_messages_to_input_filters_tool_responses_for_processed_apply_patch (function, L1841-L1859)

> *Summary: This test verifies that a specific message conversion method correctly filters out tool responses when processing messages for an `apply_patch` operation. Given a list containing a tool message, the function is expected to result in zero items being added to the output list.*


### test_convert_messages_to_input_raises_error_for_invalid_content_type (function, L1862-L1876)

> *Summary: This test verifies that the message conversion utility throws a `ValueError` when provided with a message containing an unrecognized content type. It passes a list of messages with invalid content and asserts that the expected error is raised during processing.*


### test_convert_messages_to_input_handles_empty_content_blocks (function, L1879-L1902)

> *Summary: This test verifies that the message conversion logic correctly ignores messages whose content consists entirely of filtered blocks. It passes a list containing an assistant message with only an `apply_patch_call` and asserts that no input items are generated.*


### test_convert_messages_to_input_null_content_assistant_message (function, L1905-L1944)

> *Summary: This test verifies that an `assistant` message with `None` content (indicating a tool-call-only response) is correctly transformed into the API input format. It asserts that the resulting text block for this assistant message contains an empty string (`""`) instead of `null`, preventing rejection by the Responses API.*


### test_convert_messages_to_input_empty_string_content_assistant_message (function, L1947-L1975)

> *Summary: This test verifies that the message conversion utility correctly processes an assistant message containing empty string content. It asserts that the resulting structured output for this specific input retains an empty text block while still including tool call information.*


### test_message_retrieval_tool_call_only_produces_none_content (function, L1978-L2009)

> *Summary: Verifies that when a response contains only function calls, the resulting message object has `content` set to `None`. It simulates an OpenAI-like response with a tool call and asserts the structure of the processed output.*


### test_convert_messages_to_input_preserves_order_in_reverse (function, L2012-L2030)

> *Summary: This test verifies that the internal message conversion process adds messages to an output list in reverse chronological order. It takes a list of structured messages as input and asserts that the resulting items are ordered from the last message provided to the first.*


### test_shell_tool_shell_call_outcome_model_dump (function, L2038-L2050)

> *Summary: This test verifies the `model_dump()` method of the `ShellCallOutcome` model by asserting correct dictionary serialization for both successful exit and timeout scenarios, using predefined input values. It confirms that the resulting dictionary accurately reflects the provided outcome type and associated exit code.*


### test_shell_tool_shell_command_output_model_dump (function, L2053-L2066)

> *Summary: Verifies the serialization of a `ShellCommandOutput` instance into a dictionary format. It takes an initialized output object containing standard output, standard error, and a shell call outcome, then asserts that the resulting dictionary accurately reflects these values.*


### test_shell_tool_shell_call_output_model_dump (function, L2069-L2101)

> *Summary: This test verifies the `model_dump` serialization of a `ShellCallOutput` object. It confirms that the method correctly serializes both an empty state and a populated state containing multiple command outputs with associated standard output, error streams, and exit codes.*


### test_shell_tool_shell_call_output_post_init (function, L2104-L2110)

> *Summary: Verifies that the `ShellCallOutput` object's `output` attribute is initialized as an empty list upon instantiation. This confirms the expected default state for storing shell command results.*


### test_shell_tool_extract_shell_calls_from_content (function, L2118-L2141)

> *Summary: This test verifies that the `_extract_shell_calls` method correctly parses a list of messages containing structured content. It takes mock OpenAI client data as input and asserts that it successfully extracts one shell call object, verifying its ID and type.*


### test_shell_tool_extract_shell_calls_from_tool_calls (function, L2144-L2166)

> *Summary: This test verifies that the `_extract_shell_calls` method correctly parses a list of messages containing tool calls. Given an input message with a specific shell call structure, it asserts that the output contains exactly one entry matching the expected shell call ID and type.*


### test_shell_tool_extract_shell_calls_from_both_content_and_tool_calls (function, L2169-L2197)

> *Summary: This test verifies that the extraction logic successfully retrieves shell calls from both the message content and the `tool_calls` array within a single assistant message. It takes a list of messages as input and asserts that two distinct shell call IDs are present in the returned collection.*


### test_shell_tool_extract_shell_calls_ignores_non_assistant_messages (function, L2200-L2231)

> *Summary: This test verifies that a message extraction utility correctly filters shell calls, only processing those originating from the assistant role. Given a list of messages containing both user and assistant inputs, it asserts that only the assistant's shell call is returned.*


### test_shell_tool_extract_shell_calls_skips_items_without_call_id (function, L2234-L2259)

> *Summary: This test verifies that the `_extract_shell_calls` method correctly filters out shell call objects lacking a `call_id`. It takes a list of messages containing mixed shell calls and asserts that only the one with a valid ID is returned.*


### test_shell_tool_execute_shell_calls_returns_empty_when_not_in_built_in_tools (function, L2262-L2281)

> *Summary: When the `shell_call` type is present in the input dictionary but the shell tool is not explicitly enabled via `built_in_tools`, the function returns an empty list. This verifies that execution of external shell commands is suppressed by default unless configured otherwise.*


### test_shell_tool_execute_shell_calls_returns_empty_for_empty_dict (function, L2284-L2295)

> *Summary: When provided with an empty dictionary for shell calls, the function returns an empty list. This test verifies that `OpenAIResponsesClient._execute_shell_calls` correctly handles zero input calls when using the "shell" tool.*


### test_shell_tool_execute_shell_calls_with_shell_tool (function, L2298-L2337)

> *Summary: This test verifies that the `_execute_shell_calls` method correctly processes shell tool requests when the "shell" is available as a built-in tool. It simulates an execution by mocking the shell executor to return specific command outputs and asserts that the client returns the corresponding structured results.*


### test_shell_tool_execute_shell_calls_handles_multiple_calls (function, L2340-L2382)

> *Summary: This test verifies that the `_execute_shell_calls` method correctly processes and handles multiple shell command requests provided in a dictionary input. It mocks the underlying executor to simulate successful execution for two distinct calls, asserting that both results are returned in the output.*


### test_shell_tool_execute_shell_calls_skips_calls_without_action (function, L2385-L2418)

> *Summary: This test verifies that the shell execution logic only processes tool calls containing an explicit action. It passes a dictionary of potential shell calls, one with and one without an action, asserting that only the call with defined commands is executed by the mocked executor.*


### test_shell_tool_execute_shell_operation_with_no_commands (function, L2421-L2437)

> *Summary: When called with an empty action dictionary, this test verifies that the shell operation execution returns a specific error indicating no commands were provided. The output confirms an exit status of 1 and includes the "No commands provided" message in standard error.*


### test_shell_tool_execute_shell_operation_success (function, L2440-L2482)

> *Summary: Verifies that the shell operation execution successfully processes a list of commands, returning structured output containing standard output and exit codes for each command. It simulates successful command execution by mocking the underlying executor to return predefined results.*


### test_shell_tool_execute_shell_operation_handles_exceptions (function, L2485-L2508)

> *Summary: This test verifies that the `_execute_shell_operation` method correctly handles exceptions thrown by the underlying shell executor. It asserts that when an error occurs during command execution, the returned result object accurately reflects the failure, including specific error messages and a non-zero exit code.*


### test_shell_tool_execute_shell_operation_initializes_executor (function, L2511-L2554)

> *Summary: This test verifies that the `OpenAIResponsesClient` correctly initializes a `ShellExecutor` instance when executing shell operations. It passes specific configuration parameters like workspace directory, allowed/denied commands, and filtering settings to the executor upon invocation.*


### test_shell_tool_execute_shell_operation_updates_existing_executor (function, L2557-L2598)

> *Summary: This test verifies that the `_execute_shell_operation` method correctly updates an existing shell executor's configuration when called subsequently with new parameters. It simulates two calls, ensuring the second call successfully overwrites the initial workspace directory and allowed paths on the mocked executor object.*


### test_shell_tool_normalize_messages_for_responses_api_with_shell_calls (function, L2606-L2656)

> *Summary: This test verifies that the message normalization process correctly transforms messages containing shell calls into a structured response format. It feeds in an assistant message with a `shell_call` and asserts that the resulting list contains a corresponding `shell_call_output` entry for the executed command.*


### test_shell_tool_normalize_messages_for_responses_api_filters_shell_calls (function, L2659-L2709)

> *Summary: This test verifies that the message normalization function correctly filters out `shell_call` objects from a list of messages when preparing them for an API response. It inputs a message containing both text and a shell call, mocks the execution environment, and asserts that the resulting content only contains the original text while excluding the shell call structure.*


### test_shell_tool_normalize_messages_for_responses_api_with_previous_shell_calls (function, L2712-L2757)

> *Summary: This test verifies that the message normalization process correctly incorporates results from prior shell executions when preparing data for the responses API. It simulates a scenario where previous shell calls exist and asserts that the resulting messages contain the expected `shell_call_output`.*


### test_shell_tool_create_with_shell_tool_added_to_built_in_tools (function, L2765-L2795)

> *Summary: This test verifies that when initializing an `OpenAIResponsesClient` with a specific configuration, the system correctly includes the "shell" tool within the list of built-in tools sent to the mocked OpenAI client. It simulates a user request and asserts that the resulting API call arguments contain the expected shell tool definition.*


### test_shell_tool_create_with_shell_calls_executes_commands (function, L2798-L2836)

> *Summary: This test verifies that the client correctly executes shell commands when provided with a message containing a `shell_call` action. It mocks an external shell executor to confirm that the `create` method invokes the command execution logic as expected.*


### test_shell_tool_create_with_shell_and_other_built_in_tools (function, L2839-L2863)

> *Summary: This test verifies that the client correctly includes multiple specified built-in tools, including "shell," when creating a response. It mocks the shell executor and asserts that the resulting API call to the OpenAI client contains all requested tool types.*


### test_shell_tool_create_with_no_built_in_tools_excludes_shell (function, L2866-L2877)

> *Summary: This test verifies that the `OpenAIResponsesClient` does not include a "shell" tool when initialized without any built-in tools provided. It calls the client's creation method and asserts that no tool of type "shell" appears in the resulting API call arguments.*


### test_shell_tool_convert_messages_to_input_filters_shell_calls (function, L2880-L2908)

> *Summary: This test verifies that a message conversion utility correctly filters out processed `shell_call` actions when transforming messages into input structures. It asserts that the resulting list contains only the original text content, excluding any shell execution instructions.*


### test_shell_tool_convert_messages_to_input_filters_tool_responses_for_processed_shell (function, L2911-L2929)

> *Summary: This test verifies that a specific message containing a tool response for a processed shell call is correctly excluded when converting messages to input filters. It asserts that the resulting list of input items remains empty after calling the conversion method with the provided tool message.*

