# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestJobService.test_create[empty_expand] create_mutation_expand_[]"] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createJob(takeId: $take_id, metadata: $metadata) {
    id
    created
    metadata
    state
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": "{}",
            "take_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots["TestJobService.test_create[empty_expand] create_response_expand_[]"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
    "metadata": {},
    "outputs": None,
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_create[expand_client] create_mutation_expand_client"] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createJob(takeId: $take_id, metadata: $metadata) {
    id
    created
    metadata
    state
    client {
      id
      name
      created
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": "{}",
            "take_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots["TestJobService.test_create[expand_client] create_response_expand_client"] = {
    "client": {
        "created": "2023-06-12T00:00:00.000000Z",
        "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
        "name": "PYTEST_INVALID_CLIENT_NAME",
    },
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
    "metadata": {},
    "outputs": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create[expand_outputs] create_mutation_expand_outputs"
] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createJob(takeId: $take_id, metadata: $metadata) {
    id
    created
    metadata
    state
    outputs {
      key
      file {
        id
        created
        type
        metadata
        presignedUrl
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
            "metadata": "{}",
            "take_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots[
    "TestJobService.test_create[expand_outputs] create_response_expand_outputs"
] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
    "metadata": {},
    "outputs": [
        {
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {},
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "type": ".mp4",
            },
            "key": "mp4",
        },
        {
            "file": {
                "client": None,
                "created": GenericRepr(
                    "datetime.datetime(2023, 7, 3, 14, 48, 6, 29019, tzinfo=TzInfo(UTC))",
                ),
                "id": "file-a0059241-7ede-411c-a149-769a4305e8b6",
                "metadata": {},
                "presigned_url": GenericRepr(
                    "Url('https://pytest_invalid_presigned_url.com/file')",
                ),
                "type": ".mp4",
            },
            "key": "fbx",
        },
    ],
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_create[expand_take] create_mutation_expand_take"] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createJob(takeId: $take_id, metadata: $metadata) {
    id
    created
    metadata
    state
    take {
      id
      created
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
            "metadata": "{}",
            "take_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots["TestJobService.test_create[expand_take] create_response_expand_take"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
    "metadata": {},
    "outputs": None,
    "state": "RUNNING",
    "take": {
        "additional_files": None,
        "client": None,
        "created": GenericRepr(
            "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
        ),
        "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
        "metadata": {},
        "video_file": None,
    },
}

snapshots["TestJobService.test_create[no_expand] create_mutation_expand_None"] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createJob(takeId: $take_id, metadata: $metadata) {
    id
    created
    metadata
    state
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": "{}",
            "take_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots["TestJobService.test_create[no_expand] create_response_expand_None"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
    "metadata": {},
    "outputs": None,
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_fetch_service 1"] = GenericRepr(
    "JobService(api_key='usJxDFJOzwvfcVdkQqye', endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)
