# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestVolumeService.test_create[empty_expand] create_mutation_expand_[]"] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String, $clip_window: ClipWindowInput) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
    clipWindow: $clip_window
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    progress {
      state
      percentageComplete
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "areaType": "NORMAL",
            "clip_window": {
                "endTime": 9057.0,
                "startTime": 3757.0,
            },
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "deviceLabel": "realize",
                    "fileId": "530e9daa-0d45-45a7-a849-1a43874a50b9",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "deviceLabel": "realize",
                    "fileId": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
                    "format": "MOVE",
                },
            ],
            "syncMethod": None,
        },
    },
]

snapshots["TestVolumeService.test_create[empty_expand] create_response_expand_[]"] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": None,
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_create[expand_additional_sources] create_mutation_expand_sources"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String, $clip_window: ClipWindowInput) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
    clipWindow: $clip_window
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    progress {
      state
      percentageComplete
    }
    sources {
      deviceLabel
      file {
        id
        created
        type
        metadata
        name
        presignedUrl
        thumbnailUrl
        __typename
      }
      cameraSettings {
        lens
      }
      format
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "areaType": "NORMAL",
            "clip_window": {
                "endTime": 9057.0,
                "startTime": 3757.0,
            },
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "deviceLabel": "realize",
                    "fileId": "530e9daa-0d45-45a7-a849-1a43874a50b9",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "deviceLabel": "realize",
                    "fileId": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
                    "format": "MOVE",
                },
            ],
            "syncMethod": None,
        },
    },
]

snapshots[
    "TestVolumeService.test_create[expand_additional_sources] create_response_expand_sources"
] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": "2023-07-03T14:48:06.029019Z",
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "UmKdTFlLMIuIvJkRJnoM",
                    "decade": "zAvJMvacZIYSmMsDUNvC",
                    "director": "KNmpExWtgQLcAEuRyBkN",
                    "draw": "PnbQcVNCliYtuFCSJkGb",
                    "house": "aYyOUXkJPUjPJGpDdakX",
                    "huge": "eFaLyHGEQQpSzpRFSYEm",
                    "last": "dnZCcfgZNBnaEkbOzIyO",
                    "other": "XbBPNrbhtJksbBuoWXSK",
                    "table": "ACMVZcKAiGBcYgCzHAad",
                    "trouble": "UgnhIyaDJzohUigyDYZf",
                },
                "name": "",
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "MP4",
        },
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": "2023-07-03T14:48:06.029019Z",
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "UmKdTFlLMIuIvJkRJnoM",
                    "decade": "zAvJMvacZIYSmMsDUNvC",
                    "director": "KNmpExWtgQLcAEuRyBkN",
                    "draw": "PnbQcVNCliYtuFCSJkGb",
                    "house": "aYyOUXkJPUjPJGpDdakX",
                    "huge": "eFaLyHGEQQpSzpRFSYEm",
                    "last": "dnZCcfgZNBnaEkbOzIyO",
                    "other": "XbBPNrbhtJksbBuoWXSK",
                    "table": "ACMVZcKAiGBcYgCzHAad",
                    "trouble": "UgnhIyaDJzohUigyDYZf",
                },
                "name": "",
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "MOVE",
        },
    ],
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_create[expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String, $clip_window: ClipWindowInput) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
    clipWindow: $clip_window
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    progress {
      state
      percentageComplete
    }
    client {
      id
      name
      created
      metadata
      portal
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "areaType": "NORMAL",
            "clip_window": {
                "endTime": 9057.0,
                "startTime": 3757.0,
            },
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "deviceLabel": "realize",
                    "fileId": "530e9daa-0d45-45a7-a849-1a43874a50b9",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "deviceLabel": "realize",
                    "fileId": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
                    "format": "MOVE",
                },
            ],
            "syncMethod": None,
        },
    },
]

