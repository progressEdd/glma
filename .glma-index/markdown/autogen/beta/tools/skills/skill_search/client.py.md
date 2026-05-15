# autogen/beta/tools/skills/skill_search/client.py

1 class(es): SkillsClient. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SkillsClient | class |  |

## Chunks

### SkillsClient (class, L20-L118)

> *Summary: This client manages HTTP interactions with `skills.sh` and GitHub APIs for searching skills and downloading repositories as tarballs. It accepts configuration for authentication and connection settings, returning skill lists from searches or metadata and SHA256 hashes after successfully downloading and installing a skill via a provided runtime object.*


### __init__ (method, L35-L51, parent: SkillsClient)

> *Summary: Initializes a client by setting up HTTP headers, including authentication via a provided or environment-sourced GitHub token. It also configures connection parameters such as timeout, proxy settings, and SSL verification based on the input configuration.*


### _make_client (method, L53-L64, parent: SkillsClient)

> *Summary: Constructs and returns an `httpx.AsyncClient` instance by merging stored configuration settings (like timeouts, headers, and proxies) with any provided overrides. This method ensures the client is initialized with consistent network behavior defined by the object's state.*


### search (method, L66-L72, parent: SkillsClient)

> *Summary: Fetches skill records from the skills.sh API by making a GET request to the search endpoint. It accepts a search query string and an optional limit, returning a list of dictionaries containing matching skill data.*


### download_skill (method, L74-L118, parent: SkillsClient)

> *Summary: Fetches a skill's tarball from GitHub using the provided source and ID, then extracts it into a temporary directory. It installs the resulting skill via the runtime object and returns its metadata along with the file's SHA256 checksum.*

