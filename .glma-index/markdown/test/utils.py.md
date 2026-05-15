# test/utils.py

3 function(s): suppress, suppress_gemini_resource_exhausted, suppress_json_decoder_error.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| suppress | function |  |
| suppress_gemini_resource_exhausted | function |  |
| suppress_json_decoder_error | function |  |

## Chunks

### suppress (function, L22-L89)

> *Summary: Applies a decorator that wraps a function to suppress a specified exception and automatically retry execution up to a given number of times with a defined delay between attempts. It supports both synchronous and asynchronous functions, allowing for optional filtering of exceptions before suppression occurs.*


### suppress_gemini_resource_exhausted (function, L92-L102)

> *Summary: Wraps a function to automatically retry execution up to two times specifically when encountering Gemini API errors with HTTP codes 429 or 503. This prevents the application from failing due to temporary resource exhaustion issues from the service.*


### suppress_json_decoder_error (function, L105-L106)

> *Summary: Wraps a given function to catch and suppress `JSONDecodeError` exceptions during execution. It returns the decorated version of the input callable.*

