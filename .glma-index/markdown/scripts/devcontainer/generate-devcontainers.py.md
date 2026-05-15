# scripts/devcontainer/generate-devcontainers.py

2 function(s): generate_devcontainer_json_file, generate_devcontainer_files.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| generate_devcontainer_json_file | function |  |
| generate_devcontainer_files | function |  |

## Chunks

### generate_devcontainer_json_file (function, L20-L46)

> *Summary: This function creates a `devcontainer.json` file by rendering a template with the specified Python version. It writes the resulting configuration to either `.devcontainer/` or a version-specific subdirectory within it, ensuring the directory structure exists first.*


### generate_devcontainer_files (function, L49-L69)

> *Summary: This function iterates over predefined Python versions to ensure a clean state by deleting existing `.devcontainer` files and directories for each version. It then calls another helper to generate the necessary `devcontainer.json` configuration file for every specified Python environment.*

