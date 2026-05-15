# autogen/beta/events/conditions.py

1 function(s): check_eq. 6 class(es): Condition, TypeCondition, AndCondition, OrCondition, NotCondition, OpCondition. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Condition | class |  |
| TypeCondition | class |  |
| AndCondition | class |  |
| OrCondition | class |  |
| NotCondition | class |  |
| OpCondition | class |  |
| check_eq | function |  |

## Chunks

### Condition (class, L13-L38)

> *Summary: Defines an abstract base class for event conditions that must implement a callable method to evaluate against an event and return a boolean. It provides overloaded operators (`&`, `|`, `~`) to allow chaining multiple conditions together using logical AND, OR, and NOT operations.*


### __call__ (method, L15-L16, parent: Condition)

> *Summary: This method requires subclasses to implement logic that accepts an `event` object and returns a boolean indicating whether the condition is met. It serves as a contract for defining custom event-based checks.*


### __and__ (method, L18-L19, parent: Condition)

> *Summary: This method implements the logical AND operation between an instance and another object. It delegates the actual combination logic to the `and_` method, returning a new `AndCondition`.*


### and_ (method, L21-L24, parent: Condition)

> *Summary: Combines the current condition with another input by creating a new `AndCondition`. It ensures the provided `other` object is treated as a `Condition`, converting it to a `TypeCondition` if necessary.*


### __or__ (method, L26-L27, parent: Condition)

> *Summary: This method implements the logical OR operation between an existing condition object and another provided condition. It delegates the actual combination logic to the `or_` helper method, returning a new composite `OrCondition`.*


### or_ (method, L29-L32, parent: Condition)

> *Summary: Combines the current condition with another by creating a new `OrCondition`. It ensures the input is a `Condition` object, converting it to a `TypeCondition` if necessary before combining.*


### __invert__ (method, L34-L35, parent: Condition)

> *Summary: When called on a condition object, this method inverts its logic by returning a new `NotCondition` instance that represents the negation of the original condition.*


### not_ (method, L37-L38, parent: Condition)

> *Summary: Creates a negation wrapper around the current condition object. This method takes no arguments and returns an instance of `NotCondition`.*


### TypeCondition (class, L41-L55)

> *Summary: This class checks if an incoming event matches a specified type or tuple of types. It accepts a `ClassInfo` object during initialization and returns `True` if the provided event is an instance of the expected type(s).*


### __init__ (method, L42-L43, parent: TypeCondition)

> *Summary: Initializes the object by storing a `ClassInfo` instance as the expected type for subsequent checks. This sets the criteria against which other types will be compared.*


### __call__ (method, L45-L46, parent: TypeCondition)

> *Summary: Checks if a given `event` object matches the type expected by the instance. It returns `True` if the event is an instance of the stored expected type, otherwise it returns `False`.*


### __repr__ (method, L48-L55, parent: TypeCondition)

> *Summary: Provides a developer-friendly string representation of the condition object. It formats the output to clearly show whether it expects a single type, multiple types (using `|` as an OR separator), or another specified value.*


### AndCondition (class, L58-L73)

> *Summary: This class aggregates multiple `Condition` objects, evaluating to true only if *all* constituent conditions evaluate to true when passed an event. It supports nested `AndCondition` structures by flattening them during its string representation.*


### __init__ (method, L59-L60, parent: AndCondition)

> *Summary: Initializes an object by accepting a variable number of `Condition` instances and storing them in the `self.conditions` attribute. This allows the object to hold multiple criteria for subsequent use.*


### __call__ (method, L62-L63, parent: AndCondition)

> *Summary: This method checks if an incoming `event` satisfies every registered condition within the object. It returns `True` only if all constituent conditions evaluate to true for the provided event.*


### __repr__ (method, L65-L73, parent: AndCondition)

> *Summary: This method generates a string representation of the condition by recursively flattening nested `AndCondition` structures into a single list of constituent conditions. It then joins these flattened conditions with " & " and wraps them in an `And(...)` format for easy debugging and inspection.*


### OrCondition (class, L76-L91)

> *Summary: This class implements a logical OR condition, accepting multiple `Condition` objects as input. It evaluates to true if any of the contained conditions evaluate to true when passed an event, and provides a string representation showing all constituent conditions joined by " | ".*


### __init__ (method, L77-L78, parent: OrCondition)

> *Summary: Initializes an object by accepting a variable number of `Condition` instances and storing them in the `self.conditions` attribute. This allows the object to hold multiple criteria for subsequent evaluation.*


### __call__ (method, L80-L81, parent: OrCondition)

> *Summary: Determines if an event satisfies any of the stored conditions by iterating through them and returning `True` immediately upon finding a match. It accepts one event object as input and outputs a boolean indicating satisfaction.*


### __repr__ (method, L83-L91, parent: OrCondition)

> *Summary: This method generates a string representation of the condition by recursively flattening any nested `OrCondition`s within its list of conditions. The output is a formatted string showing all constituent conditions joined by " | ".*


### NotCondition (class, L94-L102)

> *Summary: This class wraps an existing `Condition` to negate its evaluation. It takes a condition object as input and returns `True` if the wrapped condition evaluates to `False` for a given event, otherwise it returns `False`.*


### __init__ (method, L95-L96, parent: NotCondition)

> *Summary: Initializes an object by storing a provided `Condition` instance as its internal state. This sets up the necessary logic for subsequent event processing based on that specific condition.*


### __call__ (method, L98-L99, parent: NotCondition)

> *Summary: This method acts as a callable wrapper that inverts the result of an internal condition check against a provided event object. It returns `True` if the underlying condition evaluates to false for the given input.*


### __repr__ (method, L101-L102, parent: NotCondition)

> *Summary: Provides a developer-friendly string representation for the condition object by prepending a tilde to its internal representation. This allows for easy debugging and logging of the condition state.*


### OpCondition (class, L105-L127)

> *Summary: This class evaluates a condition against an event object by applying a specified comparison function to a field's value and a target value. It accepts the operation, field name, comparison value, and expected event type as input, returning `True` if the event matches the criteria otherwise.*


### __init__ (method, L106-L116, parent: OpCondition)

> *Summary: Initializes a condition object by storing an operation function, the target field name, the comparison value, and the associated event class. This structure defines the criteria for when a specific event should be considered true based on data fields.*


### __call__ (method, L118-L123, parent: OpCondition)

> *Summary: This method checks if a given event satisfies the defined condition by extracting a specific field's value from it. It returns `True` only if the extracted value passes the comparison logic defined by the stored operator and target value.*


### __repr__ (method, L125-L127, parent: OpCondition)

> *Summary: Provides a developer-friendly string representation for an event condition object. It formats the output to clearly show the event class, field name, operator, and target value being checked.*


### check_eq (function, L130-L133)

> *Summary: Compares two inputs for strict equality after verifying they are of the same type. It returns `True` if both values match and share a type, otherwise it returns `False`.*

