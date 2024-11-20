# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCameraSettingsService.test_fetch_service 1'] = GenericRepr("CameraSettingsService(api_key=SecretStr('**********'), endpoint_url=Url('https://pytest_invalid_endpoint_url.com/'))")

snapshots['TestCameraSettingsService.test_list camera_settings_list_request'] = [
    [
        '''query list {
  listCameraSettings {
    items {
      lens
      __typename
    }
  }
}'''
    ],
    {
        'operation_name': None,
        'variable_values': None
    }
]

snapshots['TestCameraSettingsService.test_list list_response'] = {
    'items': [
        {
            'lens': 'blackmagic-ursa-4k-24mm'
        }
    ],
    'limit': 3757,
    'next_token': {
        'agreement': 'IROVLfjoMfevqGQzKwSq',
        'area': 'MGeUnKHFDBnmrDQHVgvC',
        'contain': 'ItsodpERiRYnOOBLwsUj',
        'design': 'KQzXIRcgffyxzegWhSCA',
        'director': 'oksQozLDQIKUXTOVnSgL',
        'figure': 'UGNjTUxVagRUsmeXePiR',
        'garden': 'HJNyPHvohoqQteqypgTr',
        'newspaper': 'awilNVmYFmacFDbYHCfB',
        'really': 'bzvYFNrFxckhfCPzGMPQ',
        'set': 'psGGIszJTdvgqoXarfFt',
        'site': 'wqiGgdMEXPdaWjqWDjsW',
        'so': 'CgTFQSEFOSeUlDbpOYnf',
        'stuff': 'UAkAvbvbIjMdtUGoSlUv'
    }
}
