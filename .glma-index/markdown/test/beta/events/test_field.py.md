# test/beta/events/test_field.py

5 class(es): TestFieldBasics, TestFieldInit, TestFieldRepr, TestFieldCompare, TestFieldPositionalArgs. 25 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestFieldBasics | class |  |
| TestFieldInit | class |  |
| TestFieldRepr | class |  |
| TestFieldCompare | class |  |
| TestFieldPositionalArgs | class |  |

## Chunks

### TestFieldBasics (class, L10-L42)

> *Summary: Verifies the basic functionality of field definitions within an event structure, testing how fields are named, initialized with provided values, and correctly handle default values or factory functions when no arguments are supplied during object instantiation.*


### test_event_with_field (method, L11-L21, parent: TestFieldBasics)

> *Summary: This test verifies that a custom event class correctly initializes and exposes fields defined using `Field()`. It confirms that field names are accessible via the descriptor and that instance attributes match the provided input values.*


### test_event_with_value_field (method, L23-L28, parent: TestFieldBasics)

> *Summary: This test verifies that an event subclass correctly initializes and exposes a predefined string attribute. It instantiates the custom `Event` class and asserts that its attribute `a` holds the expected value `"1"`.*


### test_event_with_default_field (method, L30-L35, parent: TestFieldBasics)

> *Summary: This test verifies that an event object correctly initializes a field with a predefined default value. It instantiates a custom event inheriting from `BaseEvent` and asserts the presence of the expected default string in its attribute.*


### test_event_with_default_factory (method, L37-L42, parent: TestFieldBasics)

> *Summary: This test verifies that an event object correctly initializes a field using a `default_factory`. It asserts that the attribute, configured with a factory returning `"1"`, holds the expected default value upon instantiation.*


### TestFieldInit (class, L45-L76)

> *Summary: This test suite verifies how fields behave when initialized during object creation based on the `init` flag. It confirms that fields marked with `init=True` accept constructor arguments, while those with `init=False` rely on provided defaults or factory functions, ensuring instance isolation for mutable types.*


### test_init_true_accepts_value (method, L46-L51, parent: TestFieldInit)

> *Summary: This test verifies that an event class, when defined with a field set to `init=True`, correctly accepts and stores a provided value during instantiation. It asserts that the instance attribute matches the input string.*


### test_init_false_applies_default (method, L53-L60, parent: TestFieldInit)

> *Summary: This test verifies that an uninitialized field with a default value is correctly set upon object instantiation when the constructor is called with other arguments. It confirms that `_internal` defaults to $0$ even if not explicitly provided during initialization.*


### test_init_false_with_default_factory (method, L62-L67, parent: TestFieldInit)

> *Summary: Verifies that an event object initialized with `init=False` for a field using `default_factory=list` correctly initializes the attribute to an empty list upon instantiation. The test confirms the default factory behavior is respected even when initialization is suppressed.*


### test_init_false_separate_instances (method, L69-L76, parent: TestFieldInit)

> *Summary: This test verifies that when an event class initializes a field with `init=False` and `default_factory`, each instance receives its own independent list. It confirms that modifying the list on one instance does not affect another.*


### TestFieldRepr (class, L79-L113)

> *Summary: This test suite verifies how field representation (`repr`) behaves for custom event objects. It confirms that fields marked with `repr=False` are omitted from the string representation while remaining accessible via attribute access.*


### test_repr_true_shows_field (method, L80-L85, parent: TestFieldRepr)

> *Summary: This test verifies that the string representation of an event object correctly includes its defined fields. It instantiates a simple event with a string attribute and asserts that the `repr()` output contains the field name and its value.*


### test_repr_false_hides_field (method, L87-L94, parent: TestFieldRepr)

> *Summary: This test verifies that fields marked with `repr=False` are omitted from an object's string representation. It instantiates a custom event, asserts the visible field appears in the `repr`, and confirms the hidden field is absent.*


### test_repr_false_field_still_accessible (method, L96-L101, parent: TestFieldRepr)

> *Summary: This test verifies that a field explicitly set to `repr=False` remains accessible and retains its default value when an instance of the event is created. It confirms direct attribute access works even for non-representable fields.*


### test_repr_mixed_fields (method, L103-L113, parent: TestFieldRepr)

