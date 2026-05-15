# test/fast_depends/library/test_custom.py

16 function(s): test_header, test_custom_with_class, test_header_async, test_multiple_header, test_async_header_async, test_sync_field_header, test_async_field_header, test_async_header_sync, test_header_annotated, test_annotated_header_with_meta and 6 more. 4 class(es): Header, FieldHeader, AsyncHeader, AsyncFieldHeader. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Header | class |  |
| FieldHeader | class |  |
| AsyncHeader | class |  |
| AsyncFieldHeader | class |  |
| test_header | function |  |
| test_custom_with_class | function |  |
| test_header_async | function |  |
| test_multiple_header | function |  |
| test_async_header_async | function |  |
| test_sync_field_header | function |  |
| test_async_field_header | function |  |
| test_async_header_sync | function |  |
| test_header_annotated | function |  |
| test_annotated_header_with_meta | function |  |
| test_header_required | function |  |
| test_header_not_required | function |  |
| test_depends | function |  |
| test_not_cast | function |  |
| test_reusable_annotated | function |  |
| test_arguments_mapping | function |  |

## Chunks

### Header (class, L22-L27)

> *Summary: This class overrides the `use` method to inject a specific header value into the output dictionary if one is provided for its parameter name within the input arguments. It modifies the inherited result by overwriting or setting the corresponding key in the headers section of the returned dictionary.*


### use (method, L23-L27, parent: Header)

> *Summary: This method overrides the parent's `use` behavior, then checks if a specific header value exists for the instance's parameter name within the provided keyword arguments. If found, it overwrites the original argument with that header value before returning the modified dictionary.*


### FieldHeader (class, L30-L37)

> *Summary: Extends a base `Header` class to specifically mark itself as a field header. It overrides the initialization to set an internal flag and provides a method to inject header values into keyword arguments based on its parameter name.*


### __init__ (method, L31-L33, parent: FieldHeader)

> *Summary: Initializes the object by passing `cast` and `required` parameters to the parent class constructor. It also sets an internal flag named `field` to `True`.*


### use_field (method, L35-L37, parent: FieldHeader)

> *Summary: If a specific header value is present in the input `kwargs`, this method injects that value into the main `kwargs` dictionary using the instance's parameter name as the key. It effectively pulls configuration from headers into the primary arguments passed to the function.*


### AsyncHeader (class, L40-L42)

> *Summary: Extends a base `Header` class to provide asynchronous behavior. It delegates the actual header usage logic to its parent class while maintaining an async interface that returns a dictionary of headers.*


### use (method, L41-L42, parent: AsyncHeader)

> *Summary: This method delegates the execution of its arguments to the parent class's `use` method. It accepts arbitrary keyword arguments and returns the resulting dictionary from the superclass call.*


### AsyncFieldHeader (class, L45-L53)

> *Summary: This class extends a base `Header` to specifically mark itself as a field header. Its asynchronous method modifies the input keyword arguments by injecting a value from the "headers" dictionary if it exists for the header's parameter name, after a short delay.*


### __init__ (method, L46-L48, parent: AsyncFieldHeader)

> *Summary: Initializes the object by passing `cast` and `required` parameters to its parent class constructor. It also sets an internal flag named `field` to `True`.*


### use_field (method, L50-L53, parent: AsyncFieldHeader)

> *Summary: This method asynchronously waits briefly and then checks if a specific header value, identified by `self.param_name`, exists within the provided keyword arguments' headers. If found, it injects that header value directly into the kwargs dictionary under the parameter's name.*


### test_header (function, L56-L61)

> *Summary: This test verifies that a function decorated with `@inject` correctly retrieves an integer value from the `Header()` dependency when provided with specific HTTP headers. It asserts that passing `{"key": "1"}` results in the return value of `1`.*


### test_custom_with_class (function, L64-L70)

> *Summary: This test verifies dependency injection by instantiating a class that requires an injected `Header` value for its constructor. It asserts that the instance's internal state correctly reflects the provided header input.*


### test_header_async (function, L74-L79)

> *Summary: This asynchronous test verifies that a dependency injected function correctly parses an integer value from the request headers. It asserts that calling the decorated function with `{"key": "1"}` returns the integer `1`.*


### test_multiple_header (function, L82-L88)

> *Summary: This test verifies that a function decorated with `@inject` correctly parses multiple HTTP headers. It asserts that the injected string header matches `"1"` and the integer header matches `2` when provided specific header values in the input dictionary.*


### test_async_header_async (function, L92-L99)

> *Summary: This test verifies that an asynchronous function correctly retrieves values from injected `AsyncHeader` objects using provided header dictionary inputs. It asserts the returned tuple matches the expected float and integer values derived from those headers.*


### test_sync_field_header (function, L102-L107)

> *Summary: This test verifies that a function decorated with `@inject` correctly processes input headers by converting string representations of numeric fields into their appropriate types. It asserts the return value matches the expected float and integer types derived from the provided header dictionary.*


### test_async_field_header (function, L111-L120)

> *Summary: This test verifies that an asynchronous function correctly processes inputs provided via `AsyncFieldHeader` when called with specific header values. It asserts the returned tuple matches the input types and confirms the execution completes within a strict time limit.*


### test_async_header_sync (function, L123-L128)

> *Summary: This test asserts that attempting to synchronously retrieve an `AsyncHeader` object, even when injected, raises an `AssertionError`. It verifies the expected failure mode when mixing asynchronous and synchronous contexts.*


### test_header_annotated (function, L131-L136)

> *Summary: This test verifies that a dependency function decorated with `@inject` correctly extracts and converts an integer value from HTTP headers. It asserts that passing `{"key": "1"}` in the headers results in the function returning the integer `1`.*


### test_annotated_header_with_meta (function, L140-L150)

> *Summary: This test verifies header validation behavior for a function annotated with `Header` and constraints. It asserts that providing an invalid header value raises a `ValidationError`, while correctly passing valid values or defaulting when no headers are supplied.*


### test_header_required (function, L153-L159)

> *Summary: This test verifies that a required `Header` dependency fails validation when not provided. It asserts that calling the injected function without supplying the necessary header raises a `pydantic.ValidationError`.*


### test_header_not_required (function, L162-L167)

> *Summary: This test verifies that a header parameter, when explicitly marked as optional (`required=False`), correctly defaults to `None` upon invocation. It asserts the absence of the header value in the provided context.*


### test_depends (function, L170-L178)

> *Summary: This test verifies dependency injection by creating a function that retrieves an integer header value and then uses it within another injected function. It asserts that the inner function correctly processes the provided HTTP headers to return the expected integer.*


### test_not_cast (function, L181-L192)

> *Summary: This test verifies that when `Header` injection is configured with `cast=False`, the framework accepts and returns values of arbitrary types, such as floats or logger objects, directly from HTTP headers without attempting type coercion. It asserts successful retrieval for both a float and a logger instance passed via request headers.*


### test_reusable_annotated (function, L195-L207)

> *Summary: This test verifies that functions decorated with `@inject` correctly receive and process header values typed using `Annotated[float, Header(cast=False)]`. It asserts that both injected functions return the expected float value from the provided headers dictionary.*


### test_arguments_mapping (function, L210-L224)

> *Summary: This test verifies argument mapping by calling an injected function with specific integer inputs. It asserts that the internal parameters of the function correctly receive and match these provided values across multiple iterations.*

