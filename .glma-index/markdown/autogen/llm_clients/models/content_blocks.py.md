# autogen/llm_clients/models/content_blocks.py

12 class(es): ContentType, BaseContent, TextContent, ImageContent, AudioContent, VideoContent, ReasoningContent, CitationContent, ToolCallContent, ToolResultContent, GenericContent, ContentParser. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ContentType | class |  |
| BaseContent | class |  |
| TextContent | class |  |
| ImageContent | class |  |
| AudioContent | class |  |
| VideoContent | class |  |
| ReasoningContent | class |  |
| CitationContent | class |  |
| ToolCallContent | class |  |
| ToolResultContent | class |  |
| GenericContent | class |  |
| ContentParser | class |  |

## Chunks

### ContentType (class, L26-L40)

> *Summary: Defines a set of predefined string constants representing supported content types like text, image, and video. This enumeration ensures type safety when identifying the nature of different data blocks within the system.*


### BaseContent (class, L48-L71)

> *Summary: Provides a foundational structure for various content types, enforcing a `ContentType` and allowing arbitrary provider-specific data via an `extra` dictionary. It mandates a `get_text()` method that subclasses must override to define how their specific content should be represented as text.*


### get_text (method, L65-L71, parent: BaseContent)

> *Summary: Provides a default method to extract the textual representation from a content block, returning an empty string if no specific extraction logic is implemented by a subclass. This acts as a fallback mechanism for retrieving text content.*


### TextContent (class, L79-L87)

> *Summary: Represents a simple block of plain text, storing the content in its `text` attribute. It provides a method to retrieve this stored string value.*


### get_text (method, L85-L87, parent: TextContent)

> *Summary: Retrieves the stored string content from the object's internal `text` attribute and returns it as a standard Python string.*


### ImageContent (class, L90-L105)

> *Summary: Represents image content, accepting either a remote `image_url` or base64-encoded `data_uri`. It also allows specifying an optional processing `detail` level ("auto", "low", or "high").*


### AudioContent (class, L108-L127)

> *Summary: Represents audio content, accepting either a remote URL or base64-encoded data URI for the audio source, along with an optional transcript. It provides a method to retrieve the associated text transcript if one is present.*


### get_text (method, L123-L127, parent: AudioContent)

> *Summary: Retrieves the stored audio transcript, prepending it with a specific prefix if available. Returns an empty string otherwise.*


### VideoContent (class, L130-L144)

> *Summary: Represents a video content block that can be sourced either from a remote HTTP/S URL or directly from base64-encoded data. It requires providing one of the two fields, `video_url` or `data_uri`, to define its content.*


### ReasoningContent (class, L147-L156)

> *Summary: Represents content specifically for chain-of-thought or reasoning, holding the core `reasoning` string and an optional `summary`. It provides a method to retrieve only the detailed reasoning text.*


### get_text (method, L154-L156, parent: ReasoningContent)

> *Summary: Retrieves the stored reasoning text from the object's internal `reasoning` attribute and returns it as a string.*


### CitationContent (class, L159-L172)

> *Summary: Represents a web search reference, storing the URL, title, snippet, and optional relevance score. It provides a method to return a formatted string containing only the citation's title.*


### get_text (method, L168-L172, parent: CitationContent)

> *Summary: Retrieves the citation's title, prepending "citation: " if a title exists; otherwise, it returns an empty string. This method is used to format and extract the textual representation of the citation's name.*


### ToolCallContent (class, L175-L185)

> *Summary: Represents a request to invoke an external tool or function, holding the tool's name and its serialized arguments. It provides a method to serialize this structured call into a human-readable string format.*


### get_text (method, L183-L185, parent: ToolCallContent)

> *Summary: Retrieves the structured content of a tool call by formatting its name and arguments into a single string representation. This method takes no input and outputs a descriptive string detailing the intended tool invocation.*


### ToolResultContent (class, L188-L197)

> *Summary: Represents the output from a tool or function execution, storing a unique `tool_call_id` and the resulting string `output`. It provides a method to format this result into a human-readable text string prefixed with "tool result: ".*


### get_text (method, L195-L197, parent: ToolResultContent)

> *Summary: Retrieves the stored output from the object and formats it into a string prefixed with "tool result: ". This method returns the final textual representation of the tool's execution outcome.*


### GenericContent (class, L205-L285)

> *Summary: This class serves as a fallback container for content blocks with unknown types, preserving all incoming data via Pydantic's extra fields mechanism. It provides methods to retrieve specific fields by name, access all stored data, or isolate only the unrecognized attributes.*


### get (method, L236-L247, parent: GenericContent)

> *Summary: Retrieves a value from the object either from its extra attributes or as a standard attribute if it's not found in `model_extra`. It accepts a string key and an optional default value, returning the corresponding data.*


### get_all_fields (method, L249-L257, parent: GenericContent)

> *Summary: Retrieves all defined and extra fields from the object as a single dictionary by calling `model_dump()`. This method provides a complete snapshot of the instance's data.*


### get_extra_fields (method, L259-L267, parent: GenericContent)

> *Summary: Retrieves any fields from the model instance that are not explicitly defined within its schema. It returns these unknown fields as a dictionary, or an empty dictionary if none exist.*


### has_field (method, L269-L276, parent: GenericContent)

> *Summary: Determines if an object possesses a specific attribute by checking its available members. It returns `True` if the provided string key corresponds to an existing field or extra attribute on the instance.*


### data (method, L280-L285, parent: GenericContent)

> *Summary: Provides backward compatibility by returning all extra fields associated with the object as a dictionary. This method is deprecated in favor of `get_extra_fields()` or accessing `model_extra`.*


### ContentParser (class, L293-L367)

> *Summary: This class parses input dictionaries into specific content objects based on a registered type registry. It attempts to instantiate the known type; if the type is unknown or parsing fails, it gracefully falls back to returning a `GenericContent` object to ensure data preservation and forward compatibility.*


### register (method, L324-L336, parent: ContentParser)

> *Summary: This method adds a new content type to the system's registry by mapping a string identifier (`content_type`) to its corresponding class (`content_class`). It allows external classes inheriting from `BaseContent` to be recognized and used within the framework.*


### parse (method, L339-L367, parent: ContentParser)

> *Summary: This method deserializes a dictionary of content data into a specific `BaseContent` type if its `"type"` field matches a known registry entry. If the type is unknown or parsing fails for any reason, it safely defaults to returning a `GenericContent` instance instead of raising an error.*

