# test/llm_clients/test_unified_message.py

7 class(es): TestUnifiedMessageCreation, TestUnifiedMessageTextExtraction, TestUnifiedMessageReasoningExtraction, TestUnifiedMessageCitationExtraction, TestUnifiedMessageToolCallExtraction, TestUnifiedMessageContentByType, TestUnifiedMessageSerialization. 28 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestUnifiedMessageCreation | class |  |
| TestUnifiedMessageTextExtraction | class |  |
| TestUnifiedMessageReasoningExtraction | class |  |
| TestUnifiedMessageCitationExtraction | class |  |
| TestUnifiedMessageToolCallExtraction | class |  |
| TestUnifiedMessageContentByType | class |  |
| TestUnifiedMessageSerialization | class |  |

## Chunks

### TestUnifiedMessageCreation (class, L19-L89)

> *Summary: This test suite verifies the correct instantiation and behavior of `UnifiedMessage` objects. It confirms that messages can be created with various configurations, including simple text, custom names, metadata, multiple content types (like reasoning or citations), and validates role handling via an `is_standard_role()` method.*


### test_create_simple_message (method, L22-L31, parent: TestUnifiedMessageCreation)

> *Summary: This test verifies the construction of a basic `UnifiedMessage` object, ensuring it correctly holds user-provided text content within its structure. It asserts that the resulting message has the correct role, contains exactly one element in its content list, and possesses default empty metadata.*


### test_create_message_with_name (method, L33-L38, parent: TestUnifiedMessageCreation)

> *Summary: This test verifies that an instance of `UnifiedMessage` correctly stores a provided name when initialized. It creates a message with specific role and content, asserting the assigned name matches the input value.*


### test_create_message_with_metadata (method, L40-L46, parent: TestUnifiedMessageCreation)

> *Summary: This test verifies the correct construction of a `UnifiedMessage` object, ensuring that provided text content and associated dictionary metadata are properly assigned to the resulting message instance. It confirms the message's internal state matches the input parameters.*


### test_create_message_with_multiple_content_blocks (method, L48-L60, parent: TestUnifiedMessageCreation)

> *Summary: This test verifies the construction of a `UnifiedMessage` object by providing it with an array containing mixed content types, such as reasoning, text, and citation blocks. It asserts that the resulting message correctly holds all three distinct content objects in the specified order.*


### test_create_message_all_roles (method, L62-L68, parent: TestUnifiedMessageCreation)

> *Summary: This test iterates through predefined roles ("user", "assistant", "system", "tool") to verify that a `UnifiedMessage` object is correctly instantiated for each one. It confirms the assigned role matches the input during creation.*


### test_create_message_with_custom_role (method, L70-L77, parent: TestUnifiedMessageCreation)

> *Summary: This test verifies that the system correctly handles and stores messages assigned to non-standard or future roles by iterating through a list of custom role strings. It asserts that the created `UnifiedMessage` object accurately reflects the provided custom role.*


### test_is_standard_role_method (method, L79-L89, parent: TestUnifiedMessageCreation)

> *Summary: Verifies that the `is_standard_role` method correctly identifies predefined roles ("user", "assistant", "system", "tool") as standard, while rejecting custom or non-standard roles like "moderator" and "reviewer". It takes a `UnifiedMessage` instance as input and returns a boolean indicating if the role is one of the recognized standards.*


### TestUnifiedMessageTextExtraction (class, L92-L155)

> *Summary: This test suite verifies the `get_text()` method on a unified message object by providing various combinations of content types as input. It asserts that the method correctly aggregates and formats text extracted from single, multiple, reasoning, citation, tool call, audio, and other mixed content blocks into a cohesive string output.*


### test_get_text_from_single_text_content (method, L95-L100, parent: TestUnifiedMessageTextExtraction)

> *Summary: This test verifies that the `UnifiedMessage` object correctly extracts plain text when it contains a single `TextContent` block. It asserts that calling `.get_text()` on a user message containing `"Hello world"` returns exactly `"Hello world"`.*


