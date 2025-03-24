# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestClientService.test_fetch_service 1"] = GenericRepr(
    "ClientService(api_key=SecretStr('**********'), endpoint_url=HttpUrl('https://pytest_invalid_endpoint_url.com/'))",
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
        "HttpUrl('https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=')",
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
            "metadata": '{"decade": "zAvJMvacZIYSmMsDUNvC", "other": "XbBPNrbhtJksbBuoWXSK", "draw": "PnbQcVNCliYtuFCSJkGb", "table": "ACMVZcKAiGBcYgCzHAad", "huge": "eFaLyHGEQQpSzpRFSYEm", "last": "dnZCcfgZNBnaEkbOzIyO", "trouble": "UgnhIyaDJzohUigyDYZf", "analysis": "UmKdTFlLMIuIvJkRJnoM", "house": "aYyOUXkJPUjPJGpDdakX", "director": "KNmpExWtgQLcAEuRyBkN"}',
        },
    },
]

snapshots["TestClientService.test_update update_response"] = {
    "created": GenericRepr("datetime.datetime(2023, 6, 12, 0, 0, tzinfo=TzInfo(UTC))"),
    "id": "client-47c982ec-60ab-4a0b-9286-2db4a76abc18",
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
    "name": "PYTEST_INVALID_CLIENT_NAME",
    "portal": GenericRepr(
        "HttpUrl('https://app.svix.com/login?primaryColorLight=39ddef&primaryColorDark=39ddef#key=')",
    ),
}
