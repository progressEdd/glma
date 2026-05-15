# website/mkdocs/update_releases.py

6 function(s): find_metablock, find_header, get_github_releases, convert_links_and_usernames, collect_already_published_versions, update_release_notes.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| find_metablock | function |  |
| find_header | function |  |
| get_github_releases | function |  |
| convert_links_and_usernames | function |  |
| collect_already_published_versions | function |  |
| update_release_notes | function |  |

## Chunks

### find_metablock (function, L8-L17)

> *Summary: This function splits a list of strings into two parts based on the presence of YAML front matter. It returns the header block (up to the first `---`) and the remaining content, assuming the input starts with `---`.*


### find_header (function, L20-L25)

> *Summary: Scans a list of strings to locate the first line starting with a hash symbol (`#`). It returns that header line and all subsequent lines in the input list.*


### get_github_releases (function, L28-L31)

> *Summary: Fetches all release information from the specified GitHub repository API endpoint. It returns a sequence of tuples, where each tuple contains the release tag name and its corresponding body text.*


### convert_links_and_usernames (function, L34-L46)

> *Summary: This function transforms raw text by converting standard HTTP/HTTPS URLs into Markdown link syntax and replacing mentions of GitHub usernames with clickable links pointing to their respective profiles. It only performs these substitutions if the input text does not already contain bracketed parentheses `](`.*


### collect_already_published_versions (function, L49-L51)

> *Summary: Extracts all version strings formatted as "## X.Y.Z..." from the input text using a regular expression. Returns these matched version strings as a list of strings.*


### update_release_notes (function, L54-L85)

> *Summary: Reads a release notes file, extracts existing content and metadata, then fetches recent GitHub releases to append new version entries to the changelog. It modifies the body of these new entries before rewriting the complete, updated content back to the original file path.*

