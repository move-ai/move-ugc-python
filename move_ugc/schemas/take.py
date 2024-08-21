"""Representation for Take type in Ugc API."""
from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field, Json

from move_ugc.schemas.client import Client
from move_ugc.schemas.file import FileType

ID_LITERAL = "id"


class Source(BaseModel):
    """Representation for Source type in MoveUGC."""

    device_label: str = Field(
        description="Label for the device",
        examples=["my-device"],
        title="Device label",
        alias="deviceLabel",
    )
    file: FileType = Field(  # noqa: WPS110
        description="File associated with the source",
        examples=[{ID_LITERAL: "file-1fd863d5-875b-4e48-89bb-c6234e804738"}],
        title="Source file",
    )
    format: str = Field(
        description="Format of the source",
        examples=["MP4"],
        title="Source format",
    )


class TakeType(BaseModel):
    """Representation for Take type in MoveUGC."""

    id: str = Field(
        description="Unique identifier for the take",
        examples=["take-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        title="Take ID",
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
