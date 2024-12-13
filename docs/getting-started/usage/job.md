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
job = ugc.jobs.create_singlecam(
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


## Listing jobs

To list jobs created by your client, use the `list` method given below:

```python
# By default this will return 10 takes at a time
jobs = ugc.jobs.list()

# Fetch N jobs at a time
N = 20
jobs = ugc.jobs.list(limit=N)

# Get next N jobs
next_jobs = ugc.jobs.list(limit=N, next_token=jobs.next_token)

# By default, jobs are sorted by created_at in descending order. To sort by ascending order, use the sort_by parameter
from move_ugc.schemas.commons import SortDirection
jobs = ugc.jobs.list(sort_by=SortDirection.ASC)

# You can also expand the associated types with the jobs just like with .retrieve()
jobs = ugc.jobs.list(expand=["take", "outputs", "client"])
```

## Updating a job

To update a job you can use the `ugc.jobs.update` method:

```python
job = ugc.jobs.update(
    id="job-2be2463e-ffa3-419b-beb4-ea0f99c79512",
    metadata={"foo": "bar"},
)
```

For more information on the job object, see the [API reference](/move-ugc-python/latest/api-reference/schemas/job/).


## Creating a multicam job

To create a multicam job, you can use the `create_multicam` method:

```python
job = ugc.jobs.create_multicam(
    take_id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512",
    options=JobOptions(track_fingers=True),
    name="My multicam job",
)
```

See the [API reference](/move-ugc-python/latest/api-reference/services/job/#move_ugc.schemas.job.JobOptions) for more information on available job options for multicam.

See quickstart guide [here](https://move-ai.github.io/move-ugc-api/getting-started/multicam/quickstart/) for steps to create a multicam job. Please use the equivalent methods in the SDK to create a multicam job.