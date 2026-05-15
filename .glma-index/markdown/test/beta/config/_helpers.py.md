# test/beta/config/_helpers.py

2 function(s): make_parameterless_tool, make_tool. 1 class(es): ToolStub.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ToolStub | class |  |
| make_parameterless_tool | function |  |
| make_tool | function |  |

## Chunks

### ToolStub (class, L11-L13)

> *Summary: Represents a placeholder for a tool, holding its name and the associated function schema. It serves as a basic structure to define tool metadata without implementing actual functionality.*


### make_parameterless_tool (function, L16-L26)

> *Summary: Creates a `ToolStub` instance representing an action that requires no arguments. This stub is configured to prompt the user by having a schema defined with null parameters.*


### make_tool (function, L29-L46)

> *Summary: Creates and returns a `ToolStub` instance configured to represent a documentation search capability. This tool accepts a required string query and an optional integer limit for the search operation.*

