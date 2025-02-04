"""Rig representation in pydantic schema."""

from pydantic import BaseModel, Field


class Rig(BaseModel):
    """Rig representation in pydantic schema."""

    name: str = Field(
        description="Name of the rig",
        examples=["move_mo"],
        title="Rig name",
    )
