"""Representation for Take type in Ugc API."""
from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, Json

from move_ugc.schemas.additional_file import AdditionalFileType
from move_ugc.schemas.client import Client
from move_ugc.schemas.file import FileType


class TakeType(BaseModel):
    """Representation for Take type in MoveUGC."""

    id: str = Field(
        description="Unique identifier for the file",
        examples=["file-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        title="File ID",
    )
    created: datetime = Field(
        description="Date and time when the file was created. This will be in UTC.",
        examples=["2021-08-04T15:00:00.000Z"],
        title="File creation date",
    )
    metadata: Json[Dict[str, str]] = Field(
        description="Metadata associated with the file",
        examples=[{"key": "value"}],
        title="File metadata",
    )
    client: Optional[Client] = Field(
        description="Client associated with the file",
        examples=[{"id": "client-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"}],
        title="File client",
        default=None,
    )
    video_file: Optional[FileType] = Field(
        description="Video file associated with the take",
        examples=[{"id": "file-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"}],
        title="Take video file",
        alias="videoFile",
        default=None,
    )
    additional_files: Optional[List[AdditionalFileType]] = Field(
        description="Optional additional files for the take",
        examples=[
            {
                "key": "depth",
                "file": {"id": "file-ee02c1b6-0328-4a7c-a2b2-76883acb451d"},
            },
        ],
        title="Take additional files",
        alias="additionalFiles",
        default=None,
    )
