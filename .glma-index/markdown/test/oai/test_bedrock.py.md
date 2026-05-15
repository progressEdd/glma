# test/oai/test_bedrock.py

35 function(s): mock_response, bedrock_client, test_bedrock_llm_config_entry, test_bedrock_llm_config_entry_repr, test_bedrock_llm_config_entry_str, test_initialization, test_parsing_params, test_create_response, test_create_response_with_tool_call, test_oai_messages_to_bedrock_messages and 25 more. 9 class(es): Step, MathReasoning, Address, ContactInfo, Person, TaskItem, Project, TestBedrockStructuredOutputIntegration, TestBedrockAdditionalModelRequestFieldsIntegration. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mock_response | function |  |
| bedrock_client | function |  |
| test_bedrock_llm_config_entry | function |  |
| test_bedrock_llm_config_entry_repr | function |  |
| test_bedrock_llm_config_entry_str | function |  |
| test_initialization | function |  |
| test_parsing_params | function |  |
| test_create_response | function |  |
| test_create_response_with_tool_call | function |  |
| test_oai_messages_to_bedrock_messages | function |  |
| Step | class |  |
| MathReasoning | class |  |
| test_response_format_with_pydantic_model | function |  |
| test_response_format_with_dict_schema | function |  |
| test_response_format_with_user_tools | function |  |
| test_response_format_no_tool_call_error_handling | function |  |
| test_response_format_with_tool_supporting_model | function |  |
| test_response_format_validation_error | function |  |
| test_get_response_format_schema_pydantic | function |  |
| test_get_response_format_schema_dict | function |  |
| test_create_structured_output_tool | function |  |
| test_extract_structured_output_from_tool_call | function |  |
| test_extract_structured_output_from_tool_call_not_found | function |  |
| test_validate_and_format_structured_output | function |  |
| Address | class |  |
| ContactInfo | class |  |
| Person | class |  |
| TaskItem | class |  |
| Project | class |  |
| test_get_response_format_schema_complex_pydantic | function |  |
| test_get_response_format_schema_dict_without_type | function |  |
| test_get_response_format_schema_dict_non_object_type | function |  |
| test_normalize_pydantic_schema_simple | function |  |
| test_normalize_pydantic_schema_complex | function |  |
| test_normalize_pydantic_schema_dict_with_refs | function |  |
| test_normalize_pydantic_schema_invalid_input | function |  |
| test_normalize_pydantic_schema_missing_ref | function |  |
| test_create_structured_output_tool_dict_schema | function |  |
| test_create_structured_output_tool_complex_pydantic | function |  |
| TestBedrockStructuredOutputIntegration | class |  |
| TestBedrockAdditionalModelRequestFieldsIntegration | class |  |
| test_parsing_params_with_additional_model_request_fields | function |  |
| test_bedrock_llm_config_entry_with_additional_model_request_fields | function |  |
| test_parsing_params_additional_model_request_fields_with_none_values | function |  |

## Chunks

### mock_response (function, L21-L30)

> *Summary: Provides a factory function that returns a class capable of simulating an API response object. This mock object holds structured data like generated text, choice details, token usage, and associated costs for testing purposes.*


### bedrock_client (function, L34-L40)

> *Summary: Initializes and configures a `BedrockClient` instance, setting the AWS region to "us-east-1" and enabling support for system prompts. This function returns the configured client object ready for Bedrock API interactions.*


### test_bedrock_llm_config_entry (function, L43-L78)

> *Summary: This test verifies the serialization and validation of a `BedrockLLMConfigEntry` instance, ensuring it correctly maps its configuration parameters to a dictionary structure. It also asserts that wrapping this entry in an `LLMConfig` results in the expected list format, while simultaneously testing for a specific `ValidationError` when required fields are missing or incomplete.*


### test_bedrock_llm_config_entry_repr (function, L81-L94)

> *Summary: This test verifies the string representation (`repr`) of a `BedrockLLMConfigEntry` instance. It asserts that the generated string matches an expected format, specifically masking sensitive AWS credentials while retaining configuration details like model name and region.*


