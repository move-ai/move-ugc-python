"""Unit tests for using the files service."""
import pytest
from gql.transport.exceptions import TransportQueryError

from tests.services.testcases import ServicesTestCase


class TestFileService(ServicesTestCase):
    """Test file service."""

    service_name = "files"

    @pytest.mark.parametrize(
        argnames="expand",
        argvalues=[None, [], ["client"]],
        ids=["no_expand", "empty_expand", "expand_client"],
    )
    def test_retrieve(self, expand, snapshot, faker, file_retrieve_response):
        """Test retrieving a file from Move UGC API.

        This should test -> `ugc.files.retrieve(id='files-<uuid>)'`

        Args:
            expand: The expand fixture.
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            file_retrieve_response: The file retrieve response fixture.
        """
        file_model = self.client.files.retrieve(id=faker.uuid4(), expand=expand)
        suffix = "_".join(expand or [])
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
