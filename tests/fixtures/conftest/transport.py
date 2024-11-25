"""Define mock transport for the client."""

import json
from unittest.mock import patch

import pytest
from graphql.execution.execute import ExecutionResult


@pytest.fixture
def mock_transport(request):
    """Mock the transport.

    Args:
        request: The pytest request object.

    Yields:
        mock_execute: The mocked execute method.
    """
    with patch("gql.transport.requests.RequestsHTTPTransport.execute") as mock_execute:
        if request.cls is not None:
            request.cls.mock_execute = mock_execute
        yield mock_execute


@pytest.fixture
def introspection_result(json_fixtures_path):
    """Fixture to return the introspection JSON.

    Args:
        json_fixtures_path: The json fixtures path fixture.

    Returns:
        ExecutionResult: The introspection result.
    """
    with open(f"{json_fixtures_path}/introspection.json") as file_json:
        introspection = json.load(file_json)
        return ExecutionResult(data=introspection["data"])
