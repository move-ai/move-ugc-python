"""Take fixtures."""
import json
from typing import Any, Dict

import pytest
from graphql.execution.execute import ExecutionResult

from move_ugc.schemas.additional_file import TakeAdditionalFileKeys
from tests.constants import (
    CLIENT_LITERAL,
    CREATE_TAKE_MUTATION,
    GET_TAKE_QUERY,
    LIST_TAKES_QUERY,
    UPDATE_TAKE_MUTATION,
)
from tests.fixtures.conftest.commons import build_list_response

FakeTakeJson = Dict[str, Any]


@pytest.fixture
def fake_take_json(take_fixtures_path, metadata_for_update) -> FakeTakeJson:
    """Fixture to return a fake take.

    Args:
        take_fixtures_path (str): Path to take fixtures.
        metadata_for_update (dict[str, Any]): Metadata for update.

    Returns:
        FakeTakeJson: Fake take.
    """
    with open(f"{take_fixtures_path}/fake_take.json") as take_json:
        take_json = json.load(take_json)
        take_json["metadata"] = json.dumps(metadata_for_update, default=str)
        return take_json


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
def fake_update_take_response(fake_take_json) -> FakeTakeJson:
    """Fixture to return a fake take response for updateTake mutation.

    Args:
        fake_take_json (dict[str, str]): Fake take json.

    Returns:
        FakeTakeJson: Fake take response.
    """
    return {UPDATE_TAKE_MUTATION: fake_take_json}


@pytest.fixture
def fake_retrieve_take_response(fake_take_json) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query.

    Args:
        fake_take_json (dict[str, str]): Fake take json.

    Returns:
        FakeTakeJson: Fake take response.
    """
    return {GET_TAKE_QUERY: fake_take_json}


@pytest.fixture
def fake_list_take_response(fake_take_json, faker) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query.

    Args:
        fake_take_json (dict[str, str]): Fake take json.
        faker (Faker): Faker instance.

    Returns:
        FakeTakeJson: Fake take response.
    """
    return {
        LIST_TAKES_QUERY: build_list_response(
            fake_response=fake_take_json,
            faker=faker,
        ),
    }


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
def take_retrieve_response(
    mock_transport,
    fake_retrieve_take_response,
    introspection_result,
) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query.

    Args:
        fake_retrieve_take_response (dict[str, str]): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeTakeJson: Fake take response.
    """
    take_response = ExecutionResult(data=fake_retrieve_take_response)
    mock_transport.side_effect = [introspection_result, take_response]
    yield take_response


@pytest.fixture
def take_update_response(
    mock_transport,
    fake_update_take_response,
    introspection_result,
) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query.

    Args:
        fake_update_take_response (dict[str, str]): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeTakeJson: Fake take response.
    """
    take_response = ExecutionResult(data=fake_update_take_response)
    mock_transport.side_effect = [introspection_result, take_response]
    yield take_response


def build_response_with_client(
    fake_response,
    fake_client_type,
    mock_transport,
    introspection_result,
    key,
):
    """Build response with additional files.

    Args:
        fake_response (FakeTakeJson): Fake take json.
        fake_client_type (dict[str, str]): Fake client type.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        key (str): Key of graphql query.

    Returns:
        FakeTakeJson: Fake take response.
    """
    fake_response[key][CLIENT_LITERAL] = fake_client_type
    take_response = ExecutionResult(data=fake_response)
    mock_transport.side_effect = [introspection_result, take_response]
    return take_response


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
    yield build_response_with_client(
        fake_response=fake_create_take_response.copy(),
        fake_client_type=fake_client_type,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=CREATE_TAKE_MUTATION,
    )


@pytest.fixture
def take_retrieve_response_with_client(
    mock_transport,
    fake_retrieve_take_response,
    introspection_result,
    fake_client_type,
) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query with client.

    Args:
        fake_retrieve_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        FakeTakeJson: Fake take response.
    """
    yield build_response_with_client(
        fake_response=fake_retrieve_take_response.copy(),
        fake_client_type=fake_client_type,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=GET_TAKE_QUERY,
    )


@pytest.fixture
def take_update_response_with_client(
    mock_transport,
    fake_update_take_response,
    introspection_result,
    fake_client_type,
) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query with client.

    Args:
        fake_update_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        FakeTakeJson: Fake take response.
    """
    yield build_response_with_client(
        fake_response=fake_update_take_response.copy(),
        fake_client_type=fake_client_type,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=UPDATE_TAKE_MUTATION,
    )


