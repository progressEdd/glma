# test/llm_clients/test_content_blocks.py

11 class(es): TestTextContent, TestImageContent, TestAudioContent, TestVideoContent, TestReasoningContent, TestCitationContent, TestToolCallContent, TestToolResultContent, TestGenericContent, TestContentParser, TestContentBlockInteroperability. 37 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTextContent | class |  |
| TestImageContent | class |  |
| TestAudioContent | class |  |
| TestVideoContent | class |  |
| TestReasoningContent | class |  |
| TestCitationContent | class |  |
| TestToolCallContent | class |  |
| TestToolResultContent | class |  |
| TestGenericContent | class |  |
| TestContentParser | class |  |
| TestContentBlockInteroperability | class |  |

## Chunks

### TestTextContent (class, L26-L38)

> *Summary: Verifies the `TextContent` object's initialization by testing correct assignment of `type`, `text`, and optional `extra` fields when instantiated with various inputs. It ensures that provided data is accurately stored within the resulting content block instance.*


### test_create_text_content (method, L29-L33, parent: TestTextContent)

> *Summary: This test verifies the correct initialization of a `TextContent` object by asserting that its `type` and `text` attributes match the provided inputs ("text" and "Hello world"). It confirms the object correctly stores the intended text data upon creation.*


### test_text_content_with_extra_fields (method, L35-L38, parent: TestTextContent)

> *Summary: Verifies that a `TextContent` object correctly stores arbitrary key-value pairs provided in its `extra` dictionary during initialization. It asserts the stored `extra` attribute matches the input data.*


### TestImageContent (class, L41-L63)

> *Summary: This test suite verifies the instantiation and attribute setting of an `ImageContent` object, ensuring it correctly handles initialization with either a remote `image_url`, a base64 `data_uri`, or both (though only one should be set). It confirms that optional fields like `detail` are correctly assigned when provided.*


### test_create_image_content (method, L44-L50, parent: TestImageContent)

> *Summary: This test verifies the correct initialization of an `ImageContent` object by asserting its type and image URL match the provided inputs, while also confirming that optional fields like `data_uri` and `detail` remain unset.*


### test_image_content_with_detail (method, L52-L55, parent: TestImageContent)

> *Summary: This test verifies that an `ImageContent` object correctly stores the specified detail level when initialized with an image URL and a detail string. It asserts that the stored `detail` attribute matches the input value of `"high"`.*


### test_image_content_with_data_uri (method, L57-L63, parent: TestImageContent)

> *Summary: This test verifies the correct instantiation of an `ImageContent` object when provided with a base64 data URI. It asserts that the content type and the associated data URI are set correctly, while confirming the image URL remains null.*


### TestAudioContent (class, L66-L89)

> *Summary: This test suite verifies the instantiation and attribute setting of an `AudioContent` object, ensuring it correctly handles initialization with either a remote URL, a base64 data URI, or both a transcript. It confirms that providing one input (like `data_uri`) correctly nullifies the other potential inputs (like `audio_url`).*


### test_create_audio_content (method, L69-L75, parent: TestAudioContent)

> *Summary: This test verifies the correct initialization of an `AudioContent` object when provided with a specific audio URL. It asserts that the type and URL are set correctly while ensuring optional fields like `data_uri` and `transcript` remain unset (None).*


### test_audio_content_with_transcript (method, L77-L80, parent: TestAudioContent)

> *Summary: Verifies that an `AudioContent` object correctly stores and exposes the provided transcript string when initialized with audio data. It asserts the stored transcript matches the input value.*


### test_audio_content_with_data_uri (method, L82-L89, parent: TestAudioContent)

> *Summary: This test verifies the correct instantiation of an `AudioContent` object when provided with a base64 data URI for its audio source. It asserts that the object correctly stores the type, data URI, and transcript while ensuring the dedicated audio URL remains unset.*


### TestVideoContent (class, L92-L108)

> *Summary: This test suite verifies the `VideoContent` object's initialization logic for video blocks. It confirms that the object correctly stores either a remote `video_url` or a base64 encoded `data_uri`, ensuring only one source is set at a time.*


### test_create_video_content (method, L95-L100, parent: TestVideoContent)

> *Summary: This test verifies the correct initialization of a `VideoContent` object by asserting that its type and provided video URL are set as expected, while also confirming that the data URI remains unset.*


### test_video_content_with_data_uri (method, L102-L108, parent: TestVideoContent)

> *Summary: This test verifies the correct instantiation of a `VideoContent` object when provided with a base64 data URI. It asserts that the content type and the supplied data URI are correctly stored, while confirming that the dedicated video URL remains unset.*


### TestReasoningContent (class, L111-L126)

