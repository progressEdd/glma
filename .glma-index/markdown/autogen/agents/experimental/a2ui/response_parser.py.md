# autogen/agents/experimental/a2ui/response_parser.py

1 function(s): strip_markdown_fences. 3 class(es): A2UIValidationResult, A2UIParseResult, A2UIResponseParser. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2UIValidationResult | class |  |
| A2UIParseResult | class |  |
| strip_markdown_fences | function |  |
| A2UIResponseParser | class |  |

## Chunks

### A2UIValidationResult (class, L21-L25)

> *Summary: This class encapsulates the outcome of an A2UI operation validation. It stores a boolean indicating overall validity and a list containing any specific error messages encountered during the check.*


### A2UIParseResult (class, L29-L45)

> *Summary: This structure holds the outcome of processing an agent's reply for A2UI content. It stores the conversational text, a list of parsed operation objects, a flag indicating A2UI presence, and optional raw JSON or error details.*


### strip_markdown_fences (function, L48-L56)

> *Summary: Removes surrounding markdown code fences, specifically targeting ` ```json ... ``` ` structures from a string input. It strips the opening and closing fence lines to return the raw content inside.*


### A2UIResponseParser (class, L59-L250)

> *Summary: This class parses raw agent responses to extract structured A2UI operations from text containing a specific delimiter. It can then validate these extracted operations against provided JSON schemas, offering detailed error reporting for both parsing and schema violations.*


### __init__ (method, L66-L80, parent: A2UIResponseParser)

> *Summary: Initializes a parser by storing configuration parameters such as a version string, a custom delimiter, and various schema definitions. It accepts optional inputs like server-to-client schemas, a schema registry, and component schemas to configure its parsing behavior.*


### parse (method, L82-L137, parent: A2UIResponseParser)

> *Summary: This method parses a raw agent response string to separate narrative text from structured A2UI operations embedded in JSON. It splits the input using a predefined delimiter, attempts to decode the subsequent JSON, and returns an `A2UIParseResult` containing the extracted text, list of operations, or error details if parsing fails.*


### format_validation_error (method, L139-L163, parent: A2UIResponseParser)

> *Summary: Generates a detailed string feedback message for an LLM based on parsing and validation failures. It takes the parsed result and validation details as input, outputting a comprehensive instruction set to correct structural or content errors in the generated JSON.*


### validate (method, L166-L210, parent: A2UIResponseParser)

> *Summary: Checks a list of operation dictionaries against an internal JSON schema to ensure structural correctness. It returns a result object indicating overall validity and listing any specific validation errors encountered during the process.*


### _drill_into_components (method, L212-L250, parent: A2UIResponseParser)

> *Summary: Validates individual components within an `updateComponents` operation dictionary against predefined schemas. It accepts the operation dict and returns a list of strings detailing any validation errors found for each component.*

