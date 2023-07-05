"""Representation for File type in Ugc API."""
from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel, Field, HttpUrl, Json

from move_ugc.schemas.client import Client


class FileType(BaseModel):
    """Representation for File type in MoveUGC."""

    id: str = Field(
        description="Unique identifier for the file",
        examples=["file-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        title="File ID",
    )
    type: str = Field(
        description="Type of the file",
        examples=["mp4", "avi", "mov"],
        title="File type",
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
    presigned_url: HttpUrl = Field(
        description="Presigned URL for the file",
        examples=[
            "https://s3.amazonaws.com/bucket/file.mp4?AWSAccessKeyId=123&Expires=123&Signature=123",
        ],
        title="File presigned URL",
        alias="presignedUrl",
    )
