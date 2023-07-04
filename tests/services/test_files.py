"""Unit tests for using the files service."""
import pytest
from gql.transport.exceptions import TransportQueryError

from tests.services.testcases import ServicesTestCase


class TestFileService(ServicesTestCase):
    """Test file service."""

    service_name = "files"

    def test_retrieve(self, snapshot, faker, file_retrieve_response):
        """Test creating a file.

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            file_retrieve_response: The file retrieve response fixture.
        """
        file_model = self.client.files.retrieve(id=faker.uuid4())
        self.assert_execute(snapshot, name="retrieve_query")
        snapshot.assert_match(file_model.model_dump(), name="retrieve_response")

    def test_retrieve_with_client(
        self,
        snapshot,
        faker,
        file_retrieve_response_with_client,
    ):
        """Test creating a file.

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            file_retrieve_response_with_client: The file retrieve response with client fixture.
        """
        file_model = self.client.files.retrieve(id=faker.uuid4(), expand=["client"])
        self.assert_execute(snapshot, name="retrieve_query_with_client")
        snapshot.assert_match(
            file_model.model_dump(),
            name="retrieve_response_with_client",
        )

    def test_file_not_found(self, snapshot, faker, file_not_found_response):
        """Test file not found.

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
