# test/llm_clients/test_unified_response.py

6 class(es): TestUnifiedResponseCreation, TestUnifiedResponseTextProperty, TestUnifiedResponseReasoningProperty, TestUnifiedResponseContentByType, TestUnifiedResponseSerialization, TestUnifiedResponseComplexScenarios. 28 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestUnifiedResponseCreation | class |  |
| TestUnifiedResponseTextProperty | class |  |
| TestUnifiedResponseReasoningProperty | class |  |
| TestUnifiedResponseContentByType | class |  |
| TestUnifiedResponseSerialization | class |  |
| TestUnifiedResponseComplexScenarios | class |  |

## Chunks

### TestUnifiedResponseCreation (class, L17-L125)

> *Summary: This test suite verifies the correct instantiation and behavior of `UnifiedResponse` objects by testing various configurations. It ensures that responses can be created with optional fields like usage data, cost, provider-specific metadata, finish reasons, and status flags across different providers.*


### test_create_simple_response (method, L20-L32, parent: TestUnifiedResponseCreation)

> *Summary: This test verifies the construction of a basic `UnifiedResponse` object, ensuring it correctly holds predefined metadata like ID, model name, and provider, while confirming that optional fields are initialized to default or null values. It uses a pre-built `UnifiedMessage` containing simple text content as input for validation.*


### test_create_response_with_usage (method, L34-L42, parent: TestUnifiedResponseCreation)

> *Summary: This test verifies the correct construction of a `UnifiedResponse` object, ensuring that provided message content and associated token usage statistics are accurately stored within the resulting response structure. It confirms that the input usage dictionary is correctly assigned to the response's usage attribute.*


### test_create_response_with_cost (method, L44-L49, parent: TestUnifiedResponseCreation)

> *Summary: This test verifies that a `UnifiedResponse` object correctly stores the associated monetary cost. It constructs a response with predefined content and explicitly sets the cost to $0.015 for assertion.*


### test_create_response_with_provider_metadata (method, L51-L59, parent: TestUnifiedResponseCreation)

> *Summary: This test verifies that a `UnifiedResponse` object correctly stores arbitrary, provider-specific key-value pairs within its `provider_metadata` attribute when initialized with them. It confirms the input metadata dictionary matches the stored output metadata.*


### test_create_response_with_finish_reason (method, L61-L68, parent: TestUnifiedResponseCreation)

> *Summary: This test verifies the construction of a `UnifiedResponse` object, ensuring that setting the `finish_reason` attribute correctly populates the response structure with a specific reason like `"stop"`. It takes a message and configuration details as input to produce a fully formed response object for assertion.*


### test_create_response_with_status (method, L70-L77, parent: TestUnifiedResponseCreation)

> *Summary: This test verifies the construction of a `UnifiedResponse` object, ensuring it correctly holds a specified status like `"completed"` along with associated message content and metadata. It confirms that the instantiated response object reflects the provided status attribute.*


### test_create_response_with_custom_status (method, L79-L88, parent: TestUnifiedResponseCreation)

> *Summary: This test verifies that a `UnifiedResponse` object can be successfully created and its status correctly set to various custom or future states like "streaming" or "rate\_limited". It iterates through predefined statuses, constructing a response for each one to ensure extensibility of the status field.*


### test_standard_statuses_constant (method, L90-L95, parent: TestUnifiedResponseCreation)

> *Summary: Verifies that the `UnifiedResponse` class possesses a `STANDARD_STATUSES` attribute and confirms it contains expected status strings like "completed," "in\_progress," and "failed." This test ensures the defined set of standard response statuses is correctly implemented.*


### test_is_standard_status_method (method, L97-L117, parent: TestUnifiedResponseCreation)

> *Summary: Verifies that a `UnifiedResponse` object correctly identifies standard operational statuses ("completed", "in\_progress", "failed") as true, while custom or null statuses are identified as false. It tests this behavior by instantiating responses with various status strings and `None`.*


