# cli/src/ag2_cli/testing/results.py

1 class(es): CaseResult. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CaseResult | class |  |

## Chunks

### CaseResult (class, L13-L40)

> *Summary: Stores the outcome of a single evaluation run, encapsulating details like the input case, assertion results, execution time, and errors. It provides computed properties to easily determine if all assertions passed, count successes, or calculate an overall score based on its internal results.*


### passed (method, L25-L26, parent: CaseResult)

> *Summary: Determines if all recorded assertion results within the object are successful by checking the `passed` attribute of every result. Returns a boolean indicating overall success or failure.*


### passed_count (method, L29-L30, parent: CaseResult)

> *Summary: Calculates the total number of successful assertions by iterating over stored assertion results and summing those where the `passed` attribute is true. Returns an integer representing the count of passed tests.*


### total_count (method, L33-L34, parent: CaseResult)

> *Summary: Returns the total number of assertion results stored within the object by counting the elements in `self.assertion_results`. This provides a quick count of all recorded test outcomes.*


### score (method, L37-L40, parent: CaseResult)

> *Summary: Calculates the overall success rate by dividing the number of passed assertions by the total count if assertion results exist; otherwise, it returns zero.*

