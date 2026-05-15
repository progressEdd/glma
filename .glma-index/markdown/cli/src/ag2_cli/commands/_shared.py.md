# cli/src/ag2_cli/commands/_shared.py

2 function(s): require_ag2, extract_cost.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| require_ag2 | function |  |
| extract_cost | function |  |

## Chunks

### require_ag2 (function, L12-L21)

> *Summary: Checks for the presence of the `autogen` library; if missing, it prints an error message and exits the application immediately. If found, it returns the imported `autogen` module object.*


### extract_cost (function, L24-L29)

> *Summary: Retrieves the total cost as a float from a provided dictionary structure representing AG2's cost information. It safely accesses nested keys, defaulting to zero if the expected dictionary or cost fields are missing.*

