# test/events/test_base_event.py

1 function(s): TestEvent. 1 class(es): TestBaseEvent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestEvent | function |  |
| TestBaseEvent | class |  |

## Chunks

### TestEvent (function, L19-L32)

> *Summary: This generator dynamically creates and yields a `TestEvent` class inheriting from `BaseEvent`, which includes sender, receiver, and content attributes. It manages the global registry of event classes by temporarily adding the new type and restoring the original state upon completion.*


### TestBaseEvent (class, L35-L73)

> *Summary: This test suite verifies the serialization and deserialization logic for event models, ensuring that instances created with specific inputs correctly map to a predefined dictionary structure via `model_dump()` and can be accurately reconstructed using `model_validate()` or direct instantiation. It specifically tests both general event structures and those with simplified content parameters.*


### test_model_dump_validate (method, L36-L57, parent: TestBaseEvent)

> *Summary: This test verifies the serialization and deserialization capabilities of a `BaseModel` event type using its `model_dump()` and `model_validate()` methods. It confirms that an instance created from known data matches the expected dictionary structure, and conversely, that reconstructing the model from the expected dictionary yields the same result.*


### test_single_content_parameter_event (method, L59-L73, parent: TestBaseEvent)

> *Summary: This test verifies the serialization and deserialization of an event containing a single string content parameter. It confirms that creating, validating from a dictionary, and instantiating the event all result in the expected structured output.*

