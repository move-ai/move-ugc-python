"""Representation for File type in Ugc API."""
from datetime import datetime
from typing import Any, Optional

from pydantic import AliasPath, BaseModel, Field, HttpUrl, Json

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
    metadata: Json[Any] = Field(
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
    thumbnail_url: Optional[HttpUrl] = Field(
        description="Presigned URL for the thumbnail file. Only generated for source files.",
        examples=[
            "https://s3.amazonaws.com/bucket/file.mp4?AWSAccessKeyId=123&Expires=123&Signature=123",
        ],
        title="Thumbnail file presigned URL",
        alias="thumbnailUrl",
        default="",
    )
    name: str = Field(
        description="Name of the file",
        examples=["My file"],
        title="File name",
        default="",
    )


class ShareCode(BaseModel):
    """Represents a share code associated a File in UGC API."""

    code: str = Field(
        description="Share code value for the associated file.",
        example=["123456"],
        title="Share code",
    )
    created: datetime = Field(
        description="Date and time when the share code was created. This will be in UTC.",
        examples=["2021-08-04T15:00:00.000Z"],
        title="Share code creation date",
    )
    expires: datetime = Field(
        description="Date and time when the share code expires. This will be in UTC.",
        examples=["2021-08-04T15:00:00.000Z"],
        title="Share code expiry date",
    )
    file_id: str = Field(
        description="The file id to which the share code is associated.",
        examples=["file-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        title="File ID",
        validation_alias=AliasPath("file", "id"),
    )
    url: HttpUrl = Field(
        description="Presigned URL for the file",
        examples=[
            "https://api.move.ai/ugc/file/download?code=<code>",
        ],
        title="Share code redeem url.",
    )
