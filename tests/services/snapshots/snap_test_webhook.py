# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestWebhooksService.test_add_webhook add_webhook_query"] = [
    [
        """mutation addWebhook($events: [String!]!, $uid: String!, $url: String!, $description: String, $secret: String) {
  upsertWebhookEndpoint(
    events: $events
    uid: $uid
    url: $url
    description: $description
    secret: $secret
  ) {
    description
    events
    uid
    url
    secret
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "description": "ZPnbQcVNCliYtuFCSJkG",
            "events": [
                "ugc.jobs.state.completed",
            ],
            "secret": "XbBPNrbhtJksbBuoWXSK",
            "uid": "WkDQwclzAvJMvacZIYSm",
            "url": "https://dunn.com/",
        },
    },
]

snapshots["TestWebhooksService.test_add_webhook add_webhook_response"] = {
    "description": "PYTEST_INVALID_DESCRIPTION",
    "events": [
        "PYTEST_INVALID_EVENT",
    ],
    "secret": GenericRepr("SecretStr('**********')"),
    "uid": "PYTEST_INVALID_UID",
    "url": GenericRepr("Url('https://webhook.site/invalid')"),
}

snapshots["TestWebhooksService.test_add_without_secret add_webhook_query"] = [
    [
        """mutation addWebhook($events: [String!]!, $uid: String!, $url: String!, $description: String, $secret: String) {
  upsertWebhookEndpoint(
    events: $events
    uid: $uid
    url: $url
    description: $description
    secret: $secret
  ) {
    description
    events
    uid
    url
    secret
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": {
            "description": "",
            "events": [
                "ugc.jobs.state.completed",
            ],
            "secret": None,
            "uid": "WkDQwclzAvJMvacZIYSm",
            "url": "https://dunn.com/",
        },
    },
]

snapshots["TestWebhooksService.test_add_without_secret add_webhook_response"] = {
    "description": "PYTEST_INVALID_DESCRIPTION",
    "events": [
        "PYTEST_INVALID_EVENT",
    ],
    "secret": GenericRepr("SecretStr('**********')"),
    "uid": "PYTEST_INVALID_UID",
    "url": GenericRepr("Url('https://webhook.site/invalid')"),
}

snapshots["TestWebhooksService.test_fetch_service 1"] = GenericRepr(
    "WebhookService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)
