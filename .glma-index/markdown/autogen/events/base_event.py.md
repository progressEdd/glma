# autogen/events/base_event.py

5 function(s): resolve_print_callable, camel2snake, wrap_event, get_annotated_type_for_event_classes, get_event_classes. 1 class(es): BaseEvent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BaseEvent | class |  |
| resolve_print_callable | function |  |
| camel2snake | function |  |
| wrap_event | function |  |
| get_annotated_type_for_event_classes | function |  |
| get_event_classes | function |  |

## Chunks

### BaseEvent (class, L26-L39)

> *Summary: This abstract base class defines a structure for events, ensuring every instance has a unique UUID upon initialization. It provides a `print` method to serialize and output the event data using an optional custom printing function.*


### __init__ (method, L29-L31, parent: BaseEvent)

> *Summary: Initializes an event by assigning a unique identifier; if no `uuid` is provided, it automatically generates one using `uuid4()` before calling the parent constructor.*


### print (method, L33-L39, parent: BaseEvent)

> *Summary: This method outputs the event information using a provided callable or Python's standard `print` if no function is supplied. It accepts an optional printing function as input and returns nothing.*


### resolve_print_callable (function, L42-L43)

> *Summary: If a callable function is provided, it returns that function; otherwise, it defaults to the `event_print` mechanism. This ensures a printing method is always available for event handling.*


### camel2snake (function, L46-L47)

> *Summary: Converts a string from camelCase to snake_case by inserting underscores before uppercase letters and converting them to lowercase. It takes one string input and returns the transformed snake_case string.*


### wrap_event (function, L54-L100)

> *Summary: Transforms an input event class into a new model that includes a `type` field for serialization within union types. It dynamically creates and returns this wrapped class, ensuring the original class's metadata is preserved while adapting its initialization logic to handle the added type structure.*


### get_annotated_type_for_event_classes (function, L104-L107)

> *Summary: Constructs a dynamic union type from all defined event classes and wraps it with an `Annotated` type using a specific discriminator field. This allows the system to identify the concrete event type at runtime based on this annotation.*


### get_event_classes (function, L110-L111)

> *Summary: Returns a dictionary mapping string names to their corresponding `BaseModel` types from an internal registry. This provides a centralized way to access all defined event classes.*

