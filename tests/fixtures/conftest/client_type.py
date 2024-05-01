"""Client Type fixtures for the UGC Client."""
import json
from typing import Dict

import pytest
from graphql.execution.execute import ExecutionResult

from tests.constants import GET_CLIENT_QUERY, UPDATE_CLIENT_MUTATION

FakeClientJson = Dict[str, Dict[str, str]]


@pytest.fixture
def fake_client_type(client_fixtures_path) -> FakeClientJson:
    """Fixture to return a fake client type.

    Args:
        client_fixtures_path (str): Path to client fixtures.

    Returns:
        FakeClientJson: Fake client type.
    """
    with open(f"{client_fixtures_path}/fake_client_type.json") as json_file:
        return json.load(json_file)


@pytest.fixture
def fake_update_client_response(fake_client_type) -> FakeClientJson:
    """Fixture to return a fake client response for update client mutation.

    Args:
        fake_client_type (dict[str, str]): Fake client json.

    Returns:
        FakeClientJson: Fake client response.
    """
    return {UPDATE_CLIENT_MUTATION: fake_client_type}


@pytest.fixture
def fake_get_client_response(fake_client_type) -> FakeClientJson:
    """Fixture to return a fake client response for client query.

    Args:
        fake_client_type (dict[str, str]): Fake client json.

    Returns:
        FakeClientJson: Fake client response.
    """
    return {GET_CLIENT_QUERY: fake_client_type}


@pytest.fixture
def client_retrieve_response(
    mock_transport,
    fake_get_client_response,
    introspection_result,
):
    """Fixture to return a fake client response for retrieve query.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_get_client_response (dict[str, str]): Fake client json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        client_response (ExecutionResult): Fake client response.
    """
    client_response = ExecutionResult(data=fake_get_client_response)
    mock_transport.side_effect = [introspection_result, client_response]
    yield client_response


@pytest.fixture
def client_update_response(
    mock_transport,
    faker,
    metadata_for_update,
    fake_update_client_response,
    introspection_result,
):
    """Fixture to return a fake client response for update query.

    Args:
        mock_transport (MagicMock): Mock transport.
        metadata_for_update: fake metadata for update mutations
        faker (Faker): Faker instance.
        fake_update_client_response (dict[str, str]): Fake client json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        client_response (ExecutionResult): Fake client response.
    """
    fake_update_client_response[UPDATE_CLIENT_MUTATION]["metadata"] = json.dumps(
        metadata_for_update,
        default=str,
    )
    client_response = ExecutionResult(data=fake_update_client_response)
    mock_transport.side_effect = [introspection_result, client_response]
    yield client_response
