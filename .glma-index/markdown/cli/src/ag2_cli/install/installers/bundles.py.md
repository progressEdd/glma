# cli/src/ag2_cli/install/installers/bundles.py

1 class(es): BundleInstaller. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BundleInstaller | class |  |

## Chunks

### BundleInstaller (class, L19-L164)

> *Summary: Orchestrates the installation of curated collections (bundles) by fetching metadata and sequentially installing referenced artifacts—such as skills, templates, tools, datasets, or agents—based on a defined order. It accepts a bundle name, project directory, and target configurations, returning an `InstallResult` detailing all created files and dependencies installed.*


### __init__ (method, L22-L40, parent: BundleInstaller)

> *Summary: Initializes a bundle manager by accepting various dependency and installation components, such as an artifact client, lockfile, resolver, and specific installers for skills, templates, tools, datasets, and agents. It stores these provided dependencies internally to manage the overall bundling process.*


### install (method, L42-L113, parent: BundleInstaller)

> *Summary: This method orchestrates the installation of a bundle artifact by first loading its configuration and prompting the user for optional dependencies. It then iterates through artifacts in a predefined order, installing each one via type-specific handlers before recording all created files and installed dependencies into a lockfile.*


### _select_artifacts (method, L115-L140, parent: BundleInstaller)

> *Summary: Determines which artifacts to include from a list of bundle references by first collecting all required items. It attempts an interactive prompt using `questionary` for optional items, falling back to including all optional items if the prompt fails or is unavailable.*


### _install_by_type (method, L142-L164, parent: BundleInstaller)

> *Summary: Routes the installation process based on a provided `type_key` string, dispatching to specialized installers for skills, templates, tools, datasets, or agents. It returns the result of the successful installation or raises an error if the type is unknown or the requested item cannot be found.*

