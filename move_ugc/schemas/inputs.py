"""Schemas for input structure."""
from pydantic import BaseModel, Field


class ClipWindowInputType(BaseModel):
    """Representation of the input type for clip windows when returned to the user."""

    start_time: float = Field(alias="endTime")
    end_time: float = Field(alias="endTime")