### test_bedrock_llm_config_entry_str (function, L97-L110)

> *Summary: This test verifies the string representation of a `BedrockLLMConfigEntry` object. It takes an initialized configuration instance containing AWS and model details as input and asserts that its resulting string matches a predefined expected format, masking sensitive credentials.*


### test_initialization (function, L116-L118)

> *Summary: Verifies that a `BedrockClient` instance can be successfully created by providing only an AWS region, relying on internal parameter handling for API key management. This test confirms initialization succeeds without explicitly passing credentials.*


### test_parsing_params (function, L123-L173)

> *Summary: This test verifies parameter parsing logic by calling a method with various inputs, asserting that it correctly separates and transforms configuration values into distinct dictionaries based on expected types and defaults. It also checks error handling for missing required parameters and warnings issued when incorrect input types or unsupported features are provided.*


### test_create_response (function, L179-L209)

> *Summary: This test verifies that a client correctly processes and structures the output from a mocked Bedrock API call. It feeds specific input parameters to the `create` method and asserts that the returned object contains the expected content, ID, model name, and token usage data from the mock response.*


### test_create_response_with_tool_call (function, L215-L275)

> *Summary: This test verifies the system's ability to handle a model response that includes multiple tool calls. It mocks a Bedrock client returning a message containing two distinct function calls (`currency_calculator` and `get_weather`) when provided with user input and defined tools. Assertions confirm the correct content and names of these returned tool calls in the final response object.*


### test_oai_messages_to_bedrock_messages (function, L280-L349)

> *Summary: This test verifies the `oai_messages_to_bedrock_messages` conversion logic by checking how it transforms OpenAI-style message lists into Bedrock format. It specifically tests behaviors like removing the "name" key, converting system messages to user roles, and inserting "Please continue" prompts based on the input structure.*


### Step (class, L352-L354)

> *Summary: Represents a single processing step by holding an explanatory string and the resulting output string. It inherits from `BaseModel` to structure this data for use within workflows.*


### MathReasoning (class, L357-L359)

> *Summary: This model structure holds a sequence of reasoning steps and the final computed answer. It is designed to encapsulate the output of mathematical problem-solving processes.*


### test_response_format_with_pydantic_model (function, L364-L441)

> *Summary: This test verifies that the client correctly handles structured output from Bedrock when a Pydantic model is specified. It mocks a Bedrock response containing a tool call and asserts that the resulting object extracts and validates the expected structured data, either from the message content or the tool call arguments.*


### test_response_format_with_dict_schema (function, L446-L505)

> *Summary: Tests the structured output capability by configuring a dictionary schema for Bedrock API calls. It simulates a response containing structured data and asserts that the parsed content matches the expected values defined in the input schema.*


### test_response_format_with_user_tools (function, L510-L593)

> *Summary: This test verifies that the API correctly handles structured output when both user-defined tools and a response format constraint are provided as input parameters. It mocks the Bedrock runtime to simulate a specific tool-use response and then asserts that the resulting configuration includes all expected tools and that the final response contains the required structured data.*


### test_response_format_no_tool_call_error_handling (function, L598-L625)

> *Summary: This test verifies that when a model responds with plain text instead of calling a structured output tool, the system correctly handles the fallback to textual content. It mocks a Bedrock runtime response containing only text and asserts that the resulting object reflects this non-tool-call scenario.*


### test_response_format_with_tool_supporting_model (function, L630-L690)

> *Summary: This test verifies that a model supporting Tool Use correctly returns structured output when configured with `MathReasoning`. It mocks the Bedrock runtime to simulate a response containing a `toolUse` structure and asserts that the client call includes necessary configuration, such as `toolConfig`, for this behavior.*


### test_response_format_validation_error (function, L695-L745)

> *Summary: Tests the system's ability to catch and raise an error when a Bedrock response fails to conform to a specified Pydantic schema. It mocks a response containing invalid structured output (missing required fields) and asserts that a `ValueError` or `ValidationError` is raised during processing.*