snapshots[
    "TestVolumeService.test_create[expand_client] create_response_expand_client"
] = {
    "area_type": "NORMAL",
    "client": {
        "created": "2023-06-12T00:00:00Z",
        "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
        "metadata": {
            "foo": "bar",
        },
        "name": "PYTEST_INVALID_CLIENT_NAME",
        "portal": "https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=",
    },
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": None,
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_create[expand_clip_window] create_mutation_expand_clipWindow"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String, $clip_window: ClipWindowInput) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
    clipWindow: $clip_window
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    progress {
      state
      percentageComplete
    }
    clipWindow {
      startTime
      endTime
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "areaType": "LARGE",
            "clip_window": {
                "endTime": 5315.0,
                "startTime": 849.0,
            },
            "humanHeight": 59816290182492.2,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "draw",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "set",
                    },
                    "deviceLabel": "newspaper",
                    "fileId": "37bea600-bdc6-4ffa-86c7-a4f634c4614f",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "evening",
                    },
                    "deviceLabel": "newspaper",
                    "fileId": "cba1d785-4a1e-4b59-aca4-d775bfdde401",
                    "format": "MOVE",
                },
            ],
            "syncMethod": None,
        },
    },
]

snapshots[
    "TestVolumeService.test_create[expand_clip_window] create_response_expand_clipWindow"
] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 9057.0,
        "start_time": 9057.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": None,
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_create[expand_video_file] create_mutation_expand_sources"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String, $clip_window: ClipWindowInput) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
    clipWindow: $clip_window
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    progress {
      state
      percentageComplete
    }
    sources {
      deviceLabel
      file {
        id
        created
        type
        metadata
        name
        presignedUrl
        thumbnailUrl
        __typename
      }
      cameraSettings {
        lens
      }
      format
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "areaType": "NORMAL",
            "clip_window": {
                "endTime": 9057.0,
                "startTime": 3757.0,
            },
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "deviceLabel": "realize",
                    "fileId": "530e9daa-0d45-45a7-a849-1a43874a50b9",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "deviceLabel": "realize",
                    "fileId": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
                    "format": "MOVE",
                },
            ],
            "syncMethod": None,
        },
    },
]

snapshots[
    "TestVolumeService.test_create[expand_video_file] create_response_expand_sources"
] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": "2023-07-03T14:48:06.029019Z",
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "UmKdTFlLMIuIvJkRJnoM",
                    "decade": "zAvJMvacZIYSmMsDUNvC",
                    "director": "KNmpExWtgQLcAEuRyBkN",
                    "draw": "PnbQcVNCliYtuFCSJkGb",
                    "house": "aYyOUXkJPUjPJGpDdakX",
                    "huge": "eFaLyHGEQQpSzpRFSYEm",
                    "last": "dnZCcfgZNBnaEkbOzIyO",
                    "other": "XbBPNrbhtJksbBuoWXSK",
                    "table": "ACMVZcKAiGBcYgCzHAad",
                    "trouble": "UgnhIyaDJzohUigyDYZf",
                },
                "name": "",
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "MP4",
        },
    ],
    "state": "RUNNING",
}

snapshots["TestVolumeService.test_create[no_expand] create_mutation_expand_None"] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String, $clip_window: ClipWindowInput) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
    clipWindow: $clip_window
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    progress {
      state
      percentageComplete
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "areaType": "NORMAL",
            "clip_window": {
                "endTime": 9057.0,
                "startTime": 3757.0,
            },
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "deviceLabel": "realize",
                    "fileId": "530e9daa-0d45-45a7-a849-1a43874a50b9",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "deviceLabel": "realize",
                    "fileId": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
                    "format": "MOVE",
                },
            ],
            "syncMethod": None,
        },
    },
]

snapshots["TestVolumeService.test_create[no_expand] create_response_expand_None"] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": None,
    "state": "RUNNING",
}

snapshots["TestVolumeService.test_fetch_service 1"] = GenericRepr(
    "VolumeService(api_key=SecretStr('**********'), endpoint_url=HttpUrl('https://pytest_invalid_endpoint_url.com/'))",
)

