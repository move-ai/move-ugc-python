"""Unit tests for using the camera settings service."""
import pytest
from gql.transport.exceptions import TransportQueryError
from graphql.execution.execute import ExecutionResult
from pydantic import ValidationError

from tests.constants import LIST_CAMERA_SETTINGS_QUERY
from tests.services.testcases import ServicesTestCase


class TestCameraSettingsService(ServicesTestCase):  # noqa: WPS214
    """Test camera settings service."""

    service_name = "camera_settings"

    def test_list(self,  snapshot, camera_settings_list_response):
        """Test listing jobs.

        This should test -> `ugc.jobs.list()`

        Args:
            take_id: The take id fixture.
            snapshot: The snapshot fixture.
            jobs_list_response: job list response fixture.
        """
        camera_settings_list = self.client.camera_settings.list()
        self.assert_execute(snapshot, name="camera_settings_list_request")
        snapshot.assert_match(
            camera_settings_list.model_dump(),
            name="list_response",
        )