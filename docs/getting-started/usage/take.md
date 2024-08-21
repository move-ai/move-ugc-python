Takes are a way to define a recording session. A single take can be associated with a video file and optionally additional files.

> 💡 Additional files is a planned feature which is not supported right now, the plan is to support additional file types: DEPTH, INTRINSIC, ODOMETRY, VISION, MOVE
> Currently only MOVE files are supported as part of additional files which should contain a `.move` file.


## Prequisites

As a minimum requirement to create a take you need to have a video file. You can create a video file by following the [usage guide](/move-ugc-python/latest/getting-started/usage/file/).

## Creating a take

To create a take you need at least a video file with optional additional file types mentioned above.


```python
take = ugc.takes.create_singlecam(
    sources=[
        SourceIn(
            device_label="my-device",
            file_id="file-457e23c2-6afc-4913-91f6-36522245d57d",
            format="mp4"
        ),
])
```

### Create a take with additional files (i.e. move file)

```python

take = ugc.takes.create_singlecam(
    sources=[
        SourceIn(
            device_label="my-device",
            file_id="file-457e23c2-6afc-4913-91f6-36522245d57d",
            format="mp4",
        ),
        SourceIn(
            device_label="my-device",
            file_id="file-539c5313-ebfd-4eea-b3b1-92e1fd0a3bd0",
            format="move",
        )
])
```

### Attaching some custom metadata with your take

The metadata attribute in take type accepts any valid json string and can contain any custom data. This is particularly useful if any business logic needs to be implemented such as attaching a user id to a take.

```python
from move_ugc.schemas.sources import SourceIn

take = ugc.takes.create_singlecam(
    sources=[
        SourceIn(
            device_label="my-device",
            file_id="file-457e23c2-6afc-4913-91f6-36522245d57d",
            format="mp4",
    ),
    metadata={"foo": "bar"},
)
```

## Querying for a take

```python
take = ugc.takes.retrieve(id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512")
```

## Fetching associated sources with a take

```python
take = ugc.takes.retrieve(id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512", expand=["sources"])
```

> 💡 Currently supported attributes for expand are `client` and `sources`
> Please note that expand feature can only be used to fetch types which are 1 level deep i.e. you cannot perform an expansion of `sources.client`.
> To fetch a client associated with a video_file you need to perform a [separate request](/move-ugc-python/latest/getting-started/usage/file/#retrieving-an-existing-file).

## Updating a take

To update a take you can use the `ugc.takes.update` method:

```python
take = ugc.takes.update(
    id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512",
    metadata={"foo": "bar"},
)
```

## Listing takes

To list all the takes you can use the `ugc.takes.list` method:

```python
# By default this will return 10 takes at a time
takes = ugc.takes.list()

# Fetch N takes at a time
N = 20
takes = ugc.takes.list(limit=N)

# Get next N takes
next_takes = ugc.takes.list(limit=N, next_token=takes.next_token)

# By default, takes are sorted by created_at in descending order. To sort by ascending order, use the sort_by parameter
from move_ugc.schemas.commons import SortDirection
takes = ugc.takes.list(sort_by=SortDirection.ASC)

# You can also expand the associated types with the take just like with .retrieve()
takes = ugc.takes.list(expand=["sources", "client"])
```

For more information on the take object, see the [API reference](/move-ugc-python/latest/api-reference/schemas/take/).