snapshots["TestVolumeService.test_list list_response"] = {
    "items": [
        {
            "area_type": "NORMAL",
            "client": None,
            "clip_window": {
                "end_time": 10.0,
                "start_time": 10.0,
            },
            "created": "2023-06-29T08:54:52.349467Z",
            "human_height": 1.5,
            "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
            "metadata": {
                "analysis": "UmKdTFlLMIuIvJkRJnoM",
                "decade": "zAvJMvacZIYSmMsDUNvC",
                "director": "KNmpExWtgQLcAEuRyBkN",
                "draw": "PnbQcVNCliYtuFCSJkGb",
                "house": "aYyOUXkJPUjPJGpDdakX",
                "huge": "eFaLyHGEQQpSzpRFSYEm",
                "last": "dnZCcfgZNBnaEkbOzIyO",
                "other": "XbBPNrbhtJksbBuoWXSK",
                "table": "ACMVZcKAiGBcYgCzHAad",
                "trouble": "UgnhIyaDJzohUigyDYZf",
            },
            "name": "fake_volume",
            "outputs": None,
            "progress": {
                "percentage_complete": 50,
                "state": "RUNNING",
            },
            "sources": None,
            "state": "RUNNING",
        },
    ],
    "limit": 3757,
    "next_token": {
        "agreement": "IROVLfjoMfevqGQzKwSq",
        "area": "MGeUnKHFDBnmrDQHVgvC",
        "contain": "ItsodpERiRYnOOBLwsUj",
        "design": "KQzXIRcgffyxzegWhSCA",
        "director": "oksQozLDQIKUXTOVnSgL",
        "figure": "UGNjTUxVagRUsmeXePiR",
        "garden": "HJNyPHvohoqQteqypgTr",
        "newspaper": "awilNVmYFmacFDbYHCfB",
        "really": "bzvYFNrFxckhfCPzGMPQ",
        "set": "psGGIszJTdvgqoXarfFt",
        "site": "wqiGgdMEXPdaWjqWDjsW",
        "so": "CgTFQSEFOSeUlDbpOYnf",
        "stuff": "UAkAvbvbIjMdtUGoSlUv",
    },
}

