# test/agents/experimental/a2ui/test_a2a_executor.py

1 function(s): executor. 3 class(es): TestBuildFinalParts, TestExtensionNegotiation, TestAgentCardAutoDetection. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| executor | function |  |
| TestBuildFinalParts | class |  |
| TestExtensionNegotiation | class |  |
| TestAgentCardAutoDetection | class |  |

## Chunks

### executor (function, L17-L21)

> *Summary: This function constructs and returns an `A2UIAgentExecutor` instance, injecting a fully mocked agent object into it for testing purposes. The resulting executor is configured to operate with the provided mock agent's capabilities.*


### TestBuildFinalParts (class, L24-L72)

> *Summary: This test suite verifies the logic for parsing a raw response string into structured content parts, handling cases where A2UI data is present or absent. It confirms correct output structure (text vs. data) based on input format and the `use_a2ui` flag, including error fallback behavior.*


### test_a2ui_response_returns_text_and_data_parts (method, L27-L34, parent: TestBuildFinalParts)

> *Summary: This test verifies that an executor correctly parses a response string containing both plain text and embedded A2UI JSON data. It asserts the resulting structure contains exactly two parts: one for the initial text content and another holding the parsed A2UI data.*


### test_a2ui_response_no_text_prefix (method, L36-L41, parent: TestBuildFinalParts)

> *Summary: This test verifies that when an A2UI response lacks a visible text prefix, the executor correctly constructs output containing only a `DataPart`. It asserts that the resulting list of parts has exactly one element, which must contain data.*


### test_plain_text_when_a2ui_enabled (method, L43-L46, parent: TestBuildFinalParts)

> *Summary: When A2UI is active, this test verifies that a simple string input results in exactly one structured part containing the original text content. It asserts the length of the returned parts list and checks the text within the root element of that single part.*


### test_plain_text_when_a2ui_disabled (method, L48-L53, parent: TestBuildFinalParts)

> *Summary: When the A2UI feature is disabled, this test verifies that the executor processes a raw text response by returning it as a single part containing the full original string. It asserts that the content, including any internal markers like `---a2ui_JSON---`, remains intact in the output structure.*


### test_empty_response (method, L55-L57, parent: TestBuildFinalParts)

> *Summary: When provided with an empty string as input to the internal build method, it asserts that the resulting list of parts is empty. This tests the expected behavior for handling null or no content responses from the executor.*


### test_invalid_json_falls_back_to_text (method, L59-L64, parent: TestBuildFinalParts)

> *Summary: When provided with a response containing invalid JSON within the expected A2UI format, this test verifies that the executor correctly falls back to treating the entire content as plain text. It asserts that only one part is generated and contains the original raw text marker.*


### test_markdown_fences_stripped (method, L66-L72, parent: TestBuildFinalParts)

> *Summary: This test verifies that when processing a response containing markdown fences, the executor correctly separates the content into two distinct parts. It asserts that the resulting list of parts has a length of two and that the second part contains non-null data.*


### TestExtensionNegotiation (class, L75-L175)

> *Summary: This test suite verifies how an executor handles A2UI extension negotiation based on client requests. It asserts that the response is split into separate text and data parts if the requested version matches, but remains as a single block of raw text otherwise.*


### test_client_requests_v09_gets_datapart (method, L84-L93, parent: TestExtensionNegotiation)

> *Summary: This test verifies that when a client requests an A2UI v0.9 response, the executor correctly splits the output into two distinct parts: one containing text and another containing structured data with the specific A2UI MIME type and operation details. It asserts the structure and content of both the text and data components returned by the executor.*


### test_client_does_not_request_a2ui_gets_text_only (method, L95-L101, parent: TestExtensionNegotiation)

> *Summary: When the executor is configured not to use A2UI, it constructs a single response part containing the entire raw text output, including delimiters and JSON content. This test verifies that the resulting structure has only one element and contains expected textual markers like "---a2ui_JSON---" and "deleteSurface".*


### test_client_requests_wrong_version_gets_text_only (method, L103-L114, parent: TestExtensionNegotiation)

