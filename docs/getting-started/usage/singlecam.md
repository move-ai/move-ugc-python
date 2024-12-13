# Singlecam Takes and Jobs

A singlecam take is a take that defines a recording session with only a single camera. A single take can be associated with a single video [source](/move-ugc-python/latest/api-reference/schemas/sources/) file and optional additional [source](/move-ugc-python/latest/api-reference/schemas/sources/) files.

## Creating files

Before creating a singlecam take, you must have a video file uploaded to the API. You can upload a video file using the [create file](/move-ugc-python/latest/getting-started/usage/file/#creating-a-file) method. You can use the same method to create any additional files as well if needed.

## Creating a singlecam take

First, create the singlecam take using the file ids that you have created and uploaded to the API.

Follow [this example](/move-ugc-python/latest/getting-started/usage/take/#creating-a-take) to create a singlecam take without any additional sources and [this example](/move-ugc-python/latest/getting-started/usage/take/#create-a-take-with-additional-files-ie-move-file) to create a singlecam take with additional sources.

## Processing a singlecam take

After creating a singlecam take, you can create a singlecam job using the take id. Please follow [this example](/move-ugc-python/latest/getting-started/usage/job/#creating-a-job) to create a singlecam job.

Apart from creating a job in the given example above, you can also provide specific outputs to be generated for the job. The available list of outputs is given [here](https://move-ai.github.io/move-ugc-api/schema/#outputtype).

```python
import json
job = ugc.jobs.create_singlecam(
    take_id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512",
    oututs=["MAIN_BLEND", "MAIN_GLB"],
    metadata=json.dumps({"foo": "bar"}),
)
```

> Note: After the job is processed successfully, and you provided specific outputs only the specified outputs will be generated. If you do not provide any outputs, all default outputs will be generated (render_video, main_fbx, main_usdc, main_usdz, main_blend, motion_data and render_overlay_video).
