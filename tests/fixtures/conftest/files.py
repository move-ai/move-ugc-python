"""File fixtures."""

import json
from typing import Dict

import pytest
from graphql.execution.execute import ExecutionResult

from move_ugc.gql_requests.file import generate_share_code
from tests.constants import CREATE_FILE_MUTATION, UPDATE_FILE_MUTATION

FakeFileJson = Dict[str, Dict[str, str]]


@pytest.fixture
def fake_file_json(files_fixtures_path, metadata_for_update) -> FakeFileJson:
    """Fixture to return a fake file.

    Args:
        files_fixtures_path (str): Path to files fixtures.
        metadata_for_update (dict[str, Any]): Metadata for update.

    Returns:
        FakeFileJson: Fake file.
    """
    with open(f"{files_fixtures_path}/fake_file.json") as file_json:
        file_json_obj = json.load(file_json)
        file_json_obj["metadata"] = json.dumps(metadata_for_update, default=str)
        return file_json_obj


@pytest.fixture
def fake_get_file_response(fake_file_json) -> FakeFileJson:
    """Fixture to return a fake file response for getFile query.

    Args:
        fake_file_json (dict[str, str]): Fake file json.

    Returns:
        FakeFileJson: Fake file response.
    """
    return {"getFile": fake_file_json}


@pytest.fixture
def fake_create_file_response(fake_file_json) -> FakeFileJson:
    """Fixture to return a fake file response for createFile mutation.

    Args:
        fake_file_json (dict[str, str]): Fake file json.

    Returns:
        FakeFileJson: Fake file response.
    """
    return {CREATE_FILE_MUTATION: fake_file_json}


@pytest.fixture
def file_not_found_json(files_fixtures_path) -> FakeFileJson:
    """Fixture to return a fake file.

    Args:
        files_fixtures_path (str): Path to files fixtures.

    Returns:
        FakeFileJson: Fake file.
    """
    with open(f"{files_fixtures_path}/file_not_found.json") as file_json:
        return json.load(file_json)


@pytest.fixture
def file_retrieve_response(
    mock_transport,
    fake_get_file_response,
    introspection_result,
):
    """Fixture to return a fake file response for retrieve query.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_get_file_response (dict[str, str]): Fake file json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    file_response = ExecutionResult(data=fake_get_file_response)
    mock_transport.side_effect = [introspection_result, file_response]  # noqa: WPS204
    yield file_response


@pytest.fixture
def file_retrieve_response_no_thumbnail(
    mock_transport,
    fake_get_file_response,
    introspection_result,
):
    """Fixture to return a fake file response for retrieve query with no thumbnail.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_get_file_response (dict[str, str]): Fake file json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    fake_get_file_response["getFile"].pop("thumbnailUrl")
    file_response = ExecutionResult(data=fake_get_file_response)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response


@pytest.fixture
def file_retrieve_response_with_client(
    mock_transport,
    fake_get_file_response,
    introspection_result,
    fake_client_type,
):
    """Fixture to return a fake file response for retrieve query with client.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_get_file_response (FakeFileJson): Fake file json.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    fake_file_response_with_client = fake_get_file_response.copy()
    fake_file_response_with_client["getFile"]["client"] = fake_client_type
    file_response = ExecutionResult(data=fake_file_response_with_client)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response


@pytest.fixture
def file_not_found_response(
    mock_transport,
    file_not_found_json,
    introspection_result,
):
    """Fixture to return a fake file not found response.

    Args:
        mock_transport (MagicMock): Mock transport.
        file_not_found_json (FakeFileJson): Fake file json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    file_response = ExecutionResult(errors=file_not_found_json)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response


@pytest.fixture
def file_create_response(
    mock_transport,
    fake_create_file_response,
    introspection_result,
):
    """Fixture to return a fake file response for create mutation.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_create_file_response (FakeFileJson): Fake file json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    file_response = ExecutionResult(data=fake_create_file_response)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response


@pytest.fixture
def file_update_response(
    mock_transport,
    fake_create_file_response,
    introspection_result,
):
    """Fixture to return a fake file response for update mutation.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_create_file_response (FakeFileJson): Fake file json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    fake_file_response = fake_create_file_response.copy()
    # Overwrite createFile with updateFile
    fake_file_response[UPDATE_FILE_MUTATION] = fake_file_response[CREATE_FILE_MUTATION]
    fake_file_response.pop(CREATE_FILE_MUTATION)
    file_response = ExecutionResult(data=fake_file_response)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response


@pytest.fixture
def file_create_response_with_client(
    mock_transport,
    fake_create_file_response,
    introspection_result,
    fake_client_type,
):
    """Fixture to return a fake file response for create mutation with client.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_create_file_response (FakeFileJson): Fake file json.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    fake_file_response_with_client = fake_create_file_response.copy()
    fake_file_response_with_client[CREATE_FILE_MUTATION]["client"] = fake_client_type
    file_response = ExecutionResult(data=fake_file_response_with_client)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response


@pytest.fixture
def file_update_response_with_client(
    mock_transport,
    fake_create_file_response,
    introspection_result,
    fake_client_type,
):
    """Fixture to return a fake file response for update mutation with client.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_create_file_response (FakeFileJson): Fake file json.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    fake_file_response_with_client = fake_create_file_response.copy()
    # Overwrite createFile with updateFile
    fake_file_response_with_client[CREATE_FILE_MUTATION]["client"] = fake_client_type
    fake_file_response_with_client[
        UPDATE_FILE_MUTATION
    ] = fake_file_response_with_client[CREATE_FILE_MUTATION]
    fake_file_response_with_client.pop(CREATE_FILE_MUTATION)
    file_response = ExecutionResult(data=fake_file_response_with_client)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response


@pytest.fixture
def share_code_response(
    mock_transport,
    faker,
    introspection_result,
):
    """Fixture to return a fake share code response.

    Args:
        mock_transport (MagicMock): Mock transport.
        faker (Faker): Faker fixture.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        share_code_response (ExecutionResult): Fake share code response.
    """
    fake_share_code_response = {
        generate_share_code.key: {
            "code": faker.pystr(),
            # Hard code both created and expires datetime
            # because faker & freezegun don't seem to work on windows
            # properly and changes values each time for this test
            "created": "2014-04-25T09:00:00.00",
            "expires": "2014-04-25T09:15:00.00",
            "file": {"id": faker.uuid4()},
            "url": faker.url(),
        },
    }
    share_code_response = ExecutionResult(data=fake_share_code_response)
    mock_transport.side_effect = [introspection_result, share_code_response]
    yield share_code_response
