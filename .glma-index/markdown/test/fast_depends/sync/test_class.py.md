# test/fast_depends/sync/test_class.py

2 function(s): _get_var, test_class. 1 class(es): Class. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _get_var | function |  |
| Class | class |  |
| test_class | function |  |

## Chunks

### _get_var (function, L11-L12)

> *Summary: This helper function unconditionally returns the integer `1`. It serves as a simple mock or placeholder value for testing purposes within dependency resolution logic.*


### Class (class, L15-L22)

> *Summary: This class initializes itself by injecting a value from `_get_var` into an instance attribute. It provides a method that calculates and returns the sum of this injected value and the stored instance attribute.*


### __init__ (method, L17-L18, parent: Class)

> *Summary: Initializes an instance by accepting a dependency object (`a`) resolved via `Depends(_get_var)` and stores it as an attribute.*


### calc (method, L21-L22, parent: Class)

> *Summary: This method calculates and returns an integer by adding the value of `self.a` to a dependency injected variable `a`. It requires no explicit inputs beyond the instance state and the provided dependency.*


### test_class (function, L25-L26)

> *Summary: This test verifies that an instance of `Class` returns the value `2` when its `calc()` method is called. It asserts this expected output against the actual result from the class instance.*

