# autogen/beta/events/base.py

2 function(s): truncate_repr, _process_fields. 3 class(es): Field, _ConditionMeta, BaseEvent. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| truncate_repr | function |  |
| Field | class |  |
| _ConditionMeta | class |  |
| _process_fields | function |  |
| BaseEvent | class |  |

## Chunks

### truncate_repr (function, L25-L38)

> *Summary: This utility truncates the string representation of `str` or `bytes` inputs if their resulting `repr` exceeds a specified maximum length. It returns a shortened version appended with an ellipsis and the original value's length to maintain context in logs.*


### Field (class, L41-L97)

> *Summary: This class acts as a descriptor for defining fields within an event structure, allowing configuration of default values and behavior like comparison or hashing. It manages attribute access on instances, providing getter/setter logic while enabling rich comparison operations based on the field's name.*


### __init__ (method, L42-L62, parent: Field)

> *Summary: Initializes an event structure by setting configuration flags like `init`, `repr`, and `compare`. It stores the provided default value or factory function for use in defining event properties.*


### get_default (method, L64-L67, parent: Field)

> *Summary: Retrieves a default value for the object, either by calling a specified factory function if one exists, or by returning a pre-set default attribute.*


### __get__ (method, L69-L73, parent: Field)

> *Summary: This descriptor method sets the owning class on itself and returns either the descriptor object itself (when accessed on the class) or the specific attribute value from the instance's dictionary (when accessed on an instance). It facilitates dynamic retrieval of event-related attributes bound to a class structure.*


### __set__ (method, L75-L76, parent: Field)

> *Summary: This method sets an attribute on an object by storing the provided `value` directly into the instance's internal dictionary using the attribute's name as the key. It acts as a descriptor setter, allowing custom control over how attributes are assigned.*


### __eq__ (method, L78-L79, parent: Field)

> *Summary: Compares the current object to another input by constructing an `OpCondition` using an equality check (`check_eq`), the object's name, the provided `other`, and its event class. This method returns a specific condition object based on the comparison logic.*


### __ne__ (method, L81-L82, parent: Field)

> *Summary: When comparing an instance to another object, this method generates a `Condition` object representing the "not equal" comparison using the operator's inequality function. It takes any comparable object as input and returns a structured condition for evaluation.*


### __lt__ (method, L84-L85, parent: Field)

> *Summary: Compares the current event instance to another object by creating a `Condition` object that represents "less than" using the operator and relevant event details. This method facilitates ordering or comparison logic between events.*


### __le__ (method, L87-L88, parent: Field)

> *Summary: This method checks if the current event is less than or equal to another provided object by constructing a comparison condition using `operator.le`. It returns an `OpCondition` instance containing the operator, names of both events, and the class of the current event.*


### __gt__ (method, L90-L91, parent: Field)

> *Summary: Compares the current event against another object to determine if it is strictly greater than. It returns a `Condition` object specifying the "greater than" operator using the event's name and class.*


### __ge__ (method, L93-L94, parent: Field)

> *Summary: This method checks if the current event is greater than or equal to another provided object by constructing a `Condition` object using the "greater than or equal to" operator. It takes any comparable object as input and returns a structured condition for comparison.*


### is_ (method, L96-L97, parent: Field)

> *Summary: Checks if the current event's name matches another provided object's name and returns a `Condition` object representing this equality check. This method takes any object as input and outputs a structured condition for comparison.*


### _ConditionMeta (class, L100-L114)

> *Summary: This metaclass injects class-level operators (`|`, `or_`, `not_`) that allow defining logical conditions on classes. When a class is created, it processes its fields to enable these condition checks against other types or conditions.*


### __init__ (method, L103-L105, parent: _ConditionMeta)

> *Summary: Initializes a class by calling the parent constructor and then processes its fields using an internal helper function. This sets up the class structure based on provided name, base classes, and namespace dictionary.*


### __or__ (method, L107-L108, parent: _ConditionMeta)

> *Summary: This method combines two type conditions using a logical OR operation. It takes another `Any` object and returns a new `TypeCondition` that matches if either the current class or the provided `other` condition is met.*


### or_ (method, L110-L111, parent: _ConditionMeta)

> *Summary: Combines two condition types using a logical OR operation. It takes a class type and another condition object as input to return a new `OrCondition`.*


### not_ (method, L113-L114, parent: _ConditionMeta)

> *Summary: Creates a `NotCondition` instance by wrapping a given class type within a `TypeCondition`. This allows for negation logic based on the input class.*


### _process_fields (function, L117-L144)

> *Summary: This function inspects a class's annotations to dynamically create and attach `Field` descriptors for each defined attribute. It handles both standard and modern Python annotation retrieval methods to populate the class with structured field metadata.*


### BaseEvent (class, L151-L245)

> *Summary: Provides a base structure for events, automatically injecting a creation timestamp and handling initialization by merging positional arguments with field defaults from the class hierarchy. It supports serialization to dictionaries (`to_dict`) and reconstruction from them (`from_dict`), while equality checks respect configured comparison fields.*


### __init__ (method, L165-L200, parent: BaseEvent)

> *Summary: This method initializes an event object by introspecting its class hierarchy to determine expected positional arguments and default values from defined fields. It then validates the provided `args` and `kwargs`, applies defaults first, followed by user-supplied keyword arguments, ensuring proper attribute setting order.*


### __eq__ (method, L202-L211, parent: BaseEvent)

> *Summary: Compares two instances of the same event type by iterating through defined fields; it returns `True` only if all comparable fields match between both objects.*


### __repr__ (method, L213-L223, parent: BaseEvent)

> *Summary: Generates a developer-friendly string representation of the event object by including all public attributes while omitting fields marked as non-representable within its class hierarchy. This method inspects the object's type and instance dictionary to construct the output string.*


### to_dict (method, L225-L227, parent: BaseEvent)

> *Summary: Converts the current event instance into a standard Python dictionary suitable for serialization. It delegates the actual conversion logic to an external helper function.*


### from_dict (method, L230-L245, parent: BaseEvent)

> *Summary: Reconstructs an event instance from a dictionary by first deserializing nested payloads and then filtering the input to include only fields defined within the class's inheritance hierarchy before instantiation. This ensures that unknown or extraneous data is ignored during object creation.*

