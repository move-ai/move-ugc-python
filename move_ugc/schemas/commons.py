"""Common schemas to be used across types."""

import enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, Json
from typing_extensions import Annotated

from move_ugc.schemas.job import JobType
from move_ugc.schemas.sources import CameraSettings
from move_ugc.schemas.take import TakeType
from move_ugc.schemas.volume import HumanVolumeType
from move_ugc.settings import get_settings

LIST_ITEM_TYPE = List[Dict[str, Any]]
DICT_AS_JSON_STRING_TYPE = Json[Dict[str, Any]]
UNION_LIST_ITEMS_TYPE = Union[  # noqa: WPS235
    List[JobType],
    List[TakeType],
    List[HumanVolumeType],
    List[CameraSettings],
    LIST_ITEM_TYPE,
]


def validate_list_items_type(  # noqa: WPS231
    list_items: LIST_ITEM_TYPE,
) -> UNION_LIST_ITEMS_TYPE:
    """Validate list items type.

    Args:
        list_items (LIST_ITEM_TYPE): List items.

    Returns:
        List items.

    Raises:
        ValueError: If list items type is invalid.
    """
    if list_items:
        if list_items[0].get("lens"):
            return [CameraSettings(**list_item) for list_item in list_items]
        elif str(list_items[0]["id"]).startswith("job"):
            return [JobType(**list_item) for list_item in list_items]
        elif str(list_items[0]["id"]).startswith("take"):
            return [TakeType(**list_item) for list_item in list_items]
        elif str(list_items[0]["id"]).startswith("volume"):
            return [HumanVolumeType(**list_item) for list_item in list_items]
        raise ValueError("Invalid list items type.")
    # In case the validator could not decide which type is being used,
    #  pass the data to pydantic to do its inner validations.
    return list_items


ListItem = Annotated[
    Union[
        List[JobType],
        List[TakeType],
        List[HumanVolumeType],
        List[CameraSettings],
    ],
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


class ListBaseItems(BaseModel):
    """List base items schema."""

    items: ListItem = Field(  # type: ignore[assignment]  # noqa: WPS110
        default_factory=list,
        description="List of items. This can be either list of CameraSettings, JobType or TakeType.",
    )
    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class ListBase(ListBaseItems):
    """List base schema inluding limit and next_token."""

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
    model_config = ConfigDict(populate_by_name=True, extra="allow")
