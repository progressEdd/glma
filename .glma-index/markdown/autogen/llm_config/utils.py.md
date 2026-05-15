# autogen/llm_config/utils.py

3 function(s): config_list_from_json, filter_config, _satisfies_criteria.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| config_list_from_json | function |  |
| filter_config | function |  |
| _satisfies_criteria | function |  |

## Chunks

### config_list_from_json (function, L13-L73)

> *Summary: Reads a list of API configurations from either an environment variable or a specified JSON file path. It optionally filters the retrieved configuration dictionaries based on provided criteria before returning the final list.*


### filter_config (function, L76-L154)

> *Summary: Filters a list of configuration dictionaries based on criteria provided in `filter_dict`, returning configurations that satisfy (or do not satisfy, if `exclude=True`) all specified field constraints. It uses AND logic across different filter keys and OR logic within the acceptable values for each key, handling missing fields by matching only if `None` is an allowed value.*


### _satisfies_criteria (function, L157-L223)

> *Summary: Determines if a configuration value matches specified filter criteria by applying different logic based on whether the inputs are scalar or lists. It returns `True` only if the configuration value is present and satisfies the defined matching rules (e.g., intersection, containment, or exact equality).*

