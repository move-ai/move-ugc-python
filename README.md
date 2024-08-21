# Move UGC Python SDK

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-7F00FF.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![Python version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)
![Tests](https://github.com/move-ai/move-ugc-python/blob/main/badges/tests.svg)
![Coverage](https://github.com/move-ai/move-ugc-python/blob/main/badges/coverage.svg)
[![CI](https://github.com/move-ai/move-ugc-python/actions/workflows/ci.yml/badge.svg)](https://github.com/move-ai/move-ugc-python/actions/workflows/ci.yml)
![Documentation Style](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)

## Full documentation

The full documentation is available at https://move-ai.github.io/move-ugc-python/latest/

## Installation

### With pip:

```bash
pip install move-ugc-python
```
### With poetry:

```bash
poetry add move-ugc-python
```


## Initialize with your API key

```python
from move_ugc import MoveUgc
ugc = MoveUgc(api_key='<API_KEY>')
```

## Create a file and upload to move.ai

```python
video_file = ugc.files.create(file_type="mp4")
depth_file = ugc.files.create(file_type="move")

presigned_url = video_file['presigned_url'] 
filename = "<path to file on disk>"
with open(filename, 'rb') as f:
    requests.put(presigned_url, data=f.read())
    
presigned_url = depth_file['presigned_url'] 
filename = "<path to file on disk>"
with open(filename, 'rb') as f:
    requests.put(presigned_url, data=f.read())

```

## Retrieve a file

```python
video_file = ugc.files.retrieve(file_id="<FILE_ID>")
```


## Create a take

```python
    take = ugc.takes.create_singlecam(
        sources=[
            SourceIn(
                device_label="my-device",
                file_id=video_file.id,
                format=video_file.type
    )])
    ugc.jobs.create(take_id=take.id)
```

## Create a job
    
```python
    job = ugc.jobs.create(take_id=take.id)
```


## Contribution Guide

Information for how someone can contribute to this project can be found in our [documentation](https://move-ai.github.io/move-ugc-python/latest/contributing)