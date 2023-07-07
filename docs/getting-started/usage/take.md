Takes are a way to define a recording session. A single take can be associated with a video file and optionally additional files.

> Currently, we only support additional file types: DEPTH, INTRINSIC, ODOMETRY, VISION

## Creating a take

To create a take you need at least a video file with optional additional file types mentioned above.

### Create a take with only a RGB video file

```python
take = ugc.takes.create(video_file_id="file-123-123-123-123")
```

### Create a take with additional files

```python
from move_ugc.schemas.additional_file import AdditionalFileIn, TakeAdditionalFileKeys
take = ugc.takes.create(
    video_file_id="file-123-123-123-123",
    additional_files=[
        AdditionalFileIn(
            key=TakeAdditionalFileKeys.depth,
            file_id="file-123-123-123-123",
        )
    ]
)
```

### Attaching some custom metadata with your take

The metadata attribute in take type excepts any valid json string and can contain any custom data. This is particularly useful if any business logic needs to be implemented such as attaching a user id to a take.

```python
import json
take = ugc.takes.create(
    video_file_id="file-123-123-123-123",
    metadata=json.dumps({"foo": "bar"}),
)
```