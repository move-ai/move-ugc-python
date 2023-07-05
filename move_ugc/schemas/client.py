"""Client representation in pydantic schema."""
from pydantic import BaseModel


class Client(BaseModel):
    """Client representation in pydantic schema."""

    id: str
    name: str
    created: str
