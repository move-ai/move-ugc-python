"""Representation for Volume types in Ugc API."""
from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field, Json

from move_ugc.schemas.client import Client
from move_ugc.schemas.sources import Source

ID_LITERAL = "id"


class AreaType(str, Enum):  # noqa: WPS600
    """Area type of the volume."""

    NORMAL = "NORMAL"  # noqa: WPS115
    LARGE = "LARGE"  # noqa: WPS115


class HumanVolumeType(BaseModel):
    """Representation for HumanVolume type in MoveUGC."""

    id: str = Field(
        description="Unique identifier for the volume",
        examples=["volume-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        title="Volume ID",
    )
    name: str = Field(
        description="Name of the volume",
        examples=["My volume"],
        title="Volume name",
    )
    area_type: AreaType = Field(
        description="Area type of the volume.",
        examples=["NORMAL", "LARGE"],
        title="Area type",
        alias="areaType",
    )
    human_height: float = Field(
        description="Height of the human in metres",
        examples=[1.75],
        title="Human height in metres",
        alias="humanHeight",
    )
    created: datetime = Field(
        description="Date and time when the volume was created. This will be in UTC.",
        examples=["2021-08-04T15:00:00.000Z"],
        title="Volume creation date",
    )
    metadata: Json[Any] = Field(
        description="Metadata associated with the volume",
        examples=[{"key": "value"}],
        title="Volume metadata",
    )
    client: Optional[Client] = Field(
        description="Client associated with the volume",
        examples=[{ID_LITERAL: "client-0aa9ba14-44f9-4d47-89b4-c77cdea9e801"}],
        title="Volume client",
        default=None,
    )
    sources: Optional[List[Source]] = Field(
        description="Sources associated with the volume",
        examples=[
            {
                "deviceLabel": "my-device-1",
                "file": {ID_LITERAL: "file-1fd863d5-875b-4e48-89bb-c6234e804738"},
                "format": "MP4",
            },
            {
                "deviceLabel": "my-device-2",
                "file": {ID_LITERAL: "file-1fd863d5-875b-4e48-89bb-c6234e804738"},
                "format": "MOVE",
            },
        ],
        title="Volume sources",
        default=None,
    )
    state: str = Field(
        description="State of the volume processing.",
        examples=["FINISHED", "NOT STARTED", "RUNNING", "FAILED"],
        title="Volume state",
    )
