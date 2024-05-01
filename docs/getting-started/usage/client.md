A client object represents your client in MoveUGC. It is the main resource in the SDK. It is the client that is associated to your api-key and may contain any metadata you would want to associated to it.

> 💡 You don't need to specify the client id when retrieving or updating your client object. 

## Retrieving a client

To fetch your client from MoveUGC you can use the `ugc.client.retrieve` method:

```python
client = ugc.client.retrieve()
```

## Updating your client with metadata

To update your client with metadata, you can use the `ugc.client.update` method:

```python
import json
metadata = {"foo": "bar"}
client = ugc.client.update(metadata=metadata)
```

For more information on the client object, see the [API reference](/move-ugc-python/latest/api-reference/schemas/client/).
