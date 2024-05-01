"""Representation for Webhook endpoint type in Ugc API."""
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl, SecretStr


class WebhookEndpoint(BaseModel):
    """Representation for Webhook endpoint type in MoveUGC."""

    description: str = Field(
        description="Description of the webhook endpoint.",
        examples=["My webhook endpoint"],
        title="Description",
    )
    events: List[str] = Field(
        description="List of events that the webhook endpoint is subscribed to.",
        examples=[["ugc.job.operation.completed"]],
        title="Events",
    )
    secret: Optional[SecretStr] = Field(
        description="Secret used to verify the webhook endpoint.",
        title="Secret",
        default=None,
    )
    uid: str = Field(
        description="Unique identifier for the webhook endpoint.",
        examples=["webhook-endpoint-0aa9ba14-44f9-4d47-89b4-c77cdea9e801"],
        title="Webhook endpoint ID",
    )
    url: HttpUrl = Field(
        description="URL of the webhook endpoint.",
        examples=["https://example.com/webhook"],
        title="URL",
    )
