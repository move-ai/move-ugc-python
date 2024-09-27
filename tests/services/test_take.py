"""Unit tests for using the take service."""
import json

import pytest
from gql.transport.exceptions import TransportQueryError

from move_ugc.schemas.constants import VOLUME_LITERAL
from move_ugc.schemas.sources import CameraSettings, SourceIn, TakeSourceKey
from move_ugc.schemas.sync_method import SyncMethodInput
from tests.services.testcases import ServicesTestCase

SOURCES_LITERAL = "sources"


class TestTakeService(ServicesTestCase):  # noqa: WPS214
    """Test take service."""

    service_name = "takes"

    @pytest.mark.parametrize(
        argnames="expand, take_fixture",
        argvalues=[
            (None, "take_create_response"),
            ([], "take_create_response"),
            (["client"], "take_create_response_with_client"),
            ([SOURCES_LITERAL], "take_create_response_with_video_source"),
            ([SOURCES_LITERAL], "take_create_response_with_additional_sources"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_video_file",
            "expand_additional_sources",
        ],
    )
    def test_create(  # noqa: WPS211
        self,
        snapshot,
        faker,
        request,
        expand,
        take_fixture,
    ):
        """Test creating a take.

        This should test -> `ugc.takes.create_singlecam()`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            request: The request fixture.
            expand: The expand fixture.
            take_fixture: The take fixture.
        """
        request.getfixturevalue(take_fixture)
        device_label = faker.word()
        take_model = self.client.takes.create_singlecam(
            metadata=request.getfixturevalue("metadata_for_update"),
            sources=[
                SourceIn(
                    device_label=device_label,
                    file_id=faker.uuid4(),
                    format=TakeSourceKey.mp4,
                ),
                SourceIn(
                    device_label=device_label,
                    file_id=faker.uuid4(),
                    format=TakeSourceKey.move,
                ),
            ],
            name=faker.word(),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"create_mutation_expand_{suffix}",
        )
        snapshot.assert_match(
            take_model.model_dump(),
            name=f"create_response_expand_{suffix}",
        )

    @pytest.mark.parametrize(
        argnames="expand, take_fixture",
        argvalues=[
            (None, "take_create_multicam_response"),
            ([], "take_create_multicam_response"),
            (["client"], "take_create_multicam_response_with_client"),
            ([SOURCES_LITERAL], "take_create_mc_response_with_video_source"),
            ([SOURCES_LITERAL], "take_create_mc_response_w_additional_sources"),
            ([VOLUME_LITERAL], "take_create_mc_response_with_volume"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_video_file",
            "expand_additional_sources",
            "expand_volume",
        ],
    )
    def test_create_multicam(  # noqa: WPS211
        self,
        snapshot,
        faker,
        request,
        expand,
        take_fixture,
    ):
        """Test creating a take.

        This should test -> `ugc.takes.create_multicam()`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            request: The request fixture.
            expand: The expand fixture.
            take_fixture: The take fixture.
        """
        request.getfixturevalue(take_fixture)
        device_label = faker.word()
        take_model = self.client.takes.create_multicam(
            metadata=request.getfixturevalue("metadata_for_update"),
            sources=[
                SourceIn(
                    device_label=device_label,
                    file_id=faker.uuid4(),
                    format=TakeSourceKey.mp4,
                    camera_settings=CameraSettings(
                        lens=faker.word(),
                    ),
                ),
                SourceIn(
                    device_label=device_label,
                    file_id=faker.uuid4(),
                    format=TakeSourceKey.move,
                    camera_settings=CameraSettings(
                        lens=faker.word(),
                    ),
                ),
            ],
            sync_method=SyncMethodInput(
                timecode_sync={
                    "use_timecode": faker.pybool(),
                },
            ),
            volume_id=f"volume-{faker.uuid4()}",
            name=faker.word(),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"create_mutation_expand_{suffix}",
        )
        snapshot.assert_match(
            take_model.model_dump(mode="json"),
            name=f"create_response_expand_{suffix}",
        )

    @pytest.mark.parametrize(
        argnames="expand, take_fixture",
        argvalues=[
            (None, "take_update_response"),
            ([], "take_update_response"),
            (["client"], "take_update_response_with_client"),
            ([SOURCES_LITERAL], "take_update_response_with_video_source"),
            ([SOURCES_LITERAL], "take_update_response_with_additional_sources"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_video_file",
            "expand_additional_files",
        ],
    )
    def test_update(  # noqa: WPS211
        self,
        snapshot,
        faker,
        request,
        expand,
        take_fixture,
    ):
        """Test creating a take.

        This should test -> `ugc.takes.create_singlecam()`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            request: The request fixture.
            expand: The expand fixture.
            take_fixture: The take fixture.
        """
        request.getfixturevalue(take_fixture)
        take_model = self.client.takes.update(
            id=faker.uuid4(),
            metadata=request.getfixturevalue("metadata_for_update"),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"update_mutation_expand_{suffix}",
        )
        snapshot.assert_match(
            take_model.model_dump(),
            name=f"update_response_expand_{suffix}",
        )

    def test_create_wrong_additional_file_key(self, faker):
        """Test creating a take with wrong additional file key.

        This should test -> `ugc.takes.create_singlecam()`

        Args:
            faker: The faker fixture.
        """
        with pytest.raises(ValueError):
            self.client.takes.create_singlecam(
                sources=[
                    SourceIn(
                        device_label=faker.word(),
                        file_id=faker.uuid4(),
                        format=TakeSourceKey.mp4,
                    ),
                    SourceIn(
                        device_label=faker.word(),
                        file_id=faker.uuid4(),
                        format=faker.word(),
                    ),
                ],
                metadata=json.dumps({}),
            )

    def test_create_lower_additional_file_key(
        self,
        faker,
        take_create_response,
        snapshot,
    ):
        """Test creating a take with a lower case additional file key.

        This should test -> `ugc.takes.create_singlecam()`

        Args:
            faker: The faker fixture.
            take_create_response: The take_create_response fixture.
            snapshot: The snapshot fixture.
        """
        take_model = self.client.takes.create_singlecam(
            metadata=json.dumps({}),
            sources=[
                SourceIn(
                    device_label=faker.word(),
                    file_id=faker.uuid4(),
                    format=TakeSourceKey.mp4,
                ),
                SourceIn(
                    device_label=faker.word(),
                    file_id=faker.uuid4(),
                    format="move",
                ),
            ],
        )
        self.assert_execute(
            snapshot,
            name="create_mutation_lower_additional_file_key",
        )
        snapshot.assert_match(
            take_model.model_dump(),
            name="create_response_lower_additional_file_key",
        )

    @pytest.mark.parametrize(
        argnames="expand, take_fixture",
        argvalues=[
            (None, "take_retrieve_response"),
            ([], "take_retrieve_response"),
            (["client"], "take_retrieve_response_with_client"),
            ([SOURCES_LITERAL], "take_retrieve_response_with_video_source"),
            ([SOURCES_LITERAL], "take_retrieve_response_with_additional_sources"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_video_file",
            "expand_additional_files",
        ],
    )
    def test_retrieve(  # noqa: WPS211
        self,
        snapshot,
        faker,
        request,
        expand,
        take_fixture,
    ):
        """Test retrieving a take.

        This should test -> `ugc.takes.retrieve()`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            request: The request fixture.
            expand: The expand fixture.
            take_fixture: The take fixture.
        """
        request.getfixturevalue(take_fixture)
        take_model = self.client.takes.retrieve(id=faker.uuid4(), expand=expand)
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"retrieve_request_expand_{suffix}",
        )
        snapshot.assert_match(
            take_model.model_dump(),
            name=f"retrieve_response_expand_{suffix}",
        )

    def test_take_not_found(self, snapshot, faker, take_not_found_response):
        """Test take not found.

        This should test -> `ugc.takes.retrieve(id='invalid-id')'`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            take_not_found_response: take not found response fixture.
        """
        with pytest.raises(TransportQueryError) as excinfo:
            self.client.takes.retrieve(id=faker.uuid4())
        snapshot.assert_match(
            excinfo.value.errors,  # noqa: WPS441
            name="take_not_found_response",
        )

    def test_list(self, snapshot, takes_list_response):
        """Test listing takes.

        This should test -> `ugc.takes.list()`

        Args:
            snapshot: The snapshot fixture.
            takes_list_response: take list response fixture.
        """
        take_list = self.client.takes.list()
        self.assert_execute(snapshot, name="take_list_request")
        snapshot.assert_match(
            take_list.model_dump(),
            name="list_response",
        )
