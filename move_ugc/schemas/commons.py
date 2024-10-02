"""Common schemas to be used across types."""
import enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, Json
from typing_extensions import Annotated

from move_ugc.schemas.job import JobType
from move_ugc.schemas.take import TakeType
from move_ugc.settings import get_settings

LIST_ITEM_TYPE = List[Dict[str, Any]]
DICT_AS_JSON_STRING_TYPE = Json[Dict[str, Any]]


def validate_list_items_type(
    list_items: LIST_ITEM_TYPE,
) -> Union[List[JobType], List[TakeType], LIST_ITEM_TYPE]:
    """Validate list items type.

    Args:
        list_items (LIST_ITEM_TYPE): List items.

    Returns:
        List items.

    Raises:
        ValueError: If list items type is invalid.
    """
    if list_items:
        if str(list_items[0]["id"]).startswith("job"):
            return [JobType(**list_item) for list_item in list_items]
        elif str(list_items[0]["id"]).startswith("take"):
            return [TakeType(**list_item) for list_item in list_items]
        raise ValueError("Invalid list items type.")
    # In case the validator could not decide which type is being used,
    #  pass the data to pydantic to do its inner validations.
    return list_items


ListItem = Annotated[
    Union[List[JobType], List[TakeType]],
    BeforeValidator(validate_list_items_type),
]


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
    next_token: Optional[DICT_AS_JSON_STRING_TYPE] = Field(
        default=None,
        description="Cursor for the next page.",
        alias="after",
    )
    items: ListItem = Field(  # noqa: WPS110
        default_factory=list,
        description="List of items. This can be either list of JobType or TakeType.",
    )
    model_config = ConfigDict(populate_by_name=True, extra="allow")
