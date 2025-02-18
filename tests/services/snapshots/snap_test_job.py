# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots[
    "TestJobService.test_create_multicam[-None-empty_expand] create_mutation_expand_[]"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-None-empty_expand] create_response_expand_[]"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-None-expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
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
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-None-expand_client] create_response_expand_client"
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
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-None-expand_outputs] create_mutation_expand_outputs"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    outputs {
      key
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
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-None-expand_outputs] create_response_expand_outputs"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": [
        {
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
            "format": "",
            "key": "mp4",
        },
        {
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
            "format": "",
            "key": "fbx",
        },
    ],
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-None-expand_rig] create_mutation_expand_rig"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    rig {
      name
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-None-expand_rig] create_response_expand_rig"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": {
        "name": "move_mo",
    },
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-None-expand_take] create_mutation_expand_take"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    take {
      id
      created
      name
      metadata
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 849,
            "options": {},
            "outputs": [],
            "rig": "",
            "take_id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-None-expand_take] create_response_expand_take"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": {
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
}

snapshots[
    "TestJobService.test_create_multicam[-None-no_expand] create_mutation_expand_None"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-None-no_expand] create_response_expand_None"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-options1-empty_expand] create_mutation_expand_[]"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-options1-empty_expand] create_response_expand_[]"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-options1-expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
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
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-options1-expand_client] create_response_expand_client"
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
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-options1-expand_outputs] create_mutation_expand_outputs"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    outputs {
      key
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
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-options1-expand_outputs] create_response_expand_outputs"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": [
        {
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
            "format": "",
            "key": "mp4",
        },
        {
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
            "format": "",
            "key": "fbx",
        },
    ],
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-options1-expand_rig] create_mutation_expand_rig"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    rig {
      name
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-options1-expand_rig] create_response_expand_rig"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": {
        "name": "move_mo",
    },
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[-options1-expand_take] create_mutation_expand_take"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    take {
      id
      created
      name
      metadata
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 849,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "",
            "take_id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-options1-expand_take] create_response_expand_take"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": {
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
}

snapshots[
    "TestJobService.test_create_multicam[-options1-no_expand] create_mutation_expand_None"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[-options1-no_expand] create_response_expand_None"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-empty_expand] create_mutation_expand_[]"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-empty_expand] create_response_expand_[]"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
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
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-expand_client] create_response_expand_client"
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
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-expand_outputs] create_mutation_expand_outputs"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    outputs {
      key
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
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-expand_outputs] create_response_expand_outputs"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": [
        {
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
            "format": "",
            "key": "mp4",
        },
        {
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
            "format": "",
            "key": "fbx",
        },
    ],
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-expand_rig] create_mutation_expand_rig"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    rig {
      name
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-expand_rig] create_response_expand_rig"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": {
        "name": "move_mo",
    },
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-expand_take] create_mutation_expand_take"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    take {
      id
      created
      name
      metadata
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 849,
            "options": {},
            "outputs": [],
            "rig": "move_mo",
            "take_id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-expand_take] create_response_expand_take"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": {
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
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-no_expand] create_mutation_expand_None"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-None-no_expand] create_response_expand_None"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-empty_expand] create_mutation_expand_[]"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-empty_expand] create_response_expand_[]"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
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
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-expand_client] create_response_expand_client"
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
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-expand_outputs] create_mutation_expand_outputs"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    outputs {
      key
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
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-expand_outputs] create_response_expand_outputs"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": [
        {
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
            "format": "",
            "key": "mp4",
        },
        {
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
            "format": "",
            "key": "fbx",
        },
    ],
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-expand_rig] create_mutation_expand_rig"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    rig {
      name
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-expand_rig] create_response_expand_rig"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": {
        "name": "move_mo",
    },
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-expand_take] create_mutation_expand_take"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    take {
      id
      created
      name
      metadata
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 849,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "move_mo",
            "take_id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-expand_take] create_response_expand_take"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": {
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
}

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-no_expand] create_mutation_expand_None"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "numberOfActors": 8658,
            "options": {
                "floor_plane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "rig": "move_mo",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_multicam[move_mo-options1-no_expand] create_response_expand_None"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_singlecam[no_options-empty_expand] create_mutation_expand_[]"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {},
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[no_options-empty_expand] create_response_expand_[]"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_singlecam[no_options-expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
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
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {},
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[no_options-expand_client] create_response_expand_client"
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
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_singlecam[no_options-expand_outputs] create_mutation_expand_outputs"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    outputs {
      key
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
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {},
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[no_options-expand_outputs] create_response_expand_outputs"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": [
        {
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
            "format": "",
            "key": "mp4",
        },
        {
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
            "format": "",
            "key": "fbx",
        },
    ],
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_singlecam[no_options-expand_take] create_mutation_expand_take"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    take {
      id
      created
      name
      metadata
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {},
            "outputs": [],
            "take_id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[no_options-expand_take] create_response_expand_take"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": {
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
}

