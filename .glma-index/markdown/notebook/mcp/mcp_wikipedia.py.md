# notebook/mcp/mcp_wikipedia.py

4 function(s): search_wikipedia, download_article, list_articles, get_article_summary.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| search_wikipedia | function |  |
| download_article | function |  |
| list_articles | function |  |
| get_article_summary | function |  |

## Chunks

### search_wikipedia (function, L19-L21)

> *Summary: This function queries Wikipedia using a provided string to find relevant article titles. It accepts the search term and an optional limit on the number of results, returning a list of matching titles.*


### download_article (function, L25-L35)

> *Summary: Fetches the content of a Wikipedia article given its title string, saving the text to a file within the storage path. It returns a success message with the filename or an error indicating ambiguity or that the article does not exist.*


### list_articles (function, L39-L41)

> *Summary: Retrieves a list of all downloaded Wikipedia article filenames from the storage directory. It scans the specified path and returns each file's name as a string within a list.*


### get_article_summary (function, L45-L51)

> *Summary: Retrieves the summary and title of a Wikipedia article given its name as input. It returns a dictionary containing either the requested data or an error message if the specified page does not exist.*

