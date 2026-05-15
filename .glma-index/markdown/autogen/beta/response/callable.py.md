# autogen/beta/response/callable.py

5 function(s): response_schema, response_schema, response_schema, response_schema, _unwrap_message_to_fast_depends_decorator. 1 class(es): CallableResponse. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CallableResponse | class |  |
| response_schema | function |  |
| response_schema | function |  |
| response_schema | function |  |
| response_schema | function |  |
| _unwrap_message_to_fast_depends_decorator | function |  |

## Chunks

### CallableResponse (class, L30-L51)

> *Summary: This class wraps a validator to represent a callable response structure. It takes a validator and metadata (name, schema, description) upon initialization, then executes the wrapped validator asynchronously using provided content and context to return the expected typed result.*


### __init__ (method, L31-L43, parent: CallableResponse)

> *Summary: Initializes a callable response object by storing its name, optional JSON schema, and description. It sets the provided `ResponseValidator` as the internal execution mechanism for this instance.*


### validate (method, L45-L51, parent: CallableResponse)

> *Summary: This method executes the stored content asynchronously using provided context and an optional provider. It returns the result of that execution.*


### response_schema (function, L55-L63)

> *Summary: Creates a callable response object from an asynchronous function by wrapping it with metadata like name, description, and JSON schema. It manages execution context via `sync_to_thread` and controls embedding behavior.*


### response_schema (function, L67-L75)

> *Summary: Creates a callable wrapper for a given function, allowing it to be exposed as an agent tool. It accepts the target function and optional metadata like name, description, schema, and execution behavior flags.*


### response_schema (function, L79-L87)

> *Summary: Creates a callable wrapper for functions, accepting optional metadata like name, description, and JSON schema. It returns a specialized response object that can be executed within the system's response handling mechanism.*


### response_schema (function, L90-L118)

> *Summary: This function generates a callable schema wrapper for a given hook or returns a factory that creates one. It takes optional metadata like name and description, uses the provided `ResponseHook` to generate validation logic and structure, and ultimately produces either a ready-to-use response object or a function that constructs it.*


### _unwrap_message_to_fast_depends_decorator (function, L121-L183)

> *Summary: This function wraps a response hook to integrate it with dependency injection via `fast_depends`. It constructs and returns an asynchronous wrapper function and a corresponding response schema based on whether the decorated function accepts multiple positional arguments. The wrapper validates incoming messages against the generated schema before executing the original logic.*

