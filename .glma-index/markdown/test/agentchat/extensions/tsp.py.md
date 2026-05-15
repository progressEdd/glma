# test/agentchat/extensions/tsp.py

2 function(s): solve_tsp, tsp_data.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| solve_tsp | function |  |
| tsp_data | function |  |

## Chunks

### solve_tsp (function, L16-L54)

> *Summary: Calculates the minimum total distance for a Traveling Salesperson Problem given a dictionary representing pairwise distances between nodes. It generates and evaluates every possible permutation of nodes to find and return the lowest achievable tour cost.*


### tsp_data (function, L57-L81)

> *Summary: Generates a dictionary representing the pairwise distance matrix for an $n$-node non-symmetric Traveling Salesperson Problem instance. It takes the number of nodes and an optional seed as input, returning a map where keys are node pairs $(i, j)$ and values are randomly generated distances between them.*