### test_create_response_different_providers (method, L119-L125, parent: TestUnifiedResponseCreation)

> *Summary: Iterates through a list of LLM providers to verify that a `UnifiedResponse` object correctly stores the specified provider when initialized with different inputs. It confirms the `provider` attribute matches the input value for each test case.*


### TestUnifiedResponseTextProperty (class, L128-L162)

> *Summary: Verifies the `text` property of a `UnifiedResponse` by testing how it aggregates text content from various message structures. It handles single messages, multiple content blocks within one message (concatenating reasoning and text), multiple assistant messages across the response, and empty message lists.*


### test_text_property_single_message (method, L131-L136, parent: TestUnifiedResponseTextProperty)

> *Summary: This test verifies that the `UnifiedResponse` object correctly extracts text content from a single message within its structure. It asserts that accessing the `.text` property yields the string contained in the `TextContent`.*


### test_text_property_multiple_content_blocks (method, L138-L147, parent: TestUnifiedResponseTextProperty)

> *Summary: This test verifies that a unified response correctly concatenates text from multiple content blocks within the first message. It asserts that the `response.text` property combines the reasoning and textual parts sequentially.*


### test_text_property_multiple_messages (method, L149-L156, parent: TestUnifiedResponseTextProperty)

> *Summary: Verifies that the `text` property of a unified response correctly concatenates the text content from multiple constituent messages, joining them with a space. It takes a `UnifiedResponse` containing several `UnifiedMessage` objects and asserts the resulting string matches the combined content.*


### test_text_property_empty_messages (method, L158-L162, parent: TestUnifiedResponseTextProperty)

> *Summary: When initialized with an empty list of messages, the resulting object's `text` property should evaluate to an empty string. This test verifies the default behavior for responses lacking any message content.*


### TestUnifiedResponseReasoningProperty (class, L165-L213)

> *Summary: This test suite verifies the `reasoning` property of a `UnifiedResponse` object by asserting correct extraction and aggregation of reasoning content from various message structures. It checks scenarios including single, multiple blocks within one message, reasoning spread across multiple messages, and cases where no reasoning is present.*


### test_reasoning_property_single_block (method, L168-L176, parent: TestUnifiedResponseReasoningProperty)

> *Summary: This test verifies that a `UnifiedResponse` correctly extracts and validates the presence of a single reasoning block from its content. It asserts that the extracted list contains exactly one element, matching the expected reasoning text provided in the input message structure.*


### test_reasoning_property_multiple_blocks_single_message (method, L178-L189, parent: TestUnifiedResponseReasoningProperty)

> *Summary: This test verifies that a `UnifiedResponse` correctly extracts multiple reasoning blocks when they are present within a single message's content array. It asserts that the resulting list of reasoning blocks contains exactly two entries from the provided input structure.*


### test_reasoning_property_multiple_messages (method, L191-L206, parent: TestUnifiedResponseReasoningProperty)

> *Summary: This test verifies that a `UnifiedResponse` correctly aggregates and exposes multiple reasoning blocks when provided with several assistant messages. It asserts that the resulting list of reasoning blocks contains all expected entries from the input messages.*


### test_reasoning_property_no_reasoning (method, L208-L213, parent: TestUnifiedResponseReasoningProperty)

> *Summary: When provided with a response containing only assistant text without any explicit reasoning blocks, this test asserts that the `reasoning` attribute of the unified response is empty. It verifies correct handling when no reasoning information is present in the input structure.*


### TestUnifiedResponseContentByType (class, L216-L263)

> *Summary: This test suite verifies the `get_content_by_type` method on a `UnifiedResponse`. It ensures that the method correctly filters and aggregates content blocks of a specific type (like "citation" or custom types like "reflection") across multiple messages within the response, handling cases with matches, unknown types, and no matching content.*


### test_get_content_by_type_across_messages (method, L219-L239, parent: TestUnifiedResponseContentByType)

