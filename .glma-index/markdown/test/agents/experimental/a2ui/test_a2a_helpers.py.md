# test/agents/experimental/a2ui/test_a2a_helpers.py

2 class(es): TestA2UIPartHelpers, TestA2UIExtension. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestA2UIPartHelpers | class |  |
| TestA2UIExtension | class |  |

## Chunks

### TestA2UIPartHelpers (class, L20-L82)

> *Summary: This test suite verifies helper functions for creating and inspecting A2UI parts. It confirms that a single dictionary input correctly generates a `DataPart`, while a list of dictionaries yields a list of corresponding parts, and it validates the logic for identifying and extracting `DataPart` instances from generic part objects.*


### test_create_a2ui_part_single_dict (method, L21-L31, parent: TestA2UIPartHelpers)

> *Summary: This test verifies that the `create_a2ui_part` function correctly constructs a data part when provided with a single dictionary input. It asserts that the resulting object contains the original data in its root and includes expected metadata, such as the defined MIME type.*


### test_create_a2ui_part_list (method, L33-L48, parent: TestA2UIPartHelpers)

> *Summary: This test verifies that the `create_a2ui_part` function correctly processes a list of operations (containing surface creation and deletion requests). It asserts that the output is a list where each element contains a `DataPart` mirroring one of the input operations.*


### test_is_a2ui_part_true (method, L50-L52, parent: TestA2UIPartHelpers)

> *Summary: This test verifies that an object created using `create_a2ui_part` correctly returns `True` when passed to the `is_a2ui_part` function. It uses a simple dictionary input to construct and validate the resulting part structure.*


### test_is_a2ui_part_false_wrong_mime (method, L54-L58, parent: TestA2UIPartHelpers)

> *Summary: This test verifies that a `Part` object containing data with an incorrect MIME type fails the `is_a2ui_part` check. It asserts that the function returns `False` when provided such a part instance.*


### test_is_a2ui_part_false_no_metadata (method, L60-L64, parent: TestA2UIPartHelpers)

> *Summary: When provided with a `Part` object containing data but no associated metadata, the function correctly asserts that it does not qualify as an A2UI part. This test verifies the logic for identifying A2UI parts based on the presence of metadata.*


### test_is_a2ui_part_false_text_part (method, L66-L70, parent: TestA2UIPartHelpers)

> *Summary: This test verifies that a `Part` containing only a `TextPart` evaluates to `False` when passed to the `is_a2ui_part` function. It asserts this behavior using an instantiated `Part` object constructed with a text-only component.*


### test_get_a2ui_datapart_present (method, L72-L76, parent: TestA2UIPartHelpers)

> *Summary: This test verifies that the `get_a2ui_datapart` function correctly extracts data from a created A2UI part. It asserts that the returned datapart is not null and contains the expected input data structure.*


### test_get_a2ui_datapart_absent (method, L78-L82, parent: TestA2UIPartHelpers)

> *Summary: This test verifies that the `get_a2ui_datapart` function returns `None` when provided with a `Part` structure containing only text. It asserts this behavior using a simple `TextPart` as input.*


### TestA2UIExtension (class, L85-L162)

> *Summary: This test suite verifies the behavior of A2UI extension handling by asserting correct URI versions, default and parameterized extension retrieval, and activation logic. It uses mock contexts to test scenarios like successful/failed activation based on requested extensions, version mismatches, or empty requests.*


### test_extension_uri_is_v09 (method, L86-L87, parent: TestA2UIExtension)

> *Summary: This test asserts that the `A2UI_EXTENSION_URI` string contains the version identifier "v0.9". It verifies a specific expected format within a configuration URI.*


### test_get_agent_extension_default (method, L89-L93, parent: TestA2UIExtension)

> *Summary: This test verifies the default agent extension returned by `get_a2ui_agent_extension()`. It asserts that the returned object has a specific URI, contains "A2UI" in its description, and has no parameters.*


### test_get_agent_extension_with_inline_catalog (method, L95-L98, parent: TestA2UIExtension)

> *Summary: This test verifies that when requesting an agent extension with inline catalog support enabled, the returned extension object correctly contains a `params` dictionary where `acceptsInlineCustomCatalog` is set to `True`.*


### test_try_activate_success (method, L100-L109, parent: TestA2UIExtension)

> *Summary: This test verifies successful activation of an extension by simulating a context containing the target URI. It asserts that the activation function returns `True` and that the extension URI is present in the context's metadata upon completion.*


### test_try_activate_not_requested (method, L111-L120, parent: TestA2UIExtension)

> *Summary: When called without prior extension requests, this test verifies that the activation function returns `False` and does not modify the context's metadata with any activated extensions. It simulates a scenario where no extensions were explicitly requested for activation.*


### test_try_activate_wrong_version_uri (method, L122-L134, parent: TestA2UIExtension)

> *Summary: When provided a context requesting an unsupported A2UI version (e.g., v1.0 when only v0.9 is available), the function returns `False` and ensures no extensions are recorded as activated in the context's metadata.*


### test_try_activate_multiple_extensions_only_a2ui_activated (method, L136-L150, parent: TestA2UIExtension)

> *Summary: When provided with a context requesting multiple extensions, this test verifies that the activation function only activates the specific A2UI extension URI. It asserts that the returned result is `True` and that the metadata confirms only the intended A2UI extension was activated.*


### test_try_activate_empty_extensions (method, L152-L162, parent: TestA2UIExtension)

> *Summary: When called with a context containing no requested extensions, the function returns `False`. This test verifies that attempting to activate extensions when none are provided results in failure.*

