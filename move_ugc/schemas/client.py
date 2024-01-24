"""Client representation in pydantic schema."""
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, HttpUrl, Json


class Client(BaseModel):
    """Client representation in pydantic schema."""

    id: str = Field(
        description="Unique identifier for the client",
        examples=["client-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        title="Client ID",
    )
    name: str = Field(
        description="Client name associated at the time of creation",
        examples=["MyAwesomeCompany"],
        title="Client name",
    )
    created: datetime = Field(
        description="Date and time when the file was created. This will be in UTC.",
        examples=["2021-08-04T15:00:00.000Z"],
        title="Client creation date",
    )
    metadata: Json[Any] = Field(
        description="Metadata associated with the client",
        examples=[{"key": "value"}],
        title="Client metadata",
    )
    portal: HttpUrl = Field(
        description="Portal url associated to this client.",
        examples=["https://portal.move-sandbox.com"],
        title="Portal URL",
    )
