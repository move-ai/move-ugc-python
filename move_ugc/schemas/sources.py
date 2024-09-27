"""Representation for Additional file type in Ugc API."""
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from move_ugc.schemas.file import FileType


class TakeSourceKey(str, Enum):  # noqa: WPS600
    """Choices for take source keys."""

    mp4 = "MP4"
    avi = "AVI"
    mov = "MOV"
    move = "MOVE"

    @classmethod
    def _missing_(cls, key_value: object) -> Optional[str]:  # noqa: WPS120
        """Return the value if it matches any of the members.

        This method makes the enum case-insensitive and always converts the values to upper case.

        Args:
            key_value: The value to be matched against the members.

        Returns:
            The value if it matches any of the members, None otherwise.
        """
        key_value = str(key_value).upper()
        for member in cls:
            if member.upper() == key_value:
                return member
        return None


class CameraSettings(BaseModel):
    """Camera settings input for creating a take.

    Find the list of available camera settings here:
    https://move-ai.github.io/move-ugc-api/getting-started/multicam/lenses/
    """

    lens: str = Field(
        description="Lens used for the take",
        title="Lens",
        examples=[
            "goprohero10-2-7k",
            "blackmagic-ea-4k-24mm",
            "sony-synced-fhd",
            "panasonic-lumix-dc-bgh1-4k-12mm",
            "optitrackprimecolor12mm-fhd",
        ],
    )


class ClipWindow(BaseModel):
    """Clip window for cropping a source."""

    start_time: float = Field(
        description="Start time of the clip window",
        title="Start time",
        examples=[0],
        serialization_alias="startTime",
    )
    end_time: float = Field(
        description="End time of the clip window",
        title="End time",
        examples=[10.0],
        serialization_alias="endTime",
    )


class AdditionalFileType(BaseModel):
    """Representation for Additional File type in MoveUGC."""

    key: str = Field(
        description="Identification key for the additional file",
        title="Additional file key",
        examples=["mp4", "depth", "odometry", "vision", "intrinsic"],
    )

    file: FileType = Field(  # noqa: WPS110 can't change the name due to GraphQL schema
        description="File associated with the additional file",
        title="Additional file",
        examples=[{"id": "file-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"}],
    )


class SourceIn(BaseModel, use_enum_values=True):
    """Source input required for creating a take."""

    device_label: str = Field(
        description="Label for the device",
        title="Device label",
        examples=["my-device"],
        serialization_alias="deviceLabel",
    )

    file_id: str = Field(
        description="File ID of the file associated with the source",
        title="File ID",
        examples=["file-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        serialization_alias="fileId",
    )

    format: TakeSourceKey = Field(
        description="Format of the source",
        title="Source format",
        examples=["MP4", "MOVE"],
    )

    camera_settings: Optional[CameraSettings] = Field(
        description="Camera settings used for the take",
        title="Camera settings",
        examples=[{"lens": "goprohero10-2-7k"}],
        serialization_alias="cameraSettings",
        default=None,
    )

    clip_window: Optional[ClipWindow] = Field(
        description="Clip window for cropping the source",
        title="Clip window",
        examples=[{"startTime": 0, "endTime": 10}],
        serialization_alias="clipWindow",
        default=None,
    )


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
        examples=[{"id": "file-1fd863d5-875b-4e48-89bb-c6234e804738"}],
        title="Source file",
    )
    format: str = Field(
        description="Format of the source",
        examples=["MP4"],
        title="Source format",
    )
    camera_settings: Optional[CameraSettings] = Field(
        description="Camera settings used for the take",
        title="Camera settings",
        examples=[{"lens": "goprohero10-2-7k"}],
        serialization_alias="cameraSettings",
        default=None,
    )
    clip_window: Optional[ClipWindow] = Field(
        description="Clip window for the source",
        title="Clip window",
        examples=[{"startTime": 0, "endTime": 10}],
        default=None,
    )