> *Summary: When the executor is configured to bypass A2UI functionality, this test verifies that it returns a single text part containing the full, unsplit response, including any embedded JSON markers. This confirms correct fallback behavior when version mismatch prevents A2UI activation.*


### test_version_negotiation_e2e_supported (method, L116-L135, parent: TestExtensionNegotiation)

> *Summary: This test verifies end-to-end version negotiation by simulating a client requesting an extension and confirming the system activates it. It then asserts that the executor correctly splits the response into two parts, one containing metadata with the expected MIME type.*


### test_version_negotiation_e2e_unsupported (method, L137-L156, parent: TestExtensionNegotiation)

> *Summary: This test verifies that when a client requests an unsupported A2UI extension version (v1.0 requested, v0.9 supported), the activation helper correctly returns `False`. Subsequently, it asserts that the executor builds a single output part containing the raw text response, indicating no splitting occurred due to the lack of support.*


### test_version_negotiation_e2e_no_extensions (method, L158-L175, parent: TestExtensionNegotiation)

> *Summary: This test verifies that when no extensions are requested by the client, the A2UI feature remains inactive. It simulates this scenario to confirm the executor builds a response containing only one part, indicating text-only output.*


### TestAgentCardAutoDetection (class, L178-L305)

> *Summary: This test suite verifies the automatic configuration of an agent card when wrapping an `A2UIAgent` within an `A2aAgentServer`. It asserts that the server correctly adds the A2UI extension, populates it with supported catalog IDs (including custom ones), and selects the appropriate executor based on the input agent type.*


### test_a2ui_agent_adds_extension_to_card (method, L181-L195, parent: TestAgentCardAutoDetection)

> *Summary: When wrapping an `A2UIAgent` with an `A2aAgentServer`, this test verifies that the server automatically injects a specific A2UI extension into the agent's card capabilities. It asserts that exactly one extension matching the predefined URI is present on the resulting card object.*


### test_a2ui_extension_includes_supported_catalog_ids (method, L197-L215, parent: TestAgentCardAutoDetection)

> *Summary: This test verifies that the A2UI extension exposed by an `A2aAgentServer` correctly includes a list of supported catalog IDs within its parameters. It asserts that this list is present, non-empty, and contains the specific catalog ID associated with the agent instance.*


### test_custom_catalog_id_in_card (method, L217-L235, parent: TestAgentCardAutoDetection)

> *Summary: This test verifies that a custom catalog ID provided to an agent is correctly exposed within the A2UI extension parameters. It initializes an agent with a specific `$id` and then asserts this ID is present in the `supportedCatalogIds` list returned by the server's card capabilities.*


### test_non_a2ui_agent_no_extension (method, L237-L251, parent: TestAgentCardAutoDetection)

> *Summary: This test verifies that a standard `ConversableAgent` instance, when wrapped by an `A2aAgentServer`, does not automatically receive any A2UI extensions. It asserts that the list of capabilities attached to the server's card contains zero extensions matching "a2ui".*


### test_executor_type_for_a2ui_agent (method, L253-L264, parent: TestAgentCardAutoDetection)

> *Summary: This test verifies that when an `A2UIAgent` is passed to the `A2aAgentServer`, the server's internal executor property correctly resolves to an instance of `A2UIAgentExecutor`. It confirms the expected type linkage between the agent and its serving mechanism.*


### test_executor_type_for_regular_agent (method, L266-L278, parent: TestAgentCardAutoDetection)

> *Summary: This test verifies that an `A2aAgentServer` initialized with a standard `ConversableAgent` uses the default executor type instead of the specialized `A2UIAgentExecutor`. It asserts that the server's internal executor is not an instance of `A2UIAgentExecutor`.*


### test_no_duplicate_extension_if_manually_added (method, L280-L305, parent: TestAgentCardAutoDetection)

> *Summary: Verifies that an agent's card does not contain duplicate instances of a specific extension URI when it is manually provided during server initialization. It initializes an `A2UIAgent` and `A2aAgentServer` with pre-defined extensions, then asserts the resulting list contains exactly one instance of the target extension.*