### test_get_text_from_multiple_text_contents (method, L102-L110, parent: TestUnifiedMessageTextExtraction)

> *Summary: This test verifies that a `UnifiedMessage` correctly concatenates text from multiple `TextContent` objects provided in its content list. It asserts the resulting string matches the joined input texts ("Hello world").*


### test_get_text_from_reasoning_content (method, L112-L120, parent: TestUnifiedMessageTextExtraction)

> *Summary: This test verifies that a unified message correctly concatenates text from mixed content types. It takes a list containing `ReasoningContent` and `TextContent` objects, asserting the output string combines the reasoning step and the conclusion text sequentially.*


### test_get_text_extracts_from_multiple_content_types (method, L122-L131, parent: TestUnifiedMessageTextExtraction)

> *Summary: This test verifies that the `get_text()` method correctly aggregates and formats text from a list containing mixed content types, such as plain text, citations, and tool calls. It asserts that the resulting string combines the extracted information from all provided content objects in a specific sequence.*


### test_get_text_empty_content (method, L133-L140, parent: TestUnifiedMessageTextExtraction)

> *Summary: When provided with a `UnifiedMessage` containing content blocks like citations that have empty text fields, the method returns an empty string. This verifies correct handling of messages lacking textual content.*


### test_get_text_from_all_content_types (method, L142-L155, parent: TestUnifiedMessageTextExtraction)

> *Summary: This test verifies that the `get_text()` method correctly aggregates and formats text from a list of diverse content types within a unified message. It takes a `UnifiedMessage` containing various content structures (like text, audio, tool results) as input and asserts the output matches a specific concatenated string format.*


### TestUnifiedMessageReasoningExtraction (class, L158-L190)

> *Summary: This test suite verifies the `get_reasoning()` method on a `UnifiedMessage` object. It confirms that the method correctly extracts zero, one, or multiple `ReasoningContent` blocks from a list of mixed content types within the message.*


### test_get_reasoning_single_block (method, L161-L168, parent: TestUnifiedMessageReasoningExtraction)

> *Summary: This test verifies that a `UnifiedMessage` correctly extracts all contained reasoning blocks when only one is present. It passes a message containing a single `ReasoningContent` object and asserts the resulting list has one element with the expected content.*


### test_get_reasoning_multiple_blocks (method, L170-L182, parent: TestUnifiedMessageReasoningExtraction)

> *Summary: This test verifies that a `UnifiedMessage` correctly extracts all embedded reasoning blocks from its content. It takes a message containing mixed text and multiple reasoning segments as input and asserts the returned list contains exactly two reasoning steps with the expected content.*


### test_get_reasoning_no_blocks (method, L184-L190, parent: TestUnifiedMessageReasoningExtraction)

> *Summary: When provided a `UnifiedMessage` containing only plain text, this test asserts that the method correctly returns an empty list for its reasoning blocks. It verifies that no structured reasoning components are extracted from the input message.*


### TestUnifiedMessageCitationExtraction (class, L193-L224)

> *Summary: This test suite verifies the `get_citations()` method on a `UnifiedMessage` object. It confirms that the method correctly extracts zero, one, or multiple `CitationContent` objects from the message's content array based on the input structure.*


### test_get_citations_single_citation (method, L196-L203, parent: TestUnifiedMessageCitationExtraction)

> *Summary: This test verifies that a `UnifiedMessage` containing one citation correctly returns a list of exactly one citation object, asserting the URL matches the input. It simulates retrieving citations from an assistant's message content.*


### test_get_citations_multiple_citations (method, L205-L216, parent: TestUnifiedMessageCitationExtraction)

> *Summary: This test verifies that a `UnifiedMessage` containing multiple `CitationContent` objects correctly returns all associated citations via its `get_citations()` method. It asserts that the returned list contains exactly two items, matching the URLs provided in the input message content.*