> *Summary: Given a `UnifiedResponse` containing multiple messages with mixed content types, this test verifies that retrieving content by type successfully aggregates all matching elements across all included messages. It asserts that the returned list contains the correct count and type of items based on the input structure.*


### test_get_content_by_type_unknown_type (method, L241-L255, parent: TestUnifiedResponseContentByType)

> *Summary: This test verifies that a unified response correctly extracts all content items matching a specific type from its messages. It inputs a `UnifiedResponse` containing multiple generic content blocks and asserts the returned list contains the expected number of instances of the correct content type.*


### test_get_content_by_type_no_match (method, L257-L263, parent: TestUnifiedResponseContentByType)

> *Summary: When provided with a `UnifiedResponse`, this test verifies that calling `get_content_by_type` with a non-existent content type returns an empty list. It confirms the method correctly handles cases where no matching blocks are present in the response.*


### TestUnifiedResponseSerialization (class, L266-L306)

> *Summary: This test suite verifies that a `UnifiedResponse` object can be correctly serialized into both a Python dictionary and a JSON string. It uses predefined message and response data to assert the integrity of key fields like ID, model name, provider, and cost after serialization.*


### test_response_serialization (method, L269-L294, parent: TestUnifiedResponseSerialization)

> *Summary: Verifies that a `UnifiedResponse` object can be correctly serialized into a dictionary format. It constructs a sample response containing messages and usage data, then asserts specific fields in the resulting dictionary match the input values.*


### test_response_serialization_to_json (method, L296-L306, parent: TestUnifiedResponseSerialization)

> *Summary: This test verifies that a `UnifiedResponse` object can be correctly serialized into a JSON string. It takes a constructed response object and asserts that key identifiers like the ID and model name are present in the resulting JSON output.*


### TestUnifiedResponseComplexScenarios (class, L309-L435)

> *Summary: This test suite validates the `UnifiedResponse` structure by simulating various complex LLM outputs from different providers like OpenAI and Anthropic. It verifies correct parsing and aggregation of mixed content types, including reasoning blocks, web citations, and future-proof generic data structures across multi-turn conversations.*


### test_openai_o1_with_reasoning (method, L312-L339, parent: TestUnifiedResponseComplexScenarios)

> *Summary: This test verifies that a `UnifiedResponse` correctly structures and exposes content from an OpenAI-like model output containing both structured reasoning blocks and standard text. It asserts the presence of one reasoning block with a specific summary, alongside the concatenated final text derived from all message contents.*


### test_anthropic_claude_with_reasoning (method, L341-L359, parent: TestUnifiedResponseComplexScenarios)

> *Summary: This test verifies the correct representation of an Anthropic Claude response containing structured reasoning blocks. It constructs a `UnifiedResponse` object with mixed content (text and reasoning) and asserts that the reasoning block is correctly captured in the response structure.*


### test_web_search_with_citations (method, L361-L387, parent: TestUnifiedResponseComplexScenarios)

> *Summary: This test verifies that a `UnifiedResponse` correctly encapsulates and exposes multiple web search citations alongside text content within its message structure. It asserts that the response contains exactly two citation objects, each possessing a non-null relevance score.*


### test_future_unknown_content_type (method, L389-L410, parent: TestUnifiedResponseComplexScenarios)

> *Summary: This test verifies forward compatibility by asserting that the response correctly extracts and validates content of an unknown type (`video_analysis`) from a list of mixed content types within a `UnifiedMessage`. It confirms that the specific data associated with this custom content type is accurately retrieved from the provided `UnifiedResponse` object.*


### test_multi_message_conversation (method, L412-L435, parent: TestUnifiedResponseComplexScenarios)

> *Summary: This test verifies the handling of a multi-turn conversation by asserting that a `UnifiedResponse` correctly contains all input messages and accurately counts the embedded reasoning blocks derived from the exchange. It uses a predefined sequence of user and assistant messages with mixed content types to validate the response structure.*

