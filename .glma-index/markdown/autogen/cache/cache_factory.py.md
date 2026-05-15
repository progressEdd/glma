# autogen/cache/cache_factory.py

1 class(es): CacheFactory. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CacheFactory | class |  |

## Chunks

### CacheFactory (class, L16-L104)

> *Summary: This function acts as a factory, determining and instantiating an appropriate caching mechanism based on configuration inputs like Redis URLs or Cosmos DB credentials. It prioritizes creating `RedisCache`, then `CosmosDBCache`, falling back sequentially to `DiskCache` (if available), and finally defaulting to `InMemoryCache`.*


### cache_factory (method, L18-L104, parent: CacheFactory)

> *Summary: This function acts as a factory, constructing and returning an appropriate caching implementation based on configuration inputs. It prioritizes creating `RedisCache` if a Redis URL is provided, then attempts `CosmosDBCache` with specific database credentials, falling back sequentially to `DiskCache` (if available) or finally defaulting to `InMemoryCache`.*

