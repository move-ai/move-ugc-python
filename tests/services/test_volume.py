"""Unit tests for using the volume service."""

import pytest
from graphql import ExecutionResult
from pydantic import ValidationError

from move_ugc.schemas.constants import OUTPUTS_LITERAL
from move_ugc.schemas.job import ClipWindow
from move_ugc.schemas.sources import SourceIn, TakeSourceKey
from move_ugc.schemas.volume import AreaType
from tests.constants import LIST_VOLUMES_QUERY
from tests.services.testcases import ServicesTestCase

SOURCES_LITERAL = "sources"


class TestVolumeService(ServicesTestCase):
    """Test volume service."""

    service_name = "volumes"

    @pytest.mark.parametrize(
        argnames="expand, take_fixture",
        argvalues=[
            (None, "volume_create_response"),
            ([], "volume_create_response"),
            (["client"], "volume_create_response_with_client"),
            ([SOURCES_LITERAL], "volume_create_response_with_video_source"),
            ([SOURCES_LITERAL], "volume_create_res_with_additional_sources"),
            (["clipWindow"], "volume_create_response_with_clip_window"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_video_file",
            "expand_additional_sources",
            "expand_clip_window",
        ],
    )
    def test_create(  # noqa: WPS211
        self,
        snapshot,
        snapshot_json,
        faker,
        request,
        expand,
        take_fixture,
    ):
        """Test creating a take.

        This should test -> `ugc.volumes.create_human_volume()`

        Args:
            snapshot: The snapshot fixture.
            snapshot_json: The snapshot json fixture.
            faker: The faker fixture.
            request: The request fixture.
            expand: The expand fixture.
            take_fixture: The take fixture.
        """
        request.getfixturevalue(take_fixture)
        device_label = faker.word()
        volume = self.client.volumes.create_human_volume(
            metadata=request.getfixturevalue("metadata_for_update"),
            clip_window=ClipWindow(
                start_time=faker.pyint(),
                end_time=faker.pyint(),
            ),
            sources=[
                SourceIn(
                    device_label=device_label,
                    file_id=faker.uuid4(),
                    format=TakeSourceKey.mp4,
                    camera_settings={
                        "lens": faker.word(),
                    },
                ),
                SourceIn(
                    device_label=device_label,
                    file_id=faker.uuid4(),
                    format=TakeSourceKey.move,
                    camera_settings={
                        "lens": faker.word(),
                    },
                ),
            ],
            human_height=faker.pyfloat(positive=True),
            area_type=faker.enum(AreaType),
            name=faker.word(),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"create_mutation_expand_{suffix}",
        )
        assert volume.model_dump(mode="json") == snapshot_json(
            name=f"create_response_expand_{suffix}",
        )

    @pytest.mark.parametrize(
        argnames="expand, take_fixture",
        argvalues=[
            (None, "volume_get_response"),
            ([], "volume_get_response"),
            (["client"], "volume_get_response_with_client"),
            ([OUTPUTS_LITERAL], "volume_get_response_with_outputs"),
            ([SOURCES_LITERAL], "volume_get_response_with_video_source"),
            ([SOURCES_LITERAL], "volume_get_res_with_additional_sources"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_outputs",
            "expand_video_file",
            "expand_additional_sources",
        ],
    )
    def test_retrieve(  # noqa: WPS211
        self,
        snapshot,
        snapshot_json,
        faker,
        request,
        expand,
        take_fixture,
    ):
        """Test creating a take.

        This should test -> `ugc.volumes.create_human_volume()`

        Args:
            snapshot: The snapshot fixture.
            snapshot_json: The snapshot json fixture.
            faker: The faker fixture.
            request: The request fixture.
            expand: The expand fixture.
            take_fixture: The take fixture.
        """
        request.getfixturevalue(take_fixture)
        volume = self.client.volumes.retrieve_human_volume(
            id=f"volume-{faker.uuid4()}",
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"get_query_expand_{suffix}",
        )
        assert volume.model_dump(mode="json") == snapshot_json(
            name=f"get_response_expand_{suffix}",
        )

    def test_list(self, snapshot, snapshot_json, volume_list_response):
        """Test listing volumes.

        This should test -> `ugc.volumes.list()`

        Args:
            snapshot: The snapshot fixture.
            snapshot_json: The snapshot json fixture.
            volume_list_response: volume list response fixture.
        """
        volume_list = self.client.volumes.list()
        self.assert_execute(snapshot, name="volume_list_request")
        assert volume_list.model_dump(mode="json") == snapshot_json(
            name="list_response",
        )

    def test_list_volume_invalid(self, request):
        """Test volume errors.

        This should test -> `ugc.volumes.list()`

        Args:
            request: The request fixture.
        """
        mock_transport = request.getfixturevalue("mock_transport")
        fake_list_volume_response = request.getfixturevalue("fake_list_volume_response")
        introspection_result = request.getfixturevalue("introspection_result")

        fake_list_volume_response[LIST_VOLUMES_QUERY]["items"] = [
            {"id": "dummy-123-123-123-123"},
        ]

        volume_response = ExecutionResult(data=fake_list_volume_response)
        mock_transport.side_effect = [introspection_result, volume_response]

        with pytest.raises(ValidationError) as excinfo:
            self.client.volumes.list()

    def test_list_volume_empty(self, request):
        """Test volume when it has an empty response.

        This should test -> `ugc.volumes.list()`

        Args:
            request: The request fixture.
        """
        mock_transport = request.getfixturevalue("mock_transport")
        fake_list_volume_response = request.getfixturevalue("fake_list_volume_response")
        introspection_result = request.getfixturevalue("introspection_result")

        fake_list_volume_response[LIST_VOLUMES_QUERY]["items"] = []

        volume_response = ExecutionResult(data=fake_list_volume_response)
        mock_transport.side_effect = [introspection_result, volume_response]

        assert not self.client.volumes.list().items
