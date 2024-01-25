"""Common schemas to be used accross types."""
import enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from move_ugc.schemas.job import JobType
from move_ugc.schemas.take import TakeType
from move_ugc.settings import get_settings


def get_default_page_size() -> int:
    """Return the default for page size.

    Returns:
        int: Default page size.
    """
    return get_settings().default_page_size


class SortDirection(enum.Enum):
    """Enum for sort direction."""

    ASC = "ASC"  # noqa: WPS115
    DESC = "DESC"  # noqa: WPS115


class ListBase(BaseModel):
    """List base schema."""

    limit: int = Field(
        default_factory=get_default_page_size,
        description="Number of items to be returned.",
        alias="first",
    )
    next_token: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Cursor for the next page.",
        alias="after",
    )
    items: Union[List[TakeType], List[JobType]] = Field(  # noqa: WPS110
        default_factory=list,
        description="List of items. This can be either Job or Take.",
    )
    model_config = ConfigDict(populate_by_name=True, extra="allow")
