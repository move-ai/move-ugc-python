# Move UGC Python SDK

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-7F00FF.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![Python version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)
![Tests](./badges/tests.svg)
![Coverage](./badges/coverage.svg)
[![CI](https://github.com/move-ai/move-ugc-python/actions/workflows/ci.yml/badge.svg?branch=main&event=workflow_run)](https://github.com/move-ai/move-ugc-python/actions/workflows/ci.yml)
![Documentation Style](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)

## Full documentation

The full documentation is available at https://move-ai.github.io/move-ugc-python/

## Installation

### With pip:

```bash
pip install move-ugc
```
### With poetry:

```bash
poetry add move-ugc
```


## Initialize with your API key

```python
from move_ugc import MoveUgc
ugc = MoveUgc(api_key='<API_KEY>')
```

## Create a file

```python
video_file = ugc.files.create(file_type="mp4")
depth_file = ugc.files.create(file_type="move")
```

## Retrieve a file

```python
video_file = ugc.files.get(file_id="<FILE_ID>")
```
