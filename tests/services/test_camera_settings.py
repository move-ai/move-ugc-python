"""Unit tests for using the camera settings service."""

from tests.services.testcases import ServicesTestCase


class TestCameraSettingsService(ServicesTestCase):  # noqa: WPS214
    """Test camera settings service."""

    service_name = "camera_settings"

    def test_list(self, snapshot, snapshot_json, camera_settings_list_response):
        """Test listing camera settings.

        This should test -> `ugc.camera_settings.list()`

        Args:
            snapshot (SnapshotFixture): Pytest snapshot fixture.
            snapshot_json: Snapshot JSON fixture.
            camera_settings_list_response (dict): Camera settings list response.
        """
        camera_settings_list = self.client.camera_settings.list()
        self.assert_execute(snapshot, name="camera_settings_list_request")
        assert camera_settings_list.model_dump() == snapshot_json