snapshots["TestVolumeService.test_list volume_list_request"] = [
    [
        """query list($first: Int, $after: AWSJSON, $sortDirection: SortDirection) {
  listVolumes(first: $first, after: $after, sortDirection: $sortDirection) {
    first
    after
    items {
      ... on Volume {
        ...VolumeFields
      }
    }
  }
}

fragment VolumeFields on HumanVolume {
  id
  areaType
  created
  humanHeight
  metadata
  name
  state
  progress {
    state
    percentageComplete
  }
  __typename
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "after": None,
            "expand": None,
            "first": 10,
            "sortDirection": "DESC",
            "takeId": None,
        },
    },
]

snapshots["TestVolumeService.test_retrieve[empty_expand] get_query_expand_[]"] = [
    [
        """query retrieve($id: ID!) {
  getVolume(id: $id) {
    ... on Volume {
      ...VolumeFields
    }
  }
}

fragment VolumeFields on HumanVolume {
  id
  areaType
  created
  humanHeight
  metadata
  name
  state
  progress {
    state
    percentageComplete
  }
  __typename
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "volume-8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots["TestVolumeService.test_retrieve[empty_expand] get_response_expand_[]"] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": None,
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_retrieve[expand_additional_sources] get_query_expand_sources"
] = [
    [
        """query retrieve($id: ID!) {
  getVolume(id: $id) {
    ... on Volume {
      ...VolumeFields
    }
  }
}

fragment VolumeFields on HumanVolume {
  id
  areaType
  created
  humanHeight
  metadata
  name
  state
  progress {
    state
    percentageComplete
  }
  sources {
    deviceLabel
    file {
      id
      created
      type
      metadata
      name
      presignedUrl
      thumbnailUrl
      __typename
    }
    cameraSettings {
      lens
    }
    format
  }
  __typename
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "volume-874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestVolumeService.test_retrieve[expand_additional_sources] get_response_expand_sources"
] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": "2023-07-03T14:48:06.029019Z",
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "UmKdTFlLMIuIvJkRJnoM",
                    "decade": "zAvJMvacZIYSmMsDUNvC",
                    "director": "KNmpExWtgQLcAEuRyBkN",
                    "draw": "PnbQcVNCliYtuFCSJkGb",
                    "house": "aYyOUXkJPUjPJGpDdakX",
                    "huge": "eFaLyHGEQQpSzpRFSYEm",
                    "last": "dnZCcfgZNBnaEkbOzIyO",
                    "other": "XbBPNrbhtJksbBuoWXSK",
                    "table": "ACMVZcKAiGBcYgCzHAad",
                    "trouble": "UgnhIyaDJzohUigyDYZf",
                },
                "name": "",
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "MP4",
        },
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": "2023-07-03T14:48:06.029019Z",
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "UmKdTFlLMIuIvJkRJnoM",
                    "decade": "zAvJMvacZIYSmMsDUNvC",
                    "director": "KNmpExWtgQLcAEuRyBkN",
                    "draw": "PnbQcVNCliYtuFCSJkGb",
                    "house": "aYyOUXkJPUjPJGpDdakX",
                    "huge": "eFaLyHGEQQpSzpRFSYEm",
                    "last": "dnZCcfgZNBnaEkbOzIyO",
                    "other": "XbBPNrbhtJksbBuoWXSK",
                    "table": "ACMVZcKAiGBcYgCzHAad",
                    "trouble": "UgnhIyaDJzohUigyDYZf",
                },
                "name": "",
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "MOVE",
        },
    ],
    "state": "RUNNING",
}

snapshots["TestVolumeService.test_retrieve[expand_client] get_query_expand_client"] = [
    [
        """query retrieve($id: ID!) {
  getVolume(id: $id) {
    ... on Volume {
      ...VolumeFields
    }
  }
}

fragment VolumeFields on HumanVolume {
  id
  areaType
  created
  humanHeight
  metadata
  name
  state
  progress {
    state
    percentageComplete
  }
  client {
    id
    name
    created
    metadata
    portal
    __typename
  }
  __typename
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "volume-8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestVolumeService.test_retrieve[expand_client] get_response_expand_client"
] = {
    "area_type": "NORMAL",
    "client": {
        "created": "2023-06-12T00:00:00Z",
        "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
        "metadata": {
            "foo": "bar",
        },
        "name": "PYTEST_INVALID_CLIENT_NAME",
        "portal": "https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=",
    },
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": None,
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_retrieve[expand_outputs] get_query_expand_outputs"
] = [
    [
        """query retrieve($id: ID!) {
  getVolume(id: $id) {
    ... on Volume {
      ...VolumeFields
    }
  }
}

fragment VolumeFields on HumanVolume {
  id
  areaType
  created
  humanHeight
  metadata
  name
  state
  progress {
    state
    percentageComplete
  }
  outputs {
    format
    file {
      id
      created
      type
      metadata
      name
      presignedUrl
      thumbnailUrl
      __typename
    }
    __typename
  }
  __typename
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "volume-8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestVolumeService.test_retrieve[expand_outputs] get_response_expand_outputs"
] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": [
        {
            "file": {
                "client": None,
                "created": "2023-07-03T14:48:06.029019Z",
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "UmKdTFlLMIuIvJkRJnoM",
                    "decade": "zAvJMvacZIYSmMsDUNvC",
                    "director": "KNmpExWtgQLcAEuRyBkN",
                    "draw": "PnbQcVNCliYtuFCSJkGb",
                    "house": "aYyOUXkJPUjPJGpDdakX",
                    "huge": "eFaLyHGEQQpSzpRFSYEm",
                    "last": "dnZCcfgZNBnaEkbOzIyO",
                    "other": "XbBPNrbhtJksbBuoWXSK",
                    "table": "ACMVZcKAiGBcYgCzHAad",
                    "trouble": "UgnhIyaDJzohUigyDYZf",
                },
                "name": "",
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "volume_definition",
            "key": "volume_definition",
        },
        {
            "file": {
                "client": None,
                "created": "2023-07-03T14:48:06.029019Z",
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "UmKdTFlLMIuIvJkRJnoM",
                    "decade": "zAvJMvacZIYSmMsDUNvC",
                    "director": "KNmpExWtgQLcAEuRyBkN",
                    "draw": "PnbQcVNCliYtuFCSJkGb",
                    "house": "aYyOUXkJPUjPJGpDdakX",
                    "huge": "eFaLyHGEQQpSzpRFSYEm",
                    "last": "dnZCcfgZNBnaEkbOzIyO",
                    "other": "XbBPNrbhtJksbBuoWXSK",
                    "table": "ACMVZcKAiGBcYgCzHAad",
                    "trouble": "UgnhIyaDJzohUigyDYZf",
                },
                "name": "",
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "volume_report",
            "key": "volume_report",
        },
    ],
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": None,
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_retrieve[expand_video_file] get_query_expand_sources"
] = [
    [
        """query retrieve($id: ID!) {
  getVolume(id: $id) {
    ... on Volume {
      ...VolumeFields
    }
  }
}

fragment VolumeFields on HumanVolume {
  id
  areaType
  created
  humanHeight
  metadata
  name
  state
  progress {
    state
    percentageComplete
  }
  sources {
    deviceLabel
    file {
      id
      created
      type
      metadata
      name
      presignedUrl
      thumbnailUrl
      __typename
    }
    cameraSettings {
      lens
    }
    format
  }
  __typename
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "volume-874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestVolumeService.test_retrieve[expand_video_file] get_response_expand_sources"
] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": "2023-07-03T14:48:06.029019Z",
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "UmKdTFlLMIuIvJkRJnoM",
                    "decade": "zAvJMvacZIYSmMsDUNvC",
                    "director": "KNmpExWtgQLcAEuRyBkN",
                    "draw": "PnbQcVNCliYtuFCSJkGb",
                    "house": "aYyOUXkJPUjPJGpDdakX",
                    "huge": "eFaLyHGEQQpSzpRFSYEm",
                    "last": "dnZCcfgZNBnaEkbOzIyO",
                    "other": "XbBPNrbhtJksbBuoWXSK",
                    "table": "ACMVZcKAiGBcYgCzHAad",
                    "trouble": "UgnhIyaDJzohUigyDYZf",
                },
                "name": "",
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "MP4",
        },
    ],
    "state": "RUNNING",
}

snapshots["TestVolumeService.test_retrieve[no_expand] get_query_expand_None"] = [
    [
        """query retrieve($id: ID!) {
  getVolume(id: $id) {
    ... on Volume {
      ...VolumeFields
    }
  }
}

fragment VolumeFields on HumanVolume {
  id
  areaType
  created
  humanHeight
  metadata
  name
  state
  progress {
    state
    percentageComplete
  }
  __typename
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "volume-8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots["TestVolumeService.test_retrieve[no_expand] get_response_expand_None"] = {
    "area_type": "NORMAL",
    "client": None,
    "clip_window": {
        "end_time": 10.0,
        "start_time": 10.0,
    },
    "created": "2023-06-29T08:54:52.349467Z",
    "human_height": 1.5,
    "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {
        "analysis": "UmKdTFlLMIuIvJkRJnoM",
        "decade": "zAvJMvacZIYSmMsDUNvC",
        "director": "KNmpExWtgQLcAEuRyBkN",
        "draw": "PnbQcVNCliYtuFCSJkGb",
        "house": "aYyOUXkJPUjPJGpDdakX",
        "huge": "eFaLyHGEQQpSzpRFSYEm",
        "last": "dnZCcfgZNBnaEkbOzIyO",
        "other": "XbBPNrbhtJksbBuoWXSK",
        "table": "ACMVZcKAiGBcYgCzHAad",
        "trouble": "UgnhIyaDJzohUigyDYZf",
    },
    "name": "fake_volume",
    "outputs": None,
    "progress": {
        "percentage_complete": 50,
        "state": "RUNNING",
    },
    "sources": None,
    "state": "RUNNING",
}
