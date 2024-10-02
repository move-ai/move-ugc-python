# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestFileService.test_create[empty_expand] create_mutation_expand_[]"] = [
    [
        """mutation create($type: String!, $metadata: AWSJSON!) {
  createFile(type: $type, metadata: $metadata) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "type": "png",
        },
    },
]

snapshots[
    "TestFileService.test_create[empty_expand] create_mutation_response_expand_[]"
] = {
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
    ),
    "type": ".mp4",
}

snapshots[
    "TestFileService.test_create[expand_client] create_mutation_expand_client"
] = [
    [
        """mutation create($type: String!, $metadata: AWSJSON!) {
  createFile(type: $type, metadata: $metadata) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
    __typename
    client {
      id
      name
      created
      metadata
      portal
      __typename
    }
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "type": "png",
        },
    },
]

snapshots[
    "TestFileService.test_create[expand_client] create_mutation_response_expand_client"
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
    ),
    "type": ".mp4",
}

snapshots["TestFileService.test_create[no_expand] create_mutation_expand_None"] = [
    [
        """mutation create($type: String!, $metadata: AWSJSON!) {
  createFile(type: $type, metadata: $metadata) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
            "type": "png",
        },
    },
]

snapshots[
    "TestFileService.test_create[no_expand] create_mutation_response_expand_None"
] = {
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
    ),
    "type": ".mp4",
}

snapshots["TestFileService.test_fetch_service 1"] = GenericRepr(
    "FileService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
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

snapshots["TestFileService.test_generate_share_code generate_share_code_mutation"] = [
    [
        """mutation generateShareCode($fileId: String!) {
  generateShareCode(fileId: $fileId) {
    code
    created
    file {
      id
    }
    expires
    url
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "fileId": "516b93c2-ca3c-4b89-b7d8-6704858462ab",
        },
    },
]

snapshots[
    "TestFileService.test_generate_share_code generate_share_code_mutation_response"
] = {
    "code": "WkDQwclzAvJMvacZIYSm",
    "created": GenericRepr("datetime.datetime(2010, 10, 4, 0, 0)"),
    "expires": GenericRepr("datetime.datetime(1989, 4, 22, 0, 0)"),
    "file_id": "ed34cde6-e490-42be-849a-f3db904ddfc0",
    "url": GenericRepr("Url('https://www.ramirez.biz/')"),
}

snapshots[
    "TestFileService.test_retrieve[empty_expand] file_retrieve_response_expand_[]"
] = {
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
    ),
    "type": ".mp4",
}

snapshots["TestFileService.test_retrieve[empty_expand] retrieve_query_expand_[]"] = [
    [
        """query retrieve($id: ID!) {
  getFile(fileId: $id) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
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
    "TestFileService.test_retrieve[empty_expand_no_thumbnail] file_retrieve_response_expand_[]"
] = {
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": "",
    "type": ".mp4",
}

snapshots[
    "TestFileService.test_retrieve[empty_expand_no_thumbnail] retrieve_query_expand_[]"
] = [
    [
        """query retrieve($id: ID!) {
  getFile(fileId: $id) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
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
    "TestFileService.test_retrieve[expand_client] file_retrieve_response_expand_client"
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
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
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
    __typename
    client {
      id
      name
      created
      metadata
      portal
      __typename
    }
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
    "TestFileService.test_retrieve[no_expand] file_retrieve_response_expand_None"
] = {
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
    ),
    "type": ".mp4",
}

snapshots["TestFileService.test_retrieve[no_expand] retrieve_query_expand_None"] = [
    [
        """query retrieve($id: ID!) {
  getFile(fileId: $id) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
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

snapshots["TestFileService.test_update[empty_expand] update_mutation_expand_[]"] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateFile(id: $id, metadata: $metadata) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
        },
    },
]

snapshots[
    "TestFileService.test_update[empty_expand] update_mutation_response_expand_[]"
] = {
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
    ),
    "type": ".mp4",
}

snapshots[
    "TestFileService.test_update[expand_client] update_mutation_expand_client"
] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateFile(id: $id, metadata: $metadata) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
    __typename
    client {
      id
      name
      created
      metadata
      portal
      __typename
    }
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
        },
    },
]

snapshots[
    "TestFileService.test_update[expand_client] update_mutation_response_expand_client"
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
    ),
    "type": ".mp4",
}

snapshots["TestFileService.test_update[no_expand] update_mutation_expand_None"] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateFile(id: $id, metadata: $metadata) {
    id
    created
    type
    metadata
    presignedUrl
    thumbnailUrl
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "id": "8d866324-3ab5-4d05-a9c5-e560a8020f0a",
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
        },
    },
]

snapshots[
    "TestFileService.test_update[no_expand] update_mutation_response_expand_None"
] = {
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
    "presigned_url": GenericRepr(
        "Url('https://pytest_invalid_presigned_url.com/file')",
    ),
    "thumbnail_url": GenericRepr(
        "Url('https://pytest_invalid_thumbnail_url.com/file')",
    ),
    "type": ".mp4",
}
