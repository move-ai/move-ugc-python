# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestJobService.test_create[empty_expand] create_mutation_expand_[]"] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createSingleCamJob(takeId: $take_id, metadata: $metadata) {
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "take_id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
        },
    },
]

snapshots["TestJobService.test_create[empty_expand] create_response_expand_[]"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_create[expand_client] create_mutation_expand_client"] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createSingleCamJob(takeId: $take_id, metadata: $metadata) {
    id
    created
    metadata
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "take_id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
        },
    },
]

snapshots["TestJobService.test_create[expand_client] create_response_expand_client"] = {
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
    "outputs": None,
    "state": "RUNNING",
    "take": None,
}

snapshots[
    "TestJobService.test_create[expand_outputs] create_mutation_expand_outputs"
] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createSingleCamJob(takeId: $take_id, metadata: $metadata) {
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "take_id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
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
    "outputs": [
        {
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
            "key": "fbx",
        },
    ],
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_create[expand_take] create_mutation_expand_take"] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createSingleCamJob(takeId: $take_id, metadata: $metadata) {
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "take_id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
        },
    },
]

snapshots["TestJobService.test_create[expand_take] create_response_expand_take"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "state": "RUNNING",
    "take": {
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
        "sources": None,
    },
}

snapshots["TestJobService.test_create[no_expand] create_mutation_expand_None"] = [
    [
        """mutation create($take_id: String!, $metadata: AWSJSON) {
  createSingleCamJob(takeId: $take_id, metadata: $metadata) {
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
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
            "take_id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
        },
    },
]

snapshots["TestJobService.test_create[no_expand] create_response_expand_None"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
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
            "outputs": None,
            "state": "RUNNING",
            "take": None,
        },
    ],
    "limit": 433,
    "next_token": {
        "ability": "TQtLfcoVjFwLvYXpwnub",
        "attention": GenericRepr(
            "Decimal('-94421184485993957790167155643305.1958182142991397918239901454')",
        ),
        "contain": "http://armstrong.net/postsindex.html",
        "evening": "evqGQzKwSqfRoArzmKBW",
        "figure": "alvaradocharles@example.org",
        "set": 2642,
        "so": -1000508466.811,
        "stuff": GenericRepr(
            "Decimal('-39859709324198798762190136418988284335952316805377455642414452157481053737582709181317757113.286861444124491')",
        ),
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
            "outputs": None,
            "state": "RUNNING",
            "take": None,
        },
    ],
    "limit": 433,
    "next_token": {
        "ability": "TQtLfcoVjFwLvYXpwnub",
        "attention": GenericRepr(
            "Decimal('-94421184485993957790167155643305.1958182142991397918239901454')",
        ),
        "contain": "http://armstrong.net/postsindex.html",
        "evening": "evqGQzKwSqfRoArzmKBW",
        "figure": "alvaradocharles@example.org",
        "set": 2642,
        "so": -1000508466.811,
        "stuff": GenericRepr(
            "Decimal('-39859709324198798762190136418988284335952316805377455642414452157481053737582709181317757113.286861444124491')",
        ),
    },
}

snapshots["TestJobService.test_retrieve[empty_expand] retrieve_query_expand_[]"] = [
    [
        """query retrieve($id: ID!) {
  getJob(jobId: $id) {
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
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
    "outputs": None,
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
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
    "outputs": None,
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
    outputs {
      key
      file {
        id
        created
        type
        metadata
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
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
    "outputs": [
        {
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
            "key": "fbx",
        },
    ],
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
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
    "outputs": None,
    "state": "RUNNING",
    "take": {
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
        "sources": None,
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

snapshots["TestJobService.test_retrieve[no_expand] retrieve_response_expand_None"] = {
    "client": None,
    "created": GenericRepr(
        "datetime.datetime(2023, 7, 10, 12, 13, 56, 615715, tzinfo=TzInfo(UTC))",
    ),
    "id": "job-59ff6b90-e03c-41cf-8d20-58926e0e4f3f",
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
    "outputs": None,
    "state": "RUNNING",
    "take": None,
}

snapshots["TestJobService.test_update update_mutation"] = [
    [
        """mutation update($id: String!, $metadata: AWSJSON!) {
  updateJob(id: $id, metadata: $metadata) {
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
            "id": "b898a7a5-37be-4600-bdc6-8ffa06c7a4f6",
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
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
    "outputs": None,
    "state": "RUNNING",
    "take": None,
}
