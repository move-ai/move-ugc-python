Files are the main resource in the SDK. They are the files that you want to associate to a take and eventually generate animations from.

## Creating a file 

To create a file, you need to specify the type of file you want to create:

Sample: Creating an `mp4` file.

```python
import json

# Create a file without metadata
file = ugc.files.create(file_type="mp4")

# Create a file with metadata
file_metadata = {"foo": "bar"}
file = ugc.files.create(file_type="mp4", metadata=json.dumps(file_metadata))

# Create a file and fetch the client data in the same request
file = ugc.files.create(file_type="mp4", expand=["client"])
```

This will return a pydantic object with the fields mentioned [here](/move-ugc-python/latest/api-reference/schemas/file/).

> 💡 You can fetch the client in the same request by passing `expand=["client"]` to
> either `ugc.files.create` or `ugc.files.retrieve`.


## Retrieving an existing file

To fetch an existing file from MoveUGC you can use the `ugc.files.retrieve` method:

```python
# Retrieve a file on its own
file = ugc.files.retrieve(id="file-123-123-123-123")

# Retrieve a file and fetch the client data in the same request
file = ugc.files.retrieve(id="file-123-123-123-123", expand=["client"])
```


## Updating an existing file with metadata

To update an existing file with metadata, you can use the `ugc.files.update` method:

```python
import json

# Update a file with metadata
file_metadata = {"foo": "bar"}
file = ugc.files.update(id="file-123-123-123-123", metadata=json.dumps(file_metadata))

# Update a file and fetch the client data in the same request
file = ugc.files.update(
    id="file-123-123-123-123", metadata=json.dumps(file_metadata), expand=["client"],
)
```

For more information on the file object, see the [API reference](/move-ugc-python/latest/api-reference/schemas/file/).
