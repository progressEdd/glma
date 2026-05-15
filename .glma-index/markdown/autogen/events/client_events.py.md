# autogen/events/client_events.py

1 function(s): _change_usage_summary_format. 5 class(es): ModelUsageSummary, ActualUsageSummary, TotalUsageSummary, UsageSummaryEvent, StreamEvent. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ModelUsageSummary | class |  |
| ActualUsageSummary | class |  |
| TotalUsageSummary | class |  |
| _change_usage_summary_format | function |  |
| UsageSummaryEvent | class |  |
| StreamEvent | class |  |

## Chunks

### ModelUsageSummary (class, L16-L28)

> *Summary: This data structure encapsulates a summary of model usage, holding the model name, and counts/costs for both input (prompt) and output (completion) tokens. It provides a comprehensive overview of resource consumption for an AI interaction.*


### ActualUsageSummary (class, L31-L37)

> *Summary: Represents a summary of actual resource consumption, holding an optional list of detailed usage records and the overall calculated total cost. It is structured using Pydantic's `BaseModel` for data validation.*


### TotalUsageSummary (class, L40-L46)

> *Summary: Represents a comprehensive overview of resource consumption, holding an optional list of detailed usage records and the overall calculated monetary cost. It structures the aggregated data for reporting purposes.*


### _change_usage_summary_format (function, L52-L72)

> *Summary: Transforms input usage summaries (actual and total) from a dictionary format into a standardized output structure. It restructures detailed usage entries by extracting model names and placing them within a list under the "usages" key for each summary type.*


### UsageSummaryEvent (class, L76-L146)

> *Summary: This class encapsulates usage summary data, holding actual and total cost breakdowns along with a display mode. It accepts optional dictionaries for the summaries and outputs formatted text to a provided callable based on the specified `mode` ("actual", "total", or "both").*


### __init__ (method, L86-L99, parent: UsageSummaryEvent)

> *Summary: Initializes an event object by accepting optional UUIDs and usage summaries for actual and total consumption. It standardizes the input usage dictionaries before passing them to the parent class constructor along with a specified operational mode.*


### _print_usage (method, L101-L120, parent: UsageSummaryEvent)

> *Summary: This method formats and prints a usage summary to a provided callable stream. It accepts either an actual or total usage summary object, determines the appropriate phrasing based on the `usage_type`, and iterates through individual usages to report costs and token counts.*


### print (method, L122-L146, parent: UsageSummaryEvent)

> *Summary: This method displays usage statistics based on a specified `mode` ("actual", "total", or both). It takes an optional callable function to handle output and prints either the actual or total cost summaries, including a comparison if both modes are requested.*


### StreamEvent (class, L150-L168)

> *Summary: Represents a stream event containing string content. It initializes with an optional UUID and required content, and its `print` method outputs the content to a provided file-like object in green terminal color.*


### __init__ (method, L156-L157, parent: StreamEvent)

> *Summary: Initializes an event object by accepting an optional unique identifier and a required string containing the event's content. It passes these values up to the parent class constructor for proper setup.*


### print (method, L159-L168, parent: StreamEvent)

> *Summary: This method outputs the object's content to a stream, first setting the terminal color to green and then resetting it afterward. It accepts an optional callable for outputting data.*

