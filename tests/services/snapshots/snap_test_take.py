# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestTakeService.test_create[empty_expand] create_mutation_expand_[]"] = [
    [
        """mutation create($video_file_id: String!, $additional_file_ids: [TakeFileInput!], $metadata: AWSJSON) {
  createTake(
    videoFileId: $video_file_id
    additionalFileIds: $additional_file_ids
    metadata: $metadata
  ) {
    id
    created
    metadata
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "additional_file_ids": [
                {
                    "fileId": "60b4cd1e-cf30-4be6-b9ed-32e59082cbe3",
                    "key": "DEPTH",
                },
            ],
            "metadata": "{}",
            "video_file_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots["TestTakeService.test_create[empty_expand] create_response_expand_[]"] = {
    "additional_files": None,
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
}

snapshots[
    "TestTakeService.test_create[expand_additional_files] create_mutation_expand_additional_files"
] = [
    [
        """mutation create($video_file_id: String!, $additional_file_ids: [TakeFileInput!], $metadata: AWSJSON) {
  createTake(
    videoFileId: $video_file_id
    additionalFileIds: $additional_file_ids
    metadata: $metadata
  ) {
    id
    created
    metadata
    additionalFiles {
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
            "additional_file_ids": [
                {
                    "fileId": "60b4cd1e-cf30-4be6-b9ed-32e59082cbe3",
                    "key": "DEPTH",
                },
            ],
            "metadata": "{}",
            "video_file_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots[
    "TestTakeService.test_create[expand_additional_files] create_response_expand_additional_files"
] = {
    "additional_files": [
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
            "key": "DEPTH",
        },
    ],
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
}

snapshots[
    "TestTakeService.test_create[expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($video_file_id: String!, $additional_file_ids: [TakeFileInput!], $metadata: AWSJSON) {
  createTake(
    videoFileId: $video_file_id
    additionalFileIds: $additional_file_ids
    metadata: $metadata
  ) {
    id
    created
    metadata
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
            "additional_file_ids": [
                {
                    "fileId": "60b4cd1e-cf30-4be6-b9ed-32e59082cbe3",
                    "key": "DEPTH",
                },
            ],
            "metadata": "{}",
            "video_file_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots[
    "TestTakeService.test_create[expand_client] create_response_expand_client"
] = {
    "additional_files": None,
    "client": {
        "created": "2023-06-12T00:00:00.000000Z",
        "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
        "name": "PYTEST_INVALID_CLIENT_NAME",
    },
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
}

snapshots[
    "TestTakeService.test_create[expand_video_file] create_mutation_expand_video_file"
] = [
    [
        """mutation create($video_file_id: String!, $additional_file_ids: [TakeFileInput!], $metadata: AWSJSON) {
  createTake(
    videoFileId: $video_file_id
    additionalFileIds: $additional_file_ids
    metadata: $metadata
  ) {
    id
    created
    metadata
    videoFile {
      id
      created
      type
      metadata
      presignedUrl
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "additional_file_ids": [
                {
                    "fileId": "60b4cd1e-cf30-4be6-b9ed-32e59082cbe3",
                    "key": "DEPTH",
                },
            ],
            "metadata": "{}",
            "video_file_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots[
    "TestTakeService.test_create[expand_video_file] create_response_expand_video_file"
] = {
    "additional_files": None,
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": {
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
}

snapshots["TestTakeService.test_create[no_expand] create_mutation_expand_None"] = [
    [
        """mutation create($video_file_id: String!, $additional_file_ids: [TakeFileInput!], $metadata: AWSJSON) {
  createTake(
    videoFileId: $video_file_id
    additionalFileIds: $additional_file_ids
    metadata: $metadata
  ) {
    id
    created
    metadata
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "additional_file_ids": [
                {
                    "fileId": "60b4cd1e-cf30-4be6-b9ed-32e59082cbe3",
                    "key": "DEPTH",
                },
            ],
            "metadata": "{}",
            "video_file_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots["TestTakeService.test_create[no_expand] create_response_expand_None"] = {
    "additional_files": None,
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
}

snapshots[
    "TestTakeService.test_create_lower_additional_file_key create_mutation_lower_additional_file_key"
] = [
    [
        """mutation create($video_file_id: String!, $additional_file_ids: [TakeFileInput!], $metadata: AWSJSON) {
  createTake(
    videoFileId: $video_file_id
    additionalFileIds: $additional_file_ids
    metadata: $metadata
  ) {
    id
    created
    metadata
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "additional_file_ids": [
                {
                    "fileId": "60b4cd1e-cf30-4be6-b9ed-32e59082cbe3",
                    "key": "DEPTH",
                },
            ],
            "metadata": "{}",
            "video_file_id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots[
    "TestTakeService.test_create_lower_additional_file_key create_response_lower_additional_file_key"
] = {
    "additional_files": None,
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
}

snapshots["TestTakeService.test_fetch_service 1"] = GenericRepr(
    "TakeService(api_key='usJxDFJOzwvfcVdkQqye', endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)

snapshots["TestTakeService.test_retrieve[empty_expand] retrieve_request_expand_[]"] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots["TestTakeService.test_retrieve[empty_expand] retrieve_response_expand_[]"] = {
    "additional_files": None,
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
}

snapshots[
    "TestTakeService.test_retrieve[expand_additional_files] retrieve_request_expand_additional_files"
] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    additionalFiles {
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
            "id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots[
    "TestTakeService.test_retrieve[expand_additional_files] retrieve_response_expand_additional_files"
] = {
    "additional_files": [
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
            "key": "DEPTH",
        },
    ],
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
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
            "id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots[
    "TestTakeService.test_retrieve[expand_client] retrieve_response_expand_client"
] = {
    "additional_files": None,
    "client": {
        "created": "2023-06-12T00:00:00.000000Z",
        "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
        "name": "PYTEST_INVALID_CLIENT_NAME",
    },
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
}

snapshots[
    "TestTakeService.test_retrieve[expand_video_file] retrieve_request_expand_video_file"
] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    videoFile {
      id
      created
      type
      metadata
      presignedUrl
      __typename
    }
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots[
    "TestTakeService.test_retrieve[expand_video_file] retrieve_response_expand_video_file"
] = {
    "additional_files": None,
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": {
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
}

snapshots["TestTakeService.test_retrieve[no_expand] retrieve_request_expand_None"] = [
    [
        """query retrieve($id: ID!) {
  getTake(takeId: $id) {
    id
    created
    metadata
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "fc1c1c02-3299-4ad6-a244-7a6cef18457d",
        },
    },
]

snapshots["TestTakeService.test_retrieve[no_expand] retrieve_response_expand_None"] = {
    "additional_files": None,
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 6, 29, 8, 54, 52, 349467, tzinfo=TzInfo(UTC))",
    ),
    "id": "take-af54cc45-7137-4206-a4c1-b3bc21b398fc",
    "metadata": {},
    "video_file": None,
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
