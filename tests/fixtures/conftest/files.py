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
def file_retrieve_response(mock_transport, fake_file_json, introspection_result):
    """Fixture to return a fake file response for retrieve query.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_file_json (dict[str, str]): Fake file json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    file_response = ExecutionResult(data=fake_file_json)
    mock_transport.side_effect = [introspection_result, file_response]
    yield file_response


@pytest.fixture
def file_retrieve_response_with_client(
    mock_transport,
    fake_file_json,
    introspection_result,
    fake_client_type,
):
    """Fixture to return a fake file response for retrieve query with client.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_file_json (FakeFileJson): Fake file json.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        file_response (ExecutionResult): Fake file response.
    """
    fake_file_response_with_client = fake_file_json.copy()
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
