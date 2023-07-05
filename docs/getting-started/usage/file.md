Files are the main resource in the SDK. They are the files that you want to associate to a take and eventually generate animations from.

## Creating a file 

To create a file, you need to specify the type of file you want to create:

Sample: Creating an `mp4` file.

```python
file = ugc.files.create(file_type="mp4")
```

This will return a pydantic object with the fields mentioned [here](/move-ugc-python/latest/api-reference/schemas/file/).

> 💡 You can fetch the client in the same request by passing `expand=["client"]` to
> either `ugc.files.create` or `ugc.files.retrieve`.


## Retrieving an existing file

To fetch an existing file from MoveUGC you can use the `ugc.files.retrieve` method:

```python
file = ugc.files.retrieve(file_id="file-123-123-123-123")
```
