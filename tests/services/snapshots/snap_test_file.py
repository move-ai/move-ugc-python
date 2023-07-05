# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestFileService.test_fetch_service 1"] = GenericRepr(
    "FileService(api_key='usJxDFJOzwvfcVdkQqye', endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)

snapshots["TestFileService.test_file_not_found file_not_found_response"] = [
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
            "getFile",
        ],
    },
]

snapshots[
    "TestFileService.test_retrieve[empty_expand] file_retrieve_response_expand_[]"
] = {
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
}

snapshots["TestFileService.test_retrieve[empty_expand] retrieve_query_expand_[]"] = [
    [
        """query retrieve($id: ID!) {
  getFile(fileId: $id) {
    id
    presignedUrl
    created
    type
    metadata
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
    "TestFileService.test_retrieve[expand_client] file_retrieve_response_expand_client"
] = {
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
}

snapshots[
    "TestFileService.test_retrieve[expand_client] retrieve_query_expand_client"
] = [
    [
        """query retrieve($id: ID!) {
  getFile(fileId: $id) {
    id
    presignedUrl
    created
    type
    metadata
    client {
      id
      name
      created
    }
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
    "TestFileService.test_retrieve[no_expand] file_retrieve_response_expand_None"
] = {
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
}

snapshots["TestFileService.test_retrieve[no_expand] retrieve_query_expand_None"] = [
    [
        """query retrieve($id: ID!) {
  getFile(fileId: $id) {
    id
    presignedUrl
    created
    type
    metadata
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
