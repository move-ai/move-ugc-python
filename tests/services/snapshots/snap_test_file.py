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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "type": "wav",
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "type": "wav",
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "type": "wav",
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
    "created": GenericRepr("datetime.datetime(2020, 8, 27, 13, 27, 47)"),
    "expires": GenericRepr("datetime.datetime(1993, 12, 30, 11, 32, 53)"),
    "file_id": "e49022be-849a-43db-904d-dfc0ac8201d5",
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
}
