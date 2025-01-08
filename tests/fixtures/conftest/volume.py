"""Volume fixtures."""

import json
import os
from typing import Any, Dict

import pytest
from graphql import ExecutionResult

from tests.constants import (
    CREATE_HUMAN_VOLUME_MUTATION,
    GET_VOLUME_QUERY,
    LIST_VOLUMES_QUERY,
)
from tests.fixtures.conftest.commons import build_list_response
from tests.fixtures.conftest.take import (
    build_response_with_additional_sources,
    build_response_with_video_source,
)

FakeVolumeJson = Dict[str, Any]
KEY_LITERAL = "key"
FILE_LITERAL = "file"


@pytest.fixture
def fake_volume_json(volume_fixtures_path, metadata_for_update) -> FakeVolumeJson:
    """Fixture to return a fake volume.

    Args:
        volume_fixtures_path (str): Path to volume fixtures.
        metadata_for_update (dict[str, str]): Metadata for update.

    Returns:
        FakeVolumeJson: Fake volume.
    """
    with open(os.path.join(volume_fixtures_path, "fake_volume.json")) as volume_json:
        volume_json_obj = json.load(volume_json)
        volume_json_obj["metadata"] = json.dumps(metadata_for_update, default=str)
        return volume_json_obj


@pytest.fixture
def fake_create_volume_response(fake_volume_json) -> FakeVolumeJson:
    """Fixture to return a fake volume response for createVolumeWithHuman mutation.

    Args:
        fake_volume_json (dict[str, str]): Fake volume json.

    Returns:
        FakeVolumeJson: Fake volume response.
    """
    return {CREATE_HUMAN_VOLUME_MUTATION: fake_volume_json}


@pytest.fixture
def fake_get_volume_response(fake_volume_json) -> FakeVolumeJson:
    """Fixture to return a fake volume response for getVolume query.

    Args:
        fake_volume_json (dict[str, str]): Fake volume json.

    Returns:
        FakeVolumeJson: Fake volume response.
    """
    return {GET_VOLUME_QUERY: fake_volume_json}


