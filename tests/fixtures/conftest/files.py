"""File fixtures."""
import json
from typing import Dict

import pytest
from graphql.execution.execute import ExecutionResult

FakeFileJson = Dict[str, Dict[str, str]]


@pytest.fixture
def fake_file_json(files_fixtures_path) -> FakeFileJson:
    """Fixture to return a fake file.

    Args:
        files_fixtures_path (str): Path to files fixtures.

    Returns:
        FakeFileJson: Fake file.
    """
    with open(f"{files_fixtures_path}/fake_file.json") as file_json:
        return json.load(file_json)


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
    return {"createFile": fake_file_json}


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
    fake_file_response_with_client["createFile"]["client"] = fake_client_type
    file_response = ExecutionResult(data=fake_file_response_with_client)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response