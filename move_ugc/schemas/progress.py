"""Details about the job progress."""
from pydantic import BaseModel, Field


class JobProgress(BaseModel):
    """Details about the job progress."""

    state: str
    percentage_complete: int = Field(
        serialization_alias="percentageComplete",
        description="Percentage of the job that has been completed.",
    )
