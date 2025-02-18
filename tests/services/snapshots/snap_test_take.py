# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestTakeService.test_create[empty_expand] create_mutation_expand_[]"] = [
    [
        """mutation create($sources: [SourceInput!], $name: String, $metadata: AWSJSON) {
  createSingleCamTake(sources: $sources, name: $name, metadata: $metadata) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "site",
            "sources": [
                {
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "white",
                    "fileId": "06c7a4f6-34c4-414f-930e-9daa0d4585a7",
                    "format": "MOVE",
                },
            ],
        },
    },
]

snapshots["TestTakeService.test_create[empty_expand] create_response_expand_[]"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_create[expand_additional_sources] create_mutation_expand_sources"
] = [
    [
        """mutation create($sources: [SourceInput!], $name: String, $metadata: AWSJSON) {
  createSingleCamTake(sources: $sources, name: $name, metadata: $metadata) {
    id
    created
    metadata
    name
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
      format
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "site",
            "sources": [
                {
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "white",
                    "fileId": "06c7a4f6-34c4-414f-930e-9daa0d4585a7",
                    "format": "MOVE",
                },
            ],
        },
    },
]

snapshots[
    "TestTakeService.test_create[expand_additional_sources] create_response_expand_sources"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MP4",
        },
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MOVE",
        },
    ],
    "volume": None,
}

snapshots[
    "TestTakeService.test_create[expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($sources: [SourceInput!], $name: String, $metadata: AWSJSON) {
  createSingleCamTake(sources: $sources, name: $name, metadata: $metadata) {
    id
    created
    metadata
    name
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
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "site",
            "sources": [
                {
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "white",
                    "fileId": "06c7a4f6-34c4-414f-930e-9daa0d4585a7",
                    "format": "MOVE",
                },
            ],
        },
    },
]

snapshots[
    "TestTakeService.test_create[expand_client] create_response_expand_client"
] = {
    "client": {
        "created": GenericRepr(
            "datetime.datetime(2023, 6, 12, 0, 0, tzinfo=TzInfo(UTC))",
        ),
        "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
        "metadata": {
            "foo": "bar",
        },
        "name": "PYTEST_INVALID_CLIENT_NAME",
        "portal": GenericRepr(
            "Url('https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=')",
        ),
    },
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_create[expand_video_file] create_mutation_expand_sources"
] = [
    [
        """mutation create($sources: [SourceInput!], $name: String, $metadata: AWSJSON) {
  createSingleCamTake(sources: $sources, name: $name, metadata: $metadata) {
    id
    created
    metadata
    name
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
      format
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "site",
            "sources": [
                {
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "white",
                    "fileId": "06c7a4f6-34c4-414f-930e-9daa0d4585a7",
                    "format": "MOVE",
                },
            ],
        },
    },
]

snapshots[
    "TestTakeService.test_create[expand_video_file] create_response_expand_sources"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MP4",
        },
    ],
    "volume": None,
}

snapshots["TestTakeService.test_create[no_expand] create_mutation_expand_None"] = [
    [
        """mutation create($sources: [SourceInput!], $name: String, $metadata: AWSJSON) {
  createSingleCamTake(sources: $sources, name: $name, metadata: $metadata) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "site",
            "sources": [
                {
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "white",
                    "fileId": "06c7a4f6-34c4-414f-930e-9daa0d4585a7",
                    "format": "MOVE",
                },
            ],
        },
    },
]

