Jobs are the processing entity in MoveUGC. By creating a Job, you can initiate the processing for a take.
A job can have multiple output types, currently the only output types supported are `mp4` and `fbx` files.

## Prerequisites

Before creating a job, please make sure that a take is created. If you've not created a take please refer to [this usage guide](/move-ugc-python/latest/getting-started/usage/take/).

## Creating a job

```python
job = ugc.jobs.create(take_id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512")
```

## Attaching some custom metadata with your job

The metadata attribute in job type accepts any valid json string and can contain any custom data. This is particularly useful if any business logic needs to be implemented such as attaching a user id to a job.

```python
job = ugc.jobs.create(
    take_id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512",
    metadata=json.dumps({"foo": "bar"}),
)
```

## Retrieving a job

```python
job = ugc.jobs.retrieve(id="job-2be2463e-ffa3-419b-beb4-ea0f99c79512")
```

## Retrieving a job with its nested resources

```python
job = ugc.jobs.retrieve(
    id="job-2be2463e-ffa3-419b-beb4-ea0f99c79512", expand=["take", "outputs", "client"]
)
```

> 💡 `expand` supports only `take`, `outputs` and `client` as of now.