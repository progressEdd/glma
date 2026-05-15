# cli/test_playground/tools_generated.py

7 function(s): list_tasks, create_task, get_task, update_task, delete_task, list_comments, add_comment.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| list_tasks | function |  |
| create_task | function |  |
| get_task | function |  |
| update_task | function |  |
| delete_task | function |  |
| list_comments | function |  |
| add_comment | function |  |

## Chunks

### list_tasks (function, L8-L15)

> *Summary: Fetches a list of tasks from an external API endpoint, optionally filtering by status and limiting the results. It accepts `status` and `limit` as optional string/integer inputs and returns the raw JSON response text upon success.*


### create_task (function, L18-L24)

> *Summary: This function sends a POST request to an external API endpoint to create a new task using provided title, optional description, and optional priority. It returns the raw text response from the successful API call.*


### get_task (function, L27-L32)

> *Summary: Fetches task details from a remote API endpoint using the provided integer ID. It makes an HTTP GET request and returns the response body as a string upon successful retrieval.*


### update_task (function, L35-L41)

> *Summary: This function sends a PUT request to an external API endpoint using a provided task ID and optional fields (title, status, priority). It returns the raw text response from the server upon successful update.*


### delete_task (function, L44-L49)

> *Summary: This function removes a task by sending an HTTP DELETE request to a specified API endpoint using the provided `task_id`. It returns the response body text upon successful deletion.*


### list_comments (function, L52-L57)

> *Summary: Fetches and returns the raw text content of all comments associated with a given task ID from an external API endpoint. It uses `httpx` to perform a GET request and raises an exception if the HTTP response status is not successful.*


### add_comment (function, L60-L66)

> *Summary: This function posts a comment to a specific task via an external API endpoint using the provided `task_id` and `text`. It returns the raw text response from the successful HTTP POST request.*

