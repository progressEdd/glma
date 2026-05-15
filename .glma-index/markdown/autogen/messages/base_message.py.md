# autogen/messages/base_message.py

4 function(s): camel2snake, wrap_message, get_annotated_type_for_message_classes, get_message_classes. 1 class(es): BaseMessage. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BaseMessage | class |  |
| camel2snake | function |  |
| wrap_message | function |  |
| get_annotated_type_for_message_classes | function |  |
| get_message_classes | function |  |

## Chunks

### BaseMessage (class, L21-L40)

> *Summary: Provides a foundational structure for messages, automatically assigning a unique UUID if one is not provided during initialization. It also includes a method to output the message content using an optional custom printing function.*


### __init__ (method, L24-L32, parent: BaseMessage)

> *Summary: Initializes a base message by assigning it a unique UUID if one is not provided; otherwise, it uses the supplied identifier and passes any extra keyword arguments up to the parent class.*


### print (method, L34-L40, parent: BaseMessage)

> *Summary: This method outputs the message content using a specified callable or Python's default `print` if none is provided. It accepts an optional printing function as input and returns nothing upon execution.*


### camel2snake (function, L43-L44)

> *Summary: Converts a string from CamelCase to snake_case by inserting underscores before uppercase letters and converting them to lowercase. It removes any leading underscore that might result from the conversion.*


### wrap_message (function, L51-L97)

> *Summary: Transforms a given message class into a new model that includes a `type` field for union serialization. It takes a message class as input and returns a dynamically created subclass of `BaseModel`, ensuring proper handling during instantiation to wrap the original content.*


### get_annotated_type_for_message_classes (function, L101-L104)

> *Summary: Constructs a dynamic union type from all defined message classes and wraps it with an `Annotated` wrapper that uses a "type" field as a discriminator. This resulting type is intended for use in schema definitions to allow polymorphic handling of various message types.*


### get_message_classes (function, L107-L108)

> *Summary: Returns a dictionary mapping string identifiers to their corresponding `BaseModel` types. This acts as a registry for all defined message classes within the system.*

