# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["TestCameraSettingsService.test_fetch_service 1"] = GenericRepr(
    "CameraSettingsService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))",
)

snapshots["TestCameraSettingsService.test_list camera_settings_list_request"] = [
    [
        """query list {
  listCameraSettings {
    items {
      lens
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

snapshots["TestCameraSettingsService.test_list list_response"] = {
    "after": '{"newspaper": "awilNVmYFmacFDbYHCfB", "really": "bzvYFNrFxckhfCPzGMPQ", "area": "MGeUnKHFDBnmrDQHVgvC", "garden": "HJNyPHvohoqQteqypgTr", "design": "KQzXIRcgffyxzegWhSCA", "agreement": "IROVLfjoMfevqGQzKwSq", "site": "wqiGgdMEXPdaWjqWDjsW", "director": "oksQozLDQIKUXTOVnSgL", "set": "psGGIszJTdvgqoXarfFt", "so": "CgTFQSEFOSeUlDbpOYnf", "contain": "ItsodpERiRYnOOBLwsUj", "figure": "UGNjTUxVagRUsmeXePiR", "stuff": "UAkAvbvbIjMdtUGoSlUv"}',
    "first": 3757,
    "items": [
        {
            "lens": "blackmagic-ursa-4k-24mm",
        },
    ],
}
