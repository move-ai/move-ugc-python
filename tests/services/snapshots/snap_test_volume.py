# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestVolumeService.test_create[empty_expand] create_mutation_expand_[]"] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "areaType": "NORMAL",
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "clipWindow": {
                        "endTime": 5315.0,
                        "startTime": 849.0,
                    },
                    "deviceLabel": "realize",
                    "fileId": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "clipWindow": None,
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
    "sources": None,
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_create[expand_additional_sources] create_mutation_expand_sources"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    sources {
      deviceLabel
      file {
        id
        created
        type
        metadata
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
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "clipWindow": {
                        "endTime": 5315.0,
                        "startTime": 849.0,
                    },
                    "deviceLabel": "realize",
                    "fileId": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "clipWindow": None,
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
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
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
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "MP4",
        },
        {
            "camera_settings": None,
            "clip_window": None,
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
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
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
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "clipWindow": {
                        "endTime": 5315.0,
                        "startTime": 849.0,
                    },
                    "deviceLabel": "realize",
                    "fileId": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "clipWindow": None,
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
    "sources": None,
    "state": "RUNNING",
}

snapshots[
    "TestVolumeService.test_create[expand_video_file] create_mutation_expand_sources"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    sources {
      deviceLabel
      file {
        id
        created
        type
        metadata
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
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "clipWindow": {
                        "endTime": 5315.0,
                        "startTime": 849.0,
                    },
                    "deviceLabel": "realize",
                    "fileId": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "clipWindow": None,
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
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
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
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $areaType: AreaType!, $humanHeight: Float!, $metadata: AWSJSON, $name: String) {
  createVolumeWithHuman(
    sources: $sources
    syncMethod: $syncMethod
    areaType: $areaType
    humanHeight: $humanHeight
    metadata: $metadata
    name: $name
  ) {
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "areaType": "NORMAL",
            "humanHeight": 873121848153.264,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "attention",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "design",
                    },
                    "clipWindow": {
                        "endTime": 5315.0,
                        "startTime": 849.0,
                    },
                    "deviceLabel": "realize",
                    "fileId": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "so",
                    },
                    "clipWindow": None,
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
    "sources": None,
    "state": "RUNNING",
}

snapshots["TestVolumeService.test_fetch_service 1"] = GenericRepr(
    "VolumeService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)

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
  sources {
    deviceLabel
    file {
      id
      created
      type
      metadata
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
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
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
                "presigned_url": "https://pytest_invalid_presigned_url.com/file",
                "thumbnail_url": "https://pytest_invalid_thumbnail_url.com/file",
                "type": ".mp4",
            },
            "format": "MP4",
        },
        {
            "camera_settings": None,
            "clip_window": None,
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
  sources {
    deviceLabel
    file {
      id
      created
      type
      metadata
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
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
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
    "sources": None,
    "state": "RUNNING",
}
