# Getting started

## Overview

Move's UGC API enables businesses and groups to construct tailored workflows or applications, addressing their unique requirements for mocap animation.
While our core API is built on GraphQL, this SDK provides a simple interface for interacting with the API and can be integrated into any python application.

### Installation

#### With pip:

```bash
pip install move-ugc-python
```
#### With poetry:

```bash
poetry add move-ugc-python
```

### Creating a file

```python
from move_ugc import MoveUgc
ugc = MoveUgc(api_key="YOUR_API_KEY")
video_file = ugc.files.create(file_type="mp4")
depth_file = ugc.files.create(file_type="move")
```

This will return a presigned URL that you can use to upload your video file to our servers.
Please refer to [this snippet](https://move-ai.github.io/move-ugc-api/getting-started/usage/files/#uploading-a-file-to-presignedurl) for a guide on how to upload a file to a presigned URL.