snapshots["TestTakeService.test_create[no_expand] create_response_expand_None"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_create_lower_additional_file_key create_mutation_lower_additional_file_key"
] = [
    [
        """mutation create($sources: [SourceInput!], $name: String, $metadata: AWSJSON) {
  createSingleCamTake(sources: $sources, name: $name, metadata: $metadata) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '"{}"',
            "name": "",
            "sources": [
                {
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "area",
                    "fileId": "bdc68ffa-06c7-44f6-b4c4-614f530e9daa",
                    "format": "MOVE",
                },
            ],
        },
    },
]

snapshots[
    "TestTakeService.test_create_lower_additional_file_key create_response_lower_additional_file_key"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_create_multicam[empty_expand] create_mutation_expand_[]"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $metadata: AWSJSON, $name: String, $volumeId: String!) {
  createMultiCamTake(
    sources: $sources
    syncMethod: $syncMethod
    name: $name
    volumeId: $volumeId
    metadata: $metadata
  ) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "evening",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "area",
                    },
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "director",
                    },
                    "deviceLabel": "white",
                    "fileId": "bdc68ffa-06c7-44f6-b4c4-614f530e9daa",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": False,
                },
            },
            "volumeId": "volume-cba1d785-4a1e-4b59-aca4-d775bfdde401",
        },
    },
]

snapshots[
    "TestTakeService.test_create_multicam[empty_expand] create_response_expand_[]"
] = {
    "client": None,
    "created": "2023-06-29T08:54:52.349467Z",
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_create_multicam[expand_additional_sources] create_mutation_expand_sources"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $metadata: AWSJSON, $name: String, $volumeId: String!) {
  createMultiCamTake(
    sources: $sources
    syncMethod: $syncMethod
    name: $name
    volumeId: $volumeId
    metadata: $metadata
  ) {
    id
    created
    metadata
    name
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
      format
      cameraSettings {
        lens
      }
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "evening",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "area",
                    },
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "director",
                    },
                    "deviceLabel": "white",
                    "fileId": "bdc68ffa-06c7-44f6-b4c4-614f530e9daa",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": False,
                },
            },
            "volumeId": "volume-cba1d785-4a1e-4b59-aca4-d775bfdde401",
        },
    },
]

snapshots[
    "TestTakeService.test_create_multicam[expand_additional_sources] create_response_expand_sources"
] = {
    "client": None,
    "created": "2023-06-29T08:54:52.349467Z",
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
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
    "volume": None,
}

snapshots[
    "TestTakeService.test_create_multicam[expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $metadata: AWSJSON, $name: String, $volumeId: String!) {
  createMultiCamTake(
    sources: $sources
    syncMethod: $syncMethod
    name: $name
    volumeId: $volumeId
    metadata: $metadata
  ) {
    id
    created
    metadata
    name
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
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "evening",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "area",
                    },
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "director",
                    },
                    "deviceLabel": "white",
                    "fileId": "bdc68ffa-06c7-44f6-b4c4-614f530e9daa",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": False,
                },
            },
            "volumeId": "volume-cba1d785-4a1e-4b59-aca4-d775bfdde401",
        },
    },
]

snapshots[
    "TestTakeService.test_create_multicam[expand_client] create_response_expand_client"
] = {
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
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_create_multicam[expand_video_file] create_mutation_expand_sources"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $metadata: AWSJSON, $name: String, $volumeId: String!) {
  createMultiCamTake(
    sources: $sources
    syncMethod: $syncMethod
    name: $name
    volumeId: $volumeId
    metadata: $metadata
  ) {
    id
    created
    metadata
    name
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
      format
      cameraSettings {
        lens
      }
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "evening",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "area",
                    },
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "director",
                    },
                    "deviceLabel": "white",
                    "fileId": "bdc68ffa-06c7-44f6-b4c4-614f530e9daa",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": False,
                },
            },
            "volumeId": "volume-cba1d785-4a1e-4b59-aca4-d775bfdde401",
        },
    },
]

snapshots[
    "TestTakeService.test_create_multicam[expand_video_file] create_response_expand_sources"
] = {
    "client": None,
    "created": "2023-06-29T08:54:52.349467Z",
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
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
    "volume": None,
}

snapshots[
    "TestTakeService.test_create_multicam[expand_volume] create_mutation_expand_volume"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $metadata: AWSJSON, $name: String, $volumeId: String!) {
  createMultiCamTake(
    sources: $sources
    syncMethod: $syncMethod
    name: $name
    volumeId: $volumeId
    metadata: $metadata
  ) {
    id
    created
    metadata
    name
    volume {
      ... on Volume {
        ...HumanVolumeFragment
      }
    }
    __typename
  }
}

fragment HumanVolumeFragment on HumanVolume {
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
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "evening",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "area",
                    },
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "director",
                    },
                    "deviceLabel": "white",
                    "fileId": "bdc68ffa-06c7-44f6-b4c4-614f530e9daa",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": False,
                },
            },
            "volumeId": "volume-cba1d785-4a1e-4b59-aca4-d775bfdde401",
        },
    },
]

snapshots[
    "TestTakeService.test_create_multicam[expand_volume] create_response_expand_volume"
] = {
    "client": None,
    "created": "2023-06-29T08:54:52.349467Z",
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": {
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
        "outputs": None,
        "sources": None,
        "state": "RUNNING",
    },
}

snapshots[
    "TestTakeService.test_create_multicam[no_expand] create_mutation_expand_None"
] = [
    [
        """mutation create($sources: [SourceInput!], $syncMethod: SyncMethodInput, $metadata: AWSJSON, $name: String, $volumeId: String!) {
  createMultiCamTake(
    sources: $sources
    syncMethod: $syncMethod
    name: $name
    volumeId: $volumeId
    metadata: $metadata
  ) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "evening",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "area",
                    },
                    "deviceLabel": "white",
                    "fileId": "a8491a43-874a-40b9-8d86-63243ab5ed05",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "director",
                    },
                    "deviceLabel": "white",
                    "fileId": "bdc68ffa-06c7-44f6-b4c4-614f530e9daa",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": False,
                },
            },
            "volumeId": "volume-cba1d785-4a1e-4b59-aca4-d775bfdde401",
        },
    },
]

