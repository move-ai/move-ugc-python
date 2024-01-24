"""Unit tests for using the files service."""
import pytest
from gql.transport.exceptions import TransportQueryError

from tests.services.testcases import ServicesTestCase


class TestFileService(ServicesTestCase):
    """Test file service."""

    service_name = "files"

    @pytest.mark.parametrize(
        argnames="expand, file_fixture",
        argvalues=[
            (None, "file_retrieve_response"),
            ([], "file_retrieve_response"),
            (["client"], "file_retrieve_response_with_client"),
        ],
        ids=["no_expand", "empty_expand", "expand_client"],
    )
    def test_retrieve(  # noqa: WPS211
        self,
        expand,
        snapshot,
        faker,
        request,
        file_fixture,
    ):
        """Test retrieving a file from Move UGC API.

        This should test -> `ugc.files.retrieve(id='files-<uuid>, expand=[<fixture>])'`

        Args:
            expand: The expand fixture.
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            request: The request fixture.
            file_fixture: The file fixture.
        """
        request.getfixturevalue(file_fixture)
        file_model = self.client.files.retrieve(id=faker.uuid4(), expand=expand)
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"retrieve_query_expand_{suffix}",
        )
        snapshot.assert_match(
            file_model.model_dump(),
            name=f"file_retrieve_response_expand_{suffix}",
        )

    def test_file_not_found(self, snapshot, faker, file_not_found_response):
        """Test file not found.

        This should test -> `ugc.files.retrieve(id='invalid-id')'`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            file_not_found_response: The file not found response fixture.
        """
        with pytest.raises(TransportQueryError) as excinfo:
            self.client.files.retrieve(id=faker.uuid4(), expand=["client"])
        snapshot.assert_match(
            excinfo.value.errors,  # noqa: WPS441
            name="file_not_found_response",
        )

    @pytest.mark.parametrize(
        argnames="expand, file_fixture",
        argvalues=[
            (None, "file_create_response"),
            ([], "file_create_response"),
            (["client"], "file_create_response_with_client"),
        ],
        ids=["no_expand", "empty_expand", "expand_client"],
    )
    def test_create(  # noqa: WPS211
        self,
        expand,
        snapshot,
        faker,
        request,
        file_fixture,
    ):
        """Test creating a file from Move UGC API.

        This should test -> `ugc.files.create(id='files-<uuid>, expand=[<fixture>])'`

        Args:
            expand: The expand fixture.
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            request: The request fixture.
            file_fixture: The file fixture.
        """
        request.getfixturevalue(file_fixture)
        file_model = self.client.files.create(
            file_type=faker.file_extension(),
            metadata=request.getfixturevalue("metadata_for_update"),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"create_mutation_expand_{suffix}",
        )
        snapshot.assert_match(
            file_model.model_dump(),
            name=f"create_mutation_response_expand_{suffix}",
        )