> *Summary: This test verifies that the `repr()` output of an event object correctly includes public fields while omitting internal fields marked with `repr=False`. It asserts specific string inclusions based on the provided instance data.*


### TestFieldCompare (class, L116-L170)

> *Summary: This test suite verifies the equality comparison behavior of event objects based on field definitions. It demonstrates how fields marked with `compare=True` (default) affect equality, while those with `compare=False` are ignored during comparison, including scenarios involving custom overrides and inheritance.*


### test_compare_true_includes_field (method, L117-L123, parent: TestFieldCompare)

> *Summary: Verifies that two instances of a custom event class are considered equal if all their attributes match, and unequal otherwise. It tests equality comparison using specific string and integer values for the defined fields.*


### test_compare_false_excludes_field (method, L125-L131, parent: TestFieldCompare)

> *Summary: This test verifies that an event comparison ignores fields marked with `compare=False`. It asserts that two events are considered equal if only the ignored field's value differs, while still correctly comparing other fields.*


### test_compare_false_all_fields (method, L133-L138, parent: TestFieldCompare)

> *Summary: This test verifies that two instances of an event class, where all fields are explicitly marked as non-comparable, evaluate to equal even when their field values differ. It asserts equality between two distinct event objects constructed with different data.*


### test_compare_different_types (method, L140-L147, parent: TestFieldCompare)

> *Summary: Asserts that instances of two distinct event classes, despite having the same structure and data, are not equal. This test verifies type-based inequality when comparing objects derived from a common base class.*


### test_compare_with_custom_eq_override (method, L149-L160, parent: TestFieldCompare)

> *Summary: This test verifies that an object overriding the equality operator (`__eq__`) compares only specific attributes. It asserts that two instances are equal if their `a` attribute matches, regardless of differences in other attributes like `b`.*


### test_compare_inherited_fields (method, L162-L170, parent: TestFieldCompare)

> *Summary: This test verifies that field comparison respects inheritance, specifically ensuring that fields marked with `compare=False` in a subclass do not affect equality checks between instances. It confirms that only non-excluded fields are used for determining object equivalence.*


### TestFieldPositionalArgs (class, L173-L229)

> *Summary: These tests verify that event classes correctly handle positional arguments when defined with `kw_only=False`. They confirm proper assignment, mixed usage of positional and keyword arguments, and error handling for incorrect argument counts or duplicates.*


### test_positional_arg (method, L174-L179, parent: TestFieldPositionalArgs)

> *Summary: This test verifies that a positional argument passed during object instantiation is correctly assigned to an instance field. It creates an `Event` subclass and asserts that the first string argument populates the `a` attribute.*


### test_positional_and_kwarg (method, L181-L188, parent: TestFieldPositionalArgs)

> *Summary: This test verifies that an object initialized with both positional and keyword arguments correctly assigns values to its defined fields. It confirms that the first argument maps to `a` (string) and the keyword argument `b` maps to `b` (integer).*


### test_multiple_positional (method, L190-L197, parent: TestFieldPositionalArgs)

> *Summary: This test verifies that an event object correctly accepts and stores multiple positional arguments upon instantiation. It confirms that the first argument maps to a string field (`a`) and the second maps to an integer field (`b`).*


### test_positional_still_accepts_kwarg (method, L199-L204, parent: TestFieldPositionalArgs)

> *Summary: This test verifies that an event class defined with a positional field can correctly accept and store values passed as keyword arguments during instantiation. It asserts that the assigned value matches the input provided via `a="hello"`.*


### test_too_many_positional_raises (method, L206-L211, parent: TestFieldPositionalArgs)

> *Summary: Asserts that passing too many positional arguments to an event class constructor raises a `TypeError`. This test verifies the expected behavior when an instance is initialized with more arguments than defined fields allow.*


### test_duplicate_positional_and_kwarg_raises (method, L213-L218, parent: TestFieldPositionalArgs)

> *Summary: This test verifies that attempting to pass the same argument both positionally and as a keyword argument raises a `TypeError`. It instantiates an event class with one field and calls it with conflicting arguments.*


### test_inherited_positional (method, L220-L229, parent: TestFieldPositionalArgs)

> *Summary: This test verifies that positional arguments are correctly inherited from a parent class when instantiating a child class. It confirms that the `Child` object successfully receives and stores both its own keyword argument (`b`) and the inherited positional argument (`a`).*