### test_get_response_format_schema_pydantic (function, L750-L758)

> *Summary: This test verifies that the internal method for generating a response format schema, when using a Pydantic model as input, correctly produces a JSON schema object. It asserts that the resulting schema is an object containing required properties like `steps` and `final_answer`.*


### test_get_response_format_schema_dict (function, L762-L777)

> *Summary: This test verifies that the internal method correctly processes a provided dictionary schema to generate an expected response format structure. It asserts that the resulting schema contains the correct object type, properties (like `name` and `age`), and required fields (`name`).*


### test_create_structured_output_tool (function, L782-L790)

> *Summary: This test verifies that a specific internal method correctly constructs a function-based tool definition for Bedrock. It asserts that the resulting structure includes the correct type, name, description, and parameter object schema.*


### test_extract_structured_output_from_tool_call (function, L795-L817)

> *Summary: This test verifies that a utility function correctly parses structured data from a list of tool call messages. It takes a list containing one standard tool call and one specialized structured output tool call, asserting the resulting dictionary contains the expected final answer and step details.*


### test_extract_structured_output_from_tool_call_not_found (function, L822-L834)

> *Summary: This test verifies that the extraction method returns `None` when provided with a list of tool calls where the corresponding function cannot be found. It passes a mock list containing one tool call to assert this specific failure case.*


### test_validate_and_format_structured_output (function, L839-L852)

> *Summary: This test verifies that the internal method correctly validates and formats structured data received from a Bedrock client. It takes a dictionary containing nested steps and a final answer, expecting the output to be a JSON string that can be parsed and verified against the input structure.*


### Address (class, L858-L864)

> *Summary: Defines a data structure representing an address, requiring street, city, and zip code as inputs. It optionally defaults the country to "USA" and outputs a structured address object.*


### ContactInfo (class, L867-L872)

> *Summary: Defines a data structure containing an email string, an optional phone number, and a required `Address` object. This class serves as a structured container for contact details within the system.*


### Person (class, L875-L882)

> *Summary: Defines a data structure representing a person, incorporating basic fields like name and age alongside nested contact information and optional lists/dictionaries for tags and metadata. It inherits from `BaseModel` to enforce structured data validation.*


### TaskItem (class, L885-L891)

> *Summary: Represents a single unit of work, holding a required title and an optional description. It defaults to incomplete status and a priority level of one.*


### Project (class, L894-L902)

> *Summary: Represents a complex project structure, holding details like a name, associated tasks, an owner, and collaborators. It accepts various inputs including lists of items and optional budget information, returning a structured data model.*


### test_get_response_format_schema_complex_pydantic (function, L907-L956)

> *Summary: Verifies that the schema generated for a complex Pydantic model correctly represents its structure, including nested objects and arrays. It asserts the presence of required fields, checks array item types, and validates the structure of nested properties like `tasks` and `owner`.*


### test_get_response_format_schema_dict_without_type (function, L960-L978)

> *Summary: This test verifies that the internal schema generation function correctly augments a provided dictionary schema when it lacks a top-level type. It asserts that the resulting schema includes `"type": "object"` and retains all specified properties and required fields from the input.*


### test_get_response_format_schema_dict_non_object_type (function, L982-L993)

> *Summary: This test verifies that when a dictionary schema with a non-object type is passed to the internal schema retrieval method, it correctly wraps the input into an object structure. The assertion confirms the output schema has a top-level `"type": "object"` and contains the original string data within a nested `"data"` property.*


### test_normalize_pydantic_schema_simple (function, L998-L1018)

> *Summary: This test verifies that a simple Pydantic schema is correctly converted to a dictionary format by resolving all internal references. It asserts that the resulting structure lacks `$defs` and that nested properties, such as those within `steps`, have their `$ref` pointers fully resolved into concrete types.*


### test_normalize_pydantic_schema_complex (function, L1022-L1064)

> *Summary: This test verifies that a complex Pydantic model is correctly converted into a JSON schema dictionary by resolving all internal references. It asserts the resulting structure contains no `$defs` and accurately represents nested objects (like `owner`, `contact`, `address`) and arrays of objects (`tasks`, `collaborators`).*


