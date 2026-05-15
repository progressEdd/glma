# test/beta/events/test_tool_events.py

4 class(es): TestClientToolCallEventFromCall, TestToolErrorEventContent, TestSerializedArgumentsCache, TestSerializedArgumentsEmptyInput. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestClientToolCallEventFromCall | class |  |
| TestToolErrorEventContent | class |  |
| TestSerializedArgumentsCache | class |  |
| TestSerializedArgumentsEmptyInput | class |  |

## Chunks

### TestClientToolCallEventFromCall (class, L15-L27)

> *Summary: This test suite verifies that a `ClientToolCallEvent` correctly mirrors the data from an input `ToolCallEvent`. It confirms that the event's ID, name, and arguments are accurately preserved when converting from the original call object.*


### test_parent_id_matches_original_id (method, L18-L21, parent: TestClientToolCallEventFromCall)

> *Summary: This test verifies that the `id` of a `ToolCallEvent` is preserved when converted to a `ClientToolCallEvent`. It takes an initial event and asserts its ID matches the resulting client-side event's ID.*


### test_name_and_arguments_preserved (method, L23-L27, parent: TestClientToolCallEventFromCall)

> *Summary: Verifies that when converting a `ToolCallEvent` to a `ClientToolCallEvent`, the event's name and arguments are correctly preserved in the resulting object. It takes an initial `ToolCallEvent` as input and asserts equality against its converted counterpart.*


### TestToolErrorEventContent (class, L30-L51)

> *Summary: This class contains unit tests verifying that `ToolErrorEvent` correctly captures the original exception details when created from a tool call and an error. It asserts that the resulting event content includes the specific error type and message, while also ensuring no unexpected `NoneType` appears in the output.*


### test_content_contains_original_error (method, L33-L42, parent: TestToolErrorEventContent)

> *Summary: This test verifies that a `ToolErrorEvent` correctly captures the original exception details when an error occurs during tool execution. It asserts that the resulting event's content string contains both the exception type ("ValueError") and its specific message ("test error message").*


### test_content_does_not_return_none_type (method, L44-L51, parent: TestToolErrorEventContent)

> *Summary: This test verifies that the resulting content from a `ToolErrorEvent` does not contain `"NoneType"` when an exception occurs during tool execution. It simulates a runtime error and checks the structure of the generated event's output.*


### TestSerializedArgumentsCache (class, L54-L71)

> *Summary: This test suite verifies that the `serialized_arguments` property correctly caches deserialized JSON arguments from a `ToolCallEvent`. It asserts that both empty and non-empty dictionary inputs are parsed once and subsequently returned from the cached property.*


### test_empty_dict_is_cached (method, L57-L63, parent: TestSerializedArgumentsCache)

> *Summary: When an event is initialized with empty JSON arguments, the serialization process should load it as an empty dictionary. This test verifies that `json.loads` is called exactly once and returns `{}` for the serialized arguments.*


### test_non_empty_dict_is_cached (method, L65-L71, parent: TestSerializedArgumentsCache)

> *Summary: This test verifies that when a `ToolCallEvent` contains non-empty arguments, the serialization process correctly parses and caches the dictionary content. It asserts that the underlying JSON parsing function is called exactly once during this operation.*


### TestSerializedArgumentsEmptyInput (class, L74-L94)

> *Summary: Verifies that an event's serialized arguments correctly handle empty strings and `None` by returning an empty dictionary, and also tests the setter functionality to ensure argument updates are cached properly. It confirms that when initialized with a JSON string, the arguments are parsed into a dictionary.*


### test_empty_string_returns_empty_dict (method, L77-L79, parent: TestSerializedArgumentsEmptyInput)

> *Summary: When provided with an empty string as input for the arguments, this test asserts that the resulting serialized arguments dictionary is empty. It verifies the correct serialization behavior of a `ToolCallEvent` when no arguments are present.*


### test_none_returns_empty_dict (method, L81-L83, parent: TestSerializedArgumentsEmptyInput)

> *Summary: When provided with `None` for its arguments, the event serialization method returns an empty dictionary. This test verifies that a `ToolCallEvent` initialized with null arguments correctly serializes to `{}`.*


### test_setter_updates_cache (method, L85-L94, parent: TestSerializedArgumentsEmptyInput)

> *Summary: This test verifies that updating the `serialized_arguments` attribute on a `ToolCallEvent` correctly reflects the new data structure. It asserts that after modification, the internal state matches the input and confirms that JSON deserialization was called exactly once during the process.*

