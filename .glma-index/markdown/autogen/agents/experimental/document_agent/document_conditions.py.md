# autogen/agents/experimental/document_agent/document_conditions.py

1 class(es): SummaryTaskAvailableCondition. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SummaryTaskAvailableCondition | class |  |

## Chunks

### SummaryTaskAvailableCondition (class, L17-L50)

> *Summary: Determines if a summary task is ready by checking three context variables: ensuring no documents remain to ingest, no queries are left to run, and that the count of completed tasks is greater than zero. It returns `True` only when all these conditions are satisfied.*


### is_available (method, L32-L50, parent: SummaryTaskAvailableCondition)

> *Summary: Determines if a document processing task is ready by checking agent context variables. It returns `True` only when there are no documents to ingest, no queries to run, and the overall task has been marked as complete.*