### test_get_citations_no_citations (method, L218-L224, parent: TestUnifiedMessageCitationExtraction)

> *Summary: When provided with a `UnifiedMessage` containing only plain text without any embedded references, this test asserts that the `get_citations()` method returns an empty list. It verifies correct handling of messages lacking citation data.*


### TestUnifiedMessageToolCallExtraction (class, L227-L257)

> *Summary: This test suite verifies the `get_tool_calls()` method on a `UnifiedMessage` object. It ensures correct extraction of zero, one, or multiple tool calls from the message's content list based on provided `ToolCallContent` instances.*


### test_get_tool_calls_single_call (method, L230-L238, parent: TestUnifiedMessageToolCallExtraction)

> *Summary: This test verifies that a `UnifiedMessage` containing one `ToolCallContent` correctly exposes it via the `get_tool_calls()` method. It asserts that exactly one tool call is returned and validates its ID and name against the input data.*


### test_get_tool_calls_multiple_calls (method, L240-L249, parent: TestUnifiedMessageToolCallExtraction)

> *Summary: This test verifies that a `UnifiedMessage` containing multiple `ToolCallContent` objects correctly returns all of them when calling `get_tool_calls()`. It asserts the resulting list contains exactly two tool call entries.*


### test_get_tool_calls_no_calls (method, L251-L257, parent: TestUnifiedMessageToolCallExtraction)

> *Summary: When provided with a `UnifiedMessage` containing only text content, this test verifies that the `get_tool_calls()` method correctly returns an empty list. It confirms the absence of any tool call objects in the message structure.*


### TestUnifiedMessageContentByType (class, L260-L309)

> *Summary: This test suite verifies the `get_content_by_type` method on a `UnifiedMessage` object. It ensures that the method correctly filters and returns lists of content blocks based on a specified type string, handling cases with multiple matches, no matches, and mixed content types.*


### test_get_content_by_type_text (method, L263-L274, parent: TestUnifiedMessageContentByType)

> *Summary: This test verifies that a `UnifiedMessage` correctly filters its content list based on type. Given a message containing mixed content types, it asserts that calling `get_content_by_type("text")` returns exactly the two elements matching that criterion.*


### test_get_content_by_type_unknown (method, L276-L287, parent: TestUnifiedMessageContentByType)

> *Summary: This test verifies that a `UnifiedMessage` correctly filters its content based on a specified type. Given a list of mixed content types, it asserts that the method returns only the elements matching the requested type ("reflection").*


### test_get_content_by_type_no_match (method, L289-L295, parent: TestUnifiedMessageContentByType)

> *Summary: When provided with a `UnifiedMessage` containing various content blocks, this test verifies that requesting content of a non-existent type returns an empty list. It asserts the length of the returned collection is zero when no matching types are present in the message's content.*


### test_get_content_by_type_mixed_known_and_unknown (method, L297-L309, parent: TestUnifiedMessageContentByType)

> *Summary: This test verifies that the `UnifiedMessage` correctly filters content based on a specified type. Given a list of mixed content types (including known and unknown), it asserts that only matching instances are returned as a list of the correct object type.*


### TestUnifiedMessageSerialization (class, L312-L339)

> *Summary: This test suite verifies the serialization and deserialization capabilities of a unified message object. It confirms that an instance can be converted to a dictionary representation, correctly preserving roles, names, and content structure, and also checks basic structural integrity when loading from a dictionary.*


### test_message_serialization (method, L315-L326, parent: TestUnifiedMessageSerialization)

> *Summary: Verifies that a `UnifiedMessage` object, constructed with mixed text and reasoning content types, correctly serializes into a dictionary structure. It asserts the presence of expected fields like role, name, and the correct count of content elements in the resulting dictionary.*


### test_message_deserialization (method, L328-L339, parent: TestUnifiedMessageSerialization)

> *Summary: Verifies that a dictionary representing an LLM message can be correctly structured. It asserts specific fields like `role` and the length of the `content` list match expected values from the input dictionary.*

