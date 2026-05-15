# test/agents/experimental/document_agent/test_docagent.py

2 function(s): test_document_triage_agent_init, test_document_agent_init.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_document_triage_agent_init | function |  |
| test_document_agent_init | function |  |

## Chunks

### test_document_triage_agent_init (function, L19-L22)

> *Summary: This test verifies the initialization of a document triage agent by creating an instance using provided LLM configuration credentials. It asserts that the resulting agent's configuration correctly specifies the `DocumentTask` for response formatting.*


### test_document_agent_init (function, L27-L36)

> *Summary: This test verifies that an initialized `DocAgent` instance correctly possesses several internal agent components. It confirms the presence of specific private attributes like task manager, triage, data ingestion, query, error, and summary agents after instantiation with provided credentials and a temporary path.*

