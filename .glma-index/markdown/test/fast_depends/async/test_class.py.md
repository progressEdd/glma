# test/fast_depends/async/test_class.py

2 function(s): _get_var, test_class. 1 class(es): Class. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _get_var | function |  |
| Class | class |  |
| test_class | function |  |

## Chunks

### _get_var (function, L13-L14)

> *Summary: This helper function unconditionally returns the integer `1`. It serves as a simple mock or placeholder value within tests.*


### Class (class, L17-L24)

> *Summary: This class initializes with a dependency injected value and provides an asynchronous method that calculates the sum of two dependency-injected values. The `calc` method returns an integer result based on its inputs.*


### __init__ (method, L19-L20, parent: Class)

> *Summary: Initializes the object by accepting a dependency injection instance (`a`) which is resolved via `_get_var`. This stored dependency is then assigned to the instance attribute `self.a`.*


### calc (method, L23-L24, parent: Class)

> *Summary: This asynchronous method takes an input `a` resolved via dependency injection and returns the sum of that input and the instance's attribute `self.a`.*


### test_class (function, L28-L29)

> *Summary: This asynchronous test verifies that an instance of `Class` returns the value `2` when its `calc()` method is awaited. It serves to confirm the expected behavior of the class's calculation logic in an async context.*

