# cli/src/ag2_cli/testing/assertions.py

2 function(s): check_assertion, _check_llm_judge. 1 class(es): AssertionResult.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AssertionResult | class |  |
| check_assertion | function |  |
| _check_llm_judge | function |  |

## Chunks

### AssertionResult (class, L13-L20)

> *Summary: Represents the outcome of an individual test check, storing whether it passed, the type of assertion performed, and associated details like expected and actual values. This structure encapsulates all necessary information about a single validation step.*


### check_assertion (function, L23-L171)

> *Summary: This function evaluates a specified assertion against an agent's text output, accepting the assertion object and output string as primary inputs. It supports various checks like substring presence/absence, regex matching, length constraints, turn limits, error checking, and LLM judgment, returning a detailed `AssertionResult` indicating success or failure for each type.*


### _check_llm_judge (function, L174-L266)

> *Summary: Evaluates an agent's output against specified criteria by prompting a configured LLM (defaulting to gpt-4o) via AutoGen. It takes an `EvalAssertion` containing the criteria and the raw `output` string, returning an `AssertionResult` indicating whether the LLM judged the output as PASS or FAIL.*

