# autogen/tools/experimental/crawl4ai/crawl4ai.py

1 class(es): Crawl4AITool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Crawl4AITool | class |  |

## Chunks

### Crawl4AITool (class, L27-L184)

> *Summary: This class provides a unified interface to crawl websites using `crawl4ai`, supporting both simple content extraction and advanced LLM-based information extraction. It accepts an optional URL, along with configuration for the LLM, extraction schema, and instructions, determining whether to use the simpler or more complex extraction path based on provided inputs.*


### __init__ (method, L30-L89, parent: Crawl4AITool)

> *Summary: Initializes the tool by setting up internal helper functions for web crawling. It configures which execution path to use—either a basic crawl without an LLM or a sophisticated crawl that uses an LLM for extraction—based on provided configuration parameters.*


### _validate_llm_strategy_kwargs (method, L92-L118, parent: Crawl4AITool)

> *Summary: Ensures that provided LLM strategy arguments are valid by checking for the presence of configuration-dependent or externally supplied parameters. It raises a `ValueError` if keys like `provider`, `api_token`, `schema`, or `instruction` are present in the input dictionary when they should be derived elsewhere.*


### _get_crawl_config (method, L121-L184, parent: Crawl4AITool)

> *Summary: This method constructs a `CrawlerRunConfig` by determining the appropriate extraction strategy based on provided LLM configuration and model schema. It processes inputs like an LLM config, instruction, and optional model to instantiate either an advanced or legacy LLM extraction strategy before returning the final configuration object.*

