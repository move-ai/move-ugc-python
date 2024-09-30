"""Representation for Take type in Ugc API."""
from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field, Json

from move_ugc.schemas.client import Client
from move_ugc.schemas.sources import Source
from move_ugc.schemas.volume import HumanVolumeType

ID_LITERAL = "id"


class TakeType(BaseModel):
    """Representation for Take type in MoveUGC."""

    id: str = Field(
        description="Unique identifier for the take",
        examples=["take-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        title="Take ID",
    )
    name: Optional[str] = Field(
        description="Name of the take",
        examples=["My take"],
        title="Take name",
        default="",
    )
    created: datetime = Field(
        description="Date and time when the take was created. This will be in UTC.",
        examples=["2021-08-04T15:00:00.000Z"],
        title="Take creation date",
    )
    metadata: Json[Any] = Field(
        description="Metadata associated with the take",
        examples=[{"key": "value"}],
        title="Take metadata",
    )
    client: Optional[Client] = Field(
        description="Client associated with the take",
        examples=[{ID_LITERAL: "client-0aa9ba14-44f9-4d47-89b4-c77cdea9e801"}],
        title="Take client",
        default=None,
    )
    sources: Optional[List[Source]] = Field(
        description="Sources associated with the take",
        examples=[
            {
                "deviceLabel": "my-device",
                "file": {ID_LITERAL: "file-1fd863d5-875b-4e48-89bb-c6234e804738"},
                "format": "MP4",
            },
            {
                "deviceLabel": "my-device",
                "file": {ID_LITERAL: "file-1fd863d5-875b-4e48-89bb-c6234e804738"},
                "format": "MOVE",
            },
        ],
        title="Take sources",
        alias="sources",
        default=None,
    )
    volume: Optional[HumanVolumeType] = Field(
        description="Volume associated with the take",
        examples=[{"id": "volume-4003a524-7819-4537-ac82-8a3ac2635db9"}],
        title="Take volume",
        default=None,
    )