snapshots[
    "TestTakeService.test_create_multicam[no_expand] create_response_expand_None"
] = {
    "client": None,
    "created": "2023-06-29T08:54:52.349467Z",
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots["TestTakeService.test_fetch_service 1"] = GenericRepr(
    "TakeService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)

snapshots["TestTakeService.test_list list_response"] = {
    "items": [
        {
            "client": None,
            "created": GenericRepr(
                "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
            ),
            "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
            "name": "realize",
            "sources": None,
            "volume": None,
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

snapshots["TestTakeService.test_list take_list_request"] = [
    [
        """query list($first: Int, $after: AWSJSON, $sortDirection: SortDirection) {
  listTakes(first: $first, after: $after, sortDirection: $sortDirection) {
    first
    after
    items {
      id
      created
      metadata
      name
      __typename
    }
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "after": None,
            "expand": None,
            "first": 10,
            "sortDirection": "DESC",
        },
    },
]

snapshots["TestTakeService.test_retrieve[empty_expand] retrieve_request_expand_[]"] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots["TestTakeService.test_retrieve[empty_expand] retrieve_response_expand_[]"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_retrieve[expand_additional_files] retrieve_request_expand_sources"
] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    name
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
      format
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestTakeService.test_retrieve[expand_additional_files] retrieve_response_expand_sources"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MP4",
        },
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MOVE",
        },
    ],
    "volume": None,
}

snapshots[
    "TestTakeService.test_retrieve[expand_client] retrieve_request_expand_client"
] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    name
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
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestTakeService.test_retrieve[expand_client] retrieve_response_expand_client"
] = {
    "client": {
        "created": GenericRepr(
            "datetime.datetime(2023, 6, 12, 0, 0, tzinfo=TzInfo(UTC))",
        ),
        "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
        "metadata": {
            "foo": "bar",
        },
        "name": "PYTEST_INVALID_CLIENT_NAME",
        "portal": GenericRepr(
            "Url('https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=')",
        ),
    },
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_retrieve[expand_video_file] retrieve_request_expand_sources"
] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    name
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
      format
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestTakeService.test_retrieve[expand_video_file] retrieve_response_expand_sources"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MP4",
        },
    ],
    "volume": None,
}

snapshots["TestTakeService.test_retrieve[no_expand] retrieve_request_expand_None"] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots["TestTakeService.test_retrieve[no_expand] retrieve_response_expand_None"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots["TestTakeService.test_take_not_found take_not_found_response"] = [
    {
        "data": None,
        "errorInfo": None,
        "errorType": "MoveNotFoundError",
        "locations": [
            {
                "column": 3,
                "line": 2,
                "sourceName": None,
            },
        ],
        "message": "Resource not found in move-ugc-api.",
        "path": [
            "getTake",
        ],
    },
]

snapshots["TestTakeService.test_update[empty_expand] update_mutation_expand_[]"] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON, $name: String) {
  updateTake(id: $id, metadata: $metadata, name: $name) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "Erika Johnson",
        },
    },
]

snapshots["TestTakeService.test_update[empty_expand] update_response_expand_[]"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_update[expand_additional_files] update_mutation_expand_sources"
] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON, $name: String) {
  updateTake(id: $id, metadata: $metadata, name: $name) {
    id
    created
    metadata
    name
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
      format
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "Erika Johnson",
        },
    },
]

snapshots[
    "TestTakeService.test_update[expand_additional_files] update_response_expand_sources"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MP4",
        },
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MOVE",
        },
    ],
    "volume": None,
}

snapshots[
    "TestTakeService.test_update[expand_client] update_mutation_expand_client"
] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON, $name: String) {
  updateTake(id: $id, metadata: $metadata, name: $name) {
    id
    created
    metadata
    name
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
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "Erika Johnson",
        },
    },
]

snapshots[
    "TestTakeService.test_update[expand_client] update_response_expand_client"
] = {
    "client": {
        "created": GenericRepr(
            "datetime.datetime(2023, 6, 12, 0, 0, tzinfo=TzInfo(UTC))",
        ),
        "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
        "metadata": {
            "foo": "bar",
        },
        "name": "PYTEST_INVALID_CLIENT_NAME",
        "portal": GenericRepr(
            "Url('https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=')",
        ),
    },
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_update[expand_video_file] update_mutation_expand_sources"
] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON, $name: String) {
  updateTake(id: $id, metadata: $metadata, name: $name) {
    id
    created
    metadata
    name
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
      format
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "Erika Johnson",
        },
    },
]

snapshots[
    "TestTakeService.test_update[expand_video_file] update_response_expand_sources"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": [
        {
            "camera_settings": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
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
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "thumbnail_url": GenericRepr(
                    "Url('https://pytest_invalid_thumbnail_url.com/file')",
                ),
                "type": ".mp4",
            },
            "format": "MP4",
        },
    ],
    "volume": None,
}

snapshots["TestTakeService.test_update[no_expand] update_mutation_expand_None"] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON, $name: String) {
  updateTake(id: $id, metadata: $metadata, name: $name) {
    id
    created
    metadata
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "Erika Johnson",
        },
    },
]

snapshots["TestTakeService.test_update[no_expand] update_response_expand_None"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
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
    "name": "realize",
    "sources": None,
    "volume": None,
}
