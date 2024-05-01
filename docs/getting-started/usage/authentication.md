This package requires an api key to be set in the MoveUgc object to authenticate with the MoveUGC API.

## Creating a MoveUgc object

```python
from move_ugc import MoveUgc

ugc = MoveUgc(api_key="*************")
```

The `ugc` object can then be used to access the various types provided by the Move UGC API. For example, to create a take, you can use the `ugc.takes.create` method.

> 💡 api_key is a required parameter for MoveUgc object.
