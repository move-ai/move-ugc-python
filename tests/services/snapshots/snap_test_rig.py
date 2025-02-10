# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestRigService.test_fetch_service 1"] = GenericRepr(
    "RigService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)

snapshots["TestRigService.test_list list_response"] = {
    "items": [
        {
            "name": "move_mo",
        },
    ],
}

snapshots["TestRigService.test_list rig_list_request"] = [
    [
        """query list {
  listRigs {
    items {
      name
      __typename
    }
  }
}""",
    ],
    {
        "operation_name": None,
        "variable_values": None,
    },
]
