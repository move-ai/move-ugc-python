"""Webhook mixin for the Move UGC SDK."""
from typing import List, Optional

from move_ugc.gql_requests.webhook_endpoint import add_webhook
from move_ugc.schemas.webhook_endpoint import WebhookEndpoint
from move_ugc.services.base import BaseService


class WebhookService(BaseService[WebhookEndpoint]):
    """Service which can be used to communicate with WebhookEndpoint type in UGC API.

    To use this service, you need to instantiate it with a valid Move UGC client.

    ```python
    from move_ugc import MoveUgc
    ugc = MoveUgc(api_key="my-api-key")

    events = ["ugc.jobs.operation.completed"]
    uid = "<unique-id-for-webhook>"
    url = "https://example.com/webhook"

    # Call webhook service methods directly
    webhook_endpoint = ugc.webhooks.upsert(events=events, uid=uid, url=url)
    ```
    """

    _schema = WebhookEndpoint

    def upsert(  # noqa: WPS211
        self,
        events: List[str],
        uid: str,
        url: str,
        description: Optional[str] = "",
        secret: Optional[str] = None,
    ) -> WebhookEndpoint:
        """Update or create a webhook endpoint to the client.

        Args:
            events (Any): Events to subscribe to.
            uid (str): Unique identifier for the webhook endpoint.
            url (str): URL of the webhook endpoint.
            description (str, optional): Description of the webhook endpoint. Defaults to "".
            secret (str, optional): Secret used to verify the webhook endpoint. Defaults to None.

        Returns:
            WebhookEndpoint instance of Pydantic model type.
        """
        return self.execute(
            query_key=add_webhook.key,
            gql_query=add_webhook.generate_query(),
            variable_values={
                "events": events,
                "uid": uid,
                "url": url,
                "description": description,
                "secret": secret,
            },
        )
