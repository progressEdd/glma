# test/agentchat/contrib/vectordb/test_vectordb_utils.py

2 function(s): test_retrieve_config, test_chroma_results_to_query_results.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_retrieve_config | function |  |
| test_chroma_results_to_query_results | function |  |

## Chunks

### test_retrieve_config (function, L13-L23)

> *Summary: This test verifies the `filter_results_by_distance` function by comparing its output against an expected result set. It takes a list of pairs (ID and distance) and a threshold to return only those entries whose distances are less than or equal to the provided value.*


### test_chroma_results_to_query_results (function, L26-L51)

> *Summary: This test verifies a utility function that transforms raw Chroma database output into a structured query result format. It takes a dictionary containing keys, values (for different types), and distances as input, expecting the function to return a list of lists representing matched items with their associated similarity scores.*

