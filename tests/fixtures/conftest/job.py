"""Job fixtures."""
import json
from typing import Any, Dict

import pytest
from graphql.execution.execute import ExecutionResult

from tests.constants import CREATE_JOB_MUTATION

FakeJobJson = Dict[str, Any]


@pytest.fixture
def fake_job_json(job_fixtures_path) -> FakeJobJson:
    """Fixture to return a fake job.

    Args:
        job_fixtures_path (str): Path to job fixtures.

    Returns:
        FakeJobJson: Fake job.
    """
    with open(f"{job_fixtures_path}/fake_job.json") as job_json:
        return json.load(job_json)


@pytest.fixture
def fake_create_job_response(fake_job_json) -> FakeJobJson:
    """Fixture to return a fake job response for createJob mutation.

    Args:
        fake_job_json (dict[str, str]): Fake job json.

    Returns:
        FakeJobJson: Fake job response.
    """
    return {CREATE_JOB_MUTATION: fake_job_json}


@pytest.fixture
def job_create_response(
    mock_transport,
    fake_create_job_response,
    introspection_result,
) -> FakeJobJson:
    """Fixture to return a fake job response for createJob mutation.

    Args:
        fake_create_job_response (dict[str, str]): Fake job json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeJobJson: Fake job response.
    """
    job_response = ExecutionResult(data=fake_create_job_response)
    mock_transport.side_effect = [introspection_result, job_response]
    yield job_response


@pytest.fixture
def job_create_response_with_client(
    mock_transport,
    fake_create_job_response,
    introspection_result,
    fake_client_type,
) -> FakeJobJson:
    """Fixture to return a fake job response for createJob mutation with client.

    Args:
        fake_create_job_response (dict[str, str]): Fake job json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        FakeJobJson: Fake job response.
    """
    fake_create_job_response[CREATE_JOB_MUTATION]["client"] = fake_client_type
    job_response_client = ExecutionResult(data=fake_create_job_response)
    mock_transport.side_effect = [introspection_result, job_response_client]
    yield job_response_client


@pytest.fixture
def job_create_response_with_take(
    mock_transport,
    fake_create_job_response,
    introspection_result,
    fake_take_json,
) -> FakeJobJson:
    """Fixture to return a fake job response for createJob mutation with take.

    Args:
        fake_create_job_response (dict[str, str]): Fake job json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_take_json (dict[str, str]): Fake take type.

    Yields:
        FakeJobJson: Fake job response.
    """
    fake_create_job_response[CREATE_JOB_MUTATION]["take"] = fake_take_json
    job_response_with_take = ExecutionResult(data=fake_create_job_response)
    mock_transport.side_effect = [introspection_result, job_response_with_take]
    yield job_response_with_take


@pytest.fixture
def job_create_response_with_outputs(
    mock_transport,
    fake_create_job_response,
    introspection_result,
    fake_file_json,
) -> FakeJobJson:
    """Fixture to return a fake job response for createJob mutation with outputs.

    Args:
        fake_create_job_response (FakeJobJson): Fake job json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeJobJson: Fake job response.
    """
    fake_create_job_response[CREATE_JOB_MUTATION]["outputs"] = [
        {
            "key": "mp4",
            "file": fake_file_json,
        },
        {
            "key": "fbx",
            "file": fake_file_json,
        },
    ]
    job_response_with_outputs = ExecutionResult(data=fake_create_job_response)
    mock_transport.side_effect = [introspection_result, job_response_with_outputs]
    yield job_response_with_outputs
