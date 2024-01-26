"""Unit tests for using the webhook service."""
from tests.services.testcases import ServicesTestCase


class TestWebhooksService(ServicesTestCase):
    """Test webhook service."""

    service_name = "webhooks"

    def test_add_webhook(self, faker, upsert_webhook_endpoint_response, snapshot):
        """Test adding a webhook endpoint to Move UGC API.

        Args:
            faker: The faker fixture.
            upsert_webhook_endpoint_response: mocked webhook endpoint response
            snapshot: The snapshot fixture.
        """
        webhook_model = self.client.webhooks.add(
            events=["ugc.jobs.state.completed"],
            uid=faker.pystr(),
            url=faker.url(),
            secret=faker.pystr(),
            description=faker.pystr(),
        )
        self.assert_execute(snapshot, name="add_webhook_query")
        snapshot.assert_match(webhook_model.model_dump(), name="add_webhook_response")

    def test_add_without_secret(
        self,
        faker,
        upsert_webhook_endpoint_response,
        snapshot,
    ):
        """Test adding a webhook endpoint to Move UGC API without pre-defined secret.

        Args:
            faker: The faker fixture.
            upsert_webhook_endpoint_response: mocked webhook endpoint response
            snapshot: The snapshot fixture.
        """
        webhook_model = self.client.webhooks.add(
            events=["ugc.jobs.state.completed"],
            uid=faker.pystr(),
            url=faker.url(),
        )
        self.assert_execute(snapshot, name="add_webhook_query")
        snapshot.assert_match(webhook_model.model_dump(), name="add_webhook_response")
