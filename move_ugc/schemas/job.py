"""Representation for Job type in Ugc API."""
from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, Json

from move_ugc.schemas.additional_file import AdditionalFileType
from move_ugc.schemas.client import Client
from move_ugc.schemas.take import TakeType


class JobType(BaseModel):
    """Representation for Job type in MoveUGC."""

    id: str = Field(
        description="Unique identifier for the job",
        examples=["job-2c6059be-0f91-4cb8-aa1a-512cd10a66b5"],
        title="Job ID",
    )
    created: datetime = Field(
        description="Date and time when the job was created. This will be in UTC.",
        examples=["2021-08-04T15:00:00.000Z"],
        title="Job creation date",
    )
    metadata: Json[Dict[str, str]] = Field(
        description="Metadata associated with the job",
        examples=[{"key": "value"}],
        title="Job metadata",
    )
    client: Optional[Client] = Field(
        description="Client associated with the job",
        examples=[{"id": "client-ff07d226-4ecb-49b4-8aed-0bd35cd50eeb"}],
        title="Job client",
        default=None,
    )
    outputs: Optional[List[AdditionalFileType]] = Field(
        description="Outputs for the job. This usually contains the fbx, mp4 output files when the state is `FINISHED`",
        examples=[
            {
                "key": "fbx",
                "file": {"id": "file-ee02c1b6-0328-4a7c-a2b2-76883acb451d"},
            },
        ],
        title="Job outputs",
        default=None,
    )
    state: str = Field(
        description="State of the job",
        examples=["FINISHED", "NOT STARTED", "RUNNING", "FAILED"],
        title="Job state",
    )
    take: Optional[TakeType] = Field(
        description="Take associated with the job",
        examples=[{"id": "take-4003a524-7819-4537-ac82-8a3ac2635db9"}],
        title="Job take",
        default=None,
    )
