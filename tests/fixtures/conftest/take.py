"""Take fixtures."""
import json
from typing import Any, Dict

import pytest
from graphql.execution.execute import ExecutionResult

from move_ugc.schemas.additional_file import TakeAdditionalFileKeys
from tests.constants import CREATE_TAKE_MUTATION

FakeTakeJson = Dict[str, Any]


@pytest.fixture
def fake_take_json(take_fixtures_path) -> FakeTakeJson:
    """Fixture to return a fake take.

    Args:
        take_fixtures_path (str): Path to take fixtures.

    Returns:
        FakeTakeJson: Fake take.
    """
    with open(f"{take_fixtures_path}/fake_take.json") as take_json:
        return json.load(take_json)


@pytest.fixture
def fake_create_take_response(fake_take_json) -> FakeTakeJson:
    """Fixture to return a fake take response for createTake mutation.

    Args:
        fake_take_json (dict[str, str]): Fake take json.

    Returns:
        FakeTakeJson: Fake take response.
    """
    return {CREATE_TAKE_MUTATION: fake_take_json}


@pytest.fixture
def take_create_response(
    mock_transport,
    fake_create_take_response,
    introspection_result,
) -> FakeTakeJson:
    """Fixture to return a fake take response for createTake mutation.

    Args:
        fake_create_take_response (dict[str, str]): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeTakeJson: Fake take response.
    """
    take_response = ExecutionResult(data=fake_create_take_response)
    mock_transport.side_effect = [introspection_result, take_response]
    yield take_response


@pytest.fixture
def take_create_response_with_client(
    mock_transport,
    fake_create_take_response,
    introspection_result,
    fake_client_type,
) -> FakeTakeJson:
    """Fixture to return a fake take response for createTake mutation with client.

    Args:
        fake_create_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        FakeTakeJson: Fake take response.
    """
    fake_take_response_with_client = fake_create_take_response.copy()
    fake_take_response_with_client[CREATE_TAKE_MUTATION]["client"] = fake_client_type
    take_response = ExecutionResult(data=fake_take_response_with_client)
    mock_transport.side_effect = [introspection_result, take_response]
    yield take_response


@pytest.fixture
def take_create_response_with_video_file(
    mock_transport,
    fake_create_take_response,
    introspection_result,
    fake_file_json,
) -> FakeTakeJson:
    """Fixture to return a fake take response for createTake mutation with video file.

    Args:
        fake_create_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeTakeJson: Fake take response.
    """
    fake_take_response_with_file = fake_create_take_response.copy()
    fake_take_response_with_file[CREATE_TAKE_MUTATION]["videoFile"] = fake_file_json
    take_response = ExecutionResult(data=fake_take_response_with_file)
    mock_transport.side_effect = [introspection_result, take_response]
    yield take_response


@pytest.fixture
def take_create_response_with_additional_files(
    mock_transport,
    fake_create_take_response,
    introspection_result,
    fake_file_json,
) -> FakeTakeJson:
    """Fixture to return a fake take response for createTake mutation with additional files.

    Args:
        fake_create_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeTakeJson: Fake take response.
    """
    fake_take_response_with_file = fake_create_take_response.copy()
    fake_take_response_with_file[CREATE_TAKE_MUTATION]["additionalFiles"] = [
        {
            "key": TakeAdditionalFileKeys.depth.value,
            "file": fake_file_json,
        },
    ]
    take_response = ExecutionResult(data=fake_take_response_with_file)
    mock_transport.side_effect = [introspection_result, take_response]
    yield take_response
