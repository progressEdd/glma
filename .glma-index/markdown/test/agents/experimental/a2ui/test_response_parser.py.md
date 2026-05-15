# test/agents/experimental/a2ui/test_response_parser.py

6 class(es): TestA2UIResponseParser, TestA2UIResponseParserValidation, TestPerComponentValidation, TestFormatValidationError, TestStripMarkdownFences, TestParseWithMarkdownFences. 31 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestA2UIResponseParser | class |  |
| TestA2UIResponseParserValidation | class |  |
| TestPerComponentValidation | class |  |
| TestFormatValidationError | class |  |
| TestStripMarkdownFences | class |  |
| TestParseWithMarkdownFences | class |  |

## Chunks

### TestA2UIResponseParser (class, L10-L84)

> *Summary: This test suite verifies the `A2UIResponseParser`'s ability to extract structured operations from a response string, handling cases with and without A2UI data. It validates parsing logic for various inputs, including plain text, single/multiple JSON objects, custom delimiters, and error conditions like invalid or malformed JSON.*


### test_parse_no_a2ui (method, L11-L17, parent: TestA2UIResponseParser)

> *Summary: When provided with plain text input, the parser successfully extracts the content into the `text` field while confirming no A2UI operations were found and reporting no parsing errors. The function verifies that the output structure accurately reflects a non-A2UI response.*


### test_parse_with_a2ui (method, L19-L31, parent: TestA2UIResponseParser)

> *Summary: This test verifies the `A2UIResponseParser` correctly processes a response string containing both plain text and embedded A2UI JSON data. It asserts that the parser extracts the initial text, identifies the presence of A2UI content, and accurately parses the structure of the contained operations.*


### test_parse_single_object (method, L33-L40, parent: TestA2UIResponseParser)

> *Summary: This test verifies that the parser correctly extracts a single JSON object from a response string containing both UI text and structured data. It asserts that the resulting parsed object indicates A2UI presence and contains exactly one operation.*


### test_parse_invalid_json (method, L42-L49, parent: TestA2UIResponseParser)

> *Summary: When provided with a response containing malformed JSON, the parser correctly identifies the presence of A2UI data while reporting a specific parsing error for the invalid structure. The output confirms that no operations were successfully extracted due to the input's corruption.*


### test_parse_non_array_non_object (method, L51-L58, parent: TestA2UIResponseParser)

> *Summary: When provided with a response string containing only plain text and not valid JSON, the parser successfully identifies the presence of A2UI data but reports a parsing error indicating that it expected an array or object structure within the JSON block. The output confirms this by setting `has_a2ui` to true while leaving operations empty and populating the `parse_error`.*


### test_parse_empty_after_delimiter (method, L60-L64, parent: TestA2UIResponseParser)

> *Summary: When provided with a string ending in a delimiter, this test verifies that the response parser correctly identifies no embedded A2UI JSON data and returns only the preceding text content. The input is a string containing text followed by a newline and the delimiter; the output confirms the absence of A2UI structure and retains the initial text.*


### test_parse_custom_delimiter (method, L66-L71, parent: TestA2UIResponseParser)

> *Summary: This test verifies that the response parser correctly processes a string using a custom delimiter (`<<<A2UI>>>`). It asserts that the resulting parsed object indicates A2UI presence and contains exactly one operation.*


### test_parse_multiple_operations (method, L73-L84, parent: TestA2UIResponseParser)

> *Summary: This test verifies that the response parser correctly extracts and separates multiple distinct operations from a single string input containing JSON data. It asserts that two specific operations, `createSurface` and `updateComponents`, are successfully parsed into the resulting structure.*


### TestA2UIResponseParserValidation (class, L87-L147)

> *Summary: This test suite validates the `A2UIResponseParser` by feeding it various operation lists, such as valid and invalid requests for creating or deleting surfaces. It asserts that the parser correctly returns a valid status (`is_valid=True`) when inputs conform to the schema, and reports specific errors when required fields are missing or the version is absent.*


