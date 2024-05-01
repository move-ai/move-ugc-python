"""Unit tests for using the client service."""
from tests.services.testcases import ServicesTestCase


class TestClientService(ServicesTestCase):
    """Test client service."""

    service_name = "client"

    def test_retrieve(
        self,
        snapshot,
        faker,
        client_retrieve_response,
    ):
        """Test retrieving a client from Move UGC API.

        This should test -> `ugc.client.retrieve()'`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            client_retrieve_response: The client response fixture.
        """
        client_model = self.client.client.retrieve()
        self.assert_execute(snapshot, name="retrieve_query")
        snapshot.assert_match(client_model.model_dump(), name="retrieve_response")

    def test_update(self, client_update_response, metadata_for_update, snapshot):
        """Test updating a client from Move UGC API.

        This should test -> `ugc.client.update(metadata={"foo": "bar"})'`

        Args:
            client_update_response: mocked client update response
            metadata_for_update: Metadata for update mutations
            snapshot: The snapshot fixture.
        """
        client_model = self.client.client.update(metadata=metadata_for_update)
        self.assert_execute(snapshot, name="update_query")
        snapshot.assert_match(client_model.model_dump(), name="update_response")
