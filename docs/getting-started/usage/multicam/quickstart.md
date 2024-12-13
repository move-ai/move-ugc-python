# Multicam Takes and Jobs

Before you begin, make sure you have read the [quickstart](https://help.move.ai/en/articles/8958773-move-pro-quickstart-guide) guide. This provides useful hints and tips on what equipment you need as well as general advice to get the most out of the multicam API.

A multicam take is a take that defines a recording session with multiple cameras. The process for creating mocap outputs for a multicam take has a few more steps than for [singlecam](/move-ugc-python/latest/getting-started/usage/singlecam) - but the output is generally of much higher quality.

## 1. Create calibration files

First, you need to calibrate your volume. Once you have setup your cameras and recorded your calibration videos you can upload them as normal using the files service's [create](/move-ugc-python/latest/api-reference/services/file/#move_ugc.services.file.FileService.create) method. See [here](https://move-ai.github.io/move-ugc-api/getting-started/usage/files/#uploading-a-file-to-presignedurl) for how to upload the files.

See our articles [here](https://help.move.ai/en/articles/8857646-framing-up-your-cameras) for how best to setup your cameras and [here](https://help.move.ai/en/articles/8953430-recording-a-calibration) for how to record a calibration.

## 2. Create calibration volume

Once you have created your calibration files you can now create the volume.

See the sdk docs [here](/move-ugc-python/latest/api-reference/services/volume/#move_ugc.services.volume.VolumeService.create_human_volume) for more information on the attributes on `create_human_volume` mutation. Only certain camera lenses are supported at the moment. See [here](/move-ugc-python/latest/api-reference/services/camera_settings/#move_ugc.services.camera_settings.CameraSettingsService.list) for a complete list.

Please see the example below for how to create a volume with two sources:

```python
from move_ugc.schemas.sources import ClipWindow, SourceIn, TakeSourceKey
from move_ugc.schemas.volume import AreaType
ugc.volumes.create_human_volume(
    sources=[
        SourceIn(
            source_id="source-1",
            clip_window=ClipWindow(
                start_time=0,
                end_time=10,
            ),
            file_id="file-2be2463e-ffa3-419b-beb4-ea0f99c79592",
            format=TakeSourceKey.MP4,
            camera_settings={
                "lens": "goprohero9-fhd",
            }
        ),
        SourceIn(
            source_id="source-2",
            clip_window=ClipWindow(
                start_time=0,
                end_time=10,
            ),
            file_id="file-edcf5b93-24b4-45b8-91b2-0985c4c44665",
            format=TakeSourceKey.MP4,
            camera_settings={
                "lens": "goprohero9-fhd",
            }
        ),
    ],
    human_height=1.8,
    area_type=AreaType.NORMAL,
    name="My volume",
)
```

## 3. Create multicam files

You can now shoot your take using the same camera configuration as you used for the calibration. Upload the files in the [same way](/move-ugc-python/latest/getting-started/usage/file/#creating-a-file) as you do for calibration.

## 4. Create take

Before creating the take ensure that the volume has finished processing. Use the volume id provided from the creation of the volume in step 2.
You can confirm this using [this](/move-ugc-python/latest/api-reference/services/volume/#move_ugc.services.volume.VolumeService.retrieve_human_volume) method in the volumes service.

```python
volume = ugc.volumes.retrieve_human_volume(volume_id="volume-2be2463e-ffa3-419b-beb4-ea0f99c79512")
print(volume.state) # this should be FINISHED
```

Once the volume has finished processing and the files for the take are uploaded you can then create a take object using `create_multicam` method [here](/move-ugc-python/latest/api-reference/services/take/#move_ugc.services.take.TakeService.create_multicam).

```python
take = ugc.takes.create_multicam(
    sources=[
        SourceIn(
            source_id="source-1",
            clip_window=ClipWindow(
                start_time=0,
                end_time=10,
            ),
            file_id="file-2be2463e-ffa3-419b-beb4-ea0f99c79592",
            format=TakeSourceKey.MP4,
            camera_settings={
                "lens": "goprohero9-fhd",
            }
        ),
        SourceIn(
            source_id="source-2",
            clip_window=ClipWindow(
                start_time=0,
                end_time=10,
            ),
            file_id="file-edcf5b93-24b4-45b8-91b2-0985c4c44665",
            format=TakeSourceKey.MP4,
            camera_settings={
                "lens": "goprohero9-fhd",
            }
        ),
    ],
    volume_id="volume-2be2463e-ffa3-419b-beb4-ea0f99c79512",
)
```

## 5. Process multicam take (create a job)

You can now create the job which will generate the mocap output for the take using the ID generated in step 4. See the api reference [here](/move-ugc-python/latest/api-reference/services/job/#move_ugc.services.job.JobService.create_multicam) for more information on the attributes on create_multicam job method.

### Processing with default outputs

Unless specified, Multicam runs will generate the following default output files: render_video, main_fbx, main_usdc, main_usdz, main_blend and motion_data.

```python
job = ugc.jobs.create_multicam(
    take_id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512",
    number_of_actors=1,
)
```

### Processing with specific outputs

You can also specify the outputs you want to generate by passing the outputs parameter. You can find the list of available outputs [here](https://move-ai.github.io/move-ugc-api/schema/#outputtype).

```python
job = ugc.jobs.create_multicam(
    take_id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512",
    number_of_actors=1,
    outputs=["MAIN_BLEND", "MAIN_GLB", "RENDER_VIDEO"],
)
```