### test_normalize_pydantic_schema_dict_with_refs (function, L1068-L1124)

> *Summary: This test verifies that a schema dictionary containing internal `$ref` pointers is correctly processed by resolving all references and removing the `$defs` block. It asserts that the resulting normalized structure contains fully expanded object definitions for nested types like `User`, `Contact`, and `Profile`.*


### test_normalize_pydantic_schema_invalid_input (function, L1128-L1134)

> *Summary: This test verifies that the schema normalization function correctly raises a `ValueError` when provided with invalid inputs, such as strings or integers, instead of expected Pydantic model classes or dictionaries. It asserts that the error message specifically indicates the input type is incorrect.*


### test_normalize_pydantic_schema_missing_ref (function, L1138-L1147)

> *Summary: This test verifies that the schema normalization process raises a `ValueError` when an object references a definition (`$ref`) that is missing from the provided `$defs`. It passes a dictionary containing a reference to "NonExistent" and asserts the expected error message.*


### test_create_structured_output_tool_dict_schema (function, L1152-L1221)

> *Summary: This test verifies that a complex JSON schema, defining nested objects, arrays, and constraints like minimum/maximum values, is correctly transformed into a structured output tool definition. It asserts the resulting structure contains all expected properties and maintains the deep nesting of the input schema.*


### test_create_structured_output_tool_complex_pydantic (function, L1225-L1260)

> *Summary: This test verifies that the `_create_structured_output_tool` method correctly generates a function schema for a complex Pydantic model. It asserts that all expected properties, including deeply nested objects and array structures, are fully resolved without using `$ref` references in the resulting JSON structure.*


### TestBedrockStructuredOutputIntegration (class, L1268-L1516)

> *Summary: This code provides integration tests to validate Bedrock's structured output capabilities using an AI agent. It executes two primary scenarios: one enforcing a Pydantic schema and another using a raw JSON Schema dictionary as the response format, asserting that the resulting agent output conforms correctly to the specified structure.*


### setup_method (method, L1271-L1294, parent: TestBedrockStructuredOutputIntegration)

> *Summary: This method initializes the test environment by loading variables from a `.env` file if available and then verifies that an AWS region is configured via environment variables. If no AWS region is found, it skips all subsequent tests to prevent authentication failures.*


### test_agent_with_pydantic_structured_output (method, L1298-L1403, parent: TestBedrockStructuredOutputIntegration)

> *Summary: This test verifies an agent's ability to generate structured output using Pydantic schemas when interacting with a Bedrock LLM. It configures the agent with AWS credentials and runs it on a math problem, asserting that the final response is valid JSON containing expected fields like `final_answer` and detailed reasoning steps.*


### test_agent_with_dict_schema_structured_output (method, L1407-L1516, parent: TestBedrockStructuredOutputIntegration)

> *Summary: This test verifies an agent's ability to generate structured output using a predefined JSON schema when interacting with Bedrock. It configures the LLM with the dictionary schema and asserts that the resulting assistant message contains valid, correctly structured data matching all specified fields.*


### TestBedrockAdditionalModelRequestFieldsIntegration (class, L1522-L2095)

> *Summary: This class provides integration tests for Bedrock API interactions within an agent framework, ensuring correct behavior when using `additional_model_request_fields` for features like thinking configuration. It validates various configurations, including custom retry modes (standard, adaptive, legacy) and the successful execution of agents under these specific AWS-backed settings.*


### setup_method (method, L1525-L1548, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This method initializes the test environment by loading necessary configuration from a `.env` file if available. It then verifies that an AWS region is present in the environment variables, skipping tests if this critical setting is missing.*


### test_agent_with_thinking_configuration (method, L1552-L1605, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies the successful creation of an agent configured to use AWS Bedrock with a specific "thinking" capability enabled. It reads necessary AWS credentials and model names from environment variables before instantiating a `ConversableAgent` using a custom `LLMConfig`.*


