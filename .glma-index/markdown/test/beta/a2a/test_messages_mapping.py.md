# test/beta/a2a/test_messages_mapping.py

1 class(es): TestExtraMetadata. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestExtraMetadata | class |  |

## Chunks

### TestExtraMetadata (class, L11-L40)

> *Summary: This test suite verifies how extra metadata and context updates are merged into a user message object when constructing it. It asserts correct extraction of both the `context_update` dictionary and the `extra_metadata` from the resulting message, handling cases with collisions and empty inputs.*


### test_extra_metadata_merged_alongside_context_update (method, L12-L20, parent: TestExtraMetadata)

> *Summary: This test verifies that extra metadata is correctly merged into a message alongside context updates. It asserts that the extracted context update matches the input and that the specified trace ID is present in the message's metadata.*


### test_extra_metadata_alone (method, L22-L26, parent: TestExtraMetadata)

> *Summary: Verifies that when a user message is constructed with only extra metadata, the resulting message's metadata correctly contains that data, and no context updates are extracted from it.*


### test_ag2_keys_win_on_collision (method, L28-L35, parent: TestExtraMetadata)

> *Summary: This test verifies that when a message is built with specific context update metadata, the extraction function correctly retrieves the intended `"real": True` value from the resulting message object. It confirms proper handling of context updates during message construction.*


### test_no_metadata_when_both_empty (method, L37-L40, parent: TestExtraMetadata)

> *Summary: When a user message is constructed with only text input and no other data, the resulting message object should lack any metadata field. This test verifies that empty inputs correctly result in an absence of metadata.*

