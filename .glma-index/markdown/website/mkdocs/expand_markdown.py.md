# website/mkdocs/expand_markdown.py

4 function(s): read_lines_from_file, extract_lines, expand_markdown, remove_lines_between_dashes.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| read_lines_from_file | function |  |
| extract_lines | function |  |
| expand_markdown | function |  |
| remove_lines_between_dashes | function |  |

## Chunks

### read_lines_from_file (function, L13-L44)

> *Summary: Reads content from a specified file, optionally extracting only specific lines based on a comma-separated string of line numbers or ranges. It returns the selected lines concatenated into a single string.*


### extract_lines (function, L47-L62)

> *Summary: Parses a string containing an embedded marker to extract the target file path and optional line specification. It determines the base documentation directory and then reads the specified lines from that file using a helper function.*


### expand_markdown (function, L66-L77)

> *Summary: Reads a markdown file, processing each line to either pass it through unchanged or expand lines containing `{!>` markers by calling an external extraction function before writing the result to a specified output file.*


### remove_lines_between_dashes (function, L80-L100)

> *Summary: This function reads a file, searching for two consecutive lines containing only "---". If found, it removes all content between these markers and overwrites the original file with the modified content.*

