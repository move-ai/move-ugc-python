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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "attention",
            "sources": [
                {
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "site",
                    "fileId": "0068cf0f-420a-4847-8ba1-d7854a1e1b59",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "attention",
            "sources": [
                {
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "site",
                    "fileId": "0068cf0f-420a-4847-8ba1-d7854a1e1b59",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "attention",
            "sources": [
                {
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "site",
                    "fileId": "0068cf0f-420a-4847-8ba1-d7854a1e1b59",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "attention",
            "sources": [
                {
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "site",
                    "fileId": "0068cf0f-420a-4847-8ba1-d7854a1e1b59",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "attention",
            "sources": [
                {
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "site",
                    "fileId": "0068cf0f-420a-4847-8ba1-d7854a1e1b59",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "deviceLabel": "figure",
                    "fileId": "10ba655c-0068-4f0f-820a-4847cba1d785",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "where",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "figure",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "large",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "10ba655c-0068-4f0f-820a-4847cba1d785",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": True,
                },
            },
            "volumeId": "volume-c086713f-846a-4c2f-b9d1-6d364cc7b4ac",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
        presignedUrl
        thumbnailUrl
        __typename
      }
      format
      cameraSettings {
        lens
      }
      clipWindow {
        startTime
        endTime
      }
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "where",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "figure",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "large",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "10ba655c-0068-4f0f-820a-4847cba1d785",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": True,
                },
            },
            "volumeId": "volume-c086713f-846a-4c2f-b9d1-6d364cc7b4ac",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
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
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "where",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "figure",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "large",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "10ba655c-0068-4f0f-820a-4847cba1d785",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": True,
                },
            },
            "volumeId": "volume-c086713f-846a-4c2f-b9d1-6d364cc7b4ac",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
        presignedUrl
        thumbnailUrl
        __typename
      }
      format
      cameraSettings {
        lens
      }
      clipWindow {
        startTime
        endTime
      }
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "where",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "figure",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "large",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "10ba655c-0068-4f0f-820a-4847cba1d785",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": True,
                },
            },
            "volumeId": "volume-c086713f-846a-4c2f-b9d1-6d364cc7b4ac",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "where",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "figure",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "large",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "10ba655c-0068-4f0f-820a-4847cba1d785",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": True,
                },
            },
            "volumeId": "volume-c086713f-846a-4c2f-b9d1-6d364cc7b4ac",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": None,
    "volume": {
        "area_type": "NORMAL",
        "client": None,
        "created": "2023-06-29T08:54:52.349467Z",
        "human_height": 1.5,
        "id": "volume-af54cc45-7137-4206-a4c1-b3bc21b398fc",
        "metadata": {
            "analysis": "ableRsSGSBRpUxDKSTZs",
            "decade": -127471.91004658,
            "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
            "draw": 9025,
            "house": "EQQpSzpRFSYEmmcBHMyX",
            "huge": "RLQMnHdwIMQHuSbBEcSq",
            "last": "CliYtuFCSJkGbKACMVZc",
            "other": 4537,
            "table": "fPlGoqlVJAWBmofrulqS",
            "trouble": "1982-01-05 12:28:54",
        },
        "name": "fake_volume",
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "name": "where",
            "sources": [
                {
                    "cameraSettings": {
                        "lens": "figure",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "2ca4d775-bfdd-4401-b898-a7a537bea600",
                    "format": "MP4",
                },
                {
                    "cameraSettings": {
                        "lens": "large",
                    },
                    "clipWindow": None,
                    "deviceLabel": "site",
                    "fileId": "10ba655c-0068-4f0f-820a-4847cba1d785",
                    "format": "MOVE",
                },
            ],
            "syncMethod": {
                "clapWindow": None,
                "timecodeSync": {
                    "useTimecode": True,
                },
            },
            "volumeId": "volume-c086713f-846a-4c2f-b9d1-6d364cc7b4ac",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
                "analysis": "ableRsSGSBRpUxDKSTZs",
                "decade": -127471.91004658,
                "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                "draw": 9025,
                "house": "EQQpSzpRFSYEmmcBHMyX",
                "huge": "RLQMnHdwIMQHuSbBEcSq",
                "last": "CliYtuFCSJkGbKACMVZc",
                "other": 4537,
                "table": "fPlGoqlVJAWBmofrulqS",
                "trouble": "1982-01-05 12:28:54",
            },
            "name": "agreement",
            "sources": None,
            "volume": None,
        },
    ],
    "limit": 3567,
    "next_token": {
        "ability": GenericRepr(
            "Decimal('-39859709324198798762190136418988284335952316805377455642414452157481053737582709181317757113.286861444124491')",
        ),
        "attention": "evqGQzKwSqfRoArzmKBW",
        "color": "gqjkASbVixjzHTvnHGGY",
        "evening": "alvaradocharles@example.org",
        "figure": -1000508466.811,
        "large": "TQtLfcoVjFwLvYXpwnub",
        "stuff": "http://armstrong.net/postsindex.html",
        "teacher": GenericRepr(
            "Decimal('-94421184485993957790167155643305.1958182142991397918239901454')",
        ),
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
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
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateTake(id: $id, metadata: $metadata) {
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_update[expand_additional_files] update_mutation_expand_sources"
] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateTake(id: $id, metadata: $metadata) {
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateTake(id: $id, metadata: $metadata) {
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": None,
    "volume": None,
}

snapshots[
    "TestTakeService.test_update[expand_video_file] update_mutation_expand_sources"
] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateTake(id: $id, metadata: $metadata) {
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": [
        {
            "camera_settings": None,
            "clip_window": None,
            "device_label": "foobar",
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {
                    "analysis": "ableRsSGSBRpUxDKSTZs",
                    "decade": -127471.91004658,
                    "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
                    "draw": 9025,
                    "house": "EQQpSzpRFSYEmmcBHMyX",
                    "huge": "RLQMnHdwIMQHuSbBEcSq",
                    "last": "CliYtuFCSJkGbKACMVZc",
                    "other": 4537,
                    "table": "fPlGoqlVJAWBmofrulqS",
                    "trouble": "1982-01-05 12:28:54",
                },
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
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateTake(id: $id, metadata: $metadata) {
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
            "id": "bfdde401-b898-47a5-b7be-a600bdc68ffa",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
        "analysis": "ableRsSGSBRpUxDKSTZs",
        "decade": -127471.91004658,
        "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053",
        "draw": 9025,
        "house": "EQQpSzpRFSYEmmcBHMyX",
        "huge": "RLQMnHdwIMQHuSbBEcSq",
        "last": "CliYtuFCSJkGbKACMVZc",
        "other": 4537,
        "table": "fPlGoqlVJAWBmofrulqS",
        "trouble": "1982-01-05 12:28:54",
    },
    "name": "agreement",
    "sources": None,
    "volume": None,
}
