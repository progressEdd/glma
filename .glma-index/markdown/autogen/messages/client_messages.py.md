# autogen/messages/client_messages.py

1 function(s): _change_usage_summary_format. 5 class(es): ModelUsageSummary, ActualUsageSummary, TotalUsageSummary, UsageSummaryMessage, StreamMessage. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ModelUsageSummary | class |  |
| ActualUsageSummary | class |  |
| TotalUsageSummary | class |  |
| _change_usage_summary_format | function |  |
| UsageSummaryMessage | class |  |
| StreamMessage | class |  |

## Chunks

### ModelUsageSummary (class, L18-L30)

> *Summary: This data structure encapsulates a summary of model interaction, holding the model name, and counts/costs for both input (prompt) and output (completion) tokens. It provides a comprehensive overview of resource consumption during an AI call.*


### ActualUsageSummary (class, L33-L39)

> *Summary: Represents a summary of actual model usage, containing an optional list of detailed usage records and the overall total cost as a floating-point number. It serves to encapsulate billing or consumption metrics for a given operation.*


### TotalUsageSummary (class, L42-L48)

> *Summary: Represents a comprehensive overview of resource consumption, holding an optional list of detailed usage breakdowns and the overall calculated monetary cost. It is structured using Pydantic's `BaseModel` for data validation.*


### _change_usage_summary_format (function, L54-L74)

> *Summary: Transforms raw usage dictionaries, provided as actual and total summaries, into a standardized format. It restructures nested usage data by extracting model names into a list of individual usage records under the "usages" key for each summary type.*


### UsageSummaryMessage (class, L79-L149)

> *Summary: This class structures and manages usage summary data, accepting optional actual and total usage dictionaries along with a display `Mode`. It provides methods to print the summary to a specified output function, displaying either actual, total, or both usages based on the configured mode.*


### __init__ (method, L89-L102, parent: UsageSummaryMessage)

> *Summary: Initializes a message object by accepting optional UUIDs and usage summaries for both actual and total consumption. It transforms the provided usage dictionaries before passing them to the parent class constructor along with a specified operational mode.*


### _print_usage (method, L104-L123, parent: UsageSummaryMessage)

> *Summary: This method formats and prints a usage summary based on provided cost data. It accepts either an actual or total usage summary object, determines the appropriate phrasing ("including" or "excluding"), and iterates through individual usages to display model-specific costs and token counts.*


### print (method, L125-L149, parent: UsageSummaryMessage)

> *Summary: This method displays a usage summary based on the object's configured `mode` ("actual", "total", or both). It takes an optional callable function to handle output and prints either the actual or total costs, including a specific message if no usage data is available.*


### StreamMessage (class, L154-L172)

> *Summary: Represents a message intended for streaming output, holding string content and an optional UUID. It prints its content to a provided stream or standard output, formatting it in green terminal text.*


### __init__ (method, L160-L161, parent: StreamMessage)

> *Summary: Initializes a message object by accepting an optional unique identifier and a required string containing the message content. It passes these values up to the parent class constructor for storage.*


### print (method, L163-L172, parent: StreamMessage)

> *Summary: This method outputs the object's content to a stream, prepending it with green ANSI color codes and appending a newline after resetting the color. It accepts an optional callable to control where the output is directed.*

