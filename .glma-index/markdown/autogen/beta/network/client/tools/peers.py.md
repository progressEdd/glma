# autogen/beta/network/client/tools/peers.py

2 function(s): _passport_summary, make_peers_tool.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _passport_summary | function |  |
| make_peers_tool | function |  |

## Chunks

### _passport_summary (function, L29-L48)

> *Summary: Generates a summary dictionary by combining information from a `passport` object and a `resume` object. It calculates the observed success rate based on completion counts in the resume and structures the output with identity, capabilities, performance metrics, and cost details.*


### make_peers_tool (function, L51-L130)

> *Summary: Generates a callable tool that allows querying or detailing other agents within the system. It accepts an `action` ("find" or "describe") and various optional parameters like query strings, sorting criteria, or specific agent names to retrieve peer information. The output is either a list of summarized peers (for "find") or a detailed dictionary containing passport, resume, and skill metadata for a single peer (for "describe").*

