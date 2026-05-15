# test/test_json_utils.py

3 function(s): test_resolve_json_references_no_refs, test_resolve_json_references_with_refs, test_resolve_json_references_invalid_ref.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_resolve_json_references_no_refs | function |  |
| test_resolve_json_references_with_refs | function |  |
| test_resolve_json_references_invalid_ref | function |  |

## Chunks

### test_resolve_json_references_no_refs (function, L11-L14)

> *Summary: When provided with a JSON schema containing no internal references, this test asserts that the resolution function returns the input schema unchanged. It verifies the behavior of `resolve_json_references` on a simple, self-contained structure.*


### test_resolve_json_references_with_refs (function, L17-L36)

> *Summary: This test verifies that a JSON schema containing internal `$ref` pointers is correctly expanded. It takes a schema with a reference to a definition and asserts the output matches the fully resolved structure.*


### test_resolve_json_references_invalid_ref (function, L39-L48)

> *Summary: This test verifies that attempting to resolve a JSON schema containing an invalid reference path raises the expected `_RefResolutionError`. It passes a schema where the `"address"` property points to a non-existent definition.*

