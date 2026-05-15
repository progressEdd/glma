# notebook/mcp/mcp_arxiv.py

4 function(s): search_arxiv, download_paper, list_papers, get_paper_info.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| search_arxiv | function |  |
| download_paper | function |  |
| list_papers | function |  |
| get_paper_info | function |  |

## Chunks

### search_arxiv (function, L19-L22)

> *Summary: This function queries the arXiv API using a provided search string and an optional limit on results. It returns a list containing only the unique IDs of the top matching papers found.*


### download_paper (function, L26-L35)

> *Summary: Retrieves a specific paper from arXiv using its ID and saves the PDF locally within the defined storage path. It returns a confirmation string indicating success or an error message if the ID is invalid.*


### list_papers (function, L39-L41)

> *Summary: Retrieves a list of filenames from the storage directory that end with `.pdf`. This function scans the specified path and returns an array of strings representing the names of all found PDF files.*


### get_paper_info (function, L45-L52)

> *Summary: Retrieves the title and abstract for a specific arXiv paper ID by querying the arXiv API. It returns a dictionary containing the extracted metadata or an error message if the provided ID is invalid.*

