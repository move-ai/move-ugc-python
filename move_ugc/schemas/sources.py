"""Representation for Additional file type in Ugc API."""

import warnings
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, computed_field

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


class AdditionalFileType(BaseModel):
    """Representation for Additional File type in MoveUGC."""

    format: str = Field(
        description="Identification format for the additional file",
        title="Additional file key",
        examples=["mp4", "depth", "odometry", "vision", "intrinsic"],
        default="",
    )
    file: FileType = Field(  # noqa: WPS110 can't change the name due to GraphQL schema
        description="File associated with the additional file",
        title="Additional file",
        examples=[{"id": "file-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"}],
    )

    # To be deprecated
    @computed_field  # type: ignore[misc]
    @property
    def key(self) -> str:
        """Return the key of the additional file.

        Returns:
            str: Key of the additional file.
        """
        warnings.warn(
            "`key` will be deprecated in an upcoming release. Use `format` instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.format


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
