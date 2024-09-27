"""Schemas to represent a SyncMethod entity in UGC API."""
from typing import Optional

from pydantic import BaseModel, Field


class ClapWindowInput(BaseModel):
    """ClapWindowInput schema for UGC API."""

    start_time: float = Field(
        description="Start time of the clap window.",
        examples=[0, 1.0],
        serialization_alias="startTime",
    )
    end_time: float = Field(
        description="End time of the clap window.",
        examples=[0, 1.0],
        serialization_alias="endTime",
    )


class TimecodeSyncInput(BaseModel):
    """TimecodeSyncInput schema for UGC API."""

    use_timecode: bool = Field(
        description="Flag to indicate if timecode sync is used.",
        examples=[True, False],
        serialization_alias="useTimecode",
    )


class SyncMethodInput(BaseModel):
    """SyncMethodInput schema for UGC API."""

    clap_window: Optional[ClapWindowInput] = Field(
        serialization_alias="clapWindow",
        default=None,
    )
    timecode_sync: Optional[TimecodeSyncInput] = Field(
        serialization_alias="timecodeSync",
        default=None,
    )
