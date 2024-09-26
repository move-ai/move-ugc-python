"""Unit tests for using the volume service."""
import pytest

from move_ugc.schemas.sources import SourceIn, TakeSourceKey
from move_ugc.schemas.volume import AreaType
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

        This should test -> `ugc.volumes.create_human_volume()`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            request: The request fixture.
            expand: The expand fixture.
            take_fixture: The take fixture.
        """
        request.getfixturevalue(take_fixture)
        device_label = faker.word()
        volume = self.client.volumes.create_human_volume(
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
        snapshot.assert_match(
            volume.model_dump(mode="json"),
            name=f"create_response_expand_{suffix}",
        )
