# cli/src/ag2_cli/commands/test.py

4 function(s): _run_single_case, _display_results, test_eval, test_bench.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _run_single_case | function |  |
| _display_results | function |  |
| test_eval | function |  |
| test_bench | function |  |

## Chunks

### _run_single_case (function, L24-L55)

> *Summary: Executes a single evaluation case against an agent loaded from a file by first discovering its components. It returns a `CaseResult` containing the execution output, assertion outcomes, and timing information, handling discovery errors gracefully.*


### _display_results (function, L58-L118)

> *Summary: Calculates and displays a comprehensive report of test execution results using Rich formatting. It accepts an `EvalSuite` object and a list of `CaseResult` objects, outputting detailed per-case status, assertion failures, and a final summary including pass rates, total time, cost, and token usage.*


### test_eval (function, L122-L210)

> *Summary: Executes an evaluation suite against a specified agent file using provided YAML case files. It processes the cases, runs them against the agent, and outputs results either to the console or as structured JSON if requested.*


### test_bench (function, L214-L232)

> *Summary: This function serves as a placeholder command to run standardized benchmarks against an agent defined in a specified Python file. It accepts the agent's file path and a benchmark suite identifier, currently only printing status messages before exiting gracefully.*