snapshots[
    "TestJobService.test_create_singlecam[no_options-no_expand] create_mutation_expand_None"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {},
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[no_options-no_expand] create_response_expand_None"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_singlecam[with_options-empty_expand] create_mutation_expand_[]"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {
                "floorPlane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[with_options-empty_expand] create_response_expand_[]"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_singlecam[with_options-expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
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
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {
                "floorPlane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[with_options-expand_client] create_response_expand_client"
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
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_singlecam[with_options-expand_outputs] create_mutation_expand_outputs"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    outputs {
      key
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
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {
                "floorPlane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[with_options-expand_outputs] create_response_expand_outputs"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": [
        {
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
            "format": "",
            "key": "mp4",
        },
        {
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
            "format": "",
            "key": "fbx",
        },
    ],
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create_singlecam[with_options-expand_take] create_mutation_expand_take"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    take {
      id
      created
      name
      metadata
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {
                "floorPlane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "take_id": "874a50b9-8d86-4324-bab5-ed05e9c5e560",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[with_options-expand_take] create_response_expand_take"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": {
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
}

snapshots[
    "TestJobService.test_create_singlecam[with_options-no_expand] create_mutation_expand_None"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": {
                "endTime": 10.0,
                "startTime": 1.0,
            },
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "",
            "options": {
                "floorPlane": True,
                "trackFingers": False,
            },
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_create_singlecam[with_options-no_expand] create_response_expand_None"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_fetch_service 1"] = GenericRepr(
    "JobService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)

snapshots["TestJobService.test_job_not_found job_not_found_response"] = [
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
            "getJob",
        ],
    },
]

snapshots["TestJobService.test_list[with_take_id] job_list_request"] = [
    [
        """query list($first: Int, $after: AWSJSON, $sortDirection: SortDirection, $takeId: String) {
  listJobs(
    first: $first
    after: $after
    sortDirection: $sortDirection
    takeId: $takeId
  ) {
    first
    after
    items {
      id
      created
      metadata
      state
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
            "takeId": "take-123-123-123-123",
        },
    },
]

snapshots["TestJobService.test_list[with_take_id] list_response"] = {
    "items": [
        {
            "client": None,
            "created": GenericRepr(
                "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
            ),
            "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
            "outputs": None,
            "rig": None,
            "state": "RUNNING",
            "take": None,
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

snapshots["TestJobService.test_list[without_take_id] job_list_request"] = [
    [
        """query list($first: Int, $after: AWSJSON, $sortDirection: SortDirection, $takeId: String) {
  listJobs(
    first: $first
    after: $after
    sortDirection: $sortDirection
    takeId: $takeId
  ) {
    first
    after
    items {
      id
      created
      metadata
      state
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
            "takeId": None,
        },
    },
]

snapshots["TestJobService.test_list[without_take_id] list_response"] = {
    "items": [
        {
            "client": None,
            "created": GenericRepr(
                "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
            ),
            "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
            "outputs": None,
            "rig": None,
            "state": "RUNNING",
            "take": None,
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

snapshots[
    "TestJobService.test_list_job_invalid key_error_message"
] = """1 validation error for ListBase
items
  Value error, Got __typename of '' which is not present in mapping_type_name_to_class: Rig, CameraSettings, Take, Job, HumanVolume [type=value_error, input_value=[{'id': 'dummy-123-123-123-123'}], input_type=list]
    For further information visit https://errors.pydantic.dev/2.9/v/value_error"""

snapshots[
    "TestJobService.test_output_types[None-create_multicam] create_multicam_response"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": "{}",
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_output_types[None-create_singlecam] create_singlecam_response"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": "{}",
            "name": "",
            "options": {},
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_output_types[outputs1-create_multicam] create_multicam_response"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": "{}",
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_output_types[outputs1-create_singlecam] create_singlecam_response"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": "{}",
            "name": "",
            "options": {},
            "outputs": [],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_output_types[outputs2-create_multicam] create_multicam_response"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": "{}",
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [
                "MAIN_BLEND",
                "FBX",
            ],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_output_types[outputs2-create_singlecam] create_singlecam_response"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": "{}",
            "name": "",
            "options": {},
            "outputs": [
                "MAIN_BLEND",
                "FBX",
            ],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_output_types[outputs3-create_multicam] create_multicam_response"
] = [
    [
        """mutation create($take_id: String!, $name: String, $numberOfActors: Int!, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $rig: String, $clip_window: ClipWindowInput) {
  createMultiCamJob(
    takeId: $take_id
    name: $name
    numberOfActors: $numberOfActors
    options: $options
    outputs: $outputs
    metadata: $metadata
    rig: $rig
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": "{}",
            "name": "",
            "numberOfActors": 8658,
            "options": {},
            "outputs": [
                "MAIN_GLB",
                "UNKNOWN_OUTPUT",
            ],
            "rig": "",
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_output_types[outputs3-create_singlecam] create_singlecam_response"
] = [
    [
        """mutation create($take_id: String!, $name: String, $options: OptionsInput, $outputs: [OutputType], $metadata: AWSJSON, $clip_window: ClipWindowInput) {
  createSingleCamJob(
    takeId: $take_id
    name: $name
    options: $options
    outputs: $outputs
    metadata: $metadata
    clipWindow: $clip_window
  ) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "clip_window": None,
            "metadata": "{}",
            "name": "",
            "options": {},
            "outputs": [
                "MAIN_GLB",
                "UNKNOWN_OUTPUT",
            ],
            "take_id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots["TestJobService.test_retrieve[empty_expand] retrieve_query_expand_[]"] = [
    [
        """query retrieve($id: ID!) {
  getJob(jobId: $id) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots["TestJobService.test_retrieve[empty_expand] retrieve_response_expand_[]"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_retrieve[expand_client] retrieve_query_expand_client"
] = [
    [
        """query retrieve($id: ID!) {
  getJob(jobId: $id) {
    id
    created
    metadata
    state
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
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_retrieve[expand_client] retrieve_response_expand_client"
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
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_retrieve[expand_outputs] retrieve_query_expand_outputs"
] = [
    [
        """query retrieve($id: ID!) {
  getJob(jobId: $id) {
    id
    created
    metadata
    state
    name
    outputs {
      key
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
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots[
    "TestJobService.test_retrieve[expand_outputs] retrieve_response_expand_outputs"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": [
        {
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
            "format": "",
            "key": "mp4",
        },
        {
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
            "format": "",
            "key": "fbx",
        },
    ],
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_retrieve[expand_rig] retrieve_query_expand_rig"] = [
    [
        """query retrieve($id: ID!) {
  getJob(jobId: $id) {
    id
    created
    metadata
    state
    name
    rig {
      name
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots["TestJobService.test_retrieve[expand_rig] retrieve_response_expand_rig"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": {
        "name": "move_mo",
    },
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_retrieve[expand_take] retrieve_query_expand_take"] = [
    [
        """query retrieve($id: ID!) {
  getJob(jobId: $id) {
    id
    created
    metadata
    state
    name
    take {
      id
      created
      name
      metadata
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

snapshots["TestJobService.test_retrieve[expand_take] retrieve_response_expand_take"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": {
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
}

snapshots["TestJobService.test_retrieve[no_expand] retrieve_query_expand_None"] = [
    [
        """query retrieve($id: ID!) {
  getJob(jobId: $id) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
        },
    },
]

snapshots["TestJobService.test_retrieve[no_expand] retrieve_response_expand_None"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_update update_mutation"] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON, $name: String) {
  updateJob(id: $id, metadata: $metadata, name: $name) {
    id
    created
    metadata
    state
    name
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "name": "Amber Harris",
        },
    },
]

snapshots["TestJobService.test_update update_response"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "rig": None,
    "state": "RUNNING",
    "take": None,
}