> *Summary: Verifies the instantiation and attribute setting of a `ReasoningContent` object, ensuring correct assignment for both basic reasoning text and cases including an optional summary string. It confirms that the type is set to "reasoning" and validates the presence or absence of the summary field upon creation.*


### test_create_reasoning_content (method, L114-L119, parent: TestReasoningContent)

> *Summary: This test verifies the correct initialization of a `ReasoningContent` object by asserting that its type and reasoning text match the provided inputs, while also confirming the summary field remains unset (`None`).*


### test_reasoning_content_with_summary (method, L121-L126, parent: TestReasoningContent)

> *Summary: This test verifies the correct construction of a `ReasoningContent` object, ensuring that the provided summary string is accurately stored within the instance. It asserts that the `summary` attribute matches the input value during initialization.*


### TestCitationContent (class, L129-L155)

> *Summary: This test suite verifies the instantiation and attribute setting of a `CitationContent` object. It confirms that the block correctly stores provided data like URL, title, snippet, and optionally accepts a relevance score.*


### test_create_citation_content (method, L132-L144, parent: TestCitationContent)

> *Summary: Verifies the correct initialization and attribute assignment for a `CitationContent` object, ensuring that provided citation details like URL, title, and snippet are correctly stored. It also confirms that the relevance score defaults to `None`.*


### test_citation_content_with_relevance (method, L146-L155, parent: TestCitationContent)

> *Summary: This test verifies that a `CitationContent` object correctly stores and exposes its relevance score when initialized with specific citation details. It asserts the stored `relevance_score` matches the input value of $0.87$.*


### TestToolCallContent (class, L158-L167)

> *Summary: This test verifies the correct instantiation and attribute assignment of a `ToolCallContent` object, ensuring it properly stores the type, ID, function name, and arguments for a tool call. It confirms that provided inputs result in the expected structure within the content block.*


### test_create_tool_call_content (method, L161-L167, parent: TestToolCallContent)

> *Summary: This test verifies the correct instantiation and attribute assignment of a `ToolCallContent` object. It confirms that provided inputs—including type, ID, name, and arguments string—are accurately stored within the created content block.*


### TestToolResultContent (class, L170-L178)

> *Summary: This test verifies the correct instantiation and attribute assignment of a `ToolResultContent` object. It confirms that an instance correctly holds the specified type, tool call ID, and output string upon creation.*


### test_create_tool_result_content (method, L173-L178, parent: TestToolResultContent)

> *Summary: This test verifies the correct initialization and attribute setting of a `ToolResultContent` object. It confirms that an instance correctly stores its type, associated tool call ID, and result output string upon creation.*


### TestGenericContent (class, L181-L262)

> *Summary: These tests verify the functionality of `GenericContent` by asserting correct behavior across various access patterns, including attribute-style access, dictionary-style retrieval (`get`), and methods like `get_extra_fields()`. The suite ensures backward compatibility with older `.data` properties while validating modern features for handling arbitrary input fields.*


### test_create_generic_content (method, L184-L193, parent: TestGenericContent)

> *Summary: This test verifies the correct initialization and access of data within a `GenericContent` object when provided with an unknown type. It asserts that input fields are accessible via methods like `get_extra_fields()`, `model_extra`, and the legacy `.data` attribute.*


### test_generic_content_attribute_access (method, L195-L202, parent: TestGenericContent)

> *Summary: This test verifies that attributes of a `GenericContent` object can be accessed correctly using dot notation. It instantiates the object with various fields and asserts that retrieving these values matches the input data.*


### test_generic_content_get_method (method, L204-L208, parent: TestGenericContent)

> *Summary: Verifies that the `GenericContent` object behaves like a dictionary, allowing retrieval of existing fields and providing a specified default value for missing keys via its `.get()` method.*


### test_generic_content_missing_attribute (method, L210-L214, parent: TestGenericContent)

> *Summary: This test verifies that attempting to access a non-existent attribute on a `GenericContent` instance correctly raises an `AttributeError`. It instantiates the content object and asserts that accessing `.missing` triggers the expected exception.*


### test_generic_content_preserves_all_fields (method, L216-L230, parent: TestGenericContent)

> *Summary: This test verifies that a `GenericContent` object correctly preserves all provided fields, including strings, integers, lists, and nested dictionaries. It instantiates the content with sample data and asserts that each field retains its original value after creation.*


### test_generic_content_get_all_fields (method, L232-L236, parent: TestGenericContent)

> *Summary: This test verifies that the `get_all_fields` method correctly serializes a `GenericContent` object into a dictionary. It asserts that all defined fields and an empty `"extra"` field are present in the resulting output.*


### test_generic_content_get_extra_fields (method, L238-L245, parent: TestGenericContent)

