"""Representation for Additional file type in Ugc API."""
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from move_ugc.schemas.file import FileType


class TakeAdditionalFileKeys(str, Enum):  # noqa: WPS600
    """Choices for take additional file keys."""

    depth = "DEPTH"
    odometry = "ODOMETRY"
    vision = "VISION"
    intrinsic = "INTRINSIC"
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


class AdditionalFileIn(BaseModel, use_enum_values=True):
    """Additional file input required for creating a take."""

    key: TakeAdditionalFileKeys = Field(
        description="Identification key for the additional file",
        title="Additional file key",
        examples=["depth", "odometry", "vision", "intrinsic"],
    )

    file_id: str = Field(
        description="File ID of the file to be associated with the additional file",
        title="File ID",
        examples=["file-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        serialization_alias="fileId",
    )