### parser_with_schema (method, L89-L96, parent: TestA2UIResponseParserValidation)

> *Summary: Instantiates and returns a configured response parser object by initializing an `A2UISchemaManager` to provide the necessary server-to-client schema for version "v0.9". This method prepares the parser with its required structural definitions before returning it.*


### test_validate_valid_create_surface (method, L98-L110, parent: TestA2UIResponseParserValidation)

> *Summary: This test verifies that a provided response parser correctly validates an operation list containing a valid `createSurface` request. It asserts that the validation process returns a result indicating both validity and no errors for the input structure.*


### test_validate_valid_delete_surface (method, L112-L115, parent: TestA2UIResponseParserValidation)

> *Summary: This test verifies that a list containing a valid delete surface operation, specified with version and `surfaceId`, passes validation when processed by the provided response parser. It asserts that the resulting validation object indicates success (`is_valid` is True).*


### test_validate_missing_version (method, L117-L121, parent: TestA2UIResponseParserValidation)

> *Summary: When provided with operations lacking a required version field, the validation process returns an invalid state containing exactly one error. This test confirms that missing version information correctly triggers a validation failure in the parser.*


### test_validate_missing_required_field (method, L123-L126, parent: TestA2UIResponseParserValidation)

> *Summary: When provided with operations lacking a required field, the validation process returns an invalid state. This test confirms that the parser correctly identifies and flags missing mandatory data within the input structure.*


### test_validate_no_schema_always_valid (method, L128-L131, parent: TestA2UIResponseParserValidation)

> *Summary: When initialized without a schema, this test confirms that the response parser always deems any input data as valid. It passes a list containing a dictionary to verify this behavior.*


### test_validate_multiple_ops_one_invalid (method, L133-L147, parent: TestA2UIResponseParserValidation)

> *Summary: When provided with a list of operations containing one invalid entry, the parser validates them and returns an object indicating overall failure with exactly one error detailing the issue in the second operation.*


### TestPerComponentValidation (class, L150-L241)

> *Summary: This test suite validates the error handling of component updates by feeding it JSON operations containing `updateComponents`. It asserts that invalid structures, such as using `text` instead of `child` for a Button or missing required properties, correctly generate specific, actionable errors within the validation result. Conversely, it confirms that properly structured components pass validation successfully.*


### parser_with_components (method, L154-L164, parent: TestPerComponentValidation)

> *Summary: This method constructs and returns a fully configured `A2UIResponseParser` instance by initializing an `A2UISchemaManager`. It populates the parser with necessary schemas, component definitions, and catalog IDs retrieved from the manager.*


### test_button_missing_child_gives_actionable_error (method, L166-L186, parent: TestPerComponentValidation)

> *Summary: When provided with an operation containing a Button component that uses a `text` field instead of the expected `child`, the parser should return an invalid state containing an error message specifically referencing both the button ID and the component type. This test verifies that structural errors are reported clearly to the developer.*


### test_valid_button_with_child_passes (method, L188-L212, parent: TestPerComponentValidation)

> *Summary: This test verifies that a response structure containing a `Button` component with a child reference to a `Text` component passes validation. It feeds the structured operations into the provided parser and asserts that the resulting validation status indicates success.*


### test_multiple_component_errors (method, L214-L241, parent: TestPerComponentValidation)

> *Summary: This test verifies that an input containing multiple invalid components results in distinct errors being reported by the parser. It asserts that when provided with operations having two flawed components, the resulting validation object indicates failure and contains at least two specific error messages corresponding to each faulty component.*


### TestFormatValidationError (class, L244-L277)

> *Summary: This test suite verifies the `A2UIResponseParser`'s ability to generate structured feedback based on parsing and validation results. It asserts that the generated feedback correctly incorporates specific errors (like missing required properties or JSON parsing failures) and includes version hints when necessary.*


### test_format_with_validation_errors (method, L245-L257, parent: TestFormatValidationError)

