"""Rig fixture for testing."""

import json
from typing import Any, Dict

import pytest
from graphql.execution.execute import ExecutionResult

from tests.constants import LIST_RIG_QUERY
from tests.fixtures.conftest.commons import build_list_response

FakeRigJson = Dict[str, Any]


def mock_response(fake_response, mock_transport, introspection_result):
    """Mock response for graphql.

    Args:
        fake_response (dict[str, Any]): Fake response.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.

    Returns:
        ExecutionResult: Fake response.
    """
    rig_response = ExecutionResult(data=fake_response)
    mock_transport.side_effect = [introspection_result, rig_response]
    return rig_response


@pytest.fixture
def fake_rig_json(
    rig_fixtures_path,
) -> FakeRigJson:
    """Fixture to return a fake rig.

    Args:
        rig_fixtures_path (str): Path to job fixtures.

    Returns:
        FakeRigJson: Fake Rig.
    """
    with open(f"{rig_fixtures_path}/fake_rig.json") as job_json:
        return json.load(job_json)


@pytest.fixture
def fake_list_rig_response(
    fake_rig_json,
    faker,
) -> FakeRigJson:
    """Fixture to return a fake list rig response.

    Args:
        fake_rig_json (FakeRigJson): Fake rig json.
        faker (Faker): Faker instance.

    Returns:
        FakeRigJson: Fake Rig.
    """
    return {
        LIST_RIG_QUERY: build_list_response(fake_rig_json, faker),
    }


@pytest.fixture
def rig_list_response(
    mock_transport,
    fake_list_rig_response,
    introspection_result,
):
    """Fixture to mock response for list rig.

    Args:
        mock_transport (MockTransport): Mock transport.
        fake_list_rig_response (FakeRigJson): Fake rig json.
        introspection_result (dict[str, str]): Introspection result.

    Returns:
        ExecutionResult: Fake response.
    """
    rig_response = ExecutionResult(data=fake_list_rig_response)
    mock_transport.side_effect = [introspection_result, rig_response]
    return rig_response
