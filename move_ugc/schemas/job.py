"""Representation for Job type in Ugc API."""
from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, ConfigDict, Field, Json, alias_generators

from move_ugc.schemas.client import Client
from move_ugc.schemas.sources import AdditionalFileType
from move_ugc.schemas.take import TakeType


class JobOptions(BaseModel):
    """Options which can be used for creating a job in MoveUGC.

    This schema is used to represent the options which can be used for creating a job in MoveUGC.

    The options are validated at runtime by the MoveUGC API. So, if you don't see an option you want to use,
    please check the API documentation for the allowed options, and provide the key here accordingly as the key
    may be missing in this version of the sdk but is still allowed by this schema (as extra="allow").

    You can define the options as mentioned in the documentation or use snake case equivalent.
    For example:

    JobOptions(trackBall=True) can also be written as JobOptions(track_ball=True)

    Please find the allowed options in the API documentation.
    https://move-ai.github.io/move-ugc-api/schema/#optionsinput
    """

    model_config = ConfigDict(
        extra="allow",
        alias_generator=alias_generators.to_camel,
    )


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
    metadata: Json[Any] = Field(
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
    name: Optional[str] = Field(
        description="Name of the job",
        examples=["job 1"],
        title="Job name",
        default="",
    )
