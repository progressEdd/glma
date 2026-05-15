# autogen/beta/network/ids.py

1 function(s): make_id.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| make_id | function |  |

## Chunks

### make_id (function, L18-L29)

> *Summary: Generates a unique identifier string by prioritizing UUID7 for time-ordered generation if available; otherwise, it defaults to generating a standard UUID4 and returns the resulting 32-character hexadecimal representation. This ensures a sortable ID when distributed across multiple processes.*

