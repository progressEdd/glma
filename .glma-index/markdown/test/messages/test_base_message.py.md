# test/messages/test_base_message.py

1 function(s): TestMessage. 1 class(es): TestBaseMessage. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestMessage | function |  |
| TestBaseMessage | class |  |

## Chunks

### TestMessage (function, L19-L32)

> *Summary: This function dynamically creates and yields a test message class inheriting from `BaseMessage`, injecting it into the global message registry for testing purposes. It ensures that the original state of the message classes is restored after the test execution completes.*


### TestBaseMessage (class, L35-L73)

> *Summary: This test suite verifies the serialization and deserialization logic for base message models. It asserts that instances created with specific inputs correctly serialize to a predefined dictionary structure, and conversely, that dictionaries can be successfully validated into message objects.*


### test_model_dump_validate (method, L36-L57, parent: TestBaseMessage)

> *Summary: This test verifies that a message model correctly serializes to and deserializes from a dictionary structure. It confirms consistency by comparing the output of `model_dump()` against an expected dictionary, and also validates reconstruction using both `model_validate` and direct keyword argument instantiation.*


### test_single_content_parameter_message (method, L59-L73, parent: TestBaseMessage)

> *Summary: This test verifies the serialization and deserialization of a message containing only a single string content parameter. It asserts that creating, validating from a dictionary, and instantiating the message all result in the expected structured output.*