> *Summary: This test verifies that the response parser correctly formats an output when both parsing and validation fail. It takes a parsed result and a validation result containing specific errors to generate a feedback string that includes error details and instructions for correction.*


### test_format_with_parse_error (method, L259-L268, parent: TestFormatValidationError)

> *Summary: This test verifies that the response parser correctly generates feedback when a parse error is present. It takes a `A2UIParseResult` containing an error and a `A2UIValidationResult`, then asserts the resulting feedback string includes the expected error message.*


### test_format_includes_version_hint (method, L270-L277, parent: TestFormatValidationError)

> *Summary: This test verifies that the response formatter correctly embeds a specified version hint into its output when provided with parsing and validation results. It asserts that the generated feedback string contains the expected version string ("v0.9").*


### TestStripMarkdownFences (class, L280-L301)

> *Summary: This test suite verifies the `strip_markdown_fences` function's ability to correctly extract content from markdown code blocks. It tests various scenarios, including JSON-specific fences, plain fences, edge cases like missing newlines or surrounding whitespace, and empty inputs.*


### test_no_fences (method, L281-L282, parent: TestStripMarkdownFences)

> *Summary: Verifies that the `strip_markdown_fences` function correctly returns the input string unchanged when no markdown fences are present. It asserts equality between the original JSON-like string and the output of the stripping operation.*


### test_json_fence (method, L284-L285, parent: TestStripMarkdownFences)

> *Summary: This test verifies that the `strip_markdown_fences` function correctly removes surrounding markdown code fences (specifically JSON fences) from a string input, returning only the inner content.*


### test_plain_fence (method, L287-L288, parent: TestStripMarkdownFences)

> *Summary: Asserts that stripping markdown fences from a string containing JSON results in the clean JSON content. The input is a string with surrounding triple backticks, and the expected output is the inner JSON object as a string.*


### test_fence_no_newline (method, L290-L292, parent: TestStripMarkdownFences)

> *Summary: Verifies that the markdown fence stripping function correctly handles an opening code block delimiter immediately followed by content without a preceding newline. It asserts that the input string, ````{"key": "value"}````, is parsed to return only the inner JSON object.*


### test_whitespace_around_fences (method, L294-L295, parent: TestStripMarkdownFences)

> *Summary: This test verifies that the `strip_markdown_fences` function correctly removes surrounding whitespace and markdown fences from a string containing JSON data. It asserts that input with leading/trailing spaces around the code block results in only the inner content being returned.*


### test_empty_string (method, L297-L298, parent: TestStripMarkdownFences)

> *Summary: Verifies that stripping markdown fences from an empty string correctly returns an empty string. This test confirms the parser handles null or zero-length input gracefully.*


### test_only_fences (method, L300-L301, parent: TestStripMarkdownFences)

> *Summary: Asserts that stripping markdown fences from a string containing only JSON fence markers results in an empty string. This tests the core functionality of the `strip_markdown_fences` utility.*


### TestParseWithMarkdownFences (class, L304-L324)

> *Summary: This test suite verifies that the response parser correctly extracts and processes JSON content embedded within markdown fences, regardless of whether the fence uses a specific language identifier or not. It confirms successful parsing by asserting the presence of A2UI data and the correct number of operations in the output result.*


### test_parse_json_wrapped_in_fences (method, L307-L316, parent: TestParseWithMarkdownFences)

> *Summary: This test verifies that the response parser correctly extracts JSON data when it is wrapped within markdown fences in a larger string input. It asserts that the resulting object indicates successful parsing and contains exactly one operation from the extracted JSON.*


### test_parse_plain_fence (method, L318-L324, parent: TestParseWithMarkdownFences)

> *Summary: This test verifies the parsing of a plain fence-delimited response string, expecting the parser to successfully extract one operation from the embedded JSON structure. It confirms that the resulting object indicates A2UI presence and contains exactly one parsed operation without any errors.*