### _get_aws_config (method, L1607-L1623, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: Retrieves AWS and Bedrock configuration by reading environment variables. It returns a dictionary containing the determined region, access keys, profile name, and default model identifier.*


### test_default_retry_configuration (method, L1626-L1675, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies that an agent configured with default retry settings successfully executes a complex prompt against a Bedrock LLM. It initializes the agent using AWS credentials and asserts that the resulting conversation contains non-empty assistant responses after running for a few turns.*


### test_agent_with_thinking_and_custom_fields (method, L1679-L1740, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies an agent's functionality when configured with AWS Bedrock and specific custom fields for enabling a "thinking" process. It initializes the agent using environment variables to configure the LLM connection and then executes it with a complex prompt to ensure a non-empty, reasoned response is generated.*


### test_custom_total_max_attempts (method, L1743-L1788, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies that an `LLMConfig` correctly sets a custom total maximum attempts value when configuring a Bedrock agent. It instantiates the agent with this configuration and asserts that the underlying Bedrock client reflects the specified retry settings before executing a simple run to confirm functionality.*


### test_legacy_retry_mode (method, L1791-L1838, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies the functionality of a conversational agent configured to use AWS Bedrock with legacy retry behavior. It initializes an agent using specific AWS credentials and runs it with a simple query, asserting that a non-empty response is successfully generated by the assistant.*


### test_bedrock_llm_config_entry_with_additional_model_request_fields_integration (method, L1842-L1897, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies the integration of `BedrockLLMConfigEntry` when supplying custom model request fields to an agent configured with AWS Bedrock. It initializes an agent using this configuration and asserts that it successfully executes a simple query against the underlying Bedrock client in legacy mode.*


### test_standard_retry_mode (method, L1900-L1944, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies the configuration and functionality of an agent using standard retry rules with AWS Bedrock. It initializes a `ConversableAgent` configured for "standard" mode and asserts that the underlying client correctly reflects this setting before executing a simple query to confirm successful operation.*


### test_adaptive_retry_mode (method, L1947-L1993, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies the configuration of adaptive retry mode for an agent using Bedrock. It initializes a `ConversableAgent` with specific AWS credentials and sets the retry mode to "adaptive" with 8 maximum attempts, then asserts that the underlying client reflects these settings before executing a simple query.*


### test_high_reliability_configuration (method, L1996-L2045, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies an agent's behavior when configured with a high-reliability setup using Bedrock. It initializes the agent with specific AWS credentials and sets `total_max_attempts` to 10 and mode to "adaptive" in the LLM configuration, then asserts these settings are correctly applied to the underlying client before running a simple query to confirm functionality.*


### test_fast_fail_configuration (method, L2048-L2095, parent: TestBedrockAdditionalModelRequestFieldsIntegration)

> *Summary: This test verifies the fast-fail behavior of an agent configured to use AWS Bedrock with minimal retries (2 attempts). It initializes a `ConversableAgent` using specific AWS credentials and runs it with a prompt, asserting that a non-empty response is successfully generated.*


### test_parsing_params_with_additional_model_request_fields (function, L2100-L2218)

> *Summary: This test verifies that parameters passed within `additional_model_request_fields` are correctly parsed and separated from standard request arguments. It confirms proper handling of various inputs, including multiple fields, exclusion of reserved keys, merging with other parameters, and ignoring invalid or null field types.*


### test_bedrock_llm_config_entry_with_additional_model_request_fields (function, L2222-L2256)

> *Summary: This test verifies that a `BedrockLLMConfigEntry` correctly accepts and serializes custom model request fields, specifically for "thinking." It instantiates the configuration with these extra fields and asserts that the resulting dictionary matches an expected structure when dumped.*


### test_parsing_params_additional_model_request_fields_with_none_values (function, L2261-L2565)

> *Summary: This test verifies that the parameter parsing correctly handles `None` values within the `additional_model_request_fields` dictionary when interacting with a Bedrock client. It also contains several other tests validating various configurations for retry logic, adaptive mode, and structured output handling across different agent setups.*