def build_response_with_video_file(
    fake_response,
    fake_file_json,
    mock_transport,
    introspection_result,
    key,
):
    """Build response with additional files.

    Args:
        fake_response (FakeTakeJson): Fake take json.
        fake_file_json (dict[str, str]): Fake file json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        key (str): Key of graphql query.

    Returns:
        FakeTakeJson: Fake take response.
    """
    fake_response[key]["videoFile"] = fake_file_json
    take_response = ExecutionResult(data=fake_response)
    mock_transport.side_effect = [introspection_result, take_response]
    return take_response


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
    yield build_response_with_video_file(
        fake_response=fake_create_take_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=CREATE_TAKE_MUTATION,
    )


@pytest.fixture
def take_retrieve_response_with_video_file(
    mock_transport,
    fake_retrieve_take_response,
    introspection_result,
    fake_file_json,
) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query with video file.

    Args:
        fake_retrieve_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeTakeJson: Fake take response.
    """
    yield build_response_with_video_file(
        fake_response=fake_retrieve_take_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=GET_TAKE_QUERY,
    )


@pytest.fixture
def take_update_response_with_video_file(
    mock_transport,
    fake_update_take_response,
    introspection_result,
    fake_file_json,
) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query with video file.

    Args:
        fake_update_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeTakeJson: Fake take response.
    """
    yield build_response_with_video_file(
        fake_response=fake_update_take_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=UPDATE_TAKE_MUTATION,
    )


def build_response_with_additional_files(
    fake_response,
    fake_file_json,
    mock_transport,
    introspection_result,
    key,
):
    """Build response with additional files.

    Args:
        fake_response (FakeTakeJson): Fake take json.
        fake_file_json (dict[str, str]): Fake file json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        key (str): Key of graphql query.

    Returns:
        FakeTakeJson: Fake take response.
    """
    fake_response[key]["additionalFiles"] = [
        {
            "key": TakeAdditionalFileKeys.depth.value,
            "file": fake_file_json,
        },
    ]
    take_response = ExecutionResult(data=fake_response)
    mock_transport.side_effect = [introspection_result, take_response]
    return take_response


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
    yield build_response_with_additional_files(
        fake_response=fake_create_take_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=CREATE_TAKE_MUTATION,
    )


@pytest.fixture
def take_retrieve_response_with_additional_files(
    mock_transport,
    fake_retrieve_take_response,
    introspection_result,
    fake_file_json,
) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query with additional files.

    Args:
        fake_retrieve_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeTakeJson: Fake take response.
    """
    yield build_response_with_additional_files(
        fake_response=fake_retrieve_take_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=GET_TAKE_QUERY,
    )


@pytest.fixture
def take_update_response_with_additional_files(
    mock_transport,
    fake_update_take_response,
    introspection_result,
    fake_file_json,
) -> FakeTakeJson:
    """Fixture to return a fake take response for getTake query with additional files.

    Args:
        fake_update_take_response (FakeTakeJson): Fake take json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeTakeJson: Fake take response.
    """
    yield build_response_with_additional_files(
        fake_response=fake_update_take_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=UPDATE_TAKE_MUTATION,
    )


@pytest.fixture
def take_not_found_json(take_fixtures_path) -> FakeTakeJson:
    """Fixture to return a fake take error response.

    Args:
        take_fixtures_path (str): Path to take fixtures.

    Returns:
        FakeTakeJson: Fake take response.
    """
    with open(f"{take_fixtures_path}/take_not_found.json") as take_json:
        return json.load(take_json)


@pytest.fixture
def take_not_found_response(
    mock_transport,
    take_not_found_json,
    introspection_result,
):
    """Fixture to return a fake take not found response.

    Args:
        mock_transport (MagicMock): Mock transport.
        take_not_found_json (FakeTakeJson): Fake take json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        take_response (ExecutionResult): Fake take response.
    """
    take_error_response = ExecutionResult(errors=take_not_found_json)
    mock_transport.side_effect = [introspection_result, take_error_response]
    yield take_error_response


@pytest.fixture
def takes_list_response(
    mock_transport,
    fake_list_take_response,
    introspection_result,
):
    """Fixture to return a fake take response for listTakes query.

    Args:
        mock_transport (MockTransport): Mock transport.
        fake_list_take_response (FakeTakeJson): Fake take json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeTakeJson: Fake take response.
    """
    take_response = ExecutionResult(data=fake_list_take_response)
    mock_transport.side_effect = [introspection_result, take_response]
    yield take_response
