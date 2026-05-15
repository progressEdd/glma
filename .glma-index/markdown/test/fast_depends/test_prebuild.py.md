# test/fast_depends/test_prebuild.py

4 function(s): base_func, model_func, test_prebuild, test_prebuild_with_wrapper. 1 class(es): Model.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Model | class |  |
| base_func | function |  |
| model_func | function |  |
| test_prebuild | function |  |
| test_prebuild_with_wrapper | function |  |

## Chunks

### Model (class, L18-L19)

> *Summary: Defines a data structure inheriting from `BaseModel` that requires one string field named `a`. This serves as a basic model for testing dependency resolution.*


### base_func (function, L22-L23)

> *Summary: Accepts an integer input and consistently returns the string `"success"` as its output. This serves as a simple, predictable function for testing purposes.*


### model_func (function, L26-L27)

> *Summary: This function takes a `Model` object as input and returns the value of its attribute `a` as a string. It serves to extract a specific property from an instance of the `Model`.*


### test_prebuild (function, L30-L32)

> *Summary: This test verifies the prebuilding mechanism by first constructing a call model from a base function. It then executes an injection process using this model with a specific input value.*


### test_prebuild_with_wrapper (function, L35-L50)

> *Summary: This test verifies that model building functions correctly even when the target function is wrapped by another callable. It asserts that the resulting call model has a valid model structure, potentially triggering a rebuild or forward reference update depending on the Pydantic version.*

