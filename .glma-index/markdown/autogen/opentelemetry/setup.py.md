# autogen/opentelemetry/setup.py

1 function(s): get_tracer. 1 class(es): DropNoiseSampler. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DropNoiseSampler | class |  |
| get_tracer | function |  |

## Chunks

### DropNoiseSampler (class, L18-L33)

> *Summary: This sampler decides whether to record or sample a span based on its name; if the name starts with "a2a.", it records only, otherwise, it records and samples. It provides a description indicating that it drops noisy spans prefixed with "a2a.".*


### should_sample (method, L19-L30, parent: DropNoiseSampler)

> *Summary: Determines the sampling decision for a span based on its name; it defaults to recording only if the name starts with "a2a." otherwise, it records and samples. It accepts various context details like parent context, IDs, attributes, and links as input and returns a `SamplingResult`.*


### get_description (method, L32-L33, parent: DropNoiseSampler)

> *Summary: Returns a static string describing the purpose of dropping noisy spans from `a2a.server`. This method takes no inputs and outputs a descriptive string.*


### get_tracer (function, L36-L41)

> *Summary: Retrieves a specific OpenTelemetry tracer instance from a provided `TracerProvider`. It configures the returned tracer with predefined module and library names, along with a specified schema URL.*

