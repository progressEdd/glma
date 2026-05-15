# cli/src/ag2_cli/testing/cases.py

3 function(s): _parse_assertion, _parse_case, load_eval_suite. 3 class(es): EvalAssertion, EvalCase, EvalSuite.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| EvalAssertion | class |  |
| EvalCase | class |  |
| EvalSuite | class |  |
| _parse_assertion | function |  |
| _parse_case | function |  |
| load_eval_suite | function |  |

## Chunks

### EvalAssertion (class, L11-L20)

> *Summary: Represents a single validation check against an agent's output, holding various parameters like expected types, specific values, regex patterns, or numerical thresholds. It is designed to configure different assertion mechanisms, including those involving external language models.*


### EvalCase (class, L24-L29)

> *Summary: Represents a single unit of testing for evaluations, holding the test's name and input data. It also stores a list of `EvalAssertion` objects to verify expected outcomes after execution.*


### EvalSuite (class, L33-L38)

> *Summary: This class aggregates multiple evaluation scenarios, holding a name, description, and a list of individual `EvalCase` objects. It serves as a container for grouping related test cases together.*


### _parse_assertion (function, L41-L53)

> *Summary: This function transforms a raw dictionary, typically from YAML input, into an `EvalAssertion` object. It validates the presence of a "type" field and maps all available keys to the corresponding fields in the assertion structure.*


### _parse_case (function, L56-L67)

> *Summary: This function transforms a raw dictionary from YAML into an `EvalCase` object. It validates the presence of required 'name' and 'input' fields and recursively parses any associated assertions before returning the structured case.*


### load_eval_suite (function, L70-L100)

> *Summary: Parses a YAML file located at the given path to construct an `EvalSuite` object. It reads the file, validates its structure, and converts the list of case definitions into structured objects before returning the complete suite.*

