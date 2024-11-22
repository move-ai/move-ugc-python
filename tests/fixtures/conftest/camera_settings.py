"""Camera settings fixtures."""
import json
from typing import Any, Dict

import pytest
from graphql.execution.execute import ExecutionResult

from tests.constants import LIST_CAMERA_SETTINGS_QUERY
from tests.fixtures.conftest.commons import build_list_response

FakeCameraSettingsJson = Dict[str, Any]


def mock_response(fake_response, mock_transport, introspection_result):
    """Mock response for graphql.

    Args:
        fake_response (dict[str, Any]): Fake response.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.

    Returns:
        ExecutionResult: Fake response.
    """
    camera_settings_response = ExecutionResult(data=fake_response)
    mock_transport.side_effect = [introspection_result, camera_settings_response]
    return camera_settings_response


@pytest.fixture
def fake_camera_settings_json(
    camera_settings_fixtures_path,
    metadata_for_update,
) -> FakeCameraSettingsJson:
    """Fixture to return a fake camera settings.

    Args:
        camera_settings_fixtures_path (str): Path to job fixtures.
        metadata_for_update (dict[str, str]): Metadata for update.

    Returns:
        FakeCameraSettingsJson: Fake Camera Setting.
    """
    with open(f"{camera_settings_fixtures_path}/fake_camera_settings.json") as job_json:
        camera_settings_json_obj = json.load(job_json)
        camera_settings_json_obj["metadata"] = json.dumps(
            metadata_for_update,
            default=str,
        )
        return camera_settings_json_obj


@pytest.fixture
def fake_list_camera_settings_response(
    fake_camera_settings_json,
    faker,
) -> FakeCameraSettingsJson:
    """Fixture to return a fake list camera settings response.

    Args:
        fake_camera_settings_json (dict[str, str]): Fake job json.
        faker (Faker): Faker.

    Returns:
        FakeCameraSettingsJson: Fake Camera Setting.
    """
    return {
        LIST_CAMERA_SETTINGS_QUERY: build_list_response(
            fake_response=fake_camera_settings_json,
            faker=faker,
        ),
    }


@pytest.fixture
def camera_settings_list_response(
    mock_transport,
    fake_list_camera_settings_response,
    introspection_result,
):
    """Fixture to return a fake camera settings list response.

    Args:
        mock_transport (MockTransport): Mock transport.
        fake_list_camera_settings_response (dict[str, Any]): Fake list camera settings response.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeCameraSettingsJson: Fake Camera Setting.
    """
    camera_settings_response = ExecutionResult(data=fake_list_camera_settings_response)
    mock_transport.side_effect = [introspection_result, camera_settings_response]
    yield camera_settings_response
