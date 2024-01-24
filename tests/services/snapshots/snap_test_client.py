# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestClientService.test_fetch_service 1"] = GenericRepr(
    "ClientService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)

snapshots["TestClientService.test_retrieve retrieve_query"] = [
    [
        """query retrieve {
  client {
    id
    name
    created
    metadata
    portal
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": None,
    },
]

snapshots["TestClientService.test_retrieve retrieve_response"] = {
    "created": GenericRepr("datetime.datetime(2023, 6, 12, 0, 0, tzinfo=TzInfo(UTC))"),
    "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
    "metadata": {
        "foo": "bar",
    },
    "name": "PYTEST_INVALID_CLIENT_NAME",
    "portal": GenericRepr(
        "Url('https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=')",
    ),
}

snapshots["TestClientService.test_update update_query"] = [
    [
        """mutation update($metadata: AWSJSON!) {
  updateClient(metadata: $metadata) {
    id
    name
    created
    metadata
    portal
    __typename
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "metadata": '{"decade": -127471.91004658, "other": 4537, "draw": 9025, "table": "fPlGoqlVJAWBmofrulqS", "huge": "RLQMnHdwIMQHuSbBEcSq", "last": "CliYtuFCSJkGbKACMVZc", "trouble": "1982-01-05 12:28:54", "analysis": "ableRsSGSBRpUxDKSTZs", "house": "EQQpSzpRFSYEmmcBHMyX", "director": "-947039390768730142270977422821786185341130903676661937944160217375.3552236429914030334971362203889763798631388053"}',
        },
    },
]

snapshots["TestClientService.test_update update_response"] = {
    "created": GenericRepr("datetime.datetime(2023, 6, 12, 0, 0, tzinfo=TzInfo(UTC))"),
    "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
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
    "name": "PYTEST_INVALID_CLIENT_NAME",
    "portal": GenericRepr(
        "Url('https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=')",
    ),
}