> *Summary: This test verifies that the `get_extra_fields` method correctly extracts only user-defined attributes from a content object, excluding predefined fields like 'type' and 'extra'. It asserts that the returned dictionary contains all custom fields while omitting system metadata.*


### test_generic_content_has_field (method, L247-L255, parent: TestGenericContent)

> *Summary: This test verifies the `has_field` method on a `GenericContent` instance by asserting it correctly identifies existing fields ("type", "field1") and non-existent ones ("missing"). It confirms the helper accurately reports field presence based on the object's attributes.*


### test_generic_content_backward_compat_data_property (method, L257-L262, parent: TestGenericContent)

> *Summary: Verifies that the `.data` property of a `GenericContent` instance correctly mirrors the output of `get_extra_fields()` and matches the expected dictionary structure based on provided input fields. This ensures backward compatibility for accessing content data.*


### TestContentParser (class, L265-L355)

> *Summary: This suite of tests verifies the `ContentParser`'s ability to deserialize various structured data dictionaries into specific content objects. It confirms correct parsing for known types (like text, reasoning, citation) and ensures graceful fallback to a generic object when the input type is unknown or invalid.*


### test_parse_known_text_type (method, L268-L273, parent: TestContentParser)

> *Summary: This test verifies that the `ContentParser` correctly processes a known text data structure. It asserts that the output is an instance of `TextContent` and contains the expected string value.*


### test_parse_known_reasoning_type (method, L275-L281, parent: TestContentParser)

> *Summary: This test verifies that the `ContentParser` correctly processes input data containing a known reasoning type. It asserts that the resulting object is an instance of `ReasoningContent` and accurately extracts the specified reasoning text and summary from the input dictionary.*


### test_parse_known_citation_type (method, L283-L288, parent: TestContentParser)

> *Summary: This test verifies that the `ContentParser` correctly processes a dictionary representing a known citation type. It asserts that the output is an instance of `CitationContent` and that the URL field was parsed accurately from the input data.*


### test_parse_known_tool_call_type (method, L290-L295, parent: TestContentParser)

> *Summary: This test verifies that the `ContentParser` correctly processes a dictionary representing a known tool call type. It asserts that the resulting parsed object is an instance of `ToolCallContent` and that its ID matches the input data.*


### test_parse_unknown_type (method, L297-L303, parent: TestContentParser)

> *Summary: When provided with data specifying an unrecognized type, the parser defaults to creating a `GenericContent` object. This ensures that unknown structures are still processed and retain their original type identifier and custom fields.*


### test_parse_invalid_known_type_falls_back (method, L305-L314, parent: TestContentParser)

> *Summary: When provided with data specifying a known type but missing required fields (like `text` for `TextContent`), the parser emits a warning and defaults the resulting content object to `GenericContent`. This test verifies that the fallback mechanism correctly handles incomplete structured input.*


### test_register_custom_type (method, L316-L328, parent: TestContentParser)

> *Summary: This test verifies that a custom data type can be successfully registered with the parser and subsequently parsed from input data. It confirms that the resulting object is an instance of the defined custom class and holds the correct field values.*


### test_parse_missing_type_field (method, L330-L335, parent: TestContentParser)

> *Summary: When provided with input data lacking a `type` field, the parser defaults the resulting content object's type to `"unknown"` and ensures it is an instance of `GenericContent`.*


### test_parse_all_known_types (method, L337-L355, parent: TestContentParser)

> *Summary: This test verifies that the `ContentParser` correctly instantiates and returns the appropriate content object for every predefined data structure. It iterates through a set of input dictionaries, asserting that the parsed output matches the expected content class instance.*


### TestContentBlockInteroperability (class, L358-L392)

> *Summary: Verifies the structural integrity of various content block implementations by ensuring they inherit from a base class, possess a string-based `type` attribute, and correctly handle an optional `extra` data field. It uses predefined instances of different content types as input to assert these properties hold true across all tested blocks.*


### test_all_content_blocks_are_base_content (method, L361-L376, parent: TestContentBlockInteroperability)

> *Summary: Verifies that every defined content block type—including Text, Image, Audio, Video, Reasoning, Citation, ToolCall, ToolResult, and Generic—correctly inherits from the `BaseContent` class. It iterates through a predefined list of instantiated content objects to assert this inheritance relationship for all types.*


### test_content_blocks_have_type_field (method, L378-L387, parent: TestContentBlockInteroperability)

> *Summary: Verifies that instances of `TextContent` and `GenericContent` possess a string attribute named `type`. It iterates over predefined content block types to ensure this structural requirement is met for all tested objects.*


### test_content_blocks_have_extra_field (method, L389-L392, parent: TestContentBlockInteroperability)

> *Summary: Verifies that a `TextContent` object correctly stores provider-specific metadata within its `extra` attribute when initialized with it. The test confirms the input dictionary is preserved as the output for this field.*