@pytest.fixture
def volume_create_response(
    mock_transport,
    fake_create_volume_response,
    introspection_result,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for createVolumeWithHuman mutation.

    Args:
        fake_create_volume_response (dict[str, str]): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    volume_response = ExecutionResult(data=fake_create_volume_response)
    mock_transport.side_effect = [introspection_result, volume_response]
    yield volume_response


@pytest.fixture
def volume_get_response(
    mock_transport,
    fake_get_volume_response,
    introspection_result,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for getVolume query.

    Args:
        fake_get_volume_response (dict[str, str]): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    volume_response = ExecutionResult(data=fake_get_volume_response)
    mock_transport.side_effect = [introspection_result, volume_response]
    yield volume_response


@pytest.fixture
def volume_create_response_with_client(
    mock_transport,
    fake_create_volume_response,
    introspection_result,
    fake_client_type,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for createVolumeWithHuman mutation with client.

    Args:
        fake_create_volume_response (dict[str, str]): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    fake_create_volume_response[CREATE_HUMAN_VOLUME_MUTATION][
        "client"
    ] = fake_client_type
    volume_response_client = ExecutionResult(data=fake_create_volume_response)
    mock_transport.side_effect = [introspection_result, volume_response_client]
    yield volume_response_client


@pytest.fixture
def volume_get_response_with_client(
    mock_transport,
    fake_get_volume_response,
    introspection_result,
    fake_client_type,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for getVolume query with client.

    Args:
        fake_get_volume_response (dict[str, str]): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    fake_get_volume_response[GET_VOLUME_QUERY]["client"] = fake_client_type
    volume_response_client = ExecutionResult(data=fake_get_volume_response)
    mock_transport.side_effect = [introspection_result, volume_response_client]
    yield volume_response_client


@pytest.fixture
def volume_get_response_with_outputs(
    mock_transport,
    fake_get_volume_response,
    introspection_result,
    fake_client_type,
    fake_file_json,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for getVolume query with client.

    Args:
        fake_get_volume_response (dict[str, str]): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_client_type (dict[str, str]): Fake client type.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    fake_get_volume_response[GET_VOLUME_QUERY]["outputs"] = [
        {
            "format": "volume_definition",
            FILE_LITERAL: fake_file_json,
        },
        {
            "format": "volume_report",
            FILE_LITERAL: fake_file_json,
        },
    ]
    volume_response_outputs = ExecutionResult(data=fake_get_volume_response)
    mock_transport.side_effect = [introspection_result, volume_response_outputs]
    yield volume_response_outputs


@pytest.fixture
def volume_create_response_with_video_source(
    mock_transport,
    fake_create_volume_response,
    introspection_result,
    fake_file_json,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for createVolumeWithHuman mutation with video source.

    Args:
        fake_create_volume_response (FakeVolumeJson): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    yield build_response_with_video_source(
        fake_response=fake_create_volume_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=CREATE_HUMAN_VOLUME_MUTATION,
    )


@pytest.fixture
def volume_get_response_with_video_source(
    faker,
    mock_transport,
    fake_get_volume_response,
    introspection_result,
    fake_file_json,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for getVolume query with video source.

    Args:
        faker (Faker): Faker fixture.
        fake_get_volume_response (FakeVolumeJson): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    yield build_response_with_video_source(
        fake_response=fake_get_volume_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=GET_VOLUME_QUERY,
        camera_settings={
            "lens": faker.word(),
        },
    )


@pytest.fixture
def volume_create_res_with_additional_sources(
    mock_transport,
    fake_create_volume_response,
    introspection_result,
    fake_file_json,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for createVolumeWithHuman mutation with sources.

    Args:
        fake_create_volume_response (FakeVolumeJson): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    yield build_response_with_additional_sources(
        fake_response=fake_create_volume_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=CREATE_HUMAN_VOLUME_MUTATION,
    )


@pytest.fixture
def volume_get_res_with_additional_sources(
    faker,
    mock_transport,
    fake_get_volume_response,
    introspection_result,
    fake_file_json,
) -> FakeVolumeJson:
    """Fixture to return a fake volume response for getVolume query with sources.

    Args:
        faker (Faker): Faker fixture.
        fake_get_volume_response (FakeVolumeJson): Fake volume json.
        mock_transport (MockTransport): Mock transport.
        introspection_result (dict[str, str]): Introspection result.
        fake_file_json (dict[str, str]): Fake file json.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    yield build_response_with_additional_sources(
        fake_response=fake_get_volume_response.copy(),
        fake_file_json=fake_file_json,
        mock_transport=mock_transport,
        introspection_result=introspection_result,
        key=GET_VOLUME_QUERY,
        camera_settings={
            "lens": faker.word(),
        },
    )


@pytest.fixture
def fake_list_volume_response(fake_volume_json, faker) -> FakeVolumeJson:
    """Fixture to return a fake volume response for listVolumes query.

    Args:
        fake_volume_json (dict[str, str]): Fake volume json.
        faker (Faker): Faker instance.

    Returns:
        FakeVolumeJson: Fake volume response.
    """
    return {
        LIST_VOLUMES_QUERY: build_list_response(
            fake_response=fake_volume_json,
            faker=faker,
        ),
    }


@pytest.fixture
def volume_list_response(
    mock_transport,
    fake_list_volume_response,
    introspection_result,
):
    """Fixture to return a fake volume response for listVolumes query.

    Args:
        mock_transport (MockTransport): Mock transport.
        fake_list_volume_response (FakeVolumeJson): Fake volume json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        FakeVolumeJson: Fake volume response.
    """
    volume_response = ExecutionResult(data=fake_list_volume_response)
    mock_transport.side_effect = [introspection_result, volume_response]
    yield volume_response
